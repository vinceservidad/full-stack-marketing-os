---
name: activation
description: Define and improve the post-conversion path to first meaningful customer value using evidence-backed activation criteria, time-to-value, friction diagnosis, and controlled interventions; not for inventing an “aha moment,” treating onboarding completion as value by default, or taking over CRO, lifecycle messaging, product implementation, or retention economics.
---

# Activation

Activation owns the decision between acquisition/conversion and ongoing retention: what behavior or outcome credibly represents first meaningful value, how customers reach it, where they fail to reach it, and which interventions should be tested.

Activation is not automatically a stage every business needs. If the purchase or conversion itself substantially realizes the promised value and there is no meaningful post-conversion setup/use milestone, state that no separate activation layer is decision-relevant rather than forcing a SaaS funnel onto the business.

Classify activation artifacts with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). An activation heuristic or common “aha moment” pattern is a hypothesis input, not evidence that a specific event predicts value or retention for this business.

## Inputs

Before a decision-grade activation recommendation, confirm:

- business model, primary business outcome, and lifecycle-stage definitions
- promised outcome and product/service truth
- post-conversion customer journey from signup/purchase/lead acceptance to first meaningful value
- candidate value events and their instrumentation quality
- customer research, support/success evidence, usability evidence, and observed behavior where available
- segment/cohort definitions and expected time-to-value range
- downstream retention, repeat-use, renewal, refund, or qualified-revenue evidence when available
- operational/product/service constraints and authorization boundary

If the value event cannot be measured reliably, route instrumentation integrity to `$tracking-measurement` before treating activation rate as decision-ready.

## Method

1. **Confirm whether a distinct activation stage exists.** Identify the conversion boundary and ask whether meaningful customer value occurs after it. Do not manufacture a stage when the conversion itself is the useful outcome.
2. **Define first meaningful value.** Use [Activation definition and evidence](references/activation-definition-and-evidence.md). Separate customer value from business convenience and from easy-to-track onboarding events.
3. **Map the path to value.** Use [Path to value and friction](references/path-to-value-and-friction.md). Map required steps, dependencies, wait states, handoffs, customer effort, uncertainty, and failure points.
4. **Measure activation correctly.** State eligible denominator, activation event, window, segment, exclusions, instrumentation state, and time-to-value distribution. Do not report one blended rate across incompatible cohorts or journey variants.
5. **Diagnose the first binding barrier.** Distinguish product/service availability, setup complexity, comprehension, motivation, trust, missing data/integration, operational delay, poor-fit acquisition, technical defect, and measurement failure.
6. **Choose the smallest meaningful intervention.** Remove unnecessary friction, improve guidance, change sequencing, add assistance, clarify expectations, or redesign a handoff only where evidence supports the mechanism. Route owned-channel trigger/cadence design to `$lifecycle-marketing`, wording to `$copywriting`, and surface-level conversion UX to `$cro` where relevant.
7. **Define the test and guardrails.** Use [Activation experiments and handoffs](references/activation-experiments-and-handoffs.md). Primary outcome should reflect meaningful value or a validated activation proxy; guardrails may include refund/cancellation, support burden, quality, safety/compliance, retention, and downstream revenue.
8. **Record learning and exact state.** Proposed activation definitions remain hypotheses until evidence supports them. Implemented journey changes are not verified until the expected behavior and downstream guardrails are observed.

## Rules

- Do not call an event “activation” merely because it is common in the category, easy to instrument, or correlated in one unadjusted analysis.
- Do not invent an “aha moment.” If several candidate events exist, preserve uncertainty and design evidence collection or testing.
- Onboarding completion, tutorial completion, profile completion, email open/click, number of sessions, or feature clicks are supporting events unless evidence shows they represent or predict meaningful value in scope.
- Faster time-to-value is not universally better. Necessary qualification, safety, setup, education, compliance, or service work must not be removed just to shorten the clock.
- Do not optimize activation rate by shrinking the denominator, excluding hard customers after the fact, changing the activation window post hoc, or redefining the event after seeing results.
- Do not confuse activation with retention. Activation concerns first meaningful value; `$retention-economics` owns repeat/renewal/churn economics after cohorts mature.
- Do not confuse activation with lifecycle messaging. `$lifecycle-marketing` owns communication triggers/cadence; activation owns the journey decision those communications support.
- Do not diagnose poor activation as onboarding friction before checking poor-fit acquisition, product/service failure, technical defects, operational delay, and measurement integrity.
- Product or service implementation changes remain outside this skill's execution authority unless an appropriate implementation owner and approval exist.
- A journey change that lifts an activation proxy but worsens refunds, cancellations, quality, support burden, safety/compliance, or downstream value is not a clean win.

## Output

Activation decision: business model and conversion boundary; whether a distinct activation layer exists; first meaningful value definition and evidence strength; eligible denominator/window/segment; activation and time-to-value baseline; path-to-value map; diagnosed barrier; intervention hypothesis; required owner handoffs; primary outcome and guardrails; experiment/validation plan; implementation dependencies; approval needs; exact status.

## Library references

Owned root artifacts, read when their scope applies:

- [activation-plan.md](../../../templates/activation-plan.md) — canonical activation definition, journey, diagnosis, intervention, measurement, and learning record.

## Related owners

- `$marketing-intake`: lifecycle definitions, shared context, evidence state, authorization
- `$customer-research`: customer-reported friction, desired progress, qualitative evidence
- `$icp-jtbd`: segment, JTBD, poor-fit acquisition, buying situation
- `$offer-strategy`: promised outcome and expectation boundary
- `$cro`: pre-conversion surfaces and bounded page/form UX friction
- `$lifecycle-marketing`: owned-channel onboarding/activation triggers, segmentation, cadence
- `$copywriting`: onboarding/help/message wording
- `$tracking-measurement`: event integrity, causal test validity, experiment learning
- `$retention-economics`: repeat-use, renewal, churn, LTV, payback after activation
- `$marketing-operations`: recurring activation monitoring/decision loops when needed

## QA

Confirm a distinct activation stage actually exists, the value event is not chosen for tracking convenience, denominator/window/segment are fixed before reading the result, instrumentation is decision-ready, downstream guardrails are included, plausible alternative causes are checked, lifecycle/CRO/product boundaries are preserved, and no activation definition or journey change is described as proven before evidence supports it.
