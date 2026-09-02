# Decision Trace

**Status:** Synthetic worked example.

`$optimization-scaling` applies its gates in order. A gate that fails does not
end the analysis — the later gates change what should happen instead.

## Decision record

| Evidence | Evidence state | Diagnosis / interpretation | Decision implication | Validation needed |
|---|---|---|---|---|
| Meta reports 4.2 ROAS under a 7-day click / 1-day view window | Observed | A platform's self-reported return is a scoped attributed figure, not evidence that more spend produces more revenue | Cannot satisfy the proof standard on its own | Reconciliation against the business source of truth |
| Meta + Google report £80,200; Shopify took £71,200 across all channels | Calculated | The platforms claim 112.6% of total company revenue, before any of it is apportioned to organic, email, or direct. The overlap exceeds the growth being celebrated | Every platform-derived figure in the request is unreliable | `$tracking-measurement` owns a day-level reconciliation |
| COGS asserted at "roughly 45%", no artifact; fulfillment, fees, refund rate unsupplied | Asserted / Unknown | Contribution after media cannot be calculated, only bounded at ≤ £25,160 | Profitability is blocked, not estimated | A COGS artifact and the missing cost lines |
| Spend +£400, reported revenue −£1,040 across the two periods | Calculated | The marginal return on the most recent increment is negative in Meta's own numbers, while the blended average reads healthy | This alone blocks a budget increase | Re-cut after reconciliation and promotion isolation |
| 20% off flash sale inside the recent window, absent from the comparison | Observed | A discount pulls demand forward and lifts attributed revenue at the expense of margin. The periods are not comparable | The scaling baseline is invalid as supplied | Isolate the promotion or declare the comparison void |
| Three ads live since February | Observed | The account is not constrained by permitted spend; it is short of creative. More budget buys more delivery of assets the audience has already seen | Budget is not the binding constraint | Frequency and creative-level delivery data |
| Inventory position unsupplied | Unknown | Scaling demand into an unknown stock position risks paying to acquire unfulfillable orders | Capacity gate cannot be assessed | Stock cover for a demand increase |
| "Just tell me what to do" | Observed | A request for a recommendation is not authorization to change spend | No live change is proposed or made | Explicit approval, against a specific change plan |

## Gate results

| Gate | Result | Reason |
|---|---|---|
| Proof standard | **Fail** | Platform attribution offered as proof; overclaims the business by 12.6% |
| Economics | **Fail** | COGS asserted; fulfillment, fees, refunds unsupplied |
| Marginal evidence | **Fail** | Most recent increment returns negative |
| Baseline validity | **Fail** | Promotion inside the measurement window only |
| Binding constraint | Not budget | Creative capacity, on the available evidence |
| Capacity | Cannot assess | Inventory unknown |
| Authorization | Not given | Recommendation requested, not approval granted |

The baseline failure makes the marginal finding **more** severe, not less: the
increment is negative *despite* a promotion flattering the recent period.

## On the "20% is safe" rule

Rejected. There is no universal safe percentage or cadence. Defensible step size
depends on downside exposure, conversion volume, conversion lag, volatility,
capacity, and reversibility — none constant across accounts, several unknown here.

The rule is also answering the wrong question. The issue is not how large a step
to take; it is that the evidence does not support taking one.

## Non-priorities

Explicitly **not** recommended now:

- Do not increase budget, on any campaign, by any percentage
- Do not restructure the account — nothing in the evidence points to structure
- Do not pause the campaign either; a negative increment is not a reason to withdraw spend that has not been shown unprofitable
- Do not change bid strategy and budget together; that makes the next result uninterpretable
- Do not treat the reconciliation as a tracking cleanup task to be done later — it gates every figure in the request
