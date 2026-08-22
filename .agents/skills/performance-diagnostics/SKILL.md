---
name: performance-diagnostics
description: Diagnose why marketing revenue, profit, conversions, spend, or lead quality changed by decomposing metrics and testing competing explanations; use for anomalies and cross-channel questions.
---

# Performance Diagnostics

## Method

1. Restate the anomaly with metric definition, absolute values, baseline, date range, scope, and business significance.
2. Validate timezone, attribution, lag, currency, duplicate/missing events, freshness, and denominator changes.
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
- Do not compare periods with different promotions, weekday mix, attribution maturity, or inventory without adjustment.
- Separate observed fact, inference, and recommended test.
- Never use “profit” without naming the level and included costs. Never subtract discounts or refunds twice.
- When changes overlap, propose the cheapest reversible data cut or test that distinguishes them.
- Escalate verified checkout, tracking, disapproval, stock, or destination failures while preserving an evidence trail.

## Output

Return: anomaly; data-integrity status; decomposition; confirmed findings; ranked hypotheses with supporting and contradicting evidence; estimated impact where possible; next checks; safe containment; exact status and confidence.

## QA

Reconcile totals, keep definitions and windows consistent, account for lag and mix, show arithmetic, avoid double-counting, and do not call the issue resolved until the source of truth recovers or the root cause is verified.
