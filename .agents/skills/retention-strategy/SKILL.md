---
name: retention-strategy
description: Diagnose why customers fail to continue, renew, repurchase, or return and design cause-matched retention, save, recovery, repeat-purchase, and win-back interventions using customer, behavioral, operational, and economic evidence; not for default discounting, obstructing cancellation, or substituting retention rate for realized economics.
---

# Retention Strategy

Retention Strategy owns the intervention decision after activation or initial value: why customers stay, lapse, cancel, fail to repurchase, or become at risk; which intervention matches that reason; and how that intervention should be validated.

It does not calculate lifetime value or retention curves (`$retention-economics`), define first meaningful value (`$activation`), own lifecycle communication mechanics (`$lifecycle-marketing`), set pricing (`$pricing-monetization`), or implement product/service fixes.

Classify outputs with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A churn reason, save tactic, win-back pattern, or retention benchmark is a hypothesis input until supported in this business and segment.

## Inputs

Before a decision-grade recommendation, confirm:

- business model and the relevant continuation behavior: renew, repurchase, repeat use, continue service, or remain active
- segment/cohort, lifecycle state, activation state where relevant, and observation window
- realized retention/churn/repeat behavior and economics from `$retention-economics`
- cancellation, refund, support, payment-failure, product/service, fulfillment, usage, and customer-research evidence where available
- current offer, pricing/payment terms, service commitments, and known experience defects
- lifecycle communication state and consent/suppression constraints
- implementation owner and authorization boundary

If the apparent retention change may be a measurement or cohort-definition defect, route that dependency before intervention design.

## Method

1. **Define the retention decision.** State the continuation behavior, cohort, window, and business outcome. Do not use a generic churn percentage without naming what churn means here.
2. **Separate state from reason.** A customer can be active, at risk, voluntarily cancelled, involuntarily lost, dormant/lapsed, recovered, or won back. State the observed state before inferring why.
3. **Diagnose the cause.** Use [Retention diagnosis and reason coding](references/retention-diagnosis-and-reason-coding.md). Separate customer-stated reason, observed behavior, operational facts, commercial terms, and inference.
4. **Match intervention to cause.** Use [Intervention selection and save/recovery](references/intervention-selection-and-save-recovery.md). Fix defects before persuading; handle failed payment differently from poor fit, price objection, low need, service failure, or unmet promise.
5. **Choose the correct lifecycle objective.** Retention of an active customer, cancellation save, failed-payment recovery, repeat-purchase support, lapse prevention, and win-back are different decisions. Use [Repeat, renewal, and win-back](references/repeat-renewal-and-winback.md).
6. **Define the smallest meaningful intervention.** Route lifecycle triggers/cadence to `$lifecycle-marketing`, wording to `$copywriting`, pricing changes to `$pricing-monetization`, activation barriers to `$activation`, and product/service/operations fixes to the actual implementation owner.
7. **Define measurement and guardrails.** Primary outcomes may include retained paid status, realized repeat purchase, renewal, recovered payment, contribution, or qualified continuing usage. Guardrails include refunds, complaints, support burden, discount dependency, margin, involuntary churn recurrence, customer quality, and downstream retention.
8. **Record learning and exact state.** A launched intervention is not a proven retention strategy until the observation window and downstream guardrails are complete.

## Rules

- Do not default to discounts, coupons, pause offers, or win-back messages before diagnosing the reason for loss or risk.
- Do not obstruct cancellation, hide the cancel action, add deceptive friction, or force unwanted contact to inflate retention.
- Do not treat a cancellation-survey answer as the sole cause. Preserve stated reason separately from observed evidence and inference.
- Separate voluntary churn from involuntary churn. Failed payment, expired card, and billing errors require recovery mechanics, not persuasion by default.
- Do not call a save successful merely because cancellation was delayed. Verify continued paid/value behavior over a decision-relevant window.
- Do not call a discounted renewal a clean win without checking contribution, future renewal behavior, discount dependency, and customer mix.
- Do not treat higher repeat purchase rate or lower churn as sufficient if refunds, complaints, quality, margin, or support burden worsen materially.
- Do not win back customers whose reason for leaving remains unresolved. Fix the cause or state clearly that the intervention cannot solve it.
- Honor consent, suppression, communication preferences, and cancellation rights. A retention goal never overrides them.
- Do not infer causality from retained-versus-churned customer differences without a valid design; better-fit customers may both engage more and retain longer.
- If the business has no meaningful repeat/renewal behavior, state that a dedicated retention intervention layer is not decision-relevant rather than inventing one.

## Output

Retention decision: continuation behavior; segment/cohort/window; observed retention state; evidence by source; diagnosed reason and confidence; voluntary/involuntary/lapse classification; intervention hypothesis; required owner handoffs; primary outcome; guardrails; experiment/validation plan; economics dependency; implementation dependencies; approval needs; exact status.

## Library references

Owned root artifacts, read when their scope applies:

- [retention-strategy-plan.md](../../../templates/retention-strategy-plan.md) — canonical diagnosis, intervention, save/recovery, win-back, measurement, and learning record.

## Related owners

- `$marketing-intake`: lifecycle definitions, evidence state, authorization, shared context
- `$customer-research`: customer-stated reasons, qualitative patterns, VOC
- `$icp-jtbd`: poor-fit segments, changed needs, alternatives
- `$activation`: first-value failures that later appear as retention problems
- `$offer-strategy`: promise/expectation mismatch and commercial proposition
- `$pricing-monetization`: price/payment-model changes and discount architecture
- `$lifecycle-marketing`: retention, recovery, lapse, and win-back communication triggers/cadence/suppression
- `$copywriting`: retention and recovery message wording
- `$tracking-measurement`: causal validity and experiment learning
- `$retention-economics`: realized retention, churn, repeat, LTV, payback, and cohort maturity
- `$marketing-operations`: recurring at-risk/recovery decision loops

## QA

Confirm retention is defined for this business, state is separated from reason, voluntary and involuntary loss are not blended, intervention matches diagnosed cause, cancellation rights and consent are protected, discounts are economically checked, downstream guardrails are included, product/service defects are routed to their owner, and no delayed cancellation or short-term save is described as durable retention before the observation window matures.
