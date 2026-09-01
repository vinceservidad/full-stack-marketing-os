# Price-Change Testing and Rollout

Use this reference when a proposed price, package, value metric, discount rule, or payment model needs to be tested or rolled out.

A price change affects both customer behavior and realized economics. A valid decision therefore needs more than conversion rate.

## Pre-change specification

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

## Metrics

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

## Customer treatment

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

## Rollout states

Keep exact states distinct:

1. **Proposed** — pricing design exists only as a recommendation.
2. **Approved** — authorized commercial terms and scope are recorded.
3. **Configured** — catalog/billing/checkout/contract system contains the intended terms but may not yet be customer-facing.
4. **Live** — eligible customers can actually receive/pay the new terms.
5. **Observed** — transactions or renewals under the new terms exist.
6. **Verified** — charged amounts, eligibility, accounting/revenue treatment, and decision metrics have been reconciled to the source of truth.

Never use “implemented” as shorthand when the actual state is only configured or partially live.

## Rollback

Define operational rollback before launch when feasible:

- what term returns to the prior state
- which customer cohorts are affected
- whether already-charged customers require credits/refunds or contractual handling
- system owner
- communication owner
- condition that triggers rollback

A pricing rollback can itself have customer and accounting consequences. It is not equivalent to pausing an ad.

## Interpretation

After the observation window:

1. validate implementation and measurement first
2. compare the pre-specified primary metric and guardrails
3. separate realized effect from mechanism interpretation
4. inspect package/customer mix only as pre-specified or clearly labeled exploratory analysis
5. record whether the result transfers to other segments, markets, renewal cohorts, or products
6. update the experiment learning system when a controlled test was used

## Guardrails

- Do not stop a pricing test early because conversion or revenue looks favorable unless a pre-specified harm rule triggers.
- Do not call a price increase successful from ARPU alone.
- Do not call a price decrease successful from conversion alone.
- Do not hide a failed guardrail behind aggregate revenue growth.
- Do not combine a simultaneous major offer, page, audience, and pricing change and then claim the price caused the result.
- Do not reuse approval for a different price, segment, market, package, or migration scope.
- Do not generalize a new-customer result to renewal pricing without evidence.
- Do not describe a live price as verified until the source-of-truth charged amounts and accounting treatment reconcile.