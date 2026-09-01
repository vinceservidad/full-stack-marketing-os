# Growth Strategy Behavioral Evaluations

These cases test `$growth-strategy` routing, constraint diagnosis, portfolio prioritization, horizon selection, specialist ownership, economics, learning, and authorization.

| # | Case | Expected behavior |
|---:|---|---|
| 1 | User asks for a marketing plan with no business objective | Require or label the primary business outcome before decision-grade prioritization. |
| 2 | User says “grow revenue 50%” with no baseline or horizon | Preserve the target as asserted; require baseline/horizon/economics rather than inventing a plan. |
| 3 | Team asks for a default 90-day plan | Reject 90 days as universal; choose horizon from business cycle unless user explicitly requests 90 days. |
| 4 | User explicitly asks for a 90-day plan | Use 90 days but sequence by dependencies, lag, learning, and capacity rather than generic 30/60/90 buckets. |
| 5 | Team wants 70/20/10 core/experiment allocation | Reject fixed allocation as a universal rule; size portfolio from evidence, economics, downside, and capacity. |
| 6 | Team wants 10% of budget reserved for experiments | Treat as a proposed policy, not best practice; require business/economic justification and authorization. |
| 7 | Plan includes five channels because “diversification is safer” | Reject channel-count quota; require a business reason and evidence for each channel. |
| 8 | Competitor is active on TikTok | Treat as competitor context, not proof TikTok is a priority for this business. |
| 9 | Brand Search has highest ROAS | Do not automatically allocate more budget; check incremental demand, saturation, and marginal economics. |
| 10 | Meta has lower ROAS but creates incremental new-customer demand | Preserve cross-channel role; use source-of-truth/incrementality evidence rather than attributed ROAS ranking alone. |
| 11 | Checkout is broken while team wants more traffic | Prioritize verified revenue leakage or route it before acquisition expansion. |
| 12 | Tracking is materially broken | Treat measurement repair as a prerequisite before major allocation decisions. |
| 13 | Tracking is imperfect but enough for a reversible low-risk test | Continue with explicit uncertainty rather than blocking all progress automatically. |
| 14 | CTR fell and team calls creative the bottleneck | Treat CTR as a symptom; require competing-cause diagnosis before declaring the constraint. |
| 15 | Traffic fell after season ended | Check demand/seasonality before labeling SEO or paid media the constraint. |
| 16 | Activation is low and onboarding emails are proposed | Route value definition/barrier to `$activation`; growth strategy decides only whether activation deserves portfolio priority. |
| 17 | Churn is high because of billing failures | Route intervention to `$retention-strategy`; do not choose win-back messaging as generic solution. |
| 18 | Retention is irrelevant for a one-time transaction business | Do not force a retention initiative into the portfolio. |
| 19 | No distinct activation stage exists | Do not invent an activation workstream. |
| 20 | Offer is unproven but team wants creative volume | Consider offer uncertainty as prerequisite; creative output alone is not automatically the strategic answer. |
| 21 | Price sensitivity is asserted from sales anecdotes | Route pricing evidence to `$pricing-monetization`; do not treat anecdotes as verified strategic constraint. |
| 22 | Product is out of stock | Treat inventory/capacity as a growth constraint; do not prescribe more demand generation. |
| 23 | Sales team cannot handle current lead volume | Surface sales capacity/quality constraint before increasing acquisition. |
| 24 | Fulfillment delays are causing refunds | Route operational defect; marketing plan may prioritize fixing it but cannot pretend marketing owns implementation. |
| 25 | Compliance approval blocks a campaign | Treat as dependency/constraint; do not bypass it for calendar completion. |
| 26 | Team wants “do SEO, Meta, Google, email, CRO” | Require choices, sequencing, evidence, owners, and explicit non-priorities. |
| 27 | Plan has 35 equally high-priority tasks | Reject as backlog rather than strategy; force tradeoffs and opportunity cost. |
| 28 | High-impact idea has no evidence and a verified smaller defect exists | Distinguish speculative upside from verified defect; do not rank them as equivalent certainty. |
| 29 | Small research study could unlock a major allocation decision | Allow an `explore` or `build-capability` initiative to outrank modest execution work. |
| 30 | Team wants a numerical ICE/RICE-style score with invented inputs | Reject fabricated precision; expose uncertainty or use directional comparison. |
| 31 | User requires a numerical scoring model | Provide transparent weights/ranges/sensitivity and preserve evidence quality. |
| 32 | A plan item has no owner | Do not mark it execution-ready; assign specialist/implementation owner or keep dependency open. |
| 33 | Growth strategy prescribes exact Meta bid changes | Route platform mechanics to `$meta-ads`; strategy owns priority, not channel control. |
| 34 | Growth strategy prescribes Google budget increase | Route readiness and controlled expansion to `$optimization-scaling`. |
| 35 | Paid campaign is strategically important but fails scaling readiness | Keep strategic priority if appropriate, but do not expand until scaling gates pass. |
| 36 | Scaling gates pass but CRO issue has larger verified opportunity | `$growth-strategy` may prioritize CRO over paid expansion; scaling readiness does not force portfolio priority. |
| 37 | Team approves the growth plan | Do not treat plan approval as approval for budgets, pricing, tracking, campaigns, site, or customer-state mutations. |
| 38 | Initiative is listed as approved in plan but implementation owner has not acted | Keep exact state `approved`/`proposed`, not implemented. |
| 39 | Initiative launched yesterday | Do not mark validated before decision window and guardrails mature. |
| 40 | Null experiment result | Preserve as learning; update opportunity confidence rather than deleting it from history. |
| 41 | Experiment contradicts key strategy assumption | Trigger review/rebalance before continuing calendar plan unchanged. |
| 42 | Plan assumptions become stale after major market change | Mark/review strategy; do not follow stale roadmap because dates remain. |
| 43 | Pricing changes materially mid-plan | Treat as potential strategic/economic boundary and review dependent priorities. |
| 44 | Offer changes materially mid-plan | Review dependent acquisition/creative/CRO assumptions instead of assuming transfer. |
| 45 | Conversion lag is 45 days but plan reviews performance weekly | Match strategic review to lag; weekly diagnostics may continue without premature portfolio reversal. |
| 46 | Subscription retention cohort is immature | Do not allocate heavily from predictive LTV alone; preserve immaturity and uncertainty. |
| 47 | Lead-generation sales cycle is six months | Use qualified pipeline/maturation evidence and a suitable horizon; do not force ecommerce-style weekly revenue decisions. |
| 48 | Seasonal business has one annual peak | Align plan and learning windows to seasonality; do not apply generic monthly cadence. |
| 49 | New channel has long SEO-style learning lag | Compare time-to-learn against decision horizon and opportunity cost rather than excluding it automatically. |
| 50 | Two initiatives change the same outcome simultaneously | State causal contamination risk; route experiment design if learning is decision-critical. |
| 51 | Two independent initiatives can run without capacity/measurement conflict | Allow parallel work; sequencing is not required to be strictly serial. |
| 52 | Team wants to copy a competitor’s channel mix | Reject as proof; competitor mix is context only. |
| 53 | External benchmark says best brands spend X% on marketing | Treat as external heuristic/context, not a budget mandate. |
| 54 | User asks “which channel should get the next dollar?” | `$growth-strategy` owns cross-functional portfolio priority; channel/scaling owners supply marginal evidence. |
| 55 | User asks only “can we increase this Meta campaign budget?” | Route primary ownership to `$optimization-scaling`, not growth strategy. |
| 56 | User asks “why did revenue fall yesterday?” | Route primary ownership to `$performance-diagnostics`; growth strategy joins only if diagnosis changes portfolio priority. |
| 57 | User asks for recurring weekly plan execution | `$growth-strategy` owns priorities; `$marketing-operations` owns the recurring loop/state/runtime. |
| 58 | User asks for executive summary of an existing approved strategy | `$marketing-reporting` owns communication; growth strategy does not need to recreate the plan. |
| 59 | Main blocker is product reliability outside Marketing OS | State the non-marketing constraint and route to actual implementation owner rather than inventing a marketing fix. |
| 60 | Evidence is too weak to select among major bets | Valid output is protect current performance plus the smallest decision-changing research/test, with explicit uncertainty and review trigger. |

## Review criteria

A passing implementation should consistently preserve: named business outcome and baseline; justified horizon; system-level constraint diagnosis; specialist evidence/ownership; explicit portfolio tradeoffs and non-priorities; economics/capacity/lag; reversible learning; scaling boundaries; exact state; plan revision history; and separate live-change authorization.