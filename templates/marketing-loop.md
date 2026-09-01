# Marketing Loop Contract

## Knowledge metadata

- Primary type: template / checklist
- Owner: `$marketing-operations`
- Decision: whether a recurring operating loop is sufficiently specified and controlled to run safely
- Evidence status: reusable structure; each run inherits source and specialist evidence states
- Authorization: read-only by default; live mutation requires explicit valid approval

## Identity and State

- Loop ID:
- Loop version:
- Loop owner:
- Status: designed | approved-to-configure | configured | active-verified | paused | degraded | retired
- Runtime / scheduler / trigger mechanism:
- Last successful run:
- Last failed/skipped run:
- Change log:

## Objective

- Business objective:
- Recurring decision or burden:
- Primary business outcome:
- Guardrails:
- Why a recurring loop is justified:

## Trigger and Cadence

- Trigger type: fixed cadence | event | condition-watch | state-change
- Trigger/cadence definition:
- Trigger source:
- Earliest useful next run:
- Maximum acceptable delay:
- Data/decision lag:
- Quiet/blackout window if relevant:
- Re-arm/reset rule for condition watches:

## Scope

- Business / market:
- Channel / surface / entity scope:
- Decision window:
- Explicit exclusions:

## Source and Freshness Gates

| Source / artifact | Used for | Required freshness / maturity | Owner | Block/downgrade rule if missing or stale |
|---|---|---|---|---|
|  |  |  |  |  |

## Routing and Ownership

| Step / decision | Domain owner | Supporting skill(s) | Output needed |
|---|---|---|---|
|  |  |  |  |

## Durable State

- Last processed entity/window:
- Last attempted checkpoint:
- Last successful checkpoint:
- Pending verification:
- Unresolved escalation:
- Prior condition/alert state:
- State storage/location:

## Idempotency

- Dedupe key:
- How a genuinely new event/action is distinguished from a retry:
- Mutation already-applied check:
- Duplicate alert suppression:
- Retryable failure classes:
- Non-retryable / escalate-first classes:

## Run Sequence

1. Trigger:
2. Load state/checkpoint:
3. Validate inputs/freshness:
4. Route specialist checks:
5. Diagnose/decide:
6. Approval gate:
7. Execute/hand off:
8. Verify implementation:
9. Record state:
10. Record learning/context:
11. Notify/escalate/no-op:
12. Continue/pause/retire:

## Authorization Boundary

- Read-only steps:
- Allowed mutating steps:
- Approval source:
- Scope/entities covered:
- Quantitative limits:
- Approval expiry:
- Conditions that invalidate approval:
- Rollback/stop condition:

## Execution and Verification

- Execution owner/runtime:
- Implementation status source:
- Verification source:
- Expected processing/observation delay:
- What counts as implementation verified:
- What requires later business-performance verification:

## Output and Notification Policy

- Emit when:
- Suppress when:
- Alert recipient/destination if configured:
- Reminder policy:
- Duplicate suppression rule:
- Approval-request format:
- Normal run output:

## Escalation / Stop / Retirement

- Data escalation:
- Decision escalation:
- Authorization escalation:
- Commercial/safety escalation:
- Pause condition:
- Resume condition:
- Retirement condition:

## Learning Handoff

- Experiment learning owner:
- Marketing Context update rule:
- Specialist learning destination:
- What must not be promoted to causal/best-practice status:

## Run Record

For each run preserve:

- run ID/time
- trigger and entity/window
- source versions/evidence state
- decisions and owners
- approval used
- action state
- verification state
- output/alert state
- learning/context updates
- errors/skips/escalations
- exact run status

## QA

Confirm trigger/cadence is justified; state is durable; retries cannot duplicate live effects; every substantive decision has a domain owner; source/freshness gates are explicit; live changes cannot bypass authorization; output noise is controlled; stop/escalation/retirement exists; and `active-verified` is used only after an actual expected run has been observed successfully.
