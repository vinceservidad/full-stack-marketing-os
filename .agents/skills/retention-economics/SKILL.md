---
name: retention-economics
description: Model customer lifetime value, payback period, cohort retention, and repeat-purchase or renewal economics using realized revenue and margin; not for single-period efficiency metrics, platform ROAS, or setting pricing architecture.
---

# Retention Economics

Classify each model, curve, or projection with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A cohort curve is a pattern from observed customers, not a guarantee for future ones. A projected lifetime value is a model output, not a business outcome, until realized revenue confirms it.

## Context

Business model (ecommerce, subscription, lead generation, marketplace) and its typical repeat or renewal cycle; source-of-truth system for customer-level revenue; cohort definition (acquisition period, channel, first-purchase or first-conversion date); current pricing/package state where it changes the commercial terms; revenue basis and profit level per [`$marketing-intake`](../marketing-intake/); refund and cancellation treatment; observation window relative to the business's typical payback and lifetime; and whether the request needs a historical (realized) or predictive (modeled) figure.

Do not model lifetime value or payback without the cost and profit definitions `$marketing-intake` requires. A model built on an undefined profit level is unusable the moment it is compared against anything.

## Method

1. Fix the cohort definition and observation window before computing anything. State whether the window covers full maturity or is truncated.
2. Choose historical (realized, from actual cohort revenue to date) or predictive (modeled, extrapolating from partial data) and never blend them silently.
3. Compute at the correct profit level — gross, contribution after media, or contribution after variable costs — and name it in every output.
4. Build the retention or renewal curve from the cohort, not from an average across cohorts of different age.
5. Treat material pricing, package, payment-model, or acquisition-offer changes as possible cohort boundaries. Compare pre-change and post-change cohorts separately before pooling them.
6. Compute payback period against the same profit level used for cost of acquisition; state whether payback is measured in revenue or contribution.
7. Separate new-customer economics from returning-customer economics; do not blend acquisition cost into a blended lifetime figure that then hides unprofitable acquisition.
8. State the confidence interval or the immaturity discount on any predictive figure, and what evidence would tighten it.

Read [Customer lifetime value](references/customer-lifetime-value.md) for LTV method and pitfalls. Read [Payback period](references/payback-period.md) for acquisition payback. Read [Cohort and retention analysis](references/cohort-and-retention-analysis.md) for curve construction and retention/churn. Read [Lead-to-revenue cohorts](references/lead-to-revenue-cohorts.md) for lead-generation and long sales-cycle businesses.

## Rules

- Never present a predictive lifetime value as realized revenue, and never compare a predictive figure from one model against a realized figure from another cohort.
- Never compute lifetime value or payback without a named profit level and its included costs.
- Do not extrapolate a cohort curve past its observed maturity without stating the extrapolation and its assumption.
- Do not average retention or lifetime value across cohorts of materially different age, channel, acquisition offer, price, package, or payment model without stating that the blend can mask a declining or improving trend.
- A single strong cohort does not establish a durable pattern; require replication across at least two comparable cohorts before treating a curve as decision-grade for scaling.
- Do not use predictive lifetime value alone to authorize a pricing or scaling decision. `$pricing-monetization` owns pricing structure; `$optimization-scaling` owns scaling and applies its own proof standard and marginal-economics gates.
- Refunds, cancellations, chargebacks, and returns reduce realized revenue in the period they occur; do not net them out of an earlier period to smooth a curve.
- Do not treat platform-attributed acquisition cost as the true acquisition cost; use the business source of truth.

## Output

Cohort economics: cohort definition and window; pricing/package state where relevant; historical or predictive label; profit level; retention or renewal curve with maturity state; lifetime value at stated horizons; payback period; new versus returning economics; confidence or immaturity discount; comparison to acquisition cost; exact status.

## QA

Confirm the cohort definition and window are stated, material pricing/package changes are not silently pooled, historical and predictive figures are never blended, the profit level is named and consistent with acquisition cost, curves are not averaged across incompatible cohorts, extrapolation past observed maturity is disclosed, and no figure here alone authorizes a pricing or scaling change.
