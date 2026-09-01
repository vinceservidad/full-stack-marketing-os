# Business Economics Data Contract

**Contract ID:** `business-economics`  
**Contract version:** `1.0`  
**Primary owner for intake completeness:** `$marketing-intake`  
**Economics consumers:** `$growth-strategy`, `$pricing-monetization`, `$retention-economics`, `$optimization-scaling`, `$performance-diagnostics`, and other routed owners

Use this contract for the commercial inputs needed to judge profitability, scaling, pricing, retention value, and business outcomes.

The purpose is to stop vague fields such as `margin`, `profit`, `LTV`, or `breakeven` from entering the OS without a defined basis.

## Required envelope

Apply [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md) and record business scope, period, currency, source/owner, freshness, accounting/management-reporting basis, and field lineage.

## Profit levels

Never use `profit` without naming the level.

Common named levels can include, when appropriate to the business:

- gross profit;
- contribution before media;
- contribution after media;
- operating profit;
- another explicitly defined internal management measure.

For each level, list included and excluded costs.

## Core normalized fields

Use only fields supported by the source/business model. Examples:

- `gross_sales`
- `discounts`
- `refunds_returns`
- `net_sales`
- `cogs`
- `variable_fulfillment`
- `payment_fees`
- `sales_commissions`
- `marketplace_or_channel_fees`
- `variable_support_or_service_cost`
- `media_spend`
- `contribution_before_media`
- `contribution_after_media`
- `fixed_costs` only when the scoped decision genuinely requires them and their allocation method is declared

Do not subtract the same cost twice merely because it appears in more than one source.

## Grain

Economics may exist at different grains. Declare one clearly:

- business × period;
- market/geography × period;
- product/SKU × period;
- order/order-line;
- customer/cohort × period;
- channel/campaign × period;
- service/project/account × period.

A business-level margin cannot automatically be applied to every product, market, or customer segment.

## Unit economics

When available, record the components needed for the decision rather than only the final ratio:

- realized price / revenue per order/customer/account;
- COGS or delivery cost;
- variable fulfillment/service/support cost;
- payment/channel fees;
- refund/return/cancellation allowance or realized value;
- acquisition spend/cost when relevant;
- contribution at the named level.

Derived metrics may include CAC, CPA, MER, ROAS, contribution margin, break-even ROAS, payback, LTV, and LTV:CAC. Every derived metric must record its formula, input basis, observation window, and whether it is realized or predictive.

## Break-even ROAS

Break-even ROAS is not a universal constant.

If calculated from contribution margin before media:

```text
break_even_roas = 1 / contribution_margin_before_media
```

only use that relationship when the numerator/denominator definitions and included costs actually match the decision. Taxes, shipping, returns, fees, variable service costs, and other business-specific costs can change the correct basis.

## LTV and payback

- Separate realized cohort value from predictive/modelled LTV.
- Name cohort start, observation cutoff, revenue/profit basis, and maturity.
- Predictive LTV must preserve model assumptions and uncertainty.
- Do not authorize pricing or scaling from an unlabeled model output alone.
- Customer mix, acquisition source, offer, price/package, geography, or product changes may require separate cohorts.

## Capacity and constraints

Economics decisions can be invalid if the business cannot fulfill the resulting demand. Where material, include or join:

- inventory/stock availability;
- fulfillment/service capacity;
- lead handling/sales capacity;
- cash/payback constraints;
- minimum order/contract economics;
- geographic or regulatory constraints.

These are guardrails, not optional narrative notes when they can reverse the decision.

## Pricing inputs

When pricing is in scope, keep separate:

- list/base price;
- realized price;
- discounts/credits;
- package/tier/payment model;
- fees;
- existing-customer treatment;
- product/service cost and cost-to-serve.

Competitor price and survey answers belong to their own evidence classes; they are not fields proving willingness to pay.

## Minimum decision-valid extracts

### Paid-media scaling

At minimum:

- declared business revenue basis;
- contribution margin or cost components sufficient to calculate a relevant contribution basis;
- current media spend;
- refund/return/cancellation maturity when material;
- capacity constraints;
- currency and period.

### Pricing decision

Add:

- current realized/base price and payment terms;
- product/service cost-to-serve;
- discount mix;
- package/tier state;
- existing-customer treatment where relevant.

### Retention/LTV decision

Add:

- cohort definition;
- repeat/renewal/cancellation outcomes;
- realized contribution/revenue basis;
- observation maturity;
- acquisition/offer/price context where materially different across cohorts.

## Rejection/degradation examples

Mark the dataset `degraded` or `rejected` for the scoped decision when, for example:

- `margin = 45%` is supplied without saying gross vs contribution and included costs;
- blended business margin is applied to SKU profitability despite materially different product economics;
- predictive LTV is labeled realized;
- revenue includes tax/shipping in one period but excludes them in another without adjustment;
- refunds/returns are immature but treated as final;
- mixed currencies are compared without an FX rule;
- a scaling recommendation ignores a known stock/capacity/cash constraint.
