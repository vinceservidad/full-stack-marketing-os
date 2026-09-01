# Marketing OS Data Contracts

This contract governs how structured marketing and business data is handed to Full-Stack Marketing OS.

The goal is not to force every platform into one export format. The goal is to preserve **meaning, provenance, grain, attribution, and limitations** so skills can compare data without silently changing what the numbers mean.

`$marketing-intake` owns the intake record and required-data completeness. `$tracking-measurement` owns measurement semantics, reconciliation, and whether a dataset is valid for a causal or attribution-sensitive decision. Channel and specialist skills own the business decisions made from data after those contracts are satisfied.

## Core rule

Keep two layers separate:

```text
Raw source export / query result
        ↓
Field mapping + metadata
        ↓
Normalized Marketing OS dataset
        ↓
Scoped validation
        ↓
Owning skill decision
```

Never overwrite or discard the raw source merely because a normalized dataset exists.

## Required dataset envelope

Every normalized dataset should record these fields or explicitly mark them unknown/not applicable:

| Field | Meaning |
|---|---|
| `contract_id` | Contract being used, such as `google-ads-performance` |
| `contract_version` | Version of the Marketing OS contract used for normalization |
| `dataset_id` | Stable identifier for this delivered dataset |
| `source_system` | Google Ads, Meta Ads, Shopify, GA4, internal finance, etc. |
| `source_scope` | Account/property/store/business unit covered |
| `source_method` | Export, API, connector, query, report, manual file, etc. |
| `source_generated_at` | When the source result/export was generated |
| `data_start_at` | Inclusive start of the represented period |
| `data_end_at` | Inclusive end of the represented period |
| `timezone` | Timezone used by the source/report |
| `currency` | Currency for monetary fields, or `mixed` with a mapping |
| `grain` | One row per date/campaign/order/product/etc. |
| `primary_key` | Field(s) expected to identify a row at the stated grain |
| `row_semantics` | What one row means |
| `attribution_basis` | Platform/source attribution model/window or `not_applicable` |
| `conversion_definition` | Which event/action/business outcome is counted |
| `revenue_basis` | Gross sales, net sales, platform-attributed value, booked revenue, etc. |
| `profit_basis` | Named profit level and included costs when profit is present |
| `freshness_state` | Current, delayed, stale, unknown, or source-defined lag |
| `normalization_state` | See validation states below |
| `known_limitations` | Missing joins, partial periods, modeled metrics, privacy thresholds, etc. |
| `field_lineage` | Mapping from normalized fields back to source fields/calculations |

## Data validity states

These are **dataset states**, not implementation states:

1. `received` — source data exists but has not been profiled.
2. `profiled` — grain, fields, types, date range, and obvious quality issues are understood.
3. `mapped` — normalized fields have source lineage.
4. `validated-for-scope` — fit for the specific decision named in the intake record.
5. `degraded` — usable only with explicit limitations that may affect the decision.
6. `rejected` — not safe for the requested decision without correction or replacement.

A dataset can be valid for one decision and invalid for another. Example: Meta entity-level data may be useful for creative delivery diagnosis while platform-attributed revenue remains unsuitable as verified incremental business revenue.

## Grain and joins

- Never mix multiple grains in one table without an explicit row type.
- Aggregate only after naming the source grain and aggregation rule.
- Do not join on display names when stable IDs exist.
- If IDs changed, merged, or are absent, preserve the join uncertainty.
- Many-to-many joins require an explicit bridge or allocation rule; do not silently duplicate money or conversions.
- A row missing from a report is not automatically zero.
- `0`, `null/unknown`, `not_applicable`, and `not_reported` are distinct states.

## Money and economics

- Every monetary field needs a currency.
- Do not add mixed currencies without conversion and an FX source/date convention.
- Keep platform-attributed conversion value separate from commerce/accounting revenue.
- Keep gross sales, discounts, refunds, taxes, shipping, net sales, COGS, fulfillment, payment fees, media spend, and contribution levels separate when available.
- Never label a derived field `profit` without naming the level and included costs.
- Break-even ROAS, contribution margin, CAC, MER, LTV, and payback are calculations with explicit inputs, not raw universal fields.

## Attribution and conversion semantics

- Preserve the source attribution setting/window/model and the conversion event/action definition.
- Do not sum platform-attributed revenue across platforms as business revenue.
- Do not merge GA4/session attribution with ad-platform attribution into one number without a declared reconciliation method.
- Distinguish platform conversions, analytics events/key events, commerce orders, qualified leads, closed revenue, and other business outcomes.
- When a source uses modeled, estimated, sampled, thresholded, or privacy-limited data, record that source behavior when known.

## Time

- Preserve source timezone and reporting cutoff.
- Mark partial current days/periods.
- Record known conversion/revenue maturation lag.
- Do not compare unequal weekday mix, promotion periods, or attribution maturity without disclosure.

## Privacy and minimization

Use the minimum data needed for the decision.

- Do not require customer names, emails, phone numbers, addresses, or other direct identifiers for routine marketing analysis.
- For cohort/repeat analysis, prefer a stable pseudonymous customer/entity ID when individual linkage is genuinely required.
- Do not place credentials, tokens, access keys, or secrets in a data contract or example file.
- Preserve applicable consent, retention, contractual, and access restrictions supplied with the data.

## Contract library

- [`data-contracts/google-ads.md`](data-contracts/google-ads.md)
- [`data-contracts/meta-ads.md`](data-contracts/meta-ads.md)
- [`data-contracts/commerce-orders.md`](data-contracts/commerce-orders.md)
- [`data-contracts/web-analytics.md`](data-contracts/web-analytics.md)
- [`data-contracts/business-economics.md`](data-contracts/business-economics.md)
- [`data-contracts/validation.md`](data-contracts/validation.md)

Use [`templates/data-intake-manifest.md`](templates/data-intake-manifest.md) to record delivered datasets and their decision scope.

## Versioning

A contract change is material when it changes required semantics, field meaning, validation rules, or decision compatibility. Material changes must:

1. update the relevant contract version/date;
2. preserve backward-compatibility notes where practical;
3. update behavioral evaluations;
4. update installer/distribution validation if the contract location changes.

Platform interface labels remain governed by [`PLATFORM-CURRENCY.md`](PLATFORM-CURRENCY.md). A data contract must not freeze a fast-changing UI term as permanent platform truth.
