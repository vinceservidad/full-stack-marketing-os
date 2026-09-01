---
name: lifecycle-marketing
description: Design email and lifecycle automation strategy — segmentation, trigger logic, send cadence, and deliverability — for owned-channel customer communication; not for writing the copy itself, defining activation value, or paid acquisition channels.
---

# Lifecycle Marketing

Classify each segmentation model, trigger design, or cadence rule with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Lifecycle marketing is an owned channel — the business controls the list, the send, and the relationship — which changes what evidence is available and what discipline applies compared to a paid, platform-mediated channel.

This skill designs the sequence, trigger logic, segmentation, cadence, and deliverability strategy. It does not write the copy — route to `$copywriting` for that — and it does not run paid acquisition; a lifecycle program's job is to develop demand already captured, not to generate new demand from a cold audience. When a sequence serves first meaningful value, `$activation` owns the value definition and journey outcome; lifecycle marketing owns the communication system supporting it.

## Context

Primary business outcome and lifecycle stage definitions per `$marketing-intake`; activation definition from `$activation` when relevant; list size, growth rate, and consent basis for each segment; available trigger events (purchase, signup, cart abandonment, activation-stage change, lifecycle-stage change) and their data reliability; sending platform and its deliverability history; current segmentation, if any; and the business's actual capacity to act on triggers in near-real time versus batch.

## Method

1. Map the customer lifecycle stages relevant to this business — using `$marketing-intake`'s recorded definitions, not a generic funnel — and identify which stage each planned communication serves. When the sequence targets first meaningful value, use `$activation`'s current value event and path rather than inventing an “aha moment” inside the email plan.
2. Define segmentation by behavior and lifecycle stage, not demographic proxy alone; a segment should predict a meaningfully different next action, not just describe the audience.
3. Design trigger logic: the event, the delay, the condition under which the trigger fires or is suppressed, and what happens if the triggering event's data is late or missing.
4. Set send cadence per segment, respecting frequency limits the business or the audience's stated preference implies; escalating cadence is a lever with a cost, not a free intensification.
5. Read [Deliverability](references/deliverability.md) before recommending a cadence, list-growth tactic, or content change that could affect inbox placement.
6. Read [Segmentation and triggers](references/segmentation-and-triggers.md) for segment design and trigger-condition detail.
7. Define the measurement plan per sequence: primary business outcome or the `$activation`-owned first-value outcome when the sequence specifically supports activation, evaluation window matched to the lifecycle stage's typical timing, and how a sequence's incremental effect is assessed — route to `$tracking-measurement` for method selection when a causal claim is needed.
8. State capacity required to execute and maintain the design — platform configuration, ongoing segment maintenance, and content production `$copywriting` will need to keep pace with.

## Rules

- Do not treat email open rate or click rate as the business outcome or as activation by default; report them as diagnostic signals.
- Do not invent an activation event inside a lifecycle sequence. `$activation` owns first meaningful value and the journey barrier; this skill owns communication triggers/cadence that may support it.
- Do not claim a sequence's revenue or activation lift is fully incremental without addressing what the recipient would have done anyway; route an incrementality claim to `$tracking-measurement`.
- Do not increase send frequency to compensate for a falling business or activation outcome without diagnosing the cause first; more sends do not fix poor fit, product/service failure, operational delay, or broken measurement.
- Consent and suppression rules are binding, not adjustable for reach: honor unsubscribe, consent basis, and any regulatory requirement without exception, and do not propose reactivating a suppressed contact through a workaround.
- Do not design a trigger that fires on unreliable or delayed data without a documented fallback; a broken trigger sends the wrong message at the wrong lifecycle moment, which costs more than a missed send.
- This skill does not write copy. Do not draft subject lines or body copy here; specify what each piece needs to accomplish and route drafting to `$copywriting`.

## Output

Program design: lifecycle stages covered; activation value event when relevant and its owner; segmentation logic; trigger definitions with fallback behavior; cadence per segment; deliverability considerations; measurement plan per sequence with evaluation window; capacity required; what `$copywriting` needs to produce; exact status.

## QA

Confirm segmentation predicts a meaningfully different action rather than describing a demographic; any activation event came from `$activation` rather than being invented here; every trigger has a fallback for missing/late data; cadence changes are diagnosed against a cause rather than applied reactively; consent and suppression rules are honored; open/click metrics are not presented as the business outcome or activation; and an incrementality claim is routed to `$tracking-measurement` rather than asserted here.
