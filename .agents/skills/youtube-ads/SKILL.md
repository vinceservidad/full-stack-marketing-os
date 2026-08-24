---
name: youtube-ads
description: Plan, audit, or diagnose YouTube video advertising — format selection, audience targeting, view-through measurement, and creative fit for skippable, non-skippable, bumper, and discovery placements; not for Search, Shopping, or Performance Max, and not for organic YouTube content strategy.
---

# YouTube Ads

Classify each model, format decision, or measurement method with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). YouTube runs through the Google Ads platform but is a distinct discipline from Search, Shopping, and Performance Max: it is a video, largely upper- and mid-funnel medium with different attention economics, format constraints, and measurement norms. Route Search/Shopping/PMax structure, bidding, and account mechanics to `$google-ads`; route organic YouTube content and channel growth elsewhere — this skill covers paid placement only.

## Context

Primary business outcome and where in the funnel this campaign is expected to work — awareness, consideration, or direct response — since format, targeting, and measurement all depend on that answer; available video creative assets and their length/format fit; audience data available (first-party lists, in-market/affinity segments, custom intent); brand safety and content-adjacency requirements; and whether brand lift or view-through purchase behavior needs to be measured.

## Method

1. State the funnel objective explicitly before selecting a format; a direct-response objective on a bumper ad or a brand-awareness objective evaluated on last-click conversion rate is a measurement mismatch, not a performance problem.
2. Select ad format to fit the objective and the creative actually available. See [Format selection](references/format-selection.md).
3. Build audience targeting from evidence — first-party lists and observed in-market/affinity behavior — before reaching for broad demographic or interest targeting; state which layer is doing the work.
4. Assess creative fit before launch: whether the asset communicates its message in the format's actual attention window, not the length the business happened to produce. Route to `$creative-strategy` for concept and hook development if the creative itself needs work.
5. Define the measurement plan before launch, matched to the funnel objective: brand lift study for awareness objectives, view-through and assisted-conversion tracking for consideration, direct conversion tracking for response — see [Measurement fit](references/measurement-fit.md) and route method selection and evidence grading to `$tracking-measurement`.
6. Rank actions by expected business impact, confidence, reversibility, and creative production capacity.

## Rules

- Do not evaluate an awareness-objective campaign on direct-response metrics, or a direct-response campaign on view-through reach; state the objective and hold the campaign to its own measurement standard.
- Do not present view-through conversions as equivalent to click-through conversions; a view-through credit means the ad was shown, not that it was necessarily seen, attended to, or causal — grade the claim per the causal evidence ladder in `$tracking-measurement`.
- Do not recommend a skippable in-stream format for a message that requires the full asset to land; skip rates are real and design around the first five seconds accordingly, or select a non-skippable or bumper format that matches the message's actual requirement.
- Do not reuse a Search or Shopping conversion definition unmodified for a video-campaign objective; state the definition explicitly per the funnel stage this campaign targets.
- Preserve brand-safety and content-adjacency settings; do not loosen them to expand reach without explicit approval, since a brand-safety incident carries a cost this system cannot quantify or reverse after the fact.
- A view count, watch time, or completion rate is a delivery and engagement signal, not the business outcome; require a business-outcome measurement for any performance claim beyond delivery.

## Output

Plan: funnel objective; format selection with rationale; audience targeting layers; creative fit assessment; measurement plan matched to objective; capacity required; exact status.

Diagnosis: observed change; funnel objective it should be measured against; competing explanations (creative fatigue, audience saturation, seasonality, format mismatch, measurement change) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm the funnel objective is stated and the campaign is measured against its own objective; format matches the message's actual attention requirement; audience targeting states which evidence layer is doing the work; view-through claims are graded rather than treated as equivalent to click-through; brand-safety settings are preserved absent explicit approval to change them; and no delivery or engagement metric is presented as the business outcome.
