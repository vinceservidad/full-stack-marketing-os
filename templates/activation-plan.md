# Activation Plan

Canonical activation definition, journey, diagnosis, intervention, measurement, and learning record.

Owner: `$activation`.

## Decision State

- Business / product:
- Date:
- Owner:
- Status: hypothesis | designed | approved | implemented | live | observed | verified | contradicted
- Primary business outcome:
- Source systems:
- Evidence state:

## Does a Distinct Activation Stage Exist?

- Conversion boundary:
- Does meaningful value occur after conversion? yes | no | uncertain
- Rationale:
- If no, why a separate activation layer is not decision-relevant:

## First Meaningful Value

- Candidate activation event/outcome:
- Customer progress represented:
- Why this is more than setup/admin:
- Evidence supporting the definition:
- Known confounders:
- Current definition status: hypothesis | provisional | supported | contradicted

## Metric Contract

- Eligible population:
- Journey entry event:
- Numerator:
- Denominator:
- Activation window:
- Segment/cohort:
- Exclusions fixed before analysis:
- Late-event handling:
- Identity/stitching rule:
- Instrumentation state:

## Baseline

- Activation rate:
- Median time to value:
- Other useful time-to-value bands/percentiles:
- Not-yet-activated/censored share:
- Observation period:
- Comparison period/cohort:
- Comparability caveats:

## Path to Value

| Step | Why required | Owner | Active effort | Wait time | Dependency | Failure/stall signal | Evidence | Removability |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## First Binding Barrier

- Observed stall:
- Affected segment:
- Evidence:
- Hypothesized mechanism:
- Competing explanations:
- Barrier type: comprehension | motivation/relevance | effort | technical defect | trust/anxiety | dependency | operational delay | qualification/fit | measurement failure | other
- Responsible owner:

## Intervention Hypothesis

- Change proposed:
- Why this is the smallest meaningful change:
- Expected mechanism:
- What must remain unchanged for interpretation:
- Implementation owner:
- Dependencies:
- Approval required:

## Measurement Plan

### Primary activation outcome
- Metric:
- Why it represents meaningful value:

### Supporting metrics
- 

### Guardrails
- Refund/cancellation:
- Support burden:
- Quality/error:
- Safety/compliance:
- Retention/repeat use:
- Revenue/contribution/lead quality:
- Other:

### Test design
- Control/comparison:
- Exposure/allocation:
- Sample/duration approach:
- Evaluation window:
- Instrumentation:
- Stop/rollback conditions:
- Causal-validity owner if needed: `$tracking-measurement`

## Handoffs

| Need | Owner | Artifact / action | Status |
|---|---|---|---|
| Event integrity / experiment validity | `$tracking-measurement` | | |
| Lifecycle triggers/cadence | `$lifecycle-marketing` | | |
| Wording | `$copywriting` | | |
| Bounded surface UX | `$cro` | | |
| Segment / fit | `$icp-jtbd` | | |
| Promise / expectation | `$offer-strategy` | | |
| Downstream retention economics | `$retention-economics` | | |
| Recurring operating loop | `$marketing-operations` | | |
| Product/service/operations implementation | external implementation owner | | |

## Result

- Observation:
- Activation outcome:
- Supporting metrics:
- Guardrails:
- Validity state:
- Decision: supports | contradicts | inconclusive | guardrail harm | invalid
- Scope of learning:
- Downstream effects mature? yes | no | partial
- Next action:

## Learning Handoff

- Experiment-learning record:
- Transfer status:
- Replication needed:
- Contradictions preserved:
- Marketing Context update needed? yes | no

## QA

- [ ] Distinct activation stage confirmed rather than assumed.
- [ ] Activation event represents customer value, not tracking convenience.
- [ ] Denominator, window, segment, and exclusions fixed before reading results.
- [ ] Instrumentation is decision-ready or explicitly provisional.
- [ ] First binding barrier is diagnosed with competing explanations.
- [ ] Necessary qualification/safety/compliance friction is preserved.
- [ ] Supporting metrics do not replace the value outcome.
- [ ] Downstream guardrails are included.
- [ ] Implementation ownership is explicit.
- [ ] No launched change is described as verified before the observation window supports it.
