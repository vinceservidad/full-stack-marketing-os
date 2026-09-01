# Growth Strategy Evaluation Review

Status: **Pass**

Reviewed scope: `$growth-strategy`, its three references, upgraded `templates/strategy-template.md`, routing, capability ownership, Marketing Context state, and the boundary with `$optimization-scaling`.

## Review findings

### Decision quality

Pass. The skill starts from a named primary business outcome, baseline, horizon, and evidence baseline, then identifies the current limiting condition or constraint structure without forcing every business into one bottleneck. It constructs opportunities from plausible mechanisms, requires explicit non-priorities, and sequences specialist work instead of producing a generic channel checklist.

The refinement explicitly allows `primary/binding`, `co-limiting/interacting`, `independent`, and `not yet identified` constraint states. A single binding constraint is used only when evidence supports it.

### Evidence handling

Pass. Constraint states distinguish verified blocker, supported, plausible, contradicted, and unknown. Competitor activity, external frameworks, benchmarks, forecasts, customer quotes, and local metrics cannot silently become proof of a business opportunity. The plan preserves contradictions and stale source dependencies.

A growth target is not invented to complete a plan. A business-supplied target remains asserted unless evidence supports a stronger feasibility or forecast claim.

When the constraint is not yet identified, the strategy preserves competing hypotheses and can prioritize the smallest evidence-gathering action that materially changes the allocation decision.

### Prioritization

Pass. The system rejects fixed priority counts, universal channel mixes, 70/20/10 allocation, mandatory 90-day plans, and fabricated composite scores. It uses commercial impact, evidence strength, mechanism confidence, effort, reversibility, time-to-learn, dependencies, capacity, and opportunity cost as explicit trade-offs rather than false precision.

Opportunity cost is now a formal review trigger. A priority can be deprioritized when a materially better opportunity emerges or its resource cost changes even if the original initiative has not technically failed.

### Ownership

Pass. `$growth-strategy` owns the integrated business-level direction, constraint structure, opportunity portfolio, strategic bets, non-priorities, sequence, and learning roadmap. Offer, pricing, ICP/JTBD, channels, CRO, activation, retention, measurement, and other specialists retain their underlying decisions.

### Scaling boundary

Pass. Growth Strategy may decide whether paid-media expansion deserves priority versus other business opportunities. `$optimization-scaling` still exclusively owns paid-media readiness, marginal economics, controlled expansion, hold/rollback rules, and live scaling authorization. No strategy document authorizes spend changes.

### Planning governance

Pass. Planning horizon follows decision lag, seasonality, sales cycle, and business context rather than a fixed calendar. Strategy status is separated from implementation and outcome state. Review triggers do not automatically justify strategy changes, and revisions preserve history rather than rewriting prior forecasts or hypotheses.

Plan quality is not judged by roadmap task completion. Stopping or reprioritizing work after new evidence can be a sign of good governance when it protects commercial value or improves learning.

### Marketing Context boundary

Pass. Marketing Context now preserves the strategy's actual constraint structure rather than forcing `Current binding constraint`. A context summary cannot upgrade a plural or unresolved constraint state into one verified bottleneck, and the governing strategy artifact wins when the context is stale.

### Authorization

Pass. The skill is read-only/decision-oriented by default. Live spend, pricing, offer, lifecycle, customer journey, campaign, or other external mutations remain under the owning skill's authorization boundary.

## Regression coverage

Ninety cases cover channel-first plans, framework quotas, singular/plural/unresolved constraint diagnosis, measurement defects, economics, capacity, opportunity construction, prioritization, false scoring, invented targets, specialist boundaries, paid-media scaling, forecasting, context staleness, causal overclaiming, planning horizons, exact status, operations/reporting handoffs, non-priorities, reversibility, dependencies, null/contradictory learning, opportunity-cost rebalancing, roadmap-task-completion misuse, and live-action authorization.

## Final verdict

**Pass.** The refinement keeps the strong business-level orchestration introduced by Growth Strategy while removing hidden one-bottleneck dogma. It makes the strategy more faithful to complex, multi-product, multi-market, capacity-constrained, or simply uncertain businesses without weakening focus, ownership, evidence discipline, or scaling gates.