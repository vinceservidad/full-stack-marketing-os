---
name: lifecycle-marketing
description: Design email and lifecycle automation strategy — segmentation, trigger logic, send cadence, and deliverability — for owned-channel customer communication; not for writing the copy itself, and not for paid acquisition channels.
---

# Lifecycle Marketing

Classify each segmentation model, trigger design, or cadence rule with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Lifecycle marketing is an owned channel — the business controls the list, the send, and the relationship — which changes what evidence is available and what discipline applies compared to a paid, platform-mediated channel.

This skill designs the sequence, trigger logic, segmentation, cadence, and deliverability strategy. It does not write the copy — route to `$copywriting` for that — and it does not run paid acquisition; a lifecycle program's job is to develop demand already captured, not to generate new demand from a cold audience.

## Context

Primary business outcome and lifecycle stage definitions per `$marketing-intake`; list size, growth rate, and consent basis for each segment; available trigger events (purchase, signup, cart abandonment, lifecycle-stage change) and their data reliability; sending platform and its deliverability history; current segmentation, if any; and the business's actual capacity to act on triggers in near-real time versus batch.

## Method

1. Map the customer lifecycle stages relevant to this business — using `$marketing-intake`'s recorded definitions, not a generic funnel — and identify which stage each planned communication serves.
2. Define segmentation by behavior and lifecycle stage, not demographic proxy alone; a segment should predict a meaningfully different next action, not just describe the audience.
3. Design trigger logic: the event, the delay, the condition under which the trigger fires or is suppressed, and what happens if the triggering event's data is late or missing.
4. Set send cadence per segment, respecting frequency limits the business or the audience's stated preference implies; escalating cadence is a lever with a cost, not a free intensification.
5. Read [Deliverability](references/deliverability.md) before recommending a cadence, list-growth tactic, or content change that could affect inbox placement.
6. Read [Segmentation and triggers](references/segmentation-and-triggers.md) for segment design and trigger-condition detail.
7. Define the measurement plan per sequence: primary business outcome, evaluation window matched to the lifecycle stage's typical timing, and how a sequence's incremental effect is assessed — route to `$tracking-measurement` for method selection when a causal claim is needed.
8. State capacity required to execute and maintain the design — platform configuration, ongoing segment maintenance, content production `$copywriting` will need to keep pace with.

## Rules

- Do not treat email open rate or click rate as the business outcome; report them as diagnostic signals and require a business-outcome measurement for any performance claim.
- Do not claim a sequence's revenue is fully incremental without addressing what the recipient would have done anyway; a purchase already in motion is not caused by the email that happened to arrive first. Route an incrementality claim to `$tracking-measurement`.
- Do not increase send frequency to compensate for a falling business outcome without diagnosing the cause first; more sends into a fatigued or poorly-segmented list typically worsens deliverability and does not fix acquisition or content problems underneath it.
- Consent and suppression rules are binding, not adjustable for reach: honor unsubscribe, consent basis, and any regulatory requirement without exception, and do not propose reactivating a suppressed contact through a workaround.
- Do not design a trigger that fires on unreliable or delayed data without a documented fallback; a broken trigger sends the wrong message at the wrong lifecycle moment, which costs more than a missed send.
- This skill does not write copy. Do not draft subject lines or body copy here; specify what each piece needs to accomplish and route drafting to `$copywriting`.

## Output

Program design: lifecycle stages covered; segmentation logic; trigger definitions with fallback behavior; cadence per segment; deliverability considerations; measurement plan per sequence with evaluation window; capacity required; what `$copywriting` needs to produce; exact status.

## QA

Confirm segmentation predicts a meaningfully different action rather than describing a demographic; every trigger has a stated fallback for missing or late data; cadence changes are diagnosed against a cause rather than applied reactively; consent and suppression rules are honored without exception; open/click metrics are not presented as the business outcome; and an incrementality claim is routed to `$tracking-measurement` rather than asserted here.
