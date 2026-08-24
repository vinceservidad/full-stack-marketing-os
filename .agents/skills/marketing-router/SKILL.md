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
5. Before a substantial audit, diagnosis, scaling decision, or any live implementation, confirm scope, evidence state, metric definitions, and authorization are recorded. Route to `$marketing-intake` when they are not; it owns the response until the evidence state is known.
6. State missing inputs that could reverse the decision. Continue with labeled assumptions when safe.
7. When the request says current, latest, new, AI, algorithm, rollout, or interface—or depends on a fast-changing platform control—route to the channel skill and enforce `PLATFORM-CURRENCY.md` before accepting the stored label or behavior.
8. Classify the requested deliverable by its primary knowledge type; use secondary types only when they change how the artifact should be used or validated.

## Skill map

- Google campaign structure, queries, Shopping/PMax, bids, or budgets: `$google-ads`.
- Meta structure, audiences, delivery, placements, or ads: `$meta-ads`.
- Angles, hooks, concepts, formats, briefs, or creative tests: `$creative-strategy`.
- Landing page, product page, form, checkout, or persuasion friction: `$cro`.
- Metric change, spend/sales anomaly, or causal triage: `$performance-diagnostics`.
- Event integrity, attribution differences, conversion architecture, source reconciliation, incrementality testing, or causal evidence grading: `$tracking-measurement`.
- Interviews, reviews, surveys, customer language, objections, or evidence synthesis: `$customer-research`.
- Priority segments, buying situations, buyer roles, or Jobs-to-be-Done: `$icp-jtbd`.
- Scale readiness, marginal economics, budget/coverage expansion, portfolio allocation, de-scaling, recovery, or budget/outcome pacing within an approved plan: `$optimization-scaling`.
- Undefined scope, unclear data provenance, missing economics, ambiguous conversion definitions, uncertain access, or an unclear authorization boundary: `$marketing-intake`.
- Customer lifetime value, payback period, cohort retention, churn, or lead-to-revenue maturation: `$retention-economics`.

Common compositions:

- Spend rose and sales fell: performance diagnostics owns; channel skill supports; CRO joins only if landing evidence suggests a site issue.
- Produce Meta concepts: creative strategy owns; Meta Ads supplies placement and delivery constraints.
- Clicks without conversions: performance diagnostics owns; channel skill and CRO support; flag measurement integrity as an unresolved dependency when needed.
- Define a new audience and message: ICP/JTBD owns the segment decision; customer research supplies evidence; creative strategy translates it into tests.
- Platforms disagree on revenue: tracking and measurement owns; performance diagnostics joins only if the business outcome itself changed.
- Is this channel actually incremental: tracking and measurement owns method selection and evidence grading; the channel skill supplies account controls; optimization and scaling consumes the result and never substitutes attribution for it.
- Is this customer base or channel worth scaling on a lifetime basis: retention economics owns the lifetime value and payback model; optimization and scaling owns the scaling decision and applies its own proof standard to the model's output.
- Audit request with no economics, scope, or source of truth supplied: intake owns until the evidence state is recorded; the channel skill then owns the audit itself.
- Scale campaigns or allocate more budget: optimization and scaling owns; channel skill supplies account controls; performance diagnostics localizes the constraint; tracking joins when measurement is not decision-ready.

## Capability boundary

Route only to a skill that exists. Check [`CAPABILITY-REGISTRY.md`](../../../CAPABILITY-REGISTRY.md) before answering a request outside the skill map. Boundaries are task-level, not discipline-level: a discipline can be partly governed and partly unsupported.

- Analytics: tracking architecture, event integrity, and attribution differences belong to `$tracking-measurement`; performance analysis, segmentation, and anomaly diagnosis to `$performance-diagnostics`; allocation and marginal evidence to `$optimization-scaling`. Business-intelligence engineering, pipeline or warehouse design, and dashboard implementation have no governed specialist.
- Reporting: a bounded report is owned by the skill that owns the underlying decision — the Google Ads audit report by `$google-ads`, the measurement integrity report by `$tracking-measurement`, the scaling review by `$optimization-scaling`. Cross-channel executive reporting, budget and outcome pacing, forecasting, and recurring reporting governance have no governed specialist.
- Copywriting: paid-ad hooks, angles, concepts, and creative briefs belong to `$creative-strategy`; conversion-page copy evaluation to `$cro`. Email, lifecycle, website, sales-page, long-form, brand, and Search Engine Optimization copywriting have no governed specialist and must not be routed to `$creative-strategy` as though governed.
- Search Engine Optimization and content strategy: no governed specialist. Do not substitute `$google-ads`. Customer research, CRO, or measurement may support a distinct part of the request; the Search Engine Optimization work itself remains ungoverned.
- Other unsupported channels — email and lifecycle, TikTok, LinkedIn, YouTube as a discipline, affiliate, influencer, organic social, programmatic, public relations: the router owns the response and declares the gap.

When no governed specialist covers the primary discipline: do not silently substitute an adjacent channel skill; name the missing capability; apply platform-agnostic frameworks only where they address a distinct part of the request; label platform-specific guidance as ungoverned and unverified by this system; never name a skill that does not exist; and state the gap in the exact-status line.

## Rules

- Do not activate every plausible skill.
- Do not route a request to a skill absent from the capability registry, and do not present a partially covered discipline as fully governed.
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

Return: objective; primary knowledge type; routed skills and owner; capability status (governed, partially covered, or unsupported); evidence; missing inputs; approach; findings or deliverable; recommended next action; exact status.


## Library references

Owned root artifacts, read when their scope applies:

- [decision-prioritization.md](../../../frameworks/decision-prioritization.md) — prioritization framework for routed work.
- [strategy-template.md](../../../templates/strategy-template.md) — strategy deliverable format.

## QA

Confirm routing is minimal, an owner is named, every named skill exists in the capability registry, any capability gap is disclosed, unknowns are visible, commercial outcome is explicit, current-platform claims meet the freshness gate, and no external action is implied without authorization.
