---
name: cro
description: Audit and improve landing pages, product pages, forms, and checkout journeys leading to qualified conversion using evidence and testable hypotheses; not for post-conversion activation ownership or claiming causality from heuristics alone.
---

# Conversion Rate Optimization

Classify each deliverable with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Heuristic observations are hypothesis inputs, not causal findings or universal best practices.

## Required inputs

Use the strongest available evidence for the scoped pre-conversion journey:

- exact page, form, checkout, or funnel state being evaluated, including device/viewport when material
- primary business outcome, conversion boundary, and any qualified/supporting conversion definitions
- upstream traffic source, audience/intent, promise, ad/query/message, and destination where message scent matters
- funnel and page metrics with date range, denominator, source, and useful segments such as device, source, new/returning, geography, product, or landing page
- product, offer, price, shipping/fees, eligibility, claims, proof, and policy truth that materially affect the page decision
- available recordings, surveys, usability evidence, support/sales objections, experiment results, technical errors, accessibility issues, and page-speed evidence
- commercial/downstream guardrails such as contribution, AOV, refund/return rate, lead quality, support burden, accessibility, or compliance
- implementation and test authority if the request includes a live change rather than analysis or a draft

Mark missing inputs explicitly. Do not invent user behavior, customer objections, page defects, or causal explanations to complete an audit.

## Method

1. Define the primary business outcome and any qualified or supporting conversion. Reserve “Primary conversion action” for the Google Ads setting.
2. Map message scent from ad or query through page and conversion boundary.
3. Inspect motivation, relevance, clarity, trust, and friction/anxiety before conversion.
4. Segment by source, device, intent, landing page, and new/returning user when data permits.
5. Identify the first meaningful pre-conversion leak and distinguish technical failure from persuasion weakness.
6. Rank hypotheses by evidence strength, expected impact, effort, risk, and learning value.
7. When the problem begins after signup, purchase, lead acceptance, or another defined conversion and concerns reaching first meaningful customer value, route the journey decision to `$activation`. CRO may support a bounded page/form/surface intervention without owning the activation definition.

## Rules

- Fix verified defects before testing persuasion variants.
- Do not remove necessary qualification, legal, accessibility, pricing, or expectation-setting information to inflate raw conversion rate.
- Optimize for purchases, qualified leads, or contribution—not button clicks alone.
- Protect refund rate, lead quality, AOV, accessibility, and support burden.
- Do not default to redesign when a focused change can test the mechanism.
- Message scent means continuity between the upstream promise and the destination's immediate message. Keep funnel/journey stage, awareness level, audience temperature, activation state, and lifecycle stage distinct.
- Do not relabel post-conversion onboarding or first-value work as CRO merely because the intervention appears on a web/app surface. `$activation` owns the first-value decision.

## Output

Audit finding: location; observation; evidence; affected segment; hypothesized mechanism; business impact; confidence; recommendation; validation method.

Experiment: problem; hypothesis; control; variant; primary metric; guardrails; audience; duration/sample approach; stop conditions; instrumentation; decision rule.

## Library references

Owned root artifacts, read when their scope applies:

- [shopify-cro.md](../../../frameworks/shopify-cro.md) — Shopify-specific conversion framework.
- [ecommerce.md](../../../playbooks/ecommerce.md) — ecommerce conversion playbook.
- [ecommerce-growth.md](../../../playbooks/ecommerce-growth.md) — ecommerce growth playbook.
- [landing-page-review.md](../../../templates/landing-page-review.md) — landing page review format.
- [cro-improvement.md](../../../workflows/cro-improvement.md) — improvement workflow sequence.

## QA

Verify the actual page/state and device, keep the conversion boundary explicit, route post-conversion first-value decisions to `$activation`, avoid causal language without a test, include downstream guardrails, flag accessibility/compliance risks, and distinguish recommendations from implementation.
