<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Optimization and Scaling

## Skill: $optimization-scaling

**Use when:** Determine whether paid-media campaigns are ready to scale, choose a controlled scaling mode, model marginal economics, and define hold or rollback rules; not for automatic spend, bid, audience, or campaign changes.

Primary knowledge type: methodology. Classify supporting models, strategies, tactics, techniques, templates, heuristics, and evidence with `KNOWLEDGE-TAXONOMY.md`.

Scaling means increasing a verified primary business outcome while keeping named economics, quality, capacity, measurement, and risk guardrails acceptable. More spend, attributed revenue, conversions, or ROAS alone does not prove scaling.

### Required context

Collect the business model and outcome; account/channel scope; dates and comparison; source of truth; spend and conversion lag; revenue or lead-stage definitions; contribution inputs or qualified-outcome economics; campaign/entity evidence; demand opportunity; creative, funnel, inventory/sales, cash-flow, and operational capacity; current platform controls; and authorization scope.

### Method

1. Apply the proof standard and label current evidence.
2. Run the readiness gates. Stop when a verified blocker makes scaling unsafe.
3. Model economics and marginal efficiency; expose missing inputs and sensitivity ranges.
4. Diagnose the binding constraint and select a scaling mode using constraints and modes.
5. Define one interpretable scaling hypothesis, exact entity/change, maximum exposure, decision window, conversion-lag allowance, business metric, guardrails, hold rule, and rollback condition.
6. Use controlled steps to test, wait for maturity, evaluate marginal business outcome, and decide `increase`, `hold`, `continue evidence`, `apply`, `rollback`, `switch mode`, `de-scale`, or `inconclusive`.
7. Verify the result against the business source of truth and record scope, proof level, exceptions, and replication status.

Read only the relevant conditional reference: portfolio allocation, creative capacity, Google Ads, Meta Ads, business-model overlays, guardrails and recovery, or budget and outcome pacing when spend or outcome is off an already-approved plan within the current period. For current platform controls, apply `PLATFORM-CURRENCY.md` and confirm account visibility.

### Decision rules

- Never use a universal budget-increase percentage or cadence.
- Do not scale while measurement integrity, primary business outcome, or decision-critical economics are unknown.
- Evaluate blended and marginal performance separately; platform attribution is not incrementality or realized revenue.
- Increasing a budget is a tactic, not the scaling strategy. Address the binding constraint.
- Preserve valuable brand, query, product, audience, and market coverage unless evidence supports removal.
- Prefer one reversible, interpretable change; account for conversion lag and relevant demand cycles.
- Forecasts and platform recommendations are inputs, not guarantees or authorization.
- A tactic is “proven” only for its stated account, scope, period, and evidence level.
- All live budget, bid, target, audience, campaign, conversion, coverage, or status changes require explicit approval.
- A pacing correction inside an already-approved plan is not a scaling decision; a correction that would exceed the approved plan is, and requires the full gate set.
- Predictive lifetime value or payback from `$retention-economics` may inform economics but does not by itself satisfy the marginal-evidence gate; it still requires the proof standard.

### Output

Return: scaling objective; primary knowledge type; proof level; readiness verdict and failed gates; source-of-truth outcome; economics and sensitivity; binding constraint; chosen scaling mode; protected coverage; exact proposed step; primary metric; guardrails; decision window/lag; hold/rollback rules; owner and approval; unknowns; exact status.

### QA

Verify formulas and cost scope, sample and lag maturity, account/platform availability, marginal versus blended evidence, downstream quality, operational capacity, maximum downside, one interpretable variable, source-of-truth verification, and authorization. Do not call scaling successful until the business result is verified.

### Reference: budget and outcome pacing ($optimization-scaling)

### Budget and Outcome Pacing

Tracks spend and outcomes against plan within a period, and reforecasts when variance appears. An operational-control process, distinct from the economic models in `$retention-economics` — pacing asks whether the current period is on track; lifetime value and payback ask whether a customer relationship is profitable.

#### What to track

Spend-to-plan variance by period-to-date, with the plan's own seasonality curve rather than a straight-line daily average — most accounts do not spend evenly across a month.

Outcome-to-plan variance for the primary business outcome, at the source-of-truth profit level, not a platform-attributed proxy.

Time remaining in the period versus budget or outcome remaining, expressed as required daily run-rate to hit plan.

#### Method

1. Establish the plan's expected spend and outcome curve for the period, not just its total — a plan flat across the month reads as behind-pace in a business with a weekend or end-of-month skew.
2. Compare actual to planned at the current point in the period, in both spend and outcome, separately. Spend can be on-pace while outcome is not, and the reverse.
3. Attribute variance to a cause before recommending a response: demand shortfall, delivery or auction pressure, a tracking defect, a promotion, a capacity constraint, or a genuine change in performance. An unattributed variance should not trigger a budget change.
4. State the reforecast: given current pace and its cause, what the period is now expected to deliver, and by when that becomes clear enough to act on.
5. Distinguish a pacing correction (spend adjusted to hit an already-approved period plan) from a scaling decision (increasing the plan itself). Pacing corrections within an approved budget do not require new scaling authorization; changing the plan does.

#### Rules

- Do not correct pacing by raising budget before attributing the variance to a cause. A demand shortfall will not be fixed by more budget; a delivery constraint might be.
- Do not treat early-period variance as decisive. State the point in the period at which the variance becomes statistically meaningful given typical day-of-week and conversion-lag noise.
- Outcome pacing must use the source-of-truth definition from `$marketing-intake`; do not pace against a platform-reported conversion count that has not been reconciled.
- A pacing correction is bounded by the already-approved plan. Any correction that would exceed the approved budget or period is a scaling decision and requires the `optimization-scaling` gates and explicit approval, not a pacing note.
- Reforecast on a stated cadence appropriate to the business's decision cycle; do not reforecast so frequently that noise is mistaken for a trend.
- Record every reforecast with its date, cause, and resulting revised expectation, so a pattern of repeated reforecasting itself becomes visible as a signal.

#### Output

Plan curve; actual-to-plan variance in spend and outcome, separately; attributed cause; required run-rate to close the gap; reforecast with date and cause; whether the situation calls for a pacing correction within the approved plan or a scaling decision requiring new authorization; exact status.

### Reference: business overlays ($optimization-scaling)

### Business-Model Overlays

Apply the common scaling gates, then use the business-specific outcome and constraints.

#### Ecommerce

Primary evidence: paid/fulfilled orders, net revenue, named contribution profit, new-customer economics, refunds/cancellations, product/variant stock, fulfillment, and cash timing. Diagnose by product and marginal contribution, not blended ROAS.

#### Lead generation and services

Primary evidence: defined lead stages, contact/qualification/appointment/opportunity/close rates, realized value, response time, invalid leads, sales and service capacity. Scale the deepest reliable feedback signal, not raw leads.

#### SaaS and subscription

Primary evidence: activated/qualified accounts, paid conversion, net recurring revenue, gross margin, churn/retention, expansion, payback, cohort maturity, sales/onboarding capacity. Treat predicted LTV as a model, not realized value.

#### Local services

Primary evidence: serviceable geography, appointment capacity, qualification, show/close rate, realized job value, travel/service cost, response time, and schedule saturation.

#### Nonprofit/donations

Primary evidence: verified donations, net funds, donor acquisition cost, recurrence/retention, restricted-fund or grant constraints, mission capacity, and compliance. Do not treat form or thank-you events as payment proof.

#### Apps, marketplaces, and omnichannel

Define the deepest verified outcome, take rate/margin, fraud/refund, supply-side capacity, cohort lag, offline overlap, and incrementality question before adapting tactics.

### Reference: constraints and modes ($optimization-scaling)

### Constraints and Scaling Modes

Identify the binding constraint before selecting a tactic: measurement, economics, demand, auction, budget, bid/optimization, eligibility/policy, feed, inventory, audience, creative, offer, landing/checkout/form, sales, fulfillment, cash flow, geography, compliance, or learning/sample.

Choose the smallest mode that addresses it:

- **Vertical budget:** more exposure inside existing coverage.
- **Bid-target:** change bidding pressure or economic target; separate from budget effects.
- **Horizontal demand:** expand queries, products, audiences, placements, geographies, languages, devices, schedules, or buying situations.
- **Creative:** expand distinct evidence-backed angles, concepts, proof, formats, creators, or awareness coverage.
- **Product/service:** allocate toward economically and operationally supportable offers.
- **Market:** enter a new geography, segment, role, use case, or buying situation.
- **Funnel:** increase qualified post-click capacity or reliability.
- **Value:** optimize toward higher-quality, higher-contribution, or deeper verified outcomes.
- **Portfolio:** reallocate the next unit of budget by marginal opportunity and strategic protection.
- **Operational:** expand stock, fulfillment, sales, support, onboarding, or cash capacity.
- **Structural:** change architecture only when structure blocks control, measurement, learning, or allocation.
- **De-scaling/recovery:** reduce exposure and verify restoration after a breach.

Budget is not the constraint when a campaign cannot spend its existing budget. High blended ROAS does not identify the next scalable mode. State why rejected modes do not address the constraint.

### Reference: controlled steps ($optimization-scaling)

### Controlled Scaling Steps

1. Establish a mature comparable baseline and protected state.
2. Write one falsifiable scaling hypothesis tied to the primary business outcome.
3. Specify exact entity, current/proposed state, one major variable, maximum exposure, owner, approval, rollback path, and expected mechanism.
4. Predefine primary metric, business and quality guardrails, minimum practical effect, decision window, conversion-lag allowance, and invalidity conditions.
5. Choose the strongest feasible design: platform experiment, holdout, geo test, cohort split, campaign/creative split, portfolio allocation test, or bounded sequential step.
6. Avoid contaminating control and treatment; document unavoidable concurrent changes.
7. Wait for the predefined maturity condition; do not decide from partial lag or one unusual day.
8. Evaluate total, blended, marginal, incremental/counterfactual evidence, mix, cannibalization, downstream quality, operational cost, and uncertainty.
9. Decide `increase`, `hold`, `continue-evidence`, `apply`, `rollback`, `switch-mode`, `de-scale`, or `inconclusive`.
10. Verify the business source of truth, record proof level and scope, and replicate when risk warrants it.

There is no universal safe percentage or cadence. Step size depends on downside, volume, lag, auction/demand volatility, bid strategy, capacity, reversibility, and learning value.

### Reference: creative capacity ($optimization-scaling)

### Creative Capacity

Map spend and business outcomes to stable creative IDs and distinguish angle, hook, concept, asset, ad, format, and placement adaptation.

Inspect coverage by customer situation, awareness, angle, objection, proof, product, format, placement, and market; spend concentration; production lead time; approval/claim capacity; and result distribution.

Creative-scaling decisions:

- **Expand:** a concept has business-verified evidence and additional expression/coverage opportunity.
- **Refresh:** the message remains valid but delivery/attention evidence deteriorates within a scoped audience.
- **Replace:** the core hypothesis is unsupported or downstream quality is unacceptable.
- **Hold:** sample, lag, or identity mapping is insufficient.
- **Retire/reactivate:** use explicit evidence and context; never use age alone.

Rising frequency plus worsening response is a pattern, not proof of fatigue. Check audience, auction, spend distribution, destination, offer, and business outcome. Creative quantity is not scaling unless it increases useful learning or verified outcome capacity.

### Reference: economics ($optimization-scaling)

### Scaling Economics and Marginal Efficiency

Use verified inputs and state whether tax/shipping revenue and each cost are included.

#### Ecommerce

`Contribution profit after media = gross sales - discounts - refunds - COGS - variable fulfillment - payment fees - other scoped variable costs - media spend`

Or, when net revenue already includes discounts/refunds:

`Contribution profit after media = net revenue - COGS - variable fulfillment - payment fees - other scoped variable costs - media spend`

Never subtract discounts or refunds twice.

`Break-even ROAS = 1 / contribution margin before media` when revenue and margin bases match.

`Break-even CPA = contribution profit before media per acquired order/customer` under the stated acquisition definition.

#### Lead generation

`Expected lead value = qualification rate × close rate × realized customer value`, adjusted for stage definitions, lag, invalid leads, sales cost, and servicing costs in scope.

#### Marginal model

- Blended efficiency uses all scoped spend/outcomes.
- Marginal efficiency uses the change in outcome divided by the change in spend between comparable states.
- Incremental outcome requires a credible counterfactual; marginal and attributed are not synonyms.
- Marginal contribution after media is the additional scoped contribution minus additional media and operational costs.

Model a sensitivity range when costs, lag, or rates are uncertain. Do not interpolate beyond supported demand or treat a platform forecast as realized business impact. Include cash-flow timing, inventory/sales capacity, cannibalization, and opportunity cost when material.

### Reference: google scaling ($optimization-scaling)

### Google Ads Scaling

Apply `$google-ads`, its relevant Search/Shopping/PMax reference, and the current platform registry. Confirm account-visible controls before an account-specific plan.

#### Search

Separate brand/protected demand and non-brand acquisition. Inspect query/keyword intent, match source, budget and rank constraints, impression opportunity, bid strategy, marginal CPC/CPA/value, location/device/schedule, landing alignment, and conversion-goal integrity.

Potential modes: budget, bid-target, query/keyword coverage, current keywordless matching/AI layer, geography, landing alignment, or creative/assets. Exact-match or protected coverage must not be sacrificed without evidence.

#### Shopping and Performance Max

Inspect item ID, product economics, stock, feed eligibility, price/promotion, listing groups, product/query evidence, asset groups, search themes, URL/brand/query controls, and available channel reporting. Do not infer unseen channel allocation.

Potential modes: profitable product coverage, inventory-aware allocation, asset/message coverage, demand controls, or bounded budget/bid tests. Campaign totals cannot hide unprofitable items.

#### Planning and experiments

Performance Planner, simulators, recommendations, experiment guidance, and platform forecasts are evidence inputs. They do not prove marginal contribution, incrementality, account eligibility, or authorization. Disable any automatic application that conflicts with the approved experiment contract.

Live budgets, bids, targets, conversion goals/actions, negatives, brand/URL controls, product coverage, experiments, or status changes require explicit approval and post-change verification.

### Reference: guardrails and recovery ($optimization-scaling)

### Guardrails, De-scaling, and Recovery

Predefine scoped thresholds rather than inventing universal benchmarks.

- **Financial:** allowable CPA, minimum marginal contribution/qualified value, payback, cash exposure, maximum test loss.
- **Customer quality:** refund/cancel/invalid rate, qualification, close rate, complaints, support burden, retention where mature.
- **Delivery:** spend/creative concentration, query/product/audience/placement/geographic quality, protected coverage.
- **Operations:** stock, fulfillment time, sales response, appointments/onboarding, support, payout timing.
- **Measurement:** event loss/duplication, value/currency, conversion-role/window, consent, lag, reconciliation.

On breach: contain the smallest affected scope; preserve evidence; distinguish measurement defect from performance harm; stop further scaling; execute the approved rollback; verify persistence/recovery in the business source of truth; then decide whether to resume, redesign, or de-scale.

De-scaling must protect valuable coverage and learning. Avoid broad pauses when a product, query, creative, market, or measurement defect is isolated. Report exact states: proposed, approved, saved, live, processing, rolled back, or recovery-verified.

### Reference: meta scaling ($optimization-scaling)

### Meta Ads Scaling

Apply `$meta-ads`, the relevant acquisition/retargeting reference, and the current platform registry. Confirm account-visible objective, conversion location, performance goal, dataset/event, attribution, audience, placement, and automation controls.

Inspect delivery and spend concentration, CPM, reach/frequency, outbound response, landing-page views, destination conversion, business outcome, new-customer/lead quality, creative IDs and concept coverage, audience source/window/exclusions, placement/geography, and operational capacity.

Potential modes: controlled budget allocation, audience/market coverage, documented Advantage+ controls, placements, creative concepts/formats, catalog/product sets, value or qualified-event optimization, funnel, or operational capacity.

Rules:

- Broad, lookalike, interest, Custom Audience, and automated audience approaches are hypotheses, not doctrines.
- Retargeting efficiency does not prove incrementality.
- Rising frequency does not by itself prove fatigue.
- A high platform ROAS does not prove profitable marginal new-customer growth.
- Preserve stable entity and creative IDs for interpretable learning where practical.
- Do not fragment ad sets or duplicate campaigns without a distinct constraint/hypothesis.

Live budgets, bid strategy/controls, audiences, exclusions, placements, ads, experiments, or status changes require explicit approval and post-change verification.

### Reference: portfolio allocation ($optimization-scaling)

### Portfolio Allocation

Evaluate where the next unit of budget should go using marginal contribution or qualified-value potential, evidence strength, demand opportunity, measurement integrity, capacity, reversibility, time to learn, cannibalization, strategic importance, inventory/sales constraints, creative capacity, and maximum downside.

Classify each entity: `protect`, `maintain`, `diagnostic-test`, `increase`, `expand`, `hold`, `reduce`, `exit`, or `recovery-watch`.

Rules:

- Separate protected brand/demand capture from non-brand acquisition before comparing efficiency.
- Do not sum overlapping platform attribution as incremental value.
- Do not move all budget to the highest blended ROAS; estimate marginal opportunity and coverage loss.
- Preserve a control or stable baseline when it materially improves learning.
- Include opportunity cost and operational bottlenecks.
- Reallocation requires the same approval, exposure, and rollback contract as a budget increase.

### Reference: proof standard ($optimization-scaling)

### Scaling Proof Standard

Assign the highest supported level; do not skip levels by assertion.

| Level | Status | Required meaning |
|---|---|---|
| S0 | Unverified | Recommendation, assumption, or claim without decision-ready account evidence |
| S1 | Officially documented | Platform capability documented; availability and impact unverified |
| S2 | Account-visible | Capability or condition observed in the scoped account and date |
| S3 | Analytically supported | Historical evidence supports a hypothesis; causality not isolated |
| S4 | Experimentally validated | Controlled comparison supports the mechanism within the test scope |
| S5 | Business-verified | Source of truth confirms an acceptable commercial or qualified result |
| S6 | Replicated | Result survives another meaningful period, cohort, entity, or scaling step |
| S7 | Currently scalable | Replicated result remains within current economics, capacity, measurement, and risk gates |

“Proven” means proven for the named account, scope, period, outcome definition, and evidence standard. Platform documentation, forecasts, recommendations, attributed results, or statistical significance alone do not establish business-verified scalability.

For high-risk changes, require stronger replication, smaller exposure, or credible incrementality evidence. Record contradictory results and regression conditions.

Credible incrementality evidence means a graded causal result, not platform attribution. S4 requires a controlled comparison at C3 or above on the causal evidence ladder; `$tracking-measurement` owns method selection and grading. Platform-attributed performance is C0 and cannot raise a claim above S3 regardless of volume or consistency.

### Reference: readiness ($optimization-scaling)

### Scaling Readiness

Return a pass, fail, or decision-changing unknown for each gate.

1. **Business outcome:** source of truth, revenue/lead stage, new-customer definition, refunds/cancellations, cohort/date basis.
2. **Measurement:** event correctness, values/currency, deduplication, bidding-signal role, attribution, consent, reconciliation, conversion lag.
3. **Economics:** named contribution level or qualified-outcome value, break-even and allowable acquisition cost, cash exposure.
4. **Stability:** adequate sample and cycles, mature lag, no unresolved promotion, tracking, policy, inventory, or simultaneous-change distortion.
5. **Opportunity:** additional eligible demand or coverage; distinguish budget, rank, demand, audience, product, and market constraints.
6. **Creative:** concept diversity, spend concentration, evidence-backed refresh pipeline, production capacity.
7. **Funnel:** destination reliability, qualified conversion, message scent, checkout/form, offer, downstream quality.
8. **Operations:** inventory, fulfillment, sales response, support, appointments/onboarding, cash and payout timing.
9. **Risk and authorization:** maximum exposure, owner, metric, guardrails, hold/rollback, approval.

Verdicts: `not-ready-blocked`, `not-ready-unknown`, `diagnostic-test-ready`, `limited-test-ready`, `controlled-scale-ready`, `portfolio-expansion-ready`, `hold`, `rollback-required`, `de-scale-required`, or `recovery-verification`.

Do not average gate scores into a green verdict when one critical gate fails. Measurement, economic, legal/policy, capacity, or authorization failures are blocking gates.
