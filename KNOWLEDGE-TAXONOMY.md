# Marketing OS Knowledge Taxonomy

The Marketing OS uses these terms as distinct operating layers. They are related, but they are not synonyms. Classify a deliverable by its primary purpose and state any secondary layers it contains.

## The operating stack

```text
Principles and definitions
        ↓
Strategy
        ↓
Frameworks and models
        ↓
Methodology
        ↓
Process / playbook / SOP
        ↓
Tactics and techniques
        ↓
Templates and checklists
        ↓
Measurement, experiments, and feedback
        ↓
Patterns and revised heuristics
```

The order is a dependency guide, not a mandatory writing format. A single skill can contain several layers, but the response must name the layer driving the decision.

## Definitions and decision boundaries

| Type | Meaning | Marketing example | Evidence rule |
|---|---|---|---|
| **Principle** | Durable rule or constraint that governs decisions | Protect the primary business outcome; do not call ROAS profit | State as a governance rule; revise only deliberately |
| **Definition / standard** | Contract for what a term, metric, or state means | Net revenue includes refunds under the client's stated source definition | Record source, scope, and included costs/stages |
| **Strategy** | Directional choice about where to compete, for whom, why, and how resources are allocated | Acquire profitable new customers while protecting branded demand | Tie to a business outcome, constraints, and trade-offs |
| **Framework** | Structured lens or decision map | Demand → auction → click → site → outcome decomposition | Explains how to reason; does not prove a result |
| **Model** | Simplified representation, relationship, or formula | Revenue = traffic × conversion rate × AOV | Show variables, assumptions, and limits |
| **Methodology** | Named way of solving a class of problems | Evidence-led audit, JTBD research, controlled experimentation | State steps, evidence standard, and decision rule |
| **Process** | Ordered repeatable workflow | Intake → measure → diagnose → plan → approve → test → verify | State owner, inputs, outputs, handoffs, and status |
| **Playbook / SOP** | Process adapted to a recurring context or scenario | Ecommerce Shopping diagnostic playbook | Include prerequisites, exceptions, escalation, and QA |
| **Pattern** | Recurring shape in observed evidence | Frequency rises while outbound CTR falls | Pattern is not causality; name source, scope, and sample |
| **Hypothesis** | Falsifiable explanation or proposed mechanism | Creative fatigue may be reducing qualified response | Include disconfirming evidence and test design |
| **Tactic** | Specific action chosen to advance a strategy | Add a PMax negative keyword or launch a new creative angle | State target, expected effect, risk, and approval |
| **Technique** | Method for executing one tactic or process step | Search-term mining with intent and economic thresholds | Explain how it works and when it fails |
| **Template** | Reusable structure for producing an artifact | Audit, creative brief, or experiment brief | Keep placeholders explicit; do not imply completed work |
| **Checklist / QA** | Completeness and validation control | Pre-launch event and claim checklist | Must test observable invariants, not only wording |
| **Best practice** | Evidence-backed default that is broadly useful in a defined scope | Verify post-payment purchase events before bidding on them | Scope, source, date, and exceptions are required |
| **Heuristic** | Practical shortcut used under uncertainty | Do not pause a keyword solely because a small sample has no conversion | Label as heuristic; never present as a guarantee |
| **Guardrail / policy** | Limit that protects against unacceptable downside | No budget increase while measurement integrity is unknown | State trigger, owner, and escalation or stop action |

## How to classify a response

1. Identify the decision or business outcome.
2. Select one primary type from the table. Add secondary types only when they materially help the user.
3. Separate claims from actions: a pattern or model is not a recommendation; a tactic is not a strategy.
4. Label evidence as `observed`, `calculated`, `experimentally observed`, `inferred`, `assumed`, or `unknown` using `GLOSSARY.md`.
5. For best practices and heuristics, state scope, confidence, freshness, and the condition that would override them.
6. For a live recommendation, state authorization, rollback/stop condition, and exact status.

## Artifact metadata contract

When creating or materially revising an OS artifact, record the following fields. Use [templates/knowledge-artifact.md](templates/knowledge-artifact.md) when a standalone artifact needs a header.

```yaml
artifact_type: strategy | framework | model | methodology | process | playbook | sop | pattern | hypothesis | tactic | technique | template | checklist | best-practice | heuristic | policy | standard
decision: the decision or business outcome this supports
scope: channel, funnel stage, market, business model, and exclusions
owner: the skill or role accountable for the final interpretation
inputs: required evidence or prerequisites
evidence_status: observed | calculated | officially-documented | account-visible | experimentally-observed | inferred | assumed | unknown
confidence: high | medium | low | not-assessed
freshness: stable | 180-days | 90-days | 30-days | live-check
dependencies: measurement, economics, platform access, approval, or other prerequisites
authorization: read-only | draft | approval-required | live-verified
rollback_or_stop: containment or test stopping condition when action is involved
```

Metadata is a decision aid, not a substitute for the evidence or the artifact itself. Do not mark an artifact `live-verified` without matching verification.

## OS mapping

- `AGENTS.md`, `PLATFORM-CURRENCY.md`, and policies are principles, standards, and governance.
- `GLOSSARY.md` contains definitions and metric contracts.
- `frameworks/` contains frameworks and models.
- `SKILL.md` files contain methodologies, decision rules, and QA.
- `playbooks/` contains processes, SOP-like workflows, and scenario adaptations.
- `references/` contains techniques, platform detail, patterns, and scoped best practices.
- `templates/` contains reusable output structures and checklists.
- `tests/evaluations/` validates whether the layers are being used correctly.
