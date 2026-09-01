# Input Evidence

**Status:** Synthetic worked example

## Decision to make

What is the highest-priority conversion problem on Packwell's Shopify product journey, and what should remain unchanged until that problem is validated?

## Funnel evidence

Latest 30 days, synthetic:

| Metric | Current | Prior | State |
|---|---:|---:|---|
| Product-page sessions | 48,000 | 44,000 | Observed |
| Add-to-cart rate | 9.4% | 9.1% | Observed |
| Checkout-start rate from PDP sessions | 5.7% | 5.6% | Observed |
| Purchase rate from PDP sessions | 1.65% | 2.05% | Observed |
| Checkout completion | 29% | 37% | Observed |
| Mobile checkout completion | 24% | 34% | Observed |
| Desktop checkout completion | 42% | 43% | Observed |

## Page evidence

- Hero clearly shows the organizer set and primary use case.
- Product price is visible before scrolling.
- Variant selection is simple.
- Add-to-cart CTA is visible on mobile without excessive scrolling.
- Product-page add-to-cart behavior is stable, not collapsing.
- Shipping cost is only revealed after address entry in checkout.
- Delivery estimate language on PDP says “ships fast” but gives no specific range.
- Returns summary is buried near the bottom of the PDP.
- Mobile checkout has a large promotional-code field above the order total.

## Synthetic customer/support evidence

These are fictional observations created only for the example:

- “I didn't know what shipping would cost until checkout.”
- “I was trying to figure out whether it would arrive before my trip.”
- “I went looking for a discount code because checkout asked for one.”
- “The organizer looked useful, but I wasn't sure whether returns were easy if it didn't fit my suitcase.”

These statements are synthetic teaching inputs, not publishable testimonials.

## Traffic evidence

- Paid traffic mix changed only slightly by device and channel.
- Landing-page sessions increased, while add-to-cart behavior remained stable.
- There is no supplied evidence that paid traffic quality alone explains the checkout drop.

## Offer/pricing state

- Base price is approved and unchanged.
- No new price decision is requested.
- Current promotion is supplied as legitimate and already approved.

## Unknowns

- Exact contribution impact of any checkout-information change.
- Whether shipping uncertainty, delivery timing, promo-code salience, returns uncertainty, or a technical issue is the largest causal driver.
- Whether Shopify checkout configuration allows every proposed UI change in the merchant's current plan/runtime.

## Evidence boundary

The evidence supports a checkout-stage diagnosis. It does **not** support a claim that the entire PDP, brand design, price, or traffic acquisition system is broken.
