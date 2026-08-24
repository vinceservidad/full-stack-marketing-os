# Customer Lifetime Value

The projected or realized profit a customer generates over the relationship, at a stated profit level. Not a single number — always paired with a horizon, a profit level, and a historical-versus-predictive label.

## Variants, and when each applies

| Variant | Definition | Use for |
|---|---|---|
| Historical (realized) lifetime value | Actual cumulative profit from a cohort to date | Reporting what happened; the only variant that can stand alone as a business outcome |
| Predictive lifetime value | Modeled projection from partial cohort data or a fitted curve | Forward planning, with its confidence interval stated |
| Gross lifetime value | Revenue-based, no costs deducted | Top-line scale only; never for acquisition-spend decisions |
| Contribution lifetime value | Revenue minus cost of goods sold and variable costs, before media | Acquisition and payback decisions |
| Contribution-after-media lifetime value | Contribution lifetime value minus acquisition cost | Net customer profitability |

Reserve "lifetime value" alone for ambiguity the reader must resolve; always qualify which variant is being reported.

## Method

1. Define the cohort: acquisition period, channel or campaign if segmenting, and first-transaction or first-conversion date.
2. Choose the horizon — 30/60/90-day, 12-month, or full projected lifetime — matched to the business's typical repeat cycle. A 30-day horizon on a business with an 18-month repeat cycle understates lifetime value by construction.
3. Sum realized profit per customer at the stated profit level, to the horizon, from the business source of truth.
4. For a predictive figure, fit a retention or spend-decay curve to the observed portion of the cohort and project forward; state the model and its fit quality.
5. Report per-customer lifetime value, not only cohort totals, so it can be compared to per-customer acquisition cost.

## Common errors

- Comparing a 90-day lifetime value against a payback period measured over 12 months — mismatched horizons produce a false payback conclusion.
- Reporting gross lifetime value against contribution-based acquisition cost, inflating apparent profitability.
- Using a young cohort's early-period lifetime value as if it were mature, before repeat behavior has had time to occur.
- Blending predictive and historical figures into one number without disclosure.
- Computing an average lifetime value across channels with different retention shapes and using it to justify budget for the worst-retaining channel.

## Rules

- State horizon, profit level, and historical/predictive status every time the figure is reported.
- A predictive lifetime value used to justify scaling must meet the `optimization-scaling` proof standard; a single cohort's projection is not sufficient on its own.
- Do not update a historical lifetime value retroactively without recording the revision and its cause.
