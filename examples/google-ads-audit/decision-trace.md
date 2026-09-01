# Decision Record

**Status:** Synthetic worked example

## Routing

`$google-ads` owns campaign/query/product/bidding/budget diagnosis. `$tracking-measurement` is consulted only for measurement questions. `$optimization-scaling` decides readiness after the channel owner establishes what is actually working.

## Decision record

| Evidence | State | Diagnosis / interpretation | Decision implication | Validation needed |
|---|---|---|---|---|
| Brand Search 7.50x ROAS with high impression share | Observed | Brand demand capture is efficient in platform reporting | Protect coverage; do not raid brand budget just because non-brand is weaker | Incrementality is still unknown, so do not call all brand revenue incremental |
| Non-brand spend +34%, revenue +12% | Observed | Marginal expansion produced weaker return | Inspect where added spend went before further scaling | Query, match-type, device, geo and campaign marginal breakdown |
| Adjacent/informational terms consume 21% of non-brand spend | Observed | Part of marginal spend appears weak against the stated direct-response objective | Reduce/exclude only the clearly poor-fit subset after query review | Check assisted/lagged evidence where relevant |
| Strong converting non-brand terms remain | Observed | Non-brand is not globally broken | Preserve proven demand; do not blanket-pause the campaign | Continue query-level monitoring |
| Low-margin product group 1.90x | Observed + commercial model | Average revenue efficiency is insufficient for several SKUs after product economics | Product-level budget/feed/campaign control is higher priority than account-wide tROAS guessing | Confirm SKU contribution and current product labels |
| Four low-margin SKUs absorb disproportionate spend | Observed | Product mix is distorting account-level ROAS | Restrict or separate weak-economics products where architecture allows | Product-level volume and learning impact |
| High-margin group 3.30x with healthy inventory | Observed | Better candidate for controlled expansion | Prepare a budget/reach test only after marginal threshold is defined | Marginal efficiency under additional spend |
| Automated recommendations say increase budgets | Platform suggestion | Google identifies available traffic, not business profitability | Do not accept automatically | Business economics and scaling gate decide |
| Tracking supplied stable | Observed scenario input | No evidence of a tracking defect | Do not make “fix tracking first” the default recommendation | Reopen only if a new anomaly appears |

## Account diagnosis

The account does **not** need a blanket pause or blanket scale.

The main commercial issue is **allocation quality**:

1. non-brand marginal expansion is weaker than the prior base
2. low-margin products receive too much spend relative to contribution
3. strong high-margin demand still exists and may support controlled expansion

## Actions

### Protect

- Brand demand coverage while monitoring actual business role.
- Proven non-brand queries with strong commercial fit.
- High-margin products with healthy inventory and stable conversion evidence.

### Reduce / restructure

- Clearly adjacent informational query spend that fails the current acquisition objective.
- Product exposure where SKU economics cannot support the current ad cost.
- Any budget increases that are based only on platform recommendations.

### Test

For high-margin products, define a controlled expansion test with:

- current baseline
- incremental budget/exposure change
- primary contribution outcome
- marginal efficiency guardrail
- inventory guardrail
- observation/maturity condition
- rollback/hold rule

## What not to do

- Do not pause all broad match because some broad queries are weak.
- Do not force all products to one ROAS threshold when margins differ.
- Do not increase the whole account budget because total ROAS is above an arbitrary benchmark.
- Do not call platform-attributed revenue incremental revenue.
- Do not rebuild conversion tracking without evidence of a tracking defect.
- Do not judge the scaling test only by average ROAS.

## Status

Draft account recommendations only. No campaign setting, bid, budget, query exclusion, feed label, or product status has been changed.
