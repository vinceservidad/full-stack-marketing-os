# Activation Experiments and Handoffs

Use this reference after the activation definition and first binding barrier are explicit.

## Experiment contract

An activation experiment should specify:

- target segment/cohort
- journey entry event
- activation definition and window fixed before reading results
- diagnosed barrier and evidence
- intervention and mechanism hypothesis
- control/comparison when feasible
- primary business-relevant activation outcome
- supporting journey metrics
- downstream guardrails
- instrumentation and identity requirements
- exposure/allocation method
- decision window matched to value timing
- stop/rollback conditions
- implementation owner and authorization state

Route causal-validity design to `$tracking-measurement` when the conclusion needs to be causal.

## Metric hierarchy

### Primary
Prefer the defined meaningful-value event or a validated proxy.

### Supporting
Examples:

- step completion
- setup completion
- error rate
- assistance request
- time in step
- time-to-value
- abandon/stall rate

Supporting metrics diagnose why the primary result moved. They do not replace it.

### Guardrails
Depending on the business:

- refund/cancellation
- complaint/support burden
- service capacity
- quality/error rate
- safety/compliance
- downstream retention/repeat use
- contribution/revenue quality
- lead/customer quality

## Avoid activation metric gaming

Reject designs that:

- shorten the activation window after seeing a favorable early result
- change the denominator after randomization/exposure
- redefine activation to a more common event because the true value event did not move
- remove qualification or required safeguards to inflate completion
- auto-complete or system-generate the event being measured
- optimize tutorial/checklist completion while value is unchanged
- ignore negative downstream effects because activation rate increased

## Handoff map

Activation often diagnoses a problem whose implementation belongs elsewhere.

### `$tracking-measurement`
Owns event integrity, attribution/reconciliation where relevant, causal method, experiment validity, and post-test learning classification.

### `$lifecycle-marketing`
Owns onboarding/activation communication segmentation, triggers, cadence, suppression, and deliverability.

### `$copywriting`
Owns the wording for approved onboarding, help, instructional, reminder, and reassurance messages.

### `$cro`
Owns bounded page/form/conversion-surface UX where the activation intervention uses those surfaces. Activation keeps ownership of the post-conversion value decision.

### `$icp-jtbd`
Owns upstream segment/fit decisions when low activation is caused by poor-fit acquisition rather than the activation journey.

### `$offer-strategy`
Owns promise/deliverable expectation changes when the journey reveals a mismatch between what was sold and what customers actually receive.

### `$retention-economics`
Owns mature downstream cohort effects. Activation should not claim that a lift in first value guarantees improved LTV or churn.

### `$marketing-operations`
Owns recurring activation-health checks, condition watches, state, alert dedupe, escalation, and runtime truth when a repeated operating loop is needed.

### Product/service/operations owner
Owns product feature, fulfillment, service process, integration, support, or operational implementation not governed by a Marketing OS specialist.

Do not hide an ownership gap by pretending Activation can implement product or service changes directly.

## Decision outcomes

Classify an activation experiment or intervention as:

- supports the local hypothesis
- contradicts the local hypothesis
- inconclusive / underpowered / immature
- guardrail harm
- invalid / compromised

Then route the learning record to `$tracking-measurement`'s Experiment Learning System. A local activation win does not become a universal onboarding best practice.

## Rollout

Before wider rollout confirm:

- the value definition is unchanged
- source instrumentation is healthy
- the affected segment matches the evidence scope
- guardrails cleared the intended observation window
- operational capacity can support the change
- any new lifecycle communications preserve consent/suppression rules
- any product/service mutation has the correct implementation owner and approval
- rollback path is known where reversible

## Exact status

Keep these separate:

`hypothesis → designed → approved → configured/implemented → live → observed → verified`

Do not call an activation program “working,” “optimized,” or “verified” merely because the intervention was launched or a supporting metric moved.
