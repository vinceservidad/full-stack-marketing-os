---
name: marketing-router
description: Route ambiguous or multi-discipline marketing requests to the smallest useful set of Marketing OS skills when a task spans channels, funnel stages, diagnosis, or deliverables.
---

# Marketing Router

Turn the request into a bounded plan, select the minimum skills needed, and appoint one owner for the final response.

Use [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md) when the request asks for a strategy, framework, model, methodology, process, playbook, pattern, tactic, technique, template, best practice, or heuristic. Name the primary knowledge type in the response.

## Route

1. Identify the business outcome, business model, funnel stage, timeframe, market, channel, and requested action.
   Keep funnel/journey stage, awareness level, audience temperature, and lifecycle stage distinct.
2. Classify intent: `audit`, `diagnose`, `plan`, `create`, `optimize`, `report`, or `activate`.
3. Classify risk: read-only analysis; reversible draft; external mutation; spend, tracking, or revenue-critical mutation.
4. Select one primary skill and only supporting skills that answer a distinct dependency.
5. State missing inputs that could reverse the decision. Continue with labeled assumptions when safe.
6. When the request says current, latest, new, AI, algorithm, rollout, or interface—or depends on a fast-changing platform control—route to the channel skill and enforce `PLATFORM-CURRENCY.md` before accepting the stored label or behavior.
7. Classify the requested deliverable by its primary knowledge type; use secondary types only when they change how the artifact should be used or validated.

## Skill map

- Google campaign structure, queries, Shopping/PMax, bids, or budgets: `$google-ads`.
- Meta structure, audiences, delivery, placements, or ads: `$meta-ads`.
- Angles, hooks, concepts, formats, briefs, or creative tests: `$creative-strategy`.
- Landing page, product page, form, checkout, or persuasion friction: `$cro`.
- Metric change, spend/sales anomaly, or causal triage: `$performance-diagnostics`.
- Event integrity, attribution differences, conversion architecture, or source reconciliation: `$tracking-measurement`.
- Interviews, reviews, surveys, customer language, objections, or evidence synthesis: `$customer-research`.
- Priority segments, buying situations, buyer roles, or Jobs-to-be-Done: `$icp-jtbd`.
- Scale readiness, marginal economics, budget/coverage expansion, portfolio allocation, de-scaling, or recovery: `$optimization-scaling`.

Common compositions:

- Spend rose and sales fell: performance diagnostics owns; channel skill supports; CRO joins only if landing evidence suggests a site issue.
- Produce Meta concepts: creative strategy owns; Meta Ads supplies placement and delivery constraints.
- Clicks without conversions: performance diagnostics owns; channel skill and CRO support; flag measurement integrity as an unresolved dependency when needed.
- Define a new audience and message: ICP/JTBD owns the segment decision; customer research supplies evidence; creative strategy translates it into tests.
- Platforms disagree on revenue: tracking and measurement owns; performance diagnostics joins only if the business outcome itself changed.
- Scale campaigns or allocate more budget: optimization and scaling owns; channel skill supplies account controls; performance diagnostics localizes the constraint; tracking joins when measurement is not decision-ready.

## Rules

- Do not activate every plausible skill.
- Do not let a channel metric define the business outcome.
- Use “primary business outcome” for the main commercial result. Reserve “Primary conversion action” for Google Ads' action-optimization setting.
- When terms differ by platform or client, preserve the strategic concept and state the current interface or source-system label separately.
- If measurement integrity is unknown, treat platform conversion changes as provisional.
- For live changes, first state the exact change, expected effect, downside, rollback condition, and approval boundary.
- Never describe a draft recommendation as implemented.
- Never convert an undocumented platform “algorithm change” into a fact. Label official documentation, account observation, experimental evidence, inference, and unknowns separately.
- Do not present a pattern as causality, a heuristic as a guarantee, a tactic as a strategy, or a framework/model as proof of an outcome.
- Do not treat more spend, conversions, attributed revenue, or blended ROAS as proof of scaling; require scoped readiness, marginal business evidence, capacity, and rollback rules.

## Output

Return: objective; primary knowledge type; routed skills and owner; evidence; missing inputs; approach; findings or deliverable; recommended next action; exact status.

## QA

Confirm routing is minimal, an owner is named, unknowns are visible, commercial outcome is explicit, current-platform claims meet the freshness gate, and no external action is implied without authorization.
