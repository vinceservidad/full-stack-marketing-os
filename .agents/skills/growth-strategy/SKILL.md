---
name: growth-strategy
description: Turn a verified business objective and specialist evidence into a prioritized, time-bounded growth portfolio across acquisition, conversion, activation, retention, monetization, and enabling capabilities; not for generic channel lists, fixed 90-day plans, universal budget splits, or bypassing specialist ownership and scaling gates.
---

# Growth Strategy

Growth Strategy owns cross-functional growth direction: which constraints and opportunities deserve attention, how specialist initiatives fit together, what should happen first, and what evidence should change the plan.

It does not own channel mechanics, customer research, offer design, pricing, CRO, activation, retention interventions, measurement validity, or scaling execution. Those decisions stay with their governed owners. Growth Strategy consumes their evidence and assembles a coherent portfolio.

Primary knowledge type: methodology. Classify supporting frameworks, heuristics, models, tactics, experiments, and evidence with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md).

## Inputs

Before a decision-grade plan, confirm:

- business model, primary business outcome, and decision horizon
- source-of-truth baseline for the primary outcome and relevant guardrails
- current economics, cash/capacity constraints, and material operational limits
- market, ICP/JTBD, positioning, offer, and pricing state where decision-relevant
- acquisition/channel evidence and current demand/coverage constraints
- conversion, activation, and retention state where those stages exist
- measurement integrity, experiment learning, and important unknowns
- current strategic commitments, dependencies, implementation capacity, and authorization boundary

Use the decision-relevant parts of `.agents/marketing-context.md` when available, but preserve the evidence state of the underlying specialist artifacts.

## Method

1. **Define the growth decision.** State the primary business outcome, current baseline, target or desired direction if one is actually supplied, horizon, scope, economics, and guardrails. Do not invent a growth target.
2. **Map the growth system.** Use [Growth system and constraints](references/growth-system-and-constraints.md). Check market/demand, acquisition, conversion, activation, retention, monetization, measurement/learning, and operational capacity only where they are relevant to the business model.
3. **Identify constraints without forcing one-bottleneck dogma.** Separate verified constraints, likely constraints, symptoms, dependencies, and unknowns. A single weak metric does not prove the binding constraint.
4. **Build the opportunity set from governed owners.** Candidate opportunities must trace to a diagnosed problem, evidence-backed upside, capability gap, or learning need. Do not generate a channel list because channels exist.
5. **Prioritize the portfolio.** Use [Opportunity prioritization and portfolio](references/opportunity-prioritization-and-portfolio.md). Consider commercial impact, evidence strength, mechanism confidence, reversibility, time-to-learn, capacity, dependencies, downside, and opportunity cost. Avoid false-precision scores unless the user explicitly needs a scoring model.
6. **Assign a portfolio role.** When useful, classify an initiative as `protect`, `exploit`, `explore`, or `build-capability`. These are planning labels, not universal allocation percentages.
7. **Sequence by dependency and learning.** Use [Planning horizons and review](references/planning-horizons-and-review.md). Resolve verified defects and blockers first; put prerequisite measurement, product/operations, offer/pricing, or capacity work before dependent growth bets. Use the requested horizon or a justified one; never default to 30/60/90 or quarterly planning as a universal rule.
8. **Hand each initiative to its owner.** The plan names the specialist, decision, evidence needed, deliverable, review condition, and exact status. Growth Strategy coordinates the portfolio; the specialist owns the substantive recommendation and any live change.
9. **Connect measurement and learning.** Route causal design and experiment validity to `$tracking-measurement`. Feed valid learning back into the opportunity set. A failed or null test is a planning input, not wasted work.
10. **Review and rebalance.** Revisit the plan when the primary outcome, constraint, evidence, economics, capacity, or market conditions materially change. Preserve decision history instead of rewriting the plan to make prior choices look correct.

## Rules

- Do not use a fixed 90-day plan, 70/20/10 allocation, experiment-budget percentage, channel count, funnel mix, or stage quota as a universal best practice.
- Do not call a metric problem a strategic constraint before checking competing explanations and the specialist owner.
- Do not allocate budget from platform ROAS alone. Use source-of-truth economics and route paid-media expansion through `$optimization-scaling`.
- Do not recommend a new channel merely because a competitor uses it or because the current portfolio is “too concentrated.” Diversification has cost and requires a business reason.
- Do not force every business through acquisition → activation → retention when a stage is not decision-relevant.
- Do not let planning become a backlog of every good idea. A strategy requires choices, sequencing, explicit non-priorities, and opportunity cost.
- Do not treat a high-impact but unsupported idea as equivalent to a verified defect or replicated opportunity. Preserve evidence strength.
- Do not hide capacity, cash flow, inventory, sales, fulfillment, product, compliance, or service constraints just because the artifact is called a marketing plan.
- Do not let a growth plan authorize live changes. Spend, pricing, offer, tracking, customer-state, campaign, or site mutations still require the owning skill's approval boundary.
- Do not call a planned initiative implemented, a launched initiative validated, or a portfolio successful until the relevant owner verifies the state and outcome.
- When evidence is too weak to choose a growth direction, the valid strategy may be to protect current performance and run the smallest decision-changing research or experiment.
- If the main constraint is outside governed marketing scope, state that explicitly rather than inventing a marketing solution.

## Output

Return: business objective; primary business outcome and baseline; horizon; growth-system map; verified/likely constraints and unknowns; opportunity set; prioritized portfolio with role, rationale, evidence, owner, dependency, cost/capacity, risk, and status; explicit non-priorities; sequence; measurement/learning plan; scaling handoffs; review triggers; approval boundaries; exact status.

## Library references

- [strategy-template.md](../../../templates/strategy-template.md) — canonical growth strategy and planning record.
- [Growth system and constraints](references/growth-system-and-constraints.md) — system mapping and constraint diagnosis.
- [Opportunity prioritization and portfolio](references/opportunity-prioritization-and-portfolio.md) — evidence-led opportunity selection and portfolio roles.
- [Planning horizons and review](references/planning-horizons-and-review.md) — dependency sequencing, horizon selection, and plan revision.

## Related owners

- `$marketing-intake`: primary outcome, shared context, evidence state, definitions, authorization
- `$performance-diagnostics`: performance anomaly and competing-cause diagnosis
- `$customer-research` / `$icp-jtbd`: customer, segment, market, JTBD, and competitive evidence
- `$offer-strategy` / `$pricing-monetization`: proposition and commercial exchange decisions
- channel skills: channel-specific opportunity and execution evidence
- `$cro`: conversion constraints
- `$activation`: first-value constraints
- `$retention-strategy` / `$retention-economics`: continuation interventions and mature economics
- `$tracking-measurement`: measurement validity, causal evidence, experiment learning
- `$optimization-scaling`: readiness and controlled expansion of proven paid-media opportunities
- `$marketing-operations`: recurring execution/decision loops after the plan defines what must recur
- `$marketing-reporting`: stakeholder communication of the plan or its results

## QA

Confirm the plan starts from a named business outcome and baseline; constraints are evidence-graded rather than guessed; every initiative traces to a diagnosed opportunity or learning need; specialist ownership is preserved; portfolio choices include non-priorities and opportunity cost; no universal horizon/allocation/channel formula is smuggled in; paid-media expansion still passes scaling gates; live changes retain their authorization boundaries; and the plan has explicit review triggers rather than becoming a static calendar.