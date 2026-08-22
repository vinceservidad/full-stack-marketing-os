---
name: google-ads
description: Audit, diagnose, or plan Google Ads Search, Shopping, and Performance Max work using business outcomes and query or product evidence; not for unsupported live changes.
---

# Google Ads

## Context

Collect business goal, account and market scope, date range and comparison, budget, bidding strategy, campaign type, conversion goals, conversion actions, action-optimization status, revenue or qualified-lead definition, and available exports. For ecommerce profitability, request price, COGS, variable fulfillment, payment fees, discounts, refunds, revenue basis, and feed status.

## Method

1. Verify conversion goals, their included conversion actions, each action's Primary/Secondary status, campaign goal selection, counting, values, attribution windows, consent gaps, and agreement with the business source of truth. A Primary action influences bidding only when the campaign uses its containing goal.
2. Decompose demand and eligibility → auctions and spend → clicks → site behavior → conversions → revenue, margin, or lead quality.
3. Inspect the correct unit:
   - Search: queries, match type, intent, ad relevance, landing alignment, geography, device, and schedule.
   - Shopping/PMax: item ID, product type, price, feed quality, availability, asset-group segmentation, and available channel-mix evidence.
4. Compare like-for-like periods and separate volume, efficiency, mix, and measurement effects.
5. Rank actions by expected business impact, confidence, reversibility, and learning value.

For substantial mode-specific work, read only the relevant reference: [Search](references/search.md), [Shopping](references/shopping.md), or [Performance Max](references/pmax.md).

## Rules

- Never add a negative solely because a query did not convert in a small sample; consider intent, spend against allowable CPA, assisted value, and protected brand/product coverage.
- Do not increase budgets while measurement integrity or unit economics are unknown.
- Avoid structural rebuilds when the issue is isolated to measurement, feed eligibility, landing experience, or a small set of queries/items.
- Do not infer unseen PMax channel allocation.
- Use profit or qualified-lead economics when available. Label ROAS/CPA conclusions provisional otherwise.
- Use “conversion goal” for the Google Ads grouping and “conversion action” for the measured action. Do not call the main commercial result a Primary conversion action; call it the primary business outcome.

## Output

Audit: scope; measurement status; findings with evidence, impact, and confidence; protected coverage; prioritized actions; tests; unknowns.

Change plan: exact entity; current and proposed state; rationale; risk; rollback/stop rule; approval required.

## QA

Check date and attribution consistency, conversion scope, sample size, query/item evidence, margin or lead-quality caveats, and preservation of valuable coverage.
