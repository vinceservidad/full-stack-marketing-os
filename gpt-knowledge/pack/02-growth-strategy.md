<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Business-Level Growth Strategy

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/growth-strategy/SKILL.md`

---
name: growth-strategy
description: Build an evidence-led business-level marketing growth strategy by defining the commercial objective, identifying the current limiting constraint or constraint set, prioritizing growth opportunities, sequencing specialist work, and governing a learning roadmap; not for generic channel checklists, arbitrary budget splits, or taking over specialist execution decisions.
---

# Growth Strategy

Growth Strategy owns the integrated marketing direction: where the business should focus, why that opportunity deserves priority, which specialist decisions are required, what should deliberately not be prioritized, and how the plan will learn and adapt.

It does not replace `$icp-jtbd`, `$offer-strategy`, `$pricing-monetization`, channel skills, `$cro`, `$activation`, `$retention-strategy`, `$tracking-measurement`, or `$optimization-scaling`. It composes their decision-grade outputs into one business-level strategy.

Primary knowledge type: strategy. Use `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`) to label supporting frameworks, methodologies, hypotheses, tactics, templates, and evidence correctly.

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
3. **Identify the current limiting condition(s).** Use Growth constraint and opportunity diagnosis (source: `.agents/skills/growth-strategy/references/growth-constraint-and-opportunity.md`). Separate symptoms from constraints. Name a primary/binding constraint only when the evidence supports one; otherwise preserve a constraint set, independent constraints, or `not yet identified` rather than forcing false singularity.
4. **Build the opportunity set.** Consider market/segment, positioning, offer, pricing, acquisition, conversion, activation, retention, distribution, capacity, and measurement only where evidence makes them plausible. Do not start with a channel shopping list.
5. **Prioritize strategic bets.** Use Portfolio prioritization and sequencing (source: `.agents/skills/growth-strategy/references/portfolio-prioritization-and-sequencing.md`). Compare commercial impact, evidence strength, mechanism confidence, effort, reversibility, time to learn, dependencies, capacity, and opportunity cost without hiding uncertainty in fake precision.
6. **Route specialist validation.** Every chosen bet gets the specialist owner that governs its underlying decision. Growth Strategy owns the integrated priority and sequence, not the specialist's technical method.
7. **Sequence the plan.** Resolve verified defects and blocking dependencies before expansion. Prefer actions that either protect commercial downside or create decisive learning before large irreversible commitments.
8. **Define the learning agenda.** State the hypothesis, business metric, guardrails, decision window, evidence needed, and the owner of causal validity. Use `$tracking-measurement` when a causal claim is required.
9. **Define review and adaptation.** Use Plan governance and review (source: `.agents/skills/growth-strategy/references/plan-governance-and-review.md`). Set context-appropriate review triggers/horizons, decision gates, and `continue`, `hold`, `kill`, `revise`, `defer`, or `route to scaling` outcomes. Material opportunity-cost changes are valid review triggers even when the original initiative has not failed.
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

- strategy-template.md (source: `templates/strategy-template.md`) — canonical integrated growth-strategy and marketing-plan record.

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

## Source: `.agents/skills/growth-strategy/references/growth-constraint-and-opportunity.md`

# Growth Constraint and Opportunity Diagnosis

Use this reference when the business asks where growth should come from, what is holding growth back, or which opportunity should be pursued first.

A growth constraint is a condition materially limiting the primary business outcome within the stated horizon. A single primary/binding constraint may exist, but do not assume one must exist. Multiple independent or interacting constraints can matter at the same time, and evidence may be insufficient to identify the limiting condition yet.

## Diagnose in layers

Start from the primary business outcome and work outward:

1. **Outcome reality** — did realized revenue, qualified pipeline, contribution, customer count, or the approved business outcome actually change?
2. **Measurement integrity** — are source definitions, tracking, timing, and cohort boundaries stable enough to compare?
3. **Demand / market** — is sufficient qualified demand available in the chosen market and segment?
4. **Positioning / offer / pricing** — does the proposition, exchange structure, or perceived value block demand or conversion?
5. **Acquisition** — are qualified prospects being reached efficiently enough, with appropriate coverage and creative/message fit?
6. **Conversion** — is avoidable pre-conversion friction blocking demand that already exists?
7. **Activation** — where a distinct activation stage exists, are converted customers reaching first meaningful value?
8. **Retention** — are customers continuing, renewing, repurchasing, or returning at an economically acceptable rate?
9. **Capacity / operations** — can inventory, fulfillment, service, sales, cash flow, support, or production support more growth?
10. **Scale ceiling** — only after the system is commercially sound, ask whether the proven acquisition system can absorb more investment.

Do not mechanically inspect every layer when evidence already identifies a verified blocker. The list is a diagnostic map, not a mandatory funnel sequence.

## Constraint evidence states

Classify each candidate constraint:

- **verified blocker** — direct source evidence shows it currently prevents or materially limits the objective
- **supported constraint** — multiple decision-relevant signals point to it, but causal certainty is incomplete
- **plausible constraint** — a reasonable hypothesis with important missing evidence
- **contradicted** — current evidence weighs against it
- **unknown** — insufficient evidence to judge

Then classify the strategic structure:

- **primary / binding** — one constraint is sufficiently supported as the dominant current limit within the stated horizon
- **co-limiting / interacting** — two or more constraints jointly limit the outcome and treating one alone as binding would misrepresent the system
- **independent constraints** — separate business units, segments, products, markets, or pathways have different meaningful limits within the same plan scope
- **not yet identified** — evidence cannot yet distinguish among decision-changing candidates

A low metric is not automatically a constraint. For example, a low email click rate may be irrelevant if the business is inventory-constrained; a high acquisition CPA may not be the first constraint if gross margin or lead quality makes the entire offer uneconomic.

## Symptoms versus constraints

Common symptoms that require diagnosis:

- traffic down
- ROAS down
- conversion rate down
- churn up
- repeat purchase down
- activation down
- CAC up
- engagement down
- revenue flat despite more spend
- strong channel metrics with weak profit

For each symptom, ask what mechanism could produce it and what competing explanation remains plausible. Route measurement defects to `$tracking-measurement`, broad metric shifts to `$performance-diagnostics`, and specialist mechanisms to their owners.

## Opportunity construction

Generate an opportunity only when it connects:

`constraint or uncertainty → mechanism hypothesis → proposed strategic change/evidence step → expected business or learning effect → required specialist validation → evidence needed`

An opportunity can include:

- deepen a validated segment or buying situation
- fix positioning or offer mismatch
- change pricing/package architecture
- improve an existing acquisition channel or test a new one where demand/channel fit is supported
- remove conversion friction
- improve activation path-to-value
- resolve a retention cause
- fix measurement that blocks decisions
- expand capacity that is suppressing otherwise-valid demand
- run the smallest research/test that can distinguish between unresolved major constraints
- scale a proven system through `$optimization-scaling`

Do not create an opportunity merely because a tactic exists.

## Channel opportunity gate

Before calling a new channel a strategic opportunity, identify:

- the audience/buying situation it can plausibly reach
- why the channel's format and economics fit the objective
- the evidence supporting demand or audience-channel fit
- required creative/content/operational capacity
- measurement path to the business outcome
- opportunity cost versus improving existing validated channels

Competitor presence, platform popularity, or a generic benchmark is not enough.

## Cross-constraint interactions

More than one constraint can coexist. Do not force a single binding constraint when the evidence supports a constraint set.

Examples:

- weak retention may make acquisition scaling economically unsafe
- poor activation may create later churn
- a pricing change may improve contribution but reduce acquisition conversion
- a strong offer may still fail if fulfillment capacity is exhausted
- measurement failure may prevent choosing between otherwise-plausible constraints
- two product lines may have different independent constraints inside one business-level plan

When one primary constraint is supported, name it and distinguish secondary dependencies. When several are co-limiting or independent, preserve that structure and prioritize across them using commercial impact, dependency, evidence, capacity, and opportunity cost.

## When the constraint is not yet identified

`Not yet identified` is a valid decision state. Do not choose a bottleneck simply to complete the template.

When uncertainty blocks a major allocation decision:

1. protect current verified value and downside
2. preserve competing constraint hypotheses
3. choose the smallest evidence-gathering action that can materially change the strategic choice
4. predefine what evidence would support or contradict each candidate
5. review the portfolio when that evidence matures

## Minimum output

Return: objective and baseline; candidate constraints; evidence state for each; strategic constraint structure (`primary/binding`, `co-limiting/interacting`, `independent`, or `not yet identified`); confidence; competing explanations; opportunity or learning hypotheses; specialist owners; missing evidence; stop/escalation condition.

## Source: `.agents/skills/growth-strategy/references/plan-governance-and-review.md`

# Plan Governance and Review

Use this reference to turn a strategic direction into an adaptive plan without confusing the plan with implementation or turning a calendar into evidence.

## Planning horizon

Choose a horizon that matches the business decision, conversion/retention lag, seasonality, sales cycle, cash runway, operational capacity, and learning speed.

Examples such as 30 days, 90 days, a quarter, or a year are planning conveniences, not universal standards. A short-cycle ecommerce test and an enterprise sales strategy should not be forced into the same review rhythm.

Record:

- strategy start date
- decision horizon
- expected signal window for each major hypothesis
- business-outcome maturity window
- known seasonal/event constraints
- conditions that require an earlier review

## Plan layers

Separate:

1. **Objective** — the business result and guardrails.
2. **Strategic bets** — the chosen mechanisms and priorities.
3. **Validation work** — evidence needed before larger commitment.
4. **Specialist plans** — channel, offer, pricing, CRO, activation, retention, measurement, or operations work owned by specialists.
5. **Execution state** — what is actually approved, configured, live, or verified.
6. **Learning** — what the observed result changes about the strategy.

Never collapse these into a task list and call it strategy.

## Decision gates

For each strategic bet define:

- hypothesis
- evidence state at entry
- specialist owner
- dependencies
- primary business metric or validated leading indicator
- guardrails
- minimum decision window or maturity condition
- what evidence supports `continue`
- what evidence supports `hold`
- what evidence supports `revise`
- what evidence supports `kill`
- what condition routes to `$optimization-scaling`

Do not write decision rules after seeing the result when they could reasonably have been defined before the test.

## Review triggers

A strategy review can be triggered by:

- scheduled decision point
- material business-outcome deviation
- verified constraint removal or a change from one constraint structure to another
- newly verified blocker or newly supported co-limiting constraint
- evidence showing the previously assumed binding constraint is not actually singular or dominant
- economics or capacity change
- market/competitor change that materially alters the decision
- experiment result that supports or contradicts a strategic assumption
- major offer/pricing/product/service change
- measurement-definition change that breaks comparability
- material change in opportunity cost, such as a newly available higher-value opportunity or a priority consuming much more capacity than expected

A review trigger does not itself prove the strategy should change.

## Change control

When revising the strategy:

- preserve the previous decision and evidence state
- state what new evidence changed the view
- distinguish constraint change from tactic failure
- record whether the strategy moved between `primary/binding`, `co-limiting/interacting`, `independent`, or `not yet identified` constraint states
- record which priorities were added, removed, deferred, or resequenced
- state when opportunity cost, rather than failure, caused a reprioritization
- update Marketing Context only after the specialist/strategy artifact has a clear state
- do not rewrite prior forecasts or hypotheses as though the new evidence had been known earlier

## Strategy status

Use exact states:

- `draft`
- `decision-ready`
- `approved`
- `in execution`
- `under review`
- `superseded`

A strategy is not `verified`. Individual hypotheses, implementations, and business outcomes can be verified; strategy remains an adaptive decision system.

## Operating handoff

Once approved, recurring review or cross-skill coordination can be expressed as a `$marketing-operations` loop. Writing the loop does not make it active; runtime state must still be configured and verified.

Stakeholder progress summaries route to `$marketing-reporting`. The report should preserve the strategy's evidence and exact-status language rather than converting an in-progress test into a success claim.

## Plan-quality check

Do not judge a growth strategy by percentage of roadmap tasks completed. A plan can be well governed when it stops or deprioritizes work after new evidence changes the constraint, economics, or opportunity cost.

Judge plan quality by whether it:

- focused limited resources on the best-supported opportunities
- protected material downside and current value
- produced decision-grade learning
- preserved specialist ownership and authorization boundaries
- adapted when evidence or opportunity cost changed
- kept prior decisions and assumptions auditable

## Minimum output

Return: horizon; strategic bets; validation work; specialist dependencies; constraint structure; decision gates; review triggers including opportunity-cost changes; implementation state; learning/change log; next review condition; exact status.

## Source: `.agents/skills/growth-strategy/references/portfolio-prioritization-and-sequencing.md`

# Portfolio Prioritization and Sequencing

Use this reference after a plausible opportunity set exists. It governs which strategic bets should be pursued now, later, or not at all.

The goal is not to maximize the number of initiatives. It is to concentrate limited attention, budget, creative capacity, engineering/operations effort, and learning bandwidth on the few opportunities most likely to improve the primary business outcome or resolve the binding constraint.

## Compare opportunities on explicit dimensions

For each opportunity, record:

- connection to the binding constraint
- expected commercial impact and the basis for that expectation
- evidence strength
- confidence in the proposed mechanism
- time to meaningful signal and time to business outcome
- implementation effort and specialist capacity
- cash, inventory, service, creative, sales, or technical dependencies
- reversibility and downside
- measurement quality and ability to learn
- opportunity cost
- strategic optionality created if the hypothesis is supported

Do not invent precise numeric scores when the underlying judgments are ordinal or uncertain. Use qualitative tiers, explicit trade-offs, or ranges when that represents the evidence more honestly.

## Priority states

A useful portfolio can classify work as:

- **protect / fix now** — verified defect, legal/compliance issue, broken measurement, customer harm, or material commercial leakage
- **priority bet** — strongest current combination of commercial relevance, evidence, feasibility, and learning value
- **validate first** — potentially important but requires a smaller evidence-gathering step before material commitment
- **maintain** — currently healthy capability that needs continuity but not major additional investment
- **defer** — plausible, but blocked by dependency, capacity, or a higher-value opportunity
- **reject / stop** — contradicted, uneconomic, outside strategy, or not worth the opportunity cost

These are decision states, not universal categories that every plan must contain.

## Sequence by dependency

Prefer this order when the dependencies apply:

1. protect customers, legal/compliance boundaries, and source-of-truth integrity
2. fix verified blockers and measurement defects that prevent decisions
3. validate the binding constraint and core mechanism
4. repair economics, offer, product/service promise, activation, or retention where they make acquisition expansion unsafe
5. test focused opportunities that create decisive learning
6. expand a supported strategy through the relevant specialist
7. route paid-media scaling to `$optimization-scaling` only when its readiness and marginal-economics gates are satisfied

Do not use this as a rigid funnel order. A verified market-demand problem can take priority over a minor conversion issue; a capacity ceiling can make all growth tests premature.

## Strategic bets versus tasks

A strategic bet should express a choice and mechanism, for example:

`Deepen Segment A with Offer B because verified buying-situation evidence and contribution economics suggest the current broad-market approach is diluting qualified conversion.`

Tasks such as “launch Meta campaign,” “rewrite homepage,” or “send emails” are implementation activities. They become relevant only after a strategic bet explains why they are needed.

## Portfolio concentration

Do not force a fixed number of priorities. Use the smallest set that:

- addresses the binding constraint
- fits actual implementation capacity
- preserves business-critical maintenance
- allows tests to remain interpretable
- avoids so much simultaneous change that learning becomes ambiguous

A business with one urgent blocker may need one strategic priority. A diversified business may need several independent bets. The number comes from scope and capacity, not a framework quota.

## Channel portfolio rules

Growth Strategy may decide a channel's strategic role, such as `core acquisition`, `validation test`, `retention support`, `brand/education`, or `deprioritized`, but the channel skill owns the technical execution decision.

Do not allocate media budget from a universal ratio. Budget implications should reflect:

- proven or plausible marginal opportunity
- economics
- demand capacity
- channel-specific constraints
- learning objective
- downside tolerance
- cash/capacity limits

Actual paid-media expansion routes to `$optimization-scaling`.

## Non-priorities

Every decision-grade plan should state important work that is intentionally not being pursued during the current horizon, especially tempting initiatives with high distraction cost.

For each non-priority, state the reason and what evidence or condition would cause reconsideration.

## Minimum output

Return: opportunity; constraint link; evidence/confidence; commercial upside; effort/capacity; reversibility/downside; time to learn; dependencies; priority state; owner; sequence; reconsideration trigger.
