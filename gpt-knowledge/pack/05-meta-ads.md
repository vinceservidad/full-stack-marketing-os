<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Meta Ads

## Skill: $meta-ads

**Use when:** Audit, diagnose, or plan Meta Ads delivery, structure, audiences, placements, and ads using funnel and business evidence; not for automatic publishing or spend changes.

Classify each audit, strategy, process, tactic, technique, best practice, or heuristic with `KNOWLEDGE-TAXONOMY.md`. Name the primary type and keep documented platform capability separate from expected business impact.

### Context

Collect campaign objective, conversion location, performance goal, dataset or Meta Pixel, selected optimization event, Conversions API status, attribution setting, market, dates and comparison, spend, campaign/ad-set/ad results, creative IDs, destinations, business revenue or lead-quality data, and constraints. Do not collapse those configuration fields into one “optimization” setting.

### Method

1. Confirm event quality and deduplication before treating platform results as business truth.
2. Decompose delivery (CPM, reach, frequency), response (outbound CTR or relevant attention signal), visit quality, conversion rate, value/lead quality, and profit.
3. Use breakdowns only when sample sizes support them; account for aggregation and attribution bias.
4. Diagnose at the right layer: auction, objective, audience, creative, destination, offer, or measurement.
5. Treat rising frequency plus worsening response as suggestive of fatigue, not conclusive without audience and delivery context.

For substantial funnel-mode work, read new-customer acquisition / prospecting or retargeting / remarketing as relevant. These are strategic categories; also state the current Meta implementation such as Advantage+ audience, audience suggestions, Custom Audiences, exclusions, or other controls. For current AI, automation, audience, placement, objective, or interface claims, read Platform Registry and apply the root `PLATFORM-CURRENCY.md` freshness gate.

### Rules

- Do not fragment budgets into many ad sets without a distinct hypothesis or constraint.
- Judge broad targeting, automated placements, and automation by incremental business outcome and control needs, not ideology.
- Do not pause an ad for low CTR when it produces profitable or high-quality outcomes.
- Do not scale from short windows or platform ROAS alone; require stability, capacity, unit economics, and a rollback threshold.
- Publishing, budget, bid, audience, and status changes require explicit approval.
- Do not call performance volatility an undocumented “Meta algorithm change.” Separate officially documented capability, account-visible behavior, experimentally observed impact, inference, and unknowns. Confirm account availability before recommending a current control.

### Output

Audit: measurement status; funnel decomposition; entity-level and creative findings; ranked actions; test plan; risks and unknowns.

Build plan: objective; architecture; optimization event; audience logic; creative matrix; budget logic; measurement; launch checklist; approval status.


### Library references

Owned root artifacts, read when their scope applies:

- meta-ads-full-stack.md — full-account decision model beyond a single audit or diagnosis.
- meta-ads-audit.md — step-by-step audit workflow.
- meta-ads-optimization.md — recurring optimization cadence.
- campaign-brief.md — campaign brief format, shared with $google-ads.

### QA

Verify attribution and event definitions, distinguish link clicks from landing-page views, connect creative IDs to results, account for frequency and spend distribution, label platform-only conclusions, check platform-registry freshness, and confirm account-visible availability for current controls.

### Reference: platform current ($meta-ads)

### Meta Ads Platform Registry

**Last verified:** 2026-08-22  
**Freshness class:** High-change; recheck within 30 days or whenever current behavior affects a decision.

Read this reference for current Meta AI, automation, audience, placement, objective, or interface terminology. Apply the root `PLATFORM-CURRENCY.md` contract.

#### Current mappings

| Stable concept | Current official product label or capability | Verified scope |
|---|---|---|
| AI-assisted audience expansion | **Advantage+ audience** | Uses audience suggestions while allowing documented audience controls. Confirm availability, defaults, and control behavior in the current ad account. |
| Automated inventory selection | **Advantage+ placements** | Allocates delivery across eligible Meta placements. Availability and placement inventory can vary by objective, format, market, and account. |
| Prior-relationship audience | **Custom Audience** plus an exact source, membership window, and exclusions | “Retargeting” remains a strategy label, not a complete Meta configuration. |
| Delivery outcome selection | **Performance goal** and selected optimization event | Record separately from campaign objective, conversion location, dataset/Meta Pixel, and attribution setting. |

#### First-party sources

- [Advantage+ audience](https://www.facebook.com/business/ads/meta-advantage-plus/audience) — audience suggestions, expansion, and documented controls.
- [Advantage+ placements](https://www.facebook.com/business/ads/meta-advantage-plus/placements) — automated placement scope and product framing.

Meta help content and account creation flows can be login-, market-, and rollout-dependent. If a precise creation default, eligibility rule, objective, performance goal, conversion location, dataset, event, attribution option, or Advantage+ control affects the decision, verify it in first-party help and then in the actual account.

#### Watchlist

Reverify Advantage+ campaign/audience naming and defaults, strict controls versus suggestions, placement inventory, creative automation, objective and performance-goal options, attribution settings, event/dataset terminology, Conversions API and deduplication guidance, reporting breakdown availability, and experiment/lift tooling.

Do not call delivery volatility an “algorithm change” without official evidence. Diagnose auction, audience, creative, destination, offer, measurement, and business demand separately; label causal explanations as observed, experimentally observed, inferred, or unknown.

### Reference: prospecting ($meta-ads)

### Meta New-Customer Acquisition / Prospecting

Use for new-customer acquisition planning or diagnosis. “Prospecting” is the practitioner strategy label, not necessarily the Meta interface label.

#### Inspect

- Optimization event quality, attribution, exclusions, and new-customer definition
- Audience breadth, Advantage+ audience or other current audience mode, strict geographic/age/language constraints, audience suggestions, Custom Audience exclusions, overlap, spend concentration, and delivery stability
- Creative angle and format coverage by audience situation and awareness
- Landing-page continuity, offer, unit economics, and downstream customer quality

#### Decisions

Broad, interest, lookalike, and automated audience approaches are hypotheses, not doctrines. Prefer enough consolidation for delivery while preserving constraints that change economics or message. Judge prospecting with new-customer or qualified-outcome evidence when available, not platform ROAS alone.

### Reference: retargeting ($meta-ads)

### Meta Retargeting / Remarketing

Use for analysis of eligible people with a qualifying prior engagement, visit, customer, or behavioral signal. Name the exact Custom Audience or other source, membership window, and exclusions; “retargeting” is a strategic label, not a complete audience definition.

#### Inspect

- Audience membership rule, window, size, exclusions, source quality, and overlap
- Purchase/lead/customer suppression and its reporting lag
- Frequency, reach, recency, spend saturation, creative sequence, and offer dependency
- View-through influence, branded demand capture, and incremental evidence

#### Decisions

Retargeting efficiency does not prove incrementality. Avoid tiny overlapping windows that fragment delivery or repeatedly target converted users. Match message to the unresolved barrier or next step; do not default to discounting when proof, reassurance, product education, or urgency is more appropriate.
