# Markdown patterns → components

Source: `GK-WP-HC-Plugin/includes/gkhc-passc.php`. If this file and the PHP
disagree, the PHP is right; update this file.

Patterns are matched against **rendered HTML**, so small Markdown details
matter. For example, the bold label in a run-in must end in `.` or `:`
*inside* the `**`. Each transform is forgiving: if the pattern isn't there,
the content renders unchanged.

Every page of every help center goes through the **general pipeline**
(`gkhc_passc_restructure_general`, priority 17), after
`gkhc_docs_clean_parsedown` (15), which removes empty `<p>` elements and stray
`<br>` elements between blocks. Help centers other than Insights also run the
content adapters (below). A product can have more: Insights' metric pages,
playbooks and settings blocks are described in its `product/metric-pages.md`.

Everywhere: plain numbered Markdown lists (`1.`) are drawn as the site-wide
step rail by CSS. Headings feed the right-hand "On this page" TOC (the
product's `toc_levels`; H2 and H3 unless `product/PRODUCT.md` says otherwise).

## Heading ids (the Add Anchor Links plugin)

Heading ids don't come from GK-WP-HC-Plugin or WordPress. The **Add Anchor
Links** WordPress plugin (active on production and staging, for posts)
inserts `<a href="#slug" aria-hidden="true" class="aal_anchor" id="slug">`
into every heading, with slug = `sanitize_title()` of the heading text:
lowercase, punctuation dropped, spaces to hyphens (`## Quick start` →
`#quick-start`). Two headings with the same text get the **same** id (the
plugin does not de-duplicate), so a `#link` lands on the first of them.
`#heading` links, the TOC and `anchor_map` depend on these ids; renaming a
heading breaks links to it. GK-WP-HC-Design's `preview/` emulates the plugin.

## Callouts: the standard (decided 2026-11-09)

Write callouts as Markdown blockquotes with a bold prefix, in every help
center:

```markdown
> **Note:** Text of the note.

> **Tip:** Text of the tip.

> **Warning:** Text of the warning.
```

Never write HTML callouts (`<div class="callout callout--…">`,
`<div class="bbb-callout bbb--…">`, `<div class="note">`, in either quote
style). The plugin still converts existing ones (content adapters, below),
but `check_pages.py` reports each page that has one as an ERROR until it is
converted. **Exception (decided 2026-11-10): a callout inside a table cell**
(an HTML `<td>`, or a Markdown table row) is allowed and only warns: a
blockquote can't go in a table cell, and the adapter renders the HTML one.
A callout the product lists in `product/config.json` → `known_html_callouts`
(page slug and the first 60 characters of its text) was left as HTML by
decision and also only warns. The other lead phrases below (`**Important:**`, `**Caution:**`,
`**Prerequisites:**`, Insights' `**Before you start:**`, `**Heads up:**`)
still render; prefer the three standard ones in new content.

---

## General pages (everything except metric pages)

| Pattern (Markdown) | Becomes | Applies to |
|---|---|---|
| First `## Heading` equal to `title` or `nav_label` | removed | `content` pages |
| `> _Italic-only sentence._` before the first H2, under 500 characters | `.gkhc-definition` lede | `content` pages (playbooks open this way) |
| `> **Lead phrase:** text…` | typed callout `.gkhc-callout--warn/info/tip/note` | all general pages |
| `> _italic-only_` (anywhere else, or nested in a callout) | `.gkhc-quote` (quotation, not a callout) | all general pages |
| `<figure>` before the first H2/H3, not preceded by a numbered list | `.gkhc-hero-figure` | `content` pages |
| ```` ```lang ```` fenced block | labelled code panel: `json`→JSON, `sh`/`bash`/`shell`→Shell, `text`→Code, else the language upper-cased, none→Code | all general pages |
| Table with ≥2 body rows whose first cell is a link in every row | `.gkhc-related-table` | all general pages |
| `* [ ] item` / `* [x] item` (every item in the list) | `.gkhc-checklist` with drawn boxes | all general pages |
| `**Label.** text` / `**Label:** text` | run-in | all general pages |

### Callout types

The type comes from the bold lead phrase. With no bold lead, it comes from
the first 80 characters. The first rule that matches wins:

| Type | Lead contains |
|---|---|
| **warn** | private, owner, heads up, don't merge, warn, restart, precedence, caution, do not, don't, won't, never, requires, watch, must |
| **info** | before you start, privacy, data appears, backfill, already send, note, suppress, only returns |
| **tip** | tip, recommended, you can edit, shortcut |
| **note** | anything else |

So `> **Before you start:** …` is info, `> **Heads up:** …` is warn, and
`> **Tip:** …` is tip. Pick the lead phrase for the type you want, but don't
twist the wording to get it.

## Index pages (`page_type: index` / `main-index`)

```markdown
<kbd>Last updated: November 2026</kbd>

One or two intro paragraphs.

---

## First overview section
…
```

The template splits at the **first** `---`. Above it is the intro. Then come
the landing search ("What are you looking for?") and the card grid. Everything
after the rule goes in `.gkhc-below-cards`. If an index page is only an intro,
it doesn't need a rule.

Home (`main-index`) uses the same split: the intro is the hero's lede, then
come the home blocks (below; Insights has its own home, see its
`product/PRODUCT.md`), then the rest of the content.

### Index pages in every help center

Any page with `page_type: index`, at any depth, in any help center, gets the
same layout: intro → landing search → card grid → everything after the first
`---`. Outside Insights the cards are the page's **children in the nav**
(NAV-CONTRACT.md): every page whose `nav_parent` is this page's slug, every
`nav_also` placement under it, and every link of the product nav file under
it, in `nav_order`. A label-only group of the nav file under the page becomes
a titled section with its own children as cards. A page placed under itself
(`nav_also` with its own slug) gets no card.

Cards read `card_icon`, `card_color` and `card_description`. Without them the
card still renders: a folder icon for a page with children, a file icon for a
page, an external-link icon for a link, purple, and as description the labels
of the page's first children ("A, B, C and 2 more").

Turning a label-only group into an index page:

1. **Pick a product-prefixed slug that is free site-wide**, for example
   `kepler-integrations` for Kepler's `integrations` group. Git It Write finds
   a page's post **by slug across the whole site**, whatever the category, so
   a file named after a bare group key can take over another help center's
   post: `integrations` is a live Desktop post, and `start-here`,
   `release-notes` and `getting-started` recur in several help centers. Check
   the slug is unused on production (WP Admin → Posts, search for the slug)
   and in every docs repo.
2. Write the index page under that file name, with `page_type: index`, and
   `nav_parent`/`nav_order`/`nav_label` from the group.
3. Point the children at it: change each child's `nav_parent` (and any
   `nav_also` parent, `nav_category` of descendants, nav-file `parent`) from
   the group key to the new slug.
4. Remove the group from `config/products/<key>.json` (plugin change, same PR
   or before).

Only if the group key itself is product-prefixed and free (rare) can the
index page take the group key as its file name and leave the children as
they are.

### Generic home (`main-index` outside Insights)

The home page is composed of blocks: the product nav file's `home_blocks`
(plugin side), else the registry default, which lists every block type.
Each renders only when its data exists, so the home shows exactly what the
pages and the nav file supply, and the page's content always renders. Items
of `paths` (with a `group`), `cards`, `chips`, `cta` and `links` come from
pages whose `home_group` lists the group (ordered by `home_order`) plus the
nav file's `home_cards` entries with that group. The field contract is in
`redesign-expansion/NAV-CONTRACT.md`, "Fields the plugin reads beyond the
nav". Default groups: `cta`, `paths`, `install`, `features`, `chips`,
`links`; default facet field `git_hosts`.

| Block | Comes from |
|---|---|
| hero | product title, the page's H1, its lede (content above the first `---`; without a rule, `card_description`), the landing search |
| paths | pages with `entry_title` (+ `entry_role`, `entry_desc`), ordered by `entry_order` |
| sections | the top-most `page_type: index` pages of the nav |
| cards | a named set: pages with that `home_group`, ordered by `home_order`, plus `home_cards` entries of the product nav file (cards that aren't pages, e.g. install methods) |
| facet | one card per value of a custom field listing the pages that carry it; by default `git_hosts` (GIJ Cloud's host grid), shown by host name |
| chips | a named set as a chip row (Kepler agents, MCP clients) |
| cta | a named set as buttons, the first one filled (GitLens install) |
| links | a named set as a styled link list (GIJ Data Center) |
| module | a per-product block registered in PHP (none yet) |
| content | the rest of the page |

Decided shapes (PER-PRODUCT-DECISIONS.md) and the data each needs:

| Help center | Blocks | Data |
|---|---|---|
| Kepler | hero, paths ×4, sections, chips | `entry_*` on 4 pages; section index pages; `home_cards` group `chips` (agents) |
| MCP | paths ×2 (install), cards (tools by category), chips (clients) | `home_cards` groups `install` (with `role`), `tools`, `clients` and a `home_blocks` naming them |
| GIJ Cloud | paths ×3, facet (9 hosts) | `entry_*` on 3 pages; `git_hosts` mirrored under `custom_fields` |
| Desktop, gkdev | paths ×4, sections | `entry_*` on 4 pages; section index pages |
| GitLens | cta, paths ×4, cards (curated features) | `home_cards` group `cta`; `entry_*`; `home_group: features` on the curated pages |
| CLI | hero, cards ×4 (install) | `home_cards` group `install` (anchors on the home page) |
| GIJ DC | links, cards | `home_group: links` / a cards group on the pages |

## Release notes

`layout: release-notes` on a release-notes page collapses its TOC to H2
(one entry per version: write each version as `## Version x.y`). A
release-notes `page_type: index` page is the version picker: its version
pages are its cards, like any index page. A release-notes content page that
has version pages under it in the nav (GitLens' current notes) shows them
as cards above its notes. Only front matter changes: add `layout:
"release-notes"` to each version page and to the landing page, and make a
label-only "Release Notes" group an index page if the help center wants a
landing page.

## Settings spec panels

In Kepler and GitLens (`settings_panels`), a settings table becomes one
mini spec panel per row: tables whose first column is headed `Setting`,
`Control`, `Option` or `Field`, and `Name | Description` tables whose every
name is a `<code>` key such as `gitlens.currentLine.enabled`. The first
cell names the panel; every other cell becomes a field under its column
header. Write settings as such tables; a table with a ragged row stays a
table.

---

## Patterns of the other help centers (content adapters)

Pages written for the old theme keep working: the plugin's content adapters
(`includes/gkhc-adapters.php`) convert these patterns. Don't add new
instances of the left column in new content; write the right column's source
form instead (a `> **Note:**` blockquote, a normal fenced code block).
Insights runs none of the adapters.

| Source pattern | Renders as |
|---|---|
| `<div class="callout callout--basic\|note\|neutral\|info\|warning\|danger\|success">` (also on `<figure>`, also plain `callout`) | typed callout (note / info / warn / danger / tip) |
| `<div class="bbb-callout bbb--info\|note\|tip\|alert\|error">…<div class="imsgbox">` | typed callout with only the `imsgbox` body |
| `<div class="note">` | note callout |
| `> **Note:**`, `**Tip:**`, `**Warning:**`, `**Important:**`, `**Caution:**`, `**Deprecated:**`, `**Requirements:**`, `**Prerequisites:**` blockquotes | callout of that type (explicit prefix wins over the keyword guess) |
| `<style>`/`<script>` copy-button blocks (`.copy-btn`) | removed; code panels have a Copy button |
| a leading `<kbd>Last updated: …</kbd>` | the muted page-meta line under the H1 |
| `**On this page:**` / `**What's on this page:**` lists of `#anchor` links | removed: the right-hand TOC lists the same headings |
| `**Requirements and limits**` + a list where **every** item is `Key: value` | spec panel (any other list is left as a list). **Off by default**: Desktop keeps the block as written (decided 2026-11-09) |
| `### Problem` / `Diagnosis` / `Cause` / `Solution` (2+ at one level) | issue rows: label column + body |
| `` `PRO` `` / `` `PREVIEW` `` / `` `ADVANCED` `` / `` `BETA` `` / `` `EXPERIMENTAL` `` in a heading | badge, left out of the TOC text. **Off by default** (GitLens declined badges, 2026-11-09) |
| tables headed `Setting` / `Control` / `Option` / `Field` | settings table (stacks on narrow screens) |
| tables headed `Agent` / `Provider` / `Tracker` / `Integration` / `Host` / `Client`, 4+ rows, each first cell one `**Name**` | card grid, one card per row |
| spacer `&nbsp;` / `<br>` paragraphs | removed |
| an unlabelled fenced code block | code panel labelled with the product's default (CLI: "Terminal"; else "Code") |

The right-hand TOC lists the product's heading levels (`toc_levels`: H2/H3,
GIJ Data Center H3/H4) and falls back to H2/H3 on a page with fewer than 3
headings at those levels.

## Anchor map (split pages)

When a page is split, links to its old anchors must keep landing on the
content. The page that stays behind lists them:

```yaml
custom_fields:
    anchor_map: ["hovers|gitlens-inline-blame#hovers", "commit-graph|gl-commit-graph", "old|#new-anchor"]
```

Each entry is `"<old anchor>|<target>"`. The target is a page slug of the same
help center with an optional `#anchor`, an `#anchor` on the same page, or a
`/path` or `https://` URL. One old anchor maps to one target; the first entry
for an anchor wins. In the browser, a `#fragment` that no element on the page
has, and that the map lists, goes to its target. Anchors that still exist on
the page keep working, so don't map an anchor whose heading is still there
(the checker warns). A block list (`- "a|b"` lines) works too.

---

## Figures

```html
<figure>
  <img src="/wp-content/uploads/gkhc-board-metrics-page-01-v4@2x.png" class="help-center-img img-bordered" alt="Full description of what the screenshot shows" />
  <figcaption>Board Metrics — KPI tiles, then …</figcaption>
</figure>
```

The image file lives in `_images/<name>`. The preview maps
`/wp-content/uploads/<name>` there, and `check_pages.py` checks it exists.
Inside the `<figure>`, Markdown isn't parsed (Parsedown v1), so write any link
in a caption as `<a href>`. All figures get the lightbox.
