#!/usr/bin/env python3
"""Lint a help center's Markdown pages against what GK-WP-HC-Plugin expects.

Shared file of the gkhc-docs-authoring skill: identical in every docs repo.
Everything product-specific comes from the product config: product/config.json
beside this skill (the docs repo's own), or a central seed with --product.
The metadata schema is scripts/schema.json, generated from FRONTMATTER-SCHEMA.md.

Checks: front matter metadata (Core and Conditional fields, types,
vocabulary), nav fields (custom_fields nesting, nav_parent resolution, depth,
order) and the plugin's other fields (page_type, card_*, entry_*,
home_group/home_order, git_hosts, anchor_map, layout), the callout standard,
copy-button blocks, scripts, internal links and images, and, where the
product has the metric pipeline (Insights), the metric-page skeleton.
Standard library only.

    python .claude/skills/gkhc-docs-authoring/scripts/check_pages.py            # every page
    python .claude/skills/gkhc-docs-authoring/scripts/check_pages.py FILE ...   # report on these pages only

  --config PATH     product config (default: ../product/config.json)
  --product KEY     in GK-WP-HC-Design: use skills/products/KEY/config.json
  --root DIR        the docs repo to check (default: the repo this skill is in)
  --nav-file PATH   the product nav file, GK-WP-HC-Plugin/config/products/<key>.json. Default: found
                    through $GKHC_DESIGN_DIR, or a GK-WP-HC-Design checkout beside the docs repo
  --summary         print only the totals

Slugs are the file names as WordPress stores them: sanitize_title() of the
file stem (lowercase). Exit status 0 when clean, 1 if any ERROR was reported
(fails CI), 2 on a usage or config problem. WARN lines are judgement calls;
INFO lines are notes.
"""
import json
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
SCHEMA_FILE = os.path.join(HERE, 'schema.json')

PAGE_TYPES = {'content', 'index', 'main-index'}
CARD_COLORS = {'purple', 'blue', 'green', 'amber', 'red'}
CUSTOM_FIELDS = {'page_type', 'nav_category', 'nav_order', 'nav_label', 'nav_parent',
                 'card_icon', 'card_color', 'card_description',
                 'nav_also',   # extra placements, NAV-CONTRACT.md
                 'layout',     # settings spec panels / release notes
                 # Generic home (NAV-CONTRACT.md, "Fields the plugin reads beyond the nav")
                 'entry_role', 'entry_title', 'entry_desc', 'entry_order', 'home_group', 'home_order',
                 'anchor_map',  # old anchor -> new location, for split pages
                 'git_hosts'}   # mirrored metadata for the home host grid
NAV_FIELDS = ('page_type', 'nav_category', 'nav_order', 'nav_label')
LAYOUTS = {'settings', 'release-notes'}
GIT_HOSTS = {'generic', 'n/a', 'github', 'github-enterprise', 'gitlab', 'gitlab-self-managed', 'bitbucket',
             'bitbucket-data-center', 'azure-devops', 'azure-devops-server', 'aws-codecommit', 'gerrit'}
# Card-set groups of the registry's default home blocks (gkhc-registry.php).
DEFAULT_HOME_GROUPS = {'cta', 'paths', 'install', 'features', 'chips', 'links'}
TOP_LEVEL_FIXED = {'title', 'description', 'taxonomy', 'custom_fields'}

# gkhc_passc_section_order() in GK-WP-HC-Plugin/includes/gkhc-passc.php (metric pipeline)
METRIC_SECTIONS = [
    ('At a glance', r'^at a glance$'),
    ('Formula', r'^(formulas?|the rubric)$'),
    ('How GitKraken Insights calculates it', r'^how .* (calculates|applies|computes) it$'),
    ('Why it matters', r'^why '),
    ('How to read it', r'^how to read it$'),
    ('Settings that affect it', r'^settings that affect it$'),
    ('How to improve/use ...', r'^how to (improve|use) '),
    ('Limitations and gotchas', r'^limitations'),
    ('FAQ', r'^faq$'),
    ('Related metrics', r'^related metrics$'),
    ('Where it appears', r'^where it appears$'),
]

# Theme-era callout markup. The plugin's callouts adapter still converts it, but
# the standard (decided 2026-11-09) is a > **Note:** / **Tip:** / **Warning:** blockquote.
HTML_CALLOUT = re.compile(r'<(?:div|figure)\s+class=(["\'])\s*(callout(?:\s+callout--[a-z]+)?|bbb-callout(?:\s+bbb--[a-z]+)?|note)\s*\1', re.I)
STYLE_SCRIPT = re.compile(r'<(style|script)\b[^>]*>.*?</\1>', re.I | re.S)

CFG = {}            # product config
SCHEMA = {}         # scripts/schema.json
NAV_EXTRA = {}      # groups and links of the product nav file, by key
HOME_GROUPS = None  # card-set groups the product's home uses (None: nav file not loaded)
problems = []


def report(level, slug, msg):
    problems.append((level, slug, msg))


# ------------------------------------------------------------------ front matter

class Scalar(str):
    """A YAML scalar: its text, and whether it was quoted."""
    quoted = False


def scalar(raw):
    raw = raw.strip()
    if raw[:1] == '"':
        m = re.match(r'"((?:[^"\\]|\\.)*)"', raw)
        out = Scalar(re.sub(r'\\(.)', r'\1', m.group(1)) if m else raw[1:])
        out.quoted = True
        return out
    if raw[:1] == "'":
        m = re.match(r"'((?:[^']|'')*)'", raw)
        out = Scalar(m.group(1).replace("''", "'") if m else raw[1:])
        out.quoted = True
        return out
    return Scalar(re.sub(r'(^|\s+)#.*$', '', raw).strip())


def flow_list(raw):
    """[a, "b, c", 'd']  # comment  ->  [Scalar, ...]"""
    items, cur, quote, i = [], '', None, 1
    while i < len(raw):
        ch = raw[i]
        if quote:
            cur += ch
            if ch == '\\' and quote == '"' and i + 1 < len(raw):
                cur += raw[i + 1]
                i += 1
            elif ch == quote:
                quote = None
        elif ch in '"\'':
            quote = ch
            cur += ch
        elif ch in ',]':
            items.append(cur)
            cur = ''
            if ch == ']':
                break
        else:
            cur += ch
        i += 1
    return [scalar(x) for x in items if x.strip()]


def value(raw):
    raw = raw.strip()
    return flow_list(raw) if raw.startswith('[') else scalar(raw)


def parse_front_matter(text):
    """Return (dict, body). Two levels of block mappings, flow and block lists,
    quoted and plain scalars, trailing comments: the YAML these pages use."""
    m = re.match(r'^﻿?---\r?\n(.*?)\r?\n---\r?\n?(.*)$', text, re.S)
    if not m:
        return None, text
    data, parent, last, top = {}, None, None, None
    for raw in m.group(1).splitlines():
        stripped = raw.strip()
        if not stripped or stripped.startswith('#'):
            continue
        indent = len(raw) - len(raw.lstrip())
        if stripped.startswith('- ') or stripped == '-':
            item = scalar(stripped[2:])
            if indent > 0 and parent is not None and last is not None and isinstance(data.get(parent), dict):
                target, key = data[parent], last
            elif top is not None:
                target, key = data, top
            else:
                continue
            if not isinstance(target.get(key), list):
                target[key] = []
            target[key].append(item)
            continue
        km = re.match(r'^\s*([A-Za-z0-9_-]+):(?:\s+(.*))?$', raw)
        if not km:
            continue
        key, val = km.group(1), (km.group(2) or '').strip()
        if indent == 0:
            last, top = None, key
            if val == '' or val.startswith('#'):
                data[key] = {}
                parent = key
            else:
                data[key] = value(val)
                parent = None
        elif parent is not None and isinstance(data.get(parent), dict):
            data[parent][key] = value(val)
            last = key
    return data, m.group(2)


def slugify(name):
    """sanitize_title(), as wp_insert_post() makes post_name from a Git It Write file name."""
    out = re.sub(r'<[^>]*>', '', name).lower()
    out = out.replace('.', '-').replace('/', '-')
    out = re.sub(r'[^a-z0-9 _-]', '', out)
    out = re.sub(r'\s+', '-', out)
    out = re.sub(r'-+', '-', out)
    return out.strip('-')


def load_pages(content):
    pages = {}
    for name in sorted(os.listdir(content)):
        if not name.endswith('.md') or name[0] in '_.' or not os.path.isfile(os.path.join(content, name)):
            continue  # Git It Write skips _ and . files
        with open(os.path.join(content, name), encoding='utf-8', errors='replace') as fh:
            text = fh.read()
        fm, body = parse_front_matter(text)
        pages[slugify(name[:-3])] = {'file': name, 'fm': fm, 'body': body}
    return pages


def cf(page):
    fields = (page.get('fm') or {}).get('custom_fields')
    return fields if isinstance(fields, dict) else {}


def s(v):
    """A field as the plugin sees it: a string (lists joined)."""
    if isinstance(v, list):
        return ', '.join(v)
    return '' if v is None or isinstance(v, dict) else str(v)


def as_list(v):
    """A list field: a YAML list, or a string holding a flow list or one value."""
    if isinstance(v, list):
        return [str(x) for x in v if str(x).strip()]
    v = s(v).strip()
    if not v:
        return []
    if v.startswith('['):
        return [m.group(1) or m.group(2) for m in re.finditer(r'"((?:[^"\\]|\\.)*)"|\'([^\']*)\'', v)]
    return [v]


def strip_code(body):
    return re.sub(r'```.*?```', '', body, flags=re.S)


def is_int(v):
    return bool(re.fullmatch(r'-?\d+', s(v).strip()))


def nav_cfg(key, default=None):
    return CFG.get('nav', {}).get(key, default)


def page_category(page):
    tax = (page.get('fm') or {}).get('taxonomy')
    return s(tax.get('category')) if isinstance(tax, dict) else ''


# ------------------------------------------------------------------ page checks

def check_front_matter(slug, page):
    """False when the page is not part of this help center (no front matter, or
    another category by decision); then nothing else is checked."""
    fm = page['fm']
    if fm is None:
        report('ERROR', slug, 'no YAML frontmatter (--- block) at the top of the file')
        return False
    cat = page_category(page)
    if slugify(cat) != slugify(CFG['category']):
        if cat and CFG.get('other_category_pages', {}).get(slug) == cat:
            return False  # publishes in another category by decision
        report('ERROR', slug, f'taxonomy.category must be {CFG["category"]}, or the post lands outside the Help Center'
               + (f' (it is "{cat}")' if cat else ''))
    prefix = nav_cfg('slug_prefix')
    if prefix and not slug.startswith(prefix):
        report('WARN', slug, f'file name does not start with {prefix}-; the slug comes from the file name')
    if not s(fm.get('title')):
        report('ERROR', slug, 'missing title')
    metadata_on = CFG['metadata'].get('check', 'off') != 'off'
    if not metadata_on and not s(fm.get('description')):
        report('WARN', slug, 'missing description (used for SEO and the page summary)')
    # Page templates (for example GL-New-Page-Template.md) carry placeholder
    # values by design and stay out of the nav, so their metadata isn't checked.
    is_template = 'template' in slug and not s((fm.get('custom_fields') or {}).get('nav_category') if isinstance(fm.get('custom_fields'), dict) else '')
    if metadata_on and is_template:
        report('WARN', slug, 'page template outside the nav: metadata not checked')
    elif metadata_on:
        check_metadata(slug, fm)
    for key in CUSTOM_FIELDS - metadata_fields():
        if key in fm:
            report('ERROR', slug, f'{key} is a top-level key; Git It Write only stores fields nested under custom_fields:')
    fields = fm.get('custom_fields')
    if not isinstance(fields, dict):
        if nav_cfg('every_page_in_nav'):
            report('ERROR', slug, 'no custom_fields: block; the page will not appear in the nav or card grids')
        return True
    for key in fields:
        if key not in CUSTOM_FIELDS:
            report('WARN', slug, f'custom_fields.{key} is not read by the plugin')
    nav_category = s(fields.get('nav_category'))
    if nav_cfg('every_page_in_nav') or nav_category:
        for key in NAV_FIELDS:
            if not s(fields.get(key)):
                report('ERROR', slug, f'custom_fields.{key} is missing or empty')
        if not nav_cfg('section_fallback') and 'nav_parent' not in fields:
            report('WARN', slug, 'custom_fields.nav_parent is missing; write nav_parent: "" for a top-level page '
                                 '(Git It Write never clears a field, so an omitted key can keep a stale value)')
    elif any(s(fields.get(k)) for k in ('nav_order', 'nav_label', 'nav_parent', 'nav_also')):
        report('ERROR', slug, 'has nav fields but no nav_category; the page is left out of the nav and search')
    ptype = s(fields.get('page_type'))
    if ptype and ptype not in PAGE_TYPES:
        report('ERROR', slug, f'page_type "{ptype}" is not one of {sorted(PAGE_TYPES)}')
    if ptype == 'main-index' and CFG.get('home_slug') and slug != slugify(CFG['home_slug']):
        report('WARN', slug, f'page_type main-index, but this help center\'s home page is {CFG["home_slug"]} (repos.json home_slug)')
    sections = nav_cfg('sections')
    if sections and nav_category and nav_category not in sections:
        report('WARN', slug, f'nav_category "{nav_category}" is new: it renders after Admin & API unless added to section_order in includes/gkhc-registry.php')
    order = s(fields.get('nav_order'))
    if order and not is_int(order):
        report('ERROR', slug, f'nav_order "{order}" must be an integer (the plugin casts it with (int))')
    for key in ('entry_order', 'home_order'):
        if s(fields.get(key)) and not is_int(fields[key]):
            report('ERROR', slug, f'{key} "{s(fields[key])}" must be an integer')
    if (s(fields.get('entry_role')) or s(fields.get('entry_desc')) or s(fields.get('entry_order'))) and not s(fields.get('entry_title')):
        report('ERROR', slug, 'entry_role/entry_desc/entry_order are set but entry_title is empty; the home only shows pages with an entry_title as entry paths')
    if s(fields.get('entry_title')) and not s(fields.get('entry_desc')):
        report('WARN', slug, 'entry_title without entry_desc; the entry path card shows no description')
    if s(fields.get('layout')) and s(fields['layout']) not in LAYOUTS:
        report('ERROR', slug, f'layout "{s(fields["layout"])}" is not one of {sorted(LAYOUTS)}; the plugin ignores it')
    # The vocabulary comes from schema.json (FRONTMATTER-SCHEMA.md), so the
    # custom_fields mirror and the top-level metadata accept the same hosts.
    # GIT_HOSTS is only the fallback when schema.json can't be read.
    host_vocab = set(((SCHEMA.get('vocabulary') or {}).get('git_hosts') or {}).get('values') or []) or GIT_HOSTS
    for host in as_list(fields.get('git_hosts')):
        if host not in host_vocab:
            report('ERROR', slug, f'git_hosts value "{host}" is not a git_hosts slug (FRONTMATTER-SCHEMA.md vocabulary)')
    check_mirror(slug, fm, fields)
    groups = [g.strip() for item in as_list(fields.get('home_group')) for g in item.split(',') if g.strip()]
    for g in groups:
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', g):
            report('ERROR', slug, f'home_group "{g}" is not a group key (lowercase letters, digits, - and _)')
        elif HOME_GROUPS is not None and g not in HOME_GROUPS:
            report('WARN', slug, f'home_group "{g}" is not used by any block of this help center\'s home '
                                 f'({", ".join(sorted(HOME_GROUPS)) or "none"}); the page shows in no home card set')
    if s(fields.get('home_order')) and not groups:
        report('WARN', slug, 'home_order without home_group has no effect')
    if nav_category != 'hidden':
        color = s(fields.get('card_color'))
        if nav_cfg('card_fields_required'):
            if color not in CARD_COLORS:
                report('ERROR', slug, f'card_color "{color}" must be one of {sorted(CARD_COLORS)}')
            if not s(fields.get('card_icon')):
                report('WARN', slug, 'card_icon is empty; the card renders with no icon (Tabler icon name without the ti- prefix)')
            elif s(fields['card_icon']).startswith('ti-'):
                report('ERROR', slug, 'card_icon must not include the ti- prefix')
            if not s(fields.get('card_description')):
                report('WARN', slug, 'card_description is empty; it is the card subtitle and part of the search index')
        else:
            if color and color not in CARD_COLORS:
                report('ERROR', slug, f'card_color "{color}" must be one of {sorted(CARD_COLORS)}')
            if s(fields.get('card_icon')).startswith('ti-'):
                report('ERROR', slug, 'card_icon must not include the ti- prefix')
    return True


def check_mirror(slug, fm, fields):
    """custom_fields.git_hosts mirrors the page's top-level host metadata (NAV-CONTRACT.md)."""
    mirror = as_list(fields.get('git_hosts'))
    if not mirror:
        return
    alias = CFG['metadata'].get('aliases', {}).get('git_hosts')
    top = as_list(fm.get('git_hosts')) or (as_list(fm.get(alias)) if alias else [])
    if top and {norm_host(h) for h in top} != set(mirror):
        report('WARN', slug, f'custom_fields.git_hosts {mirror} does not mirror the top-level value {top}')


# ------------------------------------------------------------------ metadata

def metadata_fields():
    return set(SCHEMA.get('core', {})) | set(SCHEMA.get('conditional', {}))


def norm_host(h):
    """Desktop keeps display names ("GitLab Self-Managed"); compare in slug form."""
    return re.sub(r'\s+', '-', h.strip().lower())


def check_metadata(slug, fm):
    """FRONTMATTER-SCHEMA.md: Core fields on every page, the product's Conditional fields, types, vocabulary."""
    md = CFG['metadata']
    level = 'ERROR' if md.get('check') == 'error' else 'WARN'
    aliases = md.get('aliases', {})
    for name in list(SCHEMA['core']) + list(md.get('conditional', [])):
        if name not in fm and aliases.get(name) not in fm:
            kind = 'Core' if name in SCHEMA['core'] else 'Conditional'
            report(level, slug, f'metadata: {name} is missing (FRONTMATTER-SCHEMA.md {kind} field)')
    specs = dict(SCHEMA['conditional'], **SCHEMA['core'])
    for name, spec in specs.items():
        if name in fm:
            check_value(slug, name, fm[name], spec, level)
    for name, want in md.get('constants', {}).items():
        have = s(fm.get(name))
        if name in fm and have != want:
            if name == 'product':
                report('WARN', slug, f'metadata: product is "{have}", not "{want}"; fine only for a page really about that product')
            else:
                report(level, slug, f'metadata: {name} must be "{want}" in this help center (it is "{have}")')
    known = TOP_LEVEL_FIXED | metadata_fields() | set(md.get('extra_fields', [])) | set(aliases.values()) | CUSTOM_FIELDS
    for name in fm:
        if name not in known:
            report('WARN', slug, f'metadata: top-level key {name} is not in FRONTMATTER-SCHEMA.md')


def check_value(slug, name, v, spec, level):
    kind = spec['type']
    if (isinstance(v, list) and not v) or (not isinstance(v, list) and not s(v).strip()):
        if not spec.get('allow_empty'):
            report(level, slug, f'metadata: {name} is empty')
        return
    vocab = SCHEMA['vocabulary'].get(spec.get('vocabulary') or '')
    if kind == 'bool':
        if isinstance(v, list) or getattr(v, 'quoted', False) or s(v) not in ('true', 'false'):
            report(level, slug, f'metadata: {name} must be true or false, unquoted (it is {s(v)!r})')
    elif kind == 'month':
        if isinstance(v, list) or not re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])', s(v)):
            report(level, slug, f'metadata: {name} must be YYYY-MM (it is "{s(v)}")')
    elif kind in ('string', 'enum'):
        if isinstance(v, list):
            report(level, slug, f'metadata: {name} must be a single value, not a list')
        elif kind == 'enum' and vocab and s(v) not in vocab['values']:
            report(level, slug, f'metadata: {name} "{s(v)}" is not in the vocabulary ({", ".join(vocab["values"])})')
    elif kind == 'list':
        if isinstance(v, list):
            items = [str(x) for x in v]
        elif spec.get('comma_string_ok'):
            items = [x.strip() for x in s(v).split(',') if x.strip()]
        else:
            report(level, slug, f'metadata: {name} must be a list ([a, b]), not "{s(v)}"')
            return
        if name == 'plan_required':
            allowed = CFG['metadata'].get('plan_required') or []
            bad = [x for x in items if allowed and x not in allowed]
            if bad:
                plan_level = 'WARN' if CFG['metadata'].get('plan_required_vocabulary', 'error') == 'warn' else level
                report(plan_level, slug, f'metadata: plan_required value(s) {bad} are not plans of this help center ({", ".join(allowed)})')
        elif vocab:
            bad = [x for x in items if (norm_host(x) if name == 'git_hosts' else x) not in vocab['values']]
            if bad and vocab.get('open'):
                report('WARN', slug, f'metadata: {name} value(s) {bad} are not in the vocabulary yet; '
                                     f'add new values to FRONTMATTER-SCHEMA.md in slug form')
            elif bad:
                report(level, slug, f'metadata: {name} value(s) {bad} are not in the vocabulary')


# ------------------------------------------------------------------ hierarchy

def parent_key(value):
    """nav_parent as the plugin reads it: a bare key, matched exactly; a leading group: is tolerated."""
    value = s(value).strip()
    return value[6:] if value.startswith('group:') else value


def section_index(pages, cat, exclude=None):
    return [x for x, p in pages.items() if x != exclude and s(cf(p).get('nav_category')) == cat
            and s(cf(p).get('page_type')) == 'index' and not s(cf(p).get('nav_parent'))]


def nav_depth(slug, pages):
    """The nav level a page renders at, as the plugin builds it: 1 at the top;
    one more per nav_parent step (pages, or groups/links of the nav file); with
    the section fallback (Insights), an un-parented page hangs under its
    section's un-parented index page."""
    depth, cur, seen = 0, slug, set()
    while cur and cur not in seen:
        seen.add(cur)
        depth += 1
        if cur in pages:
            f = cf(pages[cur])
            nxt = parent_key(f.get('nav_parent'))
            if not nxt and nav_cfg('section_fallback') and s(f.get('page_type')) not in ('index', 'main-index'):
                idx = section_index(pages, s(f.get('nav_category')), exclude=cur)
                nxt = idx[0] if idx else ''
            cur = nxt if (nxt in pages or nxt in NAV_EXTRA) else ''
        else:
            cur = parent_key(NAV_EXTRA[cur].get('parent', ''))
    return depth


def top_ancestor(slug, pages):
    """The key of the top-level item a page sits under (NAV-CONTRACT.md: its nav_category)."""
    cur, seen = slug, set()
    while cur not in seen:
        seen.add(cur)
        if cur in pages:
            parent = parent_key(cf(pages[cur]).get('nav_parent'))
        else:
            parent = parent_key(NAV_EXTRA.get(cur, {}).get('parent', ''))
        if not parent:
            return cur
        if parent not in pages and parent not in NAV_EXTRA:
            return None
        cur = parent
    return None


def unknown_key(slug, field, key, pages, nav_file_known):
    """Report a nav_parent / nav_also key that names no page, group or link."""
    if slugify(key) in pages:
        report('ERROR', slug, f'{field} "{key}" does not match the slug "{slugify(key)}" exactly; WordPress lowercases '
                              f'slugs and the plugin matches the key as written, so the page drops out of the nav')
    elif nav_file_known:
        report('ERROR', slug, f'{field} "{key}" is not a page slug (file name without .md, lowercase)'
               + (' or a group/link key of the nav file' if CFG.get('nav_file') else '') + '; the page drops out of the nav')
    else:
        report('WARN', slug, f'{field} "{key}" is not a page slug; it may be a group or link of '
                             f'config/products/{CFG["nav_file"]}.json, which was not found (pass --nav-file)')


def check_hierarchy(pages):
    nav_file_known = HOME_GROUPS is not None or not CFG.get('nav_file')
    siblings = defaultdict(list)
    for slug, page in pages.items():
        fields = cf(page)
        if not fields or not page.get('in_help_center'):
            continue
        parent = parent_key(fields.get('nav_parent'))
        ptype = s(fields.get('page_type'))
        cat = s(fields.get('nav_category'))
        if not cat and not nav_cfg('every_page_in_nav'):
            continue  # not in the nav
        if parent:
            if parent not in pages and parent not in NAV_EXTRA:
                unknown_key(slug, 'nav_parent', parent, pages, nav_file_known)
            elif parent in pages and nav_cfg('parent_must_be_index'):
                pf = cf(pages[parent])
                if s(pf.get('page_type')) != 'index':
                    report('ERROR', slug, f'nav_parent "{parent}" is not an index page')
                if s(pf.get('nav_category')) != cat:
                    report('ERROR', slug, f'nav_category "{cat}" differs from its parent\'s "{s(pf.get("nav_category"))}"')
            seen, cur = {slug}, parent
            while cur and cur in pages:
                if cur in seen:
                    report('ERROR', slug, 'nav_parent chain loops back on itself')
                    break
                seen.add(cur)
                cur = parent_key(cf(pages[cur]).get('nav_parent'))
        if cat and cat != 'hidden':
            depth = nav_depth(slug, pages)
            max_depth = CFG.get('max_depth', 5)
            if depth > max_depth:
                report('ERROR', slug, f'sits {depth} levels deep; the nav renders {max_depth} levels and shows deeper pages at level {max_depth}')
            if not nav_cfg('sections') and nav_file_known:
                top = top_ancestor(slug, pages)
                if top and cat != top:
                    report('WARN', slug, f'nav_category "{cat}" is not the key of its top-level ancestor "{top}" (NAV-CONTRACT.md)')
        for also in as_list(fields.get('nav_also')):
            parts = also.split('|', 2)
            if len(parts) != 3 or not re.fullmatch(r'-?\d+', parts[1].strip()):
                report('ERROR', slug, f'nav_also entry "{also}" is not "<parent>|<order>|<label>"')
            elif parent_key(parts[0]) and parent_key(parts[0]) not in pages and parent_key(parts[0]) not in NAV_EXTRA:
                unknown_key(slug, 'nav_also parent', parent_key(parts[0]), pages, nav_file_known)
        check_anchor_map(slug, page, pages)
        if ptype == 'main-index' or cat == 'hidden':
            continue
        if nav_cfg('section_fallback'):
            key = parent or ('section-index' if ptype == 'index' else f'section:{cat}')
            if key == f'section:{cat}':
                idx = section_index(pages, cat)
                if idx:
                    key = idx[0]
        else:
            key = parent or '(top level)'
        siblings[key].append((s(fields.get('nav_order')), slug))
    mains = [x for x, p in pages.items() if p.get('in_help_center') and s(cf(p).get('page_type')) == 'main-index']
    if len(mains) != 1:
        report('ERROR', '(site)', f'expected exactly one main-index page, found {len(mains)}: {mains}')
    if nav_cfg('section_fallback'):
        for cat in {s(cf(p).get('nav_category')) for p in pages.values()} - {'home', 'hidden', ''}:
            idx = section_index(pages, cat)
            if len(idx) != 1:
                report('ERROR', '(site)', f'nav_category "{cat}" needs exactly one un-parented index page, found {len(idx)}: {idx}')
    for key, items in siblings.items():
        by_order = defaultdict(list)
        for order, slug in items:
            by_order[order].append(slug)
        for order, slugs in by_order.items():
            if len(slugs) > 1:
                for x in slugs:
                    report('WARN', x, f'shares nav_order {order} with {[y for y in slugs if y != x]} under the same parent; order between them is not defined')


def heading_anchors(body):
    """Ids a page's headings get on the site: sanitize_title() of the heading
    (Add Anchor Links plugin), approximated from the Markdown."""
    out = set()
    for m in re.finditer(r'^#{2,6}\s+(.+?)\s*#*\s*$', strip_code(body), re.M):
        text = re.sub(r'`|\*|_|\[|\]\([^)]*\)', '', m.group(1)).strip().lower()
        out.add(re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', text)))
    return out


def check_anchor_map(slug, page, pages):
    """anchor_map: ["<old anchor>|<target>", ...]; target = <slug>[#anchor], #anchor, /path or https://..."""
    seen = set()
    own = heading_anchors(page['body'])
    for e in as_list(cf(page).get('anchor_map')):
        parts = e.split('|', 1)
        old = parts[0].strip().lstrip('#')
        target = parts[1].strip() if len(parts) == 2 else ''
        if not old or not target:
            report('ERROR', slug, f'anchor_map entry "{e}" is not "<old anchor>|<target>"')
            continue
        if old in seen:
            report('WARN', slug, f'anchor_map lists "{old}" more than once; the first entry wins')
        seen.add(old)
        if old in own:
            report('WARN', slug, f'anchor_map "{old}": this page still has a heading with that anchor, so the redirect never fires')
        if target.startswith('#') or target.startswith('/') or re.match(r'https?://', target):
            continue
        tslug = target.split('#', 1)[0].strip('/').lower()  # gkhc-anchors.php lowercases the target
        if tslug not in pages:
            report('ERROR', slug, f'anchor_map "{old}" points at "{tslug}", which is not a page slug of this help center; the plugin skips it')


# ------------------------------------------------------------------ body

def check_body(slug, page, pages, images, archived):
    fields = cf(page)
    body = page['body']
    ptype = s(fields.get('page_type')) or 'content'
    cat = s(fields.get('nav_category'))
    prose = strip_code(body)

    if (ptype in ('index', 'main-index') and re.search(r'^##\s', prose, re.M)
            and not re.search(r'^(---|\*\*\*|___)\s*$', prose, re.M)):
        report('WARN', slug, 'index page has sections but no --- rule; the card grid renders after all of them instead of after the intro')

    if CFG.get('features', {}).get('metric_pipeline') and cat == 'metrics' and ptype == 'content':
        check_metric(slug, prose, pages, fields)

    if re.search(r'^#\s', prose, re.M):
        report('WARN', slug, 'contains an H1 (#); the template already prints the page title as the H1')

    kinds, in_cells, known = defaultdict(int), defaultdict(int), defaultdict(int)
    allowed = CFG.get('known_html_callouts', {}).get(slug, [])
    for m in HTML_CALLOUT.finditer(prose):
        kind = re.sub(r'\s+', '.', m.group(2).strip().lower())
        if in_table_cell(prose, m.start()):
            in_cells[kind] += 1
        elif callout_fingerprint(prose, m.end()) in allowed:
            known[kind] += 1
        else:
            kinds[kind] += 1
    if known:
        what = ', '.join(f'{n}x {k}' for k, n in sorted(known.items()))
        report('WARN', slug, f'HTML callout markup ({what}); known: left as HTML by decision 2026-11-11')
    if kinds:
        what = ', '.join(f'{n}x {k}' for k, n in sorted(kinds.items()))
        report('ERROR', slug, f'HTML callout markup ({what}); write a > **Note:** / > **Tip:** / > **Warning:** blockquote instead (callout standard, 2026-11-09)')
    if in_cells:
        what = ', '.join(f'{n}x {k}' for k, n in sorted(in_cells.items()))
        report('WARN', slug, f'HTML callout markup in a table cell ({what}); allowed: callout in a table cell; the adapter renders it')

    copy_blocks = [m for m in STYLE_SCRIPT.finditer(body) if 'copy-btn' in m.group(0).lower()]
    if copy_blocks:
        report('WARN', slug, f'{len(copy_blocks)} copy-button <style>/<script> block(s); the plugin strips them and its code panels have a Copy button. '
                             f'Remove them from the Markdown (decided 2026-11-09)')
    scripts = len(re.findall(r'<script\b', body, re.I))
    if scripts > sum(1 for m in copy_blocks if m.group(1).lower() == 'script'):
        report('ERROR', slug, 'contains <script>; scripts in content are not supported')

    category = slugify(CFG['category'])
    checks = CFG.get('checks', {})
    ignore = set(checks.get('ignore_link_targets', []))
    level = 'ERROR' if checks.get('missing_link_target', 'error') == 'error' else 'WARN'
    rx = r'(?<![\w.:/-])(?:https?://help\.gitkraken\.com)?/%s/([A-Za-z0-9_.-]+)/?(#[^)\s"]*)?' % re.escape(category)
    for m in re.finditer(rx, prose, re.I):
        target = slugify(m.group(1))
        if target in ignore or target in pages:
            continue
        why = 'an archived page (_archive/)' if target in archived else 'not a page in ' + CFG['content_dir'] + '/'
        report(level, slug, f'links to /{category}/{target}, which is {why}')
    # Images: missing from the images folder is an ERROR, except a known, pre-existing
    # reference that still serves from WordPress uploads, on the page it is listed for
    # (product config known_wp_images, made by GK-WP-HC-Design skills/known_images.py;
    # decided 2026-11-10). A known image used on another page is not covered.
    known = CFG.get('known_wp_images', {})
    images_dir = CFG.get('images_dir') or '_images'
    for m in re.finditer(r'(?<![\w.])/wp-content/uploads/([^\s"\')]+)', prose):
        if m.group(1) in images:
            continue
        if slug in known.get(m.group(0), []):
            report('WARN', slug, f'image {m.group(1)} is not in {images_dir}/ (known: lives in WordPress uploads)')
        else:
            report('WARN' if checks.get('missing_image', 'error') == 'warn' else 'ERROR', slug,
                   f'image {m.group(1)} is not in {images_dir}/')
    if checks.get('figures_only'):
        for m in re.finditer(r'!\[[^\]]*\]\((/[^)]+)\)', prose):
            report('WARN', slug, f'Markdown image ![...]({m.group(1)}); the site uses <figure><img class="help-center-img ..."> with a <figcaption>')


def callout_fingerprint(text, end):
    """The first 60 characters of a callout's text (tags stripped, whitespace
    collapsed): how known_html_callouts in the product config names it."""
    rest = re.sub(r'<[^>]*>', ' ', text[end:end + 3000])
    return re.sub(r'\s+', ' ', rest).strip()[:60]


def in_table_cell(text, pos):
    """True when pos sits inside an HTML <td>/<th>, or on a Markdown table row
    (a line starting with |). Callouts there are allowed (decided 2026-11-10):
    a blockquote can't go in a table cell, and the callouts adapter renders them."""
    before = text[:pos]
    # The nearest cell tag before pos is an opening one (tolerates stray extra </td>).
    opens = [m.start() for m in re.finditer(r'<t[dh]\b', before, re.I)]
    closes = [m.start() for m in re.finditer(r'</t[dh]\s*>|</t(?:r|able)\s*>', before, re.I)]
    if opens and (not closes or opens[-1] > closes[-1]):
        return True
    line = before[before.rfind('\n') + 1:]
    return line.lstrip().startswith('|')


def check_metric(slug, prose, pages, fields):
    parent = s(fields.get('nav_parent'))
    if not parent or s(cf(pages.get(parent, {'fm': {}})).get('page_type')) != 'index':
        report('ERROR', slug, 'metric page needs nav_parent set to its family sub-index (e.g. expo-ai-adoption-dora-metrics), or it is missing from the Home metric map')
    lines = prose.splitlines()
    first_h3 = next((i for i, l in enumerate(lines) if l.startswith('### ')), len(lines))
    head = '\n'.join(lines[:first_h3])
    bq = re.search(r'^>\s*(.+)$', head, re.M)
    if not bq:
        report('WARN', slug, 'no > _definition_ blockquote before the first H3; the definition lede will be missing')
    elif len(re.sub(r'[_*>]', '', bq.group(1)).strip()) >= 400:
        report('WARN', slug, 'definition blockquote is 400+ characters; the plugin will not lift it as the lede')
    if not re.search(r'^\*\*Family:\*\*', head, re.M):
        report('WARN', slug, 'no **Family:** ... line before the first H3; the spec panel will be missing')
    h3s = [l[4:].strip() for l in lines if l.startswith('### ')]
    for label, rx in METRIC_SECTIONS:
        if not any(re.search(rx, h, re.I) for h in h3s):
            report('WARN', slug, f'no "{label}" H3 (canonical metric section)')
    for h in h3s:
        if not any(re.search(rx, h, re.I) for _, rx in METRIC_SECTIONS):
            report('INFO', slug, f'H3 "{h}" is not a canonical section; it travels with the section before it')


# ------------------------------------------------------------------ setup

def find_nav_file(explicit, root):
    if explicit:
        return explicit
    key = CFG.get('nav_file')
    if not key:
        return None
    rel = os.path.join('GK-WP-HC-Plugin', 'config', 'products', key + '.json')
    candidates = [os.path.join(os.environ['GKHC_DESIGN_DIR'], rel)] if os.environ.get('GKHC_DESIGN_DIR') else []
    candidates.append(os.path.join(SKILL, '..', '..', '..', rel))  # the skill's own copy in GK-WP-HC-Design
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(root)), 'GK-WP-HC-Design', rel))
    return next((os.path.abspath(c) for c in candidates if os.path.isfile(c)), None)


def load_nav_file(path):
    """Groups and links of a product nav file (NAV-CONTRACT.md), by key, and the home's card-set groups."""
    global HOME_GROUPS
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    for item in data.get('groups', []) + data.get('links', []):
        NAV_EXTRA[item['key']] = item
    if 'home_blocks' in data:
        HOME_GROUPS = {b['group'] for b in data['home_blocks'] if isinstance(b, dict) and b.get('group')}
    else:
        HOME_GROUPS = set(DEFAULT_HOME_GROUPS)


def parse_args(argv):
    opts = {'config': None, 'product': None, 'root': None, 'nav_file': None, 'summary': False}
    files, i = [], 0
    while i < len(argv):
        a = argv[i]
        if a in ('--config', '--product', '--root', '--nav-file'):
            if i + 1 >= len(argv):
                print(f'{a} needs a value')
                sys.exit(2)
            opts[a[2:].replace('-', '_')] = argv[i + 1]
            i += 2
            continue
        if a == '--summary':
            opts['summary'] = True
        elif a in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        elif a.startswith('--'):
            print(f'unknown option {a}')
            sys.exit(2)
        else:
            files.append(a)
        i += 1
    return opts, files


def main(argv):
    global CFG, SCHEMA
    opts, files = parse_args(argv)
    if opts['config']:
        config = opts['config']
    elif opts['product']:
        config = os.path.abspath(os.path.join(SKILL, '..', '..', '..', 'skills', 'products', opts['product'], 'config.json'))
    else:
        config = os.path.join(SKILL, 'product', 'config.json')
    if not os.path.isfile(config):
        print(f'No product config at {config}. In a docs repo it is .claude/skills/gkhc-docs-authoring/product/config.json; '
              'in GK-WP-HC-Design pass --product <key> (skills/products/<key>/) and --root <docs repo>.')
        return 2
    with open(config, encoding='utf-8') as fh:
        CFG = json.load(fh)
    CFG.setdefault('metadata', {'check': 'off'})
    with open(SCHEMA_FILE, encoding='utf-8') as fh:
        SCHEMA = json.load(fh)
    root = os.path.abspath(opts['root'] or os.path.join(SKILL, '..', '..', '..'))
    content = os.path.join(root, CFG['content_dir'])
    if not os.path.isdir(content):
        print(f'No content folder {content} (content_dir of {config}); pass --root <docs repo>')
        return 2
    nav_file = find_nav_file(opts['nav_file'], root)
    if nav_file:
        load_nav_file(nav_file)
    images_dir = os.path.join(root, CFG.get('images_dir') or '_images')
    images = set(os.listdir(images_dir)) if os.path.isdir(images_dir) else set()
    archived = set()
    for _, _, names in os.walk(os.path.join(root, '_archive')):
        archived |= {slugify(re.sub(r'^ARCHIVED-', '', n[:-3])) for n in names if n.endswith('.md')}

    pages = load_pages(content)
    if not pages:
        print(f'No pages found in {content}')
        return 2
    only = None
    if files:
        only = {slugify(os.path.splitext(os.path.basename(a))[0]) for a in files}
        for u in sorted(only - set(pages)):
            report('ERROR', u, f'not found in {CFG["content_dir"]}/ (or its name starts with _ and Git It Write skips it)')
    for slug, page in pages.items():
        page['in_help_center'] = check_front_matter(slug, page)
        if page['in_help_center']:
            check_body(slug, page, pages, images, archived)
    check_hierarchy(pages)

    shown = [p for p in problems if only is None or p[1] in only or p[1] == '(site)']
    order = {'ERROR': 0, 'WARN': 1, 'INFO': 2}
    if not opts['summary']:
        for level, slug, msg in sorted(shown, key=lambda p: (order[p[0]], p[1])):
            print(f'{level:5} {slug}: {msg}')
    errors = sum(1 for p in shown if p[0] == 'ERROR')
    warns = sum(1 for p in shown if p[0] == 'WARN')
    scope = f'{len(only)} page(s)' if only else f'{len(pages)} pages'
    note = '' if nav_file or not CFG.get('nav_file') else \
        f' Nav file config/products/{CFG["nav_file"]}.json not found: nav_parent keys naming groups or links were not verified.'
    print(f'\n{scope} checked: {errors} error(s), {warns} warning(s).{note}')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
