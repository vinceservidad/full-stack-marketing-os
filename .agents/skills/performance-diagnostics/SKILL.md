---
name: performance-diagnostics
description: Diagnose why marketing revenue, profit, conversions, spend, or lead quality changed by decomposing metrics and testing competing explanations; use for anomalies and cross-channel questions.
---

# Performance Diagnostics

Classify each decomposition, pattern, hypothesis, model, tactic, or test plan with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A pattern or correlation remains a hypothesis until evidence supports the mechanism.

## Required inputs

For the anomaly being diagnosed, collect or explicitly mark missing:

- the changed business/marketing metric, its exact definition, absolute values, baseline/comparison, date range, timezone, and scope
- source systems and freshness for spend, traffic, conversions, revenue, profit, lead quality, or other relevant outcomes
- attribution/window/lag state and any known tracking, tagging, deduplication, currency, tax, refund, or denominator changes
- useful breakdowns such as channel, campaign, product/service, geography, device, audience, creative, landing page, customer type, and time
- economics needed to interpret the change, including the named profit level and included costs when profitability is in scope
- material business/marketing changes during the period: budgets, bids, targeting, creative, offer, price, promotion, site, inventory, fulfillment, policy, seasonality, or external demand shifts
- the decision or business significance the diagnosis must support, including any urgent containment need
- authorization boundary if the request extends from diagnosis into a live mutation

When structured datasets are supplied, apply [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) and the relevant contract under [`data-contracts/`](../../../data-contracts/). Do not fill missing history, attribution settings, economics, join semantics, or change events with invented assumptions. State which missing input could reverse the diagnosis.

## Method

1. Restate the anomaly with metric definition, absolute values, baseline, date range, scope, and business significance.
2. Validate dataset fitness for the comparison: source, grain, key, timezone, attribution, lag, currency, duplicate/missing events, freshness, denominator changes, revenue/profit basis, and join behavior. Route measurement/reconciliation uncertainty to `$tracking-measurement` when material.
3. Decompose the relevant identity:
   - Ecommerce revenue = traffic × conversion rate × AOV.
   - From gross sales: contribution profit after media = gross sales − discounts − refunds − COGS − variable fulfillment − payment fees − media spend.
   - From net revenue already reflecting discounts/refunds: contribution profit after media = net revenue − COGS − variable fulfillment − payment fees − media spend.
   - Lead value = leads × qualification rate × close rate × realized value.
   - Ad spend = impressions / 1,000 × CPM; conversions = impressions × CTR × post-click conversion rate.
4. Localize the break by channel, campaign, product/service, geography, device, audience, creative, page, and time.
5. Maintain competing hypotheses across measurement, demand, auction, delivery, creative, offer, site, inventory, operations, and mix.
6. Seek disconfirming evidence and rank causes by evidence strength and estimated contribution.

## Rules

- Correlation and timing are clues, not proof.
- Do not compare periods with different promotions, weekday mix, attribution maturity, inventory, dataset grain, or revenue basis without adjustment/disclosure.
- Separate observed fact, inference, and recommended test.
- Never use “profit” without naming the level and included costs. Never subtract discounts or refunds twice.
- Do not aggregate platform-attributed values across channels and call the sum business revenue.
- Never let one-to-many joins duplicate spend, revenue, conversions, orders, or customers. Missing rows are not automatically zeros.
- When changes overlap, propose the cheapest reversible data cut or test that distinguishes them.
- Escalate verified checkout, tracking, disapproval, stock, or destination failures while preserving an evidence trail.

## Output

Return: anomaly; dataset/data-integrity status; decomposition; confirmed findings; ranked hypotheses with supporting and contradicting evidence; estimated impact where possible; next checks; safe containment; exact status and confidence.

## Library references

Owned root artifacts, read when their scope applies:

- [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) — canonical structured-data provenance, grain, semantics, and decision-validity contract.
- [`data-contracts/validation.md`](../../../data-contracts/validation.md) — profiling, reconciliation, missingness, and cross-source comparison method.
- [cross-channel-diagnostic.md](../../../playbooks/cross-channel-diagnostic.md) — cross-channel diagnostic workflow.
- [audit.md](../../../templates/audit.md) — evidence-graded audit format.

## QA

Reconcile totals where their definitions should match, keep grain/keys/definitions/windows/currencies consistent, preserve cross-source attribution differences, account for lag and mix, show arithmetic, avoid double-counting, keep missing distinct from zero, and do not call the issue resolved until the source of truth recovers or the root cause is verified.
