# Examples

## Worked runs

Three complete deliverables, each reproducible from a fixture in
[`fixtures/`](fixtures/). These show the actual output shape and standard, not a list
of headings.

| Example | Skill | What it demonstrates |
|---|---|---|
| [Google Ads audit](google-ads-audit.md) | `$google-ads` | Three measurement defects that invalidate a 5.07x blended ROAS; brand masking near-break-even acquisition; why only one of four zero-conversion queries earns a negative |
| [Shopify product page review](cro-audit.md) | `$cro` | Localizing the loss before explaining it; the largest finding drawn from the store's own review language; one finding handed to a different owner because no page change fixes it |
| [A budget increase the system will not authorize](scaling-request-refused.md) | `$optimization-scaling` | **Start here.** The guardrails firing: negative marginal return under a healthy blended average, a 12.6% platform overclaim, a promotion invalidating the baseline, and the "20% is safe" rule rejected |

Every fixture is synthetic. No client data appears in this repository, and no example
contains a performance claim about a real account or a prediction of what a change
would produce.

## Outlines

The remaining files are structural outlines of a process, not worked deliverables:
[meta-ads-audit](meta-ads-audit.md), [ecommerce-growth-review](ecommerce-growth-review.md),
[creative-strategy-brief](creative-strategy-brief.md),
[google-ads-audit-workflow](google-ads-audit-workflow.md),
[meta-ads-creative-testing-workflow](meta-ads-creative-testing-workflow.md),
[shopify-cro-audit-workflow](shopify-cro-audit-workflow.md),
[custom-gpt-setup](custom-gpt-setup.md). They are labeled as such rather than
presented as demonstrations of output.

## Contributing an example

An example should demonstrate problem diagnosis, framework selection, strategy
development, an execution plan, and a measurement approach — and should carry its
input fixture so a reader can reproduce it.

Do not include client confidential information, account access details, personal data,
or unverified performance claims. `scripts/check-confidentiality.sh` enforces the
first three in CI; the fourth is a review judgment.
