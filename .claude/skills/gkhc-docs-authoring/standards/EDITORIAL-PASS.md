# The editorial pass — brief for the editor

The editorial pass is the judgment check on an audit's prose (`WRITING-STANDARDS.md` §9.7). Lint
catches the mechanical rules; this pass catches what only a reader can: content a user cannot see or
use (implementation detail, internal syntax), text that narrates the app or the docs instead of
helping someone do a task, internal names, padding, and pages that are accurate but hard to use. Every page an audit edits gets one before `run --apply`.

You are the editor. You did not write the prose. Edit the page in place so it reads as professional
help-center documentation for the product's audience.

## Read first

- `standards/WRITING-STANDARDS.md`: §2 (HARD rules), §3 (SOFT rules: prose quality, paragraphs and
  organization, audience), §8 (the house context) and §9 (GitKraken's writing rubric, the AI
  giveaways, names and the house rulings). §9 is the part most often missed.
- `docs/products/<product>.md` for product facts, and the product's `internalTerms` in
  `src/core/registry.ts` (code names that must not reach a page, with the UI name to use).
- The product's own UI strings (its locale file or rendered UI) whenever you change a label. UI
  labels are written exactly as the product shows them.

## What to fix

- **Scope first: only what users can see, do or affect** (HOUSE-7). Read every section, including
  text that predates the audit, and ask of each: can a user see this, do this, or be affected by it
  in the product? Cut what fails, or rewrite it as the outcome the user sees ("Kepler retries a few
  times", not the health-check interval and backoff). Out of scope however accurate: internal routes,
  anchors and ids; link forms and syntax no UI produces or shows; source paths; launch flags Kepler
  passes for the user; timers, caches, storage, fallback order and matching algorithms; protocol
  names; design rationale; legacy keys; changelog history. Check a doubtful item against the
  product's UI strings: no string and no entry point means it is internal.
- **Narrating the docs or the app instead of helping the reader** (R-10). No "this page covers",
  "these docs", "the following sections", "as described above". Don't describe how the app is
  organized ("the first two entries of the sidebar", "the third group holds…") unless a step needs
  it to find something. Open each page and section with what the reader can do there.
- **Internal names** (R-5, HOUSE-4). Use the UI's name for every control, panel and view.
- **Plain language and sentences** (R-11 to R-14, S-1 to S-6): one idea per sentence, active voice
  with an actor, everyday words, no padding, officialese, commercialese or marketing (S-7).
- **Weasel words and AI giveaways** (R-15, R-17).
- **House rulings** (§9.4): no negative contractions in prose, numerals for numbers, no metaphors in
  instructions, US spelling, and capitalization that follows the product's UI.
- **Structure** (R-6 to R-9, S-12 to S-22): the opening sentence states the point; one topic per
  paragraph; long paragraphs and runs of facts become lists or tables; steps are numbered;
  headings are task- or topic-based and parallel.
- **Names** (R-18 to R-20).

## Humanizer, last (added 2026-11-17)

After the style edits, run gitkraken-marketing-os's `ai-copy-humanizer` skill on the text the audit
changed (`git diff origin/main -- <page>` in the docs repo), on a fresh checkout of that repo:

- Read the skill (`.agents/skills/ai-copy-humanizer/SKILL.md`) and its checklist
  (`Misc/10 major AI giveaways.txt`) from the repo each time, never from memory.
- Mode: minimal edits, keep the voice. Fix real hits only (puffery, ornate words, false balance,
  empty "-ing" add-ons, reflexive triads, fancy verbs, em-dash overuse, mixed quote styles, stock
  phrases, unverifiable references). A real 3-step sequence or a quoted UI string is not a hit.
- The house rules still win: no negative contractions in prose, UI labels exactly as the product
  shows them, no new or lost facts. Release-notes pages are exempt.
- Record what you did in `--humanizer` (below): the checklist items fixed by number with a short
  before → after, or "no checklist hits", and any hit you left on purpose with the reason.

## What not to do

- **No new facts, no lost facts** (H-79). Every behavior, label, default and limit survives unless it
  is wrong or out of scope (HOUSE-7). If you think a statement is wrong, check the product source at the audited release and
  fix it only with that evidence; otherwise report it.
- Don't rewrite clear, accurate sentences for the sake of it. Do check the whole page, including
  text that predates the audit.
- **Figures:** never change `src`/`href`, add, remove or move figures. Change alt text or a
  figcaption only when it breaks a rule here, and list each one: those images are re-judged.
- **Headings:** keep existing headings as they are. A renamed heading changes its anchor, and links
  from outside the docs repo (the product's in-app links, support replies, search results) cannot be
  found by grep (GKD 12.7.0, 2026-11-17: 12 renames reverted). Rename only a heading the audit's own
  change makes wrong, and then list the old and new anchor.
- **Frontmatter:** keep every field; `description` may be improved (no `: ` inside it).
- **Line endings:** keep the page's own (docs pages are often CRLF). Edit in place; never rewrite
  the whole file through a tool that changes them. `sed -i` in Git Bash on Windows strips CR from
  every line (it did on 3 Kepler pages in one pass, 2026-10-30): use an editor tool, or check that
  the CR count still equals the line count afterwards.
- Never edit release-notes pages.

## Outside an audit

The pass is the same for a page changed outside an audit (a docs repo session, another skill's
edit): same reading, scope first, same humanizer, same three fields. Only the record differs:

- With a gk-docs-automation checkout: `gkdocs style review <product> <page-file> --standalone …`,
  then `gkdocs check <page-file>` (CLAUDE.md "Standalone checks"). The record stays out of every
  audit.
- Without one: run the shared skill's `check_pages.py <page>` for the mechanical rules, and put
  the record in the PR description under an "Editorial pass" heading, one entry per page with the
  same three parts: reason, scope, and humanizer.

Read the standards from this folder's files (`WRITING-STANDARDS.md`, `PAGE-RULES.md`,
`IMAGE-STANDARDS.md`, `products.json`); in a docs repo they are the skill's synced copy.

## Finish

1. `gkdocs lint <page>` → 0 errors, and no H-90 to H-97 warning you could fix. Read every H-30
   (serial comma) warning: the rule is a heuristic, so fix each real one and leave the rest.
2. `gkdocs style review <product> <page> --reason "<what you checked and changed>" --scope "<what
   you confirmed user-facing, and what internal detail you cut>" --humanizer "<checklist items fixed,
   or no checklist hits, and hits left on purpose>"`. Do not edit the page after recording it.
3. Report per page: what you cut for scope, the kinds of change with a few before → after examples, renamed headings
   (old → new anchor), changed alt text or captions (basename), factual issues found (with the source
   evidence), and anything you deliberately left.
