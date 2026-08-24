# User-Level Holdout Experiments

Randomly withholds treatment from a share of users and compares business outcomes. The strongest routinely available design (C4).

## Design

Define the population, randomization unit, split, primary business outcome, minimum detectable effect, duration including full conversion lag, and stopping rule before launch.

- Randomize at the level at which contamination occurs — usually the user or household, not the session or device.
- Size the holdout for power, not for comfort. A holdout too small to detect the expected effect produces an uninformative null.
- Hold the control for the entire period. Releasing it early destroys the comparison and cannot be repaired analytically.
- Measure in the business source of truth, joined to assignment. Platform-reported lift is the platform grading its own work.

## Contamination

The most common cause of a false null. Check each before trusting a result:

- Cross-device and logged-out users landing in both arms.
- Shared households or accounts.
- Other channels retargeting the control group.
- Organic, email, or lifecycle activity correlated with assignment.
- Brand spillover from the treated group.
- Assignment leaking through audience syncs or lookalike seeds built on treated users.

Record the contamination risk and its direction. Contamination almost always biases toward zero, so a null under known contamination is not evidence of no effect.

## Reading the result

- Report effect size with its confidence interval, not a point estimate alone.
- Report the minimum detectable effect alongside any null.
- Convert to business terms — incremental contribution, not incremental attributed conversions.
- Subtract the holdback's forgone revenue when stating the test's net value.
- State the scope: population, period, spend range, creative set. The estimate holds there and is not established elsewhere.

## Rules

- Do not stop early on a favorable read. Do not extend a test to reach significance.
- Do not change targeting, budget, creative, or bidding mid-test; the result then measures the bundle, not the treatment.
- Do not reuse a holdout group across concurrent tests without accounting for interaction.
- A holdout answers whether the tested spend was incremental at that level. It does not establish the incrementality of a larger budget.
