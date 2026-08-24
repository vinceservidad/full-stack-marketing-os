# Budget and Outcome Pacing

Tracks spend and outcomes against plan within a period, and reforecasts when variance appears. An operational-control process, distinct from the economic models in `$retention-economics` — pacing asks whether the current period is on track; lifetime value and payback ask whether a customer relationship is profitable.

## What to track

Spend-to-plan variance by period-to-date, with the plan's own seasonality curve rather than a straight-line daily average — most accounts do not spend evenly across a month.

Outcome-to-plan variance for the primary business outcome, at the source-of-truth profit level, not a platform-attributed proxy.

Time remaining in the period versus budget or outcome remaining, expressed as required daily run-rate to hit plan.

## Method

1. Establish the plan's expected spend and outcome curve for the period, not just its total — a plan flat across the month reads as behind-pace in a business with a weekend or end-of-month skew.
2. Compare actual to planned at the current point in the period, in both spend and outcome, separately. Spend can be on-pace while outcome is not, and the reverse.
3. Attribute variance to a cause before recommending a response: demand shortfall, delivery or auction pressure, a tracking defect, a promotion, a capacity constraint, or a genuine change in performance. An unattributed variance should not trigger a budget change.
4. State the reforecast: given current pace and its cause, what the period is now expected to deliver, and by when that becomes clear enough to act on.
5. Distinguish a pacing correction (spend adjusted to hit an already-approved period plan) from a scaling decision (increasing the plan itself). Pacing corrections within an approved budget do not require new scaling authorization; changing the plan does.

## Rules

- Do not correct pacing by raising budget before attributing the variance to a cause. A demand shortfall will not be fixed by more budget; a delivery constraint might be.
- Do not treat early-period variance as decisive. State the point in the period at which the variance becomes statistically meaningful given typical day-of-week and conversion-lag noise.
- Outcome pacing must use the source-of-truth definition from `$marketing-intake`; do not pace against a platform-reported conversion count that has not been reconciled.
- A pacing correction is bounded by the already-approved plan. Any correction that would exceed the approved budget or period is a scaling decision and requires the `optimization-scaling` gates and explicit approval, not a pacing note.
- Reforecast on a stated cadence appropriate to the business's decision cycle; do not reforecast so frequently that noise is mistaken for a trend.
- Record every reforecast with its date, cause, and resulting revised expectation, so a pattern of repeated reforecasting itself becomes visible as a signal.

## Output

Plan curve; actual-to-plan variance in spend and outcome, separately; attributed cause; required run-rate to close the gap; reforecast with date and cause; whether the situation calls for a pacing correction within the approved plan or a scaling decision requiring new authorization; exact status.
