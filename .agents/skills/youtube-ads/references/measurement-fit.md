# Measurement Fit

YouTube's measurement norms differ from Search and Shopping because the medium is upper- and mid-funnel more often than not, and because a "view" is a weaker, more ambiguous signal than a click. Matching measurement to funnel objective prevents the two most common YouTube measurement errors: judging an awareness campaign on conversion rate, and treating a view-through credit as equivalent to a click-through one.

## Matching method to objective

| Objective | Primary measurement | Method |
|---|---|---|
| Awareness | Brand lift (aided/unaided recall, favorability, purchase intent) | Platform-native brand lift study — apply the same scrutiny as any platform lift study in `$tracking-measurement`'s [platform lift studies](../../tracking-measurement/references/platform-lift-studies.md): verify randomization, holdout integrity, and whether it is independent verification of the same platform's own delivery |
| Consideration | View-through and assisted-conversion signal, directional not causal | Report as C1–C2 evidence; do not present as a confirmed causal effect without an incrementality design |
| Direct response | Conversion tracking against the campaign's stated definition | Standard conversion measurement, but confirm the conversion definition is appropriate to a video-driven action rather than reused unmodified from Search |

## Rules

- A view-through conversion means the ad was served to a user who later converted, not that the ad caused the conversion; grade any causal claim about view-through effect on the `$tracking-measurement` causal evidence ladder, and expect it to land no higher than C1–C2 without a designed incrementality test.
- Do not sum view-through and click-through conversions into one total presented as incremental; they are different evidence types and summing them overstates the campaign's effect.
- A brand lift study is platform-run; apply the same seller-grades-own-work caution `$tracking-measurement` applies to any platform lift study before treating its result as independent verification.
- If the decision at stake — a sustained budget increase, a channel-mix shift — requires evidence above what YouTube's native measurement can provide, route to `$tracking-measurement` for an incrementality design (holdout, geo experiment) rather than accepting the platform's own reporting as sufficient.
- Completion rate, view rate, and watch time measure delivery and engagement, not business outcome; do not present them as performance evidence for a business decision without a stated business-outcome metric alongside them.
