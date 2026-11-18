#!/usr/bin/env python3
"""The help center prose and image rules, for any docs repo, with or without gk-docs-automation.

Shared file of the gkhc-docs-authoring skill. A port of gk-docs-automation's
`gkdocs lint` (src/lint/rules.ts): the same rule IDs (WRITING-STANDARDS.md
§2.11), the same severities, the same patterns. Both implementations pass the
same cases, `../standards/conformance.json`, synced from gk-docs-automation with
the rest of `../standards/` by GK-WP-HC-Design `skills/standards_sync.py`.
Change a rule in gk-docs-automation first (rules.ts, conformance.json and the
standard), then port it here and re-run the sync; `standards_sync.py check`
fails while this port does not pass the synced cases.

check_pages.py runs these rules on the pages you name, or on the pages your
branch changed. Run them alone with:

    python .claude/skills/gkhc-docs-authoring/scripts/prose_rules.py FILE ... [--product ID]
    python .claude/skills/gkhc-docs-authoring/scripts/prose_rules.py --test     # the conformance cases

--product is a gk-docs-automation product id (`../standards/products.json`):
it selects the internal terms (H-90) and internal-only syntax (H-96) to check.
Exit 1 if any ERROR was found. Standard library only.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STANDARDS = os.path.join(os.path.dirname(HERE), 'standards')

# ------------------------------------------------------------------ helpers

_ABBREV_SPLIT = re.compile(r'\b(e\.g|i\.e|etc|vs|Mr|Ms|Dr|Fig|approx|Inc|Ltd)\.', re.I)
_SENT_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z"\'`(\[])')


def split_sentences(text):
    t = _ABBREV_SPLIT.sub(lambda m: m.group(1) + '<DOT>', text)
    return [s for s in (p.replace('<DOT>', '.').strip() for p in _SENT_SPLIT.split(t)) if s]


def _blank(m):
    return re.sub(r'[^\n]', ' ', m.group(0))


def _spaces(m):
    return ' ' * len(m.group(0))


def mask_non_prose(body):
    body = re.sub(r'^```[\s\S]*?^```', _blank, body, flags=re.M)
    body = re.sub(r'`[^`\n]*`', _spaces, body)
    body = re.sub(r'<[^>]+>', _spaces, body)
    return re.sub(r'\]\([^)]*\)', _spaces, body)


def mask_ui_text(masked):
    masked = re.sub(r'\*\*[^*\n]+\*\*', _spaces, masked)
    masked = re.sub(r'(?<![*\w])\*[^*\n]+\*(?!\*)', _spaces, masked)
    return re.sub(r'(?<!\w)_[^_\n]+_(?!\w)', _spaces, masked)


def line_of(text, index):
    return text.count('\n', 0, index) + 1


ABBREV = re.compile(r'\b(e\.g|i\.e|etc|vs|Mr|Ms|Dr|Fig|approx|Inc|Ltd|No)\.', re.I)
ONE_DOT = '․'


def _shield_abbrev(text):
    return ABBREV.sub(lambda m: m.group(0).replace('.', ONE_DOT, 1), text)


# ------------------------------------------------------------------ page parsing (gray-matter + scan.ts)

IMG_TAG = re.compile(r'<img\b(?:[^>"\']|"[^"]*"|\'[^\']*\')*>', re.I | re.S)
MD_IMG = re.compile(r'!\[((?:[^\]\\]|\\.)*)\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+"[^"]*")?\s*\)')
SRC_ATTR = re.compile(r'\bsrc\s*=\s*["\']([^"\']*?)["\']', re.I)
ALT_ATTR = re.compile(r'\balt\s*=\s*["\']([^"\']*)["\']', re.I)
UPLOADS = '/wp-content/uploads/'


def _basename_of(url):
    i = url.find(UPLOADS)
    if i == -1:
        return None
    clean = re.split(r'[?#]', url[i + len(UPLOADS):])[0]
    name = clean.split('/')[-1]
    return name or None


def scan_images(text):
    """Every wp-content image reference, both syntaxes: dicts with basename, line, alt (None = no attribute)."""
    refs = []
    for m in IMG_TAG.finditer(text):
        src = SRC_ATTR.search(m.group(0))
        base = _basename_of(src.group(1)) if src else None
        if not base:
            continue
        alt = ALT_ATTR.search(m.group(0))
        refs.append({'basename': base, 'line': line_of(text, m.start()), 'alt': alt.group(1) if alt else None})
    for m in MD_IMG.finditer(text):
        base = _basename_of(re.sub(r'^<|>$', '', m.group(2)))
        if not base:
            continue
        refs.append({'basename': base, 'line': line_of(text, m.start()), 'alt': m.group(1)})
    return sorted(refs, key=lambda r: r['line'])


def split_page(raw):
    """(body, line offset) the way gray-matter splits a page: the body after the closing --- line."""
    lines = raw.split('\n')
    if lines and lines[0].rstrip('\r').rstrip() == '---':
        for j in range(1, len(lines)):
            if lines[j].rstrip('\r').rstrip() == '---':
                return '\n'.join(lines[j + 1:]), j + 1
    return raw, 0


class Ctx:
    def __init__(self, raw, internal_terms=None, internal_patterns=None):
        self.body, self.offset = split_page(raw)
        self.lines = re.split(r'\r?\n', raw)
        self.images = scan_images(raw)
        self.internal_terms = internal_terms or []
        self.internal_patterns = internal_patterns or []


# ------------------------------------------------------------------ rules

RULES = []  # (id, severity, description, check)


def rule(rid, severity, description):
    def deco(fn):
        RULES.append((rid, severity, description, fn))
        return fn
    return deco


def F(rid, line, message, hint=None):
    return {'rule': rid, 'line': line, 'message': message, 'hint': hint}


@rule('H-62', 'error', 'Every image has an alt attribute')
def alt_present(c):
    return [F('H-62', i['line'], f"No alt attribute on {i['basename']}",
              'Screen readers announce the filename instead. Use alt="" only if decorative.')
            for i in c.images if i['alt'] is None]


@rule('H-63', 'error', 'Alt text is at most two sentences')
def alt_length(c):
    return [F('H-63', i['line'], f"Alt text on {i['basename']} runs {len(split_sentences(i['alt']))} sentences",
              'Summarize the purpose; move detail into body prose.')
            for i in c.images if i['alt'] and len(split_sentences(i['alt'])) > 2]


@rule('H-64', 'warn', 'Alt text does not begin with "image of", "screenshot of", etc.')
def alt_prefix(c):
    p = re.compile(r'^\s*(an?\s+)?(image|photo|picture|screenshot|graphic|icon|illustration|diagram)\s+(of|showing)\b', re.I)
    return [F('H-64', i['line'], f"Alt text on {i['basename']} opens with a redundant prefix",
              'Screen readers already announce it as an image. Describe the content directly.')
            for i in c.images if i['alt'] and p.search(i['alt'])]


@rule('H-62a', 'error', 'Alt text is not a filename')
def alt_filename(c):
    out = []
    for i in c.images:
        if not i['alt']:
            continue
        a = i['alt'].strip().lower()
        if a == i['basename'].lower() or re.search(r'\.(png|jpe?g|gif|svg|webp)$', a, re.I):
            out.append(F('H-62a', i['line'], f"Alt text on {i['basename']} is a filename"))
    return out


VAGUE_LINKS = {'click here', 'here', 'read more', 'learn more', 'more', 'this', 'this document', 'this page',
               'this article', 'link', 'website', 'article'}


@rule('H-55', 'warn', 'Link text is descriptive out of context')
def link_text(c):
    out = []
    for pat, hint in ((r'\[([^\]]+)\]\([^)]+\)', 'Describe the destination, e.g. "the Commit Graph settings".'),
                      (r'<a\b[^>]*>([^<]+)</a>', None)):
        for m in re.finditer(pat, c.body, re.I if pat.startswith('<') else 0):
            text = re.sub(r'[.!?,:;]+$', '', m.group(1).strip().lower())
            if text in VAGUE_LINKS:
                out.append(F('H-55', line_of(c.body, m.start()) + c.offset, f'Link text "{m.group(1).strip()}" is not descriptive', hint))
    return out


@rule('H-52a', 'error', 'Page body contains no level-1 heading (title lives in frontmatter)')
def no_h1(c):
    masked = mask_non_prose(c.body)
    return [F('H-52a', line_of(masked, m.start()) + c.offset, 'Level-1 heading in body; the platform renders frontmatter title as h1')
            for m in re.finditer(r'^#\s+\S', masked, re.M)]


@rule('H-53', 'warn', 'Heading levels increase by one')
def heading_order(c):
    out, prev = [], 0
    masked = mask_non_prose(c.body)
    for m in re.finditer(r'^(#{1,6})\s+(\S.*)$', masked, re.M):
        level = len(m.group(1))
        if prev > 0 and level > prev + 1:
            out.append(F('H-53', line_of(masked, m.start()) + c.offset, f'Heading jumps from h{prev} to h{level}'))
        prev = level
    return out


@rule('H-54', 'warn', 'A level-2 heading has content before its first level-3')
def empty_h2(c):
    out = []
    lines = mask_non_prose(c.body).split('\n')
    for i, line in enumerate(lines):
        if not re.match(r'^##\s+\S', line):
            continue
        for j in range(i + 1, len(lines)):
            l = lines[j].strip()
            if l == '':
                continue
            if re.match(r'^###\s+\S', l):
                out.append(F('H-54', i + 1 + c.offset, 'Level-3 heading immediately follows a level-2 with no prose between'))
            break
    return out


@rule('H-49', 'warn', 'Paragraphs are at most seven sentences')
def paragraph_length(c):
    out, offset = [], 0
    masked = mask_non_prose(c.body)
    for para in re.split(r'\n\s*\n', masked):
        t = para.strip()
        if t and not re.match(r'^[#>\-*|\d]', t):
            n = len(split_sentences(t))
            if n > 7:
                out.append(F('H-49', line_of(masked, offset) + c.offset, f'Paragraph runs {n} sentences',
                             'Split it, or convert to a list if it is enumerating.'))
        offset += len(para) + 2
    return out


@rule('H-48', 'warn', 'Table cells hold at most two sentences')
def table_cells(c):
    out = []
    for i, line in enumerate(c.lines):
        if not line.strip().startswith('|') or re.match(r'^\s*\|[\s:|-]+\|\s*$', line):
            continue
        for cell in line.split('|')[1:-1]:
            if len(split_sentences(cell.strip())) > 2:
                out.append(F('H-48', i + 1, 'Table cell holds more than two sentences'))
                break
    return out


@rule('H-36', 'warn', 'No en dashes')
def en_dash(c):
    masked = mask_non_prose(c.body)
    return [F('H-36', line_of(masked, m.start()) + c.offset, 'En dash (–) found', 'Use an em dash (—) or rewrite.')
            for m in re.finditer('–', masked)]


@rule('H-15', 'warn', 'No direction-only or color-only references to UI')
def directional(c):
    masked = mask_non_prose(c.body)
    p = (r'\b(?:the\s+)?(?:button|link|icon|panel|menu|tab|field|box)\s+(?:on|to|at)\s+the\s+(?:left|right|top|bottom)\b'
         r'|\bthe\s+(?:red|green|blue|purple|yellow|orange|highlighted|circled)\s+(?:button|icon|box|circle|area|section|oval|ring)\b')
    return [F('H-15', line_of(masked, m.start()) + c.offset, f'Position- or color-only reference: "{m.group(0).strip()}"',
              'Name the control, e.g. "Click **Start Review**".')
            for m in re.finditer(p, masked, re.I)]


INTRO = re.compile(
    r'^(?:if|when|whenever|after|before|once|while|although|though|because|since|unless|until|as|where|wherever|whether|'
    r'to|in|on|for|by|with|without|from|at|during|under|over|within|through|across|via|per|like|unlike|besides|then|next|'
    r'now|also|otherwise|finally|first|second|third|here|there|however|instead|meanwhile|later|again|afterwards|similarly|'
    r'likewise|optionally|alternatively|today|currently|yes|no|e\.g\.|i\.e\.|for example|for instance|by default|in addition)\b',
    re.I)
CLAUSE_WORD = re.compile(
    r'^(?:either|neither|both|with|without|then|so|but|which|that|where|who|whose|while|because|and|or|nor|yet|if|when|'
    r'unless|until|since|as|after|before|once|although|though)\b', re.I)
ITEM = r"[A-Za-z0-9][\w'’/.+#-]*(?: [A-Za-z0-9][\w'’/.+#-]*){0,2}"
SERIES = re.compile(r"(?<![\w'’/.+#-])(" + ITEM + r"), (" + ITEM + r") (and|or) (?=[A-Za-z0-9])")


@rule('H-30', 'warn', 'Series of three or more use the serial comma')
def serial_comma(c):
    out = []
    text = _shield_abbrev(mask_non_prose(c.body))
    text = re.sub(r'\*\*|__|(?<![\w*])[*_](?=\S)|(?<=\S)[*_](?![\w*])', '', text)
    text = re.sub(r'[ \t]+,', ',', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    for i, line in enumerate(text.split('\n')):
        if re.match(r'^\s*(#|\|)', line):
            continue
        for m in SERIES.finditer(line):
            before = line[:m.start()]
            start = max(before.rfind(','), before.rfind('('))
            for s in re.finditer(r'[.!?:;](?=\s)', before):
                start = max(start, s.start())
            clause = (re.sub(r'^\s*(?:[-*+]|\d+[.)])\s+', '', before[start + 1:]) + m.group(1)).strip()
            if INTRO.search(clause.replace(ONE_DOT, '.')) or CLAUSE_WORD.search(m.group(2)):
                continue
            shown = re.sub(r'\s+', ' ', m.group(0).strip()).replace(ONE_DOT, '.')
            out.append(F('H-30', i + 1 + c.offset, f'No serial comma: "{shown} …"',
                         f'Add a comma before "{m.group(3)}" ("A, B, {m.group(3)} C"), or make the series a list.'))
    return out


@rule('H-51', 'error', 'No bold-only paragraphs used as headings')
def pseudo_heading(c):
    out = []
    lines = mask_non_prose(c.body).split('\n')

    def blank(k):
        return k < 0 or k >= len(lines) or lines[k].strip() == ''
    for i, line in enumerate(lines):
        m = re.match(r'^(\*\*|__)(?!\s)([^*_\n]{1,100}?)(?<![\s:])\1$', line.strip())
        if not m or not blank(i - 1):
            continue
        if not blank(i + 1) and not re.match(r'^\s*(?:[-*+]\s|\d+[.)]\s|\||#)', lines[i + 1]):
            continue
        out.append(F('H-51', i + 1 + c.offset, f'Bold line used as a heading: "{m.group(2).strip()}"',
                     'Make it a real heading (## or ###), or a run-in label with its text on the same line ("**Label:** text").'))
    return out


@rule('H-97', 'error', 'No numeral at the start of a sentence')
def numeral_start(c):
    out = []
    body = re.sub(r'<sup>[\s\S]*?</sup>', _blank, c.body, flags=re.I)
    lines = _shield_abbrev(mask_ui_text(mask_non_prose(body))).split('\n')
    prev_ends = True
    for i, raw in enumerate(lines):
        if raw.strip() == '' or re.match(r'^\s*(#|\||>?\s*$)', raw):
            prev_ends = True
            continue
        marker = re.match(r'^\s*>?\s*(?:[-*+]|\d+[.)])\s+', raw)
        if marker:
            line = ' ' * len(marker.group(0)) + raw[len(marker.group(0)):]
        else:
            line = re.sub(r'^\s*>\s?', _spaces, raw, count=1)
        starts = []
        first = re.search(r'\S', line)
        if (marker or prev_ends) and first:
            starts.append(first.start())
        starts += [m.end() for m in re.finditer(r'[.!?]["\')\]]?\s+(?=\S)', line)]
        for s in starts:
            n = re.match(r'\d[\d,.]*(?=\s+[A-Za-z])', line[s:])
            if n:
                out.append(F('H-97', i + 1 + c.offset, f'Sentence starts with the numeral "{n.group(0)}"',
                             'Spell the number out, or reword so the sentence starts with a word (HOUSE-3).'))
        prev_ends = bool(re.search(r'[.!?:]["\')\]]?\s*$', line))
    return out


@rule('H-90', 'error', 'No internal product terms (use the UI name)')
def internal_term(c):
    out = []
    prose = mask_non_prose(c.body)
    for t in c.internal_terms:
        term, use, allow = t['term'], t['use'], t.get('allow') or []

        def allowed(s):
            for a in allow:
                s = re.sub(re.escape(a), _spaces, s, flags=re.I)
            return s
        masked = allowed(prose)
        for m in re.finditer(r'\b' + re.escape(term) + r's?\b', masked, re.I):
            out.append(F('H-90', line_of(masked, m.start()) + c.offset, f'Internal term "{m.group(0)}"', f'Use {use}.'))
        for img in c.images:
            if img['alt'] and re.search(r'\b' + re.escape(term) + r's?\b', allowed(img['alt']), re.I):
                out.append(F('H-90', img['line'], f'Internal term "{term}" in the alt text of {img["basename"]}', f'Use {use}.'))
    return out


@rule('H-91', 'warn', 'No narration of the document (say what the reader can do)')
def narration(c):
    masked = mask_ui_text(mask_non_prose(c.body))
    p = (r'\b(?:this|the following|the next|the previous)\s+(?:page|article|document|doc|guide|section|sections)\s+'
         r'(?:covers?|describes?|documents?|explains?|walks|shows?|lists?|is about|goes through|will)\b|\bthese docs\b'
         r'|\bin (?:this|these) (?:docs|documents|articles)\b|\bas (?:described|mentioned|explained|shown) (?:above|below|earlier|later)\b')
    return [F('H-91', line_of(masked, m.start()) + c.offset, f'Narrates the document: "{m.group(0)}"',
              'Start with what the reader can do or learn; link to a section by its name.')
            for m in re.finditer(p, masked, re.I)]


PLAIN = [
    (r'\bin order to\b', 'to'), (r'\bin order that\b', 'so'),
    (r'\bdue to the fact that\b|\bin light of the fact that\b|\bfor the reason that\b', 'because'),
    (r'\bin spite of the fact that\b|\bregardless of the fact that\b', 'although'),
    (r'\bin the event (?:that|of)\b', 'if'), (r'\bthe majority of\b', 'most'), (r'\bat the present time\b', 'now'),
    (r'\bfor the purpose of\b', 'to'), (r'\bby means of\b', 'with'), (r'\bprior to\b', 'before'),
    (r'\butili[sz](?:e|es|ed|ing|ation)\b', 'use'), (r'\bcommenc(?:e|es|ed|ing)\b', 'start'),
    (r'\bascertain(?:s|ed|ing)?\b', 'find out'), (r'\bendeavou?r(?:s|ed|ing)?\b', 'try'),
    (r'\bsubsequently\b', 'afterwards, then'), (r'\bleverag(?:e|es|ed|ing)\b', 'use'),
    (r'\bseamless(?:ly)?\b', 'what actually happens'),
]


@rule('H-92', 'warn', 'No padding, officialese or commercialese')
def plain_words(c):
    masked = mask_ui_text(mask_non_prose(c.body))
    return [F('H-92', line_of(masked, m.start()) + c.offset, f'"{m.group(0)}"', f'Use "{use}".')
            for p, use in PLAIN for m in re.finditer(p, masked, re.I)]


@rule('H-93', 'warn', 'No negative contractions in prose')
def negative_contraction(c):
    masked = mask_ui_text(mask_non_prose(c.body))
    p = r"\b(?:can|don|doesn|didn|isn|aren|wasn|weren|won|wouldn|shouldn|couldn|hasn|haven|hadn|mustn|needn)['’]t\b"
    return [F('H-93', line_of(masked, m.start()) + c.offset, f'Negative contraction "{m.group(0)}"',
              'Write it out ("cannot", "do not", "is not").')
            for m in re.finditer(p, masked, re.I)]


@rule('H-94', 'warn', 'No AI-giveaway vocabulary or phrases')
def ai_giveaway(c):
    masked = mask_ui_text(mask_non_prose(c.body))
    p = (r"\b(?:delv(?:e|es|ed|ing)|tapestry|intricate|underscor(?:e|es|ed|ing)|robust|serves as|plays an? (?:key|crucial|vital|pivotal) role"
         r"|it['’]s not just)\b|\bnot only\b[^.]{0,60}\bbut also\b")
    return [F('H-94', line_of(masked, m.start()) + c.offset, f'AI giveaway: "{m.group(0)}"',
              'Say it plainly ("is" for "serves as"; drop the "not only… but also" frame).')
            for m in re.finditer(p, masked, re.I)]


@rule('H-95', 'warn', 'No product source paths in prose or comments')
def source_path(c):
    text = re.sub(r'^```[\s\S]*?^```', _blank, c.body, flags=re.M)
    text = re.sub(r'`[^`\n]*`', _spaces, text)
    p = r'\b(?:src|packages)/[\w./()-]+\.(?:tsx?|jsx?|mjs|go|java|kt|py|rs|swift)\b'
    return [F('H-95', line_of(text, m.start()) + c.offset, f'Product source path "{m.group(0)}"',
              'Describe what the reader sees; keep source references in findings, not on the page.')
            for m in re.finditer(p, text)]


@rule('H-96', 'error', 'No internal-only syntax (routes, link forms, ids the UI never shows)')
def internal_pattern(c):
    out = []
    for p in c.internal_patterns:
        for m in re.finditer(p['pattern'], c.body, re.I):
            out.append(F('H-96', line_of(c.body, m.start()) + c.offset, f'Internal-only syntax "{m.group(0)}"', p['why']))
    return out


SEVERITY = {rid: sev for rid, sev, _, _ in RULES}


def lint_text(raw, internal_terms=None, internal_patterns=None, only=None):
    """All findings for one page's text: dicts with rule, severity, line, message, hint."""
    c = Ctx(raw, internal_terms, internal_patterns)
    out = []
    for rid, sev, _, fn in RULES:
        if only and rid not in only:
            continue
        try:
            found = fn(c)
        except Exception as e:  # a broken rule must not hide the others
            found = [F(rid, 0, f'Rule threw: {e}')]
            sev = 'warn'
        for f in found:
            f['severity'] = sev
            out.append(f)
    return sorted(out, key=lambda f: (f['line'], f['rule']))


# ------------------------------------------------------------------ product facts

def load_json(name):
    path = os.path.join(STANDARDS, name)
    if not os.path.isfile(path):
        return None
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def product_rules(product_id):
    """(internal_terms, internal_patterns) of a gk-docs-automation product id, from standards/products.json."""
    data = load_json('products.json') or {}
    p = (data.get('products') or {}).get(product_id) or {}
    return p.get('internalTerms') or [], p.get('internalPatterns') or []


def product_for_key(key):
    """The gk-docs-automation product id of a help center key (product/config.json `key`)."""
    data = load_json('repo-products.json') or {}
    return (data.get('products') or {}).get(key)


# ------------------------------------------------------------------ conformance

def run_conformance(path=None):
    spec_path = path or os.path.join(STANDARDS, 'conformance.json')
    with open(spec_path, encoding='utf-8') as fh:
        spec = json.load(fh)
    failures = []
    if spec['rules'] != SEVERITY:
        failures.append(f'rule set or severities differ: conformance {spec["rules"]} vs port {SEVERITY}')
    fm = '---\ntitle: A page\ndescription: A description.\n---\n\n'
    for case in spec['cases']:
        found = lint_text(fm + case['body'], case.get('internalTerms'), case.get('internalPatterns'))
        for rid, count in case['expect'].items():
            got = [f for f in found if f['rule'] == rid]
            if len(got) != count:
                failures.append(f'{case["name"]}: {rid} expected {count}, got {len(got)} {[f["message"] for f in got]}')
    return len(spec['cases']), failures


def main(argv):
    if '--test' in argv:
        n, failures = run_conformance()
        for f in failures:
            print(f'FAIL {f}')
        print(f'{n} conformance cases, {len(failures)} failure(s)')
        return 1 if failures else 0
    product, files, i = None, [], 0
    while i < len(argv):
        if argv[i] == '--product' and i + 1 < len(argv):
            product = argv[i + 1]
            i += 2
            continue
        files.append(argv[i])
        i += 1
    if not files:
        print(__doc__)
        return 2
    terms, patterns = product_rules(product) if product else ([], [])
    errors = 0
    for path in files:
        with open(path, encoding='utf-8') as fh:
            for f in lint_text(fh.read(), terms, patterns):
                level = 'ERROR' if f['severity'] == 'error' else 'WARN'
                errors += level == 'ERROR'
                print(f'{level:5} {path}:{f["line"]}: {f["rule"]} {f["message"]}' + (f'  ({f["hint"]})' if f['hint'] else ''))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
