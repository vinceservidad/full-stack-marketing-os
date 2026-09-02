<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Lifecycle and Email Marketing

## Skill: $lifecycle-marketing

**Use when:** Design email and lifecycle automation strategy — segmentation, trigger logic, send cadence, and deliverability — for owned-channel customer communication; not for writing the copy itself, defining activation value, diagnosing retention causes, or paid acquisition channels.

Classify each segmentation model, trigger design, or cadence rule with `KNOWLEDGE-TAXONOMY.md`. Lifecycle marketing is an owned channel — the business controls the list, the send, and the relationship — which changes what evidence is available and what discipline applies compared to a paid, platform-mediated channel.

This skill designs the sequence, trigger logic, segmentation, cadence, suppression, and deliverability strategy. It does not write the copy — route to `$copywriting` for that — and it does not run paid acquisition. When a sequence serves first meaningful value, `$activation` owns the value definition and journey outcome. When a sequence serves retention, recovery, lapse prevention, or win-back, `$retention-strategy` owns the reason diagnosis, eligibility, and intervention objective; lifecycle marketing owns the communication system supporting it.

### Context

Primary business outcome and lifecycle stage definitions per `$marketing-intake`; activation definition from `$activation` when relevant; retention state/reason/intervention eligibility from `$retention-strategy` when relevant; list size, growth rate, and consent basis for each segment; available trigger events (purchase, signup, cart abandonment, activation-stage change, retention-risk/lapse/payment-failure/renewal state, lifecycle-stage change) and their data reliability; sending platform and its deliverability history; current segmentation, if any; and the business's actual capacity to act on triggers in near-real time versus batch.

### Method

1. Map the customer lifecycle stages relevant to this business — using `$marketing-intake`'s recorded definitions, not a generic funnel — and identify which stage each planned communication serves. When the sequence targets first meaningful value, use `$activation`'s current value event/path. When it targets retention or recovery, use `$retention-strategy`'s current state/reason/eligibility rather than inventing a churn cause inside the messaging plan.
2. Define segmentation by behavior and lifecycle stage, not demographic proxy alone; a segment should predict a meaningfully different next action, not just describe the audience.
3. Design trigger logic: the event, the delay, the condition under which the trigger fires or is suppressed, and what happens if the triggering event's data is late or missing.
4. Set send cadence per segment, respecting consent, suppression, contact preferences, and frequency limits the business or audience implies; escalating cadence is a lever with a cost, not a free intensification.
5. Read Deliverability before recommending a cadence, list-growth tactic, or content change that could affect inbox placement.
6. Read Segmentation and triggers for segment design and trigger-condition detail.
7. Define the measurement plan per sequence: primary business outcome, `$activation`-owned first-value outcome, or `$retention-strategy`-owned retained/recovered outcome as appropriate; evaluation window matched to the lifecycle stage; and how incremental effect is assessed — route to `$tracking-measurement` for method selection when a causal claim is needed.
8. State capacity required to execute and maintain the design — platform configuration, ongoing segment maintenance, and content production `$copywriting` will need to keep pace with.

### Rules

- Do not treat email open rate or click rate as the business outcome, activation, recovery, or retention by default; report them as diagnostic signals.
- Do not invent an activation event inside a lifecycle sequence. `$activation` owns first meaningful value and the journey barrier.
- Do not invent a churn reason, at-risk definition, save eligibility rule, or win-back rationale inside a lifecycle sequence. `$retention-strategy` owns those decisions.
- Do not claim a sequence's revenue, activation lift, save, or retention lift is fully incremental without addressing what the recipient would have done anyway; route causal claims to `$tracking-measurement`.
- Do not increase send frequency to compensate for a falling business, activation, or retention outcome without diagnosing the cause first; more sends do not fix poor fit, product/service failure, operational delay, payment defects, or broken measurement.
- Consent and suppression rules are binding, not adjustable for retention: honor unsubscribe, consent basis, communication preference, and any regulatory requirement without exception. Do not re-contact a suppressed or cancelled customer through a workaround.
- Do not design a trigger that fires on unreliable or delayed data without a documented fallback; a broken trigger sends the wrong message at the wrong lifecycle moment, which costs more than a missed send.
- This skill does not write copy. Do not draft subject lines or body copy here; specify what each piece needs to accomplish and route drafting to `$copywriting`.

### Output

Program design: lifecycle stages covered; activation value event or retention state/reason eligibility when relevant and its owner; segmentation logic; trigger definitions with fallback behavior; consent/suppression conditions; cadence per segment; deliverability considerations; measurement plan per sequence with evaluation window; capacity required; what `$copywriting` needs to produce; exact status.

### QA

Confirm segmentation predicts a meaningfully different action rather than describing a demographic; any activation event came from `$activation`; any retention/save/recovery/win-back eligibility came from `$retention-strategy`; every trigger has a fallback for missing/late data; cadence changes are diagnosed against a cause rather than applied reactively; consent and suppression rules are honored; open/click metrics are not presented as the business outcome, activation, recovery, or retention; and an incrementality claim is routed to `$tracking-measurement` rather than asserted here.

### Reference: deliverability ($lifecycle-marketing)

### Deliverability

Inbox placement is a prerequisite for every other lifecycle-marketing decision — a perfectly designed sequence that lands in spam has zero effect regardless of its logic or copy. Deliverability is also slow to damage and slow to repair; a decision made for short-term reach can cost weeks of placement afterward.

#### What governs deliverability

Sender reputation (domain and IP), authenticated correctly (SPF, DKIM, DMARC configured and aligned); list hygiene (bounce rate, spam-complaint rate, engagement rate); consistency of sending volume and pattern; and recipient engagement signals (opens, clicks, and — more heavily weighted by mailbox providers — deletions without opening and spam reports).

#### Rules

- Do not increase send volume or frequency sharply without a ramp; mailbox providers treat a sudden volume spike as a risk signal regardless of list quality.
- Remove or suppress chronically unengaged contacts on a stated cadence rather than continuing to send indefinitely; sending to an unengaged segment drags overall engagement metrics down and damages reputation for engaged segments sharing the same sending domain.
- Do not purchase, rent, or otherwise acquire a list from outside the business's own consented capture; it is both a consent violation and near-certain to damage deliverability immediately.
- A spike in spam complaints or bounce rate is a stop condition, not a metric to monitor passively; treat it with the same urgency as a tracking defect — pause the implicated send and diagnose before continuing.
- Warm a new sending domain or IP gradually with the most engaged segment first; do not launch a new domain directly into full-list volume.
- Authentication configuration (SPF/DKIM/DMARC) is a prerequisite check before diagnosing any other deliverability problem; verify it is correctly configured and aligned before attributing a placement issue to content or list quality.

### Reference: segmentation and triggers ($lifecycle-marketing)

### Segmentation and Triggers

Owned-channel communication has no auction, no bid, and no platform-native targeting — segmentation and trigger logic are the entire targeting mechanism. Getting them wrong wastes the channel's main advantage: knowing exactly who someone is and what they just did.

#### Segmentation

Segment by behavior and lifecycle stage first: recency, frequency, monetary value, cart or browse behavior, lifecycle-stage transitions, and engagement with prior sends. Demographic or firmographic attributes are useful as a secondary refinement, not a primary segment, unless the business's offer genuinely varies by them.

A segment is only useful if membership predicts a meaningfully different next action or message. A segment that would receive the identical message as another segment is not a segment — merge them.

Recompute segment membership on a cadence matched to how fast the underlying behavior changes; a segment based on last-30-days behavior computed monthly is already stale for most of its own window.

#### Trigger design

Define for every trigger: the firing event, the delay before firing, the suppression conditions (a purchase completing suppresses the abandoned-cart trigger; an unsubscribe suppresses everything), and the fallback if the triggering event's data arrives late, arrives twice, or never arrives.

Common trigger types: transactional (order confirmation, shipping), lifecycle-stage change (welcome, win-back, renewal), behavioral (cart abandonment, browse abandonment, post-purchase follow-up), and milestone (anniversary, usage threshold).

#### Rules

- A trigger without a documented suppression condition will eventually send the wrong message to someone who already completed the triggering action's resolution — check every trigger against its own resolution event.
- Do not layer so many triggers that a single customer action can fire multiple overlapping messages; define trigger priority and mutual exclusion where sequences could collide.
- A late or duplicate event is not rare; design the fallback (delay window, deduplication check) as a first-class part of the trigger, not an edge case handled later.
- Segment size matters: a segment too small to reach meaningful volume is not worth a dedicated sequence; consider merging it into a broader segment with a conditional message instead.
- Test a new trigger or segmentation change on a subset before full rollout when the sending platform allows it; a broken trigger at full volume is a worse failure than a broken trigger caught in a controlled subset.
