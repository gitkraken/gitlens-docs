# Image standards for help center pages

**Status:** Normative for every image on a GitKraken help center page, whether an audit captured it
or a person added it by hand. This file gathers rules that were spread across
`WRITING-STANDARDS.md`, `CLAUDE.md`, the docs-audit skill and `polish-policy.json`, so an author
outside an audit finds them in one place. Where this file and those sources differ, the source
named in each section wins; fix this file.

It travels with the shared help center skill (`gkhc-docs-authoring`), synced from
gk-docs-automation by GK-WP-HC-Design `skills/standards_sync.py` (`standards/BUNDLE.json`). Edit
it in gk-docs-automation only.

## 1. Alt text

Source: `WRITING-STANDARDS.md` §4 (the specification), §8.3 (the house pattern) and §2.9 (H-62 to
H-71).

- Every `<img>` has an `alt` attribute (H-62, an error). `alt=""` only for decoration, which a
  product screenshot never is (§4.3).
- One or two sentences, never more (H-63, an error since 2026-11-18). Google states no word count
  (NEG-2); our working target for a single-panel screenshot is 10 to 20 words **[EXTENSION]**.
- Never a filename (H-62a, an error), and never "Image of", "Screenshot of" and the like (H-64).
- Capitalize the first word, end with a period, no all caps (H-65, H-66).
- Say what the reader is looking at and what it shows, in the context of the step it illustrates
  (§4.4). Name the product and the UI surface when the prose around it does not. Do not list every
  column, icon, and color, and do not repeat the figcaption (H-67).
- **Describe the pixels, not the intent.** Write it with the image open. Every noun in it must be
  findable in the frame. When a capture masks something, say so rather than describing what is
  behind the mask.
- Name the control the way the product does (HOUSE-6), never by an annotation: "the **Start
  Review** button", never "the highlighted button" or "the teal box" (HOUSE-1, H-15).
- No internal terms in alt text either (H-90; `products.json` → `internalTerms`).
- One image, one alt. The same basename on two pages, and the figcaption beside it, change
  together: search the docs repo for the basename.
- A GIF that shows a workflow gets a short alt, and the numbered steps appear in the body (§5.2).
  A GIF that loops for more than 5 seconds needs a way to stop it (§5.3, WCAG 2.2.2).

`gkdocs lint` and the skill's checker test H-62, H-62a, H-63, and H-64 mechanically. The rest is
judged in the editorial pass and the image review (section 7).

## 2. Annotation

Source: `WRITING-STANDARDS.md` HOUSE-1 (§7.1).

One accent for every product: house teal `#01FEE0`, a 3 CSS px stroke, corners that follow the
highlighted element's own radius plus its padding, or 5 px where the element has none. No
numbers, badges, or second colors. Images captured before 2026-11-03 keep purple until they are
next recaptured. The prose and alt text name the control, so the color carries no meaning on its
own.

## 3. What a figure shows: subject and context

Source: the docs-audit skill, "2b. Which figures a change makes wrong".

Every figure has a **subject** (what it is about) and a **context**:

- `none`: the surroundings are padding (a dialog, a menu, a settings card). Crop tight.
- `locating`: the reader uses the surroundings to find the subject (the toolbar a button sits
  in, the row a menu opens from). Keep the nearest landmark, no more.
- `relational`: how things sit together is the point (a docked panel, panels in a grid, an
  overlay over a page). The wider frame is the subject.

A figure is replaced when its subject changed, when a landmark it relies on changed (`locating`),
when anything in frame changed (`relational`), or when a control the page or alt names was
removed or renamed. A change elsewhere in the frame alone is not a reason to recapture.

## 4. Polish: what ships as is and what is fixed

Source: `polish-policy.json` (the owner's standing policy; read the file for the exact classes).

- **Ships as is:** an edge fragment behind an overlay that the crop cannot avoid, uneven padding,
  inner whitespace that only a crop through a component removes, a harmless hover or focus
  state, a staged-state oddity the page does not contradict, the product's own glyphs, and public
  names production shows every user.
- **Fixed, when the fix is easy:** whitespace outside the subject that a crop removes, a large
  empty band a smaller viewport removes, a subject too small to find (add a HOUSE-1 ring), a frame
  missing the context to locate the subject, a crop that slices a component, alt or caption text
  slightly off from the pixels, and a frame so wide that its text cannot be read at page width
  (roughly over 1600 CSS px for a text-heavy subject).
- Never crop through a component.

## 5. Privacy and identity

Source: the docs-audit skill, "Write guard and masking", and hard constraint 8.

- **No published image shows a real identity**: no real name, email, avatar, organization
  member, or account id of the person who captured it or of anyone else. Captures use the neutral
  identity *Alex Lee* / `alex.lee@example.com`, or stage around identity (fixtures, crops that
  leave the account out). An image that may show a real identity is not published.
- No tokens, keys, private repository names, customer data, or internal URLs in frame.
- Never capture or replace third-party UI screenshots (Okta, Azure, PingIdentity): leave them as
  they are.
- Public names production shows every user (public theme authors, the GitKraken organization)
  are fine.

## 6. Names, files, and replacing an image

Source: the docs-audit skill, hard constraints 2 and 5; `CLAUDE.md`, "Screenshots for gap
findings".

- **Never overwrite or delete a published image.** A new capture gets a new file name, and every
  reference to the old one is rewritten, in every docs repo that uses it. WordPress serves images
  from one flat uploads folder shared by every product, so the old file may still be in use
  elsewhere.
- New names: `<prefix>-<feature>-<aspect>.png`, lowercase and hyphenated, with `@2x` for retina
  captures and `-v2`, `-v3` for a replacement of an existing name. The prefix is the product's
  `imagePrefix` in `products.json` (`ade-`, `gkd-`, `gl-` and so on). Lowercase hyphenated names
  are our convention, not Google's (NEG-7).
- Markup is the docs repo's own: in help center pages, `<figure>` with
  `<img src="/wp-content/uploads/<file>" class="help-center-img img-bordered" alt="…">` and an
  optional `<figcaption>` after it (H-78). Never convert an HTML image to Markdown `![]()`, which
  cannot carry the classes.
- Keep `src` and `alt` exactly as they are when you move a figure.
- Screenshots normally come from the docs-audit capture flow (a spec that reaches STABLE in
  Docker). An image made any other way meets every rule in this file and gets the image review.

## 7. Checks before an image ships

- `gkdocs lint <page>` or the skill's `check_pages.py`: H-62, H-62a, H-63, and H-64 pass, the file
  exists in the docs repo's image folder, and no published image was modified in place.
- The image review: in an audit, the final visual judgement (`final-visual-judgement-comparison`
  skill). Outside an audit, the same review in standalone mode
  (`python scripts/capture-review/review.py init --standalone …`, `CLAUDE.md` "Standalone
  checks"). A FAIL blocks the merge; a polish note is fixed under section 4 or accepted.
