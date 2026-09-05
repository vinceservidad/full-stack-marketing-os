<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# LinkedIn and Programmatic

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/linkedin-ads/SKILL.md`

---
name: linkedin-ads
description: Plan, audit, or diagnose LinkedIn B2B advertising — account-based and firmographic targeting, format selection, Lead Gen Forms, and cost-structure economics; not for consumer/demographic-targeted channels, and not for the underlying sales-cycle or CRM ownership.
---

# LinkedIn Ads

Classify each model, targeting decision, or economics claim with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). LinkedIn's targeting unit is frequently the buying account or the buying committee, not the individual consumer — a fundamentally different targeting logic than Meta, TikTok, or YouTube, and one that should be built from `$icp-jtbd` evidence about buying situations and buyer roles, not demographic proxies.

## Context

Primary business outcome and lead-stage definitions per `$marketing-intake`, since LinkedIn's cost per click and cost per lead run materially higher than consumer platforms and a cost conclusion is meaningless without the qualified-lead or pipeline economics behind it; target account list or firmographic criteria if account-based marketing is in use; buyer roles and buying-committee structure per `$icp-jtbd`; available formats (Sponsored Content, Message/Conversation Ads, Lead Gen Forms, Text/Dynamic Ads) and creative fit for each; and sales-cycle length, since a lead generated today frequently will not show revenue for months.

## Method

1. Establish whether targeting is account-based (a defined target account list, matched via account targeting) or attribute-based (job title, seniority, function, industry, company size) — state which and why; see Account and firmographic targeting (source: `.agents/skills/linkedin-ads/references/account-and-firmographic-targeting.md`).
2. Select ad format to fit the funnel stage and buying-committee role being reached; a Message/Conversation Ad to a senior decision-maker and a Lead Gen Form to a research-stage individual contributor are different mechanisms for different roles, not interchangeable defaults.
3. Assess Lead Gen Forms (native, pre-filled, lower-friction) against an off-platform landing page (higher friction, potentially higher intent signal) for the specific offer; the friction/quality tradeoff is a real decision, not a default.
4. Set cost expectations against the account's own economics, not a consumer-platform benchmark; LinkedIn's cost per click and cost per lead are structurally higher, and evaluating them against a Meta or Google benchmark produces a false efficiency conclusion.
5. Define the measurement plan against the actual sales cycle: lead volume and immediate cost-per-lead are early, weak signals; route to `$retention-economics`'s lead-to-revenue cohort method for a maturity-honest read, and do not treat an early cohort's incomplete pipeline as a final quality verdict. See Lead quality and sales cycle (source: `.agents/skills/linkedin-ads/references/lead-quality-and-sales-cycle.md`) for format- and role-segmented quality discipline.
6. Rank actions by expected pipeline impact, confidence, reversibility, and the account's actual budget tolerance for this channel's cost structure.

## Rules

- Do not evaluate LinkedIn cost-per-click or cost-per-lead against a consumer-platform benchmark; the platforms serve structurally different audiences and buying contexts, and the comparison produces a false conclusion about efficiency.
- Do not treat lead volume as the business outcome; for a long sales cycle, immediate lead metrics are a weak, early signal and a business-outcome conclusion requires the lead-to-revenue cohort maturity check `$retention-economics` provides.
- Do not build attribute-based targeting from an assumed persona when `$icp-jtbd` has actual buying-committee and buyer-role evidence available; use the evidence.
- Do not treat every buyer role identically; a campaign reaching only one role in a multi-stakeholder buying committee is reaching part of the decision, and the plan should state which role or roles it targets and which it does not.
- Do not claim account-based targeting reached a target account without confirming the platform's actual match rate for that account list; a low match rate means the campaign is reaching a different, broader audience than the plan states.
- Do not conflate Lead Gen Form volume with off-platform landing-page volume when comparing cost per lead; the two carry different friction and typically different downstream qualification rates, and a raw comparison without that context misleads.

## Output

Plan: targeting approach (account-based or attribute-based) with rationale; format selection matched to buying-committee role and funnel stage; Lead Gen Form versus landing-page decision; cost expectations against this account's own economics; measurement plan matched to sales-cycle length; capacity required; exact status.

Diagnosis: observed change; competing explanations (targeting-match-rate shift, format change, seasonality tied to B2B budget cycles, sales-cycle-stage immaturity misread as a decline) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm targeting approach and its rationale are stated; format matches the buying-committee role and funnel stage rather than defaulting to one format; cost conclusions are checked against this account's own economics rather than a consumer-platform benchmark; lead-quality claims route through `$retention-economics`'s maturity-honest cohort method rather than asserting a final read on an immature cohort; and account-based match rate is confirmed rather than assumed.

## Source: `.agents/skills/linkedin-ads/references/account-and-firmographic-targeting.md`

# Account and Firmographic Targeting

LinkedIn's defining targeting advantage over consumer platforms is professional and firmographic data: job title, seniority, function, skills, industry, company size, and — where the business runs account-based marketing — a defined target account list. Building this well is largely an evidence problem: targeting should reflect who actually buys and how, not an assumed persona.

## Account-based targeting

Match a target account list (from `$icp-jtbd` or the business's own account-based marketing program) against the platform's account targeting. Confirm the actual match rate — the platform will report what share of the uploaded list it could match and target — before assuming the campaign reaches the intended accounts. A low match rate (common with smaller or less LinkedIn-active companies) means the campaign is reaching a narrower or different set of accounts than the plan states, and budget or expectations should be adjusted accordingly rather than assumed to be working as planned.

Within a matched account, layer buyer-role targeting (seniority, function, title) to reach the actual buying-committee members rather than the entire company; targeting an entire matched account indiscriminately dilutes spend across roles with no purchasing influence.

## Attribute-based targeting

Where no defined account list exists, build targeting from `$icp-jtbd`'s buyer-role and buying-situation evidence: which functions and seniority levels are actually involved in this purchase decision, not a generic "decision-maker" assumption. Layer firmographic filters (company size, industry) to the segment `$marketing-intake` established as the primary business outcome's actual addressable market.

## Buying-committee coverage

State explicitly which buyer roles a given campaign targets and which it does not. A multi-stakeholder purchase (common in B2B) is rarely won by reaching one role; a plan should either cover the relevant roles with role-appropriate messaging, or state clearly that it targets only part of the committee and why.

## Rules

- Confirm match rate for any account-based campaign before reporting reach or budget efficiency; an unconfirmed match rate is an unverified claim about who the campaign actually reaches.
- Do not target an entire matched company indiscriminately when buyer-role evidence is available to narrow to the actual buying committee; broad within-account targeting wastes spend on non-influential roles.
- Do not assume a "decision-maker" title-based filter reflects the actual buying committee without `$icp-jtbd` evidence; job titles vary widely across companies and a title-only filter can both include irrelevant roles and exclude actual influencers with different titles.
- Firmographic targeting narrows reach; do not stack filters (industry, company size, seniority, function) so tightly that the addressable audience becomes too small to deliver meaningfully, without checking estimated audience size before launch.

## Source: `.agents/skills/linkedin-ads/references/lead-quality-and-sales-cycle.md`

# Lead Quality and Sales Cycle

LinkedIn's cost structure and typical use case — reaching a longer B2B sales cycle — make lead-quality discipline especially load-bearing. A cost-per-lead number in isolation, without a maturity-honest read on what those leads actually become, is close to meaningless for a channel whose economics depend entirely on pipeline and revenue, not lead volume.

## Method

1. Establish the lead stage definitions and Customer Relationship Management outcome mapping per `$marketing-intake` before evaluating any LinkedIn lead performance.
2. Route lead-to-revenue evaluation to `$retention-economics`'s lead-to-revenue cohort method; cohort by lead-creation date, track open share, and do not treat an immature cohort's interim conversion rate as final.
3. Segment lead quality by format and targeting approach: Lead Gen Form leads (low friction, pre-filled, typically lower intent signal per lead) versus off-platform landing-page leads (higher friction, typically stronger intent signal but fewer total leads) should be evaluated separately, not blended into one quality figure.
4. Segment by buyer role reached; a lead from a role with genuine purchasing influence and a lead from a role with none carry different pipeline value even at the same cost per lead.

## Rules

- Do not compare LinkedIn's cost per lead against a consumer-platform channel's cost per lead without accounting for the fundamentally different intent signal and sales-cycle length; the comparison as a raw number misleads regardless of caveat placement.
- Do not conclude a campaign underperformed from an early-period lead volume or cost figure alone when the sales cycle has not had time to mature; check the open share per `$retention-economics`'s lead-to-revenue method before concluding quality declined.
- Do not blend Lead Gen Form and landing-page lead quality into one figure; report them separately since they carry different friction and typically different downstream qualification rates.
- A budget cycle tied to B2B fiscal quarters or annual planning periods can produce real seasonality in both lead volume and deal velocity; check for this before attributing a change to campaign performance.
- Where a claim about a LinkedIn lead's incremental contribution to pipeline is needed, route the causal question to `$tracking-measurement`; this reference covers quality segmentation and maturity discipline, not incrementality method selection.

## Source: `.agents/skills/programmatic/SKILL.md`

---
name: programmatic
description: Plan or diagnose demand-side-platform display and video buying across the open exchange — supply-path optimization, inventory quality and fraud screening, and viewability/verification; not for a single walled-garden platform, and not for the underlying creative or audience-strategy decision.
---

# Programmatic

Classify each buying method, verification approach, or economics claim with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). Programmatic buys inventory aggregated from thousands of largely unknown sites and apps through a multi-party supply chain — a fundamentally different risk profile than a single walled-garden platform (`$meta-ads`, `$tiktok-ads`, `$linkedin-ads`, `$youtube-ads`), where the platform itself curates and is directly accountable for its own inventory. Inventory quality, supply-chain cost, and fraud are the defining concerns here, not creative or targeting alone.

## Context

Primary business outcome and funnel objective; demand-side platform in use and its available inventory sources (open exchange, private marketplace, programmatic guaranteed); available first-party or contextual targeting signal, since third-party-cookie-based audience targeting is increasingly unreliable or unavailable; brand-safety and content-adjacency requirements; and whether independent verification (viewability, invalid-traffic, brand-safety measurement) is in place.

## Method

1. Assess the buying method against the objective: open exchange (broadest reach, least curated, highest fraud/quality risk), private marketplace (negotiated access to specific publishers, better quality control), and programmatic guaranteed (reserved inventory at a fixed price, most predictable but least flexible) each trade reach against quality and cost predictability differently — state which is used and why.
2. Screen inventory quality and supply-chain cost before scaling spend. See Supply-path optimization (source: `.agents/skills/programmatic/references/supply-path-optimization.md`).
3. Require independent, third-party verification for viewability, invalid traffic, and brand safety rather than accepting the DSP's or a single seller's self-reported figures alone. See Verification and fraud screening (source: `.agents/skills/programmatic/references/verification-and-fraud-screening.md`).
4. Set targeting from available first-party or contextual signal, and state explicitly where third-party-cookie-dependent targeting is degraded or unavailable rather than assuming a targeting configuration still functions as it did in a prior period.
5. Define the measurement plan against the funnel objective, applying the same view-through discipline `$youtube-ads` applies: a served impression is not a caused outcome, and any causal claim should be graded on `$tracking-measurement`'s evidence ladder.
6. Rank actions by expected business impact, confidence, reversibility, and the account's actual capacity to monitor a fragmented, multi-party supply chain on an ongoing basis.

## Rules

- Do not accept a DSP's or single supply-side platform's self-reported viewability, brand-safety, or invalid-traffic figures as sufficient; require independent third-party verification, since the reporting party frequently has a financial interest in favorable numbers.
- Do not treat open-exchange inventory as equivalent in quality to a private marketplace or programmatic-guaranteed deal without evidence; the open exchange includes the least curated, highest-fraud-risk supply by construction.
- Do not scale spend into inventory whose supply path has not been screened; an unscreened path can route through multiple resellers each taking a fee, and can include made-for-advertising sites optimized to generate ad calls rather than genuine audience engagement.
- Do not present a served or viewable impression as a caused business outcome; grade any resulting claim on the causal evidence ladder in `$tracking-measurement`, the same discipline `$youtube-ads` applies to view-through.
- Do not assume a targeting configuration that relied on third-party cookies still functions as in a prior period without confirming current signal availability; state degraded or unavailable targeting explicitly rather than reporting reach as if unaffected.
- Do not conflate cost per impression across supply paths with different fee structures; a lower headline cost per impression through a longer, fee-stacked resale path can be more expensive in total than a shorter, direct path with a higher headline rate.

## Output

Plan: buying method and rationale; supply-path screening approach; verification vendor and metrics in place; targeting signal available and any degradation disclosed; measurement plan with evidence-level expectation; capacity to monitor ongoing supply quality; exact status.

Diagnosis: observed change (cost, viewability, invalid-traffic rate, or outcome); competing explanations (supply-path shift, verification-vendor methodology change, seasonality, targeting-signal degradation) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm the buying method is stated with rationale rather than defaulted; supply-path screening happened before scaling spend; verification relies on an independent third party rather than the seller's self-report; targeting-signal degradation is disclosed rather than assumed away; no served impression is presented as a caused outcome without evidence-level grading; and total supply-chain cost, not headline cost per impression alone, informs any efficiency conclusion.

## Source: `.agents/skills/programmatic/references/supply-path-optimization.md`

# Supply-Path Optimization

The same ad impression can frequently be bought through multiple different paths — direct from the publisher, or through one or more reselling supply-side platforms — each taking a fee along the way. Unscreened, a buyer can end up paying a stack of intermediary fees for inventory that could have been bought more cheaply and with better visibility through a shorter, direct path.

## What to check

For each significant supply source: how many intermediary steps sit between the demand-side platform and the actual publisher, and what each takes as a fee, where visible. Whether the same publisher's inventory is available through a shorter path (direct or through a preferred supply-side platform relationship) at a lower effective cost. Whether the specific domains or apps being bought are declared by the publisher-facing supply-side platform accurately (a mismatch between declared and actual destination is itself a red flag for arbitrage or fraud). And whether spend concentration in the open exchange versus private marketplace or guaranteed deals matches the account's actual risk tolerance for inventory quality.

## Made-for-advertising sites

A meaningful share of open-exchange inventory can consist of sites and apps built primarily to generate ad-call volume — high page-refresh rates, minimal genuine content, auto-playing video stacked to maximize impression count — rather than sites with real audience engagement. This inventory can pass basic brand-safety keyword screens while still delivering little genuine attention. Screen for known made-for-advertising indicators (site-quality lists from verification vendors, unusually high impression-to-engagement ratios, minimal content-to-ad ratio) rather than relying on category or keyword safety alone.

## Method

1. Request supply-path transparency reporting from the demand-side platform where available, showing the actual chain of intermediaries for spend.
2. Identify the highest-spend supply sources and check for shorter available paths to the same inventory.
3. Cross-reference inventory against independent site-quality and made-for-advertising screening lists rather than relying on the DSP's default brand-safety category filters alone.
4. Consolidate spend toward verified, direct or short-path, non-made-for-advertising sources progressively, rather than making one large abrupt shift that could disrupt delivery or introduce a different unverified change at the same time.

## Rules

- Do not judge inventory cost by headline cost-per-impression alone; the effective cost including all intermediary fees along the actual supply path is the decision-relevant figure.
- Do not assume a brand-safety category filter screens out made-for-advertising inventory; these sites can pass keyword and category screens while still lacking genuine audience engagement.
- A supply-path change is a real change to what inventory is being bought; evaluate it with before/after discipline rather than assuming a consolidation toward "better" paths is automatically an improvement without checking delivered performance.
- Do not treat a declared publisher domain as verified without independent confirmation where fraud or arbitrage risk is a concern; a mismatch between declared and actual destination is a specific, checkable red flag.

## Source: `.agents/skills/programmatic/references/verification-and-fraud-screening.md`

# Verification and Fraud Screening

Programmatic's fragmented, multi-party supply chain creates more opportunity for inflated or fabricated metrics than a single walled-garden platform, where the platform itself is directly accountable for its own reporting. Independent, third-party verification is the primary defense — not a nice-to-have add-on.

## What to verify independently

**Viewability** — whether an impression was actually rendered in a viewable position on screen, per an industry-recognized standard (such as the Media Rating Council's viewability definition), rather than accepting a served-impression count as equivalent to a viewable one.

**Invalid traffic** — bot and non-human traffic, both general invalid traffic (detectable via known patterns) and sophisticated invalid traffic (harder to detect, often indistinguishable from genuine traffic without specialized detection). A meaningful invalid-traffic rate inflates delivered volume without corresponding genuine audience reach.

**Brand safety and suitability** — whether ads served adjacent to content the business would consider unsafe or unsuitable, measured against a stated policy rather than a generic default.

## Method

1. Confirm an independent, third-party verification vendor is in place and its methodology is current — verification standards and detection methods evolve, and a vendor relationship or configuration from a prior period should be periodically reconfirmed rather than assumed still adequate.
2. Compare the DSP's or seller's self-reported metrics against the independent verification vendor's figures; a persistent, large discrepancy is itself a signal worth investigating rather than defaulting to either source as automatically correct.
3. Set explicit thresholds for acceptable viewability rate and invalid-traffic rate, and treat inventory or supply sources falling outside them as a screening and potential exclusion candidate, not a rounding error.
4. Where brand-safety or suitability incidents occur, document them and adjust exclusion lists rather than relying solely on a static category-based safety setting to prevent recurrence.

## Rules

- Do not accept viewability, invalid-traffic, or brand-safety figures from the party financially benefiting from favorable numbers (the DSP, the supply-side platform, or the individual seller) as sufficient verification on their own.
- Do not treat a low invalid-traffic rate as evidence of overall inventory quality; sophisticated invalid traffic is specifically designed to evade basic detection, and a clean basic-IVT reading does not rule it out.
- A large, persistent discrepancy between self-reported and independently verified metrics is a fraud or misconfiguration signal requiring investigation, not a rounding difference to average away.
- Do not treat verification as a one-time setup; detection methods and fraud tactics change, and a verification configuration should be periodically reconfirmed as current.
