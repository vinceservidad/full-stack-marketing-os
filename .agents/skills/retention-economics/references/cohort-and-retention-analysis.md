# Cohort and Retention Analysis

Groups customers by a shared starting point and tracks their behavior over time. The unit of analysis that makes lifetime value, payback, and churn meaningful — comparing point-in-time snapshots across cohorts of different age produces false trends.

## Cohort definition

Define by acquisition period (week, month, or quarter) and, when segmenting, by acquisition channel, campaign, offer, or first-purchase category. State the definition before building any curve; changing it mid-analysis invalidates the comparison.

## Curve construction

1. Index each cohort's behavior by periods-since-acquisition (period 0, 1, 2, ...), not by calendar date, so cohorts of different starting dates align on the same axis.
2. Compute the metric of interest per period: active customers, repeat-purchase rate, cumulative revenue, retained subscribers.
3. Mark each cohort's maturity — how many periods of data actually exist for it. A cohort acquired last month has no period-11 data; do not plot a projected value as if observed.
4. Distinguish retention (customers still active or transacting) from repeat-purchase rate (customers who transacted again, which can exceed one per customer) — do not use them interchangeably.

## Churn and retention

For subscription and recurring-revenue models, define churn precisely: logo churn (accounts lost) versus revenue churn (revenue lost, which can be negative when expansion exceeds loss). Report both; a business can retain most logos while losing revenue, or the reverse.

For ecommerce and lead generation without a subscription mechanism, use repeat-purchase rate or reactivation rate rather than churn, and state the inactivity window used to declare a customer lapsed.

## Rules

- Never plot or report a period beyond a cohort's observed maturity without explicitly marking it as projected.
- Do not average retention across cohorts of different age; a blend of mature and immature cohorts understates or overstates the current trend depending on which dominates.
- A retention improvement observed in one cohort is a hypothesis until it replicates in the next; do not report it as an established trend from a single cohort.
- State the inactivity or lapse window used for any repeat-purchase or reactivation definition — a 30-day window and a 180-day window on the same data produce different conclusions.
- Revenue churn and logo churn answer different questions; report the one relevant to the decision and do not substitute one for the other.
- Cohort curves inform strategy; they do not authorize a scaling change on their own. Route through `optimization-scaling` for that decision.
