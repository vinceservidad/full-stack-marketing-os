# Incrementality Method Selector

Selects how to measure incremental effect. There is no universally correct method; the constraint set decides.

## Inputs required before selecting

Decision being made and cost of being wrong; required evidence level from the causal ladder; spend under test; expected effect size; available unit of randomization; geographic or audience independence; sample size and power; contamination risk; seasonality and known events; conversion lag; platform availability of the mechanism; ability to hold a control for the full period; and who authorizes the holdback.

Absent inputs are recorded `unknown` by `$marketing-intake`. Do not select a method by defaulting an unknown.

## Selection

| Condition | Method | Reference |
|---|---|---|
| Platform supports randomized user split and the audience can be held out | User-level holdout | [Holdouts](holdout-experiments.md) |
| Users cannot be split cleanly, but regions are independent and numerous enough | Geo experiment or matched-market test | [Geo experiments](geo-experiments.md) |
| Platform offers a native randomized lift mechanism and its design is acceptable | Platform lift study | [Lift studies](platform-lift-studies.md) |
| Effect is short-lived and treatment can alternate on a schedule | Switchback | [Geo experiments](geo-experiments.md) |
| No control is possible, but a comparable untreated series exists | Synthetic control or interrupted time series (C3) | [Geo experiments](geo-experiments.md) |
| Question is long-horizon cross-channel allocation, not a single change | Marketing Mix Modeling (C2) | [Marketing Mix Modeling](marketing-mix-modeling.md) |
| Several imperfect sources exist and no single test is decisive | Triangulate | [Triangulation](measurement-triangulation.md) |

## Disqualifiers

Do not run the test if any holds — fix the condition or lower the decision's commitment instead:

- Measurement integrity is unresolved. A causal test inherits every collection defect beneath it.
- The control cannot be held for the full period plus conversion lag.
- Expected effect is smaller than the design can detect; the likely result is an uninformative null read as "no effect."
- Treatment and control cannot be kept separate — shared audiences, overlapping geographies, cross-device users, brand spillover.
- A promotion, launch, outage, or seasonal peak overlaps the window and cannot be excluded.
- The holdback's revenue cost exceeds the value of the decision it informs.

## Rules

- Power the test before running it. State minimum detectable effect, duration, and required volume in advance; a test that cannot detect the effect it seeks is not evidence.
- Fix the stopping rule and primary metric before launch. Do not stop early on a favorable read, and do not switch the primary metric after seeing results.
- One primary metric, defined by `$marketing-intake` before launch. Secondary metrics are supporting only.
- Measure the business outcome, not the platform-attributed proxy.
- Include the full conversion lag in the measurement window.
- A null result is a result. Report it with its minimum detectable effect so absence of evidence is not read as evidence of absence.
- Record cost: the holdback's forgone revenue is part of the test's price and belongs in the decision.
