---
name: meta-ads
description: Audit, diagnose, or plan Meta Ads delivery, structure, audiences, placements, and ads using funnel and business evidence; not for automatic publishing or spend changes.
---

# Meta Ads

Classify each audit, strategy, process, tactic, technique, best practice, or heuristic with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Name the primary type and keep documented platform capability separate from expected business impact.

## Context

Collect campaign objective, conversion location, performance goal, dataset or Meta Pixel, selected optimization event, Conversions API status, attribution setting, market, dates and comparison, spend, campaign/ad-set/ad results, creative IDs, destinations, business revenue or lead-quality data, and constraints. Do not collapse those configuration fields into one “optimization” setting.

When structured Meta Ads exports/API results are supplied, apply [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) and [`data-contracts/meta-ads.md`](../../../data-contracts/meta-ads.md). Preserve raw source data and keep campaign, ad set, ad/creative, placement, and audience breakdown grains distinct unless a declared mapping can combine them without duplicating spend or attributed value.

## Method

1. Confirm event quality and deduplication before treating platform results as business truth.
2. Confirm the data is valid for the scoped decision: timezone, currency, grain, stable campaign/ad set/ad/creative IDs, click metric definition, conversion event, attribution setting, partial/lagged periods, and any business-revenue join.
3. Decompose delivery (CPM, reach, frequency), response (outbound CTR or relevant attention signal), visit quality, conversion rate, value/lead quality, and profit.
4. Use breakdowns only when sample sizes support them; account for aggregation and attribution bias.
5. Diagnose at the right layer: auction, objective, audience, creative, destination, offer, or measurement.
6. Treat rising frequency plus worsening response as suggestive of fatigue, not conclusive without audience and delivery context.

For substantial funnel-mode work, read [new-customer acquisition / prospecting](references/prospecting.md) or [retargeting / remarketing](references/retargeting.md) as relevant. These are strategic categories; also state the current Meta implementation such as Advantage+ audience, audience suggestions, Custom Audiences, exclusions, or other controls. For current AI, automation, audience, placement, objective, or interface claims, read [Platform Registry](references/platform-current.md) and apply the root `PLATFORM-CURRENCY.md` freshness gate.

## Rules

- Do not fragment budgets into many ad sets without a distinct hypothesis or constraint.
- Judge broad targeting, automated placements, and automation by incremental business outcome and control needs, not ideology.
- Do not pause an ad for low CTR when it produces profitable or high-quality outcomes.
- Do not scale from short windows or platform ROAS alone; require stability, capacity, unit economics, and a rollback threshold.
- Keep Meta-attributed purchase value separate from commerce/accounting revenue until reconciled; do not sum Meta, Google Ads, and analytics attribution into one business-revenue number.
- Do not join campaign totals to ad/placement/audience rows in a way that duplicates spend, conversions, or value. A missing or withheld breakdown row is not automatically zero.
- Audience comparisons are provisional when creative, budget, timing, optimization, placement, or delivery differs materially between cells.
- Publishing, budget, bid, audience, and status changes require explicit approval.
- Do not call performance volatility an undocumented “Meta algorithm change.” Separate officially documented capability, account-visible behavior, experimentally observed impact, inference, and unknowns. Confirm account availability before recommending a current control.

## Output

Audit: dataset validity when structured data is used; measurement status; funnel decomposition; entity-level and creative findings; ranked actions; test plan; risks and unknowns.

Build plan: objective; architecture; optimization event; audience logic; creative matrix; budget logic; measurement; launch checklist; approval status.

## Library references

Owned root artifacts, read when their scope applies:

- [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) — canonical structured-data provenance and decision-validity contract.
- [`data-contracts/meta-ads.md`](../../../data-contracts/meta-ads.md) — Meta campaign/ad set/ad/creative, audience, placement, attribution, and metric semantics.
- [meta-ads-full-stack.md](../../../frameworks/meta-ads-full-stack.md) — full-account decision model beyond a single audit or diagnosis.
- [meta-ads-audit.md](../../../playbooks/meta-ads-audit.md) — step-by-step audit workflow.
- [meta-ads-optimization.md](../../../workflows/meta-ads-optimization.md) — recurring optimization cadence.
- [campaign-brief.md](../../../templates/campaign-brief.md) — campaign brief format, shared with $google-ads.

## QA

Verify data-contract scope where structured exports are used; attribution and event definitions; timezone/currency; stable ad/creative identity; incompatible grain or duplicated joins; link clicks versus landing-page views; creative IDs connected to results; frequency and spend distribution; platform-only conclusions labeled; platform-registry freshness; and account-visible availability for current controls.
