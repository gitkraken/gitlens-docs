# Page skeletons

Copy the skeleton, then copy real values from a sibling page in the same nav
section: its metadata style, its `custom_fields` and its voice. `<…>` marks
something to fill in. Delete any section the source material can't support:
don't pad it, and don't invent behaviour to fill it. Product-specific
skeletons (Insights' metric pages and playbooks) are in `product/`.

After writing, run `scripts/check_pages.py <file>` and the preview
(SKILL.md, step 6).

---

## Content page (how-to, concept, reference)

File: `<content folder>/<product-prefixed-slug>.md`, lowercase and hyphenated.
Check the slug is free site-wide first (frontmatter.md, "Slugs are site-wide").

````markdown
---
title: "<Task-phrased title>"
description: "<One sentence, under 160 characters>"
product: <constant from product/PRODUCT.md>
feature: <Feature, reuse an existing value>
content_type: how-to
audience: developer
plan_required: <[all] | the lowest plans>
status: GA
last_verified: <YYYY-MM>
llms_include: true
tags: [<3 to 8 keywords>]
# + this help center's Conditional fields (product/PRODUCT.md)
taxonomy:
    category: <category from product/config.json>
custom_fields:
    nav_category: "<key of the top-level ancestor>"
    nav_label: "<Label in the nav>"
    nav_order: <between its siblings, steps of 10>
    nav_parent: "<parent slug or group key, or "" at the top>"
    page_type: "content"
---
<kbd>Last updated: <Month YYYY></kbd>

<One or two sentences: what this page helps the reader do.>

> **Note:** <a prerequisite or a fact the reader must not miss>.

## <Task-based heading>

1. <Step.>
2. <Step.>

> **Warning:** <a consequence the reader must not miss>.

## <Next task>

…
````

## Landing page (`page_type: index`)

Turns a nav heading into a page of cards (patterns.md, "Index pages in every
help center"; follow its steps for the slug and the children).

````markdown
---
title: "<Section title>"
description: "<what the section covers>"
# … metadata as above, content_type: overview, audience: all
taxonomy:
    category: <category>
custom_fields:
    card_description: "<one line, no final period>"
    nav_category: "<its own slug if top level, else its top-level ancestor>"
    nav_label: "<the heading's label>"
    nav_order: <the group's order>
    nav_parent: "<the group's parent, or "">"
    page_type: "index"
---
<kbd>Last updated: <Month YYYY></kbd>

<Intro: one or two paragraphs. Everything above the first rule.>

---

## <Optional overview section below the cards>
````

## Home page (`page_type: main-index`)

One per help center, the `home_slug` of `product/config.json`. The hero lede
is the intro above the first `---` (or `card_description` without a rule).
Entry paths come from `entry_*` fields on other pages, card sets from
`home_group`, everything else from the product nav file's `home_blocks` and
`home_cards` (patterns.md, "Generic home").

## Moving content out of a page (a split)

Keep the original page, move the sections to new pages, and add an
`anchor_map` to the original so old `#anchor` links land on the new pages
(patterns.md, "Anchor map").
