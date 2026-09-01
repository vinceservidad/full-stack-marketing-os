# Activation Definition and Evidence

Use this reference when deciding what counts as activation and whether the current definition is strong enough for decisions.

## Core distinction

Activation is the first behavior or outcome that credibly indicates the customer has received meaningful value from the product, service, or relationship. It is not automatically the first logged-in session, setup step, tutorial completion, purchase confirmation, or any event labeled “activation” in an analytics tool.

A valid activation definition should satisfy three questions:

1. **Value:** does the event represent customer progress toward the promised outcome?
2. **Specificity:** is the event meaningfully different from mere presence, setup, or administrative completion?
3. **Evidence:** what supports the claim that this event matters in this business and segment?

## Evidence ladder for activation candidates

From weaker to stronger decision support:

- **Category convention:** another company or framework calls this event activation.
- **Internal assertion:** team believes the event is the “aha moment.”
- **Qualitative evidence:** customers consistently describe this step as the point value became clear or useful.
- **Observed behavioral association:** customers reaching the event show different downstream behavior, with cohort/segment and obvious confounding considered.
- **Replicated predictive evidence:** the association holds across comparable cohorts and periods.
- **Controlled evidence:** an intervention that changes reaching the event also changes a downstream value outcome under a valid design.

Do not collapse this ladder into “proven/not proven.” State the current level and what uncertainty remains.

## Candidate event test

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

## Business-model examples as hypotheses, not defaults

- **SaaS/app:** completing a real job, publishing/using a core output, connecting required data and receiving a useful result.
- **Marketplace:** completing the first successful value exchange, not merely creating a listing or account.
- **Service:** completing the first substantive delivery or achieving an agreed milestone, not just booking the kickoff.
- **Lead generation:** a qualified lead reaching a meaningful sales/service step may be an activation-like milestone, but do not relabel lead progression when the customer has not yet received value.
- **Subscription/ecommerce:** receipt, first use, successful replenishment setup, or another post-purchase event can matter when meaningful value occurs after purchase. If purchase itself is the decision-relevant outcome and no post-purchase activation decision exists, do not create one.

These are prompts for analysis, never universal definitions.

## Metric contract

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

## Time to value

Report a distribution where possible rather than only an average:

- median time to value
- relevant percentiles or bands
- censored/not-yet-activated share
- segment differences
- operational waiting time versus active customer effort where distinguishable

A faster value time is only desirable when value quality and guardrails remain intact.

## Correlation caution

Customers who activate may already be more motivated, better fit, better resourced, or easier to serve. An observed retention difference does not prove the activation event caused retention.

Use `$tracking-measurement` when the decision requires a causal claim.

## Anti-gaming rules

Do not:

- define activation as a step almost everyone completes just to make the rate look strong
- exclude slow or difficult customers after results are known
- expand the window after a miss without preserving the original read
- choose whichever candidate event correlates best after scanning many events and present it as pre-specified proof
- count synthetic/system-generated events as customer value without validating what they mean
- convert email clicks or tutorial completion into value because they are easy to move

## When no activation definition is needed

State `no distinct activation layer` when:

- the primary customer value is substantially realized at conversion/purchase itself, and
- there is no decision-relevant post-conversion milestone the marketing system can or should manage separately.

This is a valid conclusion, not a missing framework.
