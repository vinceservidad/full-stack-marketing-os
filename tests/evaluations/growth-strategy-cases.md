# Growth Strategy Behavioral Evaluations

Owner: `$growth-strategy`.

These cases test routing, evidence discipline, constraint diagnosis, opportunity prioritization, specialist ownership, planning governance, and the Growth Strategy versus Scaling boundary.

| # | Case | Expected behavior |
|---|---|---|
| 1 | “Make a full marketing plan” with no objective or economics | Route to intake first; do not fill a generic channel checklist. |
| 2 | User asks “where should we focus?” with decision-ready context | `$growth-strategy` owns the integrated priority decision. |
| 3 | Plan starts with Meta, Google, SEO, email because they are common | Reject channel-first construction; start from objective and constraint. |
| 4 | Template requires exactly a 90-day plan | Treat 90 days as optional convenience, not universal horizon. |
| 5 | Plan allocates 70/20/10 by default | Reject universal allocation ratio. |
| 6 | Plan forces AARRR stages for every business | Use only if decision-relevant; do not force lifecycle taxonomy. |
| 7 | Plan requires TOFU/MOFU/BOFU work in every stage | Reject completeness theater; include only needed work. |
| 8 | Competitor is on TikTok so TikTok becomes a priority | Competitor presence is context, not proof of channel opportunity. |
| 9 | CTR is lowest metric, so creative is called the binding constraint | Diagnose relationship to business outcome before naming constraint. |
| 10 | Revenue fell but source definitions changed | Measurement dependency precedes growth-constraint claim. |
| 11 | ROAS is strong but contribution is negative | Commercial outcome/economics govern; do not call acquisition healthy. |
| 12 | Acquisition is efficient but inventory is capped | Surface inventory/capacity as possible binding constraint. |
| 13 | Lead volume is strong but sales capacity is exhausted | Surface sales capacity; do not prescribe more lead generation by default. |
| 14 | Activation failure is causing later churn | Treat activation as upstream cause candidate; preserve owner split. |
| 15 | Retention economics make new acquisition uneconomic | Retention can block acquisition expansion; route retention dependencies. |
| 16 | Two constraints have evidence | Name binding constraint for horizon and secondary dependency; do not collapse causality. |
| 17 | Constraint evidence is weak | Label plausible/unknown rather than “the problem is definitely X.” |
| 18 | Verified checkout defect exists | Protect/fix verified blocker before speculative growth bets. |
| 19 | Legal/compliance issue exists | Protect/fix takes priority over growth experiments. |
| 20 | Measurement defect prevents comparison | Repair/reconcile before strategic allocation. |
| 21 | Opportunity list includes every available tactic | Require constraint → mechanism → business effect connection. |
| 22 | New channel has no audience-channel fit evidence | Classify as weak/plausible or reject, not priority by novelty. |
| 23 | Existing channel has validated demand and unused capacity | May be a strategic opportunity, subject to specialist/scaling gates. |
| 24 | Opportunity uses precise composite score built from guesses | Reject false precision; use explicit trade-offs or qualitative tiers. |
| 25 | User asks for 10 priorities | Do not force count; stop when capacity/focus becomes diluted. |
| 26 | Only one verified blocker exists | One priority can be the correct strategy. |
| 27 | Diversified business has independent constraints | Multiple bets allowed when scope/capacity support them. |
| 28 | Plan has tasks but no strategic choice | Reject task list as strategy; require thesis/mechanism/priorities. |
| 29 | “Launch Meta campaign” is presented as the strategy | Treat as implementation task under a strategic bet. |
| 30 | Plan omits non-priorities | Require important intentional exclusions/reconsideration triggers. |
| 31 | Strategy changes offer terms itself | Route proposition decision to `$offer-strategy`. |
| 32 | Strategy sets price tiers itself | Route exchange structure to `$pricing-monetization`. |
| 33 | Strategy defines activation event itself | Route first-value definition to `$activation`. |
| 34 | Strategy decides churn-save discount itself | Retention strategy owns intervention; pricing owns discount architecture. |
| 35 | Strategy dictates Google bidding mechanics | Route technical channel decision to `$google-ads`. |
| 36 | Strategy dictates Meta placements | Route platform decision to `$meta-ads`. |
| 37 | Strategy selects a landing-page redesign mechanism | CRO owns the page decision; Growth Strategy may prioritize the workstream. |
| 38 | Strategy claims experiment caused lift from simple before/after | Route causal validity to `$tracking-measurement`. |
| 39 | Strategy chooses channel role but not live budget | Allowed; channel role is business-level portfolio direction. |
| 40 | Strategy sets live paid-media budget increase | Reject; route scaling step to `$optimization-scaling`. |
| 41 | Paid media is proven but question is “is scaling it our best opportunity?” | `$growth-strategy` owns priority versus alternatives. |
| 42 | Question is “can this campaign safely take 30% more budget?” | `$optimization-scaling` owns readiness and controlled step. |
| 43 | Growth Strategy says scale because ROAS is high | Reject; scaling proof/marginal gates still apply. |
| 44 | Forecast says strategy will add $1M revenue | Require assumptions/scenarios/confidence; no guarantee. |
| 45 | Forecast range is based on unsupported benchmark | Label unsupported and do not use as decision-grade evidence. |
| 46 | Funding stage used to prescribe marketing spend | Treat as heuristic/context at most, not universal budget rule. |
| 47 | “Best practice says first hire a strategist” | Do not convert external heuristic into operating fact. |
| 48 | Strategy uses a 12-month roadmap for a 2-week decision | Match horizon to decision and lag, not template convention. |
| 49 | Enterprise sales cycle is six months | Review/maturity windows reflect long lag. |
| 50 | Ecommerce conversion signal matures quickly | Shorter review may be appropriate; no mandatory quarterly delay. |
| 51 | Strategy reads stale Marketing Context as current | Mark dependency/staleness; source artifact governs. |
| 52 | Marketing Context conflicts with newer specialist evidence | Newer source decision artifact governs until context updates. |
| 53 | Strategic bet supported by one weak case study | Keep as low-confidence hypothesis; no universal transfer. |
| 54 | Strategy treats customer quote as market prevalence | Preserve qualitative evidence limits. |
| 55 | Experiment success metric is CTR while profit can be measured | Use business outcome/validated leading indicator; CTR is diagnostic. |
| 56 | Decision rule is invented after result is seen | Flag post-hoc rule; do not present as pre-specified validation. |
| 57 | A strategy review is triggered by competitor launch | Review evidence; trigger does not itself require strategy change. |
| 58 | New evidence changes the binding constraint | Revise strategy with change log; preserve prior decision/history. |
| 59 | Strategy history is rewritten to make old forecast look correct | Reject hindsight rewrite; preserve original assumptions. |
| 60 | Approved strategy is described as implemented | Keep exact status; approval is not execution. |
| 61 | Workstream is live but outcome window is immature | `in execution`/under review, not successful. |
| 62 | Recurring strategy review loop is documented only | Route loop to `$marketing-operations`; do not call it active. |
| 63 | Executive strategy update is requested | `$marketing-reporting` communicates; Growth Strategy owns priority decisions. |
| 64 | Strategy includes unsupported capacity assumptions | Label assumptions and identify capacity evidence needed. |
| 65 | Cash constraint makes otherwise-good expansion unsafe | Surface financing/cash constraint rather than forcing marketing action. |
| 66 | Product/service failure is the blocker | Surface implementation owner; marketing cannot message around the defect. |
| 67 | One-time purchase business has no meaningful retention lever | Do not force retention workstream into the plan. |
| 68 | Business has no distinct activation stage | Do not force activation workstream. |
| 69 | Strong brand search masks weak nonbrand acquisition | Route diagnosis; do not treat aggregate channel result as sufficient strategy evidence. |
| 70 | Strategy calls tactic “proven” from competitor visibility | Reject; competitor visibility is not performance evidence. |
| 71 | Strategy chooses a market solely from keyword volume | Require market/ICP/JTBD/commercial evidence; search volume alone insufficient. |
| 72 | Opportunity would create irreversible rebuild before testing mechanism | Prefer smaller reversible validation where feasible. |
| 73 | User wants every idea executed simultaneously | Protect interpretability and capacity; sequence rather than flood. |
| 74 | Priority bet has unresolved dependency on pricing | Mark dependency and route pricing owner before downstream commitment. |
| 75 | Priority bet becomes contradicted by experiment | `revise`, `kill`, or defer based on evidence; preserve learning. |
| 76 | Null experiment result | Preserve inconclusive learning; do not automatically kill whole strategy. |
| 77 | Strategy has high impact but no feasible implementation capacity | Defer or resolve capacity; do not pretend priority equals executable. |
| 78 | Low-impact quick win distracts from verified revenue leak | Verified commercial blocker outranks cosmetic win. |
| 79 | User asks for benchmark-based channel mix | Explain no universal mix; use evidence and capacity. |
| 80 | User asks Growth Strategy to publish/change live assets | No plan authorizes mutation; hand off with approval boundary. |
