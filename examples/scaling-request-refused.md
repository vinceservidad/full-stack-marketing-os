# Worked example: a budget increase the system will not authorize

**Skill under test:** `$optimization-scaling`
**Input:** [`fixtures/scaling-request.md`](fixtures/scaling-request.md)

Synthetic fixture. This is the example worth reading first, because it shows the
system declining to do the thing it was asked to do, and showing its work.

---

## The answer

**No budget change is proposed, and none is executed.** Not because scaling is wrong
here, but because on the evidence supplied it is not yet possible to say whether the
last 14 days represent performance at all.

Three of the seven gates in this skill fail outright, and a fourth cannot be assessed.

---

## Gate 1 — Proof standard: **fail**

The claim is "4.2 ROAS, best we've had." The evidence is Meta's own reported ROAS
under a 7-day click, 1-day view window.

**A platform's self-reported return is not proof that spending more produces more.**
It is a scoped, attributed, in-platform figure. Reconciling it against the business:

| | Last 14 days | Prior 14 days |
|---|---:|---:|
| Meta reported revenue | £58,800 | £59,840 |
| Google Ads reported revenue | £21,400 | — |
| **Platform-reported total** | **£80,200** | — |
| **Shopify net revenue (all channels)** | **£71,200** | £69,900 |
| **Overclaim** | **£9,000 (12.6%)** | — |

Meta and Google together claim £80,200 of a business that took £71,200 — and that
£71,200 also includes organic, email, and direct. The overlap is not a rounding
error; it is larger than the entire growth being celebrated.

## Gate 2 — Economics: **fail**

COGS is *"roughly 45%"* with no artifact — **asserted**, not observed. Fulfillment and
payment fees were not supplied. Refund rate is *"low"*, which is not a number.

Contribution after media cannot be calculated. It can only be bounded:

```
Shopify net revenue, last 14 days              £71,200
At the asserted 45% COGS            × 0.55     £39,160
Media, Meta + Google (Google spend unsupplied)  ≥ £14,000
                                               --------
Contribution before fulfilment, fees, refunds  ≤ £25,160
```

That ceiling drops by every unsupplied cost line. **The business may well be
profitable — the point is that nothing supplied establishes it**, and this system does
not raise a budget while unit economics are unknown.

## Gate 3 — Marginal evidence: **fail, and it inverts the premise**

The request is built on a blended average. The relevant question is what the *last*
increment of spend returned.

| | Spend | Meta reported revenue | Reported ROAS |
|---|---:|---:|---:|
| Prior 14 days | £13,600 | £59,840 | 4.40 |
| Last 14 days | £14,000 | £58,800 | 4.20 |
| **Increment** | **+£400** | **−£1,040** | **negative** |

**The additional £400 of spend is associated with £1,040 less reported revenue.** The
marginal return on the most recent increase is negative even in Meta's own numbers.

"Crushing it" describes the average. The increment — the thing a budget increase
actually buys more of — is going the wrong way. This alone would block the request.

## Gate 4 — Baseline validity: **fail**

A 20% off flash sale ran last weekend, inside the 14-day window and not in the
comparison period. A discount pulls forward demand and lifts attributed revenue at
the expense of margin.

The two periods are **not comparable as supplied**. Either the promotion is isolated
out or the comparison is declared invalid. It cannot be used as a scaling baseline
in its current form — and note this makes Gate 3 *generous*: the marginal return is
negative despite the promotion flattering the recent period.

## Gate 5 — Binding constraint: **not budget**

Three ads have been live since February. The account is not constrained by how much
it is allowed to spend; it is constrained by **creative capacity**. Adding 20% more
budget to three fatiguing ads buys more delivery of assets the audience has already
seen.

This is a diagnosis to test, not a certainty — frequency and creative-level delivery
data were not supplied. But budget is not the constraint the evidence points to.

## Gate 6 — Capacity: **cannot assess**

Inventory position was not supplied. Scaling ecommerce demand into an unknown stock
position risks paying to acquire orders that cannot be fulfilled.

## Gate 7 — Authorization: **not given**

The client said *"just tell me what to do."* That is a request for a recommendation.
It is **not** authorization to change spend, and this system does not treat it as one.

---

## On the "20% is the safe increment" rule

Rejected. There is no universal safe percentage or cadence.

The defensible step size depends on downside exposure, conversion volume, conversion
lag, volatility, capacity, and reversibility — none of which are constant across
accounts, and several of which are unknown here. The rule is also being applied to
the wrong question: the issue is not how large a step to take, it is that the
evidence does not support taking one.

## What to do instead, in order

| # | Action | Why first | Reversible |
|---|---|---|---|
| 1 | Supply a COGS artifact, fulfillment cost, payment fees, and actual refund rate | Every economic conclusion is blocked without them | n/a |
| 2 | Reconcile Meta and Google reported revenue against Shopify by day (`$tracking-measurement` owns) | The 12.6% overclaim must be understood before any figure is trusted | Read-only |
| 3 | Re-cut the last 28 days with the promotion period isolated | Restores a comparable baseline | Read-only |
| 4 | Produce new creative against the existing winning angle (`$creative-strategy` owns) | Addresses the constraint the evidence actually points to | Reversible |
| 5 | Confirm inventory cover for a demand increase | Prevents paying for unfulfillable orders | n/a |

**Only after 1–3** does the scaling question become answerable. If it then supports a
step, it arrives as a change plan with the exact entity, current and proposed state,
a rollback rule, a guardrail, and an explicit approval request — not as a percentage.

## If the client wants to proceed anyway

That is their decision to make, and this system will help them make it deliberately
rather than refuse to engage:

- Take the smallest reversible step on the **single** best-performing ad set, not across the account.
- Change **one** variable. Budget only — no simultaneous bid or targeting change, or the result is uninterpretable.
- Set the guardrail in advance: roll back if contribution after media falls below its pre-change level, measured against Shopify rather than Meta, over a full conversion-lag window.
- Record it as a test with a stopping rule, not as a scaling decision.

## Unknowns

| Unknown | Blocks |
|---|---|
| COGS artifact, fulfillment, fees, refund rate | Gate 2 entirely |
| Google Ads spend | Total media cost, and therefore blended contribution |
| Frequency and creative-level delivery | Confirming Gate 5's creative-capacity diagnosis |
| Inventory position | Gate 6 |
| New versus returning customer split | Whether reported ROAS reflects acquisition |
| Promotion revenue and margin impact | Restoring a valid baseline |

## What this example is for

A 4.2 ROAS and a request for 20% more budget is the most common conversation in paid
media. Almost every tool answers it with a number.

The evidence here supports a different answer: the marginal return on the most recent
increment is **negative**, the platforms are claiming 12.6% more revenue than the
business actually made, a promotion has invalidated the comparison, and the account is
short of creative rather than short of budget.

The 20% increase would probably have looked fine for a fortnight — the promotion's
pulled-forward demand and the attribution overlap would both have flattered it — and
the account would have been worse off underneath.
