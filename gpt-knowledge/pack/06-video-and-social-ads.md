<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# YouTube and TikTok Advertising

## Skill: $youtube-ads

**Use when:** Plan, audit, or diagnose YouTube video advertising — format selection, audience targeting, view-through measurement, and creative fit for skippable, non-skippable, bumper, and discovery placements; not for Search, Shopping, or Performance Max, and not for organic YouTube content strategy.

Classify each model, format decision, or measurement method with `KNOWLEDGE-TAXONOMY.md`. YouTube runs through the Google Ads platform but is a distinct discipline from Search, Shopping, and Performance Max: it is a video, largely upper- and mid-funnel medium with different attention economics, format constraints, and measurement norms. Route Search/Shopping/PMax structure, bidding, and account mechanics to `$google-ads`; route organic YouTube content and channel growth elsewhere — this skill covers paid placement only.

### Context

Primary business outcome and where in the funnel this campaign is expected to work — awareness, consideration, or direct response — since format, targeting, and measurement all depend on that answer; available video creative assets and their length/format fit; audience data available (first-party lists, in-market/affinity segments, custom intent); brand safety and content-adjacency requirements; and whether brand lift or view-through purchase behavior needs to be measured.

### Method

1. State the funnel objective explicitly before selecting a format; a direct-response objective on a bumper ad or a brand-awareness objective evaluated on last-click conversion rate is a measurement mismatch, not a performance problem.
2. Select ad format to fit the objective and the creative actually available. See Format selection.
3. Build audience targeting from evidence — first-party lists and observed in-market/affinity behavior — before reaching for broad demographic or interest targeting; state which layer is doing the work.
4. Assess creative fit before launch: whether the asset communicates its message in the format's actual attention window, not the length the business happened to produce. Route to `$creative-strategy` for concept and hook development if the creative itself needs work.
5. Define the measurement plan before launch, matched to the funnel objective: brand lift study for awareness objectives, view-through and assisted-conversion tracking for consideration, direct conversion tracking for response — see Measurement fit and route method selection and evidence grading to `$tracking-measurement`.
6. Rank actions by expected business impact, confidence, reversibility, and creative production capacity.

### Rules

- Do not evaluate an awareness-objective campaign on direct-response metrics, or a direct-response campaign on view-through reach; state the objective and hold the campaign to its own measurement standard.
- Do not present view-through conversions as equivalent to click-through conversions; a view-through credit means the ad was shown, not that it was necessarily seen, attended to, or causal — grade the claim per the causal evidence ladder in `$tracking-measurement`.
- Do not recommend a skippable in-stream format for a message that requires the full asset to land; skip rates are real and design around the first five seconds accordingly, or select a non-skippable or bumper format that matches the message's actual requirement.
- Do not reuse a Search or Shopping conversion definition unmodified for a video-campaign objective; state the definition explicitly per the funnel stage this campaign targets.
- Preserve brand-safety and content-adjacency settings; do not loosen them to expand reach without explicit approval, since a brand-safety incident carries a cost this system cannot quantify or reverse after the fact.
- A view count, watch time, or completion rate is a delivery and engagement signal, not the business outcome; require a business-outcome measurement for any performance claim beyond delivery.

### Output

Plan: funnel objective; format selection with rationale; audience targeting layers; creative fit assessment; measurement plan matched to objective; capacity required; exact status.

Diagnosis: observed change; funnel objective it should be measured against; competing explanations (creative fatigue, audience saturation, seasonality, format mismatch, measurement change) considered before attributing a cause; evidence level; recommended action.

### QA

Confirm the funnel objective is stated and the campaign is measured against its own objective; format matches the message's actual attention requirement; audience targeting states which evidence layer is doing the work; view-through claims are graded rather than treated as equivalent to click-through; brand-safety settings are preserved absent explicit approval to change them; and no delivery or engagement metric is presented as the business outcome.

### Reference: format selection ($youtube-ads)

### Format Selection

Format determines both the attention window available and the metrics that are even measurable — selecting it is not a creative-team preference, it is a decision that constrains everything downstream.

#### Formats and fit

| Format | Skippable | Typical length | Fits |
|---|---|---|---|
| Skippable in-stream | Yes, after 5 seconds | 12s–3min+ | Broad reach at controlled cost; message must land or hook within the first 5 seconds since most viewers can skip |
| Non-skippable in-stream | No | 15–20s | A complete message the audience must see in full; higher cost per impression, used when the message cannot be compressed to a bumper or cannot risk a skip |
| Bumper | No | 6s max | A single, simple message or reinforcement of a message delivered elsewhere; not for a message requiring explanation |
| In-feed / discovery | User-initiated (thumbnail click) | Any | Audiences actively browsing; performance depends heavily on thumbnail and title, evaluated more like search intent than interruption advertising |
| Outstream | Yes | Any | Mobile-first reach off YouTube itself, on partner sites and apps; typically muted-by-default, so design for sound-off comprehension |

#### Method

1. Match format to funnel objective first, creative length second. An awareness objective can use any format; a direct-response objective needs enough time or clarity to communicate the offer and call to action.
2. For skippable formats, design the first five seconds to work whether or not the viewer skips after — the hook must communicate the core message, not just earn attention for a longer reveal.
3. For bumper, the message must be genuinely compressible to six seconds; forcing a longer message into a bumper produces something incomprehensible, not something efficient.
4. For in-feed/discovery, treat thumbnail and title with the same rigor as a search ad's headline — they are the entire mechanism determining whether the format is even seen.
5. For outstream, assume sound-off; a message relying on audio narration alone will fail regardless of targeting quality.

#### Rules

- Do not select non-skippable to force message completion when the message itself is weak; a forced view of unpersuasive creative is not a fix for the creative problem.
- Do not use the same creative asset unedited across formats with different length and skip constraints; a 30-second asset trimmed to 6 seconds without redesign usually loses its message, not just its length.
- Format selection is reversible and testable; when uncertain between two formats for the same objective, prefer testing over asserting one is correct from principle alone.

### Reference: measurement fit ($youtube-ads)

### Measurement Fit

YouTube's measurement norms differ from Search and Shopping because the medium is upper- and mid-funnel more often than not, and because a "view" is a weaker, more ambiguous signal than a click. Matching measurement to funnel objective prevents the two most common YouTube measurement errors: judging an awareness campaign on conversion rate, and treating a view-through credit as equivalent to a click-through one.

#### Matching method to objective

| Objective | Primary measurement | Method |
|---|---|---|
| Awareness | Brand lift (aided/unaided recall, favorability, purchase intent) | Platform-native brand lift study — apply the same scrutiny as any platform lift study in `$tracking-measurement`'s platform lift studies: verify randomization, holdout integrity, and whether it is independent verification of the same platform's own delivery |
| Consideration | View-through and assisted-conversion signal, directional not causal | Report as C1–C2 evidence; do not present as a confirmed causal effect without an incrementality design |
| Direct response | Conversion tracking against the campaign's stated definition | Standard conversion measurement, but confirm the conversion definition is appropriate to a video-driven action rather than reused unmodified from Search |

#### Rules

- A view-through conversion means the ad was served to a user who later converted, not that the ad caused the conversion; grade any causal claim about view-through effect on the `$tracking-measurement` causal evidence ladder, and expect it to land no higher than C1–C2 without a designed incrementality test.
- Do not sum view-through and click-through conversions into one total presented as incremental; they are different evidence types and summing them overstates the campaign's effect.
- A brand lift study is platform-run; apply the same seller-grades-own-work caution `$tracking-measurement` applies to any platform lift study before treating its result as independent verification.
- If the decision at stake — a sustained budget increase, a channel-mix shift — requires evidence above what YouTube's native measurement can provide, route to `$tracking-measurement` for an incrementality design (holdout, geo experiment) rather than accepting the platform's own reporting as sufficient.
- Completion rate, view rate, and watch time measure delivery and engagement, not business outcome; do not present them as performance evidence for a business decision without a stated business-outcome metric alongside them.

## Skill: $tiktok-ads

**Use when:** Plan, audit, or diagnose TikTok paid advertising — native-feeling creative fit, Spark Ads versus standard in-feed, targeting breadth, and creative-fatigue cadence; not for Meta or YouTube, and not for organic TikTok content strategy.

Classify each model, format decision, or targeting recommendation with `KNOWLEDGE-TAXONOMY.md`. TikTok's core mechanic — an algorithmic feed that rewards content viewers do not perceive as an ad — makes this a distinct discipline from Meta and YouTube, not a reskin of either. A creative asset that performs on Meta frequently underperforms on TikTok unedited, and the reverse.

### Context

Primary business outcome and profit level per `$marketing-intake`; available creative — specifically whether native, creator-style, or user-generated content exists or can be produced, versus only polished brand assets; whether an existing organic post with real engagement is available to boost via Spark Ads; TikTok Shop or commerce integration status if relevant; current targeting approach (broad/automated versus defined audiences) and its platform-documented status per `PLATFORM-CURRENCY.md`; and creative production cadence and capacity, since TikTok creative fatigues faster than most other paid channels.

### Method

1. Assess creative fit before targeting or budget: does the available creative read as native to the feed, or does it read as an interruption. See Native creative fit.
2. Choose between Spark Ads (boosting an existing organic post, inheriting its engagement and comments) and standard in-feed ads (new campaign-only creative with no organic history); state which and why, since they have different creative, comment-moderation, and measurement implications.
3. Assess targeting approach against current platform documentation per `PLATFORM-CURRENCY.md`; do not assume a specific manual-targeting configuration remains the platform's recommended or even available approach without confirming current account-visible behavior.
4. Plan creative cadence and refresh rate to the account's actual fatigue signal — see Creative fatigue and refresh cadence — rather than a fixed calendar borrowed from a different platform.
5. Define the measurement plan: primary business outcome, pixel/events configuration, and — since TikTok's audience and behavior differ from Meta and YouTube — do not assume a conversion or attribution pattern observed on another platform transfers here without evidence.
6. Rank actions by expected business impact, confidence, reversibility, and native-creative production capacity, which is frequently the actual binding constraint on this channel.

### Rules

- Do not judge TikTok creative by the production standards of a polished Meta or YouTube asset; native-feeling, lower-fidelity content frequently outperforms high-production creative on this platform, and a recommendation to "polish" creative without evidence of an actual quality problem can hurt performance.
- Do not recommend narrow manual targeting as a default without confirming, per `PLATFORM-CURRENCY.md`, that the platform's current documented guidance and account-visible behavior still support it over automated/broad targeting; this is an area where platform-recommended practice changes faster than most and an assumed configuration can be stale.
- Do not treat Spark Ads and standard in-feed ads as interchangeable; a Spark Ad inherits the original post's comments and engagement history, which is a genuine account-moderation and brand-safety consideration a standard ad does not carry.
- Do not propose a creative cadence without checking the account's actual fatigue signal (rising frequency, falling click-through at stable spend, rising cost per result with unchanged targeting); a fixed weekly-refresh assumption borrowed from another platform is not evidence.
- Preserve comment moderation and brand-safety review for Spark Ads specifically, since public comments on the boosted post remain visible and attributable to the brand's spend.
- Do not conflate organic TikTok trend performance with paid ad performance; a trend performing well organically does not establish that a paid version of the same content will perform, and vice versa.

### Output

Plan: creative fit assessment; Spark Ads versus standard in-feed decision with rationale; targeting approach with platform-currency confirmation; creative cadence matched to actual fatigue signal; measurement plan; capacity required; exact status.

Diagnosis: observed change; competing explanations (creative fatigue, targeting-approach shift, platform algorithm or policy change, seasonality, comment-moderation incident on a Spark Ad) considered before attributing a cause; evidence level; recommended action.

### QA

Confirm creative fit is assessed on TikTok's own native-feel standard rather than another platform's production standard; the Spark Ads versus standard in-feed choice is stated with rationale; targeting approach is checked against current platform documentation rather than assumed; creative cadence is driven by an observed fatigue signal, not a borrowed calendar; and no claim about targeting or algorithm behavior is presented as current without a `PLATFORM-CURRENCY.md` check.

### Reference: creative fatigue and refresh cadence ($tiktok-ads)

### Creative Fatigue and Refresh Cadence

TikTok creative typically fatigues faster than the same audience's tolerance for Meta or Search creative, because the feed's discovery mechanic exposes an asset to a large volume of impressions quickly. Refresh cadence should be driven by an observed fatigue signal from the account, not a fixed calendar borrowed from a slower-fatiguing channel.

#### Fatigue signal

Rising frequency at stable or falling reach; falling click-through rate at stable spend and stable targeting; rising cost per result with no change to targeting, bidding, or competitive conditions; and — where available — a falling engagement-rate trend on the specific creative rather than the account overall.

Distinguish creative fatigue from a targeting-approach change, a platform algorithm update, or a seasonal shift; check `PLATFORM-CURRENCY.md` and the competitive/seasonal calendar before attributing a performance decline to creative fatigue specifically.

#### Method

1. Track frequency, click-through rate, and cost per result at the individual-creative level, not only the campaign level; fatigue is a property of a specific asset's exposure, and campaign-level averages can mask an early-fatiguing top performer being propped up by newer creative in the same campaign.
2. Set a refresh trigger from the account's own observed fatigue curve — the point at which the signals above begin degrading — rather than a fixed number of days or weeks assumed from another platform.
3. Maintain a creative production pipeline sized to the account's actual observed refresh need; a channel with a genuinely faster fatigue cycle requires proportionally more production capacity, and a plan that does not account for this will underperform on cadence regardless of individual creative quality.
4. When introducing new creative to replace a fatiguing asset, vary more than the surface execution — a new video using the identical hook, structure, and offer as the fatiguing one often fatigues on a similar timeline rather than resetting performance.

#### Rules

- Do not set a refresh cadence before observing at least one fatigue cycle on the account; an assumed cadence from another platform or from general industry pattern is a hypothesis, not evidence, until the account's own signal confirms or contradicts it.
- Do not treat a declining metric as creative fatigue by default; check competing explanations (targeting-approach change, platform update, seasonality, competitive shift) before concluding the creative itself is the cause.
- A creative production plan that cannot sustain the account's actual observed refresh need is a capacity constraint, not merely a scheduling inconvenience; report it as a constraint per `$optimization-scaling`'s creative-capacity gate when it bears on a scaling decision.

### Reference: native creative fit ($tiktok-ads)

### Native Creative Fit

The single most consequential creative decision on TikTok is whether an asset reads as native to the feed or as an obvious ad. This is not a stylistic preference; it directly affects the algorithm's distribution of the content and the audience's willingness to watch past the first moment.

#### What "native" means here

Vertical, full-screen, shot to look like organic creator content — handheld camera feel, on-screen text or captions in the platform's visual language, sound or trending audio used the way organic creators use it, and a message delivered the way a person would say it rather than the way a brand would write it. Production polish (professional lighting, studio sets, scripted voiceover) is not disqualifying, but it is a signal the format has to work harder to overcome.

#### Assessing available creative

1. Ask whether the asset was produced for TikTok specifically or repurposed from another platform. Repurposed vertical-cropped horizontal video is a common and visible tell that a viewer's attention discounts immediately.
2. Ask whether the opening one to two seconds work as a native hook — a question, a visual pattern interrupt, or a claim stated the way a creator would state it — rather than a logo or brand card, which reads as an ad and invites an immediate scroll past.
3. Ask whether creator or user-generated content is available or producible; a real or convincingly real creator voice is frequently the highest-leverage creative lever on this platform specifically.
4. Ask whether the audio is native to the platform (trending sound, native voiceover) rather than a licensed brand jingle or a track that reads as a commercial.

#### Rules

- Do not default to reformatting an existing high-production asset for TikTok without assessing whether its production quality itself is the mismatch; a lower-fidelity, purpose-built asset frequently outperforms a repurposed polished one, and recommending "polish it more" without that check can make the mismatch worse.
- Route concept, hook, and angle development to `$creative-strategy`; this reference assesses fit to the platform's native format, it does not develop the underlying creative concept.
- Test native-style and higher-production creative against each other rather than asserting one wins by default; the fit varies by category and audience, and a categorical claim without account-specific evidence should be treated as a hypothesis.
- A single high-performing native asset does not establish a durable creative pattern; require replication before generalizing "this style works" into a standing creative brief.
