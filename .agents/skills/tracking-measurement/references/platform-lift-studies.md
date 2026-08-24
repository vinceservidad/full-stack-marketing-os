# Platform Lift Studies

Randomized studies run by the ad platform itself — Conversion Lift, Brand Lift, and equivalents. Convenient and genuinely randomized, but graded by the seller.

## What they can support

A well-designed platform lift study is randomized and can reach C4 **for the outcome the platform measures, in the population it holds out, over the window it defines**. It does not establish business-level incrementality unless its conversion definition matches the business source of truth.

## Verify before accepting

- Randomization unit and whether the holdout is genuinely withheld from all of the advertiser's activity on that platform, or only from the tested campaign.
- Conversion definition and whether it matches the primary business outcome.
- Whether reported conversions are modeled; a modeled outcome inside a randomized design caps the level below C4.
- Attribution window and whether it covers the full conversion lag.
- Holdout size and the study's minimum detectable effect.
- Whether the platform selected the study population in a way correlated with likelihood to convert.
- Whether other channels continued reaching the holdout.

## Rules

- Do not treat platform lift as independent verification of that platform's own attribution. It is the same party measuring its own contribution with a better method.
- Do not compare lift results across platforms as if they used one definition. Each defines outcome, window, and holdout differently; the numbers are not commensurable and must not be added.
- Reconcile the study's conversion counts against the business source of truth before using its lift estimate commercially.
- A lift result at the campaign level does not establish incrementality of the platform's whole budget, nor of a larger budget.
- Record who designed, ran, and analyzed the study as part of its provenance.

## When to prefer an independent design

Prefer a user holdout or geo experiment when the decision is large, when the platform's holdout cannot exclude the advertiser's other activity, when the conversion definition cannot be reconciled, or when the result would be used to justify sustained budget increases.
