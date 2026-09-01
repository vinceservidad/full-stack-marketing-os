# Growth Strategy Evaluation Review

Status: **Pass**

Scope reviewed: `$growth-strategy`, its three references, upgraded `templates/strategy-template.md`, router/registry boundaries, Marketing Context integration, Optimization & Scaling boundary, Marketing Operations boundary, and the 60 behavioral cases in `growth-strategy-cases.md`.

## Decision review

Pass.

The skill owns a previously ungoverned orchestration decision: how a verified business objective becomes a cross-functional growth-system map, prioritized opportunity portfolio, sequence, explicit non-priorities, and review/rebalancing logic.

It does not take over the substantive decisions of channel skills, customer research, ICP/JTBD, offer, pricing, CRO, activation, retention strategy/economics, measurement, scaling, operations, or reporting.

The methodology allows multiple meaningful constraints, distinguishes verified/likely constraint from symptom/dependency/unknown, and permits “constraint not yet identified” when evidence is insufficient.

## Evidence review

Pass.

The design requires a named primary business outcome, baseline, horizon, economics/guardrails, and specialist evidence. Strategic priorities inherit the evidence state of the source work; approval of a plan does not upgrade a mechanism to proven.

External benchmarks, competitor activity, platform ROAS, category conventions, and generic planning frameworks remain context or heuristics rather than proof.

False precision is blocked: arbitrary scores, fixed experiment percentages, channel quotas, and default portfolio splits are not treated as evidence-backed allocation rules.

## Portfolio and sequencing review

Pass.

The plan requires choices and explicit non-priorities. Optional `protect`, `exploit`, `explore`, and `build-capability` labels are planning roles only; no fixed allocation is attached to them.

Sequencing is dependency- and learning-led rather than calendar-led. A user-requested 90-day horizon is supported, but 30/60/90 and quarterly structures are not universal defaults. Parallel work is allowed when capacity and interpretability remain acceptable.

## Scaling and commercial review

Pass.

`$growth-strategy` may decide that paid-media expansion deserves strategic priority, but `$optimization-scaling` still owns readiness, proof, marginal economics, controlled expansion, and de-scaling. A growth plan cannot bypass scaling gates or live-change authorization.

The strategy explicitly considers cash flow, margin, inventory, service/sales capacity, fulfillment, compliance, product/service defects, and opportunity cost instead of treating marketing spend as an isolated growth lever.

## Authorization and state review

Pass.

The strategy artifact distinguishes draft, proposed, approved, in progress, implemented, observing, validated, contradicted, paused, and retired states. Plan approval does not automatically authorize spend, pricing, offer, tracking, campaign, website, customer-state, or operational mutations.

Decision history is preserved when assumptions change; the plan is revised rather than rewritten with hindsight.

## Ownership review

Pass.

- `$marketing-router`: routes the request; does not own the strategy
- `$growth-strategy`: cross-functional growth direction, portfolio, sequencing, non-priorities, review/rebalancing
- `$performance-diagnostics`: unexplained metric/performance changes
- specialist/channel skills: substantive domain decisions
- `$tracking-measurement`: causal validity and experiment learning
- `$optimization-scaling`: paid-media scaling readiness/method
- `$marketing-operations`: recurring stateful execution/decision loops
- `$marketing-reporting`: stakeholder communication
- `$marketing-intake`: evidence state, shared context, definitions, authorization

The old `strategy-template.md` ownership moves from `$marketing-router` to `$growth-strategy`, eliminating the prior generic-planning ambiguity.

## Regression coverage review

Pass.

The 60 cases cover undefined objectives/baselines, default 90-day plans, fixed 70/20/10 and experiment-budget percentages, channel quotas, competitor copying, ROAS-only allocation, verified defects, measurement blockers, false bottlenecks, seasonality, activation/retention relevance, offer/pricing dependencies, inventory/sales/fulfillment/compliance capacity, backlog masquerading as strategy, false-precision scoring, ownerless initiatives, channel/scaling ownership, plan approval versus live authorization, immature results, contradictory learning, stale plans, pricing/offer changes, lag and cohort maturity, long sales cycles, parallel-test contamination, external spend benchmarks, strategic-versus-scaling routing, diagnostics/reporting/operations boundaries, non-marketing constraints, and insufficient evidence.

## Final result

**Pass.** Growth Strategy is a decision-changing orchestration layer that strengthens the existing Marketing OS without becoming a duplicate all-purpose marketing skill or importing fixed external planning formulas.