# Intervention Selection and Save / Recovery

Use after the retention state and leading cause are defined.

## Core rule

Match the intervention to the diagnosed cause. A retention tactic that does not address the cause is noise, margin leakage, or coercion.

## Intervention map

### Involuntary payment failure

Possible responses: payment retry logic, card/account update path, billing-error correction, payment-method fallback, customer notification, service grace where commercially appropriate.

Owner boundaries: lifecycle marketing owns communications; pricing/monetization owns payment-model changes; billing/product implementation remains with the relevant system owner.

Do not use a discount as the default solution to a technical payment failure.

### Product/service/fulfillment defect

Possible responses: repair the defect, complete missing delivery/service, proactive support, replacement/remediation under actual policy, expectation reset where truthful.

Do not persuade a customer to remain while leaving the verified defect unresolved.

### Activation/value-realization failure

Route the value barrier to `$activation`. Retention may define the business risk, but Activation owns the first-value journey intervention.

### Poor fit / wrong acquisition

Route qualification/segment implications to `$icp-jtbd` and relevant acquisition owners. Do not improve apparent retention by trapping poor-fit customers after acquisition.

### Price / affordability / value tradeoff

Possible responses may include plan/package fit, pause/downgrade where truly available, payment timing, or a tested commercial offer. Pricing changes and discount architecture belong to `$pricing-monetization`.

A discount is a commercial intervention with margin and future-behavior effects, not a universal save tactic.

### Temporary no-need / seasonality

Possible responses: pause, reminder at evidence-backed timing, reorder/renewal timing support, lower-frequency communication. Do not treat a customer whose need has ended as a persuasion failure.

### Habit / attention / usage lapse

Possible responses: relevant reminder, progress cue, education, assistance, or workflow integration, only if the customer still has the underlying job and contact is permitted.

### Expectation mismatch

Fix the source of the expectation: offer, acquisition message, onboarding, product/service scope, or sales process. A retention message cannot repair a promise that remains false.

### Competitive switch

Understand the decision criteria and alternative. Do not automatically copy the competitor or undercut its price. Route positioning implications to `$icp-jtbd`, offer changes to `$offer-strategy`, and pricing decisions to `$pricing-monetization`.

## Save design

A cancellation-save intervention should define:

- eligible state and reason
- intervention and mechanism hypothesis
- who should not receive it
- customer choice and easy cancellation path
- commercial cost
- observation window
- primary retained-value outcome
- guardrails
- follow-up behavior required to call the save durable

### What is not a valid save

- customer gives up because cancellation is hard
- cancellation is delayed for a few days with no subsequent value/paid behavior
- a large discount retains revenue but destroys contribution
- support persuades the customer while the root defect remains
- the customer is moved to a plan they did not knowingly choose

## Recovery design

For involuntary loss, distinguish:

- retry attempted
- payment method updated
- payment recovered
- service/account restored
- customer remained active after recovery window

Do not label a successful payment retry as durable retention until the business-relevant continuation window is observed.

## Ethics and control

- Cancellation must remain understandable and accessible.
- Never use fake urgency, hidden downgrade consequences, misleading buttons, or repeated unwanted contact.
- Do not suppress legitimate refund/cancellation rights to protect a metric.
- Consent, unsubscribe, suppression, and contact preferences are binding.
- Any external account, billing, plan, or commercial mutation requires explicit authorization and exact-state verification.

## Measurement

Prefer realized continuing behavior and economics over “save accepted.” Guardrails can include contribution, discount cost, refund rate, complaints, support burden, payment-failure recurrence, next renewal/reorder, and customer quality.
