# Attribution Integrity

Affiliate commission is paid on a tracked event, almost always last-click within a cookie window. That mechanism has well-known structural weaknesses that directly determine whether a paid commission reflects genuine incremental value — understanding them is a prerequisite to evaluating any commission report, not an optional deep-dive.

## Known structural weaknesses

**Last-click bias.** The affiliate credited is whichever partner's link the customer clicked last before converting, regardless of what actually persuaded the purchase decision. A content partner that built genuine purchase intent earlier in the journey routinely loses credit to a coupon or cashback partner clicked moments before checkout.

**Cookie duration and overwriting.** A longer cookie window increases the chance an unrelated later click overwrites an earlier, more influential one. Confirm the cookie duration in use and who it favors — typically the partner positioned closest to checkout.

**Cross-device and cross-session gaps.** A customer who researches on one device and purchases on another breaks cookie-based tracking entirely in many configurations, understating some partners' contribution and potentially crediting none.

**Coupon-code leakage.** A customer who searches for a coupon code mid-checkout — regardless of what originally drove them to the site — can trigger credit to a coupon-site partner that did not create the original demand. This is one of the most common ways tracked commission diverges from actual incremental contribution.

## Method

1. Document the actual attribution configuration in use: cookie duration, last-click or another model, cross-device handling, and whether coupon-code entry alone can trigger credit.
2. Identify which partner types are structurally favored by the current configuration (typically checkout-adjacent partners: coupon, cashback, loyalty) and which are structurally disadvantaged (typically upper-funnel content and comparison partners).
3. Where the decision at stake requires knowing the program's actual incremental contribution — not just tracked commission volume — route to `$tracking-measurement` for an incrementality design; this reference documents the tracking mechanism's known bias, it does not itself establish incremental value.
4. Consider a partner-type-differentiated attribution or commission model (e.g., a smaller window or lower rate for checkout-adjacent partner types) as a mitigation once the bias is documented, rather than treating the default last-click configuration as neutral.

## Rules

- Do not report tracked commission volume as a measure of the program's business contribution without stating the attribution mechanism's known bias toward checkout-adjacent partners.
- Do not conclude a partner type (coupon, cashback) is high-performing from tracked conversion volume alone without checking whether coupon-code leakage inflates its apparent contribution.
- Do not assume cross-device customers are a small, ignorable share without checking; the share varies widely by category and audience, and an unchecked assumption can substantially understate true contribution from upper-funnel partners.
- A cookie-duration or attribution-model change is a real change to who gets paid for what; treat it with the same before/after evaluation discipline as any other measurement change, not as a routine configuration tweak.
