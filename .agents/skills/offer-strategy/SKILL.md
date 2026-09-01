---
name: offer-strategy
description: Diagnose and design the commercial offer itself — promised outcome, core deliverable, value architecture, bundle, risk reversal, urgency/scarcity, and offer-level friction — using verified product, customer, proof, and economics evidence; not for writing the page, setting base pricing strategy, or claiming conversion lift from heuristics.
---

# Offer Strategy

An offer is the commercial proposition the buyer is being asked to accept. It is not the landing page, ad, headline, pricing model, or creative execution that presents it.

Classify each offer artifact with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Offer patterns and direct-response frameworks are hypothesis inputs, not proof that a specific audience will buy.

## Context

Use the relevant sections of [`templates/marketing-context.md`](../../../templates/marketing-context.md) when available. Before a decision-grade recommendation, confirm:

- product truth and claim boundaries
- priority segment, buying situation, JTBD, and desired outcome
- customer objections, anxieties, alternatives, and selection criteria
- current offer and supplied price/payment terms
- available proof and its allowed use
- margin, refund, fulfillment, inventory, service, or delivery constraints
- legal, compliance, brand, and authorization boundaries

If these are materially unclear, route the missing evidence to `$marketing-intake`, `$customer-research`, or `$icp-jtbd` rather than inventing it.

## Method

1. **State the current offer plainly.** What must the buyer give, what do they receive, what outcome is promised, what conditions apply, and what happens if they do nothing?
2. **Identify the offer job.** Tie the proposition to the customer's desired progress and buying situation rather than to product features alone.
3. **Audit value architecture.** Use [Offer architecture](references/offer-architecture.md) to inspect outcome relevance, confidence/proof, time-to-value, buyer effort, friction, completeness, and economic feasibility.
4. **Diagnose the binding offer constraint.** Identify the weakest decision-relevant component instead of rebuilding everything by default. See [Offer diagnosis](references/offer-diagnosis.md).
5. **Design the smallest meaningful change.** Improve the core deliverable, bundle, service layer, risk reversal, eligibility, timing, convenience, or other offer component while preserving product truth and margin constraints.
6. **Audit risk reversal and urgency.** Use [Risk reversal and urgency](references/risk-reversal-and-urgency.md). A guarantee must transfer a real risk the business can bear. Urgency or scarcity must be true, specific, and operationally enforceable.
7. **Specify proof requirements.** Match each promise to evidence strong enough to support it. Customer-reported experience is not automatically causal business proof.
8. **Define the test.** State the offer hypothesis, controlled change, primary business outcome, guardrails, decision window, and what a win, loss, or inconclusive result would teach. Route causal experiment design to `$tracking-measurement` when needed.

## Rules

- Do not confuse a weak offer with weak copy. `$copywriting` expresses an approved offer; `$cro` diagnoses conversion friction in the page or journey.
- Do not manufacture value by inflating fictitious bonus values, unverifiable comparisons, or arbitrary “worth” numbers.
- Do not invent scarcity, countdowns, deadlines, capacity limits, waitlists, stock pressure, or expiring bonuses.
- Do not invent guarantees, refund terms, service commitments, or make-good remedies the business has not approved and cannot operationally honor.
- Do not use a discount as the default response to weak conversion. Diagnose whether the problem is relevance, confidence, effort, risk, timing, product-market fit, price, or page execution first.
- Do not promise a conversion lift, revenue lift, or expected percentage improvement from an offer heuristic.
- Do not turn a customer aspiration into a product claim unless product truth and proof support the bridge.
- Do not treat a bundle as stronger merely because it contains more items. Every component needs a job in the buying decision or delivery outcome.
- Do not hide meaningful conditions in fine print to make the headline offer look stronger.
- Do not set a base price, value metric, pricing tier architecture, willingness-to-pay result, or monetization strategy. Those pricing decisions remain a separate capability until governed explicitly. Treat supplied price/payment terms as inputs and label any unowned pricing recommendation as such.
- A proposed offer is not approved, live, or proven. Preserve draft, approved, published/live, and verified states.

## Output

Offer decision: business objective; audience and buying situation; current offer; diagnosed constraint; evidence; proposed offer architecture; promise and proof boundary; core deliverable; bundle/service components; risk reversal; real urgency/scarcity; supplied price/payment terms; economics/capacity check; objections addressed; hypothesis; measurement and guardrails; approval needs; exact status.

## Related owners

- `$marketing-intake`: shared context, evidence state, economics definitions, authorization
- `$customer-research`: objections, VOC, reported outcomes, review evidence
- `$icp-jtbd`: segment, buying situation, JTBD, switching forces
- `$copywriting`: wording that presents the offer
- `$cro`: landing/product-page and funnel friction
- `$creative-strategy`: paid creative angle, concept, proof treatment, and CTA
- `$tracking-measurement`: experiment validity and causal evidence
- `$retention-economics`: cohort value, payback, retention economics
- `$optimization-scaling`: whether an offer-supported acquisition system is ready to scale

## QA

Confirm the offer is distinct from its copy and page, the desired outcome is evidence-grounded, every promise fits product truth, proof strength matches claim strength, urgency/scarcity is real, risk reversal is operationally supportable, margin/capacity consequences are visible, no pricing capability is silently claimed, the proposed change is testable, and no draft is described as approved or proven.
