# Segmentation and Triggers

Owned-channel communication has no auction, no bid, and no platform-native targeting — segmentation and trigger logic are the entire targeting mechanism. Getting them wrong wastes the channel's main advantage: knowing exactly who someone is and what they just did.

## Segmentation

Segment by behavior and lifecycle stage first: recency, frequency, monetary value, cart or browse behavior, lifecycle-stage transitions, and engagement with prior sends. Demographic or firmographic attributes are useful as a secondary refinement, not a primary segment, unless the business's offer genuinely varies by them.

A segment is only useful if membership predicts a meaningfully different next action or message. A segment that would receive the identical message as another segment is not a segment — merge them.

Recompute segment membership on a cadence matched to how fast the underlying behavior changes; a segment based on last-30-days behavior computed monthly is already stale for most of its own window.

## Trigger design

Define for every trigger: the firing event, the delay before firing, the suppression conditions (a purchase completing suppresses the abandoned-cart trigger; an unsubscribe suppresses everything), and the fallback if the triggering event's data arrives late, arrives twice, or never arrives.

Common trigger types: transactional (order confirmation, shipping), lifecycle-stage change (welcome, win-back, renewal), behavioral (cart abandonment, browse abandonment, post-purchase follow-up), and milestone (anniversary, usage threshold).

## Rules

- A trigger without a documented suppression condition will eventually send the wrong message to someone who already completed the triggering action's resolution — check every trigger against its own resolution event.
- Do not layer so many triggers that a single customer action can fire multiple overlapping messages; define trigger priority and mutual exclusion where sequences could collide.
- A late or duplicate event is not rare; design the fallback (delay window, deduplication check) as a first-class part of the trigger, not an edge case handled later.
- Segment size matters: a segment too small to reach meaningful volume is not worth a dedicated sequence; consider merging it into a broader segment with a conditional message instead.
- Test a new trigger or segmentation change on a subset before full rollout when the sending platform allows it; a broken trigger at full volume is a worse failure than a broken trigger caught in a controlled subset.
