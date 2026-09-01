---
name: growth-strategy
description: Build an evidence-led business-level marketing growth strategy by defining the commercial objective, identifying the current limiting constraint or constraint set, prioritizing growth opportunities, sequencing specialist work, and governing a learning roadmap; not for generic channel checklists, arbitrary budget splits, or taking over specialist execution decisions.
---

# Growth Strategy

Growth Strategy owns the integrated marketing direction: where the business should focus, why that opportunity deserves priority, which specialist decisions are required, what should deliberately not be prioritized, and how the plan will learn and adapt.

It does not replace `$icp-jtbd`, `$offer-strategy`, `$pricing-monetization`, channel skills, `$cro`, `$activation`, `$retention-strategy`, `$tracking-measurement`, or `$optimization-scaling`. It composes their decision-grade outputs into one business-level strategy.

Primary knowledge type: strategy. Use [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md) to label supporting frameworks, methodologies, hypotheses, tactics, templates, and evidence correctly.

## Inputs

Before a decision-grade growth strategy, confirm:

- business model, primary business outcome, planning horizon, and strategic constraints
- source-of-truth baseline for revenue or qualified pipeline and the named profit/economic level where available
- any target or desired direction explicitly supplied by the business; do not invent a growth target to complete the plan
- market, segment, JTBD, buyer/user roles, alternatives, and current positioning evidence
- product/service truth, offer state, pricing/monetization state, and material capacity constraints
- acquisition, conversion, activation, retention, and lifecycle evidence relevant to the business model
- current specialist findings, experiment learning, known defects, and unresolved contradictions
- implementation capacity, budget/cash constraints where relevant, and authorization boundary

Use the current `.agents/marketing-context.md` when available, but do not let it upgrade stale or weak underlying evidence.

## Method

1. **Define the growth objective.** State the primary business outcome, baseline, horizon, economic boundary, quality guardrails, and what would count as meaningful progress. Preserve a supplied target as asserted until supported; do not manufacture one.
2. **Establish the evidence baseline.** Summarize only decision-relevant specialist evidence and distinguish observed facts, calculations, inference, assumptions, unknowns, and contradictions.
3. **Identify the current limiting condition(s).** Use [Growth constraint and opportunity diagnosis](references/growth-constraint-and-opportunity.md). Separate symptoms from constraints. Name a primary/binding constraint only when the evidence supports one; otherwise preserve a constraint set, independent constraints, or `not yet identified` rather than forcing false singularity.
4. **Build the opportunity set.** Consider market/segment, positioning, offer, pricing, acquisition, conversion, activation, retention, distribution, capacity, and measurement only where evidence makes them plausible. Do not start with a channel shopping list.
5. **Prioritize strategic bets.** Use [Portfolio prioritization and sequencing](references/portfolio-prioritization-and-sequencing.md). Compare commercial impact, evidence strength, mechanism confidence, effort, reversibility, time to learn, dependencies, capacity, and opportunity cost without hiding uncertainty in fake precision.
6. **Route specialist validation.** Every chosen bet gets the specialist owner that governs its underlying decision. Growth Strategy owns the integrated priority and sequence, not the specialist's technical method.
7. **Sequence the plan.** Resolve verified defects and blocking dependencies before expansion. Prefer actions that either protect commercial downside or create decisive learning before large irreversible commitments.
8. **Define the learning agenda.** State the hypothesis, business metric, guardrails, decision window, evidence needed, and the owner of causal validity. Use `$tracking-measurement` when a causal claim is required.
9. **Define review and adaptation.** Use [Plan governance and review](references/plan-governance-and-review.md). Set context-appropriate review triggers/horizons, decision gates, and `continue`, `hold`, `kill`, `revise`, `defer`, or `route to scaling` outcomes. Material opportunity-cost changes are valid review triggers even when the original initiative has not failed.
10. **Record exact status.** A strategy can be `draft`, `decision-ready`, `approved`, `in execution`, `under review`, or `superseded`. Do not describe a plan as implemented or successful without source-of-truth evidence.

## Rules

- Do not build a “full-funnel plan” by automatically filling every channel or lifecycle stage. Include only decision-relevant work.
- Do not treat AARRR, funnel-stage models, channel portfolios, 90-day plans, 70/20/10 allocation, funding-stage budgets, or any other planning framework as universal structure or evidence.
- Do not assume every business has one binding constraint. Multiple independent or interacting constraints can matter within the same horizon; preserve that structure when evidence supports it.
- Do not force a fixed number of strategic priorities. Stop when additional priorities dilute focus, exceed capacity, or lack decision-grade evidence.
- Do not allocate live paid-media budget here. `$optimization-scaling` owns paid-media scale readiness, marginal economics, and controlled budget/coverage expansion.
- Do not call a channel an opportunity because competitors use it, a benchmark recommends it, or it is currently popular.
- Do not rank opportunities by a fabricated composite score when the inputs are not comparable. Directional tiers or explicit trade-offs are preferable to false precision.
- Do not forecast revenue as guaranteed. State assumptions, scenario ranges, dependencies, and confidence where a forecast is useful.
- A business-level constraint can be upstream of marketing. Product availability, fulfillment, sales capacity, inventory, service quality, cash flow, or measurement failure may block growth and should be surfaced rather than disguised as a marketing tactic problem.
- Preserve non-priorities. A strong strategy states what the business will not focus on during the current horizon and why.
- When evidence cannot yet distinguish between major strategic paths, protecting current value while running the smallest decision-changing research or experiment is a valid strategy.
- No plan authorizes live changes. Spend, pricing, offers, customer journeys, lifecycle systems, or other external mutations still require the owning skill's approval boundary.

## Output

Growth strategy: business objective, baseline, supplied target/desired direction if any, and horizon; economic/quality guardrails; evidence baseline; current limiting constraint/constraint set and confidence; opportunity set; prioritized strategic bets; explicit non-priorities; specialist owners and dependencies; sequence; learning agenda and experiments; measurement owner; capacity/resource implications; review triggers including opportunity-cost changes; scaling handoff where applicable; unknowns/contradictions; exact status.

## Library references

- [strategy-template.md](../../../templates/strategy-template.md) — canonical integrated growth-strategy and marketing-plan record.

## Related owners

- `$marketing-intake`: scope, evidence state, economics definitions, shared context, authorization
- `$icp-jtbd`: segment, JTBD, buying situations, alternatives, positioning implications
- `$customer-research`: qualitative customer evidence and VOC
- `$offer-strategy`: commercial proposition
- `$pricing-monetization`: pricing and exchange structure
- channel skills: channel-specific feasibility and execution decisions
- `$cro`: conversion-boundary friction
- `$activation`: first meaningful value
- `$retention-strategy`: continuation, save, recovery, repeat/renewal, win-back interventions
- `$retention-economics`: realized/predictive customer economics
- `$tracking-measurement`: causal validity and experiment learning
- `$performance-diagnostics`: cross-metric anomaly/constraint diagnosis when performance changed
- `$optimization-scaling`: paid-media scale readiness and controlled scaling after a system is proven
- `$marketing-operations`: recurring execution/review loops once a strategy is approved
- `$marketing-reporting`: stakeholder communication of strategy progress and results

## QA

Confirm the objective and baseline are named, any target was supplied rather than invented, the limiting constraint or constraint set is evidence-based rather than forced into a single bottleneck, opportunities are not channel-first defaults, priorities fit capacity, specialist ownership is preserved, non-priorities are explicit, forecasts are not guarantees, experiments have decision rules and guardrails, scaling is handed to `$optimization-scaling`, opportunity-cost changes can trigger rebalancing, and no draft plan is described as implemented or successful.