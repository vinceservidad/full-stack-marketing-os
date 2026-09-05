# Refused Budget Increase — Worked Example

**Status:** Synthetic worked example. Fictional business and data; no real account was inspected or changed.

This walkthrough shows how a request for a fixed budget increase can lead to a useful hold recommendation and evidence plan. It applies the existing scaling gates without treating a healthy reported ROAS as proof of readiness.

Governing sources: [`$optimization-scaling`](../../.agents/skills/optimization-scaling/SKILL.md), its [readiness gates](../../.agents/skills/optimization-scaling/references/readiness.md), [economics contract](../../.agents/skills/optimization-scaling/references/economics.md), and [proof standard](../../.agents/skills/optimization-scaling/references/proof-standard.md), plus [`GLOSSARY.md`](../../GLOSSARY.md) and the [worked-example standard](../WORKED-EXAMPLE-STANDARD.md). This example adds no canonical decision rule.

## Starting request

> "Meta reports 4.2 ROAS for the last 14 days, the best we've had. Should we raise budgets 20% across the account today, then do it again next week if ROAS holds? I've heard 20% is a safe increase that doesn't reset learning. Give me a recommendation only; do not change the account."

## Business and scope

- Fictional brand: **Harrow Lane**, a United Kingdom ecommerce homeware store.
- Meta and Google Ads both contribute paid traffic to one Shopify storefront.
- Snapshot date: 1 September 2026. Recent period: 18–31 August 2026; prior period: 4–17 August 2026.
- Currency: GBP. All supplied exports and stakeholder statements below are synthetic teaching inputs.
- Primary business outcome: increase contribution profit after media, with the revenue and cost scope defined in [input-evidence.md](input-evidence.md). Current inputs are insufficient to establish this outcome.

## Knowledge and authorization metadata

```yaml
artifact_type: methodology
decision: determine whether the supplied evidence supports a Meta budget increase
scope: synthetic UK ecommerce example; Meta scaling with cross-channel economics
owner: optimization-scaling
inputs: synthetic platform summaries, Shopify net revenue, promotion and creative notes
evidence_status: calculated
confidence: high for the hold recommendation; not-assessed for actual scalability
freshness: stable
dependencies: verified costs, reconciled measurement, comparable mature evidence, capacity, approval
authorization: read-only
rollback_or_stop: hold budget changes while decision-critical gates remain unresolved
```

The metadata describes the teaching artifact, not the proof level of a real account. The decision record separately labels observations, assumptions, inferences, and unknowns. The scaling claim remains **S0, unverified**; no live account evidence or causal test is supplied.

## Owner chain

```text
$marketing-intake          records scope, definitions, evidence, and authorization
→ $optimization-scaling    owns readiness, the hold verdict, and the final response
→ $tracking-measurement    owns reconciliation, collection validation, and causal grading
→ $meta-ads                owns account delivery and opportunity diagnosis
→ $creative-strategy       owns creative diagnosis if the account evidence supports it
```

The business owner supplies finance and inventory evidence. These are proposed handoffs, not claims that specialist analysis has already run.

## Learning objectives

- Distinguish a platform's period-average attributed ROAS from business economics.
- Do not call a raw revenue/spend difference marginal efficiency when the periods are not comparable, or incremental revenue without a credible counterfactual.
- Reconcile attribution differences before classifying them as collection defects.
- Keep a promotion's effect and creative fatigue as hypotheses until tested.
- Reject a universal budget percentage and preserve existing coverage while readiness is unknown.
- Produce a bounded evidence plan; a request to proceed does not supply missing measurement, economics, or capacity evidence.

## Walkthrough

1. [Input evidence and reproducible arithmetic](input-evidence.md)
2. [Decision record, gates, and specialist handoffs](decision-trace.md)
3. [Final recommendation and implementation status](final-output.md)
