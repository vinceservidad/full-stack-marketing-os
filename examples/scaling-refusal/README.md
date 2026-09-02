# Refused Budget Increase — Worked Example

**Status:** Synthetic worked example

This example shows `$optimization-scaling` declining a budget increase that looks
obviously correct on the surface, and showing its work. It is the counterpart to
the other walkthroughs: those show the system producing a deliverable, this one
shows it refusing to.

## Starting request

> "Meta's been crushing it — 4.2 ROAS last 14 days, best we've had. Let's push
> budget up 20% across the account today, and do the same again next week if it
> holds. I've read that 20% is the safe increment that doesn't reset learning."

## Business

Fictional brand: **Harrow Lane**

Category: direct-to-consumer homeware

Market: United Kingdom

Business model: ecommerce, single storefront, Meta and Google both active.

All figures are synthetic.

## Owner chain

```text
$marketing-intake            evidence state of the supplied figures
→ $optimization-scaling      owns the scaling decision and this response
→ $tracking-measurement      owns the platform-versus-business reconciliation
→ $creative-strategy         owns the constraint the evidence actually points to
```

`$optimization-scaling` owns the final response throughout. It consumes the other
skills' outputs; it does not perform their analysis.

## Learning objective

A healthy blended ROAS and a request for a modest, widely-repeated budget step is
the most common conversation in paid media. This example shows why the answer is
not a number:

- the **marginal** return on the most recent increment can be negative while the **blended** average looks strong
- platform-reported revenue can exceed the total revenue the business actually took
- a promotion inside the measurement window invalidates the comparison the decision rests on
- "20% is the safe increment" is a heuristic, not a decision rule
- the binding constraint can be creative capacity while the request is about budget

It also shows the system helping a client proceed deliberately when they choose to
override the recommendation, rather than refusing to engage.
