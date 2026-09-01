# Marketing Operations Loop

## Knowledge metadata

- Primary type: workflow / process
- Decision: how recurring marketing work moves safely from trigger to verified outcome
- Owner: `$marketing-operations`
- Evidence status: stable operating method; each run inherits the evidence quality of its sources and specialist decisions
- Authorization: read-only by default; mutating steps require explicit valid approval

## Canonical sequence

`Trigger → Load checkpoint → Validate sources/freshness → Route specialist checks → Diagnose/decide → Approval gate → Execute or hand off → Verify implementation → Record state → Record learning/context → Notify/escalate/no-op → Schedule/await next trigger`

Not every loop needs every step. Omissions must be deliberate and justified.

## Step 1 — Trigger

Identify why this run exists:

- fixed cadence
- verified event
- condition-watch check
- verified state change

Record trigger time, trigger source, relevant entity/window, and dedupe key.

## Step 2 — Load checkpoint

Read the last durable state before collecting new evidence. Determine:

- last completed run
- last processed entity/window
- unresolved prior action
- prior alert state
- approval state/expiry
- pending verification

If state cannot determine whether a prior mutation occurred, stop the mutating path and verify/escalate.

## Step 3 — Validate sources and freshness

Check only the evidence needed for the recurring decision. Confirm:

- source available
- metric/definition unchanged or disclosed
- data sufficiently mature for the decision
- shared Marketing Context fields used are current enough
- platform-specific claims pass freshness requirements

A stale input can downgrade the run to read-only or block it entirely.

## Step 4 — Route specialist checks

`$marketing-operations` coordinates. The domain owner still decides.

Examples:

- Google Ads health/optimization → `$google-ads`
- Meta delivery → `$meta-ads`
- cross-channel anomaly → `$performance-diagnostics`
- offer review → `$offer-strategy`
- creative fatigue/iteration → `$creative-strategy`
- landing/page issue → `$cro`
- experiment validity/learning → `$tracking-measurement`
- scaling/pacing → `$optimization-scaling`
- recurring executive communication → `$marketing-reporting`

Use the smallest useful specialist set.

## Step 5 — Diagnose or decide

State:

- current evidence
- domain owner's decision
- confidence/evidence state
- whether action is needed
- no-op reason if not

“No action” is a valid result when the evidence does not justify intervention.

## Step 6 — Approval gate

Before any live mutation, confirm authorization covers:

- exact action type
- entity/scope
- quantitative bounds if relevant
- current conditions
- expiry
- stop/rollback rule

If not, emit an approval request and stop the mutating path.

## Step 7 — Execute or hand off

Only the authorized runtime/domain owner performs the live mutation. Record:

- intended action
- submitted/saved/live status
- execution identifier if available
- timestamp
- expected verification source

A written loop workflow does not itself constitute execution.

## Step 8 — Verify implementation

Confirm the source system reflects the intended change. Distinguish:

- submitted/saved
- live/processing
- observed
- verified

If business impact requires a later observation window, create a pending-verification state rather than claiming success.

## Step 9 — Record state

Persist the checkpoint, dedupe key, decision, authorization used, action state, verification state, and unresolved items.

Do not overwrite failed/skipped history.

## Step 10 — Record learning/context

- validated experiment learning → `$tracking-measurement`
- reusable context change → `$marketing-intake`
- specialist-specific operational pattern → owning skill

Repeated observation alone is not causal proof.

## Step 11 — Output policy

Emit exactly what the loop contract requires:

- alert
- approval request
- decision summary
- recurring report handoff
- escalation
- no output when nothing materially changed

Avoid duplicate alerts by using condition state and re-arm rules.

## Step 12 — Continue, pause, or retire

End each run with one explicit status:

- next run eligible normally
- waiting for data maturity
- waiting for approval
- waiting for verification
- degraded / retryable
- paused / escalated
- retired

## Example loop shapes

### Paid-media review loop

`Weekly trigger → validate cost/revenue windows → channel audit → performance diagnosis if anomaly → pacing/scaling decision if eligible → approval if mutation → execute → verify → log decision/learning`

### Creative learning loop

`New creative data window → validate sample → creative-strategy read → identify fatigue/winner hypothesis → tracking-measurement learning status → draft next controlled test → no live launch without channel approval`

### Conversion loop

`Page-change/event trigger → verify deployment → wait for valid observation window → CRO review → experiment learning → keep/iterate/revert decision → log context`

### Condition-watch loop

`Scheduled check → read current condition + prior alert state → validate persistence/window → if unchanged false: no output → if newly true: route specialist → alert/approval request → set notified state → re-arm only after reset rule`

## QA

A valid loop has a justified trigger, durable checkpoint, source/freshness gate, domain owner for each substantive decision, idempotency for repeated effects, approval before mutation, implementation verification, bounded output policy, explicit escalation/stop behavior, and exact runtime status.
