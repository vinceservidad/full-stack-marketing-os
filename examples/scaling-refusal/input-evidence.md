# Input Evidence

**Status:** Synthetic worked example. All figures are fictional.

## Supplied by the client

| Input | Value | Evidence state | Note |
|---|---|---|---|
| Meta reported ROAS, last 14 days | 4.2 | Observed | Platform-reported, Meta default 7-day click / 1-day view |
| Meta spend, last 14 days | £14,000 | Observed | |
| Meta spend, prior 14 days | £13,600 | Observed | |
| Meta reported ROAS, prior 14 days | 4.4 | Observed | |
| Meta reported revenue, last 14 days | £58,800 | Calculated | 14,000 × 4.2 |
| Meta reported revenue, prior 14 days | £59,840 | Calculated | 13,600 × 4.4 |
| Google Ads reported revenue, last 14 days | £21,400 | Observed | |
| Google Ads spend | — | **Unknown** | Not supplied; blended media cost cannot be completed |
| Shopify net revenue, last 14 days | £71,200 | Observed | Business source of truth, all channels |
| Shopify net revenue, prior 14 days | £69,900 | Observed | |
| COGS | "roughly 45%" | **Asserted** | No artifact supplied |
| Fulfillment, payment fees | — | **Unknown** | Not supplied |
| Refund rate | "low" | **Asserted** | Not a number |
| Promotion in window | 20% off flash sale, last weekend | Observed | Inside the recent period, absent from the comparison period |
| Creative in rotation | 3 ads, all live since February | Observed | |
| Inventory position | — | **Unknown** | Not supplied |
| Authorization to change budgets | Not given | Observed | Client said "just tell me what to do" |

## Derived figures

| Figure | Value | Evidence state | Calculation |
|---|---:|---|---|
| Platform-reported total revenue | £80,200 | Calculated | 58,800 + 21,400 |
| Platform overclaim vs business | £9,000 (12.6%) | Calculated | 80,200 − 71,200, over 71,200 |
| Spend increment | +£400 | Calculated | 14,000 − 13,600 |
| Reported revenue change | −£1,040 | Calculated | 58,800 − 59,840 |
| Contribution ceiling, last 14 days | ≤ £25,160 | Calculated | (71,200 × 0.55) − 14,000, at the **asserted** COGS |

The contribution ceiling uses an asserted input and omits every unsupplied cost
line. It bounds the answer; it does not establish it.

## What the client believes

| Belief | Evidence state |
|---|---|
| "Best ROAS we've had" | Observed for the platform-reported metric; **unknown** for the business outcome |
| "20% is the safe increment that doesn't reset learning" | **Assumed** — a repeated heuristic, no source, not account-specific |
| Meta performance is improving | **Contradicted** — reported ROAS fell 4.4 → 4.2, and the increment is negative |

## Not established

- Whether the business was profitable in either period
- What the £71,200 owes to organic, email, direct, or returning customers
- How much of the recent period's revenue the promotion pulled forward
- Whether Meta's reported revenue survives reconciliation at all
- Whether inventory could absorb increased demand
