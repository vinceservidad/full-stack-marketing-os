# Decision Record

**Status:** Synthetic worked example

This is an auditable professional decision record, not hidden chain-of-thought.

## Routing

1. `$marketing-intake` confirms objective, economics, evidence state, attribution boundaries, inventory, and authorization.
2. `$growth-strategy` decides the current business-level constraint set and opportunity portfolio.
3. `$performance-diagnostics` tests competing explanations for the revenue/spend divergence.
4. `$cro`, `$google-ads`, `$meta-ads`, and `$creative-strategy` own their specialist diagnoses.
5. `$tracking-measurement` defines how proposed changes will be evaluated.
6. `$optimization-scaling` is deferred until the system is economically and operationally ready.

## Decision record

| Evidence | State | Diagnosis / interpretation | Decision implication | Validation needed |
|---|---|---|---|---|
| Revenue flat while spend +22% | Observed + calculated | The current growth system is producing weaker marginal returns | Do not solve the plateau with another broad spend increase | Channel-level marginal analysis and contribution guardrails |
| Checkout completion 52% → 43% | Observed | A meaningful conversion-stage deterioration exists | Checkout diagnosis becomes a high-priority workstream | Device, step, payment, shipping and error breakdown |
| Mobile checkout 49% → 37% | Observed | The deterioration is concentrated on mobile | `$cro` should investigate mobile checkout before a full-site redesign | Reproduce checkout, inspect analytics/session evidence if available |
| Shipping-confusion tickets increased | Observed | Delivery expectation may contribute to friction | Test clearer delivery/shipping information as a hypothesis, not a proven cause | Checkout/user research and controlled measurement |
| Google non-brand spend +28%, revenue +7% | Observed | Marginal paid-search efficiency weakened | `$google-ads` should identify products/queries/campaigns consuming marginal spend | Search terms, product economics, auction/bid context |
| Meta spend +19%, new-customer revenue +2% | Observed | Extra delivery produced limited incremental commercial value | Stop automatic spend expansion; inspect audience/creative/offer mix | Marginal performance by concept/audience and contribution |
| 68% of Meta spend on three concepts | Observed | Creative concentration exists | `$creative-strategy` should broaden evidence-compatible concepts | Do not label fatigue without time/frequency/performance evidence |
| Repeat purchase stable | Observed | No current evidence of a sudden retention collapse | Retention remains important but is not the first response to this plateau | Continue monitoring cohorts |
| Hero SKU inventory = 5 weeks | Observed | Supply capacity is a scaling constraint | Avoid aggressive scale that could create stockout/service damage | Replenishment timing and scenario plan |
| Competitor discount | Competitor observation | Competitor is promoting price | No pricing response is justified from this fact alone | `$pricing-monetization` only if internal price/value evidence suggests a pricing decision |

## Constraint state

The evidence supports a **co-limiting constraint set**, not one magical bottleneck:

1. **Mobile checkout deterioration** — likely suppressing conversion after traffic is acquired.
2. **Weakening marginal paid-media efficiency** — additional spend is not converting into proportional new-customer value.
3. **Near-term inventory capacity** — limits how aggressively a recovered system can scale.

Creative concentration is a relevant opportunity/uncertainty, but creative fatigue is not yet established as a causal constraint.

## Prioritized opportunity portfolio

### Priority 1 — Diagnose and repair mobile checkout loss

Owner: `$cro`

Hypotheses to test:
- delivery-time or shipping-cost uncertainty is introduced too late
- mobile payment/checkout usability degraded
- a technical or rendering issue affects one step/device cohort
- traffic mix changed and is exposing a weaker mobile segment

### Priority 2 — Stop low-quality marginal paid expansion

Owners: `$google-ads`, `$meta-ads`

Actions are diagnostic first:
- identify where the incremental spend went
- compare marginal contribution, not only average ROAS
- protect strong existing demand/coverage while removing clearly weak marginal allocation

### Priority 3 — Expand creative learning without claiming fatigue

Owner: `$creative-strategy`

Use customer/product evidence to create new angle/mechanic cells. Keep the offer stable where practical so the test teaches creative rather than changing every variable at once.

### Priority 4 — Prepare inventory-aware scaling conditions

Owners: `$growth-strategy` + `$optimization-scaling` once readiness exists

Define the inventory threshold, contribution threshold, checkout recovery condition, and channel marginal-efficiency condition required before further expansion.

## Explicit non-priorities

Do **not**:

- increase total paid budget just because top-line revenue is flat
- rebuild the entire Shopify theme before isolating checkout friction
- call the top Meta concepts fatigued from spend concentration alone
- copy the competitor's discount
- launch a new acquisition channel to escape unresolved problems in the current system
- claim tracking is broken merely because platform and blended numbers differ
- scale before inventory and marginal economics are ready

## Measurement plan

### Checkout workstream

Hypothesis: removing the identified mobile checkout friction increases completed orders from eligible mobile checkout users without worsening refunds, support burden, contribution, or payment failure.

Primary outcome: completed purchase rate from eligible mobile checkout sessions.

Guardrails: contribution/order, refund/cancel rate, support contacts, payment failure, page/checkout errors.

### Paid-media workstream

Hypothesis: reallocating away from low-quality marginal spend improves contribution while preserving qualified demand coverage.

Primary outcome: incremental/marginal contribution or the closest valid commercial proxy available.

Guardrails: new-customer volume, brand demand capture, coverage, inventory, learning disruption.

### Creative workstream

Hypothesis: strategically distinct evidence-compatible concepts improve qualified new-customer acquisition relative to current creative cells.

Primary outcome: commercial acquisition result appropriate to the account.

Guardrails: conversion quality, spend distribution, claim compliance, destination consistency.

## Implementation status

All actions in this worked example are **draft recommendations**. No platform, store, price, or campaign change is live.
