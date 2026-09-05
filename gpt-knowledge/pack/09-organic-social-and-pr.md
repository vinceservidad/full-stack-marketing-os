<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Organic Social and Public Relations

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/organic-social/SKILL.md`

---
name: organic-social
description: Plan or diagnose unpaid social content strategy — platform-native format, posting cadence, community management, and algorithm-distribution fit; not for paid/boosted campaigns on any platform, and not for a business outcome claim from reach or engagement alone.
---

# Organic Social

Classify each content pattern, cadence rule, or distribution claim with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). Organic social has no bid, no budget lever, and no platform-native attribution to a business outcome — the entire distribution mechanism is an undocumented algorithm the business does not control, which makes this the platform-currency-sensitive discipline in the system and the one furthest from a controlled channel.

Paid campaigns on any platform — including boosted or Spark-Ad versions of organic content — are owned by that platform's own skill (`$meta-ads`, `$tiktok-ads`, `$linkedin-ads`, `$youtube-ads`). This skill covers unpaid, algorithmically-distributed content only.

## Context

Platforms in scope and their current documented algorithm behavior per `PLATFORM-CURRENCY.md`; primary goal for organic presence — audience/community building, customer service and reputation, top-of-funnel content that feeds paid creative testing, or search-adjacent discovery (some platforms function as a search surface); available content production capacity per platform, since native format requirements differ meaningfully across platforms; and whether any attribution mechanism (bio link tracking, unique promo codes) exists to connect organic activity to a business outcome at all.

## Method

1. Confirm current algorithm-distribution behavior per platform before setting content or cadence strategy; do not carry forward an assumed distribution mechanic from a prior period or from a different platform without checking `PLATFORM-CURRENCY.md`. See Algorithm distribution fit (source: `.agents/skills/organic-social/references/algorithm-distribution-fit.md`).
2. Set content strategy per platform's actual native format and audience behavior — a format or posting pattern that performs on one platform frequently does not transfer unedited to another, the same discipline `$tiktok-ads` applies to paid creative, applied here to organic.
3. Set posting cadence and community-management expectations against actual production and response capacity; an unsustainable cadence degrades both content quality and response time, and a plan that cannot be sustained is not a plan. See Cadence and community management (source: `.agents/skills/organic-social/references/cadence-and-community-management.md`).
4. Where organic content is a source for paid creative testing (a native-style post later run as a paid ad on `$tiktok-ads` or boosted on `$meta-ads`), state that connection explicitly and route the paid decision to the owning channel skill.
5. Define what can and cannot be measured: reach, engagement, and follower growth are visible and real, but a business-outcome connection requires an actual attribution mechanism (tracked bio link, unique code); state which applies and do not claim a business outcome from engagement metrics alone.
6. Rank actions by expected value to the stated goal, confidence, reversibility, and actual production/community-management capacity.

## Rules

- Do not claim a documented algorithm change or ranking factor without a current source; distinguish official platform documentation, observed account behavior, industry inference, and unknowns per `PLATFORM-CURRENCY.md`, the same discipline `$seo` applies to search algorithm claims.
- Do not present engagement rate, reach, or follower growth as a business outcome; they are delivery and audience-response signals, and a business-outcome claim requires a stated attribution mechanism connecting the activity to it.
- Do not recommend a posting cadence the account cannot sustain with its actual production capacity; a burst-then-abandon pattern typically underperforms a lower, sustainable cadence.
- Do not reuse a content format or hook pattern across platforms unedited; assess native fit per platform the way `$tiktok-ads` assesses it for that platform specifically.
- Community management (responding to comments, messages, and mentions) carries real brand-reputation and customer-service weight; do not treat unanswered public engagement as a low-priority backlog when it is visible to the account's full audience.
- A single viral post does not establish a durable content strategy; require replication before generalizing a format or topic that performed once into a standing content pillar.
- Route any paid amplification decision (boosting a post, running organic content as a paid ad) to the owning platform skill; this skill assesses organic content and distribution, not paid budget allocation.

## Output

Plan: platforms in scope with current algorithm-behavior status; content strategy per platform's native format; cadence matched to production capacity; community-management expectations; measurement approach with attribution mechanism stated or its absence disclosed; paid-amplification candidates flagged for the owning channel skill; exact status.

Diagnosis: observed change in reach, engagement, or follower growth; competing explanations (algorithm update, format-fit mismatch, cadence change, seasonality, a single post's outsized influence on the average) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm algorithm-distribution claims are checked against current platform documentation rather than assumed; content and cadence are matched to platform-native format and actual capacity; no engagement metric is presented as a business outcome without a stated attribution mechanism; a single high-performing post is not generalized into a standing strategy without replication; and any paid-amplification decision is routed to the owning channel skill rather than decided here.

## Source: `.agents/skills/organic-social/references/algorithm-distribution-fit.md`

# Algorithm Distribution Fit

Organic reach is entirely mediated by a platform's algorithm, which the business does not control, cannot see the internals of, and which changes without notice. This makes distribution the single most platform-currency-sensitive question in the entire system — more so than any paid channel, where at least a bid and budget provide a controllable lever.

## What can actually be known

Officially documented ranking or distribution factors (rare, and platforms disclose selectively); account-visible behavior observed directly in the account's own analytics (a real signal, but specific to that account and period, not necessarily generalizable); industry-reported patterns and testing (inference, useful for hypothesis generation, not fact); and unknowns, which are the majority of any platform's actual distribution logic.

Keep these four categories separate in every claim about why content performed or didn't. A claim like "the algorithm favors X" should state which category it falls into.

## Method

1. Before setting strategy, check `PLATFORM-CURRENCY.md` for each platform in scope; do not assume a distribution mechanic observed a year ago, or reported in industry commentary from another period, still holds.
2. Distinguish a genuine algorithm shift from an account-specific issue (a policy strike, a shadow-restriction from a terms-of-service violation, a technical posting error) before concluding the platform's broader distribution changed.
3. When account-visible performance changes, check for competing explanations before crediting or blaming the algorithm: content-format change, posting-time change, a competitor's content shift, seasonal audience behavior, or a single unusually high- or low-performing post skewing a short-window average.
4. Treat platform-provided "best practice" guidance with the same discipline `$google-ads` and `$seo` apply to platform recommendations: an input to consider, not a guarantee, and current guidance can change or be superseded.

## Rules

- Never state a specific algorithmic ranking factor as fact without a named, current source; label it as officially documented, account-observed, industry-inferred, or unknown.
- Do not attribute a reach or engagement change to "the algorithm changed" as a default explanation before checking account-specific and content-specific competing explanations first.
- A distribution pattern observed on one platform does not transfer to another; each platform's algorithm is distinct and a claim from one platform's behavior does not evidence a claim about a different platform.
- Where the platform genuinely offers no visibility into why distribution changed, report that as an honest unknown rather than constructing a plausible-sounding but unverifiable explanation.

## Source: `.agents/skills/organic-social/references/cadence-and-community-management.md`

# Cadence and Community Management

Posting cadence and community response are the two organic-social commitments most likely to be set unsustainably — either from an assumed "best practice" cadence or from underestimating the ongoing effort of monitoring and responding to public engagement.

## Cadence

Set posting frequency from actual sustainable production capacity, not a generic recommendation; a platform-suggested or industry-typical cadence that this account cannot sustain will produce either declining content quality over time or an unpredictable burst-then-gap pattern, both of which typically underperform a lower, consistent cadence.

Match content type to production reality: a cadence built around a content type requiring heavy production (multi-shot video, extensive editing) is a different capacity commitment than one built around lower-production formats (single-shot, text-forward, or repurposed content), and the plan should be honest about which it assumes.

## Community management

Public comments, messages, and mentions on organic content are visible to the account's full audience and carry real brand-reputation and customer-service weight — an unanswered public complaint or question reads differently than an unanswered private support ticket.

Set an explicit response-time expectation and staffing plan for community management proportional to the account's actual audience size and posting cadence; a plan that scales posting volume without scaling response capacity will produce a visibly unattended account.

Distinguish routine engagement response from an emerging issue requiring escalation (a complaint pattern, a misinformation spread, a brewing reputational concern) — route an escalating pattern to `$public-relations` for crisis-communications discipline rather than treating every comment as routine.

## Rules

- Do not set cadence from a platform-suggested or generic industry benchmark without checking it against this account's actual sustainable production capacity.
- Do not treat community management as a low-priority backlog item; it is public-facing and reputational, and unanswered engagement is visible to the full audience, not just the commenter.
- Do not scale posting cadence without scaling community-management capacity proportionally; the two commitments grow together.
- A single post's engagement pattern is not evidence for a cadence decision; assess cadence effects over a sustained period long enough to separate a cadence change's effect from normal post-to-post variance.

## Source: `.agents/skills/public-relations/SKILL.md`

---
name: public-relations
description: Plan media relations, pitch strategy, and crisis-communications response — earned coverage with no purchased placement and no message-control guarantee; not for paid or owned-channel messaging, and not a substitute for legal review of a public statement with real liability exposure.
---

# Public Relations

Classify each pitch strategy, media-relations method, or reputational claim with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). This is the least controllable channel in the system: there is no purchased placement, no algorithm, and no guarantee the resulting coverage reflects the business's intended message — a journalist or outlet retains full editorial control over the actual story, including an angle the business did not intend or would not choose.

This skill is not a substitute for legal review of a public statement carrying real liability exposure (a securities disclosure, a safety incident, an employment matter); it identifies what a statement or response should address and flags legal-review triggers, and a qualified reviewer should confirm the specifics.

## Context

The news hook or newsworthiness basis for the outreach — genuine public relations coverage requires an actual reason a journalist or outlet would cover it, not just a desire for coverage; target media list and its actual fit to the story and audience; whether this is proactive (a planned pitch or announcement) or reactive (crisis or incident response); the business's actual message-control tolerance, since coverage can include context, criticism, or an angle the business did not supply; and legal-review status for any statement with liability exposure.

## Method

1. Assess newsworthiness honestly before building outreach around it; a pitch built on a story with no genuine news hook typically fails regardless of pitch quality, and the diagnosis for low pickup should start there before blaming execution.
2. Build a targeted media list from actual outlet and journalist fit to the story and its likely audience, not from a generic or oversized list; a mismatched pitch to an irrelevant outlet or journalist wastes the relationship and typically produces no coverage.
3. For crisis or reactive communications, follow Crisis communications (source: `.agents/skills/public-relations/references/crisis-communications.md`); response speed, factual accuracy, and legal-review discipline matter more here than in any other communication this system covers.
4. State the message-control tolerance explicitly: earned coverage may include facts, context, or criticism the business did not supply, and a plan should account for that rather than assume the pitch's framing will be reproduced as written.
5. Define the measurement plan honestly per Measurement and evidence limits (source: `.agents/skills/public-relations/references/measurement-and-evidence-limits.md`); media mentions, share of voice, and sentiment are observable signals with no clean causal link to a business outcome, and any resulting claim should be graded on `$tracking-measurement`'s evidence ladder rather than presented as proof of business impact.
6. Rank outreach targets and pitch angles by expected coverage likelihood, confidence, reversibility, and legal-review requirements.

## Rules

- Do not build a pitch or campaign around a story with no genuine newsworthiness; if none exists, name that rather than proceeding with a pitch expected to fail.
- Do not present a business claim to media that exceeds what the business can substantiate; never fabricate a benchmark, result, credential, or customer quotation for press purposes, per the same standard `AGENTS.md` applies to any other deliverable.
- Do not assume message control over resulting coverage; earned media retains editorial independence, and a plan should not treat a pitch's framing as guaranteed to appear in the final story.
- For any statement with real legal exposure (safety, employment, financial, regulatory), flag the legal-review requirement explicitly rather than treating the communications angle as sufficient on its own; this skill does not make the legal determination.
- Do not present media mentions, share of voice, or sentiment score as a business outcome; they are observable activity and perception signals, and a business-outcome claim requires a stated evidence level, typically low on the causal ladder absent a specific attribution design.
- In a crisis, do not delay a factually accurate initial response while waiting for a complete narrative; state what is confirmed, what is not yet known, and when an update will follow, rather than either an incomplete rushed statement or silence.

## Output

Plan: newsworthiness basis; target media list with fit rationale; proactive or reactive framing; message-control tolerance stated; legal-review status; measurement plan with evidence-level expectation; exact status.

Crisis response: situation summary with what is confirmed versus unknown; immediate response draft with legal-review flag; escalation path; update cadence commitment; exact status.

## QA

Confirm newsworthiness is assessed honestly rather than assumed; the media list is fit-checked against the story and audience rather than generic; no claim to press exceeds what the business can substantiate; message control is not assumed over final coverage; legal-review triggers are flagged for statements with real exposure; and no reputational or coverage metric is presented as a business outcome without a stated evidence level.

## Source: `.agents/skills/public-relations/references/crisis-communications.md`

# Crisis Communications

The highest-stakes discipline in this skill: response speed, factual accuracy, and legal-review discipline all matter simultaneously, and getting any one wrong compounds the others. Unlike a planned pitch, a crisis response happens under time pressure with incomplete information, which is exactly when the discipline below is easiest to skip and most costly to skip.

## Method

1. Establish the facts actually confirmed, separately from what is suspected, reported by others, or unknown; a crisis response should state only what is confirmed, and explicitly acknowledge what is not yet known rather than speculating to fill a gap.
2. Flag legal-review requirements immediately for anything touching safety, employment, financial, or regulatory exposure; a communications response and a legal exposure assessment need to happen in parallel, not sequentially with communications going first.
3. Draft an initial response prioritizing speed on what is confirmed over completeness; a factually accurate partial statement issued promptly, with a clear commitment to update, is typically better received than either a delayed complete statement or a rushed inaccurate one.
4. Set an explicit update cadence and honor it; a stated "we will update by [time]" that is not honored damages credibility further, compounding the original issue.
5. Identify the escalation path — who has authority to approve the response, who needs to be looped in (legal, executive leadership, affected individuals) — before drafting, not after a first version is ready to send.
6. After the acute phase, conduct a factual after-action review separating what was a genuine failure from what was reasonable given the information available at the time; this supports future crisis response without treating hindsight as if it were available in the moment.

## Rules

- Do not speculate to fill a factual gap under time pressure; state explicitly what is not yet known rather than constructing a plausible-sounding but unverified explanation.
- Do not let a communications response proceed without a parallel legal-exposure check for anything touching safety, employment, financial, or regulatory matters; sequencing legal review after communications drafting creates real risk of an issued statement the business cannot support.
- Do not treat silence as a safe default while awaiting complete information; an accurate, appropriately scoped initial statement acknowledging what is confirmed and what is pending is typically more defensible than no response.
- Do not miss a stated update commitment; if new information changes the timeline, communicate that change rather than letting a deadline pass silently.
- Do not conduct the after-action review with hindsight bias substituting for what was actually knowable and decidable at the time; separate a genuine process failure from a reasonable decision that had an unfavorable outcome.
- Escalation and approval authority should be established before an incident occurs where possible; if no plan exists at the time of an incident, establish and communicate the approval chain as the first step rather than proceeding without clarity on who can authorize a statement.

## Source: `.agents/skills/public-relations/references/measurement-and-evidence-limits.md`

# Measurement and Evidence Limits

Public relations has the weakest measurement connection to business outcome of any channel in this system — media mentions, share of voice, and sentiment are real, observable signals, but none of them has a reliable, direct causal path to revenue, leads, or any other primary business outcome without a specific attribution design most programs do not have.

## What can actually be measured

Volume and reach of coverage (mentions, estimated audience reached); sentiment, imperfectly and often subjectively assessed; share of voice relative to competitors in coverage of a topic or category; and, where a specific attribution mechanism exists (a unique tracked link in coverage, a documented traffic or conversion spike tightly correlated with a specific placement's publication time), a directional signal of downstream effect.

## What typically cannot be established without a specific design

A direct causal link from coverage to revenue, leads, brand lift, or any other primary business outcome. Correlated timing (a traffic spike the same day as a major placement) is suggestive but not proof — the same causal-ladder discipline `$tracking-measurement` applies elsewhere applies here: correlated timing without a controlled comparison is low on the evidence ladder, typically C1, regardless of how compelling the timing looks.

## Method

1. State what is actually being measured — volume, sentiment, share of voice, or a specific attributed action — and do not conflate them into one undifferentiated "PR impact" figure.
2. Where a business-outcome claim is genuinely needed, check whether an attribution mechanism (unique link, dedicated landing page, timing tightly isolated from other concurrent activity) exists; if not, state plainly that the claim cannot be supported at a level above correlation.
3. Route an incrementality or causal question that matters to a real decision to `$tracking-measurement` for method selection, the same as any other channel; public relations does not have a unique exemption from that discipline.
4. Report sentiment with its actual methodology and limitations stated (automated sentiment analysis has known accuracy limits, particularly on nuance, sarcasm, and mixed coverage) rather than presenting a sentiment score as a precise, objective measure.

## Rules

- Do not present media-mention volume or estimated reach as equivalent to a business outcome; they are delivery signals only.
- Do not claim a specific revenue or lead impact from a public relations campaign without a stated attribution mechanism; absent one, report the timing correlation honestly and at its actual evidence level.
- Do not treat an automated sentiment score as precise or objective; state its known limitations alongside the figure.
- Do not blend share-of-voice, sentiment, and coverage volume into one composite score without stating what each component measures and how they were weighted; a composite score can obscure which underlying signal actually moved.
