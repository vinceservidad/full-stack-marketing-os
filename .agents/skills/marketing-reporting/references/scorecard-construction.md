# Scorecard Construction

Builds the comparable, decision-grade table a cross-channel report is built around. The scorecard is where mismatched definitions most often slip into a report unnoticed — one channel's "conversion" is not another's.

## Method

1. Name the primary business outcome once, at the profit level and revenue basis `$marketing-intake` recorded, and use it consistently for every channel and every period shown.
2. For each row: current value, comparison value, absolute delta, relative delta, target (if one exists), and the exact metric definition — source system, counting rule, attribution window.
3. Where a channel's native metric differs from the business outcome (platform ROAS versus contribution margin, lead volume versus qualified pipeline), show both, labeled, rather than presenting the platform metric as the outcome.
4. Mark each row's evidence state per the intake evidence ladder — `observed`, `reconciled`, `verified` — visibly, not only in a footnote a reader will skip.
5. Where a period comparison is invalid per `$marketing-intake`'s comparability check (definition changed, promotion overlapped, incomplete period), mark the row rather than showing a misleading delta.

## Rules

- One profit level and one revenue basis per scorecard. Switching mid-table to make a number look better is a definitional violation, not a formatting choice.
- Do not compute a blended or portfolio-level total by summing rows whose underlying definitions differ; reconcile first or show the components unsummed.
- A target without a stated source (business plan, prior period, industry reference) is not a target — label it as an unverified benchmark or omit it.
- Do not backfill a missing comparison period with an estimate; mark it unavailable.
- Currency and timezone must match across every row in a single scorecard; state the conversion basis if they do not natively.
