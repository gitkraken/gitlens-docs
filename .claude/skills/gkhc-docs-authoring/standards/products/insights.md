<!-- Synced from gk-docs-automation docs/products/insights.md by GK-WP-HC-Design skills/standards_sync.py. Edit it there. -->

## Disclosure standard — how much detail the docs publish (measured 2026-09-28)

Some calculations are proprietary and deliberately left out of the help
center; what the docs say now is the safe side of the line. Derived by
comparing every documented metric against its implementation
(insights-service `db/repositories/analytics/*`, gitkraken.dev
`src/features/ai-adoption/*`) and the product's own tooltips. Expo and live
disclose the same content (expo only dropped an internal ticket id).

**Publish (the docs already do, or the product shows it to every customer):**
- What each metric is for, the signals it uses, and which way each pushes it.
- The *shape* of each formula — "a weighted composite of adoption, autonomy
  and output", with the terms named — and worked examples.
- Every admin setting: name, UI label, default, range, effect. Settings the
  Settings UI exposes but the docs lack (working hours per week, cycle-time
  cap in days, exclude bot reviews, per-provider weights) are safe to add.
- Thresholds that define categories a customer sees: tier cut-offs
  (25/55/80), the 10-tool-call autonomy threshold, effort anchors, the
  AI-correlation window, data start dates, sync lag.
- Normalisation *named*: "capped at your org's 90th percentile, org-wide,
  per window".
- Edge cases by outcome ("a developer on PTO for the whole window shows as
  On PTO"), never by mechanism.
- Anything the product's own help text states: the in-app tooltips are the
  outer bound of what is safe (they say "median", "per working week",
  "PRs ≤ 30 days", show per-provider weights and the formula strip).
- Editorial "how to read it" guidance and healthy ranges — written, not
  derived from code.

**Never publish (in code, in no doc, would tempt a writer reading the diff):**
- Hard-coded internal weights and constants: the four adoption-factor
  weights, percentile method and floors, cohort minimums and small-cohort
  fallbacks, `MinWorkingWeeks`, the Devin synthetic session value, Copilot
  and Cursor scoring bands.
- LLM classifier internals: vendor, model, prompt text, rubric version
  string, token limits, retry counts.
- Attribution algorithms beyond behaviour: CFR's release windowing and team
  union, lead-time matching mechanics.
- Calibration figures (conversion factors, accuracy percentages) unless
  already public.
- Implementation identifiers: table and column names, SQL (`COALESCE`,
  `LATERAL`, `EXISTS`), Go/TS type and function names, env vars, internal
  endpoints, pipeline/worker names and cadences, internal ticket ids, and
  settings that exist in code but not in the Settings UI (`merged_pr_weight`,
  `bug_escape_window_days`, …).

**Applying it when code and docs disagree.** Many documented values have
drifted from the code (Maturity Factor default 0.75 vs 1.0; a Cursor boost
env var that no longer exists, replaced by per-provider weights; mean vs
median for cycle time, lead time and MTTR; correlation window 60 vs 30
minutes; Output Score as a sum vs a per-working-week rate; CapEx and Spend
methods). Correct a drifted value **only to what the product shows** — its
tooltip or Settings UI — cite that file as evidence, and describe the new
behaviour at the same level of detail as the text it replaces. Never
"correct" toward a number that only the backend knows. Record drift whose
correct value is not UI-visible as a finding for a human, not a prose edit.

**Rulings (Viz, 2026-10-15):**
1. Adoption-factor weights (35/25/25/15): **publish** (revised 2026-10-15,
   superseding an earlier "withhold" the same day). The Developers page
   formula card shows them to every customer, and the docs' sandbox claimed
   equal weights. General rule from the same ruling: where the docs already
   publish a figure that the code has since changed, update it to the
   current value — prose *and* the interactive sandboxes.
2. Existing over-disclosure (table/column names, SQL keywords, env vars such
   as `SCORE_SECONDARY_BOOST`, `JIRA_CUSTOMER_BUG_FIELD_ID`,
   `DEMO_MODE=stellar|launchpad|atlas`, worker cadences, accuracy figures,
   `EffortScoreRubricVersion`): **not approved for cleanup** in this audit —
   leave as-is; do not add more.
3. Drift: **approved** — correct drifted values to what the UI shows
   (tooltip / Settings UI cited as evidence); backend-only drift is a
   finding for a human.

