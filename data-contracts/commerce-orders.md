# Commerce / Orders Data Contract

**Contract ID:** `commerce-orders`  
**Contract version:** `1.0`  
**Primary owner for intake completeness:** `$marketing-intake`  
**Measurement/reconciliation:** `$tracking-measurement`  
**Decision owners:** `$performance-diagnostics`, `$cro`, `$retention-economics`, `$pricing-monetization`, `$optimization-scaling`, or another routed owner

Use this contract for Shopify or another commerce/order system when Marketing OS needs actual order, product, revenue, refund, or customer-cohort evidence.

This contract is intentionally platform-neutral. Shopify-specific raw field names may change or differ by export/API surface; preserve source lineage rather than forcing the raw export to match this file exactly.

## Required envelope

Apply [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md) and record store/source scope, timezone, currency, export/query time, represented order period, revenue basis, refund handling, and field lineage.

## Separate order and line-item grains

Prefer two normalized datasets when product analysis is required.

### `orders`

One row per order (or stable order transaction if the source requires a different declared grain).

Recommended fields:

- `order_id`
- `order_created_at`
- `order_updated_at` when late refunds/status changes matter
- `order_status`
- `financial_status` or equivalent source state when relevant
- `currency`
- `gross_sales`
- `discounts`
- `refunds` or returns/refund value with source timing rule
- `shipping_revenue`
- `taxes`
- `net_sales` or other declared source revenue basis
- `total_collected` when available and materially different from net sales
- `customer_id_pseudonymous` only when cohort/repeat analysis requires it
- `customer_type` such as new/returning when the source definition is known
- `channel` / source attribution fields when provided by commerce source
- landing/UTM/referrer fields when available and decision-relevant
- destination country/region at a non-identifying level when required for geography analysis

### `order_lines`

One row per order × line item (or another declared stable line grain).

Recommended fields:

- `order_id`
- `line_id`
- `product_id`
- `variant_id`
- `sku`
- `product_title` as display context, not primary join key when stable IDs exist
- `quantity`
- `line_gross_sales`
- `line_discount`
- `line_refund`
- `line_net_sales`
- `unit_cogs` or `line_cogs` only when sourced from a governed business-economics source

## Revenue semantics

Do not assume `total`, `gross sales`, `net sales`, `sales`, `revenue`, and `amount paid` are interchangeable.

For each monetary field, document what is included/excluded. In particular:

- discounts may be recognized at order or line level;
- refunds can be dated to original order date or refund date depending on source/report;
- taxes and shipping may be included or excluded from reported revenue;
- gift cards, credits, duties, fees, subscriptions, partial captures, and cancellations may require business-specific treatment.

Marketing OS should not manufacture a universal revenue formula when the source/accounting convention differs. Name the basis used for each decision.

## Customer/cohort privacy

Routine acquisition/CRO analysis generally does **not** need direct customer identity.

If repeat purchase, retention, or LTV analysis requires linkage:

- prefer `customer_id_pseudonymous` or another stable non-direct identifier;
- do not include customer name, email, phone, street address, or other direct identifiers unless a specific authorized workflow truly requires them;
- preserve consent/access/retention constraints supplied with the data.

## Returns and refunds

Record:

- whether refunds are complete/partial;
- whether return quantity and refund value can be joined to product lines;
- date basis used for period reporting;
- whether returns/refunds are mature for the analyzed cohort.

Do not call an immature recent cohort more profitable merely because refunds/returns have not yet matured.

## Product joins

Use stable product/variant/SKU identifiers to join:

- Google/Meta product performance;
- COGS/margin data;
- inventory/capacity;
- return/refund rates;
- merchandising attributes.

If a source system uses different product IDs, maintain a mapping table. Do not join only on product title when titles can change or collide.

## Minimum decision-valid extracts

### Revenue reconciliation

At minimum:

- stable order ID
- order timestamp/date
- currency
- declared revenue basis
- refunds/discount treatment
- order status/eligibility rules

### Product profitability

Add:

- order lines with stable product/variant/SKU IDs
- quantity and line revenue/discount/refund values
- separate business-economics join for COGS/variable costs

### Repeat / retention economics

Add:

- stable pseudonymous customer ID
- order date/time
- order revenue basis
- cancellation/refund maturity rules
- cohort definition and observation cutoff

## Rejection/degradation examples

Mark the dataset `degraded` or `rejected` for the scoped decision when, for example:

- order IDs are missing and duplicates cannot be detected;
- mixed currencies are aggregated without an FX rule;
- refunded/cancelled orders are indistinguishable from fulfilled/realized orders for a profitability decision;
- line-level revenue is joined to order-level totals and double-counted;
- product profitability is requested but product identifiers cannot be reliably joined to COGS;
- LTV/retention is requested but customer linkage is absent or observation maturity is too short;
- direct customer PII is supplied unnecessarily for a routine aggregate analysis.
