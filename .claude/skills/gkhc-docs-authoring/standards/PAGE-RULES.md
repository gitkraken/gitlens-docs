# Page rules for help center pages

**Status:** Normative for every change to a GitKraken help center page, inside or outside an
audit. `WRITING-STANDARDS.md` governs how a page is written; `IMAGE-STANDARDS.md` governs its
images. This file holds the rest: what a page may claim, how much it says, what it keeps up to
date, and what must pass before a change is committed. Each rule names its source in this repo.

It travels with the shared help center skill (`gkhc-docs-authoring`), synced from
gk-docs-automation by GK-WP-HC-Design `skills/standards_sync.py` (`standards/BUNDLE.json`). Edit
it in gk-docs-automation only.

## 1. Verify every claim against the product

Source: `CLAUDE.md` ("Products", "Two sources, different questions") and hard constraints 3, 10
and 16 of the docs-audit skill.

- Check every behavior, label, default, limit, and shortcut you write against the **product
  source at its latest release tag**: the newest tag in `sourceRepo` that matches the product's
  `stableTagPattern` in `products.json`. Read it with `git show <tag>:<path>` after a fetch, never
  in a working tree, which lags behind or runs ahead of what customers have.
- UI labels come from the product's own strings at that tag (its locale file or rendered UI),
  written exactly as the product shows them (HOUSE-4, HOUSE-6).
- The changelog and release notes say what was announced, not what shipped. Use them for
  orientation, never as evidence.
- Document only what every customer has. A feature behind a build-channel gate or rollout flag
  is not documented until the gate is gone.
- Never invent a number, version, shortcut, or menu path (H-79). If you cannot verify a claim,
  leave it out and say so in the PR.

## 2. Only what users can see, do, or affect

Source: `WRITING-STANDARDS.md` HOUSE-7, and the product sections in `products/<id>.md` of this
bundle (from `docs/products/<id>.md`).

Test every section and sentence: can a user see this, do this, or be affected by it in the
product? If not, cut it, or rewrite it as the outcome the user sees. Out of scope however
accurate: internal routes and ids, link forms no UI produces, source paths, launch flags, timers
and retry counts, caches and storage, matching algorithms, protocol names, design rationale, and
changelog history. Each product's internal-only syntax is in `products.json` →
`internalPatterns` (lint H-96, an error), and its own list of what is not documented on purpose
is in `products/<id>.md` where it has one.

## 3. Detail level

Source: the Kepler-Docs reviewer's ruling on PR #49 (2026-11-04), `products/kepler.md` "Detail
level", which applies to every product; Insights adds its disclosure standard
(`products/insights.md`).

- Keep the control's name, where it is, what it does, and any limit that changes what the reader
  does.
- Cut exhaustive lists of states, messages, buttons, defaults, and counts (keep the two or three
  the reader acts on), quoted UI strings outside troubleshooting, edge cases a typical user will
  not hit, timing and ordering, layout narration, and repetition across sections (say it once and
  link to it).
- Tables: one short sentence per cell.

## 4. Names

Source: `WRITING-STANDARDS.md` R-18 to R-20, HOUSE-4, and HOUSE-6.

Product names in full, features capitalized the way the product's UI shows them, and never a
code name: each product's internal terms, with the name to use, are in `products.json` →
`internalTerms` (lint H-90, an error).

## 5. Keep the page's markers and the repo's index files current

Source: the docs-audit skill, "Update the last-updated markers and the derived index files", and
`CLAUDE.md` "AEO index files after the judgement".

- A page you change substantively gets its date markers set to the current month: the visible
  `<kbd>Last updated: <Month YYYY></kbd>` and any front matter `last_updated` / `last_verified`.
  A wording-only change is not substantive (S-54): do not fake freshness.
- Then bring the docs repo's index files up to date with the pages you added, changed, or
  deleted. `products.json` → `docsRepos.<repo>.indexFiles` says which: a generator to run (Kepler-Docs
  `python scripts/build-llms.py`), the three files `llms.txt`, `llms-full.txt` and `sitemap.xml`
  (in an audit, `gkdocs aeo`; by hand, edit each entry in place in the shape of its neighbors), or
  `none` (Insights: never add its pages to any index).

## 6. Pages and structure you leave alone

Source: `EDITORIAL-PASS.md` "What not to do" and the docs-audit skill, hard constraints 6 and 7.

- Keep existing headings: a renamed heading breaks its anchor for links you cannot search. Rename
  one only when your change makes it wrong, and list the old and new anchor in the PR.
- Never write a `# ` heading in the body; the title comes from front matter (H-52a).
- Never hand-edit release-notes pages (`products.json` → `releaseNotesPage`).
- Keep the page's line endings. Check `git diff --stat` before committing.

## 7. Before you commit

Every changed page passes both layers of `WRITING-STANDARDS.md` before its commit:

1. **The mechanical checks.** `gkdocs lint <page>` or `gkdocs check <page>`, or in a docs repo
   without gk-docs-automation, the skill's `check_pages.py <page>`. Zero errors. Read every
   warning, and fix it or record why it stays.
2. **The editorial pass** (`EDITORIAL-PASS.md`): an editor who did not write the change reads the
   whole page, scope first, then style, then the humanizer. Inside an audit it is recorded with
   `gkdocs style review`; outside one with `gkdocs style review --standalone` (`CLAUDE.md`
   "Standalone checks"), or, with no gk-docs-automation checkout, in the PR description under the
   same three headings (reason, scope, humanizer).
3. **Images** pass `IMAGE-STANDARDS.md` section 7.
