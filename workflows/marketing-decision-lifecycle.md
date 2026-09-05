# Marketing Decision Lifecycle

## Knowledge metadata

- Primary type: workflow / process
- Decision: how a marketing request moves from decision context to verified learning without duplicating specialist ownership
- Orchestration owner: `$marketing-router`
- Specialist ownership: retained by the skill that owns each substantive decision
- Evidence status: stable operating method; each stage inherits the evidence quality of its sources and specialist artifacts
- Authorization: read-only by default; this workflow never authorizes a live mutation by itself

## Canonical lifecycle

`CONTEXT → GOAL → STRATEGY → PLAN → EXECUTE → REVIEW → OPTIMIZE ↺`

This is a state model, not a mandatory seven-step checklist. Start at the earliest unresolved stage that can materially change the requested decision. Skip stages already satisfied by current evidence, an approved artifact, or the user's bounded request. Re-enter an earlier stage when new evidence invalidates an assumption, changes the business objective, or supersedes the strategy.

The lifecycle coordinates existing Marketing OS owners. It does **not** create separate `context`, `goal`, `strategy`, `plan`, `execute`, `review`, or `optimize` skills.

Runtimes or interfaces may expose labels such as `/context`, `/goal`, `/strategy`, `/plan`, `/execute`, `/review`, and `/optimize` as convenience aliases. Those labels must route to the governed owners below rather than become a competing instruction layer.

## Stage map

| Stage | Core question | Default ownership | Exit condition |
|---|---|---|---|
| `context` | What do we know, how do we know it, and what is missing? | `$marketing-intake` when evidence, definitions, economics, scope, or authorization are materially unclear | Decision-relevant context is sufficient for the next decision, or remaining gaps are explicitly labeled and safe to carry |
| `goal` | What outcome or decision must change? | `$growth-strategy` for business-level objective framing; the domain owner for an already-bounded specialist objective | Outcome, scope, baseline/desired direction where relevant, horizon, and guardrails are explicit enough to govern the work |
| `strategy` | Where will we focus and why? | `$growth-strategy` for integrated business direction; the specialist owner for domain strategy | Strategic choice, mechanism/hypothesis, non-priorities or boundaries, and evidence state are explicit |
| `plan` | Who does what, in what order, with what dependencies and decision rules? | `$marketing-router` coordinates decomposition; specialist skills own their workstream decisions | Owners, sequence/dependencies, required artifacts, measurement, and approval boundaries are clear enough to act |
| `execute` | What work should be created, configured, published, or changed now? | Owning specialist plus the actually available authorized runtime/tool | Intended action is completed to an exact implementation state and verification requirement is recorded |
| `review` | What actually happened relative to the goal and guardrails? | Domain owner, `$performance-diagnostics`, `$tracking-measurement`, `$marketing-reporting`, or `$growth-strategy` according to the decision | Evidence is mature enough to support a bounded decision, or review remains explicitly pending/blocked |
| `optimize` | What should change next given the learning? | Domain owner; `$optimization-scaling` for paid-media scale/de-scale and allocation decisions | Continue, hold, revise, kill, reprioritize, or route to scaling is decided and the next lifecycle stage is named when useful |

## Stage detection

1. Identify the requested deliverable or decision and the current implementation state.
2. Check whether decision-relevant context already exists in the request, current Marketing Context, specialist artifacts, or source systems.
3. Identify the **earliest unresolved lifecycle stage that can reverse the requested decision**. That is the current stage.
4. Do not restart at `context` merely because the workflow begins there. A simple bounded rewrite can begin at `execute`; a performance drop can begin at `review`; a proven paid-media expansion request can begin at `optimize`.
5. Do not skip a blocking earlier stage. Missing profitability inputs may force a scaling request back to `context`; an undefined business objective may block an integrated strategy; an unapproved live mutation may block `execute` even when the plan is complete.
6. Route the current stage to one primary owner and only the supporting owners needed for distinct dependencies.
7. Record the next decision point only when it helps continuation. Do not manufacture a future stage for a task that is complete.

## Stage contracts

### 1. Context

Use `$marketing-intake` when scope, provenance, economics, metric definitions, source of truth, access, or authorization could change the decision.

Minimum output when context is active:

- primary business outcome or bounded task objective if known
- scope and relevant period
- source/evidence state
- decision-relevant economics and constraints when applicable
- unknowns/contradictions capable of reversing the decision
- authorization boundary
- exact context status: `sufficient`, `partial`, or `blocked`

A lightweight task does not require a formal intake artifact when the request itself supplies enough safe context.

### 2. Goal

For integrated growth work, `$growth-strategy` owns the primary business outcome, baseline, horizon, economic boundary, quality guardrails, and supplied target or desired direction. Do not invent a target merely to fill the stage.

For bounded specialist work, preserve the already-supplied objective instead of escalating every task into business-level strategy.

A valid goal controls downstream trade-offs. A local proxy such as CTR, CPC, engagement, activation rate, or ROAS must not silently replace the actual business outcome when that outcome is observable.

### 3. Strategy

Strategy is a choice, not a task list.

For business-level work, `$growth-strategy` owns the constraint structure, opportunity set, strategic bets, non-priorities, sequence, and learning agenda. For a bounded domain strategy, the relevant specialist owns the technical or commercial decision inside its scope.

Record:

- chosen direction
- evidence/mechanism supporting it
- material alternatives or non-priorities
- what would change the choice
- owner and status

### 4. Plan

Planning decomposes an approved or decision-ready direction into owned workstreams. `$marketing-router` coordinates only when multiple owners are needed.

A useful plan names:

- workstream and specialist owner
- deliverable/decision
- dependency and sequence
- evidence/measurement requirement
- approval or live-mutation boundary
- stopping/review rule where relevant

The plan never transfers decision authority from a specialist to the router or growth strategy.

### 5. Execute

Execution routes to the owning specialist and the actually available tool/runtime. Before material live mutation, validate the action, scope, downside, rollback/stop condition, and authorization.

Use exact implementation states rather than a generic `done`:

`draft → saved/configured → published → live → processing → verified`

Not every artifact uses every state. Never infer a later state from an earlier one.

### 6. Review

Review compares mature evidence with the goal and guardrails.

Common owners:

- metric/business anomaly → `$performance-diagnostics`
- experiment validity, attribution, or causal learning → `$tracking-measurement`
- single-domain outcome → the domain owner
- cross-channel stakeholder synthesis → `$marketing-reporting`
- integrated strategy progress or reprioritization → `$growth-strategy`

Separate observed results from mechanism interpretation. A channel metric can diagnose a system without becoming the business success criterion.

### 7. Optimize

Optimization is a new decision made from review evidence, not a synonym for “make the number better.”

Possible outcomes:

- `continue`
- `hold`
- `revise`
- `kill`
- `reprioritize`
- `route to scaling`

The domain owner handles ordinary optimization inside its scope. `$optimization-scaling` owns paid-media scale readiness, marginal economics, controlled allocation/coverage expansion, de-scaling, and rollback. A fixed percentage budget increase is not a lifecycle rule.

Optimization may return to any earlier stage:

- new evidence invalidates product/customer truth → `context`
- business priority changes → `goal` or `strategy`
- strategy stands but work decomposition changes → `plan`
- approved next iteration is ready → `execute`
- more mature evidence is required → `review`

## Decision record

Use [`templates/marketing-decision-record.md`](../templates/marketing-decision-record.md) when continuity across agents, sessions, or several lifecycle stages matters. Do not create one for every tiny task.

The record stores lifecycle state and links to specialist artifacts; it does not replace Marketing Context, strategy records, experiment records, campaign artifacts, or other specialist-owned sources.

## Relationship to Marketing Operations

This lifecycle governs the state of a bounded marketing decision or initiative. [`marketing-operations-loop.md`](marketing-operations-loop.md) governs **recurring** execution with cadence/triggers, checkpoints, idempotency, approval reuse, alerts, escalation, and runtime verification.

A recurring loop may invoke this lifecycle during a run, but the two are not interchangeable:

- decision lifecycle: where this decision currently is
- operations loop: how repeated runs are safely triggered and coordinated

## Examples

### New business growth plan

`context → goal → strategy → plan`

Execution begins only after the relevant workstream decisions and approvals are ready.

### Existing account performance drop

`review → optimize → execute → review`

Do not rebuild the business strategy unless the evidence shows the prior objective or strategic assumptions no longer hold.

### Approved creative production task

`execute → review`

If the concept and evidence are already approved, do not force new intake or growth strategy.

### Simple copy rewrite

`execute`

The request itself can satisfy context, goal, strategy, and plan when the wording change is bounded and safe.

### Profitable campaign asking for more budget

`optimize`

Route to `$optimization-scaling`; if economics or source-of-truth evidence are missing, step back to `context` before a scale decision.

## QA

A valid lifecycle decision names the current stage only when useful, starts at the earliest **materially unresolved** stage rather than blindly at `context`, preserves one primary owner, does not create duplicate lifecycle skills, does not confuse strategy with planning or planning with execution, preserves exact implementation state, requires authorization before live mutation, evaluates results against the relevant business outcome and guardrails, routes paid-media scaling to `$optimization-scaling`, and allows learning to move the work backward or forward without rewriting history.