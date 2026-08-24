# Geo Experiments and Quasi-Experimental Designs

Used when users cannot be split cleanly but geographies can. Randomized geo assignment reaches C4; matched or synthetic designs reach C3.

## Randomized geo experiment

Randomly assign comparable regions to treatment and control, change spend in treatment only, and compare business outcomes.

- Require enough regions for randomization to balance. A handful of large markets does not randomize; it pairs.
- Regions must be economically independent. Adjacent metros, shared media markets, and national retail or delivery footprints leak.
- Balance on pre-period outcome level, trend, seasonality, and size — then verify balance rather than assuming it.
- Run for the full conversion lag plus a stable post-change period.

## Matched-market test (C3)

Where randomization is impossible, pair each treated region with the most similar untreated region on pre-period behavior. This is quasi-experimental: unobserved differences remain a competing explanation, and the estimate is provisional.

## Synthetic control and interrupted time series (C3)

Construct a counterfactual from a weighted combination of untreated regions, or model the pre-period series and compare post-change deviation. Both require a stable, well-fitted pre-period and no coincident shock. Report the pre-period fit; a design that cannot reproduce the pre-period does not support a post-period claim.

## Switchback

Alternate treatment on and off on a fixed schedule within the same region. Suitable only when the effect is short-lived relative to the switching interval. Carryover between periods biases the estimate toward zero; state the assumed carryover window and make the interval longer than it.

## Common failures

- National promotions, PR events, or competitor activity overlapping the window.
- Regional seasonality differing between arms — weather, holidays, term dates, paydays.
- Insufficient regions for the effect size sought.
- Spend changed in treatment without verifying delivery actually changed.
- Measuring platform-attributed conversions by region instead of business outcomes by region.
- Population differences mistaken for treatment effect because balance was assumed, not tested.

## Reading the result

Report effect size, confidence interval, minimum detectable effect, pre-period balance or fit, and every coincident event considered and excluded. State the design level (C3 or C4) explicitly, and name the scope in which the estimate holds.
