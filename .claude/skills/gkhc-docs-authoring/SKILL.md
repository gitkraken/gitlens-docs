---
name: gkhc-docs-authoring
description: Write, add, move, split, archive or edit pages of a GitKraken help center (help.gitkraken.com, rendered by the GK-WP-HC-Plugin WordPress plugin through Git It Write) so they render and navigate correctly. Covers the front matter metadata schema (checked in CI), the custom_fields that build the nav, breadcrumbs, card landing pages, home page and search; page types; the Markdown patterns the plugin turns into components; the callout standard; Git It Write's rules for renames, archives, slugs and clearing fields; the house writing, page and image standards (standards/, synced from gk-docs-automation: alt text, serial commas, no pseudo-headings, numerals, scope, claims checked at the latest release tag, image naming and privacy); and the check_pages.py lint (structure plus the same prose and image rules as gkdocs lint), the editorial pass and preview to run before committing. This help center's own facts are in product/ (PRODUCT.md, config.json). Use for any content change in a help center docs repo. For changes to the plugin's PHP, CSS or JS, use the gkhc-plugin-design skill in GK-WP-HC-Design instead.
---

# Authoring help center pages

Pages are plain Markdown. The plugin gives them their design, so you never
write layout HTML. There are three levers:

1. **Metadata** (top-level front matter): product, feature, content type,
   audience, plans, status and so on. Not stored in WordPress; read by
   `llms.txt`, the docs audit and agents. **Checked in CI**:
   [references/metadata.md](references/metadata.md).
2. **`custom_fields`** become WordPress post meta. The plugin builds the left
   nav, breadcrumbs, landing-page card grids, the home page and the search
   index from them: [references/frontmatter.md](references/frontmatter.md).
3. **Recognised Markdown patterns.** After Parsedown renders the page, the
   plugin's `the_content` filters find known patterns (callouts, code
   panels, step rails, settings tables, checklists…) and replace them with
   components. Write the pattern and the page gets the component; otherwise
   it renders as plain prose. Nothing breaks either way:
   [references/patterns.md](references/patterns.md).

How the pipeline runs: Markdown in the content folder → Git It Write
(Parsedown v1.7.4 + ParsedownExtra) → a WordPress `post` in the help center's
category → the Add Anchor Links plugin (heading ids) → GK-WP-HC-Plugin's
filters → its page template. The slug is the file name, lowercased. The URL
is `/<category>/<slug>/`.

## Start here: this help center

**Read `product/PRODUCT.md` first.** The shared files (this one,
`references/`, `scripts/`) are identical in every docs repo and owned by
GK-WP-HC-Design: edit them there, or edit them here and let
`skills/skillsync.py collect` bring the change up. `product/` belongs to this
repo and is never overwritten. It holds:

- `product/PRODUCT.md`: content folder, category, home page, nav file, TOC
  levels, metadata constants and the conventions of this help center
- `product/config.json`: the same facts for `check_pages.py` and the preview
- any product-specific references (Insights: `metric-pages.md`, `templates.md`)

`.source.json` records the GK-WP-HC-Design commit and plugin version the
shared files came from. In GK-WP-HC-Design itself there is no `product/`:
the seeds are in `skills/products/<key>/`.

## The house standards (`standards/`)

Every help center is written to the same standards, and this skill carries
them in `standards/`: a synced copy of gk-docs-automation's own files, the
ones its audits enforce. Read them before you write. Do not edit them here
(`standards/SOURCE.json` records where they came from); GK-WP-HC-Design
`skills/standards_sync.py` brings changes down.

| File | What it governs |
|---|---|
| `standards/WRITING-STANDARDS.md` | How a page is written. §2 (HARD rules; §2.11 lists what the checker tests), §3, §8 and §9 (GitKraken's rubric and house rulings: no negative contractions, numerals except at a sentence start, US spelling, UI names) are the parts most often missed. §4 is alt text |
| `standards/PAGE-RULES.md` | What a page may claim (**check every claim against the product source at its latest release tag**), the scope rule (only what users can see, do, or affect), detail level, names, last-updated markers and index files, and what to run before committing |
| `standards/IMAGE-STANDARDS.md` | Alt text, the teal annotation, what a figure shows, the polish policy, privacy and identity, image names, and never overwriting a published image |
| `standards/EDITORIAL-PASS.md` | The editor's brief for the judgment rules |
| `standards/products.json` | Per product: internal terms and syntax that never reach a page, the image prefix, the release tag pattern, and the index files |
| `standards/products/<id>.md` | A product's own detail level and "not documented on purpose" list, where it has one |

## Before you start

- Read `standards/PAGE-RULES.md` and the parts of `standards/WRITING-STANDARDS.md`
  named above, plus `CLAUDE.md` if the repo has one. Don't invent product
  behaviour, don't add, rename or remove images without being asked, and
  don't rewrite text you were only asked to move.
- Look at two or three sibling pages in the same nav section. Copy their
  front matter style and structure, not this skill's examples.
- **Branch from `expo`** for redesign work, and merge back into `expo`. Never
  commit redesign work to `main`.

## Workflow

1. **Place the page.** Pick its parent (`nav_parent`: a page slug or a group
   key of the product nav file), its `nav_category` (the key of its
   top-level ancestor), `page_type` and a `nav_order` between its siblings
   (steps of 10). For a new file, pick a **product-prefixed slug that is free
   site-wide** (below). See [references/frontmatter.md](references/frontmatter.md).
2. **Start from a skeleton** in [references/skeletons.md](references/skeletons.md)
   (content page, landing page, home), or the product's own in `product/`.
3. **Fill the metadata** from the page itself: every Core field and this
   help center's Conditional fields ([references/metadata.md](references/metadata.md),
   `product/PRODUCT.md`).
4. **Write the body using the patterns** in
   [references/patterns.md](references/patterns.md). Callouts are
   `> **Note:**` / `> **Tip:**` / `> **Warning:**` blockquotes, never HTML.
5. **Wire it in.** Nav, breadcrumbs and card grids update on their own.
   Hand-written cross-references don't: check overview tables on the parent,
   "Related" tables on siblings, and every page that links to a slug you
   renamed. Internal links are root-relative, `/<category>/<slug>/`, plus
   `#anchor`: the heading text lowercased and hyphenated, as the Add Anchor
   Links plugin makes it (patterns.md, "Heading ids").
6. **Lint:**
   `python .claude/skills/gkhc-docs-authoring/scripts/check_pages.py [files…]`.
   With no arguments it checks every page and the whole hierarchy, and runs
   the house standards (`scripts/prose_rules.py`: the same rules and
   severities as gk-docs-automation's `gkdocs lint`) on every page your
   branch changed; name files to check those. It also stops a published
   image from being overwritten. **Fix every `ERROR`: CI fails on them.**
   Read each `WARN` and either fix it or know why it's fine; the serial-comma
   warning (H-30) is a heuristic, so check each one. To resolve `nav_parent`
   keys that are nav-file groups it needs a GK-WP-HC-Design checkout beside
   this repo (or `GKHC_DESIGN_DIR`, or `--nav-file`). It needs nothing else:
   no gk-docs-automation checkout, no Node.
7. **Editorial pass (required before you commit).** Someone who did not
   write the change, or you in a fresh read, reads each changed page whole
   against `standards/EDITORIAL-PASS.md`: scope first (HOUSE-7), then style,
   then the humanizer. Then run the lint again. Record it:
   - with a gk-docs-automation checkout: `gkdocs style review <product>
     <page-file> --standalone --reason "…" --scope "…" --humanizer "…"`, then
     `gkdocs check <page-file>` (strict: lint errors or a missing pass fail).
     This needs no audit and writes nothing to one;
   - without one: in the PR description, under "Editorial pass", per page:
     reason, scope, and humanizer.
   If you changed or added an image, it also gets the image review
   (`standards/IMAGE-STANDARDS.md` section 7). Set the changed pages'
   `Last updated` markers and bring the repo's index files up to date
   (`standards/PAGE-RULES.md` section 5).
8. **Preview** with GK-WP-HC-Design's `preview/`, run from that checkout:
   `python preview/build.py --product <key> --tree <this repo>` (or
   `--ref origin/<branch>`). It renders every page with the plugin's own PHP
   and exits non-zero on a broken internal link or a missing image. Open the
   page you changed and check its nav position, breadcrumb, card,
   components and TOC.
9. **Commit** on your branch and open a PR into `expo`. Tell the user about
   any WordPress-side cleanup the change needs (next section).

## Git It Write: rules that follow from how it publishes

Git It Write only creates and updates posts, and only sets fields. It never
deletes, unpublishes or clears anything (verified in its code;
GK-WP-HC-Design `redesign-expansion/WORKFLOW.md`).

- **Clear a field with `""`, never by deleting the key.** A deleted
  `custom_fields` key keeps its old value on the post: `nav_parent: ""` at
  the top level, `nav_also: ""` (or `[]`) to remove placements.
- **Renames and archives leave the old post published**, nav fields and
  all, at its old URL. A rename also changes the slug: update every link,
  `nav_parent`, `nav_also` and `anchor_map` that names it, and tell the user
  the old post has to be trashed on staging and unpublished and redirected
  at cutover.
- **Rename before adding nav fields**, so the old post never carries them.
- **Archive into `_archive/`**: `_archive/<content folder>/ARCHIVED-<name>.md`.
  Git It Write skips every file and folder whose name starts with `_` or `.`.
- **Slugs are site-wide.** Git It Write finds a page's post by slug across
  every category of the site. A new page or landing page gets a
  product-prefixed slug (`kepler-integrations`, not `integrations`), checked
  free on production and in the other docs repos before the first push:
  `integrations` is a live Desktop post, and `start-here`, `release-notes`
  and `getting-started` recur.
- **Slugs are lowercase** (`sanitize_title()` of the file name:
  `GL-Commit-Graph.md` is `gl-commit-graph`). Reference pages by the
  lowercase slug everywhere; the plugin matches `nav_parent` exactly.
- **Everything the plugin reads goes under `custom_fields:`.** A top-level
  `nav_order:` is silently dropped and the page falls out of the nav.

## Changes that need more than a content edit

| Change | What else is needed |
|---|---|
| Delete, rename or archive a file | The old post stays live (above). Update every reference to its slug, and flag the WordPress cleanup to the user. |
| A label-only nav group, or a nav link to something that isn't a page here | Neither can live in a Markdown file. They go in the product nav file, `GK-WP-HC-Plugin/config/products/<key>.json` in GK-WP-HC-Design (NAV-CONTRACT.md). That's plugin work. |
| Turn a group into a landing page | patterns.md, "Index pages in every help center": a new product-prefixed slug, the children re-pointed, the group removed from the nav file. |
| Home blocks, home cards that aren't pages | The nav file's `home_blocks` / `home_cards`: plugin work. Pages join home card sets with `home_group`. |
| A page needs a component no pattern produces | Don't add HTML to the Markdown. The transform has to learn a pattern: plugin work (gkhc-plugin-design skill). |
| New screenshot | Screenshots normally come from the docs-audit capture flow. Any new image follows `standards/IMAGE-STANDARDS.md`: a new file name (never overwrite a published image), no real identity in frame, alt text of one or two sentences. |

## Rules that are easy to miss

- **Nav depth: up to 5 levels.** The checker reports a page deeper than
  that; the plugin shows such a page at level 5 rather than dropping it.
- **One page, two places: `nav_also`.** `"<parent>|<order>|<label>"` entries
  add the page to the nav again under another parent.
- **`nav_label` is what readers see**: the H1, the nav entry, the breadcrumb
  and the card title. `title` is the SEO/post title.
- **Don't write an H1.** The template prints the title. A leading H2 that
  repeats the title or `nav_label` is removed.
- **Landing and home pages split at the first `---`**: intro above, cards
  after it, then the rest.
- **Parsedown v1 won't parse Markdown inside an HTML block.** Inside
  `<figure>`, write links and emphasis as HTML.
- **Images**: `/wp-content/uploads/<file>` must exist in `_images/`, or the
  checker reports an ERROR. The only exception is a pre-existing reference
  listed in `product/config.json` → `known_wp_images` for that page (it
  still serves from WordPress uploads): a warning. A new or moved reference
  is never covered. Keep `src` and `alt` exactly as they are when you move a
  figure.
- **Open each page with `<kbd>Last updated: <Month YYYY></kbd>`**, and update
  it on substantive changes only.
- **Splitting a page? Add an `anchor_map`** to the page that stays
  (patterns.md, "Anchor map"). The checker validates its targets.
- **Old-theme markup is converted, not needed.** The plugin still adapts
  HTML callouts and copy-button `<style>`/`<script>` blocks, but the checker
  reports them (callouts as errors, copy-button blocks as warnings): convert
  and remove them. "On this page" lists are removed by the plugin; the
  right-hand TOC replaces them.
