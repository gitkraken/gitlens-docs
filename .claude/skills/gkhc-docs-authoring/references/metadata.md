# Metadata (top-level front matter)

The source is `redesign-expansion/FRONTMATTER-SCHEMA.md` in GK-WP-HC-Design.
`scripts/schema.json` is generated from it, and `check_pages.py` enforces it:
**a metadata error fails CI** (exit 1, decided 2026-11-09). This help
center's Conditional fields, constants and plan names are in
`product/config.json` → `metadata` and summarised in `product/PRODUCT.md`.

Metadata is not stored in WordPress (Git It Write keeps only `custom_fields`),
so adding or fixing it changes nothing on the site. It feeds `llms.txt`, the
docs audit and agents.

## Core fields: every page, every help center

| Field | Type | What it says |
|---|---|---|
| `title` | string | The page H1 (the plugin prints it; never write `# ` in the body) |
| `description` | string, ≤ 160 chars | Meta and llms summary |
| `product` | string | The product's display name: this help center's constant. Another product's name only on a page really about that product (WARN) |
| `feature` | string | The feature the page covers, title case; reuse an existing value |
| `content_type` | enum | `home`, `overview`, `how-to`, `concept`, `reference`, `troubleshooting`, `faq`, `release-notes`, `install`, `integration`, `security`, `policy`, `form`, `api-reference`, `admin` |
| `audience` | enum | `all`, `developer`, `team-lead`, `admin`, `enterprise-admin`, `buyer`, `reseller`, `agent` |
| `plan_required` | list (a comma string is accepted) | The lowest plans that can use it, from this help center's plan names; `[all]` when unrestricted |
| `status` | enum | `GA`, `preview`, `beta`, `deprecated`, `legacy`, `draft` |
| `last_verified` | `YYYY-MM` | When the content was last substantively checked. Adding metadata is not substantive: don't bump it |
| `llms_include` | `true` / `false`, unquoted | `true` for nav pages; `false` for templates, forms, tests, pages outside the nav |
| `tags` | list | 3-8 lowercase search keywords |

## Conditional fields: where the product has the dimension

When a field applies to the product, every page carries it (`[n/a]` or `[]`
where it doesn't matter). `product/config.json` → `metadata.conditional`
lists them; `metadata.aliases` names a legacy key kept in its place by
decision (GIJ Cloud `git_host_support` for `git_hosts`, gitkraken.dev
`cloud_only` for `hosted_variant`).

| Field | Type | What it says |
|---|---|---|
| `os_support` | list | Operating systems; `[n/a]` for account/web pages |
| `git_hosts` | list | Hosts the page applies to: `generic`, `n/a`, `github`, `github-enterprise`, `gitlab`, `gitlab-self-managed`, `bitbucket`, `bitbucket-data-center`, `azure-devops`, `azure-devops-server`, `aws-codecommit`, `gerrit`, `beanstalk`, `bonobo`, `gitblit`, `gitolite`, `windows-network-share`. Open vocabulary: a new host warns until FRONTMATTER-SCHEMA.md lists it. Display names ("GitLab Self-Managed") are compared in slug form |
| `integrations` | list | Third-party integrations; `[]` when none |
| `hosted_variant` | enum | `cloud`, `self-hosted`, `both` |
| `deployment` | constant | `Jira Cloud` / `Jira Data Center` |
| `role_required` | list (comma string accepted) | The role needed: `Jira Administrator`, `Owner`, `Admin`, `Billing Contact`, `Server Administrator`; `[all]` when any user can |
| `version_required` | string | Minimum app version; `all` otherwise |
| `og_image` | path | Social preview image, only where a page already has one |

## Rules

- **Add only.** Keep existing fields and values exactly as written (style,
  comma strings, display names). The one exception: a value the page clearly
  contradicts, or a value outside the vocabulary, is a real error: fix it in
  its own small PR.
- **Never delete a key to clear it.** Write `""` (or `[]`).
- **Don't bump `last_verified`** or the `<kbd>Last updated</kbd>` line for
  metadata-only changes.
- A top-level key the schema doesn't know warns: either it belongs under
  `custom_fields:`, or it is a product-specific key that `product/config.json`
  should list in `metadata.extra_fields`.
- **Mirror what the plugin needs.** A home block that reads a metadata value
  (GIJ Cloud's host grid) needs it under `custom_fields:` too, same value
  (frontmatter.md, `git_hosts`). The checker warns when the mirror differs.

## What the checker reports

| Level | Finding |
|---|---|
| ERROR | a Core or Conditional field missing or empty (an empty list only where `[]` is allowed); a wrong type (list vs value, unquoted bool, `YYYY-MM`); an enum value or plan outside the vocabulary; a constant (`deployment`) that differs |
| WARN | `product` differs from the constant; a `git_hosts` value not in the open vocabulary; an unknown top-level key; a `custom_fields.git_hosts` mirror that differs |

`metadata.check` in `product/config.json` is `error` for the redesign help
centers and `off` where the schema doesn't apply yet (Insights).
`metadata.plan_required_vocabulary: "warn"` lets plan values outside the
product's list through as warnings (default `error`). Outside metadata,
`checks.missing_image: "warn"` does the same for images missing from
`_images/`.
