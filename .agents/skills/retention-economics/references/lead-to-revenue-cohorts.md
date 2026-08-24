# Lead-to-Revenue Cohorts

Extends cohort economics to lead generation and long sales-cycle businesses, where the gap between marketing conversion and realized revenue can be weeks or quarters. Read alongside [Cohort and retention analysis](cohort-and-retention-analysis.md).

## Why lead generation needs a separate method

Ecommerce cohorts mature in days; lead-generation cohorts mature on the sales cycle, which can exceed a typical reporting period. A lead cohort's revenue is systematically incomplete until the cycle closes — treating incomplete cohorts as final understates value and can trigger a premature scale-down of a channel that is actually performing, just not yet realized.

## Method

1. Cohort by lead-creation date, not by opportunity-creation or close date; cohorting on a later stage survivorship-biases the analysis toward leads that already progressed.
2. Track each cohort through its stages — lead, marketing qualified, sales qualified, opportunity, customer — using the stage definitions `$marketing-intake` recorded, joined from the Customer Relationship Management system.
3. Report cohort revenue only after stating what share of the cohort has reached each stage and what share remains open. An "open" lead is neither won nor lost; do not treat it as either.
4. Compute conversion rate and revenue per lead-cohort period as cycle length increases, and mark the point at which a cohort is judged mature enough for a stable read — typically when the open share has fallen below a stated threshold.
5. Separate pipeline velocity (how fast leads move through stages) from revenue lag (how long until cash or booked revenue appears); a channel can accelerate the first without changing the second, or the reverse.

## Rules

- Never report a lead cohort's conversion rate or revenue as final while a material share remains open; state the open share alongside any interim figure.
- Do not compare a mature channel's cohort conversion rate against an immature cohort from a newer channel; normalize for cycle stage first.
- A sudden apparent drop in lead quality in the most recent cohorts is often incomplete maturation, not a real decline; check open share before concluding quality fell.
- Join marketing source to Customer Relationship Management outcome at the lead level, not at an aggregate channel level, so misattributed or unsourced leads do not silently inflate or deflate a channel's realized cohort revenue.
- A lead-to-revenue conclusion used for a scaling decision must satisfy the `optimization-scaling` conversion-lag and marginal-evidence gates in addition to this cohort's own maturity threshold.
