# Data Contracts

This directory contains normalized structured-data contracts for Full-Stack Marketing OS.

Start with [`../DATA-CONTRACTS.md`](../DATA-CONTRACTS.md). It defines the shared dataset envelope, data-validity states, grain/join rules, money/attribution semantics, privacy rules, and versioning.

## Contracts

| Source/domain | Contract | Typical decisions |
|---|---|---|
| Google Ads | [`google-ads.md`](google-ads.md) | campaign/query/product audits, bidding/budget diagnosis, Shopping/PMax analysis |
| Meta Ads | [`meta-ads.md`](meta-ads.md) | delivery, creative, audience, placement, prospecting/retargeting diagnosis |
| Commerce/orders | [`commerce-orders.md`](commerce-orders.md) | realized revenue, orders, product/SKU analysis, refunds, repeat/cohort linkage |
| Web analytics | [`web-analytics.md`](web-analytics.md) | traffic, landing pages, events, funnels, analytics attribution |
| Business economics | [`business-economics.md`](business-economics.md) | contribution, unit economics, scaling, pricing, LTV/payback inputs |
| Validation | [`validation.md`](validation.md) | profiling, field mapping, within/cross-source reconciliation, scope validity |

For substantial multi-source work, record the delivered datasets with [`../templates/data-intake-manifest.md`](../templates/data-intake-manifest.md).

## How to use

```text
1. Keep the raw export/query result.
2. Record the DATA-CONTRACTS.md envelope.
3. Select the relevant source/domain contract.
4. Map normalized fields back to source fields/calculations.
5. Validate grain, keys, dates, currency, semantics, and reconciliation.
6. Grade the dataset for the named decision.
7. Hand only supported conclusions to the owning skill.
```

Do not flatten different platform grains into one universal CSV merely for convenience. A shared envelope makes datasets interoperable without pretending Google Ads campaigns, Meta creatives, GA4 sessions, commerce orders, and business economics are the same entity.

## Current integration status

These are **data semantics contracts**, not live connectors.

They work with:

- manually supplied CSV/XLSX exports;
- pasted tables;
- API/query results;
- future connector/MCP results;
- other structured evidence whose source meaning can be mapped.

A connector can automate retrieval later, but it must still preserve these semantics. A data contract does not provide credentials, live account access, or authorization to mutate an external system.
