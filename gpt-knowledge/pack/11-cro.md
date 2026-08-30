<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Conversion Rate Optimization

## Skill: $cro

**Use when:** Audit and improve landing pages, product pages, forms, and checkout journeys for qualified conversion using evidence and testable hypotheses; not for claiming causality from heuristics alone.

Classify each deliverable with `KNOWLEDGE-TAXONOMY.md`. Heuristic observations are hypothesis inputs, not causal findings or universal best practices.

Prefer analytics by segment, recordings, surveys, usability tests, support/sales objections, experiment results, page speed, and funnel errors. Heuristic observations generate hypotheses; they do not prove causes.

### Method

1. Define the primary business outcome and any qualified or supporting conversion. Reserve “Primary conversion action” for the Google Ads setting.
2. Map message scent from ad or query through page and next step.
3. Inspect motivation, relevance, clarity, trust, and friction/anxiety.
4. Segment by source, device, intent, landing page, and new/returning user when data permits.
5. Identify the first meaningful leak and distinguish technical failure from persuasion weakness.
6. Rank hypotheses by evidence strength, expected impact, effort, risk, and learning value.

### Rules

- Fix verified defects before testing persuasion variants.
- Do not remove necessary qualification, legal, accessibility, pricing, or expectation-setting information to inflate raw conversion rate.
- Optimize for purchases, qualified leads, or contribution—not button clicks alone.
- Protect refund rate, lead quality, AOV, accessibility, and support burden.
- Do not default to redesign when a focused change can test the mechanism.
- Message scent means continuity between the upstream promise and the destination's immediate message. Keep funnel/journey stage, awareness level, audience temperature, and lifecycle stage distinct.

### Output

Audit finding: location; observation; evidence; affected segment; hypothesized mechanism; business impact; confidence; recommendation; validation method.

Experiment: problem; hypothesis; control; variant; primary metric; guardrails; audience; duration/sample approach; stop conditions; instrumentation; decision rule.


### Library references

Owned root artifacts, read when their scope applies:

- shopify-cro.md — Shopify-specific conversion framework.
- ecommerce.md — ecommerce conversion playbook.
- ecommerce-growth.md — ecommerce growth playbook.
- landing-page-review.md — landing page review format.
- cro-improvement.md — improvement workflow sequence.

### QA

Verify the actual page/state and device, avoid causal language without a test, include downstream guardrails, flag accessibility/compliance risks, and distinguish recommendations from implementation.
