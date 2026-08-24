# Verification and Fraud Screening

Programmatic's fragmented, multi-party supply chain creates more opportunity for inflated or fabricated metrics than a single walled-garden platform, where the platform itself is directly accountable for its own reporting. Independent, third-party verification is the primary defense — not a nice-to-have add-on.

## What to verify independently

**Viewability** — whether an impression was actually rendered in a viewable position on screen, per an industry-recognized standard (such as the Media Rating Council's viewability definition), rather than accepting a served-impression count as equivalent to a viewable one.

**Invalid traffic** — bot and non-human traffic, both general invalid traffic (detectable via known patterns) and sophisticated invalid traffic (harder to detect, often indistinguishable from genuine traffic without specialized detection). A meaningful invalid-traffic rate inflates delivered volume without corresponding genuine audience reach.

**Brand safety and suitability** — whether ads served adjacent to content the business would consider unsafe or unsuitable, measured against a stated policy rather than a generic default.

## Method

1. Confirm an independent, third-party verification vendor is in place and its methodology is current — verification standards and detection methods evolve, and a vendor relationship or configuration from a prior period should be periodically reconfirmed rather than assumed still adequate.
2. Compare the DSP's or seller's self-reported metrics against the independent verification vendor's figures; a persistent, large discrepancy is itself a signal worth investigating rather than defaulting to either source as automatically correct.
3. Set explicit thresholds for acceptable viewability rate and invalid-traffic rate, and treat inventory or supply sources falling outside them as a screening and potential exclusion candidate, not a rounding error.
4. Where brand-safety or suitability incidents occur, document them and adjust exclusion lists rather than relying solely on a static category-based safety setting to prevent recurrence.

## Rules

- Do not accept viewability, invalid-traffic, or brand-safety figures from the party financially benefiting from favorable numbers (the DSP, the supply-side platform, or the individual seller) as sufficient verification on their own.
- Do not treat a low invalid-traffic rate as evidence of overall inventory quality; sophisticated invalid traffic is specifically designed to evade basic detection, and a clean basic-IVT reading does not rule it out.
- A large, persistent discrepancy between self-reported and independently verified metrics is a fraud or misconfiguration signal requiring investigation, not a rounding difference to average away.
- Do not treat verification as a one-time setup; detection methods and fraud tactics change, and a verification configuration should be periodically reconfirmed as current.
