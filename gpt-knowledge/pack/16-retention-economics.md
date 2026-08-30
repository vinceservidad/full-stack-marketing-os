<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Retention and Customer Economics

## Skill: $retention-economics

**Use when:** Model customer lifetime value, payback period, cohort retention, and repeat-purchase or renewal economics using realized revenue and margin; not for single-period efficiency metrics or platform ROAS.

Classify each model, curve, or projection with `KNOWLEDGE-TAXONOMY.md`. A cohort curve is a pattern from observed customers, not a guarantee for future ones. A projected lifetime value is a model output, not a business outcome, until realized revenue confirms it.

### Context

Business model (ecommerce, subscription, lead generation, marketplace) and its typical repeat or renewal cycle; source-of-truth system for customer-level revenue; cohort definition (acquisition period, channel, first-purchase or first-conversion date); revenue basis and profit level per `$marketing-intake`; refund and cancellation treatment; observation window relative to the business's typical payback and lifetime; and whether the request needs a historical (realized) or predictive (modeled) figure.

Do not model lifetime value or payback without the cost and profit definitions `$marketing-intake` requires. A model built on an undefined profit level is unusable the moment it is compared against anything.

### Method

1. Fix the cohort definition and observation window before computing anything. State whether the window covers full maturity or is truncated.
2. Choose historical (realized, from actual cohort revenue to date) or predictive (modeled, extrapolating from partial data) and never blend them silently.
3. Compute at the correct profit level — gross, contribution after media, or contribution after variable costs — and name it in every output.
4. Build the retention or renewal curve from the cohort, not from an average across cohorts of different age.
5. Compute payback period against the same profit level used for cost of acquisition; state whether payback is measured in revenue or contribution.
6. Separate new-customer economics from returning-customer economics; do not blend acquisition cost into a blended lifetime figure that then hides unprofitable acquisition.
7. State the confidence interval or the immaturity discount on any predictive figure, and what evidence would tighten it.

Read Customer lifetime value for LTV method and pitfalls. Read Payback period for acquisition payback. Read Cohort and retention analysis for curve construction and retention/churn. Read Lead-to-revenue cohorts for lead-generation and long sales-cycle businesses.

### Rules

- Never present a predictive lifetime value as realized revenue, and never compare a predictive figure from one model against a realized figure from another cohort.
- Never compute lifetime value or payback without a named profit level and its included costs.
- Do not extrapolate a cohort curve past its observed maturity without stating the extrapolation and its assumption.
- Do not average retention or lifetime value across cohorts of materially different age, channel, or acquisition offer without stating that the blend can mask a declining or improving trend.
- A single strong cohort does not establish a durable pattern; require replication across at least two comparable cohorts before treating a curve as decision-grade for scaling.
- Do not use predictive lifetime value alone to authorize a scaling decision; it must clear the `optimization-scaling` proof standard and marginal economics gates.
- Refunds, cancellations, chargebacks, and returns reduce realized revenue in the period they occur; do not net them out of an earlier period to smooth a curve.
- Do not treat platform-attributed acquisition cost as the true acquisition cost; use the business source of truth.

### Output

Cohort economics: cohort definition and window; historical or predictive label; profit level; retention or renewal curve with maturity state; lifetime value at stated horizons; payback period; new versus returning economics; confidence or immaturity discount; comparison to acquisition cost; exact status.

### QA

Confirm the cohort definition and window are stated, historical and predictive figures are never blended, the profit level is named and consistent with acquisition cost, curves are not averaged across incompatible cohorts, extrapolation past observed maturity is disclosed, and no figure here alone authorizes a scaling change.

### Reference: cohort and retention analysis ($retention-economics)

### Cohort and Retention Analysis

Groups customers by a shared starting point and tracks their behavior over time. The unit of analysis that makes lifetime value, payback, and churn meaningful — comparing point-in-time snapshots across cohorts of different age produces false trends.

#### Cohort definition

Define by acquisition period (week, month, or quarter) and, when segmenting, by acquisition channel, campaign, offer, or first-purchase category. State the definition before building any curve; changing it mid-analysis invalidates the comparison.

#### Curve construction

1. Index each cohort's behavior by periods-since-acquisition (period 0, 1, 2, ...), not by calendar date, so cohorts of different starting dates align on the same axis.
2. Compute the metric of interest per period: active customers, repeat-purchase rate, cumulative revenue, retained subscribers.
3. Mark each cohort's maturity — how many periods of data actually exist for it. A cohort acquired last month has no period-11 data; do not plot a projected value as if observed.
4. Distinguish retention (customers still active or transacting) from repeat-purchase rate (customers who transacted again, which can exceed one per customer) — do not use them interchangeably.

#### Churn and retention

For subscription and recurring-revenue models, define churn precisely: logo churn (accounts lost) versus revenue churn (revenue lost, which can be negative when expansion exceeds loss). Report both; a business can retain most logos while losing revenue, or the reverse.

For ecommerce and lead generation without a subscription mechanism, use repeat-purchase rate or reactivation rate rather than churn, and state the inactivity window used to declare a customer lapsed.

#### Rules

- Never plot or report a period beyond a cohort's observed maturity without explicitly marking it as projected.
- Do not average retention across cohorts of different age; a blend of mature and immature cohorts understates or overstates the current trend depending on which dominates.
- A retention improvement observed in one cohort is a hypothesis until it replicates in the next; do not report it as an established trend from a single cohort.
- State the inactivity or lapse window used for any repeat-purchase or reactivation definition — a 30-day window and a 180-day window on the same data produce different conclusions.
- Revenue churn and logo churn answer different questions; report the one relevant to the decision and do not substitute one for the other.
- Cohort curves inform strategy; they do not authorize a scaling change on their own. Route through `optimization-scaling` for that decision.

### Reference: customer lifetime value ($retention-economics)

### Customer Lifetime Value

The projected or realized profit a customer generates over the relationship, at a stated profit level. Not a single number — always paired with a horizon, a profit level, and a historical-versus-predictive label.

#### Variants, and when each applies

| Variant | Definition | Use for |
|---|---|---|
| Historical (realized) lifetime value | Actual cumulative profit from a cohort to date | Reporting what happened; the only variant that can stand alone as a business outcome |
| Predictive lifetime value | Modeled projection from partial cohort data or a fitted curve | Forward planning, with its confidence interval stated |
| Gross lifetime value | Revenue-based, no costs deducted | Top-line scale only; never for acquisition-spend decisions |
| Contribution lifetime value | Revenue minus cost of goods sold and variable costs, before media | Acquisition and payback decisions |
| Contribution-after-media lifetime value | Contribution lifetime value minus acquisition cost | Net customer profitability |

Reserve "lifetime value" alone for ambiguity the reader must resolve; always qualify which variant is being reported.

#### Method

1. Define the cohort: acquisition period, channel or campaign if segmenting, and first-transaction or first-conversion date.
2. Choose the horizon — 30/60/90-day, 12-month, or full projected lifetime — matched to the business's typical repeat cycle. A 30-day horizon on a business with an 18-month repeat cycle understates lifetime value by construction.
3. Sum realized profit per customer at the stated profit level, to the horizon, from the business source of truth.
4. For a predictive figure, fit a retention or spend-decay curve to the observed portion of the cohort and project forward; state the model and its fit quality.
5. Report per-customer lifetime value, not only cohort totals, so it can be compared to per-customer acquisition cost.

#### Common errors

- Comparing a 90-day lifetime value against a payback period measured over 12 months — mismatched horizons produce a false payback conclusion.
- Reporting gross lifetime value against contribution-based acquisition cost, inflating apparent profitability.
- Using a young cohort's early-period lifetime value as if it were mature, before repeat behavior has had time to occur.
- Blending predictive and historical figures into one number without disclosure.
- Computing an average lifetime value across channels with different retention shapes and using it to justify budget for the worst-retaining channel.

#### Rules

- State horizon, profit level, and historical/predictive status every time the figure is reported.
- A predictive lifetime value used to justify scaling must meet the `optimization-scaling` proof standard; a single cohort's projection is not sufficient on its own.
- Do not update a historical lifetime value retroactively without recording the revision and its cause.

### Reference: lead to revenue cohorts ($retention-economics)

### Lead-to-Revenue Cohorts

Extends cohort economics to lead generation and long sales-cycle businesses, where the gap between marketing conversion and realized revenue can be weeks or quarters. Read alongside Cohort and retention analysis.

#### Why lead generation needs a separate method

Ecommerce cohorts mature in days; lead-generation cohorts mature on the sales cycle, which can exceed a typical reporting period. A lead cohort's revenue is systematically incomplete until the cycle closes — treating incomplete cohorts as final understates value and can trigger a premature scale-down of a channel that is actually performing, just not yet realized.

#### Method

1. Cohort by lead-creation date, not by opportunity-creation or close date; cohorting on a later stage survivorship-biases the analysis toward leads that already progressed.
2. Track each cohort through its stages — lead, marketing qualified, sales qualified, opportunity, customer — using the stage definitions `$marketing-intake` recorded, joined from the Customer Relationship Management system.
3. Report cohort revenue only after stating what share of the cohort has reached each stage and what share remains open. An "open" lead is neither won nor lost; do not treat it as either.
4. Compute conversion rate and revenue per lead-cohort period as cycle length increases, and mark the point at which a cohort is judged mature enough for a stable read — typically when the open share has fallen below a stated threshold.
5. Separate pipeline velocity (how fast leads move through stages) from revenue lag (how long until cash or booked revenue appears); a channel can accelerate the first without changing the second, or the reverse.

#### Rules

- Never report a lead cohort's conversion rate or revenue as final while a material share remains open; state the open share alongside any interim figure.
- Do not compare a mature channel's cohort conversion rate against an immature cohort from a newer channel; normalize for cycle stage first.
- A sudden apparent drop in lead quality in the most recent cohorts is often incomplete maturation, not a real decline; check open share before concluding quality fell.
- Join marketing source to Customer Relationship Management outcome at the lead level, not at an aggregate channel level, so misattributed or unsourced leads do not silently inflate or deflate a channel's realized cohort revenue.
- A lead-to-revenue conclusion used for a scaling decision must satisfy the `optimization-scaling` conversion-lag and marginal-evidence gates in addition to this cohort's own maturity threshold.

### Reference: payback period ($retention-economics)

### Payback Period

The time for cumulative customer profit to recover acquisition cost, at a stated profit level. Governs how long capital is at risk per customer and how fast a scaling program can be reinvested.

#### Method

1. Fix the profit level — contribution before or after variable costs — and use the identical level on both sides: acquisition cost and cumulative customer profit.
2. Use the business source of truth for acquisition cost, not platform-attributed cost per acquisition; if only platform cost is available, label the payback figure as platform-attributed and provisional.
3. Track cumulative contribution per customer (or per cohort, divided by cohort size) period by period from acquisition date.
4. Payback period is the period in which cumulative contribution first exceeds acquisition cost. Report it in the same time unit the business plans around — days, weeks, or months.
5. Where payback varies materially by channel, offer, or segment, report it segmented; a blended payback period can mask a channel that never pays back within an acceptable window.

#### Revenue payback versus contribution payback

Revenue payback (cumulative revenue exceeds acquisition cost) is faster and less meaningful; it ignores cost of goods sold and fulfillment. Contribution payback is the decision-relevant figure for scaling and cash planning. Always label which is reported, and prefer contribution payback when a scaling decision depends on it.

#### Rules

- Do not report payback period without stating the profit level used.
- Do not use platform-attributed acquisition cost as the numerator for a scaling decision without labeling it provisional per the causal evidence ladder — platform-attributed cost is not a verified acquisition cost.
- A payback period shorter than the observation window is more reliable than one that requires extrapolation past the data available; state which applies.
- Do not compare payback periods across channels with different cohort ages without normalizing for maturity.
- Cash payback and accounting payback can differ when revenue is recognized on delivery, subscription billing, or installment terms; state which convention is used.
