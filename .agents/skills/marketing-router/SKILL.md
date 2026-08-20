---
name: marketing-router
description: Route ambiguous or multi-discipline marketing requests to the smallest useful set of Marketing OS skills when a task spans channels, funnel stages, diagnosis, or deliverables.
---

# Marketing Router

Turn the request into a bounded plan, select the minimum skills needed, and appoint one owner for the final response.

## Route

1. Identify the business outcome, business model, funnel stage, timeframe, market, channel, and requested action.
2. Classify intent: `audit`, `diagnose`, `plan`, `create`, `optimize`, `report`, or `activate`.
3. Classify risk: read-only analysis; reversible draft; external mutation; spend, tracking, or revenue-critical mutation.
4. Select one primary skill and only supporting skills that answer a distinct dependency.
5. State missing inputs that could reverse the decision. Continue with labeled assumptions when safe.

## Skill map

- Google campaign structure, queries, Shopping/PMax, bids, or budgets: `$google-ads`.
- Meta structure, audiences, delivery, placements, or ads: `$meta-ads`.
- Angles, hooks, concepts, formats, briefs, or creative tests: `$creative-strategy`.
- Landing page, product page, form, checkout, or persuasion friction: `$cro`.
- Metric change, spend/sales anomaly, or causal triage: `$performance-diagnostics`.
- Event integrity, attribution differences, conversion architecture, or source reconciliation: `$tracking-measurement`.
- Interviews, reviews, surveys, customer language, objections, or evidence synthesis: `$customer-research`.
- Priority segments, buying situations, buyer roles, or Jobs-to-be-Done: `$icp-jtbd`.

Common compositions:

- Spend rose and sales fell: performance diagnostics owns; channel skill supports; CRO joins only if landing evidence suggests a site issue.
- Produce Meta concepts: creative strategy owns; Meta Ads supplies placement and delivery constraints.
- Clicks without conversions: performance diagnostics owns; channel skill and CRO support; flag measurement integrity as an unresolved dependency when needed.
- Define a new audience and message: ICP/JTBD owns the segment decision; customer research supplies evidence; creative strategy translates it into tests.
- Platforms disagree on revenue: tracking and measurement owns; performance diagnostics joins only if the business outcome itself changed.

## Rules

- Do not activate every plausible skill.
- Do not let a channel metric define the business outcome.
- If measurement integrity is unknown, treat platform conversion changes as provisional.
- For live changes, first state the exact change, expected effect, downside, rollback condition, and approval boundary.
- Never describe a draft recommendation as implemented.

## Output

Return: objective; routed skills and owner; evidence; missing inputs; approach; findings or deliverable; recommended next action; exact status.

## QA

Confirm routing is minimal, an owner is named, unknowns are visible, commercial outcome is explicit, and no external action is implied without authorization.
