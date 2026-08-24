---
name: meta-ads
description: Audit, diagnose, or plan Meta Ads delivery, structure, audiences, placements, and ads using funnel and business evidence; not for automatic publishing or spend changes.
---

# Meta Ads

Classify each audit, strategy, process, tactic, technique, best practice, or heuristic with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Name the primary type and keep documented platform capability separate from expected business impact.

## Context

Collect campaign objective, conversion location, performance goal, dataset or Meta Pixel, selected optimization event, Conversions API status, attribution setting, market, dates and comparison, spend, campaign/ad-set/ad results, creative IDs, destinations, business revenue or lead-quality data, and constraints. Do not collapse those configuration fields into one “optimization” setting.

## Method

1. Confirm event quality and deduplication before treating platform results as business truth.
2. Decompose delivery (CPM, reach, frequency), response (outbound CTR or relevant attention signal), visit quality, conversion rate, value/lead quality, and profit.
3. Use breakdowns only when sample sizes support them; account for aggregation and attribution bias.
4. Diagnose at the right layer: auction, objective, audience, creative, destination, offer, or measurement.
5. Treat rising frequency plus worsening response as suggestive of fatigue, not conclusive without audience and delivery context.

For substantial funnel-mode work, read [new-customer acquisition / prospecting](references/prospecting.md) or [retargeting / remarketing](references/retargeting.md) as relevant. These are strategic categories; also state the current Meta implementation such as Advantage+ audience, audience suggestions, Custom Audiences, exclusions, or other controls. For current AI, automation, audience, placement, objective, or interface claims, read [Platform Registry](references/platform-current.md) and apply the root `PLATFORM-CURRENCY.md` freshness gate.

## Rules

- Do not fragment budgets into many ad sets without a distinct hypothesis or constraint.
- Judge broad targeting, automated placements, and automation by incremental business outcome and control needs, not ideology.
- Do not pause an ad for low CTR when it produces profitable or high-quality outcomes.
- Do not scale from short windows or platform ROAS alone; require stability, capacity, unit economics, and a rollback threshold.
- Publishing, budget, bid, audience, and status changes require explicit approval.
- Do not call performance volatility an undocumented “Meta algorithm change.” Separate officially documented capability, account-visible behavior, experimentally observed impact, inference, and unknowns. Confirm account availability before recommending a current control.

## Output

Audit: measurement status; funnel decomposition; entity-level and creative findings; ranked actions; test plan; risks and unknowns.

Build plan: objective; architecture; optimization event; audience logic; creative matrix; budget logic; measurement; launch checklist; approval status.


## Library references

Owned root artifacts, read when their scope applies:

- [meta-ads-full-stack.md](../../../frameworks/meta-ads-full-stack.md) — full-account decision model beyond a single audit or diagnosis.
- [meta-ads-audit.md](../../../playbooks/meta-ads-audit.md) — step-by-step audit workflow.
- [meta-ads-optimization.md](../../../workflows/meta-ads-optimization.md) — recurring optimization cadence.
- [campaign-brief.md](../../../templates/campaign-brief.md) — campaign brief format, shared with $google-ads.

## QA

Verify attribution and event definitions, distinguish link clicks from landing-page views, connect creative IDs to results, account for frequency and spend distribution, label platform-only conclusions, check platform-registry freshness, and confirm account-visible availability for current controls.
