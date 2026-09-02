<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Conversion, Offer, and Pricing

## Skill: $cro

**Use when:** Audit and improve landing pages, product pages, forms, and checkout journeys leading to qualified conversion using evidence and testable hypotheses; not for post-conversion activation ownership or claiming causality from heuristics alone.

Classify each deliverable with `KNOWLEDGE-TAXONOMY.md`. Heuristic observations are hypothesis inputs, not causal findings or universal best practices.

### Required inputs

Use the strongest available evidence for the scoped pre-conversion journey:

- exact page, form, checkout, or funnel state being evaluated, including device/viewport when material
- primary business outcome, conversion boundary, and any qualified/supporting conversion definitions
- upstream traffic source, audience/intent, promise, ad/query/message, and destination where message scent matters
- funnel and page metrics with date range, denominator, source, and useful segments such as device, source, new/returning, geography, product, or landing page
- product, offer, price, shipping/fees, eligibility, claims, proof, and policy truth that materially affect the page decision
- available recordings, surveys, usability evidence, support/sales objections, experiment results, technical errors, accessibility issues, and page-speed evidence
- commercial/downstream guardrails such as contribution, AOV, refund/return rate, lead quality, support burden, accessibility, or compliance
- implementation and test authority if the request includes a live change rather than analysis or a draft

Mark missing inputs explicitly. Do not invent user behavior, customer objections, page defects, or causal explanations to complete an audit.

### Method

1. Define the primary business outcome and any qualified or supporting conversion. Reserve “Primary conversion action” for the Google Ads setting.
2. Map message scent from ad or query through page and conversion boundary.
3. Inspect motivation, relevance, clarity, trust, and friction/anxiety before conversion.
4. Segment by source, device, intent, landing page, and new/returning user when data permits.
5. Identify the first meaningful pre-conversion leak and distinguish technical failure from persuasion weakness.
6. Rank hypotheses by evidence strength, expected impact, effort, risk, and learning value.
7. When the problem begins after signup, purchase, lead acceptance, or another defined conversion and concerns reaching first meaningful customer value, route the journey decision to `$activation`. CRO may support a bounded page/form/surface intervention without owning the activation definition.

### Rules

- Fix verified defects before testing persuasion variants.
- Do not remove necessary qualification, legal, accessibility, pricing, or expectation-setting information to inflate raw conversion rate.
- Optimize for purchases, qualified leads, or contribution—not button clicks alone.
- Protect refund rate, lead quality, AOV, accessibility, and support burden.
- Do not default to redesign when a focused change can test the mechanism.
- Message scent means continuity between the upstream promise and the destination's immediate message. Keep funnel/journey stage, awareness level, audience temperature, activation state, and lifecycle stage distinct.
- Do not relabel post-conversion onboarding or first-value work as CRO merely because the intervention appears on a web/app surface. `$activation` owns the first-value decision.

### Output

Audit finding: location; observation; evidence; affected segment; hypothesized mechanism; business impact; confidence; recommendation; validation method.

Experiment: problem; hypothesis; control; variant; primary metric; guardrails; audience; duration/sample approach; stop conditions; instrumentation; decision rule.

### Library references

Owned root artifacts, read when their scope applies:

- shopify-cro.md — Shopify-specific conversion framework.
- ecommerce.md — ecommerce conversion playbook.
- ecommerce-growth.md — ecommerce growth playbook.
- landing-page-review.md — landing page review format.
- cro-improvement.md — improvement workflow sequence.

### QA

Verify the actual page/state and device, keep the conversion boundary explicit, route post-conversion first-value decisions to `$activation`, avoid causal language without a test, include downstream guardrails, flag accessibility/compliance risks, and distinguish recommendations from implementation.

## Skill: $offer-strategy

**Use when:** Diagnose and design the commercial offer itself — promised outcome, core deliverable, value architecture, bundle, risk reversal, urgency/scarcity, and offer-level friction — using verified product, customer, proof, and economics evidence; not for writing the page, setting pricing architecture, or claiming conversion lift from heuristics.

An offer is the commercial proposition the buyer is being asked to accept. It is not the landing page, ad, headline, pricing model, or creative execution that presents it.

Classify each offer artifact with `KNOWLEDGE-TAXONOMY.md`. Offer patterns and direct-response frameworks are hypothesis inputs, not proof that a specific audience will buy.

### Context

When `.agents/marketing-context.md` exists in the active project, read the relevant sections before a decision-grade recommendation. Before deciding, confirm:

- product truth and claim boundaries
- priority segment, buying situation, JTBD, and desired outcome
- customer objections, anxieties, alternatives, and selection criteria
- current offer and current price/payment terms
- available proof and its allowed use
- margin, refund, fulfillment, inventory, service, or delivery constraints
- legal, compliance, brand, and authorization boundaries

If these are materially unclear, route the missing evidence to `$marketing-intake`, `$customer-research`, or `$icp-jtbd` rather than inventing it. A Marketing Context summary never upgrades the underlying evidence state.

### Method

1. **State the current offer plainly.** What must the buyer give, what do they receive, what outcome is promised, what conditions apply, and what happens if they do nothing?
2. **Identify the offer job.** Tie the proposition to the customer's desired progress and buying situation rather than to product features alone.
3. **Audit value architecture.** Use Offer architecture to inspect outcome relevance, confidence/proof, time-to-value, buyer effort, friction, completeness, and economic feasibility.
4. **Diagnose the binding offer constraint.** Identify the weakest decision-relevant component instead of rebuilding everything by default. See Offer diagnosis.
5. **Design the smallest meaningful change.** Improve the core deliverable, bundle, service layer, risk reversal, eligibility, timing, convenience, or other offer component while preserving product truth and margin constraints.
6. **Audit risk reversal and urgency.** Use Risk reversal and urgency. A guarantee must transfer a real risk the business can bear. Urgency or scarcity must be true, specific, and operationally enforceable.
7. **Specify proof requirements.** Match each promise to evidence strong enough to support it. Customer-reported experience is not automatically causal business proof.
8. **Route pricing when material.** If the binding constraint may be base price, value metric, package/tier architecture, payment model, or discount architecture, route that decision to `$pricing-monetization`; Offer Strategy may supply the offer context but does not set the exchange structure.
9. **Define the test.** State the offer hypothesis, controlled change, primary business outcome, guardrails, decision window, and what a win, loss, or inconclusive result would teach. Route causal experiment design to `$tracking-measurement` when needed.

### Rules

- Do not confuse a weak offer with weak copy. `$copywriting` expresses an approved offer; `$cro` diagnoses conversion friction in the page or journey.
- Do not manufacture value by inflating fictitious bonus values, unverifiable comparisons, or arbitrary “worth” numbers.
- Do not invent scarcity, countdowns, deadlines, capacity limits, waitlists, stock pressure, or expiring bonuses.
- Do not invent guarantees, refund terms, service commitments, or make-good remedies the business has not approved and cannot operationally honor.
- Do not use a discount as the default response to weak conversion. Diagnose whether the problem is relevance, confidence, effort, risk, timing, product-market fit, price, or page execution first.
- Do not promise a conversion lift, revenue lift, or expected percentage improvement from an offer heuristic.
- Do not turn a customer aspiration into a product claim unless product truth and proof support the bridge.
- Do not treat a bundle as stronger merely because it contains more items. Every component needs a job in the buying decision or delivery outcome.
- Do not hide meaningful conditions in fine print to make the headline offer look stronger.
- Do not set base price, value metric, pricing tier/package architecture, willingness-to-pay estimates, discount architecture, or monetization model. Route those decisions to `$pricing-monetization` and consume its approved/current terms as pricing inputs.
- A proposed offer is not approved, live, or proven. Preserve draft, approved, published/live, and verified states.

### Output

Offer decision: business objective; audience and buying situation; current offer; diagnosed constraint; evidence; proposed offer architecture; promise and proof boundary; core deliverable; bundle/service components; risk reversal; real urgency/scarcity; current or approved price/payment terms from `$pricing-monetization`; economics/capacity check; objections addressed; hypothesis; measurement and guardrails; approval needs; exact status.

### Related owners

- `$marketing-intake`: shared context, evidence state, economics definitions, authorization
- `$customer-research`: objections, VOC, reported outcomes, review evidence
- `$icp-jtbd`: segment, buying situation, JTBD, switching forces
- `$pricing-monetization`: base price, value metric, packages/tiers, payment model, discount architecture, price-change testing
- `$copywriting`: wording that presents the offer
- `$cro`: landing/product-page and funnel friction
- `$creative-strategy`: paid creative angle, concept, proof treatment, and CTA
- `$tracking-measurement`: experiment validity and causal evidence
- `$retention-economics`: cohort value, payback, retention economics
- `$optimization-scaling`: whether an offer-supported acquisition system is ready to scale

### QA

Confirm the offer is distinct from its copy, page, and pricing architecture; the desired outcome is evidence-grounded; every promise fits product truth; proof strength matches claim strength; urgency/scarcity is real; risk reversal is operationally supportable; margin/capacity consequences are visible; pricing decisions route to `$pricing-monetization`; the proposed change is testable; and no draft is described as approved or proven.

### Reference: offer architecture ($offer-strategy)

### Offer Architecture

Use this methodology to reason about what the buyer is being asked to accept without confusing the offer with the copy, page, or ad that presents it.

#### Offer structure

A decision-grade offer can be described through seven questions:

1. **Outcome:** What meaningful progress is the buyer trying to make?
2. **Deliverable:** What exactly will the business provide?
3. **Confidence:** Why should the buyer believe the deliverable can help produce the promised progress?
4. **Time-to-value:** When can the buyer reasonably expect the first meaningful value, and what determines that timing?
5. **Buyer effort:** What work, complexity, switching cost, or behavior is required from the buyer?
6. **Risk allocation:** What financial, time, implementation, quality, or uncertainty risk remains with the buyer versus the business?
7. **Commercial fit:** Can the business deliver the offer within its margin, capacity, legal, fulfillment, and service constraints?

The goal is not to maximize every dimension. It is to make the tradeoff credible and attractive for the priority buying situation.

#### Core deliverable versus support components

Separate:

- **Core deliverable:** the thing the buyer primarily pays to receive.
- **Enabling component:** makes the core easier, faster, safer, or more complete to use.
- **Proof component:** reduces uncertainty but is not itself the product.
- **Risk-reversal component:** changes who bears a defined failure risk.
- **Convenience component:** reduces buyer effort or coordination cost.
- **Optional bonus:** additive value with a real job; not filler added to inflate perceived value.

A component belongs only if it improves the customer outcome, confidence, effort, risk, or decision clarity. More components do not automatically create a stronger offer.

#### Outcome ladder

Keep these distinct:

```text
Product capability
→ immediate functional benefit
→ customer progress / use-case outcome
→ broader desired result
```

An offer may communicate higher on the ladder only when the business has a supportable bridge from capability to result. Do not jump from a product feature to a guaranteed life or business outcome.

#### Confidence architecture

Confidence can be supported by:

- clear product mechanism or service process
- demonstration
- traceable customer experience
- case-study evidence
- independent validation
- credentials or authority relevant to the claim
- transparent conditions and limitations
- risk reversal the business can honor

The proof form must match the promise. A testimonial can support that someone reported an experience; it does not by itself prove the same causal outcome for future buyers.

#### Time-to-value

Separate:

- time to start
- time to first value
- time to full delivery
- time to the broader desired result

Do not collapse them into one aggressive promise. If timing varies materially by customer effort, eligibility, external dependency, or implementation complexity, state the dependency.

#### Buyer effort

Map required effort honestly:

- setup
- learning
- data/content/input required
- approvals
- implementation
- behavioral change
- ongoing maintenance
- coordination with other people or systems

Reducing unnecessary effort can strengthen an offer. Hiding necessary effort creates expectation failure, refunds, churn, or support burden.

#### Commercial feasibility gate

Before recommending an offer change, check:

- gross or contribution margin impact at the named profit level
- inventory / fulfillment capacity
- service or support capacity
- refund / cancellation exposure
- fraud / abuse exposure
- delivery dependencies
- legal or compliance constraints
- effect on existing customers or channel conflict

An attractive offer that the business cannot deliver profitably or reliably is not decision-ready.

#### Offer hypothesis format

Use:

`Because [evidence-backed buying constraint], we believe changing [one offer component] will improve [primary business outcome] for [priority buying situation] because [expected mechanism], while protecting [guardrails].`

Do not insert a numeric expected lift unless evidence supports that forecast.

### Reference: offer diagnosis ($offer-strategy)

### Offer Diagnosis

Use this method when an offer is underperforming or feels weak. Diagnose before adding more copy, bonuses, discounts, or urgency.

#### Diagnostic order

##### 1. Relevance

Does the offer solve a valuable problem or desired progress for the priority buying situation?

Signals to inspect:
- customer research and repeated objections
- segment economics and retention
- buying trigger and urgency of the underlying problem
- current alternatives and switching forces

If relevance is weak, adding persuasion usually amplifies the wrong proposition.

##### 2. Clarity

Can the buyer explain:
- what they get
- who it is for
- what result or progress it supports
- what they must do
- what it costs or commits them to
- what happens next

Clarity problems may belong to `$copywriting` or `$cro` if the underlying offer is sound.

##### 3. Confidence

What uncertainty blocks acceptance?

Separate:
- product skepticism
- business/provider trust
- outcome uncertainty
- implementation uncertainty
- fit uncertainty
- switching anxiety

Match the response to the uncertainty. Do not use generic social proof when the buyer needs product demonstration, eligibility clarity, process transparency, or evidence relevant to their exact risk.

##### 4. Time and effort

Is the buyer rejecting the offer because:
- value arrives too late
- setup is too heavy
- switching cost is too high
- too many decisions are required
- delivery is inconvenient
- ongoing effort is unclear

Reduce unnecessary effort where feasible. Do not hide necessary effort.

##### 5. Risk

Map what the buyer could lose:
- money
- time
- status/reputation
- opportunity
- data
- operational continuity
- switching flexibility

Then ask whether the business can credibly absorb or reduce that risk without creating unsustainable exposure.

##### 6. Completeness

Does the core deliverable leave a predictable gap that prevents the promised progress?

A supporting component is useful when it closes a real delivery or adoption gap. It is filler when it only makes the stack look larger.

##### 7. Economics and capacity

An offer can increase raw conversion while worsening the business outcome through:
- lower margin
- refunds
- poor-fit customers
- support burden
- fulfillment failures
- fraud/abuse
- cannibalization
- channel conflict

Protect the primary business outcome and downstream guardrails.

##### 8. Price sensitivity versus value problem

If the buyer says “too expensive,” do not automatically conclude the base price is wrong. The statement can reflect:
- insufficient perceived relevance
- weak proof
- poor timing
- cash-flow constraint
- comparison against another alternative
- genuine willingness-to-pay mismatch

`$offer-strategy` may change non-price value/risk components or test a supplied commercial term, but base pricing strategy remains a separate capability until governed.

#### Constraint statement

End diagnosis with one sentence:

`The strongest current evidence suggests the binding offer constraint is [constraint] for [segment/situation], because [evidence]. Confidence: [level]. It would be reversed by [missing evidence or result].`

If the evidence does not support one primary constraint, keep multiple hypotheses and design a test that distinguishes them.

### Reference: risk reversal and urgency ($offer-strategy)

### Risk Reversal and Urgency

Use this reference when an offer needs to reduce buyer risk or create a legitimate reason to act now.

#### Risk reversal

Risk reversal changes who bears a defined downside. It is not a promise that every customer will get the desired outcome.

Common forms include:

- refund or return policy
- trial or evaluation period
- cancellation flexibility
- service-level commitment
- implementation support
- milestone-based payment
- replacement / repair commitment
- eligibility or fit assessment before purchase

##### Design questions

For any proposed risk reversal, state:

1. What exact buyer risk is being reduced?
2. What event triggers the remedy?
3. What conditions or exclusions are necessary?
4. Can the business operationally honor it?
5. What fraud or abuse risk does it create?
6. What margin, support, cash-flow, or fulfillment exposure does it create?
7. How will the buyer understand the terms before accepting?

Do not propose a guarantee that depends on an outcome outside the business's control unless the remedy and conditions are both truthful and approved.

#### Proof versus guarantee

Keep these separate:

- **Proof** supports why a claim may be credible.
- **Risk reversal** limits a defined downside if the purchase does not meet stated conditions.
- **Guarantee language** is a contractual/commercial promise and requires operational and, where relevant, legal review.

A guarantee cannot substitute for missing product evidence.

#### Urgency

Urgency is legitimate when delay changes the buyer's opportunity or the business's ability to provide the offer.

Examples of potentially real urgency:

- actual enrollment or event date
- genuine inventory or production limit
- real fulfillment or service-capacity limit
- documented price or offer change effective on a specific date
- seasonal or regulatory timing
- expiring eligibility or externally imposed deadline

Urgency is not legitimate merely because a marketer wants faster conversion.

#### Scarcity

Scarcity must describe a real constrained resource such as:

- units
- seats
- appointment capacity
- geographic/service coverage
- production slots
- limited access created by a real operational constraint

Do not invent quantities, “spots,” stock pressure, waitlists, or scarcity tiers.

#### Deadline integrity

For a deadline, record:

- exact date/time or event
- what changes after the deadline
- why it changes
- who is affected
- source/approval
- whether extensions are allowed and under what rule

If the deadline repeatedly resets or is routinely extended without disclosure, it should not be presented as urgency.

#### Ethical offer pressure test

Reject or escalate a tactic when it relies on:

- a false deadline
- fake inventory pressure
- hidden cancellation barriers
- a guarantee with undisclosed material conditions
- fear disproportionate to the real risk
- a fabricated “regular value” or comparison anchor
- confusing opt-in/opt-out language
- an offer that intentionally obscures total commitment

The test is not whether the tactic could increase conversion. The test is whether the commercial proposition remains true, understandable, supportable, and reversible where promised.

## Skill: $pricing-monetization

**Use when:** Diagnose and design base price, value metric, package/tier architecture, payment model, and monetization changes using customer, competitive, cost, demand, and realized-economics evidence; not for inventing willingness-to-pay, copying competitor prices, or treating conversion rate as the pricing objective.

Pricing and Monetization owns the commercial exchange structure: what is charged, for what unit of value, in which package, on what payment model, and under which economic constraints. It does not own the broader offer promise, page copy, checkout UX, or lifetime-value calculation.

Classify pricing outputs with `KNOWLEDGE-TAXONOMY.md`. A pricing framework or benchmark is a hypothesis input, not evidence that a specific price is optimal.

### Context

Before a decision-grade recommendation, confirm:

- product/service truth and delivery model
- priority segment, buying situation, JTBD, alternatives, and selection criteria
- current base price, fees, discounts, payment terms, packages/tiers, and eligibility
- current offer architecture from `$offer-strategy`
- realized unit economics, margin/cost-to-serve, refunds/cancellations, capacity, and tax/fee treatment
- retention/payback evidence where repeat behavior materially affects the decision
- customer research that actually bears on price sensitivity or value perception
- relevant competitor/alternative pricing with date and source, when available
- legal, contractual, fairness, brand, and authorization constraints

If inputs are weak, return a pricing hypothesis and evidence plan rather than a false point estimate.

### Method

1. **State the pricing decision.** Separate base price, value metric, packaging/tier, payment model, discount architecture, and price-change decision. Do not solve several at once by default.
2. **Define the economic floor and operating constraints.** Use Pricing architecture to identify variable cost, cost-to-serve, contribution target, capacity, refund/cancellation risk, and any channel or payment costs that materially change economics.
3. **Define the customer value unit.** Decide whether the business charges per product, seat, usage, outcome proxy, subscription period, project, bundle, or another unit. A value metric must align reasonably with customer value and business cost without creating perverse incentives.
4. **Assess evidence on price sensitivity.** Use Willingness-to-pay evidence. Separate observed purchases and behavioral tests from stated survey answers, sales anecdotes, competitor prices, and model inference.
5. **Design package/tier architecture only when differentiation is real.** Each tier or package needs a distinct customer/job, entitlement, usage boundary, service level, or economic reason. Do not manufacture three tiers because a framework says three is standard.
6. **Model scenarios.** Compare price/package options on realized or explicitly modeled revenue, contribution, conversion/close rate, mix shift, retention/refund risk, capacity, and customer impact. Do not optimize one metric in isolation.
7. **Choose the smallest decision-valid test.** Use Price-change testing and rollout. Specify population, eligibility, treatment, primary business outcome, guardrails, duration/lag, grandfathering or migration rules, and rollback/stop conditions.
8. **Record exact commercial state.** Proposed, approved, configured, live, observed, and verified are different states. A price change is not verified until the actual charged amount and resulting economics are observed in the source of truth.

### Rules

- Customer research may reveal price language, objections, tradeoffs, and relative value. It does not automatically produce a numeric willingness-to-pay estimate.
- Competitor price is context, not the answer. Never infer optimal price, market share, demand, margin, or willingness-to-pay from a competitor price alone.
- Do not use arbitrary psychological endings, price buckets, “industry standard” markups, or universal good-better-best rules as proof.
- Do not treat a higher conversion rate as a pricing win if contribution, refund rate, retention, lead quality, capacity, or customer mix worsens materially.
- Do not treat a higher average order value or ARPU as a win without checking volume, contribution, retention, and mix effects.
- Do not hide a price increase through mandatory fees, confusing unit changes, shrinkage, or materially harder cancellation. Make the commercial exchange legible.
- Do not fabricate scarcity, anchor prices, crossed-out prices, savings percentages, reference prices, or “most popular” labels.
- Discounts are part of pricing architecture when they change realized price. Do not evaluate list price while ignoring discount frequency and mix.
- Grandfathering, migration, renewal, and existing-customer treatment must be explicit when a price change affects current customers.
- A modeled price recommendation is not realized economics. Preserve assumption ranges and sensitivity.
- Any live price, billing, checkout, contract, or catalog change remains approval-bound.

### Output

Pricing decision: decision type; audience/segment; current commercial structure; evidence base and strength; economic floor/constraints; value metric; package/tier logic; candidate price/payment scenarios; modeled business impact with assumptions; customer and retention risks; competitor context if relevant; test/rollout plan; grandfathering/migration rules; measurement and guardrails; approval needs; exact status.

### Library references

Owned root artifacts, read when their scope applies:

- pricing-decision.md — canonical pricing decision, scenario, rollout, migration, and verification record.

### Related owners

- `$marketing-intake`: shared context, source/evidence state, cost definitions, authorization
- `$customer-research`: price objections, tradeoffs, value language, stated research evidence
- `$icp-jtbd`: segment, JTBD, alternatives, competitive context
- `$offer-strategy`: promised outcome, bundle, risk reversal, offer architecture
- `$cro`: checkout/page friction and presentation of approved pricing
- `$copywriting`: wording that communicates approved pricing
- `$tracking-measurement`: experiment validity and causal evidence
- `$retention-economics`: realized retention, lifetime value, renewal, and payback effects
- `$optimization-scaling`: downstream scaling decisions using validated economics

### QA

Confirm the pricing decision type is explicit, observed behavior is separated from stated research and inference, competitor price is not treated as optimal price, cost/profit level is named, package differences are real, scenarios include volume and contribution effects, current-customer treatment is explicit, no fake anchor/savings/urgency is introduced, the test is interpretable, and no proposed/configured price is described as live or verified prematurely.

### Reference: price change testing and rollout ($pricing-monetization)

### Price-Change Testing and Rollout

Use this reference when a proposed price, package, value metric, discount rule, or payment model needs to be tested or rolled out.

A price change affects both customer behavior and realized economics. A valid decision therefore needs more than conversion rate.

#### Pre-change specification

Record before launch:

- exact pricing decision being tested
- population and eligibility
- control/current commercial terms
- treatment/new commercial terms
- whether existing customers are excluded, grandfathered, migrated, or renewed into the change
- primary business outcome
- revenue basis and profit level
- guardrails
- conversion/renewal lag
- implementation owner and approval status
- rollback or harm stop condition
- expected learning if result is positive, negative, or inconclusive

If the test is intended to support a causal claim, use `$tracking-measurement` for design validity, power, allocation, contamination, lag, and stopping rules.

#### Metrics

Choose the primary metric according to the decision. Relevant measures can include:

- realized revenue
- contribution at the named profit level
- conversion or close rate
- average realized price
- package/tier mix
- average order value or revenue per account
- refund/return/cancellation rate
- renewal/retention when mature enough
- support/service load
- capacity utilization
- lead/customer quality

Do not create a composite score after seeing the outcome to manufacture a win.

#### Customer treatment

Price changes can create a migration decision separate from the new-customer pricing decision.

For existing customers document:

- grandfathering duration, if any
- renewal date treatment
- notice period
- contract/legal constraints
- entitlement changes
- downgrade/cancel options
- support and exception process
- cohort tracking needed to observe retention impact

A new-customer test does not prove an existing-customer migration is safe.

#### Rollout states

Keep exact states distinct:

1. **Proposed** — pricing design exists only as a recommendation.
2. **Approved** — authorized commercial terms and scope are recorded.
3. **Configured** — catalog/billing/checkout/contract system contains the intended terms but may not yet be customer-facing.
4. **Live** — eligible customers can actually receive/pay the new terms.
5. **Observed** — transactions or renewals under the new terms exist.
6. **Verified** — charged amounts, eligibility, accounting/revenue treatment, and decision metrics have been reconciled to the source of truth.

Never use “implemented” as shorthand when the actual state is only configured or partially live.

#### Rollback

Define operational rollback before launch when feasible:

- what term returns to the prior state
- which customer cohorts are affected
- whether already-charged customers require credits/refunds or contractual handling
- system owner
- communication owner
- condition that triggers rollback

A pricing rollback can itself have customer and accounting consequences. It is not equivalent to pausing an ad.

#### Interpretation

After the observation window:

1. validate implementation and measurement first
2. compare the pre-specified primary metric and guardrails
3. separate realized effect from mechanism interpretation
4. inspect package/customer mix only as pre-specified or clearly labeled exploratory analysis
5. record whether the result transfers to other segments, markets, renewal cohorts, or products
6. update the experiment learning system when a controlled test was used

#### Guardrails

- Do not stop a pricing test early because conversion or revenue looks favorable unless a pre-specified harm rule triggers.
- Do not call a price increase successful from ARPU alone.
- Do not call a price decrease successful from conversion alone.
- Do not hide a failed guardrail behind aggregate revenue growth.
- Do not combine a simultaneous major offer, page, audience, and pricing change and then claim the price caused the result.
- Do not reuse approval for a different price, segment, market, package, or migration scope.
- Do not generalize a new-customer result to renewal pricing without evidence.
- Do not describe a live price as verified until the source-of-truth charged amounts and accounting treatment reconcile.

### Reference: pricing architecture ($pricing-monetization)

### Pricing Architecture

Use this reference when the decision concerns base price, value metric, packaging, tiers, payment structure, or discount architecture.

#### Core distinctions

Keep these separate:

- **Base price**: nominal amount before conditional discounts or fees.
- **Realized price**: what customers actually pay after discounts, credits, fees, refunds, and mix.
- **Value metric**: the unit that scales price, such as product, seat, usage, project, subscription period, or another measurable unit.
- **Package / tier**: a defined bundle of entitlement, quantity, service, access, limits, or support.
- **Payment model**: one-time, recurring, installment, usage-based, prepaid, retainer, project, or hybrid structure.
- **Discount architecture**: documented rules for when realized price differs from list price.

A business can change one without changing the others.

#### Economic floor

A pricing decision needs the relevant unit economics before it can be called commercially viable. Name the profit level and include decision-relevant costs such as:

- product or service delivery cost
- payment processing
- fulfillment/shipping where applicable
- returns, refunds, cancellations, chargebacks
- variable support/service cost
- commissions or channel fees
- taxes or marketplace fees when borne by the business
- incremental capacity or implementation cost

The economic floor is not automatically the recommended price. It identifies where a price or package becomes structurally unsafe under the stated assumptions.

#### Value metric test

A useful value metric should be evaluated on:

1. **Customer alignment**: does paying more generally correspond to receiving more value or consuming more of the service?
2. **Predictability**: can customers understand and forecast the charge?
3. **Business alignment**: does the metric reasonably track cost-to-serve or value capture?
4. **Measurability**: can the business measure the unit reliably?
5. **Resistance to gaming**: does the metric create avoidance behavior that destroys product value?
6. **Segment fit**: does the same unit make sense across materially different customer segments?

No value metric is proven by theory alone. Treat a proposed metric as a commercial hypothesis until customer behavior and economics support it.

#### Package and tier design

Create multiple packages only when there is a real segmentation or delivery reason. Useful differentiators can include:

- quantity or usage allowance
- capability/entitlement boundary
- service level or response time
- implementation/support scope
- contract length or commitment
- access/seat count
- risk transfer or operational responsibility

Avoid cosmetic tiers where the only purpose is to make one option look artificially attractive.

For each package record:

| Field | Package |
|---|---|
| Intended segment / buying situation | |
| Job / value difference | |
| Entitlements / limits | |
| Price and payment terms | |
| Expected realized price | |
| Variable cost / cost-to-serve | |
| Contribution implication | |
| Capacity implication | |
| Cannibalization / mix risk | |
| Migration / eligibility rule | |

#### Discount architecture

Discounting changes realized price and must be evaluated as part of pricing, not as a harmless promotion layer.

Document:

- eligibility
- discount amount/method
- duration
- stacking rule
- frequency
- renewal behavior
- channel or segment scope
- expected mix
- margin consequence

A discount should solve a defined commercial problem. Do not use permanent discounting to hide that list price is not the real price.

#### Scenario model

Compare candidate structures using ranges where uncertainty is material.

At minimum model:

`Realized revenue = eligible volume × conversion/close rate × realized price`

Then evaluate contribution at the named profit level, not revenue alone.

For recurring businesses include retention/renewal effects when the observation window allows it. For ecommerce include order mix, units/order, shipping/fulfillment, refund/return effects, and discount mix when material.

Do not present a scenario as a forecast guarantee. State assumptions, sensitivity, and which input most changes the decision.

#### Guardrails

Reject or flag a structure that depends on:

- a fabricated reference price or fake crossed-out price
- hidden mandatory fees
- confusing unit conversion designed to obscure an increase
- materially worse cancellation or renewal disclosure
- unsupported “most popular” or “best value” labels
- package restrictions that contradict product truth or approved service capability

The strongest architecture is one the business can explain plainly and operationally honor.

### Reference: willingness to pay evidence ($pricing-monetization)

### Willingness-to-Pay Evidence

Use this reference when the business wants to estimate price sensitivity, willingness-to-pay, acceptable tradeoffs, or value perception.

There is no single observed field called “willingness to pay.” Different methods produce different evidence strengths and biases.

#### Evidence layers

##### 1. Realized purchase behavior

Strongest direct commercial evidence when definitions are comparable:

- actual transactions at known prices
- renewal behavior after price changes
- close rate at quoted prices
- expansion/downgrade behavior
- refund/cancellation/return behavior after purchase
- product/package mix at known commercial terms

Observed purchases still contain confounds such as channel mix, offer changes, seasonality, promotions, product changes, and selection effects. They are behavior evidence, not automatically causal pricing evidence.

##### 2. Controlled behavioral evidence

Examples include properly designed price/package experiments or controlled quote/offer tests. These can support causal price decisions when measurement, allocation, exposure, lag, and contamination are decision-ready.

Route experiment validity to `$tracking-measurement`.

##### 3. Structured stated-preference research

Surveys, interviews, tradeoff exercises, and sales discovery can reveal:

- price objections
- reference points
- budget process
- perceived value drivers
- package preferences
- tradeoffs customers say they would make
- relative sensitivity across segments

This evidence is useful, but stated intention is not purchase behavior. Do not convert an interview statement such as “I would pay X” into a verified demand curve.

##### 4. Sales/support anecdotes

Useful for generating hypotheses when traceable, but vulnerable to selection and recall bias. “Sales says prospects think we are expensive” is not enough to set a new price without knowing which prospects, compared with what, and whether price actually caused the loss.

##### 5. Competitor and market context

Competitor list prices, marketplace prices, third-party estimates, and category conventions can provide context. They do not prove:

- what customers actually pay
- competitor margin
- competitor conversion/retention
- customer willingness-to-pay for this product
- an optimal relative position

#### Research design rules

Before collecting stated preference, define:

- decision to be made
- segment and buying situation
- current price/package context shown to participants
- realistic alternatives
- whether the research seeks qualitative language, relative tradeoff, or numeric estimation
- sample/source and known selection bias
- how results will be combined with behavior and economics

Avoid leading respondents toward a desired price. Do not present artificial savings, unsupported reference prices, or impossible packages inside the research stimulus.

#### Triangulation

A decision becomes stronger when several independent evidence types point in the same direction and their biases differ.

Example:

- customers consistently describe the same value driver
- realized mix shows stronger adoption of the package containing that driver
- a controlled price/package test maintains contribution and retention guardrails

That combination is stronger than any one input alone.

When sources disagree, preserve the contradiction and investigate segment, channel, timing, package, acquisition source, and research-design differences rather than averaging the conflict away.

#### Output

Return:

- decision being supported
- segment/buying situation
- evidence sources by layer
- what each source actually establishes
- known bias/confound
- observed price/value signals
- contradictions
- numeric estimates only where the method supports them
- confidence and scope
- missing evidence that could reverse the pricing decision

#### Guardrails

- Never fabricate willingness-to-pay percentages, ranges, elasticity, or demand curves.
- Do not call a survey response observed demand.
- Do not infer affordability from demographics alone.
- Do not treat non-purchase as price rejection without evidence separating price from product, offer, timing, trust, competition, or sales execution.
- Do not remove negative or contradictory evidence to create a cleaner pricing story.
- Do not generalize one segment's price response to another without evidence.
