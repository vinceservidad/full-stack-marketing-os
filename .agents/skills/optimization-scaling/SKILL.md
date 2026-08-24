---
name: optimization-scaling
description: Determine whether paid-media campaigns are ready to scale, choose a controlled scaling mode, model marginal economics, and define hold or rollback rules; not for automatic spend, bid, audience, or campaign changes.
---

# Optimization and Scaling

Primary knowledge type: methodology. Classify supporting models, strategies, tactics, techniques, templates, heuristics, and evidence with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md).

Scaling means increasing a verified primary business outcome while keeping named economics, quality, capacity, measurement, and risk guardrails acceptable. More spend, attributed revenue, conversions, or ROAS alone does not prove scaling.

## Required context

Collect the business model and outcome; account/channel scope; dates and comparison; source of truth; spend and conversion lag; revenue or lead-stage definitions; contribution inputs or qualified-outcome economics; campaign/entity evidence; demand opportunity; creative, funnel, inventory/sales, cash-flow, and operational capacity; current platform controls; and authorization scope.

## Method

1. Apply the [proof standard](references/proof-standard.md) and label current evidence.
2. Run the [readiness gates](references/readiness.md). Stop when a verified blocker makes scaling unsafe.
3. Model [economics and marginal efficiency](references/economics.md); expose missing inputs and sensitivity ranges.
4. Diagnose the binding constraint and select a scaling mode using [constraints and modes](references/constraints-and-modes.md).
5. Define one interpretable scaling hypothesis, exact entity/change, maximum exposure, decision window, conversion-lag allowance, business metric, guardrails, hold rule, and rollback condition.
6. Use [controlled steps](references/controlled-steps.md) to test, wait for maturity, evaluate marginal business outcome, and decide `increase`, `hold`, `continue evidence`, `apply`, `rollback`, `switch mode`, `de-scale`, or `inconclusive`.
7. Verify the result against the business source of truth and record scope, proof level, exceptions, and replication status.

Read only the relevant conditional reference: [portfolio allocation](references/portfolio-allocation.md), [creative capacity](references/creative-capacity.md), [Google Ads](references/google-scaling.md), [Meta Ads](references/meta-scaling.md), [business-model overlays](references/business-overlays.md), or [guardrails and recovery](references/guardrails-and-recovery.md). For current platform controls, apply `PLATFORM-CURRENCY.md` and confirm account visibility.

## Decision rules

- Never use a universal budget-increase percentage or cadence.
- Do not scale while measurement integrity, primary business outcome, or decision-critical economics are unknown.
- Evaluate blended and marginal performance separately; platform attribution is not incrementality or realized revenue.
- Increasing a budget is a tactic, not the scaling strategy. Address the binding constraint.
- Preserve valuable brand, query, product, audience, and market coverage unless evidence supports removal.
- Prefer one reversible, interpretable change; account for conversion lag and relevant demand cycles.
- Forecasts and platform recommendations are inputs, not guarantees or authorization.
- A tactic is “proven” only for its stated account, scope, period, and evidence level.
- All live budget, bid, target, audience, campaign, conversion, coverage, or status changes require explicit approval.

## Output

Return: scaling objective; primary knowledge type; proof level; readiness verdict and failed gates; source-of-truth outcome; economics and sensitivity; binding constraint; chosen scaling mode; protected coverage; exact proposed step; primary metric; guardrails; decision window/lag; hold/rollback rules; owner and approval; unknowns; exact status.

## QA

Verify formulas and cost scope, sample and lag maturity, account/platform availability, marginal versus blended evidence, downstream quality, operational capacity, maximum downside, one interpretable variable, source-of-truth verification, and authorization. Do not call scaling successful until the business result is verified.
