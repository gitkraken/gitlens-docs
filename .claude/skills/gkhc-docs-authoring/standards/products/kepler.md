<!-- Synced from gk-docs-automation docs/products/kepler.md by GK-WP-HC-Design skills/standards_sync.py. Edit it there. -->

## Detail level: what the reader meets, and the one action (reviewer, 2026-11-04)

The Kepler-Docs reviewer's feedback on PR #49 was "too much detail", with this
example from Getting Started: "a guided start takes you through 2 steps. It
fills the whole window, without the top bar … Existing users also see the
guided start once, with a *Welcome back* note…" → "After you sign in, a guided
start walks you through setup. To skip it at any point, click **I'll explore on
my own**." Audits read the diff, so prose drifts toward documenting everything
the code does. Write at the reviewer's level from the first draft, and put this
in every prose and editorial brief:

- Keep the control's name, where it is, what it does, and any limit that changes
  what the reader does.
- Cut exhaustive lists of states, messages, buttons, defaults and counts (keep the
  2–3 the reader acts on); quoted UI strings outside troubleshooting; edge cases a
  typical user will not hit; timing, ordering and how it works; layout narration;
  repetition across sections (say it once, link to it).
- Tables: one short sentence per cell.

The tightening pass on PR #49 (Kepler-Docs 19ab7c2) removed about a third of the
audit's added prose across 26 pages without losing a user-facing fact.

## Not documented on purpose (HOUSE-7, 2026-11-02)

The help center documents what a Kepler user can see, do or affect
(WRITING-STANDARDS.md HOUSE-7). Kepler's source makes a lot of its internals
easy to describe, and two audits did. Kepler-Docs #48 removed them from 20 of 29
pages; do not add them back, however a diff presents them. The syntax ones are
lint errors (H-96, `internalPatterns` in `src/core/registry.ts`).

| Internal | What the page says instead |
|---|---|
| Settings hash routes and anchors (`/settings/<page>#<section>`, `setting-<id>`), `kepler://settings[/<id>]` links | Clicking a setting Ask Kepler names opens it in Settings; a link or search result highlights the setting, or says why it is not shown |
| `@id:` settings search | Search by name (no UI shows a setting id) |
| `kepler://session?agent=&id=&cwd=` | Nothing (no UI produces it). **Copy session link** / **Copy task link** and the `kepler://task/<id>` and `kepler://session/<id>` they copy are user-facing and stay |
| `host=` link parameter | A link copied in a window on a remote machine opens on that machine |
| Remote-server layers, cache paths, architecture tokens, manifest diff; health-check intervals, retry counts, backoff; tunnels, ports, WSL passthrough | The first connection downloads the server; later updates download only what changed; the chip reads **Reconnecting…** and Kepler retries; `~/.kepler-server` (users clean it up by hand) |
| Editor command-line arguments (`--remote ssh-remote+…`), agent launch flags (`--acp`, `agent stdio`, `agy_acp_server`), Pi/OpenCode injection, OSC 7501 | Which editors open remote folders over SSH/WSL; which agents run in Chat or Terminal; what an agent gets in Terminal mode |
| Provider capability lists, facet logic, `/connect`, link-matching passes and precedence, auto-attach rule table | One line each: which providers appear in which filters; Connect opens GitKraken's site and returns you; what gets attached and that Kepler never removes a link |
| Internal state names (attention/active/idle/errored/inactive), id prefixes (`task:`, `session:`…), MCP tool parameters (`refresh:true`, `limit:1`), storage and fallback logic, layout constants, design rationale, legacy shortcuts | The visible outcome, or nothing |

A change in this list gets `nothing` ("no user-visible surface") at the
finding stage: `finding add` refuses an actionable verdict without
`--user-surface`. Findings that recorded the settings links and anchors, and the
session-agent link, are superseded by `v0.16.0:settings-links-and-anchors-not-user-facing`
and `v0.15.0:session-agent-link-not-user-facing`.

