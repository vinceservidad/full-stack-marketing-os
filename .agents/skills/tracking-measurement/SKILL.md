---
name: tracking-measurement
description: Audit, design, or diagnose marketing conversion measurement, attribution reconciliation, event integrity, experiment validity, and reusable experiment learning; not for changing production tracking without approval or turning one test into a universal best practice.
---

# Tracking and Measurement

Classify architecture maps, models, methodologies, processes, checklists, experiment results, and recommendations with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Keep a collection defect, attribution difference, business-performance change, experimental estimate, and reusable learning as distinct evidence categories.

Establish whether the available data can support the requested decision before optimizing against it. Keep three questions distinct: is the data collected correctly, do sources agree, and did the activity cause the result. A causal question inherits every collection defect beneath it.

## Scope

Define the primary business outcome, platforms and properties, conversion journey, reporting timezone and currency, consent environment, attribution question, source of truth, and requested level of assurance. For a causal question, also define the decision at stake, its cost of being wrong, and the evidence level it requires. For an experiment-learning request, define the tested scope, pre-registered decision rule, domain owner, and whether the result is being used locally or considered for transfer. Reserve “Primary conversion action” for Google Ads' action-optimization status.

## Method

1. Map the event chain from user action to browser/server collection, platform receipt, deduplication, attribution, reporting, and business-system outcome.
2. Inventory each event's name, trigger, parameters, identifiers, value/currency, counting rule, destination, and primary/secondary role.
3. Test integrity across coverage, correctness, uniqueness, ordering, timeliness, identity continuity, consent behavior, and reconciliation.
4. Separate collection failures from attribution differences and reporting lag.
5. Reconcile using matched definitions and cohorts; explain expected gaps instead of forcing equality.
6. For a causal question, grade the available evidence, select a method the constraints actually permit, and state the level the result can reach before running it.
7. Rank fixes and tests by decision risk, affected volume/value, confidence, reversibility, validation cost, and learning value.
8. When an experiment concludes, validate execution before reading direction, classify the result, separate observed effect from mechanism interpretation, and create a scoped learning record using [Experiment Learning System](references/experiment-learning-system.md) and [`templates/experiment-learning.md`](../../../templates/experiment-learning.md).
9. Before a new experiment, inspect relevant prior learning for same decision, mechanism, segment, surface, offer state, guardrail failure, or contradiction. Use prior learning to change the new test or explain why it is not decision-relevant.

Read only the reference the question requires:

- Event-level QA: [event integrity](references/event-integrity.md).
- Totals differ across platforms or business systems: [attribution reconciliation](references/attribution-reconciliation.md).
- Grading how strongly evidence supports a causal claim: [causal evidence ladder](references/causal-evidence-ladder.md).
- Choosing how to measure incremental effect: [incrementality method selector](references/incrementality-method-selector.md).
- Randomized audience split: [holdout experiments](references/holdout-experiments.md).
- Geographic treatment and control, matched markets, synthetic control, switchback: [geo experiments](references/geo-experiments.md).
- Platform-native lift mechanisms: [platform lift studies](references/platform-lift-studies.md).
- Long-horizon cross-channel allocation: [Marketing Mix Modeling](references/marketing-mix-modeling.md).
- Several imperfect sources and no decisive test: [triangulation](references/measurement-triangulation.md).
- Turning completed tests into durable scoped knowledge and a decision-relevant backlog: [Experiment Learning System](references/experiment-learning-system.md).

## Rules

- Do not declare tracking healthy from a tag firing once; verify payload quality, receipt, deduplication, downstream reporting, and business reconciliation.
- Do not make several production tagging changes at once when one controlled change can isolate the failure.
- Never expose secrets, raw personal data, or persistent identifiers in reports.
- Do not change primary conversion goals or bidding signals without explicit approval and a dependency analysis.
- For Google Ads, distinguish conversion goals from their conversion actions and each action's Primary/Secondary status. For Meta, distinguish objective, conversion location, performance goal, dataset/pixel, selected event, and attribution setting.
- Treat consented and non-consented coverage explicitly; do not recommend bypassing consent or privacy controls.
- Platform attribution never supports a causal claim at any volume. Report its evidence level rather than its confidence.
- Do not design a causal test while measurement integrity is unresolved; the test inherits the defect.
- Power the test, fix the primary metric and stopping rule before launch, and include the full conversion lag. Do not stop early on a favorable read or switch the primary metric afterwards.
- Report a null with its minimum detectable effect. Absence of evidence is not evidence of absence.
- Do not sum attributed conversions across platforms, and do not average an experimental estimate with an attributed one.
- State the scope of every causal estimate — population, geography, period, spend range. A result proven in one scope is not proven outside it.
- Count the holdback's forgone revenue as part of a test's cost.
- Assess experiment validity before result direction. A favorable outcome does not repair instrumentation defects, contamination, treatment drift, early stopping, or missing conversion lag.
- Do not call a null/inconclusive result a control winner by default, and do not call guardrail-harming treatment a winner because the primary metric improved.
- Separate the observed treatment effect from the story used to explain it. A result can support an outcome claim without proving the proposed mechanism.
- A single experiment remains a local result unless stronger replication supports a broader scoped pattern. Never promote one test, competitor example, external case study, or platform benchmark into a universal best practice.
- Post-hoc segment cuts generate hypotheses unless independently validated. Do not promote the most favorable slice into durable learning.
- Preserve contradictory tests and the conditions under which each occurred. Do not rewrite the learning archive to make the latest result look consistent.
- An experiment backlog exists to resolve valuable uncertainty, not to hit an arbitrary test count, win-rate benchmark, or calendar cadence.

## Output

Return: decision supported; architecture map; integrity status by event; reconciliation table; confirmed defects; expected discrepancies; risk-ranked actions; validation plan; exact implementation status.

Causal question: decision and required evidence level; achievable level and why; selected method with the constraints that chose it; primary metric and its definition; minimum detectable effect, duration, and stopping rule; contamination and confounding risks with direction; holdback cost; scope of the resulting estimate; what the result may and may not be used for.

Experiment learning: validity class; observed result and uncertainty; achieved evidence level; guardrail status; observation versus mechanism interpretation; operational disposition; scoped learning statement; transfer status; contradictions/dependencies; next hypothesis or reason no follow-up is justified; backlog change; exact status.

## Library references

Owned root artifacts, read when their scope applies:

- [measurement-and-evidence.md](../../../frameworks/measurement-and-evidence.md) — measurement and evidence framework.
- [experimentation.md](../../../frameworks/experimentation.md) — general experimentation framework.
- [experiment.md](../../../templates/experiment.md) — pre-test experiment brief format.
- [experiment-learning.md](../../../templates/experiment-learning.md) — post-test validity, learning, transfer, and follow-up record.

## QA

Confirm event definitions and timezones match, test and production traffic are separated, duplicate paths are checked, values/currency are verified, attribution windows are visible, privacy boundaries are preserved, and “received” is not confused with “correct.” For a causal question, confirm the evidence level is stated, the method matches the constraints, the test was powered before launch, contamination and coincident events were assessed, the business outcome rather than a platform proxy was measured, and the estimate's scope is named. For experiment learning, confirm validity was assessed before direction, the pre-test decision rule was preserved, full relevant lag is included, nulls and guardrail harms are classified correctly, mechanism remains separate from observed effect, post-hoc slices are not promoted, transfer status does not exceed replication evidence, and contradictory prior results remain visible.