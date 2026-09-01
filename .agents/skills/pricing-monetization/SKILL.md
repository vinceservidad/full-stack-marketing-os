---
name: pricing-monetization
description: Diagnose and design base price, value metric, package/tier architecture, payment model, and monetization changes using customer, competitive, cost, demand, and realized-economics evidence; not for inventing willingness-to-pay, copying competitor prices, or treating conversion rate as the pricing objective.
---

# Pricing and Monetization

Pricing and Monetization owns the commercial exchange structure: what is charged, for what unit of value, in which package, on what payment model, and under which economic constraints. It does not own the broader offer promise, page copy, checkout UX, or lifetime-value calculation.

Classify pricing outputs with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A pricing framework or benchmark is a hypothesis input, not evidence that a specific price is optimal.

## Context

Before a decision-grade recommendation, confirm:

- product/service truth and delivery model
- priority segment, buying situation, JTBD, alternatives, and selection criteria
- current base price, fees, discounts, payment terms, packages/tiers, and eligibility
- current offer architecture from `$offer-strategy`
- realized unit economics, margin/cost-to-serve, refunds/cancellations, capacity, and tax/fee treatment
- retention/payback evidence where repeat behavior materially affects the decision
- customer research that actually bears on price sensitivity or value perception
- relevant competitor/alternative pricing with date and source, when available
- legal, contractual, fairness, brand, and authorization constraints

If inputs are weak, return a pricing hypothesis and evidence plan rather than a false point estimate.

## Method

1. **State the pricing decision.** Separate base price, value metric, packaging/tier, payment model, discount architecture, and price-change decision. Do not solve several at once by default.
2. **Define the economic floor and operating constraints.** Use [Pricing architecture](references/pricing-architecture.md) to identify variable cost, cost-to-serve, contribution target, capacity, refund/cancellation risk, and any channel or payment costs that materially change economics.
3. **Define the customer value unit.** Decide whether the business charges per product, seat, usage, outcome proxy, subscription period, project, bundle, or another unit. A value metric must align reasonably with customer value and business cost without creating perverse incentives.
4. **Assess evidence on price sensitivity.** Use [Willingness-to-pay evidence](references/willingness-to-pay-evidence.md). Separate observed purchases and behavioral tests from stated survey answers, sales anecdotes, competitor prices, and model inference.
5. **Design package/tier architecture only when differentiation is real.** Each tier or package needs a distinct customer/job, entitlement, usage boundary, service level, or economic reason. Do not manufacture three tiers because a framework says three is standard.
6. **Model scenarios.** Compare price/package options on realized or explicitly modeled revenue, contribution, conversion/close rate, mix shift, retention/refund risk, capacity, and customer impact. Do not optimize one metric in isolation.
7. **Choose the smallest decision-valid test.** Use [Price-change testing and rollout](references/price-change-testing-and-rollout.md). Specify population, eligibility, treatment, primary business outcome, guardrails, duration/lag, grandfathering or migration rules, and rollback/stop conditions.
8. **Record exact commercial state.** Proposed, approved, configured, live, observed, and verified are different states. A price change is not verified until the actual charged amount and resulting economics are observed in the source of truth.

## Rules

- Customer research may reveal price language, objections, tradeoffs, and relative value. It does not automatically produce a numeric willingness-to-pay estimate.
- Competitor price is context, not the answer. Never infer optimal price, market share, demand, margin, or willingness-to-pay from a competitor price alone.
- Do not use arbitrary psychological endings, price buckets, “industry standard” markups, or universal good-better-best rules as proof.
- Do not treat a higher conversion rate as a pricing win if contribution, refund rate, retention, lead quality, capacity, or customer mix worsens materially.
- Do not treat a higher average order value or ARPU as a win without checking volume, contribution, retention, and mix effects.
- Do not hide a price increase through mandatory fees, confusing unit changes, shrinkage, or materially harder cancellation. Make the commercial exchange legible.
- Do not fabricate scarcity, anchor prices, crossed-out prices, savings percentages, reference prices, or “most popular” labels.
- Discounts are part of pricing architecture when they change realized price. Do not evaluate list price while ignoring discount frequency and mix.
- Grandfathering, migration, renewal, and existing-customer treatment must be explicit when a price change affects current customers.
- A modeled price recommendation is not realized economics. Preserve assumption ranges and sensitivity.
- Any live price, billing, checkout, contract, or catalog change remains approval-bound.

## Output

Pricing decision: decision type; audience/segment; current commercial structure; evidence base and strength; economic floor/constraints; value metric; package/tier logic; candidate price/payment scenarios; modeled business impact with assumptions; customer and retention risks; competitor context if relevant; test/rollout plan; grandfathering/migration rules; measurement and guardrails; approval needs; exact status.

## Related owners

- `$marketing-intake`: shared context, source/evidence state, cost definitions, authorization
- `$customer-research`: price objections, tradeoffs, value language, stated research evidence
- `$icp-jtbd`: segment, JTBD, alternatives, competitive context
- `$offer-strategy`: promised outcome, bundle, risk reversal, offer architecture
- `$cro`: checkout/page friction and presentation of approved pricing
- `$copywriting`: wording that communicates approved pricing
- `$tracking-measurement`: experiment validity and causal evidence
- `$retention-economics`: realized retention, lifetime value, renewal, and payback effects
- `$optimization-scaling`: downstream scaling decisions using validated economics

## QA

Confirm the pricing decision type is explicit, observed behavior is separated from stated research and inference, competitor price is not treated as optimal price, cost/profit level is named, package differences are real, scenarios include volume and contribution effects, current-customer treatment is explicit, no fake anchor/savings/urgency is introduced, the test is interpretable, and no proposed/configured price is described as live or verified prematurely.
