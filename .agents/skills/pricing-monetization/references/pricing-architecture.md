# Pricing Architecture

Use this reference when the decision concerns base price, value metric, packaging, tiers, payment structure, or discount architecture.

## Core distinctions

Keep these separate:

- **Base price**: nominal amount before conditional discounts or fees.
- **Realized price**: what customers actually pay after discounts, credits, fees, refunds, and mix.
- **Value metric**: the unit that scales price, such as product, seat, usage, project, subscription period, or another measurable unit.
- **Package / tier**: a defined bundle of entitlement, quantity, service, access, limits, or support.
- **Payment model**: one-time, recurring, installment, usage-based, prepaid, retainer, project, or hybrid structure.
- **Discount architecture**: documented rules for when realized price differs from list price.

A business can change one without changing the others.

## Economic floor

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

## Value metric test

A useful value metric should be evaluated on:

1. **Customer alignment**: does paying more generally correspond to receiving more value or consuming more of the service?
2. **Predictability**: can customers understand and forecast the charge?
3. **Business alignment**: does the metric reasonably track cost-to-serve or value capture?
4. **Measurability**: can the business measure the unit reliably?
5. **Resistance to gaming**: does the metric create avoidance behavior that destroys product value?
6. **Segment fit**: does the same unit make sense across materially different customer segments?

No value metric is proven by theory alone. Treat a proposed metric as a commercial hypothesis until customer behavior and economics support it.

## Package and tier design

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

## Discount architecture

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

## Scenario model

Compare candidate structures using ranges where uncertainty is material.

At minimum model:

`Realized revenue = eligible volume × conversion/close rate × realized price`

Then evaluate contribution at the named profit level, not revenue alone.

For recurring businesses include retention/renewal effects when the observation window allows it. For ecommerce include order mix, units/order, shipping/fulfillment, refund/return effects, and discount mix when material.

Do not present a scenario as a forecast guarantee. State assumptions, sensitivity, and which input most changes the decision.

## Guardrails

Reject or flag a structure that depends on:

- a fabricated reference price or fake crossed-out price
- hidden mandatory fees
- confusing unit conversion designed to obscure an increase
- materially worse cancellation or renewal disclosure
- unsupported “most popular” or “best value” labels
- package restrictions that contradict product truth or approved service capability

The strongest architecture is one the business can explain plainly and operationally honor.