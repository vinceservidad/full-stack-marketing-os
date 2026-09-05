# Marketing Decision Record

Owner: `$marketing-router` for lifecycle state only. Every substantive decision remains owned by its governing specialist skill.

Use this record when a marketing initiative needs continuity across multiple lifecycle stages, agents, sessions, or handoffs. Do not create it for a tiny bounded task that can be completed safely in one step.

Canonical lifecycle: `CONTEXT → GOAL → STRATEGY → PLAN → EXECUTE → REVIEW → OPTIMIZE ↺`

See [`workflows/marketing-decision-lifecycle.md`](../workflows/marketing-decision-lifecycle.md).

## Record State

- Record ID / initiative:
- Business / account / scope:
- Version:
- Current lifecycle stage: context | goal | strategy | plan | execute | review | optimize
- Stage status: active | blocked | satisfied | complete | superseded
- Primary decision owner:
- Supporting owners:
- Source-of-truth system(s):
- Marketing Context version, if used:
- Last updated:
- Next decision point, if any:

Do not mark a stage complete merely because a document exists. Stage state must reflect the decision and evidence actually available.

## 1. Context

Status: not required | active | partial | sufficient | blocked | superseded

- Primary business outcome or bounded task objective:
- Business model / product / service:
- Market / geography:
- Relevant period / horizon:
- Source systems / artifacts:
- Evidence state:
- Metric / lifecycle definitions that matter:
- Economics / profit level, if decision-relevant:
- Capacity / operational constraints:
- Authorization boundary:
- Contradictions / unknowns capable of reversing the decision:
- Context owner / source artifact:

Do not copy raw evidence that belongs in a specialist artifact or source system. Link or name the source and preserve evidence state.

## 2. Goal

Status: not required | active | decision-ready | approved | superseded

| Field | Decision |
|---|---|
| Outcome / decision to change |  |
| Current baseline, if relevant |  |
| Supplied target / desired direction, if any |  |
| Target evidence state |  |
| Time horizon / decision window |  |
| Economic boundary |  |
| Quality / customer guardrails |  |
| What meaningful progress means |  |
| Goal owner |  |

Do not invent a target or replace the business outcome with a convenient platform metric.

## 3. Strategy

Status: not required | draft | decision-ready | approved | under review | superseded

- Strategic choice / direction:
- Constraint, opportunity, or mechanism it addresses:
- Evidence / confidence:
- Material alternatives considered:
- Explicit non-priorities / boundaries:
- What would change the strategy:
- Strategy owner:
- Source strategy / specialist artifact:

Strategy is the chosen direction and rationale. Keep task lists in the Plan section.

## 4. Plan

Status: not required | draft | decision-ready | approved | in execution | superseded

| Workstream | Specialist owner | Decision / deliverable | Dependency / sequence | Measurement / review rule | Approval boundary | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Planning coordinates work; it does not transfer specialist decision ownership.

## 5. Execute

Status: not required | draft | saved/configured | published | live | processing | verified | blocked | superseded

| Action / artifact | Owner / runtime | Intended state | Actual observed state | Verification source | Authorization used | Open issue |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Record only implementation states supported by evidence. A recommendation is not execution; a saved configuration is not verified delivery.

## 6. Review

Status: not required | waiting for maturity | active | decision-ready | blocked | complete | superseded

- Review question:
- Observation window / maturity requirement:
- Primary business outcome:
- Guardrails:
- Observed result:
- Supporting metrics:
- Measurement validity / evidence state:
- Competing explanations:
- Mechanism interpretation, kept separate from observation:
- Review owner:
- Source review / experiment / diagnostic artifact:

### Review decision

- continue | hold | revise | kill | reprioritize | route to scaling | insufficient evidence
- Reason:
- What evidence could reverse this decision:

## 7. Optimize

Status: not required | active | decision-ready | approved | executed | blocked | superseded

- Decision from review:
- Change proposed:
- Domain owner:
- If paid-media scaling/de-scaling: `$optimization-scaling` handoff:
- Marginal/economic evidence required:
- Capacity / guardrails:
- Stop / rollback rule:
- Authorization boundary:
- Next lifecycle stage: context | goal | strategy | plan | execute | review | optimize | complete
- Why that next stage is correct:

Optimization may move backward or forward in the lifecycle. Do not force a linear progression when the evidence changes.

## Decision History

Newest first. Preserve prior decisions rather than rewriting them after results arrive.

| Date | From stage | Decision / evidence change | Owner | To stage | State |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Open Decisions

| Decision | Why it matters | Owner | Blocking evidence / dependency | Status |
|---|---|---|---|---|
|  |  |  |  |  |

## Exact Status

- Current lifecycle stage:
- Current stage status:
- Work actually approved:
- Work actually implemented:
- Work actually verified:
- Open contradiction / blocker:
- Next decision point:

## Usage Rules

- The lifecycle is stateful, not a mandatory checklist.
- Start at the earliest unresolved stage capable of changing the requested decision.
- Skip stages already satisfied by current evidence or a bounded request.
- Use `$marketing-intake` when decision-relevant context is materially unclear.
- Use `$growth-strategy` for integrated business-level objective and strategy decisions; preserve specialist ownership for bounded domain strategy.
- Use `$marketing-router` only to coordinate multi-owner planning and lifecycle state.
- Execution belongs to the owning specialist and an actually available authorized runtime/tool.
- Review must separate observed results from causal/mechanism interpretation.
- Paid-media scale/de-scale and allocation decisions route to `$optimization-scaling`.
- This record does not replace Marketing Context or specialist artifacts and never authorizes a live mutation by itself.