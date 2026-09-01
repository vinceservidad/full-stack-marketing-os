---
name: google-ads
description: Audit, diagnose, or plan Google Ads Search, Shopping, and Performance Max work using business outcomes and query or product evidence; not for unsupported live changes.
---

# Google Ads

Covers Search, Shopping, and Performance Max structure, bidding, and account mechanics. YouTube video advertising is a distinct discipline with different attention economics, format constraints, and measurement norms — route to `$youtube-ads` for format selection, video-specific targeting, and view-through measurement fit; this skill covers the shared Google Ads account and bidding layer YouTube campaigns also run through.

Classify each audit, model, methodology, process, tactic, technique, best practice, or heuristic with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Name the primary type and keep platform evidence separate from recommendations.

## Context

Collect business goal, account and market scope, date range and comparison, budget, bidding strategy, campaign type, conversion goals, conversion actions, action-optimization status, revenue or qualified-lead definition, and available exports. For ecommerce profitability, request price, COGS, variable fulfillment, payment fees, discounts, refunds, revenue basis, and feed status.

When structured Google Ads exports/API results are supplied, apply [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) and [`data-contracts/google-ads.md`](../../../data-contracts/google-ads.md). Preserve raw source data and keep campaign, query/keyword, product, and asset grains separate unless a declared mapping can combine them without duplicating spend or conversion value.

## Method

1. Verify conversion goals, their included conversion actions, each action's Primary/Secondary status, campaign goal selection, counting, values, attribution windows, consent gaps, and agreement with the business source of truth. A Primary action influences bidding only when the campaign uses its containing goal.
2. Confirm the data is valid for the scoped decision: timezone, currency, grain, stable IDs, conversion/value semantics, attribution basis, partial/lagged periods, and product/business-economics joins where required.
3. Decompose demand and eligibility → auctions and spend → clicks → site behavior → conversions → revenue, margin, or lead quality.
4. Inspect the correct unit:
   - Search: queries, match type, intent, ad relevance, landing alignment, geography, device, and schedule.
   - Shopping/PMax: item ID, product type, price, feed quality, availability, asset-group segmentation, and available channel-mix evidence.
5. Compare like-for-like periods and separate volume, efficiency, mix, and measurement effects.
6. Rank actions by expected business impact, confidence, reversibility, and learning value.

For substantial mode-specific work, read only the relevant reference: [Search](references/search.md), [Shopping](references/shopping.md), or [Performance Max](references/pmax.md). For current AI, automation, control, reporting, or interface claims, read [Platform Registry](references/platform-current.md) and apply the root `PLATFORM-CURRENCY.md` freshness gate.

## Rules

- Never add a negative solely because a query did not convert in a small sample; consider intent, spend against allowable CPA, assisted value, and protected brand/product coverage.
- Do not increase budgets while measurement integrity or unit economics are unknown.
- Avoid structural rebuilds when the issue is isolated to measurement, feed eligibility, landing experience, or a small set of queries/items.
- Do not infer unseen PMax channel allocation.
- Use profit or qualified-lead economics when available. Label ROAS/CPA conclusions provisional otherwise.
- Keep Google Ads `conversion_value` separate from commerce/accounting revenue until reconciled; never use a product or campaign platform ROAS as verified profitability by itself.
- Do not join campaign totals to query/product/asset rows in a way that duplicates spend, conversions, or value. A missing query/product row is not automatically zero.
- Use “conversion goal” for the Google Ads grouping and “conversion action” for the measured action. Do not call the main commercial result a Primary conversion action; call it the primary business outcome.
- Do not claim an undocumented “Google algorithm change.” Separate officially documented capability, account-visible behavior, experimentally observed impact, inference, and unknowns. Confirm account availability before recommending a current control.

## Output

Audit: scope; dataset validity when structured data is used; measurement status; findings with evidence, impact, and confidence; protected coverage; prioritized actions; tests; unknowns.

Change plan: exact entity; current and proposed state; rationale; risk; rollback/stop rule; approval required.

## Library references

Owned root artifacts, read when their scope applies:

- [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) — canonical structured-data provenance and decision-validity contract.
- [`data-contracts/google-ads.md`](../../../data-contracts/google-ads.md) — Google Ads campaign/query/product/asset grain and field semantics.
- [google-ads-full-stack.md](../../../frameworks/google-ads-full-stack.md) — full-account decision model beyond a single audit or diagnosis.
- [google-ads-audit.md](../../../playbooks/google-ads-audit.md) — step-by-step audit workflow.
- [google-ads-optimization.md](../../../workflows/google-ads-optimization.md) — recurring optimization cadence.
- [campaign-brief.md](../../../templates/campaign-brief.md) — campaign brief format, shared with $meta-ads.

## QA

Check data-contract scope where structured exports are used; date/timezone and attribution consistency; currency; stable entity/product IDs; incompatible grain or duplicated joins; conversion scope; sample size; query/item evidence; margin or lead-quality caveats; preservation of valuable coverage; platform-registry freshness; and account-visible availability for current controls.
