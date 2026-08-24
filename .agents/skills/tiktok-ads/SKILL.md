---
name: tiktok-ads
description: Plan, audit, or diagnose TikTok paid advertising — native-feeling creative fit, Spark Ads versus standard in-feed, targeting breadth, and creative-fatigue cadence; not for Meta or YouTube, and not for organic TikTok content strategy.
---

# TikTok Ads

Classify each model, format decision, or targeting recommendation with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). TikTok's core mechanic — an algorithmic feed that rewards content viewers do not perceive as an ad — makes this a distinct discipline from Meta and YouTube, not a reskin of either. A creative asset that performs on Meta frequently underperforms on TikTok unedited, and the reverse.

## Context

Primary business outcome and profit level per `$marketing-intake`; available creative — specifically whether native, creator-style, or user-generated content exists or can be produced, versus only polished brand assets; whether an existing organic post with real engagement is available to boost via Spark Ads; TikTok Shop or commerce integration status if relevant; current targeting approach (broad/automated versus defined audiences) and its platform-documented status per `PLATFORM-CURRENCY.md`; and creative production cadence and capacity, since TikTok creative fatigues faster than most other paid channels.

## Method

1. Assess creative fit before targeting or budget: does the available creative read as native to the feed, or does it read as an interruption. See [Native creative fit](references/native-creative-fit.md).
2. Choose between Spark Ads (boosting an existing organic post, inheriting its engagement and comments) and standard in-feed ads (new campaign-only creative with no organic history); state which and why, since they have different creative, comment-moderation, and measurement implications.
3. Assess targeting approach against current platform documentation per `PLATFORM-CURRENCY.md`; do not assume a specific manual-targeting configuration remains the platform's recommended or even available approach without confirming current account-visible behavior.
4. Plan creative cadence and refresh rate to the account's actual fatigue signal — see [Creative fatigue and refresh cadence](references/creative-fatigue-and-refresh-cadence.md) — rather than a fixed calendar borrowed from a different platform.
5. Define the measurement plan: primary business outcome, pixel/events configuration, and — since TikTok's audience and behavior differ from Meta and YouTube — do not assume a conversion or attribution pattern observed on another platform transfers here without evidence.
6. Rank actions by expected business impact, confidence, reversibility, and native-creative production capacity, which is frequently the actual binding constraint on this channel.

## Rules

- Do not judge TikTok creative by the production standards of a polished Meta or YouTube asset; native-feeling, lower-fidelity content frequently outperforms high-production creative on this platform, and a recommendation to "polish" creative without evidence of an actual quality problem can hurt performance.
- Do not recommend narrow manual targeting as a default without confirming, per `PLATFORM-CURRENCY.md`, that the platform's current documented guidance and account-visible behavior still support it over automated/broad targeting; this is an area where platform-recommended practice changes faster than most and an assumed configuration can be stale.
- Do not treat Spark Ads and standard in-feed ads as interchangeable; a Spark Ad inherits the original post's comments and engagement history, which is a genuine account-moderation and brand-safety consideration a standard ad does not carry.
- Do not propose a creative cadence without checking the account's actual fatigue signal (rising frequency, falling click-through at stable spend, rising cost per result with unchanged targeting); a fixed weekly-refresh assumption borrowed from another platform is not evidence.
- Preserve comment moderation and brand-safety review for Spark Ads specifically, since public comments on the boosted post remain visible and attributable to the brand's spend.
- Do not conflate organic TikTok trend performance with paid ad performance; a trend performing well organically does not establish that a paid version of the same content will perform, and vice versa.

## Output

Plan: creative fit assessment; Spark Ads versus standard in-feed decision with rationale; targeting approach with platform-currency confirmation; creative cadence matched to actual fatigue signal; measurement plan; capacity required; exact status.

Diagnosis: observed change; competing explanations (creative fatigue, targeting-approach shift, platform algorithm or policy change, seasonality, comment-moderation incident on a Spark Ad) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm creative fit is assessed on TikTok's own native-feel standard rather than another platform's production standard; the Spark Ads versus standard in-feed choice is stated with rationale; targeting approach is checked against current platform documentation rather than assumed; creative cadence is driven by an observed fatigue signal, not a borrowed calendar; and no claim about targeting or algorithm behavior is presented as current without a `PLATFORM-CURRENCY.md` check.
