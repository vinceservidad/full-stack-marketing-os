<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Tracking, Attribution, and Incrementality

## Skill: $tracking-measurement

**Use when:** Audit, design, or diagnose marketing conversion measurement, attribution reconciliation, event integrity, experiment validity, and reusable experiment learning; not for changing production tracking without approval or turning one test into a universal best practice.

Classify architecture maps, models, methodologies, processes, checklists, experiment results, and recommendations with `KNOWLEDGE-TAXONOMY.md`. Keep a collection defect, attribution difference, business-performance change, experimental estimate, and reusable learning as distinct evidence categories.

Establish whether the available data can support the requested decision before optimizing against it. Keep three questions distinct: is the data collected correctly, do sources agree, and did the activity cause the result. A causal question inherits every collection defect beneath it.

### Scope

Define the primary business outcome, platforms and properties, conversion journey, reporting timezone and currency, consent environment, attribution question, source of truth, and requested level of assurance. For a causal question, also define the decision at stake, its cost of being wrong, and the evidence level it requires. For an experiment-learning request, define the tested scope, pre-registered decision rule, domain owner, and whether the result is being used locally or considered for transfer. Reserve “Primary conversion action” for Google Ads' action-optimization status.

### Method

1. Map the event chain from user action to browser/server collection, platform receipt, deduplication, attribution, reporting, and business-system outcome.
2. Inventory each event's name, trigger, parameters, identifiers, value/currency, counting rule, destination, and primary/secondary role.
3. Test integrity across coverage, correctness, uniqueness, ordering, timeliness, identity continuity, consent behavior, and reconciliation.
4. Separate collection failures from attribution differences and reporting lag.
5. Reconcile using matched definitions and cohorts; explain expected gaps instead of forcing equality.
6. For a causal question, grade the available evidence, select a method the constraints actually permit, and state the level the result can reach before running it.
7. Rank fixes and tests by decision risk, affected volume/value, confidence, reversibility, validation cost, and learning value.
8. When an experiment concludes, validate execution before reading direction, classify the result, separate observed effect from mechanism interpretation, and create a scoped learning record using Experiment Learning System and `templates/experiment-learning.md`.
9. Before a new experiment, inspect relevant prior learning for same decision, mechanism, segment, surface, offer state, guardrail failure, or contradiction. Use prior learning to change the new test or explain why it is not decision-relevant.

Read only the reference the question requires:

- Event-level QA: event integrity.
- Totals differ across platforms or business systems: attribution reconciliation.
- Grading how strongly evidence supports a causal claim: causal evidence ladder.
- Choosing how to measure incremental effect: incrementality method selector.
- Randomized audience split: holdout experiments.
- Geographic treatment and control, matched markets, synthetic control, switchback: geo experiments.
- Platform-native lift mechanisms: platform lift studies.
- Long-horizon cross-channel allocation: Marketing Mix Modeling.
- Several imperfect sources and no decisive test: triangulation.
- Turning completed tests into durable scoped knowledge and a decision-relevant backlog: Experiment Learning System.

### Rules

- Do not declare tracking healthy from a tag firing once; verify payload quality, receipt, deduplication, downstream reporting, and business reconciliation.
- Do not make several production tagging changes at once when one controlled change can isolate the failure.
- Never expose secrets, raw personal data, or persistent identifiers in reports.
- Do not change primary conversion goals or bidding signals without explicit approval and a dependency analysis.
- For Google Ads, distinguish conversion goals from their conversion actions and each action's Primary/Secondary status. For Meta, distinguish objective, conversion location, performance goal, dataset/pixel, selected event, and attribution setting.
- Treat consented and non-consented coverage explicitly; do not recommend bypassing consent or privacy controls.
- Platform attribution never supports a causal claim at any volume. Report its evidence level rather than its confidence.
- Do not design a causal test while measurement integrity is unresolved; the test inherits the defect.
- Power the test, fix the primary metric and stopping rule before launch, and include the full conversion lag. Do not stop early on a favorable read or switch the primary metric afterwards.
- Report a null with its minimum detectable effect. Absence of evidence is not evidence of absence.
- Do not sum attributed conversions across platforms, and do not average an experimental estimate with an attributed one.
- State the scope of every causal estimate — population, geography, period, spend range. A result proven in one scope is not proven outside it.
- Count the holdback's forgone revenue as part of a test's cost.
- Assess experiment validity before result direction. A favorable outcome does not repair instrumentation defects, contamination, treatment drift, early stopping, or missing conversion lag.
- Do not call a null/inconclusive result a control winner by default, and do not call guardrail-harming treatment a winner because the primary metric improved.
- Separate the observed treatment effect from the story used to explain it. A result can support an outcome claim without proving the proposed mechanism.
- A single experiment remains a local result unless stronger replication supports a broader scoped pattern. Never promote one test, competitor example, external case study, or platform benchmark into a universal best practice.
- Post-hoc segment cuts generate hypotheses unless independently validated. Do not promote the most favorable slice into durable learning.
- Preserve contradictory tests and the conditions under which each occurred. Do not rewrite the learning archive to make the latest result look consistent.
- An experiment backlog exists to resolve valuable uncertainty, not to hit an arbitrary test count, win-rate benchmark, or calendar cadence.

### Output

Return: decision supported; architecture map; integrity status by event; reconciliation table; confirmed defects; expected discrepancies; risk-ranked actions; validation plan; exact implementation status.

Causal question: decision and required evidence level; achievable level and why; selected method with the constraints that chose it; primary metric and its definition; minimum detectable effect, duration, and stopping rule; contamination and confounding risks with direction; holdback cost; scope of the resulting estimate; what the result may and may not be used for.

Experiment learning: validity class; observed result and uncertainty; achieved evidence level; guardrail status; observation versus mechanism interpretation; operational disposition; scoped learning statement; transfer status; contradictions/dependencies; next hypothesis or reason no follow-up is justified; backlog change; exact status.

### Library references

Owned root artifacts, read when their scope applies:

- measurement-and-evidence.md — measurement and evidence framework.
- experimentation.md — general experimentation framework.
- experiment.md — pre-test experiment brief format.
- experiment-learning.md — post-test validity, learning, transfer, and follow-up record.

### QA

Confirm event definitions and timezones match, test and production traffic are separated, duplicate paths are checked, values/currency are verified, attribution windows are visible, privacy boundaries are preserved, and “received” is not confused with “correct.” For a causal question, confirm the evidence level is stated, the method matches the constraints, the test was powered before launch, contamination and coincident events were assessed, the business outcome rather than a platform proxy was measured, and the estimate's scope is named. For experiment learning, confirm validity was assessed before direction, the pre-test decision rule was preserved, full relevant lag is included, nulls and guardrail harms are classified correctly, mechanism remains separate from observed effect, post-hoc slices are not promoted, transfer status does not exceed replication evidence, and contradictory prior results remain visible.

### Reference: attribution reconciliation ($tracking-measurement)

### Attribution Reconciliation

Use when platform, analytics, CRM, storefront, or payment totals disagree.

#### Align first

Match business definition, event date versus click date, timezone, currency, tax/shipping inclusion, gross versus net revenue, cancellation/refund treatment, attribution window, model, identity scope, and reporting maturity.

#### Reconciliation table

For every source show: metric definition; cohort/date basis; total; expected exclusions; known duplicates; modeled or unattributed share; lag; comparable adjusted total.

#### Interpret gaps

Common explanations include multi-touch overlap, view-through credit, cross-device identity, consent/modeling, offline import eligibility, duplicate events, missing server/browser coverage, refunds, timezone boundaries, and late conversion reporting.

Do not sum attributed revenue across platforms as incremental business revenue. Use controlled experiments or credible incrementality methods when the decision requires causal lift.

### Reference: causal evidence ladder ($tracking-measurement)

### Causal Evidence Ladder

Ranks how strongly a body of evidence supports the claim that marketing activity *caused* a business result. Use it to state what a conclusion may be used for — not to reject weaker evidence outright.

Classify with `KNOWLEDGE-TAXONOMY.md`. A ladder position is an evidence grade, never proof of an outcome.

#### Levels

| Level | Evidence | Supports |
|---|---|---|
| C0 | Platform-attributed conversions or revenue | Delivery and efficiency observations only. Never a causal claim |
| C1 | Multi-source correlation; before-and-after without a control | Hypotheses and prioritization |
| C2 | Modeled attribution or Marketing Mix Modeling with stated assumptions | Directional allocation, revisable |
| C3 | Quasi-experiment with a non-randomized comparison — matched markets, synthetic control, interrupted time series | Provisional causal estimate within the observed scope |
| C4 | Randomized experiment with a control group — user holdout, geo experiment, platform lift study, switchback | Causal estimate within the tested scope, population, and period |
| C5 | Replicated randomized evidence across periods, geographies, or accounts | Causal claim with an established scope of generalization |

#### Rules

- Platform attribution never exceeds C0 regardless of volume, consistency, or confidence. Sample size does not convert correlation into causality.
- A result's level is set by its weakest structural element. A randomized test with a contaminated control is not C4.
- State the scope with the level: population, geography, period, spend range, creative set, and seasonality. A C4 result is causal *inside that scope only*.
- Do not generalize across business models, funnel stages, or spend ranges without evidence at the new scope. A tactic proven in one scope is not proven.
- Scaling decisions require the level demanded by the `optimization-scaling` proof standard. Do not substitute a lower level and describe it as sufficient.
- Record the level in the output. An unlabeled causal claim is treated as C0.
- A negative result carries the same level as a positive one. Do not discount a null finding because it is unwelcome.

#### Choosing a target level

Match the level to the cost of being wrong, not to what is convenient:

- Reversible, low-spend, easily monitored change: C1–C2 may be enough.
- Sustained budget increase, channel entry or exit, or a structural rebuild: C3 minimum, C4 preferred.
- A claim that will be reused as a rule across accounts or periods: C5.

If the achievable level is below what the decision needs, say so and either lower the commitment, make the change reversible, or run the test first.

### Reference: event integrity ($tracking-measurement)

### Event Integrity

Use this reference for a conversion, lead, purchase, or funnel-event audit.

#### Event contract

For each event record:

- Business meaning and qualifying condition
- Trigger location and trigger owner
- Browser, server, app, CRM, or imported source
- Required parameters and accepted types
- Event ID and deduplication scope
- User/session/order/lead identifiers and privacy treatment
- Value, currency, quantity, item, and tax/shipping rules
- Timestamp and timezone
- Consent dependency
- Receiving destinations
- Counting rule and optimization role

#### Tests

Cover valid completion, duplicate submission, refresh/back navigation, payment failure, cancellation/refund where relevant, cross-domain transition, consent accepted/denied, ad blocker or network loss, mobile/desktop, and delayed server delivery.

Grade each test as `verified`, `failed`, `not observed`, or `not applicable`. A debugger signal proves dispatch only; confirm receipt and reporting separately.

### Reference: experiment learning system ($tracking-measurement)

### Experiment Learning System

Use this reference when experiments need to become durable, reusable knowledge rather than isolated result screenshots or "winner" labels.

`$tracking-measurement` owns experiment validity and the evidence state of the resulting learning. The domain skill that owns the marketing decision still owns what to do with that learning.

#### Core principle

An experiment result is scoped evidence, not a universal best practice.

Every learning must preserve:

- the decision and hypothesis tested
- population, surface, geography, period, and operating conditions
- treatment/control definition and implementation fidelity
- primary business metric and guardrails
- measurement integrity and causal evidence level
- estimate, uncertainty, and minimum detectable effect where applicable
- result validity before result direction
- what was observed versus the explanation proposed for it
- what can and cannot be transferred to another context

A test can be statistically clean and still have narrow external validity.

#### Result classes

Classify the test before promoting any learning:

1. **Valid — supports hypothesis**: design and measurement were decision-ready and the result supports the pre-registered directional claim within scope.
2. **Valid — contradicts hypothesis**: design was decision-ready and the result provides evidence against the pre-registered claim within scope.
3. **Valid — inconclusive / null**: the result does not resolve the decision at the required effect threshold. Record the uncertainty and MDE; do not call the control a winner by default.
4. **Valid — harmful on guardrail**: primary metric may improve, but a pre-specified business guardrail crosses the stop or rejection threshold.
5. **Invalid / compromised**: instrumentation, allocation, contamination, implementation drift, early stopping, missing lag, or another defect prevents the intended inference.

Do not collapse these into `win / lose`.

#### Learning loop

##### 1. Link to the pre-test decision

Start from the approved experiment brief. Record:

- evidence-backed problem
- hypothesis and expected mechanism
- control and variant
- primary metric and business guardrails
- pre-registered decision rule
- required and achievable evidence level

If no pre-test record exists, label the analysis post hoc and lower the strength of any mechanism claim accordingly.

##### 2. Validate execution before reading direction

Check:

- allocation and exposure integrity
- treatment/control fidelity
- instrumentation health
- conversion lag completeness
- sample/duration requirements
- contamination and coincident changes
- stop-rule adherence
- whether the primary metric was changed or redefined

A favorable result does not repair a broken test.

##### 3. Record the result with uncertainty

Capture the business-outcome estimate, confidence/credible interval or other decision-appropriate uncertainty, sample/exposure, guardrail outcomes, and evidence level.

Do not substitute CTR, engagement, platform-attributed revenue, or another proxy for the pre-specified business outcome merely because it moved more clearly.

##### 4. Separate observation from explanation

Write two statements:

- **Observed result**: what changed within the measured scope.
- **Mechanism interpretation**: why the change may have happened.

The mechanism remains an inference unless the design separately isolates it.

A significant outcome does not automatically prove the story used to explain it.

##### 5. Decide the operational disposition

Choose one:

- `ship within tested scope`
- `reject within tested scope`
- `iterate and retest`
- `replicate before wider use`
- `collect more data`
- `invalidate and rerun`
- `stop because guardrail harm outweighs benefit`

The domain owner makes the business action decision; `$tracking-measurement` states what the evidence supports.

##### 6. Create a scoped learning record

Use `templates/experiment-learning.md`.

A useful learning statement follows this pattern:

`In [population/surface/context], changing [controlled variable] from [control] to [variant] produced [observed effect and uncertainty] on [primary business outcome] during [period], at [evidence level]. This supports/contradicts/does not resolve [hypothesis]. It does not establish [unproven mechanism or transfer claim].`

Avoid generic summaries such as "short copy wins" or "UGC converts better."

##### 7. Assign transfer status

Use the narrowest justified status:

- **Local result** — one valid test in one defined context.
- **Replication candidate** — worth testing in a comparable context; not yet a reusable pattern.
- **Replicated scoped pattern** — independently repeated across at least two comparable tests with compatible results and no unresolved validity conflict.
- **Segment-specific pattern** — results differ materially by segment/context and the difference is supported by pre-specified or replicated evidence.
- **Contradicted / unstable** — comparable tests conflict; do not promote until the boundary or source of heterogeneity is understood.

Replication count alone is not enough; tests must be sufficiently independent and comparable.

##### 8. Generate the next hypothesis

Use the result to reduce uncertainty rather than to maximize test count.

Good next hypotheses come from:

- unresolved mechanism
- a boundary condition exposed by the result
- guardrail tradeoff
- segment heterogeneity that was pre-specified or deserves a new test
- a failed implementation assumption
- a promising local result that needs replication before broader use

Do not manufacture a new hypothesis merely to keep an arbitrary experiment cadence.

#### Experiment backlog

Maintain a backlog only for decision-relevant tests. Each item should include:

| Field | Purpose |
|---|---|
| Decision | What choice the experiment will inform |
| Evidence-backed problem | Why the test exists |
| Hypothesis | Falsifiable prediction |
| Expected mechanism | Why the change might affect the outcome |
| Scope | Population, surface, geography, channel, offer state |
| Existing evidence | Research, diagnostics, prior tests, external evidence |
| Required evidence level | Strength needed for the decision |
| Primary business outcome | What will call the test |
| Guardrails | What must not deteriorate |
| Feasibility / dependencies | Traffic, instrumentation, production, legal, capacity |
| Risk | Cost of being wrong or causing harm |
| Learning value | What uncertainty the test resolves even if it does not win |
| Status | proposed, approved, running, concluded, parked |

##### Prioritization rule

Prioritize from actual decision impact, evidence strength, uncertainty, reversibility, feasibility, risk, and learning value.

A scoring model such as ICE or RICE may be used as a convenience only when its inputs are grounded and the resulting rank does not override a material risk, evidence gap, or strategic dependency. Do not invent numeric confidence to make a scoring table look precise.

#### Knowledge promotion rules

- A single test never becomes a universal "best practice."
- A local result may be implemented locally when the decision rule supports it without being promoted into reusable doctrine.
- Post-hoc segment cuts are hypothesis generators unless independently validated; do not promote the most favorable slice.
- External case studies, competitor tests, platform benchmarks, and published examples are prior evidence, not local experimental proof.
- A repeated result with materially different contexts may suggest a broader pattern, but only after the relevant differences are examined rather than ignored.
- Conflicting evidence is retained. Do not delete a past loser after a later test wins.
- A result that depends on a specific offer, price, creative, audience, market, or platform state keeps that dependency in the learning record.
- Platform or interface changes can invalidate transfer assumptions; apply `PLATFORM-CURRENCY.md` when current mechanics matter.
- A causal evidence level is never upgraded because a result was replicated using the same flawed design.

#### Using prior learning

Before launching a new experiment, search prior learning for:

- same decision
- same mechanism
- same segment or buying situation
- same surface/channel
- same offer and commercial conditions
- known guardrail failures
- contradictory results

Prior learning should change the new test's hypothesis, design, required evidence level, or priority. If it changes nothing, the archive is not functioning as an operating system.

#### Output

Return:

- experiment validity class
- observed result and uncertainty
- causal/evidence level
- guardrail status
- observation versus mechanism interpretation
- operational disposition
- scoped learning statement
- transfer status
- contradictions or dependencies
- next hypothesis or explicit reason no follow-up is justified
- backlog change, if any
- exact status

#### QA

Confirm the pre-test decision rule was preserved; validity was assessed before direction; the full conversion lag is included; a null is not mislabeled a loss; guardrail harm is visible; post-hoc slices are not promoted to proof; the mechanism is separated from the observed effect; scope is preserved; replication does not erase contradictions; external evidence is not mislabeled local proof; and no arbitrary experiment-velocity target overrides decision value.

### Reference: geo experiments ($tracking-measurement)

### Geo Experiments and Quasi-Experimental Designs

Used when users cannot be split cleanly but geographies can. Randomized geo assignment reaches C4; matched or synthetic designs reach C3.

#### Randomized geo experiment

Randomly assign comparable regions to treatment and control, change spend in treatment only, and compare business outcomes.

- Require enough regions for randomization to balance. A handful of large markets does not randomize; it pairs.
- Regions must be economically independent. Adjacent metros, shared media markets, and national retail or delivery footprints leak.
- Balance on pre-period outcome level, trend, seasonality, and size — then verify balance rather than assuming it.
- Run for the full conversion lag plus a stable post-change period.

#### Matched-market test (C3)

Where randomization is impossible, pair each treated region with the most similar untreated region on pre-period behavior. This is quasi-experimental: unobserved differences remain a competing explanation, and the estimate is provisional.

#### Synthetic control and interrupted time series (C3)

Construct a counterfactual from a weighted combination of untreated regions, or model the pre-period series and compare post-change deviation. Both require a stable, well-fitted pre-period and no coincident shock. Report the pre-period fit; a design that cannot reproduce the pre-period does not support a post-period claim.

#### Switchback

Alternate treatment on and off on a fixed schedule within the same region. Suitable only when the effect is short-lived relative to the switching interval. Carryover between periods biases the estimate toward zero; state the assumed carryover window and make the interval longer than it.

#### Common failures

- National promotions, PR events, or competitor activity overlapping the window.
- Regional seasonality differing between arms — weather, holidays, term dates, paydays.
- Insufficient regions for the effect size sought.
- Spend changed in treatment without verifying delivery actually changed.
- Measuring platform-attributed conversions by region instead of business outcomes by region.
- Population differences mistaken for treatment effect because balance was assumed, not tested.

#### Reading the result

Report effect size, confidence interval, minimum detectable effect, pre-period balance or fit, and every coincident event considered and excluded. State the design level (C3 or C4) explicitly, and name the scope in which the estimate holds.

### Reference: holdout experiments ($tracking-measurement)

### User-Level Holdout Experiments

Randomly withholds treatment from a share of users and compares business outcomes. The strongest routinely available design (C4).

#### Design

Define the population, randomization unit, split, primary business outcome, minimum detectable effect, duration including full conversion lag, and stopping rule before launch.

- Randomize at the level at which contamination occurs — usually the user or household, not the session or device.
- Size the holdout for power, not for comfort. A holdout too small to detect the expected effect produces an uninformative null.
- Hold the control for the entire period. Releasing it early destroys the comparison and cannot be repaired analytically.
- Measure in the business source of truth, joined to assignment. Platform-reported lift is the platform grading its own work.

#### Contamination

The most common cause of a false null. Check each before trusting a result:

- Cross-device and logged-out users landing in both arms.
- Shared households or accounts.
- Other channels retargeting the control group.
- Organic, email, or lifecycle activity correlated with assignment.
- Brand spillover from the treated group.
- Assignment leaking through audience syncs or lookalike seeds built on treated users.

Record the contamination risk and its direction. Contamination almost always biases toward zero, so a null under known contamination is not evidence of no effect.

#### Reading the result

- Report effect size with its confidence interval, not a point estimate alone.
- Report the minimum detectable effect alongside any null.
- Convert to business terms — incremental contribution, not incremental attributed conversions.
- Subtract the holdback's forgone revenue when stating the test's net value.
- State the scope: population, period, spend range, creative set. The estimate holds there and is not established elsewhere.

#### Rules

- Do not stop early on a favorable read. Do not extend a test to reach significance.
- Do not change targeting, budget, creative, or bidding mid-test; the result then measures the bundle, not the treatment.
- Do not reuse a holdout group across concurrent tests without accounting for interaction.
- A holdout answers whether the tested spend was incremental at that level. It does not establish the incrementality of a larger budget.

### Reference: incrementality method selector ($tracking-measurement)

### Incrementality Method Selector

Selects how to measure incremental effect. There is no universally correct method; the constraint set decides.

#### Inputs required before selecting

Decision being made and cost of being wrong; required evidence level from the causal ladder; spend under test; expected effect size; available unit of randomization; geographic or audience independence; sample size and power; contamination risk; seasonality and known events; conversion lag; platform availability of the mechanism; ability to hold a control for the full period; and who authorizes the holdback.

Absent inputs are recorded `unknown` by `$marketing-intake`. Do not select a method by defaulting an unknown.

#### Selection

| Condition | Method | Reference |
|---|---|---|
| Platform supports randomized user split and the audience can be held out | User-level holdout | Holdouts |
| Users cannot be split cleanly, but regions are independent and numerous enough | Geo experiment or matched-market test | Geo experiments |
| Platform offers a native randomized lift mechanism and its design is acceptable | Platform lift study | Lift studies |
| Effect is short-lived and treatment can alternate on a schedule | Switchback | Geo experiments |
| No control is possible, but a comparable untreated series exists | Synthetic control or interrupted time series (C3) | Geo experiments |
| Question is long-horizon cross-channel allocation, not a single change | Marketing Mix Modeling (C2) | Marketing Mix Modeling |
| Several imperfect sources exist and no single test is decisive | Triangulate | Triangulation |

#### Disqualifiers

Do not run the test if any holds — fix the condition or lower the decision's commitment instead:

- Measurement integrity is unresolved. A causal test inherits every collection defect beneath it.
- The control cannot be held for the full period plus conversion lag.
- Expected effect is smaller than the design can detect; the likely result is an uninformative null read as "no effect."
- Treatment and control cannot be kept separate — shared audiences, overlapping geographies, cross-device users, brand spillover.
- A promotion, launch, outage, or seasonal peak overlaps the window and cannot be excluded.
- The holdback's revenue cost exceeds the value of the decision it informs.

#### Rules

- Power the test before running it. State minimum detectable effect, duration, and required volume in advance; a test that cannot detect the effect it seeks is not evidence.
- Fix the stopping rule and primary metric before launch. Do not stop early on a favorable read, and do not switch the primary metric after seeing results.
- One primary metric, defined by `$marketing-intake` before launch. Secondary metrics are supporting only.
- Measure the business outcome, not the platform-attributed proxy.
- Include the full conversion lag in the measurement window.
- A null result is a result. Report it with its minimum detectable effect so absence of evidence is not read as evidence of absence.
- Record cost: the holdback's forgone revenue is part of the test's price and belongs in the decision.

### Reference: marketing mix modeling ($tracking-measurement)

### Marketing Mix Modeling

Regression-based estimation of channel contribution from aggregate time-series data. Answers long-horizon allocation questions that experiments cannot cover cheaply. Caps at C2: modeled, assumption-dependent, and revisable.

#### What it is for

Cross-channel allocation over months or years, including channels with no click path — offline, television, out-of-home, sponsorship — and periods where user-level measurement is unavailable. It is not a substitute for an experiment on a specific change, and not a tool for weekly optimization.

#### Requirements

Sufficient history relative to the number of channels; genuine variation in spend across channels and time; recorded prices, promotions, distribution changes, competitor activity, and seasonality; and a business outcome series from the source of truth.

Without spend variation there is nothing to identify. A channel held at a constant budget cannot have its contribution estimated, and a model that reports one for it is fitting noise.

#### Assumptions to state explicitly

Functional form; diminishing-returns and saturation shape; adstock or carryover length; which confounders are included; how seasonality and trend are handled; and how correlated channels are separated.

Every one of these is a modeling choice, not an observation. Two defensible specifications can produce materially different channel contributions from the same data. Report the specification alongside the result.

#### Validation

- Hold out a period and test out-of-sample fit; in-sample fit alone means nothing.
- Test stability across specifications. A contribution estimate that moves sharply under a reasonable alternative is not decision-grade.
- Calibrate against experimental results where they exist. Experiments discipline the model; the model does not overrule the experiment.
- Report confidence intervals. A point estimate of channel contribution without an interval overstates precision.

#### Rules

- Never present a modeled contribution as a measured outcome, and never use it to claim causality for a specific campaign or change.
- Correlated channels — often brand search and everything upstream of it — cannot be cleanly separated by a model alone. State the collinearity rather than reporting a confident split.
- Do not use a model to justify a budget increase beyond the spend range present in its data. Outside that range it extrapolates.
- Do not reconcile a model against platform attribution by adding or averaging them; they answer different questions.
- Re-estimate on a stated cadence. A model is a snapshot of a period, and it decays.

### Reference: measurement triangulation ($tracking-measurement)

### Measurement Triangulation

Combines experimental, modeled, attributed, and business evidence when no single source is decisive. Triangulation raises confidence through agreement — it does not average sources into a number.

#### Method

1. State the decision and the evidence level it requires.
2. List every available source with its causal ladder level, scope, and known bias direction.
3. Compare direction first, then magnitude. Agreement on direction across independent methods is the substantive finding; agreement on magnitude is rarer and stronger.
4. Where sources disagree, identify the mechanism — different outcome definitions, windows, populations, periods, or a genuine effect difference — before choosing what to believe.
5. Weight by evidence level and scope fit, not by convenience or recency.
6. State the resulting confidence and what would change it.

#### Rules

- Never sum attributed conversions across platforms. Overlapping attribution double-counts, and the total is not a business outcome.
- Never average an experimental estimate with an attributed one. They are different quantities; the mean of the two means nothing.
- Sources sharing a defect are not independent. Two platforms reading the same broken tag agree because they are wrong together.
- Disagreement between a randomized experiment and platform attribution is expected, not an error to be reconciled away. The experiment governs within its scope.
- A modeled result calibrated to an experiment inherits that experiment's scope, not a broader one.
- The overall claim takes the level of the evidence actually supporting it, not the highest level present among the sources.
- Where triangulation cannot resolve a disagreement, report the range and the competing explanations rather than selecting one.

#### Output

Decision; required level; source table with level, scope, and bias direction; direction agreement; magnitude range; unresolved disagreements with competing explanations; resulting confidence; what evidence would change the conclusion; and the recommended action with its reversibility.

### Reference: platform lift studies ($tracking-measurement)

### Platform Lift Studies

Randomized studies run by the ad platform itself — Conversion Lift, Brand Lift, and equivalents. Convenient and genuinely randomized, but graded by the seller.

#### What they can support

A well-designed platform lift study is randomized and can reach C4 **for the outcome the platform measures, in the population it holds out, over the window it defines**. It does not establish business-level incrementality unless its conversion definition matches the business source of truth.

#### Verify before accepting

- Randomization unit and whether the holdout is genuinely withheld from all of the advertiser's activity on that platform, or only from the tested campaign.
- Conversion definition and whether it matches the primary business outcome.
- Whether reported conversions are modeled; a modeled outcome inside a randomized design caps the level below C4.
- Attribution window and whether it covers the full conversion lag.
- Holdout size and the study's minimum detectable effect.
- Whether the platform selected the study population in a way correlated with likelihood to convert.
- Whether other channels continued reaching the holdout.

#### Rules

- Do not treat platform lift as independent verification of that platform's own attribution. It is the same party measuring its own contribution with a better method.
- Do not compare lift results across platforms as if they used one definition. Each defines outcome, window, and holdout differently; the numbers are not commensurable and must not be added.
- Reconcile the study's conversion counts against the business source of truth before using its lift estimate commercially.
- A lift result at the campaign level does not establish incrementality of the platform's whole budget, nor of a larger budget.
- Record who designed, ran, and analyzed the study as part of its provenance.

#### When to prefer an independent design

Prefer a user holdout or geo experiment when the decision is large, when the platform's holdout cannot exclude the advertiser's other activity, when the conversion definition cannot be reconciled, or when the result would be used to justify sustained budget increases.
