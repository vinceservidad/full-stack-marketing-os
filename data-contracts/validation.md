# Data Contract Validation and Reconciliation

**Contract ID:** `data-contract-validation`  
**Contract version:** `1.0`  
**Primary owner:** `$tracking-measurement` for measurement/reconciliation validity; `$marketing-intake` for completeness/provenance

Use this method before a structured dataset is treated as decision-valid.

## Validation sequence

```text
Receive
→ Profile
→ Map fields
→ Check grain/keys
→ Check time/currency
→ Check metric semantics
→ Reconcile totals where possible
→ Identify limitations
→ Grade validity for the named decision
→ Route to owning skill
```

## 1. Profile the source

Record:

- source system and scope;
- row count;
- columns/field types;
- minimum/maximum dates;
- timezone/currency;
- apparent grain;
- candidate primary key;
- duplicate/null patterns;
- generated/exported timestamp;
- report/query configuration when known.

Do not assume a filename or sheet name proves the source semantics.

## 2. Validate grain and keys

For the declared grain:

- test whether the primary key is actually unique;
- identify duplicate rows and explain whether they are valid sub-grains or errors;
- identify rows that mix entity levels;
- prevent one-to-many or many-to-many joins from duplicating spend, revenue, conversions, or orders.

If a clean stable key is unavailable, record the join limitation instead of inventing one.

## 3. Validate dates and time

Check:

- source timezone;
- inclusive/exclusive date boundaries;
- partial current periods;
- data/attribution maturation lag;
- daylight-saving or timezone changes when relevant;
- comparison periods with different weekday/promo/seasonality mix.

## 4. Validate currency and money basis

Check:

- currency per source/dataset;
- mixed-currency rows;
- FX rule/source/date if conversion is used;
- gross/net/platform-attributed/booked/collected revenue meaning;
- profit level and included costs;
- refund/return date basis.

Do not force reconciliation between money fields with different definitions.

## 5. Validate conversion/event semantics

For every decision-critical event/action:

- name the source field/event/action;
- define the represented customer/business behavior;
- record optimization/bidding role where relevant;
- record attribution/window/model where relevant;
- identify definition changes during the period;
- check deduplication/uniqueness assumptions.

If the event meaning is unclear, keep it unknown rather than calling it a purchase, lead, activation, or retained customer.

## 6. Reconcile within source

Where totals should reasonably match:

- child entities should reconcile to parent totals after known exclusions/thresholding;
- order lines should reconcile to order totals under the declared revenue rules;
- product/query/ad breakdowns should not exceed totals because of duplicated joins;
- base metrics should reproduce derived metrics within rounding tolerance.

A reconciliation gap is not automatically an error if the source documents privacy, modeling, unsupported breakdowns, or withheld rows. Record the gap and its likely source.

## 7. Reconcile across sources

Cross-source reconciliation does **not** mean forcing all numbers to equality.

Create a reconciliation table such as:

| Source | Metric | Basis | Period | Value | Why it may differ |
|---|---|---|---|---:|---|
| Meta Ads | purchase value | platform-attributed | … | … | attribution/window/modeling |
| Google Ads | conversion value | platform-attributed | … | … | attribution/action scope |
| GA4 | purchase revenue | analytics-attributed | … | … | tagging/attribution/consent |
| Commerce | net sales | order/accounting source | … | … | refunds/taxes/shipping basis |

Never sum platform-attributed values across sources and call the total business revenue.

## 8. Missingness

Distinguish:

- `0` — known zero;
- `null/unknown` — not known;
- `not_applicable` — field does not apply;
- `not_reported` — source did not report/expose it;
- `withheld/thresholded` — source intentionally suppresses detail when known.

Missing rows are not automatically zeros.

## 9. Validity for decision

Grade the dataset specifically for the requested decision.

### `validated-for-scope`

Required fields/semantics are sufficient, material reconciliation issues are understood, and remaining limitations are unlikely to reverse the named decision.

### `degraded`

Useful evidence exists, but a limitation can materially affect confidence, precision, or transfer. State exactly what can and cannot be concluded.

### `rejected`

A material defect prevents safe use for the named decision. Examples: duplicated spend from a join, unknown currency, undefined conversion event, broken order identifiers, or missing economics for a profitability claim.

## 10. Decision handoff

The validation record should end with:

- dataset IDs and versions;
- validity state for the named decision;
- confirmed semantics;
- unresolved limitations;
- reconciliation notes;
- allowed uses;
- prohibited/unsafe uses;
- owning skill for the next decision.

A dataset being `validated-for-scope` does not prove a marketing hypothesis or causal mechanism. It means the data is sufficiently trustworthy for the specific analysis it was validated to support.
