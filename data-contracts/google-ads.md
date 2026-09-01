# Google Ads Data Contract

**Contract ID:** `google-ads-performance`  
**Contract version:** `1.0`  
**Primary owner for intake completeness:** `$marketing-intake`  
**Measurement semantics:** `$tracking-measurement`  
**Decision owner after validation:** `$google-ads` or another routed owner

Use this contract for Search, Shopping, Performance Max, and other Google Ads performance exports used by Marketing OS.

This is a **normalized decision contract**, not a promise that every Google Ads interface/API export uses these exact column names.

## Required envelope

Apply [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md) and preserve account timezone, currency, reporting period, source method, conversion definitions, attribution basis, and field lineage.

## Keep separate grains separate

Prefer separate datasets when the decision needs different grains:

1. `campaign_performance` — date × campaign or a clearly declared campaign aggregate.
2. `ad_group_performance` — date × campaign × ad group where relevant.
3. `search_terms` — date/period × campaign × ad group × search term.
4. `keywords` — date/period × keyword criterion.
5. `shopping_products` — date/period × product/item identifier and campaign context.
6. `creative_or_asset_performance` — only when the source exposes decision-valid asset/ad detail and its reporting limitations are known.

Do not put campaign, search-term, product, and asset rows into one flat table with duplicated spend/conversions.

## Normalized dimensions

Use the dimensions required by the decision and preserve source lineage:

- `date` or declared `period_start` / `period_end`
- `account_id`
- `campaign_id`
- `campaign_name`
- `campaign_type` or source campaign subtype when available
- `campaign_status`
- `ad_group_id` / `ad_group_name` when applicable
- `keyword_id`, `keyword_text`, `match_type` when applicable
- `search_term` when applicable
- `product_item_id` / merchant item identifier when applicable
- `product_title`, `brand`, `product_type`, custom labels when decision-relevant and available
- `device`, `network`, `country` or geography when used for segmentation
- `conversion_action` or conversion-category breakdown when the analysis depends on action-level meaning

Stable IDs are preferred over display names for joins.

## Normalized metrics

At the correct grain, include the strongest available source metrics needed for the decision:

- `impressions`
- `clicks`
- `cost`
- `conversions`
- `conversion_value`
- `all_conversions` / `all_conversion_value` only when the distinction is decision-relevant and the source meaning is preserved
- `eligible_impressions`, impression share, lost share, or other coverage fields only when available and required for the decision

Derived metrics such as CTR, CPC, CVR, CPA, ROAS, impression-share deltas, marginal ROAS, and contribution are calculations. Prefer calculating them from base fields when possible and record the formula.

## Conversion semantics

Record:

- which Google Ads conversion actions are included in `conversions`;
- which are primary/secondary or otherwise used for bidding/reporting when decision-relevant;
- conversion value basis;
- attribution setting/model/window as exposed by the source or supporting account documentation;
- known conversion lag or maturation issues.

Do not treat Google Ads `conversion_value` as reconciled commerce/accounting revenue unless a separate reconciliation supports that claim.

## Search-term and keyword rules

- Search term and keyword are different entities.
- Preserve match type and keyword criterion when available.
- A missing search term can reflect reporting/privacy/source limitations; do not convert every absent query into zero activity.
- Query-level spend should reconcile reasonably to the parent scope after accounting for source/reporting limitations; disclose any unreconciled remainder.

## Shopping/product rules

- Preserve stable merchant/product identifiers.
- Join product economics using the stable product/item mapping, not only title text.
- Keep product-level ad cost, attributed value, commerce sales, margin, returns/refunds, and inventory/capacity as distinct fields/sources.
- A product with high platform ROAS is not automatically the best product to scale if margin, stock, returns, or business value differ.

## PMax / asset limitations

Performance Max and asset-level reporting can expose different controls, labels, and degrees of detail over time. Apply [`PLATFORM-CURRENCY.md`](../PLATFORM-CURRENCY.md) before treating a stored interface label or control as current.

Do not infer audience causality, asset-level incrementality, or hidden allocation logic from aggregate PMax reporting.

## Minimum decision-valid extracts

### Basic campaign audit

At minimum:

- campaign ID/name/type/status
- period/date
- cost
- impressions
- clicks
- conversions
- conversion value
- conversion definition + attribution basis
- account timezone/currency

### Search query audit

Add:

- search term
- campaign/ad group IDs
- keyword/match context when available
- cost/click/conversion/value fields at query grain

### Shopping/product audit

Add:

- stable item/product ID
- product segmentation fields needed for the decision
- cost/click/conversion/value fields at product grain
- separate business-economics/product join when profitability is being judged

## Rejection/degradation examples

Mark the dataset `degraded` or `rejected` for the scoped decision when, for example:

- spend is in mixed currencies without a conversion rule;
- conversion actions changed mid-period but the change is not represented;
- campaign totals are joined to query/product rows in a way that duplicates spend;
- only ROAS percentages are supplied without cost/value bases and the decision needs arithmetic verification;
- a profitability decision is requested but no named profit basis/economics is available;
- a “current platform feature” decision relies on stale interface assumptions.
