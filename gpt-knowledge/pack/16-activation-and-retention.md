<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Activation, Retention, and Customer Economics

## Skill: $activation

**Use when:** Define and improve the post-conversion path to first meaningful customer value using evidence-backed activation criteria, time-to-value, friction diagnosis, and controlled interventions; not for inventing an “aha moment,” treating onboarding completion as value by default, or taking over CRO, lifecycle messaging, retention strategy, product implementation, or retention economics.

Activation owns the decision between acquisition/conversion and ongoing retention: what behavior or outcome credibly represents first meaningful value, how customers reach it, where they fail to reach it, and which interventions should be tested. Once the customer has reached first meaningful value, `$retention-strategy` owns why they later fail to continue, renew, repurchase, or return and which retention intervention should be tested.

Activation is not automatically a stage every business needs. If the purchase or conversion itself substantially realizes the promised value and there is no meaningful post-conversion setup/use milestone, state that no separate activation layer is decision-relevant rather than forcing a SaaS funnel onto the business.

Classify activation artifacts with `KNOWLEDGE-TAXONOMY.md`. An activation heuristic or common “aha moment” pattern is a hypothesis input, not evidence that a specific event predicts value or retention for this business.

### Inputs

Before a decision-grade activation recommendation, confirm:

- business model, primary business outcome, and lifecycle-stage definitions
- promised outcome and product/service truth
- post-conversion customer journey from signup/purchase/lead acceptance to first meaningful value
- candidate value events and their instrumentation quality
- customer research, support/success evidence, usability evidence, and observed behavior where available
- segment/cohort definitions and expected time-to-value range
- downstream retention, repeat-use, renewal, refund, or qualified-revenue evidence when available
- operational/product/service constraints and authorization boundary

If the value event cannot be measured reliably, route instrumentation integrity to `$tracking-measurement` before treating activation rate as decision-ready.

### Method

1. **Confirm whether a distinct activation stage exists.** Identify the conversion boundary and ask whether meaningful customer value occurs after it. Do not manufacture a stage when the conversion itself is the useful outcome.
2. **Define first meaningful value.** Use Activation definition and evidence. Separate customer value from business convenience and from easy-to-track onboarding events.
3. **Map the path to value.** Use Path to value and friction. Map required steps, dependencies, wait states, handoffs, customer effort, uncertainty, and failure points.
4. **Measure activation correctly.** State eligible denominator, activation event, window, segment, exclusions, instrumentation state, and time-to-value distribution. Do not report one blended rate across incompatible cohorts or journey variants.
5. **Diagnose the first binding barrier.** Distinguish product/service availability, setup complexity, comprehension, motivation, trust, missing data/integration, operational delay, poor-fit acquisition, technical defect, and measurement failure.
6. **Choose the smallest meaningful intervention.** Remove unnecessary friction, improve guidance, change sequencing, add assistance, clarify expectations, or redesign a handoff only where evidence supports the mechanism. Route owned-channel trigger/cadence design to `$lifecycle-marketing`, wording to `$copywriting`, and surface-level conversion UX to `$cro` where relevant.
7. **Define the test and guardrails.** Use Activation experiments and handoffs. Primary outcome should reflect meaningful value or a validated activation proxy; guardrails may include refund/cancellation, support burden, quality, safety/compliance, retention, and downstream revenue.
8. **Record learning and exact state.** Proposed activation definitions remain hypotheses until evidence supports them. Implemented journey changes are not verified until the expected behavior and downstream guardrails are observed. If the remaining problem occurs after first meaningful value, hand the intervention question to `$retention-strategy` rather than extending Activation indefinitely.

### Rules

- Do not call an event “activation” merely because it is common in the category, easy to instrument, or correlated in one unadjusted analysis.
- Do not invent an “aha moment.” If several candidate events exist, preserve uncertainty and design evidence collection or testing.
- Onboarding completion, tutorial completion, profile completion, email open/click, number of sessions, or feature clicks are supporting events unless evidence shows they represent or predict meaningful value in scope.
- Faster time-to-value is not universally better. Necessary qualification, safety, setup, education, compliance, or service work must not be removed just to shorten the clock.
- Do not optimize activation rate by shrinking the denominator, excluding hard customers after the fact, changing the activation window post hoc, or redefining the event after seeing results.
- Do not confuse activation with retention strategy or retention economics. Activation concerns first meaningful value; `$retention-strategy` owns cause/intervention after first value; `$retention-economics` owns repeat/renewal/churn economics after cohorts mature.
- Do not confuse activation with lifecycle messaging. `$lifecycle-marketing` owns communication triggers/cadence; activation owns the journey decision those communications support.
- Do not diagnose poor activation as onboarding friction before checking poor-fit acquisition, product/service failure, technical defects, operational delay, and measurement integrity.
- Product or service implementation changes remain outside this skill's execution authority unless an appropriate implementation owner and approval exist.
- A journey change that lifts an activation proxy but worsens refunds, cancellations, quality, support burden, safety/compliance, or downstream value is not a clean win.

### Output

Activation decision: business model and conversion boundary; whether a distinct activation layer exists; first meaningful value definition and evidence strength; eligible denominator/window/segment; activation and time-to-value baseline; path-to-value map; diagnosed barrier; intervention hypothesis; required owner handoffs; primary outcome and guardrails; experiment/validation plan; implementation dependencies; approval needs; exact status.

### Library references

Owned root artifacts, read when their scope applies:

- activation-plan.md — canonical activation definition, journey, diagnosis, intervention, measurement, and learning record.

### Related owners

- `$marketing-intake`: lifecycle definitions, shared context, evidence state, authorization
- `$customer-research`: customer-reported friction, desired progress, qualitative evidence
- `$icp-jtbd`: segment, JTBD, poor-fit acquisition, buying situation
- `$offer-strategy`: promised outcome and expectation boundary
- `$cro`: pre-conversion surfaces and bounded page/form UX friction
- `$lifecycle-marketing`: owned-channel onboarding/activation triggers, segmentation, cadence
- `$copywriting`: onboarding/help/message wording
- `$tracking-measurement`: event integrity, causal test validity, experiment learning
- `$retention-strategy`: post-first-value retention/lapse/cancellation reason diagnosis and intervention strategy
- `$retention-economics`: repeat-use, renewal, churn, LTV, payback measurement after activation
- `$marketing-operations`: recurring activation monitoring/decision loops when needed

### QA

Confirm a distinct activation stage actually exists, the value event is not chosen for tracking convenience, denominator/window/segment are fixed before reading the result, instrumentation is decision-ready, downstream guardrails are included, plausible alternative causes are checked, lifecycle/CRO/product/retention boundaries are preserved, and no activation definition or journey change is described as proven before evidence supports it.

### Reference: activation definition and evidence ($activation)

### Activation Definition and Evidence

Use this reference when deciding what counts as activation and whether the current definition is strong enough for decisions.

#### Core distinction

Activation is the first behavior or outcome that credibly indicates the customer has received meaningful value from the product, service, or relationship. It is not automatically the first logged-in session, setup step, tutorial completion, purchase confirmation, or any event labeled “activation” in an analytics tool.

A valid activation definition should satisfy three questions:

1. **Value:** does the event represent customer progress toward the promised outcome?
2. **Specificity:** is the event meaningfully different from mere presence, setup, or administrative completion?
3. **Evidence:** what supports the claim that this event matters in this business and segment?

#### Evidence ladder for activation candidates

From weaker to stronger decision support:

- **Category convention:** another company or framework calls this event activation.
- **Internal assertion:** team believes the event is the “aha moment.”
- **Qualitative evidence:** customers consistently describe this step as the point value became clear or useful.
- **Observed behavioral association:** customers reaching the event show different downstream behavior, with cohort/segment and obvious confounding considered.
- **Replicated predictive evidence:** the association holds across comparable cohorts and periods.
- **Controlled evidence:** an intervention that changes reaching the event also changes a downstream value outcome under a valid design.

Do not collapse this ladder into “proven/not proven.” State the current level and what uncertainty remains.

#### Candidate event test

For each candidate event, record:

| Question | Answer |
|---|---|
| Customer progress represented | |
| Why this is more than setup/admin | |
| Segment(s) where relevant | |
| Earliest plausible time | |
| Latest useful window | |
| Instrumentation source | |
| Evidence linking it to value | |
| Evidence linking it to retention/revenue | |
| Known confounders | |
| Failure modes / gaming risk | |
| Current status | hypothesis / provisional / supported / contradicted |

#### Business-model examples as hypotheses, not defaults

- **SaaS/app:** completing a real job, publishing/using a core output, connecting required data and receiving a useful result.
- **Marketplace:** completing the first successful value exchange, not merely creating a listing or account.
- **Service:** completing the first substantive delivery or achieving an agreed milestone, not just booking the kickoff.
- **Lead generation:** a qualified lead reaching a meaningful sales/service step may be an activation-like milestone, but do not relabel lead progression when the customer has not yet received value.
- **Subscription/ecommerce:** receipt, first use, successful replenishment setup, or another post-purchase event can matter when meaningful value occurs after purchase. If purchase itself is the decision-relevant outcome and no post-purchase activation decision exists, do not create one.

These are prompts for analysis, never universal definitions.

#### Metric contract

Every activation rate needs:

- eligible population and entry event
- exclusions fixed before analysis
- activation event definition
- observation window
- segment/cohort basis
- numerator and denominator source
- late-arriving event handling
- identity/stitching rules when relevant
- instrumentation quality state

`Activation rate = customers who meet the defined activation criterion within the defined window / eligible customers entering the activation journey`

The formula is only useful after the denominator and event are valid.

#### Time to value

Report a distribution where possible rather than only an average:

- median time to value
- relevant percentiles or bands
- censored/not-yet-activated share
- segment differences
- operational waiting time versus active customer effort where distinguishable

A faster value time is only desirable when value quality and guardrails remain intact.

#### Correlation caution

Customers who activate may already be more motivated, better fit, better resourced, or easier to serve. An observed retention difference does not prove the activation event caused retention.

Use `$tracking-measurement` when the decision requires a causal claim.

#### Anti-gaming rules

Do not:

- define activation as a step almost everyone completes just to make the rate look strong
- exclude slow or difficult customers after results are known
- expand the window after a miss without preserving the original read
- choose whichever candidate event correlates best after scanning many events and present it as pre-specified proof
- count synthetic/system-generated events as customer value without validating what they mean
- convert email clicks or tutorial completion into value because they are easy to move

#### When no activation definition is needed

State `no distinct activation layer` when:

- the primary customer value is substantially realized at conversion/purchase itself, and
- there is no decision-relevant post-conversion milestone the marketing system can or should manage separately.

This is a valid conclusion, not a missing framework.

### Reference: activation experiments and handoffs ($activation)

### Activation Experiments and Handoffs

Use this reference after the activation definition and first binding barrier are explicit.

#### Experiment contract

An activation experiment should specify:

- target segment/cohort
- journey entry event
- activation definition and window fixed before reading results
- diagnosed barrier and evidence
- intervention and mechanism hypothesis
- control/comparison when feasible
- primary business-relevant activation outcome
- supporting journey metrics
- downstream guardrails
- instrumentation and identity requirements
- exposure/allocation method
- decision window matched to value timing
- stop/rollback conditions
- implementation owner and authorization state

Route causal-validity design to `$tracking-measurement` when the conclusion needs to be causal.

#### Metric hierarchy

##### Primary
Prefer the defined meaningful-value event or a validated proxy.

##### Supporting
Examples:

- step completion
- setup completion
- error rate
- assistance request
- time in step
- time-to-value
- abandon/stall rate

Supporting metrics diagnose why the primary result moved. They do not replace it.

##### Guardrails
Depending on the business:

- refund/cancellation
- complaint/support burden
- service capacity
- quality/error rate
- safety/compliance
- downstream retention/repeat use
- contribution/revenue quality
- lead/customer quality

#### Avoid activation metric gaming

Reject designs that:

- shorten the activation window after seeing a favorable early result
- change the denominator after randomization/exposure
- redefine activation to a more common event because the true value event did not move
- remove qualification or required safeguards to inflate completion
- auto-complete or system-generate the event being measured
- optimize tutorial/checklist completion while value is unchanged
- ignore negative downstream effects because activation rate increased

#### Handoff map

Activation often diagnoses a problem whose implementation belongs elsewhere.

##### `$tracking-measurement`
Owns event integrity, attribution/reconciliation where relevant, causal method, experiment validity, and post-test learning classification.

##### `$lifecycle-marketing`
Owns onboarding/activation communication segmentation, triggers, cadence, suppression, and deliverability.

##### `$copywriting`
Owns the wording for approved onboarding, help, instructional, reminder, and reassurance messages.

##### `$cro`
Owns bounded page/form/conversion-surface UX where the activation intervention uses those surfaces. Activation keeps ownership of the post-conversion value decision.

##### `$icp-jtbd`
Owns upstream segment/fit decisions when low activation is caused by poor-fit acquisition rather than the activation journey.

##### `$offer-strategy`
Owns promise/deliverable expectation changes when the journey reveals a mismatch between what was sold and what customers actually receive.

##### `$retention-economics`
Owns mature downstream cohort effects. Activation should not claim that a lift in first value guarantees improved LTV or churn.

##### `$marketing-operations`
Owns recurring activation-health checks, condition watches, state, alert dedupe, escalation, and runtime truth when a repeated operating loop is needed.

##### Product/service/operations owner
Owns product feature, fulfillment, service process, integration, support, or operational implementation not governed by a Marketing OS specialist.

Do not hide an ownership gap by pretending Activation can implement product or service changes directly.

#### Decision outcomes

Classify an activation experiment or intervention as:

- supports the local hypothesis
- contradicts the local hypothesis
- inconclusive / underpowered / immature
- guardrail harm
- invalid / compromised

Then route the learning record to `$tracking-measurement`'s Experiment Learning System. A local activation win does not become a universal onboarding best practice.

#### Rollout

Before wider rollout confirm:

- the value definition is unchanged
- source instrumentation is healthy
- the affected segment matches the evidence scope
- guardrails cleared the intended observation window
- operational capacity can support the change
- any new lifecycle communications preserve consent/suppression rules
- any product/service mutation has the correct implementation owner and approval
- rollback path is known where reversible

#### Exact status

Keep these separate:

`hypothesis → designed → approved → configured/implemented → live → observed → verified`

Do not call an activation program “working,” “optimized,” or “verified” merely because the intervention was launched or a supporting metric moved.

### Reference: path to value and friction ($activation)

### Path to Value and Friction

Use this reference to map the post-conversion journey from entry into the customer relationship to first meaningful value.

#### Build the path

Start with the conversion boundary, then map only steps necessary to reach meaningful value.

For each step record:

| Field | Meaning |
|---|---|
| Step | Customer or system action |
| Why required | Value, safety, compliance, setup, qualification, or avoidable legacy process |
| Owner | Customer, product, service team, partner, system |
| Active effort | Work the customer must perform |
| Wait time | Delay outside active effort |
| Dependency | Data, approval, integration, inventory, human service, etc. |
| Failure signal | What shows the step failed or stalled |
| Evidence | Analytics, support, usability, interviews, operations |
| Removability | required / simplify / sequence / automate / uncertain |

#### Friction taxonomy

Do not label every delay “UX friction.” Diagnose the mechanism.

##### Comprehension
Customer does not understand what to do, why it matters, or what success looks like.

##### Motivation / relevance
The customer understands the action but does not see enough value to complete it. Check poor-fit acquisition and expectation mismatch before adding reminders.

##### Effort
The step requires too much work, repeated entry, complex setup, or unnecessary coordination.

##### Technical defect
Error, broken integration, unavailable feature, payment/account state, performance problem, identity issue, or bad data prevents progress.

##### Trust / anxiety
Customer hesitates because access, permissions, privacy, risk, quality, or consequences are unclear.

##### Dependency
Value depends on another person, dataset, inventory item, approval, implementation team, or external platform.

##### Operational delay
The business itself is slow: fulfillment, support, onboarding call, approval, scheduling, service delivery, or inventory.

##### Qualification / fit
The customer cannot reach value because the product/service is a poor fit, required prerequisites are absent, or acquisition brought the wrong customer.

##### Measurement failure
The customer may have reached value, but events are missing, duplicated, delayed, or defined incorrectly.

#### First binding barrier

Prioritize the earliest barrier that materially prevents a qualified customer from reaching value. Do not optimize a later tutorial screen if customers are stalled earlier by missing data or fulfillment.

A useful diagnosis states:

`Observed stall → affected segment → evidence → plausible mechanism → competing explanations → owner → intervention hypothesis`

#### Necessary versus unnecessary friction

Some friction protects the customer or business:

- identity verification
- qualification
- consent
- safety/compliance checks
- required setup for accurate results
- expectation setting
- data permissions
- service preparation

Do not remove necessary friction merely to improve activation rate or time-to-value. Instead ask whether it can be made clearer, better sequenced, more transparent, assisted, or faster without weakening its purpose.

#### Journey variants

Do not blend materially different journeys:

- self-serve versus assisted
- free/trial versus paid
- mobile versus desktop when setup differs
- plan/tier/package differences
- new versus migrated customer
- market/geography where operations differ
- acquisition source when it materially changes fit or expectation

A blended activation rate can hide a broken journey or a mix shift.

#### Intervention families

Use only when the diagnosed mechanism supports them:

- remove a nonessential step
- prefill or reuse known data
- reorder steps so value appears earlier
- progressive setup rather than all-at-once setup
- better expectation setting
- contextual guidance
- human assistance or escalation
- clearer permissions/trust explanation
- operational SLA/process fix
- technical fix
- qualification improvement upstream
- lifecycle reminder/trigger through `$lifecycle-marketing`
- copy clarification through `$copywriting`
- bounded surface UX improvement through `$cro`

Do not default to tooltips, checklists, gamification, email sequences, discounts, or concierge onboarding without evidence of the barrier they solve.

#### Time decomposition

When useful, separate:

`Total time to value = customer active effort + system processing + business operational wait + external dependency wait`

This prevents blaming the customer journey for a fulfillment or operations problem.

#### Output

Return a path-to-value map, the first binding barrier, evidence and competing explanations, the responsible owner, and the smallest meaningful intervention to validate next.

## Skill: $retention-strategy

**Use when:** Diagnose why customers fail to continue, renew, repurchase, or return and design cause-matched retention, save, recovery, repeat-purchase, and win-back interventions using customer, behavioral, operational, and economic evidence; not for default discounting, obstructing cancellation, or substituting retention rate for realized economics.

Retention Strategy owns the intervention decision after activation or initial value: why customers stay, lapse, cancel, fail to repurchase, or become at risk; which intervention matches that reason; and how that intervention should be validated.

It does not calculate lifetime value or retention curves (`$retention-economics`), define first meaningful value (`$activation`), own lifecycle communication mechanics (`$lifecycle-marketing`), set pricing (`$pricing-monetization`), or implement product/service fixes.

Classify outputs with `KNOWLEDGE-TAXONOMY.md`. A churn reason, save tactic, win-back pattern, or retention benchmark is a hypothesis input until supported in this business and segment.

### Inputs

Before a decision-grade recommendation, confirm:

- business model and the relevant continuation behavior: renew, repurchase, repeat use, continue service, or remain active
- segment/cohort, lifecycle state, activation state where relevant, and observation window
- realized retention/churn/repeat behavior and economics from `$retention-economics`
- cancellation, refund, support, payment-failure, product/service, fulfillment, usage, and customer-research evidence where available
- current offer, pricing/payment terms, service commitments, and known experience defects
- lifecycle communication state and consent/suppression constraints
- implementation owner and authorization boundary

If the apparent retention change may be a measurement or cohort-definition defect, route that dependency before intervention design.

### Method

1. **Define the retention decision.** State the continuation behavior, cohort, window, and business outcome. Do not use a generic churn percentage without naming what churn means here.
2. **Separate state from reason.** A customer can be active, at risk, voluntarily cancelled, involuntarily lost, dormant/lapsed, recovered, or won back. State the observed state before inferring why.
3. **Diagnose the cause.** Use Retention diagnosis and reason coding. Separate customer-stated reason, observed behavior, operational facts, commercial terms, and inference.
4. **Match intervention to cause.** Use Intervention selection and save/recovery. Fix defects before persuading; handle failed payment differently from poor fit, price objection, low need, service failure, or unmet promise.
5. **Choose the correct lifecycle objective.** Retention of an active customer, cancellation save, failed-payment recovery, repeat-purchase support, lapse prevention, and win-back are different decisions. Use Repeat, renewal, and win-back.
6. **Define the smallest meaningful intervention.** Route lifecycle triggers/cadence to `$lifecycle-marketing`, wording to `$copywriting`, pricing changes to `$pricing-monetization`, activation barriers to `$activation`, and product/service/operations fixes to the actual implementation owner.
7. **Define measurement and guardrails.** Primary outcomes may include retained paid status, realized repeat purchase, renewal, recovered payment, contribution, or qualified continuing usage. Guardrails include refunds, complaints, support burden, discount dependency, margin, involuntary churn recurrence, customer quality, and downstream retention.
8. **Record learning and exact state.** A launched intervention is not a proven retention strategy until the observation window and downstream guardrails are complete.

### Rules

- Do not default to discounts, coupons, pause offers, or win-back messages before diagnosing the reason for loss or risk.
- Do not obstruct cancellation, hide the cancel action, add deceptive friction, or force unwanted contact to inflate retention.
- Do not treat a cancellation-survey answer as the sole cause. Preserve stated reason separately from observed evidence and inference.
- Separate voluntary churn from involuntary churn. Failed payment, expired card, and billing errors require recovery mechanics, not persuasion by default.
- Do not call a save successful merely because cancellation was delayed. Verify continued paid/value behavior over a decision-relevant window.
- Do not call a discounted renewal a clean win without checking contribution, future renewal behavior, discount dependency, and customer mix.
- Do not treat higher repeat purchase rate or lower churn as sufficient if refunds, complaints, quality, margin, or support burden worsen materially.
- Do not win back customers whose reason for leaving remains unresolved. Fix the cause or state clearly that the intervention cannot solve it.
- Honor consent, suppression, communication preferences, and cancellation rights. A retention goal never overrides them.
- Do not infer causality from retained-versus-churned customer differences without a valid design; better-fit customers may both engage more and retain longer.
- If the business has no meaningful repeat/renewal behavior, state that a dedicated retention intervention layer is not decision-relevant rather than inventing one.

### Output

Retention decision: continuation behavior; segment/cohort/window; observed retention state; evidence by source; diagnosed reason and confidence; voluntary/involuntary/lapse classification; intervention hypothesis; required owner handoffs; primary outcome; guardrails; experiment/validation plan; economics dependency; implementation dependencies; approval needs; exact status.

### Library references

Owned root artifacts, read when their scope applies:

- retention-strategy-plan.md — canonical diagnosis, intervention, save/recovery, win-back, measurement, and learning record.

### Related owners

- `$marketing-intake`: lifecycle definitions, evidence state, authorization, shared context
- `$customer-research`: customer-stated reasons, qualitative patterns, VOC
- `$icp-jtbd`: poor-fit segments, changed needs, alternatives
- `$activation`: first-value failures that later appear as retention problems
- `$offer-strategy`: promise/expectation mismatch and commercial proposition
- `$pricing-monetization`: price/payment-model changes and discount architecture
- `$lifecycle-marketing`: retention, recovery, lapse, and win-back communication triggers/cadence/suppression
- `$copywriting`: retention and recovery message wording
- `$tracking-measurement`: causal validity and experiment learning
- `$retention-economics`: realized retention, churn, repeat, LTV, payback, and cohort maturity
- `$marketing-operations`: recurring at-risk/recovery decision loops

### QA

Confirm retention is defined for this business, state is separated from reason, voluntary and involuntary loss are not blended, intervention matches diagnosed cause, cancellation rights and consent are protected, discounts are economically checked, downstream guardrails are included, product/service defects are routed to their owner, and no delayed cancellation or short-term save is described as durable retention before the observation window matures.

### Reference: intervention selection and save recovery ($retention-strategy)

### Intervention Selection and Save / Recovery

Use after the retention state and leading cause are defined.

#### Core rule

Match the intervention to the diagnosed cause. A retention tactic that does not address the cause is noise, margin leakage, or coercion.

#### Intervention map

##### Involuntary payment failure

Possible responses: payment retry logic, card/account update path, billing-error correction, payment-method fallback, customer notification, service grace where commercially appropriate.

Owner boundaries: lifecycle marketing owns communications; pricing/monetization owns payment-model changes; billing/product implementation remains with the relevant system owner.

Do not use a discount as the default solution to a technical payment failure.

##### Product/service/fulfillment defect

Possible responses: repair the defect, complete missing delivery/service, proactive support, replacement/remediation under actual policy, expectation reset where truthful.

Do not persuade a customer to remain while leaving the verified defect unresolved.

##### Activation/value-realization failure

Route the value barrier to `$activation`. Retention may define the business risk, but Activation owns the first-value journey intervention.

##### Poor fit / wrong acquisition

Route qualification/segment implications to `$icp-jtbd` and relevant acquisition owners. Do not improve apparent retention by trapping poor-fit customers after acquisition.

##### Price / affordability / value tradeoff

Possible responses may include plan/package fit, pause/downgrade where truly available, payment timing, or a tested commercial offer. Pricing changes and discount architecture belong to `$pricing-monetization`.

A discount is a commercial intervention with margin and future-behavior effects, not a universal save tactic.

##### Temporary no-need / seasonality

Possible responses: pause, reminder at evidence-backed timing, reorder/renewal timing support, lower-frequency communication. Do not treat a customer whose need has ended as a persuasion failure.

##### Habit / attention / usage lapse

Possible responses: relevant reminder, progress cue, education, assistance, or workflow integration, only if the customer still has the underlying job and contact is permitted.

##### Expectation mismatch

Fix the source of the expectation: offer, acquisition message, onboarding, product/service scope, or sales process. A retention message cannot repair a promise that remains false.

##### Competitive switch

Understand the decision criteria and alternative. Do not automatically copy the competitor or undercut its price. Route positioning implications to `$icp-jtbd`, offer changes to `$offer-strategy`, and pricing decisions to `$pricing-monetization`.

#### Save design

A cancellation-save intervention should define:

- eligible state and reason
- intervention and mechanism hypothesis
- who should not receive it
- customer choice and easy cancellation path
- commercial cost
- observation window
- primary retained-value outcome
- guardrails
- follow-up behavior required to call the save durable

##### What is not a valid save

- customer gives up because cancellation is hard
- cancellation is delayed for a few days with no subsequent value/paid behavior
- a large discount retains revenue but destroys contribution
- support persuades the customer while the root defect remains
- the customer is moved to a plan they did not knowingly choose

#### Recovery design

For involuntary loss, distinguish:

- retry attempted
- payment method updated
- payment recovered
- service/account restored
- customer remained active after recovery window

Do not label a successful payment retry as durable retention until the business-relevant continuation window is observed.

#### Ethics and control

- Cancellation must remain understandable and accessible.
- Never use fake urgency, hidden downgrade consequences, misleading buttons, or repeated unwanted contact.
- Do not suppress legitimate refund/cancellation rights to protect a metric.
- Consent, unsubscribe, suppression, and contact preferences are binding.
- Any external account, billing, plan, or commercial mutation requires explicit authorization and exact-state verification.

#### Measurement

Prefer realized continuing behavior and economics over “save accepted.” Guardrails can include contribution, discount cost, refund rate, complaints, support burden, payment-failure recurrence, next renewal/reorder, and customer quality.

### Reference: repeat renewal and winback ($retention-strategy)

### Repeat, Renewal, and Win-Back

Retention is not one intervention. Active-customer retention, repeat purchase, renewal, lapse prevention, recovery, and win-back occur at different states and require different evidence.

#### State-specific objectives

##### Active retention

Goal: preserve ongoing value and paid/qualified behavior without unnecessary intervention.

Do not create messaging or discounts merely because a customer is active. No-op is a valid decision when risk is low and value is being realized.

##### Repeat purchase

Define the expected need/replenishment cycle from observed behavior or product/service logic. Distinguish customers who are not yet due from customers who have actually lapsed.

A reorder reminder sent earlier than the normal need window can inflate short-term purchase rate while causing stockpiling, discount dependence, returns, or later demand pull-forward. Measure beyond the immediate purchase.

##### Renewal

Separate renewal eligibility, renewal decision date, notice requirements, payment success, and post-renewal continuation. Auto-renewal status is not proof of customer value.

Where cancellation/renewal rules apply, preserve legal and customer-choice requirements. Never optimize renewal by hiding terms or making opt-out materially harder.

##### Lapse prevention

Define an at-risk or lapse threshold before looking at outcomes. It should be based on relevant behavior/timing, not a universal day count.

Use evidence to distinguish likely temporary delay, reduced need, value failure, price issue, operational issue, and true departure.

##### Win-back

Win-back applies after genuine lapse/cancellation, not to customers still active or merely late relative to an arbitrary cadence.

Before attempting win-back:

1. confirm the customer is eligible to contact
2. confirm the original loss reason is known or at least bounded
3. check whether the reason has changed or been resolved
4. confirm the offer/product/service remains appropriate
5. choose a timing window that fits the underlying need
6. define success beyond message engagement

A win-back message does not solve a still-broken product, service, billing, or expectation problem.

#### Win-back intervention families

Use only when cause-compatible:

- evidence-backed reminder of still-relevant value
- notice that a real defect/problem has been fixed
- changed product/service capability that directly resolves the earlier reason
- return to an appropriate plan/package where available
- timing-based reminder when the job naturally recurs
- commercial incentive only when economics and customer behavior support testing it

Do not fabricate “we miss you” personalization, fake scarcity, or exclusive status.

#### Discount discipline

A discount can create a purchase without restoring underlying retention quality. Track:

- incremental contribution, not only orders or renewals
- next full-price behavior where relevant
- repeat discount use
- refund/cancellation after the incentive
- segment/customer mix
- pull-forward or stockpiling effects
- downstream retention after the incentive expires

Do not infer that discount users are universally lower quality or higher churn without business-specific evidence.

#### Experiment design

Keep population, state, reason, treatment, timing, and eligibility fixed before reading results. Use `$tracking-measurement` for causal design and experiment-learning classification.

Potential primary outcomes:

- realized renewal
- realized repeat purchase within the appropriate window
- recovered paid status
- retained contribution
- sustained qualified usage after recovery

Supporting metrics such as open, click, coupon redemption, save-button acceptance, or return visit are not sufficient business outcomes.

#### Suppression and fatigue

Lifecycle marketing owns communication frequency, trigger, consent, suppression, and deliverability. Retention Strategy defines who should receive an intervention and why; it does not override communication rights or keep contacting customers after suppression.

#### Learning states

Record whether an intervention:

- supported the reason/mechanism hypothesis
- contradicted it
- was inconclusive
- caused guardrail harm
- was invalid/compromised

A winning win-back cell remains local learning until replicated or transferred with evidence appropriate to the new segment/state.

### Reference: retention diagnosis and reason coding ($retention-strategy)

### Retention Diagnosis and Reason Coding

Use this reference before choosing a retention, save, recovery, repeat-purchase, or win-back intervention.

#### Start with state, not story

Classify what actually happened before explaining why:

- active / continuing
- at risk
- voluntarily cancelled
- involuntarily lost
- dormant / lapsed
- recovered
- won back

Do not convert state into cause. “Cancelled” does not mean “too expensive.” “Did not repurchase” does not mean “forgot.”

#### Evidence layers

Keep these separate:

1. **Customer-stated reason** — survey, interview, support message, cancellation selection.
2. **Observed behavior** — usage, repeat timing, support events, payment attempts, delivery history, product returns.
3. **Operational fact** — outage, failed fulfillment, stock issue, billing error, service delay, unresolved ticket.
4. **Commercial fact** — price, plan, contract, discount, payment term, package change.
5. **Inference** — plausible explanation synthesized from the above.

A stated reason is valuable evidence but may be incomplete, simplified, socially convenient, or selected from constrained options. Do not relabel it as verified causality.

#### Reason families

Use only families that fit the business. Keep an `unknown / mixed` category rather than forcing every customer into a neat reason.

- **No longer needs the outcome** — job completed, season ended, temporary need resolved.
- **Poor fit / wrong customer** — acquisition or qualification mismatch.
- **Value not realized** — first value never reached or benefit too weak/slow.
- **Product/service quality** — defects, reliability, usability, support, fulfillment, experience failure.
- **Expectation mismatch** — promise, scope, capability, timeline, or service level differed from expectation.
- **Price / affordability / value tradeoff** — commercial objection, not automatically solved by discounting.
- **Competitive / alternative switch** — another solution or status quo became preferable.
- **Usage / habit / attention** — value exists but use/reorder behavior did not become sustained.
- **Lifecycle timing** — reorder/renewal need has not arrived yet; customer may be dormant rather than lost.
- **Involuntary payment loss** — card failure, billing error, expiry, insufficient funds, technical payment issue.
- **Policy / compliance / eligibility** — account or customer cannot continue under legitimate constraints.
- **Unknown / mixed** — evidence insufficient or several reasons materially interact.

#### Coding rules

- Record primary reason only when evidence supports prioritization; otherwise preserve multiple contributors.
- Keep reason taxonomy stable across a reporting series unless a change is documented.
- Do not merge voluntary and involuntary churn into one actionable reason bucket.
- Preserve segment, product/plan, acquisition source, pricing state, activation state, and cohort when they change interpretation.
- Do not infer prevalence from a few vivid support tickets or public reviews.
- Do not fabricate a percentage when reason coverage is incomplete.
- Cancellation surveys with optional response create missingness; report response coverage before using the distribution.
- If options changed over time, do not compare reason percentages as if definitions were constant.

#### Diagnosis sequence

1. Verify the retention/churn/repeat metric definition and cohort window.
2. Check for measurement or lifecycle-definition changes.
3. Separate voluntary, involuntary, and dormant/lapsed states.
4. Check product/service/fulfillment/billing defects.
5. Check acquisition-fit and activation evidence.
6. Check commercial-term changes.
7. Review customer-stated reasons and qualitative evidence.
8. Compare segments/cohorts without pretending correlation is cause.
9. Record the leading reason hypothesis, alternatives, confidence, and evidence needed to discriminate.

#### Minimum output

State; cohort/window; evidence coverage; reason family; observed evidence; customer-stated evidence; operational/commercial facts; competing explanation; confidence; decision implication; owner of the suspected root cause.

## Skill: $retention-economics

**Use when:** Model customer lifetime value, payback period, cohort retention, and repeat-purchase or renewal economics using realized revenue and margin; not for single-period efficiency metrics, platform ROAS, defining activation, choosing retention interventions, or setting pricing architecture.

Classify each model, curve, or projection with `KNOWLEDGE-TAXONOMY.md`. A cohort curve is a pattern from observed customers, not a guarantee for future ones. A projected lifetime value is a model output, not a business outcome, until realized revenue confirms it.

This skill measures retention economics. `$retention-strategy` owns why customers are at risk/lost and what retention, save, recovery, repeat, renewal, or win-back intervention should be tested.

### Context

Business model (ecommerce, subscription, lead generation, marketplace) and its typical repeat or renewal cycle; source-of-truth system for customer-level revenue; cohort definition (acquisition period, channel, first-purchase or first-conversion date); activation definition/state when first meaningful value is decision-relevant; retention-strategy intervention/state when a save/recovery/win-back program may change cohort behavior; current pricing/package state where it changes the commercial terms; revenue basis and profit level per `$marketing-intake`; refund and cancellation treatment; observation window relative to the business's typical payback and lifetime; and whether the request needs a historical (realized) or predictive (modeled) figure.

Do not model lifetime value or payback without the cost and profit definitions `$marketing-intake` requires. A model built on an undefined profit level is unusable the moment it is compared against anything.

### Method

1. Fix the cohort definition and observation window before computing anything. State whether the window covers full maturity or is truncated.
2. Choose historical (realized, from actual cohort revenue to date) or predictive (modeled, extrapolating from partial data) and never blend them silently.
3. Compute at the correct profit level — gross, contribution after media, or contribution after variable costs — and name it in every output.
4. Build the retention or renewal curve from the cohort, not from an average across cohorts of different age.
5. Treat material pricing, package, payment-model, acquisition-offer, activation-definition/journey, or retention-intervention changes as possible cohort boundaries. Compare pre-change and post-change cohorts separately before pooling them.
6. When comparing activated versus non-activated customers, use `$activation`'s defined value event/window and state the selection/confounding problem explicitly. A retention difference does not prove activation caused retention.
7. When comparing exposed versus unexposed retention-intervention cohorts, preserve `$retention-strategy`'s eligibility/state/reason definitions and route causal interpretation to `$tracking-measurement`. A retained cohort difference does not prove the intervention caused it.
8. Compute payback period against the same profit level used for cost of acquisition; state whether payback is measured in revenue or contribution.
9. Separate new-customer economics from returning-customer economics; do not blend acquisition cost into a blended lifetime figure that then hides unprofitable acquisition.
10. State the confidence interval or the immaturity discount on any predictive figure, and what evidence would tighten it.

Read Customer lifetime value for LTV method and pitfalls. Read Payback period for acquisition payback. Read Cohort and retention analysis for curve construction and retention/churn. Read Lead-to-revenue cohorts for lead-generation and long sales-cycle businesses.

### Rules

- Never present a predictive lifetime value as realized revenue, and never compare a predictive figure from one model against a realized figure from another cohort.
- Never compute lifetime value or payback without a named profit level and its included costs.
- Do not extrapolate a cohort curve past its observed maturity without stating the extrapolation and its assumption.
- Do not average retention or lifetime value across cohorts of materially different age, channel, acquisition offer, activation journey/definition, retention intervention, price, package, or payment model without stating that the blend can mask a declining or improving trend.
- Do not infer that activation caused higher retention merely because activated customers retain better. Better-fit or more motivated customers may both activate and retain.
- Do not infer that a save, recovery, discount, or win-back intervention caused retention merely because exposed customers retained better. `$tracking-measurement` owns causal validity.
- A single strong cohort does not establish a durable pattern; require replication across at least two comparable cohorts before treating a curve as decision-grade for scaling.
- Do not use predictive lifetime value alone to authorize an activation, retention-intervention, pricing, or scaling decision. `$activation` owns first-value journey decisions; `$retention-strategy` owns retention interventions; `$pricing-monetization` owns pricing structure; `$optimization-scaling` owns scaling and applies its own proof standard and marginal-economics gates.
- Refunds, cancellations, chargebacks, and returns reduce realized revenue in the period they occur; do not net them out of an earlier period to smooth a curve.
- Do not treat platform-attributed acquisition cost as the true acquisition cost; use the business source of truth.

### Output

Cohort economics: cohort definition and window; activation definition/state where relevant; retention-strategy intervention/state where relevant; pricing/package state where relevant; historical or predictive label; profit level; retention or renewal curve with maturity state; lifetime value at stated horizons; payback period; new versus returning economics; confidence or immaturity discount; comparison to acquisition cost; exact status.

### QA

Confirm the cohort definition and window are stated, material activation/retention-intervention/pricing/package changes are not silently pooled, activated-versus-nonactivated and intervention-exposed comparisons are not treated as causal by default, historical and predictive figures are never blended, the profit level is named and consistent with acquisition cost, curves are not averaged across incompatible cohorts, extrapolation past observed maturity is disclosed, and no figure here alone authorizes an activation, retention, pricing, or scaling change.

### Reference: cohort and retention analysis ($retention-economics)

### Cohort and Retention Analysis

Groups customers by a shared starting point and tracks their behavior over time. The unit of analysis that makes lifetime value, payback, and churn meaningful — comparing point-in-time snapshots across cohorts of different age produces false trends.

#### Cohort definition

Define by acquisition period (week, month, or quarter) and, when segmenting, by acquisition channel, campaign, offer, or first-purchase category. State the definition before building any curve; changing it mid-analysis invalidates the comparison.

#### Curve construction

1. Index each cohort's behavior by periods-since-acquisition (period 0, 1, 2, ...), not by calendar date, so cohorts of different starting dates align on the same axis.
2. Compute the metric of interest per period: active customers, repeat-purchase rate, cumulative revenue, retained subscribers.
3. Mark each cohort's maturity — how many periods of data actually exist for it. A cohort acquired last month has no period-11 data; do not plot a projected value as if observed.
4. Distinguish retention (customers still active or transacting) from repeat-purchase rate (customers who transacted again, which can exceed one per customer) — do not use them interchangeably.

#### Churn and retention

For subscription and recurring-revenue models, define churn precisely: logo churn (accounts lost) versus revenue churn (revenue lost, which can be negative when expansion exceeds loss). Report both; a business can retain most logos while losing revenue, or the reverse.

For ecommerce and lead generation without a subscription mechanism, use repeat-purchase rate or reactivation rate rather than churn, and state the inactivity window used to declare a customer lapsed.

#### Rules

- Never plot or report a period beyond a cohort's observed maturity without explicitly marking it as projected.
- Do not average retention across cohorts of different age; a blend of mature and immature cohorts understates or overstates the current trend depending on which dominates.
- A retention improvement observed in one cohort is a hypothesis until it replicates in the next; do not report it as an established trend from a single cohort.
- State the inactivity or lapse window used for any repeat-purchase or reactivation definition — a 30-day window and a 180-day window on the same data produce different conclusions.
- Revenue churn and logo churn answer different questions; report the one relevant to the decision and do not substitute one for the other.
- Cohort curves inform strategy; they do not authorize a scaling change on their own. Route through `optimization-scaling` for that decision.

### Reference: customer lifetime value ($retention-economics)

### Customer Lifetime Value

The projected or realized profit a customer generates over the relationship, at a stated profit level. Not a single number — always paired with a horizon, a profit level, and a historical-versus-predictive label.

#### Variants, and when each applies

| Variant | Definition | Use for |
|---|---|---|
| Historical (realized) lifetime value | Actual cumulative profit from a cohort to date | Reporting what happened; the only variant that can stand alone as a business outcome |
| Predictive lifetime value | Modeled projection from partial cohort data or a fitted curve | Forward planning, with its confidence interval stated |
| Gross lifetime value | Revenue-based, no costs deducted | Top-line scale only; never for acquisition-spend decisions |
| Contribution lifetime value | Revenue minus cost of goods sold and variable costs, before media | Acquisition and payback decisions |
| Contribution-after-media lifetime value | Contribution lifetime value minus acquisition cost | Net customer profitability |

Reserve "lifetime value" alone for ambiguity the reader must resolve; always qualify which variant is being reported.

#### Method

1. Define the cohort: acquisition period, channel or campaign if segmenting, and first-transaction or first-conversion date.
2. Choose the horizon — 30/60/90-day, 12-month, or full projected lifetime — matched to the business's typical repeat cycle. A 30-day horizon on a business with an 18-month repeat cycle understates lifetime value by construction.
3. Sum realized profit per customer at the stated profit level, to the horizon, from the business source of truth.
4. For a predictive figure, fit a retention or spend-decay curve to the observed portion of the cohort and project forward; state the model and its fit quality.
5. Report per-customer lifetime value, not only cohort totals, so it can be compared to per-customer acquisition cost.

#### Common errors

- Comparing a 90-day lifetime value against a payback period measured over 12 months — mismatched horizons produce a false payback conclusion.
- Reporting gross lifetime value against contribution-based acquisition cost, inflating apparent profitability.
- Using a young cohort's early-period lifetime value as if it were mature, before repeat behavior has had time to occur.
- Blending predictive and historical figures into one number without disclosure.
- Computing an average lifetime value across channels with different retention shapes and using it to justify budget for the worst-retaining channel.

#### Rules

- State horizon, profit level, and historical/predictive status every time the figure is reported.
- A predictive lifetime value used to justify scaling must meet the `optimization-scaling` proof standard; a single cohort's projection is not sufficient on its own.
- Do not update a historical lifetime value retroactively without recording the revision and its cause.

### Reference: lead to revenue cohorts ($retention-economics)

### Lead-to-Revenue Cohorts

Extends cohort economics to lead generation and long sales-cycle businesses, where the gap between marketing conversion and realized revenue can be weeks or quarters. Read alongside Cohort and retention analysis.

#### Why lead generation needs a separate method

Ecommerce cohorts mature in days; lead-generation cohorts mature on the sales cycle, which can exceed a typical reporting period. A lead cohort's revenue is systematically incomplete until the cycle closes — treating incomplete cohorts as final understates value and can trigger a premature scale-down of a channel that is actually performing, just not yet realized.

#### Method

1. Cohort by lead-creation date, not by opportunity-creation or close date; cohorting on a later stage survivorship-biases the analysis toward leads that already progressed.
2. Track each cohort through its stages — lead, marketing qualified, sales qualified, opportunity, customer — using the stage definitions `$marketing-intake` recorded, joined from the Customer Relationship Management system.
3. Report cohort revenue only after stating what share of the cohort has reached each stage and what share remains open. An "open" lead is neither won nor lost; do not treat it as either.
4. Compute conversion rate and revenue per lead-cohort period as cycle length increases, and mark the point at which a cohort is judged mature enough for a stable read — typically when the open share has fallen below a stated threshold.
5. Separate pipeline velocity (how fast leads move through stages) from revenue lag (how long until cash or booked revenue appears); a channel can accelerate the first without changing the second, or the reverse.

#### Rules

- Never report a lead cohort's conversion rate or revenue as final while a material share remains open; state the open share alongside any interim figure.
- Do not compare a mature channel's cohort conversion rate against an immature cohort from a newer channel; normalize for cycle stage first.
- A sudden apparent drop in lead quality in the most recent cohorts is often incomplete maturation, not a real decline; check open share before concluding quality fell.
- Join marketing source to Customer Relationship Management outcome at the lead level, not at an aggregate channel level, so misattributed or unsourced leads do not silently inflate or deflate a channel's realized cohort revenue.
- A lead-to-revenue conclusion used for a scaling decision must satisfy the `optimization-scaling` conversion-lag and marginal-evidence gates in addition to this cohort's own maturity threshold.

### Reference: payback period ($retention-economics)

### Payback Period

The time for cumulative customer profit to recover acquisition cost, at a stated profit level. Governs how long capital is at risk per customer and how fast a scaling program can be reinvested.

#### Method

1. Fix the profit level — contribution before or after variable costs — and use the identical level on both sides: acquisition cost and cumulative customer profit.
2. Use the business source of truth for acquisition cost, not platform-attributed cost per acquisition; if only platform cost is available, label the payback figure as platform-attributed and provisional.
3. Track cumulative contribution per customer (or per cohort, divided by cohort size) period by period from acquisition date.
4. Payback period is the period in which cumulative contribution first exceeds acquisition cost. Report it in the same time unit the business plans around — days, weeks, or months.
5. Where payback varies materially by channel, offer, or segment, report it segmented; a blended payback period can mask a channel that never pays back within an acceptable window.

#### Revenue payback versus contribution payback

Revenue payback (cumulative revenue exceeds acquisition cost) is faster and less meaningful; it ignores cost of goods sold and fulfillment. Contribution payback is the decision-relevant figure for scaling and cash planning. Always label which is reported, and prefer contribution payback when a scaling decision depends on it.

#### Rules

- Do not report payback period without stating the profit level used.
- Do not use platform-attributed acquisition cost as the numerator for a scaling decision without labeling it provisional per the causal evidence ladder — platform-attributed cost is not a verified acquisition cost.
- A payback period shorter than the observation window is more reliable than one that requires extrapolation past the data available; state which applies.
- Do not compare payback periods across channels with different cohort ages without normalizing for maturity.
- Cash payback and accounting payback can differ when revenue is recognized on delivery, subscription billing, or installment terms; state which convention is used.
