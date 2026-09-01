# Experiment Learning System

Use this reference when experiments need to become durable, reusable knowledge rather than isolated result screenshots or "winner" labels.

`$tracking-measurement` owns experiment validity and the evidence state of the resulting learning. The domain skill that owns the marketing decision still owns what to do with that learning.

## Core principle

An experiment result is scoped evidence, not a universal best practice.

Every learning must preserve:

- the decision and hypothesis tested
- population, surface, geography, period, and operating conditions
- treatment/control definition and implementation fidelity
- primary business metric and guardrails
- measurement integrity and causal evidence level
- estimate, uncertainty, and minimum detectable effect where applicable
- result validity before result direction
- what was observed versus the explanation proposed for it
- what can and cannot be transferred to another context

A test can be statistically clean and still have narrow external validity.

## Result classes

Classify the test before promoting any learning:

1. **Valid — supports hypothesis**: design and measurement were decision-ready and the result supports the pre-registered directional claim within scope.
2. **Valid — contradicts hypothesis**: design was decision-ready and the result provides evidence against the pre-registered claim within scope.
3. **Valid — inconclusive / null**: the result does not resolve the decision at the required effect threshold. Record the uncertainty and MDE; do not call the control a winner by default.
4. **Valid — harmful on guardrail**: primary metric may improve, but a pre-specified business guardrail crosses the stop or rejection threshold.
5. **Invalid / compromised**: instrumentation, allocation, contamination, implementation drift, early stopping, missing lag, or another defect prevents the intended inference.

Do not collapse these into `win / lose`.

## Learning loop

### 1. Link to the pre-test decision

Start from the approved experiment brief. Record:

- evidence-backed problem
- hypothesis and expected mechanism
- control and variant
- primary metric and business guardrails
- pre-registered decision rule
- required and achievable evidence level

If no pre-test record exists, label the analysis post hoc and lower the strength of any mechanism claim accordingly.

### 2. Validate execution before reading direction

Check:

- allocation and exposure integrity
- treatment/control fidelity
- instrumentation health
- conversion lag completeness
- sample/duration requirements
- contamination and coincident changes
- stop-rule adherence
- whether the primary metric was changed or redefined

A favorable result does not repair a broken test.

### 3. Record the result with uncertainty

Capture the business-outcome estimate, confidence/credible interval or other decision-appropriate uncertainty, sample/exposure, guardrail outcomes, and evidence level.

Do not substitute CTR, engagement, platform-attributed revenue, or another proxy for the pre-specified business outcome merely because it moved more clearly.

### 4. Separate observation from explanation

Write two statements:

- **Observed result**: what changed within the measured scope.
- **Mechanism interpretation**: why the change may have happened.

The mechanism remains an inference unless the design separately isolates it.

A significant outcome does not automatically prove the story used to explain it.

### 5. Decide the operational disposition

Choose one:

- `ship within tested scope`
- `reject within tested scope`
- `iterate and retest`
- `replicate before wider use`
- `collect more data`
- `invalidate and rerun`
- `stop because guardrail harm outweighs benefit`

The domain owner makes the business action decision; `$tracking-measurement` states what the evidence supports.

### 6. Create a scoped learning record

Use [`templates/experiment-learning.md`](../../../../templates/experiment-learning.md).

A useful learning statement follows this pattern:

`In [population/surface/context], changing [controlled variable] from [control] to [variant] produced [observed effect and uncertainty] on [primary business outcome] during [period], at [evidence level]. This supports/contradicts/does not resolve [hypothesis]. It does not establish [unproven mechanism or transfer claim].`

Avoid generic summaries such as "short copy wins" or "UGC converts better."

### 7. Assign transfer status

Use the narrowest justified status:

- **Local result** — one valid test in one defined context.
- **Replication candidate** — worth testing in a comparable context; not yet a reusable pattern.
- **Replicated scoped pattern** — independently repeated across at least two comparable tests with compatible results and no unresolved validity conflict.
- **Segment-specific pattern** — results differ materially by segment/context and the difference is supported by pre-specified or replicated evidence.
- **Contradicted / unstable** — comparable tests conflict; do not promote until the boundary or source of heterogeneity is understood.

Replication count alone is not enough; tests must be sufficiently independent and comparable.

### 8. Generate the next hypothesis

Use the result to reduce uncertainty rather than to maximize test count.

Good next hypotheses come from:

- unresolved mechanism
- a boundary condition exposed by the result
- guardrail tradeoff
- segment heterogeneity that was pre-specified or deserves a new test
- a failed implementation assumption
- a promising local result that needs replication before broader use

Do not manufacture a new hypothesis merely to keep an arbitrary experiment cadence.

## Experiment backlog

Maintain a backlog only for decision-relevant tests. Each item should include:

| Field | Purpose |
|---|---|
| Decision | What choice the experiment will inform |
| Evidence-backed problem | Why the test exists |
| Hypothesis | Falsifiable prediction |
| Expected mechanism | Why the change might affect the outcome |
| Scope | Population, surface, geography, channel, offer state |
| Existing evidence | Research, diagnostics, prior tests, external evidence |
| Required evidence level | Strength needed for the decision |
| Primary business outcome | What will call the test |
| Guardrails | What must not deteriorate |
| Feasibility / dependencies | Traffic, instrumentation, production, legal, capacity |
| Risk | Cost of being wrong or causing harm |
| Learning value | What uncertainty the test resolves even if it does not win |
| Status | proposed, approved, running, concluded, parked |

### Prioritization rule

Prioritize from actual decision impact, evidence strength, uncertainty, reversibility, feasibility, risk, and learning value.

A scoring model such as ICE or RICE may be used as a convenience only when its inputs are grounded and the resulting rank does not override a material risk, evidence gap, or strategic dependency. Do not invent numeric confidence to make a scoring table look precise.

## Knowledge promotion rules

- A single test never becomes a universal "best practice."
- A local result may be implemented locally when the decision rule supports it without being promoted into reusable doctrine.
- Post-hoc segment cuts are hypothesis generators unless independently validated; do not promote the most favorable slice.
- External case studies, competitor tests, platform benchmarks, and published examples are prior evidence, not local experimental proof.
- A repeated result with materially different contexts may suggest a broader pattern, but only after the relevant differences are examined rather than ignored.
- Conflicting evidence is retained. Do not delete a past loser after a later test wins.
- A result that depends on a specific offer, price, creative, audience, market, or platform state keeps that dependency in the learning record.
- Platform or interface changes can invalidate transfer assumptions; apply `PLATFORM-CURRENCY.md` when current mechanics matter.
- A causal evidence level is never upgraded because a result was replicated using the same flawed design.

## Using prior learning

Before launching a new experiment, search prior learning for:

- same decision
- same mechanism
- same segment or buying situation
- same surface/channel
- same offer and commercial conditions
- known guardrail failures
- contradictory results

Prior learning should change the new test's hypothesis, design, required evidence level, or priority. If it changes nothing, the archive is not functioning as an operating system.

## Output

Return:

- experiment validity class
- observed result and uncertainty
- causal/evidence level
- guardrail status
- observation versus mechanism interpretation
- operational disposition
- scoped learning statement
- transfer status
- contradictions or dependencies
- next hypothesis or explicit reason no follow-up is justified
- backlog change, if any
- exact status

## QA

Confirm the pre-test decision rule was preserved; validity was assessed before direction; the full conversion lag is included; a null is not mislabeled a loss; guardrail harm is visible; post-hoc slices are not promoted to proof; the mechanism is separated from the observed effect; scope is preserved; replication does not erase contradictions; external evidence is not mislabeled local proof; and no arbitrary experiment-velocity target overrides decision value.