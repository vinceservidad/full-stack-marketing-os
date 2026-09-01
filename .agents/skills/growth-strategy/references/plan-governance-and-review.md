# Plan Governance and Review

Use this reference to turn a strategic direction into an adaptive plan without confusing the plan with implementation or turning a calendar into evidence.

## Planning horizon

Choose a horizon that matches the business decision, conversion/retention lag, seasonality, sales cycle, cash runway, operational capacity, and learning speed.

Examples such as 30 days, 90 days, a quarter, or a year are planning conveniences, not universal standards. A short-cycle ecommerce test and an enterprise sales strategy should not be forced into the same review rhythm.

Record:

- strategy start date
- decision horizon
- expected signal window for each major hypothesis
- business-outcome maturity window
- known seasonal/event constraints
- conditions that require an earlier review

## Plan layers

Separate:

1. **Objective** — the business result and guardrails.
2. **Strategic bets** — the chosen mechanisms and priorities.
3. **Validation work** — evidence needed before larger commitment.
4. **Specialist plans** — channel, offer, pricing, CRO, activation, retention, measurement, or operations work owned by specialists.
5. **Execution state** — what is actually approved, configured, live, or verified.
6. **Learning** — what the observed result changes about the strategy.

Never collapse these into a task list and call it strategy.

## Decision gates

For each strategic bet define:

- hypothesis
- evidence state at entry
- specialist owner
- dependencies
- primary business metric or validated leading indicator
- guardrails
- minimum decision window or maturity condition
- what evidence supports `continue`
- what evidence supports `hold`
- what evidence supports `revise`
- what evidence supports `kill`
- what condition routes to `$optimization-scaling`

Do not write decision rules after seeing the result when they could reasonably have been defined before the test.

## Review triggers

A strategy review can be triggered by:

- scheduled decision point
- material business-outcome deviation
- verified constraint removal
- newly verified blocker
- economics or capacity change
- market/competitor change that materially alters the decision
- experiment result that supports or contradicts a strategic assumption
- major offer/pricing/product/service change
- measurement-definition change that breaks comparability

A review trigger does not itself prove the strategy should change.

## Change control

When revising the strategy:

- preserve the previous decision and evidence state
- state what new evidence changed the view
- distinguish constraint change from tactic failure
- record which priorities were added, removed, deferred, or resequenced
- update Marketing Context only after the specialist/strategy artifact has a clear state
- do not rewrite prior forecasts or hypotheses as though the new evidence had been known earlier

## Strategy status

Use exact states:

- `draft`
- `decision-ready`
- `approved`
- `in execution`
- `under review`
- `superseded`

A strategy is not `verified`. Individual hypotheses, implementations, and business outcomes can be verified; strategy remains an adaptive decision system.

## Operating handoff

Once approved, recurring review or cross-skill coordination can be expressed as a `$marketing-operations` loop. Writing the loop does not make it active; runtime state must still be configured and verified.

Stakeholder progress summaries route to `$marketing-reporting`. The report should preserve the strategy's evidence and exact-status language rather than converting an in-progress test into a success claim.

## Minimum output

Return: horizon; strategic bets; validation work; specialist dependencies; decision gates; review triggers; implementation state; learning/change log; next review condition; exact status.