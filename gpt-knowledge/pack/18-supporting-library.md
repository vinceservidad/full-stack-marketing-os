<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Frameworks, Playbooks, Workflows, and Templates

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `frameworks/constraint-identification.md`

# Scaling Constraint Identification

## Knowledge metadata

- Primary type: framework
- Secondary type: diagnostic model
- Decision: which constraint must be addressed before more growth is supportable
- Evidence status: hypothesis until localized with evidence
- Freshness: account-current

Localize the binding constraint across measurement, economics, demand, auction, budget, bid/optimization, eligibility/policy, feed, inventory, audience, creative, offer, destination, sales, fulfillment, cash flow, geography, compliance, and learning/sample.

Select a scaling mode that directly addresses the constraint and state why rejected modes do not. More budget cannot solve an inability to spend, weak unit economics, invalid measurement, exhausted creative, broken funnel, unavailable stock, or full sales capacity.

## Source: `frameworks/controlled-scaling.md`

# Controlled Scaling Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: methodology / process
- Decision: continue, hold, apply, rollback, switch mode, de-scale, or remain inconclusive
- Evidence status: stable operating method; result remains account-specific
- Freshness: stable; platform implementation requires a live check

```text
Business truth → readiness → economics → constraint → mode → bounded step
→ maturity → marginal evaluation → business verification → replicate or stop
```

One step defines an exact entity/change, one major variable, maximum exposure, control/comparison, primary business metric, quality/operational guardrails, conversion-lag allowance, invalidity conditions, owner, authorization, and rollback.

There is no universal percentage or cadence. Step size follows downside, volume, lag, volatility, capacity, reversibility, and learning value.

## Source: `frameworks/creative-strategy.md`

# Creative Strategy Framework

Verified Research → Audience Situation → Pain / Desire / JTBD → Awareness → Current Belief → Required Belief Shift → Insight → Angle → Creative Mechanic → Concept → Hook → Visual Format → Persuasion → Proof → Offer → CTA → Test Hypothesis → Test → Iterate → Scale

This is a decision map, not a claim that buyers move through a fixed linear sequence. Treat awareness, belief states, mechanic fit, hook fit, and format fit as observed evidence or clearly labeled hypotheses, and use account learning to override default assumptions.

## Creative Evaluation
- Is the source insight grounded?
- Is the audience situation clear?
- Is the pain, desire, or JTBD explicit?
- Does the message match the best-supported awareness and belief state?
- Is the required belief shift supportable with available proof?
- Is the angle a distinct reason to care rather than a hook rewrite?
- Does the creative mechanic define a clear way for the concept to make the angle land?
- Is the concept distinct from the hook and visual format?
- Does the hook preserve the angle and proof boundary?
- Does the visual format serve the mechanic, product, placement, and proof requirement?
- Is there a reason to believe?
- Can the test teach something and be measured against a business outcome?

## Source: `frameworks/experimentation.md`

# Experimentation Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: methodology / process
- Decision: whether a test can produce a valid decision and what scoped learning it supports
- Evidence status: stable operating method
- Freshness: stable; confirm platform-specific implementation separately

A valid experiment connects one decision to one falsifiable hypothesis. A completed experiment becomes durable knowledge only after validity, scope, uncertainty, and transfer limits are recorded.

## Minimum pre-test specification

- Problem and evidence
- Prior relevant learning
- Hypothesis and expected mechanism
- Control and variant
- Population and allocation
- Primary metric and business guardrails
- Required evidence level
- Instrumentation and QA
- Minimum practical effect or decision threshold
- Duration covering relevant cycles and conversion lag
- Stop conditions for harm or invalid data
- Decision rule: ship, iterate, reject, or inconclusive

Avoid repeated peeking, changing several major variables without accepting ambiguity, or declaring a winner from directional noise.

## Post-test learning sequence

1. **Validate execution before direction.** Confirm allocation, treatment fidelity, instrumentation, lag, contamination, duration/sample, and stop-rule adherence.
2. **Classify the result.** Valid-supports, valid-contradicts, valid-inconclusive/null, valid-guardrail-harm, or invalid/compromised.
3. **Record the estimate and uncertainty.** Preserve the primary business outcome, guardrails, decision threshold or MDE, and achieved evidence level.
4. **Separate observation from mechanism.** The measured treatment effect can be valid even when the explanation for it remains an inference.
5. **Make the scoped decision.** Ship, reject, iterate, replicate, collect more data, invalidate/rerun, or stop for harm.
6. **Create a learning record.** Preserve population, surface, geography, period, offer/commercial conditions, platform/product state, contradictions, and what the result does not prove.
7. **Assign transfer status.** Local result → replication candidate → replicated scoped pattern. Conflicting evidence becomes contradicted/unstable rather than being erased.
8. **Generate the next hypothesis only when it resolves valuable uncertainty.** Experiment count and win rate are not objectives by themselves.

A single valid test may support a local implementation when the decision rule and authorization allow it. It does not establish a universal best practice. Post-hoc segment cuts, external case studies, competitor examples, and platform benchmarks are hypothesis inputs unless independently validated in the relevant scope.

Use `templates/experiment.md` (source: `templates/experiment.md`) before launch and `templates/experiment-learning.md` (source: `templates/experiment-learning.md`) after conclusion. Detailed knowledge-promotion rules live under `$tracking-measurement` in `references/experiment-learning-system.md`.

## Source: `frameworks/google-ads-full-stack.md`

# Google Ads Full Stack Framework

## Process
Business Economics → Research → ICP → Search Intent → Keyword Strategy → Campaign Architecture → Ad Messaging → Landing Page → Conversion Tracking → Bidding → Optimization → Offline Feedback → Scaling

## Audit Areas
- Account structure
- Search terms and keyword quality
- Match types and negatives
- Ad relevance
- Landing page alignment
- Conversion tracking integrity
- Bid strategy suitability
- Profitability and margins

## Principle
Optimize for business outcomes, not platform metrics alone.

## Source: `frameworks/marginal-economics.md`

# Marginal Economics Framework

## Knowledge metadata

- Primary type: model
- Secondary type: framework / decision rule
- Decision: whether the next unit of spend creates acceptable business value
- Evidence status: calculated from verified scoped inputs
- Freshness: refresh with economics, mix, and conversion maturity

Report total/blended and change/marginal performance separately. The next unit is scalable only when its expected or observed marginal contribution/qualified value, capacity, risk, and uncertainty meet the defined rule.

Show formulas, revenue/cost basis, lag, comparison, confidence/sensitivity, cannibalization, operational cost, and opportunity cost. Attribution is not incrementality; a platform forecast is not observed marginal performance. Missing costs produce a range or unknown, not a profitability verdict.

## Source: `frameworks/measurement-and-evidence.md`

# Measurement and Evidence Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: model / standard
- Decision: whether evidence supports a marketing decision
- Evidence status: stable operating method
- Freshness: stable; metric definitions remain client-specific

## Claim levels

- **Observed:** directly present in a named source and scope.
- **Calculated:** derived with visible formula and inputs.
- **Inferred:** a supported explanation that has not been isolated.
- **Assumed:** needed to proceed and explicitly unverified.
- **Unknown:** missing and potentially decision-changing.

Platform attribution is a model, not a ledger. Reconcile it with storefront, CRM, payment, fulfillment, refund, and cost data according to the decision.

Use the definitions in `GLOSSARY.md` (source: `GLOSSARY.md`). Attribution assigns credit; reconciliation explains differences; incrementality estimates additional outcomes caused; none of these terms is interchangeable.

## Commercial outcomes

Use the furthest trustworthy outcome: contribution profit at a named level, realized revenue, qualified pipeline, closed-won revenue, retention, or another verified business result. If only proxy metrics exist, state the limitation.

## Confidence

Confidence rises with directness, consistency across independent sources, adequate sample, stable definitions, and a plausible mechanism. It falls with attribution overlap, small samples, reporting lag, selection bias, or simultaneous changes.

## Source: `frameworks/meta-ads-full-stack.md`

# Meta Ads Full Stack Framework

## Purpose
A decision system for planning, launching, testing, optimizing, and scaling Meta Ads.

## Process
Research → ICP → Awareness → Offer → Funnel Stage → Audience → Creative Angle → Hook → Format → Copy → Campaign Structure → Tracking → Testing → Optimization → Scaling → Retention

## Core Areas
- Market and customer research
- Customer pain points and desired outcomes
- Creative testing strategy
- Campaign architecture
- Pixel, CAPI, and attribution checks
- Budget allocation
- Performance diagnosis

## Optimization Questions
- Is the problem traffic, conversion, offer, creative, or measurement?
- What evidence supports the change?
- What test will create the most learning?

## Source: `frameworks/portfolio-allocation.md`

# Portfolio Allocation Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: model / strategy
- Decision: where the next unit of marketing budget should go
- Evidence status: account-current analytical decision
- Freshness: refresh with marginal evidence and capacity

Evaluate each entity on marginal business-value potential, evidence strength, demand opportunity, measurement integrity, capacity, reversibility, time to learn, cannibalization, strategic importance, creative supply, opportunity cost, and maximum downside.

Classify: `protect`, `maintain`, `diagnostic-test`, `increase`, `expand`, `hold`, `reduce`, `exit`, or `recovery-watch`.

Do not allocate solely by blended platform ROAS or sum overlapping attribution. Protect valuable branded/strategic coverage and retain a stable comparison when it materially improves learning.

## Source: `frameworks/scale-readiness.md`

# Scale Readiness Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: checklist / decision rule
- Decision: whether and how campaign scaling may be tested
- Evidence status: stable operating method
- Freshness: stable; account/platform details require current verification

Assess nine gates: business outcome, measurement, economics, stability, opportunity, creative, funnel, operations, and risk/authorization.

Return pass, fail, or decision-changing unknown for each. Do not average away a critical failure. Measurement, economics, legal/policy, capacity, or authorization failures block live scaling.

Verdicts: `not-ready-blocked`, `not-ready-unknown`, `diagnostic-test-ready`, `limited-test-ready`, `controlled-scale-ready`, `portfolio-expansion-ready`, `hold`, `rollback-required`, `de-scale-required`, or `recovery-verification`.

## Source: `frameworks/scaling-mode-selector.md`

# Scaling Mode Selector

## Knowledge metadata

- Primary type: framework
- Secondary type: strategy selector
- Decision: which form of scaling addresses the binding constraint
- Evidence status: decision method
- Freshness: stable; channel controls require current verification

Modes: vertical budget, bid-target, horizontal demand, creative, product/service, market, funnel, value, portfolio, operational, structural, and de-scaling/recovery.

Require for each candidate: mechanism, opportunity, economics, evidence, downside, reversibility, time to learn, capacity, protected coverage, and authorization. Prefer the smallest interpretable mode with acceptable expected value. A tactic such as raising budget is not the strategy.

## Source: `frameworks/scaling-proof-standard.md`

# Scaling Proof Standard

## Knowledge metadata

- Primary type: standard
- Secondary type: framework / evidence model
- Decision: what may be called proven and scalable
- Evidence status: operating contract
- Freshness: stable; platform capability evidence remains current-source gated

Use levels S0–S7: unverified, officially documented, account-visible, analytically supported, experimentally validated, business-verified, replicated, and currently scalable.

A claim earns only the highest level directly supported. “Proven” is scoped to the named account, outcome definition, market/entity, period, experiment or comparison, and guardrails. Statistical or platform success without a verified business result is insufficient. Higher downside requires stronger design, replication, and containment.

Never convert a forecast, recommendation, attribution model, case study, or documented capability into guaranteed client impact.

## Source: `frameworks/shopify-cro.md`

# Shopify CRO Framework

Research → Traffic Source → Customer Intent → Product Page → Offer → Trust → Checkout → Retention

Audit:
- Value proposition
- Product page clarity
- Images and creative consistency
- Reviews and proof
- Pricing psychology
- Mobile experience
- Checkout friction
- Upsells and retention

Optimize based on customer behavior and evidence.

## Source: `playbooks/README.md`

# Industry Playbooks

Industry playbooks adapt the Marketing OS to different business models.

## Planned Playbooks

- Ecommerce
- SaaS
- Lead Generation
- Local Services
- Healthcare
- Nonprofit
- Education
- Subscription Businesses

Each playbook follows:

Business Model → Customer Journey → Acquisition → Conversion → Measurement → Scaling

## Source: `playbooks/creative-scaling.md`

# Creative Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: creative strategy / process
- Decision: how creative supply can support additional verified demand
- Evidence status: stable creative identity and business evidence required
- Freshness: account-current

1. Map stable creative IDs to angle, hook, concept, asset, ad, format, adaptation, audience situation, and business outcome.
2. Diagnose concept coverage, spend concentration, proof/claim limits, production lead time, placement/market needs, and destination continuity.
3. Classify each concept `expand`, `refresh`, `replace`, `hold`, `retire`, or `reactivate` with evidence.
4. Form one learning hypothesis; cosmetic variants do not count as strategic capacity.
5. Define production/test allocation, business metric, quality/brand guardrails, maturity, and stop rule.
6. Verify marginal business contribution and learning value—not CTR or asset count alone.

## Source: `playbooks/cross-channel-diagnostic.md`

# Cross-Channel Diagnostic Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / methodology
- Decision: why a cross-channel business outcome changed
- Evidence status: repeatable diagnostic method; account evidence required
- Freshness: stable; platform details require current-source checks

Use when a business outcome changes across more than one platform.

1. Anchor on the business source of truth and one consistent timezone.
2. Check measurement, site availability, inventory, promotions, and operational incidents before attributing the change to media.
3. Decompose demand, traffic mix, auction cost, response, conversion, AOV or lead quality, and margin.
4. Reconcile platform totals without summing overlapping attribution as incremental revenue.
5. Rank channel and non-channel causes, then choose the next data cut or reversible test that best distinguishes them.

## Source: `playbooks/cross-channel-scaling.md`

# Cross-Channel Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: portfolio strategy / process
- Decision: where the next unit of budget creates the best verified business value
- Evidence status: source-reconciled account evidence required
- Freshness: account-current

1. Align source of truth, definitions, timezone, currency, cohort, lag, and cost scope.
2. Reconcile platforms without adding overlapping attributed revenue.
3. Separate demand creation/capture, brand/non-brand, acquisition/retention, and new/returning customer roles.
4. Estimate marginal opportunity, capacity, cannibalization, evidence strength, time to learn, and downside by candidate.
5. Protect strategically necessary coverage and stable comparisons.
6. Choose one bounded reallocation or expansion hypothesis with approval and rollback.
7. Evaluate business-source contribution or qualified pipeline, mix shifts, downstream quality, and channel interaction.
8. Continue, hold, reverse, or switch constraint/mode; do not crown a platform from blended ROAS.

## Source: `playbooks/de-scaling-recovery.md`

# De-scaling and Recovery Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: containment / recovery process
- Decision: how to reduce exposure and verify recovery without destroying valuable coverage
- Evidence status: breach and recovery evidence required
- Freshness: incident-current

1. Identify the breached financial, quality, delivery, operations, measurement, policy, or capacity guardrail.
2. Separate measurement invalidity from genuine business harm.
3. Contain the smallest affected entity while preserving evidence and protected coverage.
4. Execute only the approved rollback or de-scaling step; document prior/current state.
5. Reconcile the business source of truth through the relevant lag/recovery window.
6. Decide `recovered`, `partially recovered`, `not recovered`, `new root cause`, or `insufficient evidence`.
7. Resume only after the failed readiness gate is restored and a new bounded plan is approved.

## Source: `playbooks/ecommerce-growth.md`

# Ecommerce Growth Playbook

## Purpose
A repeatable system for improving ecommerce revenue through acquisition, conversion, retention, and measurement.

## Flow
Research → Offer → Traffic → Conversion → Retention → Scale

## Diagnosis Areas
- Market and customer understanding
- Product-market fit
- Offer strength
- Creative performance
- Landing page conversion
- Checkout friction
- Tracking accuracy
- Customer lifetime value

## Growth Levers
- Increase qualified traffic
- Improve conversion rate
- Increase average order value
- Improve repeat purchase rate
- Reduce wasted spend

## Decision Rule
Do not scale traffic before confirming tracking, economics, and conversion fundamentals.

## Source: `playbooks/ecommerce-scaling.md`

# Ecommerce Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / economics model
- Decision: how to increase ecommerce contribution profit safely
- Evidence status: product/order economics required
- Freshness: business-current

1. Reconcile paid/fulfilled orders, gross or net revenue, discounts/refunds, COGS, variable fulfillment, payment/marketplace fees, media, and new-customer definition.
2. Diagnose contribution by item/product/variant, campaign/query/audience/creative, market, and cohort.
3. Check stock, replenishment, fulfillment, support, cash/payout timing, price/promotion, landing/checkout, and refund/cancellation capacity.
4. Select product, demand, creative, funnel, value, portfolio, or operational scaling—not budget by default.
5. Define break-even and allowable acquisition cost, marginal contribution rule, maximum exposure, inventory/quality guardrails, and rollback.
6. Verify net revenue, contribution after media, new-customer mix, refunds/cancellations, and operational effects before repeating.

## Source: `playbooks/ecommerce.md`

# Ecommerce Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / model
- Decision: how to diagnose and improve ecommerce contribution
- Evidence status: repeatable operating method; economics must be defined
- Freshness: stable; platform controls require current-source checks

1. Establish product, market, inventory, price, promotion, shipping, and return context.
2. Reconcile sessions, orders, revenue, discounts, refunds, taxes, COGS, fulfillment, fees, and media spend.
3. Diagnose by product and contribution, not blended ROAS alone.
4. Protect profitable branded demand and commercially important product coverage.
5. Test offer, creative, traffic, page, and merchandising hypotheses with AOV, refund, and margin guardrails.

Core equation:

If the source begins with gross sales:

`Contribution profit after media = gross sales - discounts - refunds - COGS - variable fulfillment - payment fees - media spend`

If the source begins with net revenue that already reflects discounts and refunds:

`Contribution profit after media = net revenue - COGS - variable fulfillment - payment fees - media spend`

Never subtract discounts or refunds twice. If an input is missing, provide a break-even table or sensitivity range rather than a false profitability verdict. Do not call the result operating profit when fixed operating expenses are unavailable.

## Source: `playbooks/google-ads-audit.md`

# Google Ads Audit Playbook

## Purpose
A structured approach for auditing Google Ads accounts.

## Audit Flow

1. Business economics
- Target CPA or ROAS
- Margin
- Customer value
- Conversion goal

2. Measurement
Check:
- Conversion actions
- Enhanced conversions
- GA4 alignment
- Attribution
- Offline conversion feedback

3. Campaign architecture
Review:
- Search
- Shopping
- Performance Max
- Brand protection
- Prospecting campaigns

4. Search quality
Analyze:
- Search terms
- Keywords
- Match types
- Negative keywords
- Ad relevance

5. Landing page
Review:
- Intent match
- Trust signals
- Offer clarity
- Conversion friction

6. Optimization
Prioritize:
- Data quality
- Budget efficiency
- Creative testing
- Bid strategy decisions

## Output
Provide:
- Account health
- Key issues
- Recommended changes
- Testing plan

## Source: `playbooks/google-ads-scaling.md`

# Google Ads Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / channel strategy
- Decision: which controlled Google Ads scaling step is justified
- Evidence status: account evidence required
- Freshness: live-check for current controls

1. Verify business source of truth, conversion goals/actions and Primary/Secondary status, values, lag, attribution, economics, and current account controls.
2. Separate protected brand/demand capture from non-brand acquisition.
3. Diagnose the constraint by query/keyword, item/product, campaign, geography/device/schedule, budget/rank, bid strategy, feed/eligibility, landing, and inventory.
4. Select one mode: budget, bid-target, query/keyword or current keywordless coverage, product, asset/message, geography, value, or portfolio.
5. Use current official/account-visible planning and experiment tools only as inputs; define the business decision rule separately.
6. Protect exact/proven demand and product coverage; do not infer unseen PMax allocation.
7. Stage the exact change, maximum exposure, maturity window, marginal metric, guardrails, approval, and rollback.
8. Verify query/item and business-source results before another step.

## Source: `playbooks/lead-generation-scaling.md`

# Lead Generation Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / value model
- Decision: how to increase qualified pipeline or realized revenue safely
- Evidence status: CRM/sales outcome evidence required
- Freshness: business-current

1. Define inquiry, lead, contacted, qualified, opportunity, appointment/proposal, closed-won, and realized-revenue stages as applicable.
2. Reconcile advertising/form data to CRM cohorts with response, qualification, show, close, value, lag, invalidity, and sales/service cost.
3. Check sales response, routing, appointment, close, onboarding, and service capacity.
4. Diagnose targeting/message, form qualification, follow-up, geography, offer, creative, and operational constraints.
5. Select demand, creative, funnel, value-signal, portfolio, or operational scaling.
6. Define allowable cost per qualified/deep outcome, maximum exposure, quality/capacity guardrails, and rollback.
7. Verify qualified pipeline, closed-won/realized value, lead quality, and sales burden before repeating.

## Source: `playbooks/lead-generation.md`

# Lead Generation Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / model
- Decision: how to optimize for qualified pipeline and realized value
- Evidence status: repeatable operating method; CRM definitions are client-specific
- Freshness: stable; lifecycle and platform labels require explicit mapping

1. Define a qualified lead, disqualifiers, sales capacity, response-time expectation, close stages, and realized value.
2. Join ad and form data to CRM outcomes where possible.
3. Diagnose volume, contact rate, qualification, appointment, show, close, and revenue separately.
4. Optimize to the deepest reliable signal; protect lead quality with offline feedback and sales notes.
5. Test targeting, message, form friction, qualification, routing, and follow-up without disguising low-quality volume as growth.

Core equation:

`Expected lead value = qualification rate × close rate × realized customer value`

Report cost per qualified lead and customer acquisition cost when data permits, not CPL alone.

Map the client's actual CRM stages before comparing results. A common reference sequence is:

`inquiry -> lead -> contacted lead -> qualified lead -> sales-qualified opportunity -> appointment or proposal -> closed-won customer -> realized revenue`

## Source: `playbooks/meta-ads-audit.md`

# Meta Ads Audit Playbook

## Purpose
A repeatable process for diagnosing Meta Ads performance before making changes.

## Audit Order

1. Business context
- Offer
- Margin
- Customer value
- Funnel objective

2. Tracking
- Pixel
- Conversions API
- Events
- Attribution settings

3. Account structure
- Campaign objective
- Budget allocation
- Audience strategy
- Advantage+ usage

4. Creative system
Review:
- Hook
- Angle
- Offer
- Proof
- Format
- Fatigue

5. Performance diagnosis
Analyze:
- CPM
- CTR
- CPC
- Landing page views
- Conversion rate
- CPA
- ROAS

6. Optimization rules
Do not change multiple variables without a reason.
Prioritize creative testing before unnecessary account restructuring.

## Output
Include:
- Findings
- Evidence
- Recommended actions
- Expected impact
- Next review point

## Source: `playbooks/meta-ads-scaling.md`

# Meta Ads Scaling Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: process / channel strategy
- Decision: which controlled Meta Ads scaling step is justified
- Evidence status: account evidence required
- Freshness: live-check for current controls

1. Verify objective, conversion location, performance goal, dataset/event, Conversions API/deduplication, attribution, business outcome, economics, and account-visible automation.
2. Diagnose delivery, spend concentration, audience source/controls, creative IDs/concepts, placement/geography, destination, offer, downstream quality, and capacity.
3. Separate new-customer acquisition and exact retargeting sources/windows/exclusions.
4. Select one mode: budget allocation, audience/market, placement, creative, catalog/product, value/quality signal, funnel, or operational capacity.
5. Treat broad/lookalike/interest/Custom Audience/automation choices as hypotheses; retargeting ROAS is not incrementality.
6. Define one interpretable step, maximum exposure, conversion maturity, business metric, creative/quality guardrails, approval, and rollback.
7. Verify business-source, marginal, new-customer/lead-quality, and operational results before another step.

## Source: `workflows/README.md`

# AI Marketing Workflows

Reusable decision workflows for common marketing tasks.

## Campaign Launch Workflow

1. Understand business economics
2. Define customer and intent
3. Select channel strategy
4. Build campaign structure
5. Create messaging and creative
6. Validate tracking
7. Launch with measurement plan

## Optimization Workflow

1. Review performance data
2. Identify constraint
3. Diagnose root cause
4. Select optimization action
5. Run controlled test
6. Measure impact
7. Document learning

## Available Workflows

### Campaign Systems
- Campaign launch
- Creative testing

### Paid Acquisition
- Google Ads optimization
- Meta Ads optimization

### Conversion
- CRO improvement

### Measurement
- Reporting analysis

## Decision Principle

Do not optimize isolated metrics. Optimize the complete system:

Business goal → Customer journey → Traffic quality → Conversion experience → Profitability

## Source: `workflows/creative-ideation-engine.md`

# Creative Ideation Engine Workflow

## Goal

Turn verified customer, product, offer, and performance evidence into a prioritized set of strategically distinct creative experiments.

Owner: `$creative-strategy`.

This workflow generates hypotheses and test cells. It does not prove that an angle, mechanic, hook, or format will work, publish ads, or replace customer research.

## Inputs

- product truth and claims boundaries
- target audience and situation
- verified customer language or clearly labeled research gaps
- pain, desire, or JTBD
- awareness stage or best-supported awareness hypothesis
- objections and current beliefs
- differentiators and offer
- available proof
- brand and placement constraints
- prior creative or performance learning when available

When reviews are a material source, use the `$customer-research` review-mining handoff rather than selecting flattering quotes directly.

## Process

1. **Verify the source insight.** Separate observed evidence, supplied facts, inference, assumptions, and unknowns.
2. **Map the audience state.** Use the awareness-belief-desire map to state the situation, desired progress, current belief, blocking belief, required belief shift, and available proof.
3. **Form angle hypotheses.** Create distinct reasons to care that connect the audience's desired progress to substantiated product or offer truth.
4. **Expand deliberately.** Use the ideation expansion method to generate evidence-compatible mechanic, concept, hook, visual-format, proof, and CTA candidates without forcing an idea quota.
5. **Choose the meaning-making structure.** Select a primary creative mechanic that defines how the concept will make the angle land: demonstrate, compare, reframe, reveal, teach, provide proof, or another supportable route.
6. **Build the execution.** Turn the mechanic into a specific concept, write the opening with the hook-execution method, and choose visual-format candidates that serve the mechanic and proof requirements.
7. **Remove duplicates.** Consolidate cosmetic variations and any cells that would teach the same strategic lesson.
8. **Prioritize.** Rank by evidence fit, business relevance, differentiation, proof availability, production feasibility, and learning value.
9. **Build the matrix.** Record each selected cell in `templates/creative-idea-matrix.md` (source: `templates/creative-idea-matrix.md`).
10. **Define the test.** Name the controlled variable, success signal, business guardrail, decision window, and what a win, loss, or inconclusive result would teach.
11. **Create production briefs.** Convert approved cells into the creative brief or static DTC render brief owned by `$creative-strategy`.
12. **Validate platform fit.** Route current platform-native fit and policy-sensitive execution to the owning channel skill before launch.
13. **Hand off to testing.** Use `creative-testing.md` (source: `workflows/creative-testing.md`) for launch, analysis, learning extraction, and iteration.

## Canonical reasoning flow

```text
Verified research
→ audience situation
→ pain / desire / JTBD
→ awareness
→ current belief
→ required belief shift
→ angle
→ creative mechanic
→ concept
→ hook
→ visual format
→ proof
→ CTA
→ test hypothesis
```

The flow is a reasoning aid, not a claim that buyers move through these states linearly.

## Decision rules

- Do not generate a belief shift that the available evidence cannot support.
- Do not treat awareness labels as facts when they are inferred from limited evidence.
- An angle changes the strategic reason to care; a mechanic changes how the audience reaches that reason; a hook changes how the concept opens; a format changes the delivery vessel.
- Do not treat a format family, mechanic family, hook tactic, or voice pattern as inherently high-performing.
- More ideas are not automatically better. Stop expansion when additional cells become cosmetic, weakly evidenced, or low-learning.
- Prior performance can inform prioritization but does not make a new execution proven.
- A generated idea remains a hypothesis until the relevant test produces interpretable evidence.

## Output

A prioritized creative idea matrix containing:

- source insight and evidence state
- audience situation
- pain/desire/JTBD
- awareness
- current and blocking belief
- required belief shift
- angle and hypothesis
- primary creative mechanic
- concept
- hook
- visual format
- proof
- offer/CTA
- controlled variable
- success signal
- business guardrail
- decision window
- expected learning
- status

## QA

Check that the source insight is grounded, review evidence is not selectively sampled, belief shifts are supportable, angles are strategically distinct, mechanics have a clear communication job, hooks preserve the angle and proof boundary, formats serve the mechanic rather than replace strategy, duplicate cells are removed, current platform fit is validated by the correct owner, and each selected test can teach something useful regardless of whether it wins.

## Source: `workflows/creative-testing.md`

# Creative Testing Workflow

## Goal
Find creative angles that improve business outcomes, not only engagement.

## Process

1. Research customer awareness and pain points
2. Identify angle and hypothesis
3. Create controlled variations
4. Define success metrics
5. Launch test
6. Analyze performance
7. Extract learning
8. Scale winning patterns

## Evaluation

Check:

- Is the audience clear?
- Is the insight supported?
- Is the offer strong?
- Is the variable controlled?
- Does the result support a decision?

## Source: `workflows/cro-improvement.md`

# CRO Improvement Workflow

## Objective
Improve conversion rates by removing friction and increasing clarity.

## Workflow

Research Users
↓
Analyze traffic sources and behavior
↓
Identify conversion barriers
↓
Create hypothesis
↓
Prioritize by impact and effort
↓
Run test
↓
Measure business impact

## Review Areas

- Message match
- Offer clarity
- Trust elements
- User experience
- Checkout or lead flow

## Source: `workflows/google-ads-optimization.md`

# Google Ads Optimization Workflow

## Objective
Improve campaign performance through structured diagnosis and testing.

## Workflow

Data Review
↓
Check spend, conversions, CPA, ROAS, CTR, CVR, search terms

Diagnosis
↓
Identify whether the issue is traffic, offer, creative, landing page, tracking, or bidding

Action
↓
Make the smallest high-impact change

Test
↓
Measure impact against the original hypothesis

Learn
↓
Document what worked and update the system

## Guardrails

- Validate tracking before optimization
- Avoid reacting to insufficient data
- Prioritize business outcomes over platform metrics

## Source: `workflows/marketing-operations-loop.md`

# Marketing Operations Loop

## Knowledge metadata

- Primary type: workflow / process
- Decision: how recurring marketing work moves safely from trigger to verified outcome
- Owner: `$marketing-operations`
- Evidence status: stable operating method; each run inherits the evidence quality of its sources and specialist decisions
- Authorization: read-only by default; mutating steps require explicit valid approval

## Canonical sequence

`Trigger → Load checkpoint → Validate sources/freshness → Route specialist checks → Diagnose/decide → Approval gate → Execute or hand off → Verify implementation → Record state → Record learning/context → Notify/escalate/no-op → Schedule/await next trigger`

Not every loop needs every step. Omissions must be deliberate and justified.

## Step 1 — Trigger

Identify why this run exists:

- fixed cadence
- verified event
- condition-watch check
- verified state change

Record trigger time, trigger source, relevant entity/window, and dedupe key.

## Step 2 — Load checkpoint

Read the last durable state before collecting new evidence. Determine:

- last completed run
- last processed entity/window
- unresolved prior action
- prior alert state
- approval state/expiry
- pending verification

If state cannot determine whether a prior mutation occurred, stop the mutating path and verify/escalate.

## Step 3 — Validate sources and freshness

Check only the evidence needed for the recurring decision. Confirm:

- source available
- metric/definition unchanged or disclosed
- data sufficiently mature for the decision
- shared Marketing Context fields used are current enough
- platform-specific claims pass freshness requirements

A stale input can downgrade the run to read-only or block it entirely.

## Step 4 — Route specialist checks

`$marketing-operations` coordinates. The domain owner still decides.

Examples:

- Google Ads health/optimization → `$google-ads`
- Meta delivery → `$meta-ads`
- cross-channel anomaly → `$performance-diagnostics`
- offer review → `$offer-strategy`
- creative fatigue/iteration → `$creative-strategy`
- landing/page issue → `$cro`
- experiment validity/learning → `$tracking-measurement`
- scaling/pacing → `$optimization-scaling`
- recurring executive communication → `$marketing-reporting`

Use the smallest useful specialist set.

## Step 5 — Diagnose or decide

State:

- current evidence
- domain owner's decision
- confidence/evidence state
- whether action is needed
- no-op reason if not

“No action” is a valid result when the evidence does not justify intervention.

## Step 6 — Approval gate

Before any live mutation, confirm authorization covers:

- exact action type
- entity/scope
- quantitative bounds if relevant
- current conditions
- expiry
- stop/rollback rule

If not, emit an approval request and stop the mutating path.

## Step 7 — Execute or hand off

Only the authorized runtime/domain owner performs the live mutation. Record:

- intended action
- submitted/saved/live status
- execution identifier if available
- timestamp
- expected verification source

A written loop workflow does not itself constitute execution.

## Step 8 — Verify implementation

Confirm the source system reflects the intended change. Distinguish:

- submitted/saved
- live/processing
- observed
- verified

If business impact requires a later observation window, create a pending-verification state rather than claiming success.

## Step 9 — Record state

Persist the checkpoint, dedupe key, decision, authorization used, action state, verification state, and unresolved items.

Do not overwrite failed/skipped history.

## Step 10 — Record learning/context

- validated experiment learning → `$tracking-measurement`
- reusable context change → `$marketing-intake`
- specialist-specific operational pattern → owning skill

Repeated observation alone is not causal proof.

## Step 11 — Output policy

Emit exactly what the loop contract requires:

- alert
- approval request
- decision summary
- recurring report handoff
- escalation
- no output when nothing materially changed

Avoid duplicate alerts by using condition state and re-arm rules.

## Step 12 — Continue, pause, or retire

End each run with one explicit status:

- next run eligible normally
- waiting for data maturity
- waiting for approval
- waiting for verification
- degraded / retryable
- paused / escalated
- retired

## Example loop shapes

### Paid-media review loop

`Weekly trigger → validate cost/revenue windows → channel audit → performance diagnosis if anomaly → pacing/scaling decision if eligible → approval if mutation → execute → verify → log decision/learning`

### Creative learning loop

`New creative data window → validate sample → creative-strategy read → identify fatigue/winner hypothesis → tracking-measurement learning status → draft next controlled test → no live launch without channel approval`

### Conversion loop

`Page-change/event trigger → verify deployment → wait for valid observation window → CRO review → experiment learning → keep/iterate/revert decision → log context`

### Condition-watch loop

`Scheduled check → read current condition + prior alert state → validate persistence/window → if unchanged false: no output → if newly true: route specialist → alert/approval request → set notified state → re-arm only after reset rule`

## QA

A valid loop has a justified trigger, durable checkpoint, source/freshness gate, domain owner for each substantive decision, idempotency for repeated effects, approval before mutation, implementation verification, bounded output policy, explicit escalation/stop behavior, and exact runtime status.

## Source: `workflows/meta-ads-optimization.md`

# Meta Ads Optimization Workflow

## Objective
Improve paid social performance through creative, audience, and conversion analysis.

## Workflow

Review Business Goal
↓
Analyze creative performance, CPM, CTR, CPC, CVR, CPA, ROAS
↓
Find bottleneck
↓
Create hypothesis
↓
Test creative, offer, audience, or landing page change
↓
Measure results
↓
Scale winners

## Priority Order

1. Creative quality
2. Offer strength
3. Landing page experience
4. Audience signals
5. Campaign settings

## Source: `workflows/reporting-analysis.md`

# Reporting Analysis Workflow

## Purpose
Turn marketing performance data into decisions, actions, and experiments.

## Workflow

Data Collection
↓
Validation
↓
Performance Review
↓
Root Cause Analysis
↓
Recommendation
↓
Action Plan
↓
Measurement

## Review Areas

- Spend efficiency
- Revenue or lead quality
- Conversion rate
- Funnel performance
- Creative performance
- Audience performance
- Search intent
- Tracking accuracy

## Output

A clear report containing:

- What changed
- Why it changed
- Evidence
- Recommended action
- Expected impact
- Next test

## Source: `templates/README.md`

# Templates

Reusable marketing templates for planning, execution, analysis, and reporting.

## Included Templates

- Campaign Brief
- Marketing Audit
- Creative Brief
- Reporting Template
- Experiment Plan

## Source: `templates/activation-plan.md`

# Activation Plan

Canonical activation definition, journey, diagnosis, intervention, measurement, and learning record.

Owner: `$activation`.

## Decision State

- Business / product:
- Date:
- Owner:
- Status: hypothesis | designed | approved | implemented | live | observed | verified | contradicted
- Primary business outcome:
- Source systems:
- Evidence state:

## Does a Distinct Activation Stage Exist?

- Conversion boundary:
- Does meaningful value occur after conversion? yes | no | uncertain
- Rationale:
- If no, why a separate activation layer is not decision-relevant:

## First Meaningful Value

- Candidate activation event/outcome:
- Customer progress represented:
- Why this is more than setup/admin:
- Evidence supporting the definition:
- Known confounders:
- Current definition status: hypothesis | provisional | supported | contradicted

## Metric Contract

- Eligible population:
- Journey entry event:
- Numerator:
- Denominator:
- Activation window:
- Segment/cohort:
- Exclusions fixed before analysis:
- Late-event handling:
- Identity/stitching rule:
- Instrumentation state:

## Baseline

- Activation rate:
- Median time to value:
- Other useful time-to-value bands/percentiles:
- Not-yet-activated/censored share:
- Observation period:
- Comparison period/cohort:
- Comparability caveats:

## Path to Value

| Step | Why required | Owner | Active effort | Wait time | Dependency | Failure/stall signal | Evidence | Removability |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## First Binding Barrier

- Observed stall:
- Affected segment:
- Evidence:
- Hypothesized mechanism:
- Competing explanations:
- Barrier type: comprehension | motivation/relevance | effort | technical defect | trust/anxiety | dependency | operational delay | qualification/fit | measurement failure | other
- Responsible owner:

## Intervention Hypothesis

- Change proposed:
- Why this is the smallest meaningful change:
- Expected mechanism:
- What must remain unchanged for interpretation:
- Implementation owner:
- Dependencies:
- Approval required:

## Measurement Plan

### Primary activation outcome
- Metric:
- Why it represents meaningful value:

### Supporting metrics
- 

### Guardrails
- Refund/cancellation:
- Support burden:
- Quality/error:
- Safety/compliance:
- Retention/repeat use:
- Revenue/contribution/lead quality:
- Other:

### Test design
- Control/comparison:
- Exposure/allocation:
- Sample/duration approach:
- Evaluation window:
- Instrumentation:
- Stop/rollback conditions:
- Causal-validity owner if needed: `$tracking-measurement`

## Handoffs

| Need | Owner | Artifact / action | Status |
|---|---|---|---|
| Event integrity / experiment validity | `$tracking-measurement` | | |
| Lifecycle triggers/cadence | `$lifecycle-marketing` | | |
| Wording | `$copywriting` | | |
| Bounded surface UX | `$cro` | | |
| Segment / fit | `$icp-jtbd` | | |
| Promise / expectation | `$offer-strategy` | | |
| Downstream retention economics | `$retention-economics` | | |
| Recurring operating loop | `$marketing-operations` | | |
| Product/service/operations implementation | external implementation owner | | |

## Result

- Observation:
- Activation outcome:
- Supporting metrics:
- Guardrails:
- Validity state:
- Decision: supports | contradicts | inconclusive | guardrail harm | invalid
- Scope of learning:
- Downstream effects mature? yes | no | partial
- Next action:

## Learning Handoff

- Experiment-learning record:
- Transfer status:
- Replication needed:
- Contradictions preserved:
- Marketing Context update needed? yes | no

## QA

- [ ] Distinct activation stage confirmed rather than assumed.
- [ ] Activation event represents customer value, not tracking convenience.
- [ ] Denominator, window, segment, and exclusions fixed before reading results.
- [ ] Instrumentation is decision-ready or explicitly provisional.
- [ ] First binding barrier is diagnosed with competing explanations.
- [ ] Necessary qualification/safety/compliance friction is preserved.
- [ ] Supporting metrics do not replace the value outcome.
- [ ] Downstream guardrails are included.
- [ ] Implementation ownership is explicit.
- [ ] No launched change is described as verified before the observation window supports it.

## Source: `templates/audit.md`

# Marketing Audit Template

## Knowledge metadata

- Primary type: template
- Secondary type: checklist / process output
- Decision: what evidence supports the audit conclusion and next action
- Evidence status: reusable structure; supplied evidence is required
- Authorization: read-only unless a separate approved change plan exists

## Decision and scope

- Business question:
- Scope and exclusions:
- Date range and comparison:
- Source-of-truth outcome:
- Canonical metric definition and included costs/stages:

## Evidence and integrity

- Sources:
- Measurement status:
- Missing decision-changing inputs:

## Findings

| Finding | Evidence | Business impact | Confidence | Recommended action |
|---|---|---:|---|---|

## Protected coverage and constraints

## Prioritized actions

For each action: owner, effort, expected impact, risk, dependency, validation, approval status.

## Exact status

State whether work is analysis, draft, approved, implemented, processing, or live-verified.

## Source: `templates/campaign-brief.md`

# Campaign Brief Template

## Business Goal

## Target Audience / ICP

## Offer

## Channel

## Budget

## Messaging Angle

## Creative Requirements

## Tracking Requirements

## Success Metrics

## Source: `templates/creative-brief.md`

# Creative Brief

Reusable framework for turning customer research into testable creative ideas.

## Purpose

Define what creative should communicate, how the idea should make the message land, why it is supportable, and how success will be measured.

## Business Context

- Business objective:
- Offer/product:
- Primary conversion goal:

## Audience

- Target audience:
- Audience situation:
- Pain / desire / JTBD:
- Awareness stage:
- Current belief:
- Blocking belief:
- Desired outcome:
- Main objections:

## Strategy

- Verified insight:
- Required belief shift:
- Creative angle:
- Hypothesis:
- Core promise:
- Reason to believe:
- Proof elements:

## Execution Architecture

- Primary creative mechanic:
- Secondary mechanic (optional):
- Concept / narrative:
- Hook objective:
- Hook/opening:
- Visual format:
- Platform/placement:
- Visual or spoken proof dependency:
- CTA:
- Required brand/product elements:
- Exclusions / claims guardrail:

## Testing Plan

- Variants:
- Controlled variable:
- Success metrics:
- Business guardrails:
- Decision window:
- Expected learning:

## Review

- Draft status:
- Approval status:
- Platform-fit validation status:
- Learnings after launch:

## Source: `templates/creative-idea-matrix.md`

# Creative Idea Matrix

Reusable template for turning one or more verified insights into strategically distinct, testable creative cells.

Owner: `$creative-strategy`.

## Source

- Business objective:
- Product/offer:
- Primary business outcome:
- Research source(s):
- Evidence state:
- Known constraints:

## Audience Map

- Audience/segment:
- Situation:
- Pain / desire / JTBD:
- Awareness:
- Current belief:
- Blocking belief:
- Required belief shift:
- Available proof:
- Evidence gaps:

## Idea Matrix

| Cell | Source insight | Angle | Hypothesis | Mechanic | Concept | Hook | Visual format | Proof | Offer / CTA | Controlled variable | Success signal | Guardrail | Decision window | Expected learning | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Draft |
| A2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Draft |
| B1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Draft |

## Distinction Check

For each pair of cells that look similar, answer:

- What different strategic reason to care is being tested?
- Is the audience reaching the point through a different mechanic, or only seeing a different surface treatment?
- What different belief, objection, motivation, proof job, opening, or format assumption is being tested?
- If one wins and the other loses, what would we learn?

If there is no meaningful difference, consolidate the cells.

## Execution Check

For each selected cell:

- Does the mechanic have one clear communication job?
- Does the concept express that mechanic rather than merely naming a format?
- Does the hook preserve the angle and proof boundary?
- Does the visual format serve the mechanic and product truth?
- Are any customer words traceable rather than synthesized and mislabeled as VOC?
- Are current platform-fit or policy questions routed to the correct channel owner?

## Prioritization

Rate or rank selected cells using evidence fit, business relevance, differentiation, proof availability, production feasibility, and learning value. Do not convert the ranking into a prediction that a cell will win.

## Approval and Handoff

- Cells approved for production:
- Cells held for missing evidence:
- Cells rejected as duplicates or weak hypotheses:
- Production brief owner:
- Platform-fit owner:
- Test owner:
- Approval status:

A matrix cell is a hypothesis until tested. Keep draft, approved, produced, published, live, and verified states distinct.

## Source: `templates/de-scaling-plan.md`

# De-scaling Plan

## Knowledge metadata

- Primary type: template
- Secondary type: containment process / tactic
- Authorization: approval-required

- Breached guardrail and evidence:
- Measurement validity:
- Smallest affected scope:
- Protected coverage:
- Current and proposed state:
- Expected containment effect:
- Recovery metric/window:
- Reversal/resumption criteria:
- Owner and approval:
- Exact status:

## Source: `templates/experiment-learning.md`

# Experiment Learning Record

## Knowledge metadata

- Primary type: template
- Secondary type: measurement / experiment / learning record
- Decision: what durable knowledge, if any, this experiment supports
- Evidence status: inherits the experiment's measurement and causal validity; never upgraded by summarization
- Owner: `$tracking-measurement` for validity and evidence state; domain skill owns the resulting business action

## Experiment identity

- Experiment / test ID:
- Decision being informed:
- Domain owner:
- Experiment owner:
- Start / end dates:
- Population / audience:
- Surface / channel:
- Geography:
- Offer / commercial conditions:
- Relevant platform or product state:
- Related experiment brief:

## Pre-registered hypothesis

- Evidence-backed problem:
- Hypothesis:
- Expected mechanism:
- Control:
- Variant:
- Primary business outcome:
- Business guardrails:
- Required evidence level:
- Pre-registered decision rule:

## Validity check

- Allocation / exposure integrity:
- Treatment-control fidelity:
- Instrumentation status:
- Conversion lag complete: yes | no | partial
- Sample / duration requirement met:
- Contamination / coincident changes:
- Early stopping or metric switching:
- Validity class: valid-supports | valid-contradicts | valid-inconclusive | valid-guardrail-harm | invalid-compromised
- Achieved evidence / causal level:

## Observed result

- Primary outcome estimate:
- Uncertainty / interval:
- Minimum detectable effect or decision threshold:
- Sample / exposure:
- Guardrail outcomes:
- Important secondary diagnostics:

## Interpretation

### Observed

What the experiment directly supports within the measured scope:

### Mechanism hypothesis

Why the result may have occurred. Label inference explicitly; do not turn the explanatory story into a proven mechanism unless the design isolates it.

### What this does not prove

- 

## Decision

- Operational disposition: ship within tested scope | reject within tested scope | iterate and retest | replicate before wider use | collect more data | invalidate and rerun | stop for guardrail harm
- Decision owner:
- Authorization status:
- Implementation scope, if approved:

## Scoped learning statement

`In [population/surface/context], changing [control] to [variant] produced [effect + uncertainty] on [primary business outcome] during [period], at [evidence level]. This [supports / contradicts / does not resolve] [hypothesis]. It does not establish [unproven mechanism or transfer claim].`

## Transfer status

- Status: local result | replication candidate | replicated scoped pattern | segment-specific pattern | contradicted / unstable
- Comparable prior tests:
- Contradictory tests:
- Conditions that must remain true for transfer:
- Contexts requiring a fresh test:

## Next learning step

- Uncertainty remaining:
- Next hypothesis, if justified:
- Why the next test is decision-relevant:
- Backlog action: add | reprioritize | park | remove | none

## Change / evidence log

Preserve revisions rather than rewriting the historical result.

- YYYY-MM-DD — change, new evidence, or contradiction — source:

## QA

- [ ] Validity was assessed before calling direction.
- [ ] Primary outcome and guardrails match the pre-test plan.
- [ ] Full relevant conversion lag is included or the limitation is stated.
- [ ] A null/inconclusive result is not mislabeled a control win.
- [ ] Post-hoc segments are not presented as confirmed effects.
- [ ] Observation and mechanism interpretation are separate.
- [ ] Scope and commercial/platform conditions are preserved.
- [ ] Contradictory prior evidence remains visible.
- [ ] External or competitor evidence is not labeled local experimental proof.
- [ ] Transfer status does not exceed the evidence.

## Source: `templates/experiment.md`

# Experiment Brief

## Knowledge metadata

- Primary type: template
- Secondary type: methodology / process / checklist
- Decision: whether a proposed test can produce a valid decision
- Evidence status: reusable structure; experiment inputs and instrumentation require verification
- Authorization: approval-required before activation

- Decision:
- Evidence-backed problem:
- Prior learning / related tests:
- Hypothesis:
- Expected mechanism:
- Control:
- Variant:
- Audience and allocation:
- Primary metric:
- Business guardrails:
- Required evidence level:
- Instrumentation checks:
- Duration/sample approach:
- Harm stop condition:
- Decision rule:
- Owner and approval status:
- Learning-record destination: `templates/experiment-learning.md` or project-equivalent

## Source: `templates/knowledge-artifact.md`

# Marketing OS Knowledge Artifact

Use this header for a standalone strategy, framework, model, methodology, process, playbook, pattern, tactic, technique, template, best-practice, heuristic, policy, or standard. See `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`).

```yaml
artifact_type:
decision:
scope:
owner:
inputs:
evidence_status:
confidence:
freshness:
dependencies:
authorization:
rollback_or_stop:
```

## Content

Describe the artifact, its intended use, limitations, and the evidence or source that supports it.

## QA

- Primary type is explicit and secondary types are justified.
- Patterns are not written as causal conclusions.
- Models expose variables and assumptions.
- Best practices and heuristics have scope, freshness, and override conditions.
- Tactics include approval and rollback/stop conditions when they could affect live systems.
- Status matches verification: draft, approved, implemented, processing, or live-verified.

## Source: `templates/landing-page-review.md`

# Landing Page Review Template

## Objective
Primary conversion goal:

## User Journey
- Traffic source:
- Audience intent:
- Expected action:

## Review Areas
- Message clarity
- Offer strength
- Trust signals
- Page structure
- Mobile experience
- Conversion friction

## Recommendations
Issue:
Impact:
Priority:
Action:

## Source: `templates/marketing-audit.md`

# Marketing Audit Template

## Business Context
- Business model:
- Goal:
- Target audience:
- Main challenges:

## Market Review
- Customer research
- Competitors
- Positioning
- Offer strength

## Channel Review
- Paid acquisition
- SEO/content
- Email/lifecycle
- Conversion journey

## Findings
What is working?
What is limiting growth?

## Recommendations
Priority:
Impact:
Effort:
Next action:

## Source: `templates/marketing-context.md`

# Marketing Context

Shared decision context for the Marketing OS.

Owner: `$marketing-intake`.

This artifact reduces repeated intake across skills. It is a curated context layer, not a replacement for source evidence, the evidence register, or specialist analysis. Every decision-relevant statement must preserve its source and evidence state. Unknowns remain unknown; contradictions remain visible.

## Document State

- Context version:
- Last updated:
- Scope / business:
- Status: draft | partial | current | stale
- Source-of-truth system(s):
- Evidence register:
- Known freshness limits:

## Business and Goals

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Business model |  |  |  |
| Primary business outcome |  |  |  |
| Market / geography |  |  |  |
| Time horizon |  |  |  |
| Strategic constraints |  |  |  |

## Growth Strategy State

Record this section when an integrated business-level growth strategy is decision-relevant. `$growth-strategy` owns the current constraint structure, opportunity portfolio, strategic priorities, non-priorities, sequencing, and review state. Specialist source artifacts still govern the underlying decisions.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Strategy version / status |  |  |  |
| Planning horizon |  |  |  |
| Constraint structure | primary/binding / co-limiting-interacting / independent / not yet identified |  |  |
| Current limiting constraint(s) |  |  |  |
| Constraint confidence / evidence state |  |  |  |
| Priority strategic bets |  |  |  |
| Explicit non-priorities |  |  |  |
| Key dependencies / capacity limits |  |  |  |
| Learning agenda / major open hypothesis |  |  |  |
| Next review trigger / decision point |  |  |  |

## Product Truth and Claim Boundaries

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Product / service |  |  |  |
| Core use case |  |  |  |
| Verified capabilities |  |  |  |
| Claim boundaries |  |  |  |
| Known limitations |  |  |  |

## Market, Segment, and JTBD

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Category / market frame |  |  |  |
| Priority segment |  |  |  |
| Secondary / experimental segment |  |  |  |
| Buying situation |  |  |  |
| JTBD / desired progress |  |  |  |
| Buyer / user roles |  |  |  |
| Exclusions / poor-fit segment |  |  |  |

## Customer Evidence and VOC

Record patterns here; keep traceable quotations in the underlying research source.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Pain / friction |  |  |  |
| Desired outcome |  |  |  |
| Trigger moments |  |  |  |
| Objections / anxieties |  |  |  |
| Selection criteria |  |  |  |
| Repeated language / themes |  |  |  |
| Contradictions / segment differences |  |  |  |

## Positioning and Differentiation

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Positioning hypothesis / decision |  |  |  |
| Differentiators |  |  |  |
| Reason to believe |  |  |  |
| Alternatives / status quo |  |  |  |
| Competitor implications |  |  |  |

## Current Offer

This section records the current offer state. `$offer-strategy` owns diagnosis or redesign of the proposition itself.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Core deliverable |  |  |  |
| Promised outcome |  |  |  |
| Offer components / bundle |  |  |  |
| Risk reversal |  |  |  |
| Real urgency / scarcity |  |  |  |

## Current Pricing and Monetization

This section records the current commercial exchange state. `$pricing-monetization` owns pricing architecture and price-change decisions. Preserve exact state: proposed, approved, configured, live, observed, or verified.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Base / list price |  |  |  |
| Realized price / discount mix |  |  |  |
| Value metric |  |  |  |
| Packages / tiers |  |  |  |
| Payment model / terms |  |  |  |
| Fees / credits |  |  |  |
| Existing-customer / renewal treatment |  |  |  |
| Commercial state |  |  |  |

## Activation and First Value

Record this section only when a distinct post-conversion activation stage is decision-relevant. `$activation` owns the first meaningful value definition, path-to-value, time-to-value, and activation diagnosis. Do not invent an activation event just to fill the template.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Conversion boundary |  |  |  |
| Distinct activation stage exists? |  |  |  |
| First meaningful value definition |  |  |  |
| Definition status | hypothesis / provisional / supported / contradicted |  |  |
| Eligible denominator / segment |  |  |  |
| Activation window |  |  |  |
| Activation baseline |  |  |  |
| Time-to-value baseline |  |  |  |
| First binding barrier |  |  |  |
| Instrumentation state |  |  |  |
| Current intervention / test state |  |  |  |

## Retention Strategy State

Record this section only when repeat, renewal, continuing use/service, lapse, recovery, or win-back is decision-relevant. `$retention-strategy` owns reason diagnosis and intervention strategy; `$retention-economics` owns realized retention/LTV/payback evidence.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Continuation behavior |  |  |  |
| Relevant segment / cohort / window |  |  |  |
| Observed state | active / at risk / voluntary cancel / involuntary loss / dormant-lapsed / recovered / won back |  |  |
| Leading reason family |  |  |  |
| Reason confidence |  |  |  |
| Voluntary / involuntary / lapse classification |  |  |  |
| Current intervention hypothesis |  |  |  |
| Root-cause owner |  |  |  |
| Current test / rollout state |  |  |  |
| Durable-save / recovery verification state |  |  |  |

## Proof Inventory

| Proof type | Available evidence | Source | Evidence state | Allowed use / limit |
|---|---|---|---|---|
| Product demonstration |  |  |  |  |
| Customer-reported experience |  |  |  |  |
| Case study / business result |  |  |  |  |
| Independent / third-party proof |  |  |  |  |
| Credentials / authority |  |  |  |  |

## Economics and Commercial Constraints

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Revenue basis |  |  |  |
| Profit level |  |  |  |
| Margin / variable-cost constraints |  |  |  |
| Refund / cancellation considerations |  |  |  |
| Capacity / inventory / service limits |  |  |  |

## Brand and Message Constraints

- Brand voice:
- Required terminology:
- Prohibited / unsupported claims:
- Legal / compliance constraints:
- Visual / production constraints:

## Channel and Funnel Context

| Channel / surface | Current role | Known constraint | Evidence / source |
|---|---|---|---|
|  |  |  |  |

## Open Decisions and Evidence Gaps

| Open item | Why it matters | Evidence needed | Owner | Status |
|---|---|---|---|---|
|  |  |  |  |  |

## Change Log

Newest first. Preserve prior entries rather than rewriting history.

- vX — YYYY-MM-DD — What changed, why, source or decision that changed it.

## Usage Rules

- Downstream skills read only the sections relevant to their decision; this is not a requirement to load the whole file for every trivial task.
- A context entry inherits the evidence state of its underlying source; summarizing it here never upgrades confidence.
- Customer language is not verbatim VOC unless it remains traceable to the supplied source.
- A model-generated synthesis is labeled synthesis or hypothesis, not customer evidence, willingness-to-pay, activation fact, verified retention cause, or a verified growth constraint.
- A growth strategy summary cannot make a specialist hypothesis true; strategy priorities stay tied to the source evidence and may become stale when constraints, economics, capacity, or opportunity cost change.
- Do not force a single binding growth constraint in context. Preserve the current `primary/binding`, `co-limiting/interacting`, `independent`, or `not yet identified` strategy state from the governing strategy artifact.
- A proposed/configured price remains proposed/configured here until the source pricing artifact verifies a later state.
- An activation event remains hypothesis/provisional here until the `$activation` artifact supports a stronger state; onboarding completion or email engagement is not silently promoted to first value.
- A customer-stated cancellation reason remains customer-stated here; it is not silently promoted to verified retention causality. A save remains provisional until the decision-relevant continuation window is observed.
- Do not silently overwrite a contradiction. Record the competing evidence and the segment, date, or source difference.
- Do not place unnecessary personal data in this artifact.
- When a decision materially changes the context, increment the context version and prepend a change-log entry.
- If a decision-relevant section is stale or contradicted, mark the context partial or stale rather than letting downstream skills treat it as current.

## Source: `templates/marketing-loop.md`

# Marketing Loop Contract

## Knowledge metadata

- Primary type: template / checklist
- Owner: `$marketing-operations`
- Decision: whether a recurring operating loop is sufficiently specified and controlled to run safely
- Evidence status: reusable structure; each run inherits source and specialist evidence states
- Authorization: read-only by default; live mutation requires explicit valid approval

## Identity and State

- Loop ID:
- Loop version:
- Loop owner:
- Status: designed | approved-to-configure | configured | active-verified | paused | degraded | retired
- Runtime / scheduler / trigger mechanism:
- Last successful run:
- Last failed/skipped run:
- Change log:

## Objective

- Business objective:
- Recurring decision or burden:
- Primary business outcome:
- Guardrails:
- Why a recurring loop is justified:

## Trigger and Cadence

- Trigger type: fixed cadence | event | condition-watch | state-change
- Trigger/cadence definition:
- Trigger source:
- Earliest useful next run:
- Maximum acceptable delay:
- Data/decision lag:
- Quiet/blackout window if relevant:
- Re-arm/reset rule for condition watches:

## Scope

- Business / market:
- Channel / surface / entity scope:
- Decision window:
- Explicit exclusions:

## Source and Freshness Gates

| Source / artifact | Used for | Required freshness / maturity | Owner | Block/downgrade rule if missing or stale |
|---|---|---|---|---|
|  |  |  |  |  |

## Routing and Ownership

| Step / decision | Domain owner | Supporting skill(s) | Output needed |
|---|---|---|---|
|  |  |  |  |

## Durable State

- Last processed entity/window:
- Last attempted checkpoint:
- Last successful checkpoint:
- Pending verification:
- Unresolved escalation:
- Prior condition/alert state:
- State storage/location:

## Idempotency

- Dedupe key:
- How a genuinely new event/action is distinguished from a retry:
- Mutation already-applied check:
- Duplicate alert suppression:
- Retryable failure classes:
- Non-retryable / escalate-first classes:

## Run Sequence

1. Trigger:
2. Load state/checkpoint:
3. Validate inputs/freshness:
4. Route specialist checks:
5. Diagnose/decide:
6. Approval gate:
7. Execute/hand off:
8. Verify implementation:
9. Record state:
10. Record learning/context:
11. Notify/escalate/no-op:
12. Continue/pause/retire:

## Authorization Boundary

- Read-only steps:
- Allowed mutating steps:
- Approval source:
- Scope/entities covered:
- Quantitative limits:
- Approval expiry:
- Conditions that invalidate approval:
- Rollback/stop condition:

## Execution and Verification

- Execution owner/runtime:
- Implementation status source:
- Verification source:
- Expected processing/observation delay:
- What counts as implementation verified:
- What requires later business-performance verification:

## Output and Notification Policy

- Emit when:
- Suppress when:
- Alert recipient/destination if configured:
- Reminder policy:
- Duplicate suppression rule:
- Approval-request format:
- Normal run output:

## Escalation / Stop / Retirement

- Data escalation:
- Decision escalation:
- Authorization escalation:
- Commercial/safety escalation:
- Pause condition:
- Resume condition:
- Retirement condition:

## Learning Handoff

- Experiment learning owner:
- Marketing Context update rule:
- Specialist learning destination:
- What must not be promoted to causal/best-practice status:

## Run Record

For each run preserve:

- run ID/time
- trigger and entity/window
- source versions/evidence state
- decisions and owners
- approval used
- action state
- verification state
- output/alert state
- learning/context updates
- errors/skips/escalations
- exact run status

## QA

Confirm trigger/cadence is justified; state is durable; retries cannot duplicate live effects; every substantive decision has a domain owner; source/freshness gates are explicit; live changes cannot bypass authorization; output noise is controlled; stop/escalation/retirement exists; and `active-verified` is used only after an actual expected run has been observed successfully.

## Source: `templates/performance-report.md`

# Performance Report

## Knowledge metadata

- Primary type: template
- Secondary type: model / decision artifact
- Decision: what changed, why it matters, and what action is justified
- Evidence status: reusable structure; source-of-truth metrics are required
- Authorization: report draft until verified

## Executive decision

What changed, why it matters, and the single most important action.

## Scorecard

Show current, comparison, absolute delta, relative delta, target, and definition for each business outcome and driver.

Name the profit level, revenue basis, attribution basis, and lead/customer stage wherever applicable.

## Drivers

Separate confirmed drivers from hypotheses. Quantify contribution where possible and expose mix changes.

## Actions

For each: action, evidence, expected business effect, owner, due date, risk/guardrail, and status.

## Unknowns

List only missing inputs that could change the decision.

## Source: `templates/pricing-decision.md`

# Pricing Decision

## Knowledge metadata

- Primary type: template
- Secondary type: methodology / checklist
- Decision: whether a price, value metric, package/tier, payment model, or discount architecture should be proposed, tested, approved, rolled out, or rejected
- Owner: `$pricing-monetization`
- Evidence status: reusable structure; project inputs require verification
- Authorization: approval-required before any live commercial change

## Decision scope

- Business / product:
- Decision type: base price | value metric | package/tier | payment model | discount architecture | price change | migration
- Segment / buying situation:
- Market / geography:
- Current state:
- Requested decision:

## Current commercial structure

- Base/list price:
- Realized price / discount mix:
- Value metric:
- Packages / tiers:
- Payment terms:
- Fees / credits:
- Existing-customer / renewal treatment:

## Evidence register

| Evidence | Source | State | What it establishes | Limitation |
|---|---|---|---|---|
|  |  |  |  |  |

## Economics

- Revenue basis:
- Profit level:
- Variable cost / cost-to-serve:
- Payment/channel/fulfillment costs:
- Refund/cancellation/return treatment:
- Capacity constraint:
- Economic floor / unsafe range:

## Customer and market evidence

- JTBD / desired progress:
- Value drivers:
- Price objections / anxieties:
- Selection tradeoffs:
- Observed purchase behavior:
- Stated-preference research:
- Competitor / alternative context:
- Contradictions:

## Candidate scenarios

| Scenario | Price / metric / package | Key assumption | Realized revenue implication | Contribution implication | Conversion / mix implication | Retention / refund risk | Capacity / service risk |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Recommendation

- Recommended structure:
- Why:
- Strongest supporting evidence:
- Decision-changing uncertainty:
- What this recommendation does **not** prove:

## Test / rollout

- Control/current terms:
- Treatment/new terms:
- Eligible population:
- Existing-customer treatment:
- Primary business outcome:
- Guardrails:
- Observation window / lag:
- Stop / rollback condition:
- Causal design owner if required: `$tracking-measurement`

## Authorization and state

- Approval owner:
- Approval scope:
- Approval expiry:
- State: draft | proposed | approved | configured | live | observed | verified | rolled-back
- Verification source:

## Follow-up

- Learning to record:
- Marketing Context update needed:
- Retention cohort follow-up needed:
- Scaling implication, if any:

## Source: `templates/recovery-verification.md`

# Scaling Recovery Verification

## Knowledge metadata

- Primary type: template
- Secondary type: checklist / evidence record
- Authorization: read-only verification

- Incident/breach:
- Containment or rollback performed and verified state:
- Source-of-truth recovery metric:
- Baseline and recovery window:
- Measurement integrity:
- Financial/quality/operational guardrails:
- Recovered / partially recovered / not recovered / new cause / insufficient evidence:
- Failed readiness gate restored?:
- Conditions for any resumption:
- Exact status and confidence:

## Source: `templates/retention-strategy-plan.md`

# Retention Strategy Plan

Owner: `$retention-strategy`

Use this artifact for a retention, save, recovery, repeat-purchase, renewal, lapse-prevention, or win-back decision. Preserve evidence state and exact implementation status.

## Decision State

- Business / scope:
- Decision type: active retention | save | involuntary recovery | repeat purchase | renewal | lapse prevention | win-back
- Status: draft | proposed | approved | configured | live | observed | verified | retired
- Decision owner:
- Implementation owner(s):
- Last updated:
- Source-of-truth systems:
- Authorization record:

## Retention Definition

- Continuation behavior:
- Eligible population:
- Segment / cohort:
- Observation window:
- Retention / churn / repeat definition:
- Revenue basis / profit level:
- Current pricing/package state:
- Activation state/definition when relevant:

## Observed State

- Current state: active | at risk | voluntary cancel | involuntary loss | dormant/lapsed | recovered | won back
- Baseline rate/count:
- Cohort maturity:
- Data quality / instrumentation state:
- Recent material changes:

## Reason Evidence

| Evidence layer | Finding | Source | Evidence state | Coverage / limit |
|---|---|---|---|---|
| Customer-stated reason |  |  |  |  |
| Observed behavior |  |  |  |  |
| Operational fact |  |  |  |  |
| Commercial fact |  |  |  |  |
| Model inference |  |  |  |  |

### Leading diagnosis

- Reason family:
- Voluntary / involuntary / lapse:
- Confidence:
- Competing explanation(s):
- Evidence needed to discriminate:
- Root-cause owner:

## Intervention Hypothesis

- Intervention:
- Mechanism hypothesis:
- Why it matches the diagnosed reason:
- Who is eligible:
- Who is excluded / suppressed:
- Customer choice / cancellation implications:
- Commercial cost:
- Product/service/operations dependency:
- Pricing dependency:
- Activation dependency:
- Lifecycle communication dependency:

## Communication Handoff

Owned by `$lifecycle-marketing` when communication is required.

- Trigger/state:
- Segment:
- Consent basis:
- Suppression conditions:
- Cadence constraint:
- Copy need for `$copywriting`:

## Test / Validation

Owned validity method: `$tracking-measurement` where causal evidence is required.

- Population:
- Control / comparison:
- Treatment:
- Primary business outcome:
- Supporting metrics:
- Observation window / lag:
- Guardrails:
- Stop conditions:
- Sample/power constraint:
- Confounding / contamination risk:
- Decision rule:

## Economics

Use `$retention-economics` for realized cohort economics and `$pricing-monetization` for commercial-term changes.

- Incremental or realized revenue basis:
- Contribution / profit level:
- Incentive / discount cost:
- Support/service cost:
- Payment-recovery cost:
- Margin risk:
- Expected downstream behavior to verify:

## Durable Save / Recovery Verification

A short-term acceptance is not automatically durable retention.

- Save/recovery accepted:
- Paid/qualified status restored:
- Continued through required window:
- Next renewal/reorder observed:
- Contribution acceptable:
- Refund/cancellation acceptable:
- Complaint/support burden acceptable:
- Discount dependency acceptable:
- Root cause resolved:
- Exact verification status:

## Learning Record

- Result: supports | contradicts | inconclusive/null | guardrail harm | invalid/compromised
- Observed effect:
- Mechanism interpretation:
- Evidence level:
- Scope where learning applies:
- Contradictory evidence:
- Replication / follow-up:
- Marketing Context update needed:

## Approval and Rollback

- Exact external mutation:
- Approved by:
- Approval scope:
- Approval expiry:
- Rollback / stop trigger:
- Customer remediation if needed:

## QA

- Retention behavior and window defined before analysis.
- State is not confused with reason.
- Voluntary and involuntary loss are separated.
- Customer-stated reason is not promoted to causal fact.
- Intervention addresses the diagnosed reason.
- Cancellation and communication rights remain intact.
- Discounts include contribution and downstream-behavior guardrails.
- Product/service defects route to their actual owner.
- A short-term save is not called durable retention prematurely.
- No external change is implied without authorization and verified state.

## Source: `templates/scale-readiness.md`

# Scale Readiness Scorecard

## Knowledge metadata

- Primary type: template
- Secondary type: checklist / decision artifact
- Authorization: read-only

- Scaling objective and scope:
- Primary business outcome and source of truth:
- Proof level:
- Measurement gate: pass / fail / unknown; evidence:
- Economics gate: pass / fail / unknown; evidence:
- Stability gate: pass / fail / unknown; evidence:
- Opportunity gate: pass / fail / unknown; evidence:
- Creative gate: pass / fail / unknown; evidence:
- Funnel gate: pass / fail / unknown; evidence:
- Operations gate: pass / fail / unknown; evidence:
- Risk/authorization gate: pass / fail / unknown; evidence:
- Blocking gate and protected coverage:
- Verdict:
- Decision-changing inputs:
- Exact status:

## Source: `templates/scaling-change-plan.md`

# Scaling Change Plan

## Knowledge metadata

- Primary type: template
- Secondary type: tactic / authorization record
- Authorization: approval-required

| Entity | Current state | Proposed state | Rationale/evidence | Expected business effect | Risk | Rollback |
|---|---|---|---|---|---|---|

- Proof/readiness level:
- Maximum exposure:
- Decision window/lag:
- Primary metric and guardrails:
- Protected coverage:
- Dependencies:
- Named approver and owner:
- Draft / approved / saved / live / processing / verified status:

## Source: `templates/scaling-decision-log.md`

# Scaling Decision Log

## Knowledge metadata

- Primary type: template
- Secondary type: evidence record
- Authorization: read-only record

| Date | Scope | Hypothesis/change | Proof before | Business result | Marginal result | Guardrails | Decision | Proof after | Status |
|---|---|---|---|---|---|---|---|---|---|

Record contradictory evidence, concurrent changes, exceptions, replication scope, and what would invalidate the learned rule.

## Source: `templates/scaling-economics.md`

# Scaling Economics Worksheet

## Knowledge metadata

- Primary type: template
- Secondary type: model
- Authorization: read-only

- Revenue basis and included tax/shipping:
- Discounts/refunds treatment:
- COGS:
- Variable fulfillment/payment/marketplace/service costs:
- Media spend:
- Contribution profit before media:
- Contribution profit after media:
- New-customer or qualified-outcome definition:
- Break-even and allowable CPA/ROAS/CPL:
- Baseline spend and outcome:
- Proposed/actual change in spend and outcome:
- Blended efficiency:
- Marginal efficiency:
- Incrementality evidence:
- Cannibalization/opportunity cost:
- Cash-flow/capacity constraint:
- Sensitivity range and unknowns:

## Source: `templates/scaling-experiment.md`

# Scaling Experiment Brief

## Knowledge metadata

- Primary type: template
- Secondary type: methodology / process / checklist
- Authorization: approval-required before activation

- Decision and hypothesis:
- Control/counterfactual:
- Treatment/scaling step:
- Population/entities and allocation:
- Baseline maturity:
- Primary business metric:
- Secondary diagnostics:
- Financial/quality/operational guardrails:
- Minimum practical effect:
- Sample/duration and lag:
- Instrumentation QA:
- Contamination/invalidity conditions:
- Maximum spend/loss at risk:
- Stop and rollback:
- Decision rule:
- Owner, approval, exact status:

## Source: `templates/scaling-hypothesis.md`

# Scaling Hypothesis Brief

## Knowledge metadata

- Primary type: template
- Secondary type: hypothesis / strategy artifact
- Authorization: draft

- Decision:
- Binding constraint and evidence:
- Scaling mode:
- Hypothesis and expected mechanism:
- Exact entity/current state:
- Proposed state and one major variable:
- Protected coverage:
- Maximum exposure:
- Primary business metric:
- Guardrails:
- Decision window and conversion lag:
- Disconfirming evidence:
- Hold/stop/rollback:
- Owner and approval:
- Proof level before test:

## Source: `templates/scaling-portfolio-review.md`

# Scaling Portfolio Review

## Knowledge metadata

- Primary type: template
- Secondary type: framework output / allocation strategy
- Authorization: read-only until a separate change plan is approved

| Entity | Role | Protected? | Blended result | Marginal opportunity | Evidence | Capacity | Cannibalization | Risk | State |
|---|---|---:|---:|---:|---|---|---|---|---|

States: protect, maintain, diagnostic-test, increase, expand, hold, reduce, exit, recovery-watch.

- Source-of-truth and cost definitions:
- Cross-platform attribution caveat:
- Next-unit allocation hypothesis:
- Maximum exposure and opportunity cost:
- Approval/rollback status:

## Source: `templates/strategy-template.md`

# Growth Strategy / Marketing Plan

Owner: `$growth-strategy`.

Use this artifact to record an integrated business-level marketing strategy. It composes specialist decisions; it does not replace their source artifacts or authorize live changes.

## Document State

- Strategy version:
- Business / scope:
- Planning horizon:
- Status: draft | decision-ready | approved | in execution | under review | superseded
- Source-of-truth system(s):
- Marketing Context version:
- Decision owner:
- Approval boundary:

## 1. Business Objective

| Field | Decision |
|---|---|
| Primary business outcome |  |
| Current baseline |  |
| Supplied target / desired direction, if any |  |
| Target evidence state |  |
| Economic level / revenue basis |  |
| Time horizon |  |
| Quality / customer guardrails |  |
| Capacity / cash constraints |  |
| What meaningful progress means |  |

Do not invent a target merely to complete this section. A business-supplied target remains asserted until its feasibility/evidence is established.

## 2. Evidence Baseline

Summarize only decision-relevant evidence. Link the specialist artifact or source rather than copying raw data.

| Area | Current state | Source | Evidence state | Decision implication |
|---|---|---|---|---|
| Market / segment / JTBD |  |  |  |  |
| Positioning |  |  |  |  |
| Offer |  |  |  |  |
| Pricing / monetization |  |  |  |  |
| Acquisition |  |  |  |  |
| Conversion |  |  |  |  |
| Activation |  |  |  |  |
| Retention |  |  |  |  |
| Customer economics |  |  |  |  |
| Measurement |  |  |  |  |
| Capacity / operations |  |  |  |  |

### Contradictions / Unknowns

| Item | Why decision-relevant | Owner | Evidence needed |
|---|---|---|---|
|  |  |  |  |

## 3. Current Limiting Constraint(s)

Do not force a single bottleneck. Use the structure the evidence supports.

- Candidate constraints:
- Constraint structure: primary/binding | co-limiting/interacting | independent | not yet identified
- Primary constraint, only if supported:
- Co-limiting / independent constraints, if relevant:
- Evidence classification per constraint: verified blocker | supported constraint | plausible constraint | contradicted | unknown
- Mechanism(s):
- Competing explanations:
- What would change this diagnosis:
- Smallest evidence step if not yet identified:

## 4. Growth Opportunity Set

Do not start with a channel list. Every opportunity must connect to the objective and a plausible constraint, mechanism, or decision-changing uncertainty.

| Opportunity | Constraint / uncertainty link | Mechanism hypothesis | Expected business or learning effect | Evidence / confidence | Specialist owner | Key dependency |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## 5. Strategic Bets and Priorities

| Priority / bet | State | Why now | Commercial upside | Effort / capacity | Reversibility / downside | Time to learn | Owner |
|---|---|---|---|---|---|---|---|
|  | protect / priority bet / validate first / maintain / defer / reject |  |  |  |  |  |  |

### Strategic Thesis

State the few choices that define the strategy. Avoid task lists.

- 

## 6. Explicit Non-Priorities

| Not pursuing now | Reason | Reconsider when |
|---|---|---|
|  |  |  |

## 7. Specialist Workstreams

| Strategic bet | Specialist owner | Decision / deliverable needed | Dependency | Status |
|---|---|---|---|---|
|  |  |  |  |  |

Growth Strategy owns the integrated sequence. Specialists retain their underlying decision authority.

## 8. Learning Agenda / Experiments

| Hypothesis | Test / evidence step | Primary business metric or validated leading indicator | Guardrails | Decision window / maturity | Tracking owner | Decision rule |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Do not define success from CTR, attributed revenue, activation rate, retention rate, or another local metric when the business objective or economics can be observed directly.

When the constraint is `not yet identified`, use this section to define the smallest evidence step that can distinguish between major competing constraints before material allocation.

## 9. Sequence and Dependencies

1. Protect / fix:
2. Validate / resolve uncertainty:
3. Execute priority bet:
4. Measure / mature:
5. Continue / hold / revise / kill / reprioritize:
6. Route to scaling when readiness is satisfied:

Do not force this sequence when the evidence supports a different dependency order. Independent workstreams may run in parallel when capacity and interpretability remain acceptable.

## 10. Resource and Capacity Implications

- Budget / cash implication:
- Creative/content capacity:
- Sales/service capacity:
- Inventory/fulfillment capacity:
- Product/engineering/technical dependency:
- Measurement dependency:
- Opportunity cost:

No budget number here authorizes live spend. Paid-media expansion routes to `$optimization-scaling`.

## 11. Review Governance

- Scheduled or condition-based review trigger:
- Earliest meaningful signal window:
- Business-outcome maturity window:
- Conditions for earlier review:
- Constraint-structure change trigger:
- Opportunity-cost / higher-value-alternative trigger:
- `continue` when:
- `hold` when:
- `revise` when:
- `kill` when:
- `reprioritize` when:
- `route to scaling` when:

## 12. Strategy Change Log

Newest first. Do not rewrite history after results arrive.

- vX — YYYY-MM-DD — evidence/change → strategy implication → constraints/priorities added/removed/resequenced.

Record when reprioritization happened because opportunity cost changed even though the original initiative had not failed.

## 13. Exact Status

- Strategy state:
- Constraint structure:
- Approved scope:
- Work actually implemented:
- Work verified:
- Open decisions:
- Next decision point:

## Usage Rules

- A strategy is a set of choices, not a list of every possible marketing activity.
- Frameworks such as AARRR, funnel stages, 90-day planning, 70/20/10 allocation, or channel portfolios may organize thinking when relevant but never provide evidence or universal quotas.
- A single binding constraint is not mandatory. Preserve co-limiting, independent, or unresolved constraints when that is what the evidence supports.
- Preserve unknowns, contradictions, and non-priorities.
- Do not convert a forecast or supplied target into a promise.
- Do not describe `approved` as `implemented`, or `in execution` as `successful`.
- Do not judge plan quality by percentage of tasks completed; strategy may improve by stopping or reprioritizing work when evidence changes.
- Specialist artifacts govern specialist decisions when they conflict with this summary.
- No live mutation is authorized by this document alone.
