# Loop Design and Governance

Use this reference to decide whether recurring work should exist at all, what should trigger it, and how ownership stays clear across repeated runs.

## When a loop is justified

A recurring loop should reduce at least one real operating burden:

- repeated decision work with stable inputs and rules
- meaningful delay between a change occurring and someone noticing it
- recurring quality-control or compliance risk
- repeated reconciliation or review that must preserve definitions over time
- a condition that should trigger a bounded response when it changes
- a learning cycle where prior results should inform the next run

Do not automate a task merely because it is repetitive if the decision itself is rare, highly bespoke, or cheaper to handle manually.

## Trigger models

### Fixed cadence

Run at a defined interval when the decision is inherently periodic, such as a weekly account review or monthly cohort review.

Choose cadence from:

- how quickly the underlying state can meaningfully change
- data/reporting lag
- minimum sample needed for a valid decision
- operational risk of waiting
- cost of reviewing too often

A daily cadence is not automatically more responsive; it can create noisy reversals when the metric needs a longer window.

### Event-triggered

Run after a specific verified event, such as:

- campaign launched
- experiment completed
- product price changed
- landing page published
- tracking configuration changed

The event must have a dedupe key or durable identifier so the same event is not processed repeatedly.

### Condition-watch

Run checks on a schedule but emit/escalate only when a defined condition becomes true. The condition must specify:

- metric/state evaluated
- evidence source
- threshold or logical rule
- minimum persistence/window if needed
- reset/re-arm behavior
- alert dedupe rule

Do not use a volatile single-point threshold where a persistence rule is required to avoid false alerts.

### State-change

Run when an entity moves from one verified state to another, such as `approved → live`, `processing → verified`, or `healthy → degraded`.

Do not infer a state transition merely because time passed. Confirm it from the source system.

## Loop ownership

Separate three roles:

1. **Loop owner** — owns the recurring process contract, state, cadence/trigger, handoffs, and run history. Usually `$marketing-operations`.
2. **Decision owner** — owns the substantive decision for a step. This remains the relevant domain skill.
3. **Execution/runtime owner** — system, user, or authorized integration that actually schedules, mutates, or sends output.

These can be different. A loop can be well-designed while not yet having a runtime capable of executing it.

## Run classes

### Read-only review loop

Collects evidence, invokes specialists, records findings, and produces an output. No live mutation.

### Decision loop

Produces a decision or recommendation at each run. If execution is not authorized, the run ends at `proposed` or `approval required`.

### Mutating loop

May make a bounded live change only when all of these are explicit:

- allowed mutation class
- exact scope/entities
- hard limits
- approval source and expiry
- rollback/stop rule
- post-change verification
- durable state proving what was changed

If any are missing, downgrade to a decision loop.

## Cadence governance

Every loop needs:

- normal cadence or trigger
- earliest useful next run
- maximum acceptable delay
- blackout/quiet windows when relevant
- trigger priority if several conditions occur together
- backoff behavior after failure
- retirement review

Do not let the schedule become independent of the decision. If the signal is only decision-ready monthly, a daily decision loop should not manufacture daily actions.

## Lifecycle states

Use exact status language:

- `designed` — specification exists
- `approved-to-configure` — configuration authorized, not yet confirmed
- `configured` — runtime/schedule exists but execution not yet verified
- `active-verified` — at least one expected run was observed successfully
- `paused` — configured but intentionally prevented from running or acting
- `degraded` — runtime works incompletely or required inputs are unavailable
- `retired` — intentionally ended; no further runs expected

Do not use `active` or `running` merely because a file or schedule definition exists.

## Loop health

Judge the loop itself on operational quality, not marketing vanity metrics:

- eligible runs completed
- stale/invalid-input runs correctly blocked
- duplicate actions prevented
- authorization failures correctly stopped
- false/duplicate alerts
- median detection-to-decision latency
- execution verification rate
- unresolved escalations
- operator effort/cost

Business performance remains owned by the domain skills; loop health measures whether the operating mechanism is trustworthy.

## Minimum governance record

For every governed loop, preserve:

- loop ID/version
- objective
- owner
- trigger/cadence
- sources and freshness limits
- state/checkpoint
- specialist routing map
- authorization boundary
- execution mechanism if any
- output/notification rule
- stop/escalation/retirement rules
- last successful run
- last failed/skipped run and why
- change log
