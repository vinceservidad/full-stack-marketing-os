# Experimentation Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: methodology / process
- Decision: whether a test can produce a valid decision and what scoped learning it supports
- Evidence status: stable operating method
- Freshness: stable; confirm platform-specific implementation separately

A valid experiment connects one decision to one falsifiable hypothesis. A completed experiment becomes durable knowledge only after validity, scope, uncertainty, and transfer limits are recorded.

## Minimum pre-test specification

- Problem and evidence
- Prior relevant learning
- Hypothesis and expected mechanism
- Control and variant
- Population and allocation
- Primary metric and business guardrails
- Required evidence level
- Instrumentation and QA
- Minimum practical effect or decision threshold
- Duration covering relevant cycles and conversion lag
- Stop conditions for harm or invalid data
- Decision rule: ship, iterate, reject, or inconclusive

Avoid repeated peeking, changing several major variables without accepting ambiguity, or declaring a winner from directional noise.

## Post-test learning sequence

1. **Validate execution before direction.** Confirm allocation, treatment fidelity, instrumentation, lag, contamination, duration/sample, and stop-rule adherence.
2. **Classify the result.** Valid-supports, valid-contradicts, valid-inconclusive/null, valid-guardrail-harm, or invalid/compromised.
3. **Record the estimate and uncertainty.** Preserve the primary business outcome, guardrails, decision threshold or MDE, and achieved evidence level.
4. **Separate observation from mechanism.** The measured treatment effect can be valid even when the explanation for it remains an inference.
5. **Make the scoped decision.** Ship, reject, iterate, replicate, collect more data, invalidate/rerun, or stop for harm.
6. **Create a learning record.** Preserve population, surface, geography, period, offer/commercial conditions, platform/product state, contradictions, and what the result does not prove.
7. **Assign transfer status.** Local result → replication candidate → replicated scoped pattern. Conflicting evidence becomes contradicted/unstable rather than being erased.
8. **Generate the next hypothesis only when it resolves valuable uncertainty.** Experiment count and win rate are not objectives by themselves.

A single valid test may support a local implementation when the decision rule and authorization allow it. It does not establish a universal best practice. Post-hoc segment cuts, external case studies, competitor examples, and platform benchmarks are hypothesis inputs unless independently validated in the relevant scope.

Use [`templates/experiment.md`](../templates/experiment.md) before launch and [`templates/experiment-learning.md`](../templates/experiment-learning.md) after conclusion. Detailed knowledge-promotion rules live under `$tracking-measurement` in `references/experiment-learning-system.md`.
