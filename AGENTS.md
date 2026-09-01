# Contributor Instructions

## Operating principles

1. Start read-only. Do not change budgets, bids, campaigns, conversion goals, audiences, product coverage, offers, tracking, or live pages without explicit approval.
2. Use source-of-truth evidence. Label observed facts, calculations, inferences, assumptions, and unknowns separately.
3. Protect commercial truth. Prefer profit, realized revenue, or qualified pipeline when available; never substitute ROAS, CTR, or platform attribution for business outcome.
4. Preserve valuable coverage and learning unless evidence supports a change. Prefer reversible tests with stopping rules.
5. Distinguish draft, saved, published, live, processing, and verified states.
6. Never fabricate benchmarks, results, customer language, credentials, margins, or causality.
7. Preserve research provenance and privacy. Do not expose unnecessary personal data or report quotations without a traceable supplied source.
8. Treat platform attribution differences separately from collection defects and business-performance changes.
9. Use `GLOSSARY.md` as the canonical terminology contract. Define client-specific metric and lifecycle variants before comparing them.
10. Reserve “Primary conversion action” for the Google Ads action-optimization setting; use “primary business outcome” for the main commercial result.
11. Do not use “profit” without naming the profit level and included costs. Do not double-count discounts or refunds already included in net revenue.
12. Apply `PLATFORM-CURRENCY.md` before current Google or Meta AI, automation, control, reporting, rollout, or interface claims. Do not claim undocumented algorithm changes; distinguish official documentation, account visibility, experiments, inference, and unknowns.
13. Classify substantial operating knowledge with `KNOWLEDGE-TAXONOMY.md`. Do not present a pattern as causality, a heuristic as a best practice, a tactic as a strategy, or a framework/model as proof of an outcome.
14. Scaling requires the `optimization-scaling` readiness, economics, constraint, marginal-evidence, capacity, guardrail, and authorization gates. Never use a universal budget-increase rule or call a tactic proven outside its verified scope.
15. When `.agents/marketing-context.md` exists in the active project, read only the decision-relevant sections before substantial downstream marketing work. Treat it as a versioned context summary, never as evidence promotion: underlying specialist artifacts and source systems still govern, contradictions and stale fields stay visible, and current platform behavior still requires `PLATFORM-CURRENCY.md`.
16. Competitor observations are evidence about competitors, not customer truth or proof that a visible tactic works. Preserve date, source, estimate/inference labels, the real alternative set including status quo where relevant, and do not copy a competitor pattern merely because it is visible.
17. Experiment learning remains scoped to the valid test conditions. Assess validity before direction, preserve nulls and contradictions, separate observed effect from mechanism interpretation, and never turn one test or one external case into a universal best practice.
18. Recurring marketing loops must preserve domain ownership, durable state, idempotency, source freshness, approval scope, verification, and stop/escalation rules. A written loop is `designed`, not scheduled, active, or monitoring; never imply background execution unless the actual runtime is configured and verified.
19. Pricing decisions must separate observed purchase behavior, stated preference, competitor context, model inference, and realized economics. Never treat a competitor price, survey answer, conversion rate, arbitrary markup, price-ending heuristic, or framework default as proof of an optimal price; live commercial changes require explicit approval and source-of-truth verification.

## Skill design

- Keep `SKILL.md` concise and decision-changing.
- Put conditional detail in linked references.
- Give every skill discriminating triggers, required inputs, decision rules, QA, and output shape.
- When several skills apply, appoint one owner for the final response.
- Advice may continue with missing data when safe, but confidence and decision-changing inputs must be explicit.

## Changes

- Update `CHANGELOG.md` for meaningful behavior changes.
- Add or revise evaluations for material decision-rule changes.
- Do not mark an evaluation passed without reviewing the decision, evidence handling, and authorization boundary.
