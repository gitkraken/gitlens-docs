# Frontmatter reference

Every page opens with a YAML block of two kinds of keys:

| Kind | Where | Read by |
|---|---|---|
| **Metadata** | top-level keys (`product`, `feature`, `content_type`, …) | Repo tooling: `llms.txt` generators, the docs audit, agents. Git It Write does **not** store them in WordPress. Schema: [metadata.md](metadata.md) |
| **Plugin fields** | under `custom_fields:` | Stored as WordPress post meta; GK-WP-HC-Plugin builds the nav, breadcrumbs, card grids, home and search from them. This file |

Git It Write also maps `title` to the post title and `taxonomy.category` to
the WordPress category. The category must be this help center's
(`product/config.json` → `category`), or the post lands outside it.

```yaml
---
title: "Agent Sessions"
description: "Run, watch and resume agent sessions in Kepler."
product: Kepler
feature: Agent Sessions
content_type: how-to
audience: developer
plan_required: all
status: preview
last_verified: 2026-11
llms_include: true
tags: [agents, sessions, resume]
# ... the product's Conditional fields (product/PRODUCT.md)
taxonomy:
    category: kepler
custom_fields:
    nav_category: "working-in-kepler"
    nav_label: "Agent Sessions"
    nav_order: 20
    nav_parent: "working-in-kepler"
    page_type: "content"
---
```

Keep the key order: metadata, then `taxonomy`, then `custom_fields`. Indent
with four spaces. Quote any value that contains `:`, `#`, `&` at the start,
or leading/trailing spaces. Copy the style of the sibling pages (quoted or
not, list or comma string) rather than this example.

## Git It Write: never delete, never clear

Git It Write only ever **sets** post meta and only ever **creates or updates**
posts (verified in its code, WORKFLOW.md "What Git It Write does on a branch
switch"):

- **Clear a field with `""`, never by deleting the key.** A deleted key
  keeps its old value on the post. Write `field: ""` (a list may be `[]`);
  the plugin treats both as not set.
- **Renames and archives leave the old post published.** A post is found by
  slug (the file name) across the whole site; a renamed, moved or archived
  file gets a new post or none, and the old one stays live with its nav
  fields. Tell the user: the old post is trashed on staging and unpublished
  (and redirected) at cutover.
- **Rename before adding nav fields.** Otherwise the old post also carries
  nav fields and both appear in the nav.
- **Archive into `_archive/`.** Move a retired page to
  `_archive/<content folder>/ARCHIVED-<name>.md`. Git It Write skips every
  file and folder starting with `_` or `.`; a file name starting with `_` is
  also how to keep a draft unpublished.
- **Slugs are site-wide.** Git It Write matches a file to a post by slug
  across every category. Give a new page (and a new landing page) a
  product-prefixed slug (`kepler-integrations`, not `integrations`) and check
  it is free on production and in the other docs repos before the first
  push: `integrations` is a live Desktop post, and `start-here`,
  `release-notes` and `getting-started` recur.
- **Slugs are lowercase.** WordPress stores `sanitize_title()` of the file
  name: `GL-Commit-Graph.md` is the post `gl-commit-graph`. Every reference
  to a page (`nav_parent`, `nav_also`, `anchor_map`, links) uses the lowercase
  slug; the plugin matches `nav_parent` exactly.
- **Branches.** Redesign work goes on a work branch off `expo`, merged into
  `expo`; never commit redesign work to `main`.

## The `custom_fields` the plugin reads

| Field | Required | Read by | Meaning |
|---|---|---|---|
| `page_type` | on nav pages | template, transforms, nav | `main-index` (the home page, exactly one: `product/config.json` → `home_slug`), `index` (a landing page whose nav children show as cards, at any depth), `content` (everything else). Missing means `content`. |
| `nav_category` | on nav pages | nav, search | Puts the page in the nav and the search index. The key of the page's top-level ancestor (a page slug or a nav-file group key), or its own slug if it is top level (NAV-CONTRACT.md). A page without it is not in the nav. Insights uses fixed section keys instead (its `product/PRODUCT.md`). |
| `nav_order` | on nav pages | nav, card grids | Integer. Sorts siblings ascending, in steps of 10. Ties have no defined order. |
| `nav_label` | on nav pages | H1, nav, breadcrumbs, card title, search | What readers see. Falls back to `title`. |
| `nav_parent` | on nav pages (`""` at the top) | nav nesting, breadcrumbs, cards | The parent's **key**: its lowercase slug (file name without `.md`), or a group or link key from the product nav file (bare; a `group:` prefix is tolerated). Write `""` for a top-level page; never omit the key. |
| `nav_also` | no | nav | Extra placements of the same page: a list of `"<parent>\|<order>\|<label>"` strings, e.g. `["configuration\|5\|Overview"]`. A parent of the page's own slug repeats it as its own first child. |
| `layout` | no | general pipeline, TOC | `settings` turns on settings spec panels where the product has them; `release-notes` collapses the TOC to H2 and shows version pages as cards (patterns.md, "Release notes"). Any other value is an error. |
| `card_icon` | no (Insights: yes) | card grids, home | A [Tabler icon](https://tabler.io/icons) name **without** `ti-`. Fallback: folder / file / external-link by kind. |
| `card_color` | no (Insights: yes) | card grids, home | `purple`, `blue`, `green`, `amber` or `red`. Fallback purple. |
| `card_description` | no (Insights: yes) | card subtitle, search index, home hero lede | One short line with no final period. Fallback: the labels of the page's first children. |
| `entry_title` | no | home `paths` | Makes the page an entry path on its help center's home. |
| `entry_role` | no | home `paths` | The kicker above the title ("Developer", "Jira admin"). Needs `entry_title`. |
| `entry_desc` | no | home `paths` | One line under the title. Needs `entry_title`. |
| `entry_order` | no | home `paths` | Integer; paths sort by it, then by nav position. |
| `home_group` | no | home `cards`, `chips`, `cta`, `links`, `paths` with a group | The card set(s) the page appears in, e.g. `"install"`; a list or comma-separated for several. The groups a home uses are its nav file's `home_blocks` (default: `cta`, `paths`, `install`, `features`, `chips`, `links`). |
| `home_order` | no | the same blocks | Integer; order within the set. |
| `git_hosts` | no | home `facet` | List of `git_hosts` slugs, **mirrored** from the page's top-level host metadata (GIJ Cloud: from `git_host_support`), so the plugin can see it. |
| `anchor_map` | no | anchor redirects | `["<old anchor>\|<target>", ...]` for a page whose sections moved; see patterns.md, "Anchor map". |

Everything the plugin reads must be under `custom_fields:`. A top-level
`nav_order:` is silently dropped by Git It Write and the page falls out of
the nav (the checker reports it). Metadata a home block needs is mirrored
under `custom_fields` with the same value; the top-level key stays.

`hidden` pages (Insights) still need `page_type`, `nav_order` and
`nav_label`. Pages that are not in the nav (no `nav_category`) need no
`custom_fields` at all, but still carry the metadata.

## How the hierarchy is built

- **Nav** (NAV-CONTRACT.md): the pages with a `nav_category`, plus the
  product nav file's label-only groups and links
  (`GK-WP-HC-Plugin/config/products/<key>.json` in GK-WP-HC-Design). Each
  node hangs under its `nav_parent` (or the `parent` of a group or link),
  looked up by key across pages, groups and links; siblings sort by order.
  The tree renders to `max_depth` levels (5); deeper pages are reported and
  shown at level 5. `nav_also` adds extra placements.
- **Breadcrumbs**: Home → each ancestor up the `nav_parent` chain → this page.
  Groups show as plain text.
- **Card grid on an `index` page**: its nav children (pages naming it in
  `nav_parent`, `nav_also` placements under it, nav-file links under it); a
  nav-file group under it becomes a titled card section.
- **Home** (`main-index`): built from blocks (patterns.md, "Generic home").
- **Things a Markdown file cannot say**: a label-only group, a nav link to
  something that is not a page of this repo, the home's block list and
  non-page home cards. They live in the product nav file, which is plugin
  work in GK-WP-HC-Design.
