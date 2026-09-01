# Decision Record

**Status:** Synthetic worked example

## Routing

- `$performance-diagnostics` establishes where the material movement is concentrated.
- `$cro` owns page/checkout friction and the prioritization of conversion hypotheses.
- `$copywriting` supports exact approved wording when needed; it does not own the CRO diagnosis.
- `$offer-strategy` is not invoked unless the commercial proposition itself becomes the diagnosed constraint.
- `$tracking-measurement` owns experiment validity and post-test learning.

## Decision record

| Evidence | State | Diagnosis / interpretation | Decision implication | Validation needed |
|---|---|---|---|---|
| PDP add-to-cart stable at ~9% | Observed | Product interest and primary CTA are not showing a broad collapse | Preserve the core hero/CTA while investigating later-stage friction | Continue device/source segmentation |
| Checkout completion 37% → 29% | Observed | Material loss occurs after checkout start | Checkout is the first priority, not full PDP redesign | Step/device/error breakdown |
| Mobile checkout 34% → 24%; desktop stable | Observed | Problem is concentrated on mobile | Prioritize mobile checkout review | Reproduce on common mobile devices/browsers |
| Shipping cost appears only after address | Observed | Cost uncertainty exists at a sensitive decision stage | Surface shipping expectation earlier where truthful/technically feasible | Test against purchase + contribution guardrails |
| “ships fast” has no delivery range | Observed page fact | Copy is vague and may not resolve trip-date uncertainty | Replace vague speed language with approved factual range when available | Fulfillment truth/source required |
| Promo-code field highly salient | Observed | It may signal that a discount exists and create code-search friction | Reduce salience only if Shopify configuration permits and offer rules remain clear | Controlled test; do not assume universal effect |
| Returns summary buried | Observed | Risk-reversal information may be hard to find | Bring concise approved return terms closer to decision point | Confirm exact policy; no invented guarantee |
| Synthetic support comments echo shipping/arrival/code/returns concerns | Synthetic example evidence | These are plausible friction signals | Use them to prioritize hypotheses, not claim causality | Real customer evidence in real engagement |
| Traffic mix mostly stable | Observed | Acquisition-quality change is not the strongest current explanation | Keep CRO diagnosis primary while monitoring traffic quality | Reopen if source/device quality evidence changes |

## Primary diagnosis

The evidence supports a **mobile checkout information/friction problem** as the first area to investigate.

It does not yet identify one proven micro-cause. The current hypothesis set is:

1. shipping-cost uncertainty
2. delivery-time uncertainty
3. promo-code search distraction
4. return-policy uncertainty
5. mobile checkout technical/usability issue

## Smallest meaningful first change

Before redesigning the product page, create a checkout-support information treatment that makes approved shipping/delivery/returns information clear **before** the buyer encounters uncertainty.

Where Shopify/runtime limitations prevent checkout UI edits, use the closest truthful pre-checkout placement, such as the PDP buy box/cart drawer, while preserving the same hypothesis.

## Test hypothesis

If qualified buyers see clear factual shipping/delivery and concise returns information before the checkout uncertainty point, then eligible mobile purchase completion will improve because fewer buyers need to leave the flow to resolve material purchase questions.

This mechanism is a hypothesis until tested.

## Primary outcome

Mobile purchase completion from eligible checkout-start users, or the closest valid funnel outcome available in the implementation.

## Guardrails

- contribution/order
- cancellation/refund rate
- support contacts about shipping/delivery/returns
- page/cart/checkout errors
- average order value where the treatment could change order composition
- desktop performance if shared components are affected

## Secondary hypothesis

Promo-code salience may cause some buyers to leave and search for a code. Test separately where possible so its effect is not mixed with shipping/returns changes.

## What not to do

- Do not redesign the entire homepage/PDP because purchase rate fell.
- Do not change base price; no pricing diagnosis has been established.
- Do not invent a shipping promise to create confidence.
- Do not hide material shipping costs or conditions.
- Do not remove all promotional messaging merely because the promo-code field is salient.
- Do not call support comments causal proof.
- Do not change five checkout variables in one cell if the goal is to learn which friction matters.

## Status

All changes are **draft hypotheses**. Technical feasibility, policy truth, approval, implementation, and live verification are still required.
