<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Influencer and Affiliate Marketing

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/influencer-marketing/SKILL.md`

---
name: influencer-marketing
description: Plan, vet, contract, or evaluate influencer and creator partnerships — audience authenticity, disclosure compliance, usage rights, and compensation structure; not for paid-media buying, and not a substitute for a legal review of the actual contract.
---

# Influencer Marketing

Classify each vetting method, contract structure, or evidence claim with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). This is a relationship and contract-based channel, not a platform auction — there is no bid, no algorithm to diagnose, and the central risks are audience authenticity, legal compliance, and unclear usage rights rather than delivery mechanics.

This skill is not a substitute for legal review of an actual influencer contract or a compliance determination on a specific disclosure; it identifies what the contract and disclosure must address and flags gaps, and a qualified reviewer should confirm the specifics for the applicable jurisdiction and platform.

## Context

Primary business outcome and whether this partnership is intended for awareness, consideration, or direct response, since that determines both creator selection criteria and measurement approach; budget and compensation structure under consideration (flat fee, commission/affiliate, gifting, or a hybrid); whether the business wants usage rights to repurpose creator content as paid advertising (whitelisting); the applicable jurisdictions and platforms' current disclosure requirements; and the business's tolerance for the creator's independent editorial control over the content.

## Method

1. Vet candidate creators on audience authenticity and actual fit, not follower count. See Audience authenticity and fit (source: `.agents/skills/influencer-marketing/references/audience-authenticity-and-fit.md`).
2. Structure compensation to the partnership's actual goal — flat fee for a guaranteed deliverable, commission for a performance-aligned partnership, gifting only where the relationship and expected content genuinely justify it — and state the tradeoffs of the structure chosen. See Compensation structure (source: `.agents/skills/influencer-marketing/references/compensation-structure.md`).
3. Confirm disclosure requirements will be met per current platform and regulatory guidance for the applicable jurisdiction; do not assume a disclosure format is compliant without checking it is current, since disclosure requirements are enforced and do change.
4. Define usage rights explicitly before content is produced: which content, on which channels, for how long, and whether it includes the right to run creator content as paid media; an unclear or unaddressed usage-rights term is a common and expensive dispute.
5. Define the measurement plan honestly: influencer content typically has no clean platform attribution the way paid media does; use unique codes, links, or landing pages where possible, and grade any resulting causal claim on `$tracking-measurement`'s evidence ladder rather than presenting correlated activity as proven effect.
6. Rank creator and format choices by expected business impact, confidence, reversibility (a single-post trial before a longer commitment), and the creator relationship's actual production reliability.

## Rules

- Do not select a creator primarily on follower count or reach; audience authenticity and fit to the actual buyer are more decision-relevant, and a large but low-authenticity or poorly-fit audience produces spend with little return.
- Do not present influencer-driven sales or traffic as a proven incremental effect without a design that can support the claim (unique codes/links, a holdout, or a comparable control period); absent that, report it as correlated activity, capped low on the causal evidence ladder.
- Do not omit or leave ambiguous the usage-rights term in a partnership agreement; the business's ability to repurpose the content as paid media, and for how long, must be explicit before content is produced, not negotiated retroactively.
- Do not assume a disclosure format used previously remains compliant; verify current requirements for the applicable jurisdiction and platform before content goes live, and never advise omitting or obscuring required disclosure to preserve an "authentic" feel.
- Do not treat gifting as free; gifted product still carries a genuine cost and an expectation of content, and the arrangement should be scoped like any other compensation structure with a stated expectation.
- Do not fabricate or assume a creator's audience demographics, engagement authenticity, or past performance without a verifiable source; flag an unverifiable claim rather than accepting it as given.
- This skill does not review or draft binding legal language; identify what a contract must address and flag gaps, and route the actual agreement to qualified legal review.

## Output

Plan: partnership goal and funnel stage; creator vetting criteria and audience-authenticity check; compensation structure and rationale; usage-rights terms; disclosure compliance check; measurement plan with stated evidence level; capacity and relationship-reliability considerations; exact status.

Evaluation: what compensation structure was used; whether usage rights were addressed; disclosure compliance status; measurement evidence level for any performance claim; recommended next step (expand, hold, discontinue).

## QA

Confirm creator selection is evidenced by audience authenticity and fit rather than follower count alone; compensation structure matches the partnership's stated goal; usage rights are explicit rather than assumed; disclosure requirements are checked as current rather than assumed from a prior campaign; any performance claim is graded on the causal evidence ladder rather than presented as proven; and no contractual or compliance determination is presented as final without flagging that qualified legal review is required.

## Source: `.agents/skills/influencer-marketing/references/audience-authenticity-and-fit.md`

# Audience Authenticity and Fit

Follower count is the weakest signal available for creator selection. The two that actually predict a partnership's return are audience authenticity (are the followers real, engaged people) and audience fit (do they overlap with the actual buyer this business needs to reach).

## Authenticity signals

Engagement rate relative to follower count, checked against category norms rather than a fixed threshold — normal engagement rates vary widely by platform, format, and niche. A follower count that grew in sudden, unexplained spikes rather than steady accumulation. Comment quality — genuine, specific comments versus generic or bot-pattern comments. Follower geography and demographic plausibility relative to the creator's stated audience and content focus. A history of promotional content that reads as genuine versus content that reads as purchased or coerced.

None of these signals is individually conclusive; a creator's authenticity assessment should weigh several together rather than resting on one metric.

## Fit signals

Whether the creator's actual audience — not just their content topic — overlaps with `$icp-jtbd`'s buyer evidence for this business. A creator whose content topic matches the product but whose audience skews away from the actual buyer (wrong life stage, wrong purchasing power, wrong geography) is a fit mismatch regardless of topical relevance.

Whether the creator's typical content style and tone fit how this business wants to be represented; a mismatch here produces content that undersells the partnership even with an authentic, well-fit audience.

Whether the creator has a credible history with the product category — prior genuine use, expertise, or interest — versus being a generic promotional vehicle with no category connection; audiences increasingly discount content from a creator with no credible connection to what they're promoting.

## Method

1. Gather engagement and audience data from the platform's own creator/business tools where available, not third-party estimates alone.
2. Cross-check authenticity signals against category norms rather than a universal threshold.
3. Assess fit against `$icp-jtbd`'s buyer evidence, not against the creator's follower count or the content topic alone.
4. For a first partnership with an unproven creator, prefer a smaller, reversible commitment (a single post or short campaign) before a longer-term or exclusive arrangement.

## Rules

- Do not treat follower count as a proxy for reach quality; a smaller, highly authentic and well-fit audience frequently outperforms a larger, low-authenticity one.
- Do not accept a creator's self-reported audience data without a platform-verifiable source where one exists; flag unverifiable claims rather than treating them as given.
- Do not assume category-topic relevance substitutes for audience fit; check both independently.
- Do not commit to a long-term or exclusive arrangement with an unproven creator before a smaller reversible trial, absent strong independent evidence of fit and authenticity.

## Source: `.agents/skills/influencer-marketing/references/compensation-structure.md`

# Compensation Structure

The compensation model shapes both cost predictability and the creator's incentive — each structure trades one for the other, and the right choice depends on the partnership's actual goal, not a default preference.

## Structures

| Structure | Cost predictability | Creator incentive | Fits |
|---|---|---|---|
| Flat fee | Fixed, known upfront | Deliver the agreed content; no direct incentive tied to resulting sales | A guaranteed deliverable, brand-safety-sensitive content, or a creator whose value is reach/credibility rather than direct conversion |
| Commission / affiliate | Variable, scales with results | Directly incentivized to drive measurable action | A partnership where attribution (unique codes/links) is feasible and the creator's audience is response-oriented |
| Gifting | Low direct cost, but product/service cost is real | Weak, informal incentive; content is not guaranteed | Early-stage relationship-building, or categories where genuine product experience is itself the credible signal — not a substitute for real compensation when guaranteed content is needed |
| Hybrid (flat fee + commission) | Partially predictable | Balances guaranteed deliverable with performance incentive | Most sustained partnerships beyond a single trial post |

## Method

1. State the partnership's actual goal (awareness, consideration, direct response) before selecting a structure; a commission-only structure on an awareness-goal partnership misaligns incentive with intent, since awareness content rarely drives an immediately attributable action.
2. For commission/affiliate structures, confirm attribution is actually feasible (unique code, tracked link, dedicated landing page) before promising the creator performance-based pay tied to a metric that cannot be reliably measured.
3. For gifting, state the actual expectation — is content guaranteed, or is the gift purely goodwill with no obligation — and do not treat an ambiguous gifting arrangement as equivalent to a paid partnership with deliverables.
4. Document payment timing, deliverable specifics, and any usage-rights fee separately from the base compensation; usage rights (repurposing creator content as paid media) commonly carry a separate negotiated fee and should not be assumed included in a flat content fee.

## Rules

- Do not default to gifting as a lower-cost alternative to real compensation when the partnership requires guaranteed, reliable content; gifting does not obligate deliverables the way a paid agreement does.
- Do not promise commission-based pay on a metric that cannot actually be tracked; this creates a dispute risk and misrepresents the partnership's true economics to the creator.
- Do not assume usage rights are included in a base compensation figure without confirming; treat it as a separate, explicit term.
- A compensation structure is a real cost even when described as "free" (gifting) or "performance-only" (commission); report the true expected cost, including product cost and the commission's expected payout at forecast volume, when comparing partnership options.

## Source: `.agents/skills/affiliate-marketing/SKILL.md`

---
name: affiliate-marketing
description: Manage or evaluate affiliate and partner programs — commission structure, attribution integrity, fraud and brand-bidding detection, and network versus direct-partner decisions; not for influencer relationship vetting, and not for the underlying paid-search brand-protection enforcement.
---

# Affiliate Marketing

Classify each commission model, attribution method, or fraud-detection heuristic with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). This is a performance-based, publisher-network channel: the defining risk is not creative or targeting quality but attribution integrity — whether the commission paid actually reflects incremental value the affiliate created, and whether the tracked conversion was legitimately earned.

Related but distinct: `$influencer-marketing` covers vetting an individual creator relationship and its compensation; this skill covers a publisher/partner network paying commission on tracked conversions, where fraud and attribution-gaming risk is structurally higher because the incentive is directly tied to the tracked action.

## Context

Primary business outcome and commission budget or acceptable cost-of-sale ceiling; program structure under consideration (in-house direct partners, third-party affiliate network, or both); attribution window and cookie/tracking method in use; current partner mix (content/review sites, coupon/deal sites, comparison sites, loyalty/cashback sites, sub-affiliate networks); and whether the business's branded search terms are being bid on by any partner.

## Method

1. Confirm the attribution mechanism (cookie duration, last-click versus another model, cross-device handling) and its known integrity gaps before evaluating any commission report; a broken or gameable attribution mechanism invalidates the payout logic built on top of it. See Attribution integrity (source: `.agents/skills/affiliate-marketing/references/attribution-integrity.md`).
2. Screen the partner mix for the specific fraud and gaming patterns common to this channel — brand bidding, cookie stuffing, coupon-code leakage, incentivized or fake traffic. See Fraud and brand-bidding detection (source: `.agents/skills/affiliate-marketing/references/fraud-and-brand-bidding-detection.md`).
3. Structure commission to reward genuinely incremental value: differentiate content/influence partners from coupon/loyalty partners whose typical role is capturing a conversion already in motion rather than creating it, and do not pay both the same rate for structurally different contribution.
4. Assess whether direct partnership or a third-party network fits the program's scale and oversight capacity; a network provides reach and infrastructure but adds a layer between the business and partner behavior, including sub-affiliates the business may never directly vet.
5. Confirm disclosure compliance for affiliate links per current requirements, consistent with `$influencer-marketing`'s disclosure discipline where a partner is also a content creator.
6. Rank program changes by expected business impact, confidence, reversibility, and the oversight capacity actually available to monitor partner behavior on an ongoing basis.

## Rules

- Do not treat a tracked affiliate conversion as automatically incremental; a last-click attribution model routinely credits a coupon or cashback partner for a sale the customer was already going to complete, and a commission-structure decision should reflect that risk rather than assume every tracked conversion was caused by the affiliate.
- Do not allow a partner to bid on the business's own branded search terms without an explicit, monitored policy; unrestricted brand bidding by affiliates typically captures spend the business would have received directly at zero incremental cost, and frequently raises the business's own paid-search costs by adding a competing bidder on its own brand.
- Do not accept a sudden spike in a partner's conversion volume as a positive signal without checking for cookie-stuffing or other attribution-gaming patterns; an unexplained spike is a fraud-screening trigger, not a reason to increase that partner's commission.
- Do not pay identical commission rates to structurally different partner types (a content partner that genuinely influences a purchase decision versus a coupon-code partner that intercepts an already-decided purchase) without deliberately deciding that is the intended structure; the default should be evaluated, not assumed.
- Do not onboard a sub-affiliate network's full downstream partner list without a stated oversight or audit mechanism; a business is typically still responsible for its overall program's compliance and fraud exposure even when a sub-affiliate's specific behavior was not directly visible.
- Route a causal or incrementality claim about the program's overall contribution to `$tracking-measurement`; this skill screens for attribution-integrity defects at the partner level, it does not itself establish the program's incremental business value.

## Output

Program review: attribution mechanism and known integrity gaps; partner mix by type; fraud/brand-bidding screening findings; commission structure and its incentive alignment; network versus direct-partner assessment; disclosure compliance status; oversight capacity; recommended actions; exact status.

Partner-level flag: partner identity; observed anomaly or gaming pattern; evidence; recommended action (monitor, restrict, suspend, terminate); confidence.

## QA

Confirm the attribution mechanism's integrity gaps are stated before any commission conclusion; brand-bidding policy is explicit and monitored; a conversion-volume spike triggers fraud screening before a commission increase; commission structure differentiates partner types deliberately rather than by default; sub-affiliate exposure is acknowledged with a stated oversight mechanism; and any incrementality claim about the program is routed to `$tracking-measurement` rather than asserted here.

## Source: `.agents/skills/affiliate-marketing/references/attribution-integrity.md`

# Attribution Integrity

Affiliate commission is paid on a tracked event, almost always last-click within a cookie window. That mechanism has well-known structural weaknesses that directly determine whether a paid commission reflects genuine incremental value — understanding them is a prerequisite to evaluating any commission report, not an optional deep-dive.

## Known structural weaknesses

**Last-click bias.** The affiliate credited is whichever partner's link the customer clicked last before converting, regardless of what actually persuaded the purchase decision. A content partner that built genuine purchase intent earlier in the journey routinely loses credit to a coupon or cashback partner clicked moments before checkout.

**Cookie duration and overwriting.** A longer cookie window increases the chance an unrelated later click overwrites an earlier, more influential one. Confirm the cookie duration in use and who it favors — typically the partner positioned closest to checkout.

**Cross-device and cross-session gaps.** A customer who researches on one device and purchases on another breaks cookie-based tracking entirely in many configurations, understating some partners' contribution and potentially crediting none.

**Coupon-code leakage.** A customer who searches for a coupon code mid-checkout — regardless of what originally drove them to the site — can trigger credit to a coupon-site partner that did not create the original demand. This is one of the most common ways tracked commission diverges from actual incremental contribution.

## Method

1. Document the actual attribution configuration in use: cookie duration, last-click or another model, cross-device handling, and whether coupon-code entry alone can trigger credit.
2. Identify which partner types are structurally favored by the current configuration (typically checkout-adjacent partners: coupon, cashback, loyalty) and which are structurally disadvantaged (typically upper-funnel content and comparison partners).
3. Where the decision at stake requires knowing the program's actual incremental contribution — not just tracked commission volume — route to `$tracking-measurement` for an incrementality design; this reference documents the tracking mechanism's known bias, it does not itself establish incremental value.
4. Consider a partner-type-differentiated attribution or commission model (e.g., a smaller window or lower rate for checkout-adjacent partner types) as a mitigation once the bias is documented, rather than treating the default last-click configuration as neutral.

## Rules

- Do not report tracked commission volume as a measure of the program's business contribution without stating the attribution mechanism's known bias toward checkout-adjacent partners.
- Do not conclude a partner type (coupon, cashback) is high-performing from tracked conversion volume alone without checking whether coupon-code leakage inflates its apparent contribution.
- Do not assume cross-device customers are a small, ignorable share without checking; the share varies widely by category and audience, and an unchecked assumption can substantially understate true contribution from upper-funnel partners.
- A cookie-duration or attribution-model change is a real change to who gets paid for what; treat it with the same before/after evaluation discipline as any other measurement change, not as a routine configuration tweak.

## Source: `.agents/skills/affiliate-marketing/references/fraud-and-brand-bidding-detection.md`

# Fraud and Brand-Bidding Detection

Because affiliate commission is directly tied to a tracked action, this channel has a structurally higher incentive for gaming than most others in this system — the partner's payment depends on triggering the tracked event, not on genuinely influencing the customer.

## Common patterns

**Cookie stuffing.** A partner drops tracking cookies on users who never actually saw or clicked a genuine affiliate link — via hidden iframes, forced redirects, or browser-extension injection — so that a later, unrelated purchase is credited to them. Detect via unusually high click-to-cookie ratios, conversion patterns disconnected from any visible traffic source, or a partner's reported clicks that do not correspond to any real referral pattern.

**Brand bidding.** A partner bids on the business's own branded search terms, often outranking the business's own ad or landing in front of an organic result the business would have received for free, then captures commission on a sale that required no incremental effort from the partner. This both pays commission for a sale the business would likely have gotten anyway and can raise the business's own paid-search costs by adding a competing bidder on its own brand.

**Coupon-code leakage and poaching**, covered in Attribution integrity (source: `.agents/skills/affiliate-marketing/references/attribution-integrity.md`), is a milder but far more common version of the same underlying problem: capturing credit for a purchase already in motion.

**Incentivized or fake traffic.** Traffic driven through pay-to-click schemes, bot networks, or explicitly incentivized clicks (users paid or rewarded to click, regardless of genuine interest) inflates click and sometimes conversion metrics without real customer intent behind them.

## Method

1. Screen partner-level metrics for anomalies before evaluating raw performance: unusually high conversion rate relative to category norms, a click pattern with no plausible traffic source, or a conversion rate that moves sharply with no corresponding change in the partner's actual promotional activity.
2. Establish and monitor an explicit brand-bidding policy: whether partners may bid on branded terms at all, and if so, under what restriction (exact match only, must not outrank the business's own ad, must use approved ad copy). Check actual bidding behavior against the stated policy, not just the policy's existence.
3. For a suspected cookie-stuffing pattern, cross-reference the partner's claimed traffic source against server-side or third-party verification where available, rather than accepting the network's or partner's self-reported numbers alone.
4. Treat an unexplained spike in any partner's volume as a screening trigger, not a success signal, until the anomaly is explained.

## Rules

- A brand-bidding violation is not a minor policy breach; it typically represents commission paid for demand the business already owned, and should be enforced (restrict, suspend, terminate) rather than tolerated for the sake of volume.
- Do not accept a partner's self-reported traffic source or promotional activity as sufficient verification for a flagged anomaly; require independent or platform-level confirmation where available.
- Do not treat a high-converting partner as automatically legitimate; a suspiciously high conversion rate relative to category norms is itself a fraud-screening signal, not proof of quality.
- Enforcement action (restrict, suspend, terminate) against a partner is a real relationship and revenue decision; state the evidence and confidence level supporting it explicitly rather than acting on a single ambiguous signal.
