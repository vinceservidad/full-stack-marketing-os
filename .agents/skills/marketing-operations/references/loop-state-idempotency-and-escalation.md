# Loop State, Idempotency, and Escalation

Repeated work becomes unsafe when the system cannot tell what already happened. Use this reference for durable state, duplicate prevention, retries, approvals, and escalation.

## State model

At minimum, persist enough state to answer:

- what entity/event/window this run is processing
- last successful checkpoint
- last attempted checkpoint
- inputs/source versions used
- decision produced
- approval state and scope
- mutation attempted or completed
- verification result
- alert/output emitted
- unresolved failure or escalation

State should be durable enough that a retry can resume safely rather than guessing.

## Idempotency

An idempotent run can be retried without causing an unintended second effect.

For each mutating or notifying step define a dedupe key, for example:

`loop_id + entity_id + decision_window + action_type + approved_change_version`

The exact shape depends on the system, but it must distinguish a genuinely new action from a retry of the same action.

### Before a mutation

Check:

1. Has this action/version already been applied?
2. Is the prior result verified, unknown, failed, or still processing?
3. Is the current approval still valid for this exact action?
4. Did any decision-relevant input change since approval?

If state is ambiguous, do not repeat the mutation. Verify or escalate.

### Before a notification

Check:

- has this condition already been reported?
- has the condition materially changed?
- has the reset/re-arm rule been met?
- is a reminder interval explicitly configured?

Suppress duplicate alerts by default.

## Retry behavior

Separate retryable failures from decision failures.

Retryable examples:

- temporary source timeout
- transient API/service error
- runtime interruption before mutation was attempted

Do not blindly retry:

- unknown mutation state
- expired approval
- contradicted inputs
- measurement integrity failure
- guardrail breach
- source schema/definition change

Use bounded retries and backoff where the runtime supports them. Escalate when the failure type cannot be safely retried.

## Approval scope

A reusable approval must state:

- loop/action it covers
- entity scope
- allowed mutation types
- quantitative limits where relevant
- valid period or expiry
- stop/rollback conditions
- who/what granted approval

Approval for one run is not automatically approval for future runs. Approval for a budget pacing correction is not approval for scaling beyond the authorized plan.

## Verification

Never equate an API success or saved state with business verification.

Use staged status where relevant:

`proposed → approved → submitted/saved → live/processing → observed → verified`

Post-action verification should confirm the source system reflects the intended change and, when necessary, that the downstream effect can be measured. Marketing performance verification may require a later observation window owned by the relevant specialist.

## Escalation classes

### Data escalation

Trigger when:

- source unavailable beyond allowed delay
- metric definition changed
- data contradicts the current context
- measurement integrity is unresolved

Route to `$marketing-intake`, `$tracking-measurement`, or the source owner as appropriate.

### Decision escalation

Trigger when:

- evidence falls below the required threshold
- several specialists disagree on a decision-relevant premise
- a new condition falls outside the loop's approved rules
- the decision would expand scope beyond the loop contract

End the automated path at a human/specialist decision request rather than improvising.

### Authorization escalation

Trigger when:

- approval missing, expired, ambiguous, or narrower than the proposed action
- a mutating step has no rollback/stop rule
- current conditions differ materially from those approved

Do not act.

### Safety/commercial escalation

Trigger when:

- business guardrail breached
- spend/revenue risk exceeds approved bound
- customer/legal/compliance risk appears
- repeated failures suggest the loop itself is unsafe

Pause the mutating path until the owning specialist resolves the issue.

## Stop and retirement

A loop needs explicit conditions that stop normal runs or end the loop entirely.

Possible stop conditions:

- source becomes invalid
- operating assumption is contradicted
- threshold is breached
- authorized action limit reached
- runtime repeatedly fails
- required specialist is unavailable

Possible retirement conditions:

- business objective no longer exists
- campaign/product/channel is retired
- the decision moved into another governed process
- marginal value of the loop no longer exceeds operating cost
- the condition is no longer expected to recur

Retirement should preserve history rather than deleting evidence of prior runs.

## Failure-safe rule

When the system cannot establish whether a live action already occurred, prefer verification/escalation over repetition. Duplicate live mutations can be more damaging than a delayed action.
