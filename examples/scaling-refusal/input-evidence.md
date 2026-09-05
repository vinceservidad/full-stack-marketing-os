# Input Evidence

**Status:** Synthetic worked example. All dates, figures, exports, and statements are fictional. `Observed` means present in this supplied fixture, not verified in a live account.

## Scope and definitions

- Snapshot: 1 September 2026, using the store's Europe/London reporting timezone.
- Recent period: 18–31 August 2026. Prior period: 4–17 August 2026. Both contain 14 calendar days.
- Platform revenue means the value attributed in each supplied platform summary; its value basis and reporting date convention have not been reconciled to Shopify.
- Shopify net revenue is order-date revenue from all channels, after discounts and recorded refunds, excluding tax and shipping revenue, as recorded at the snapshot. Later refunds and conversion lag have not been assessed.
- Target cost scope for contribution profit after media: Shopify net revenue minus COGS, variable fulfillment, payment fees, other applicable variable servicing costs, and **all** media spend. Fixed operating costs are excluded; this is not operating profit.

## Supplied inputs

| Input | Recent period | Prior period | Evidence state / limitation |
|---|---:|---:|---|
| Meta reported ROAS | 4.2 | 4.4 | Observed; period-average attributed value/spend, not business profit |
| Meta spend | £14,000 | £13,600 | Observed; actual spend, not the campaign budget settings |
| Meta attribution setting shown in fictional export | 7-day click / 1-day view | Same | Observed in fixture; not a claim about current platform defaults |
| Google Ads reported revenue | £21,400 | Not supplied | Observed / Unknown; value basis and attribution settings unresolved |
| Google Ads spend | Not supplied | Not supplied | Unknown; all-media cost cannot be completed |
| Shopify net revenue | £71,200 | £69,900 | Observed; business revenue source, all channels |
| Promotion | 20% off flash sale on 29–30 August | None supplied | Observed; effect on demand, mix, margin, and timing is unknown |
| Meta creatives | Three ads, each live since February 2026 | Same three ads | Observed; reach, frequency, spend concentration, performance, and production capacity unknown |

| Other input | Supplied statement / state | Evidence classification |
|---|---|---|
| COGS | Stakeholder says "roughly 45%"; no cost artifact or denominator definition | Statement observed; cost ratio unverified. Use only as an explicit assumption in the illustration below |
| Variable fulfillment, payment fees, other applicable variable costs | Not supplied | Unknown |
| Refunds | Stakeholder says "low"; no cohort or maturity detail | Statement observed; future refund exposure unknown. Recorded refunds already reduce Shopify net revenue |
| Inventory, fulfillment headroom, cash position | Not supplied | Unknown |
| Funnel reliability and downstream order quality | Not supplied | Unknown |
| Current campaign budgets, delivery limits, eligible demand | Not supplied | Unknown |
| Authorization | Recommendation only; no live changes | Observed and explicit |

## Reproducible calculations

| Figure | Calculation | Result | Interpretation boundary |
|---|---|---:|---|
| Meta reported revenue, recent | £14,000 × 4.2 | £58,800 | Derived from the supplied ROAS and spend |
| Meta reported revenue, prior | £13,600 × 4.4 | £59,840 | Same basis within the fictional Meta summary |
| Sum of recent platform-reported revenue | £58,800 + £21,400 | £80,200 | An arithmetic sum, not deduplicated business revenue |
| Gap between that sum and Shopify net revenue | £80,200 − £71,200 | £9,000 | Attribution/value/date differences unresolved; not proof of a tracking defect |
| Gap as a percentage of Shopify net revenue | £9,000 ÷ £71,200 × 100 | 12.6% rounded | Shopify net revenue is the denominator |
| Meta spend difference | £14,000 − £13,600 | +£400 | Raw period difference |
| Meta reported revenue difference | £58,800 − £59,840 | −£1,040 | Raw period difference; neither a profit loss nor the effect of added spend |
| Shopify net revenue difference | £71,200 − £69,900 | +£1,300 | All-channel period difference; no channel causality established |

The promotion appears only in the recent period, while lag, attribution alignment, product mix, and other changes remain unresolved. These periods do not supply a decision-ready marginal estimate. Dividing the revenue difference by the spend difference would produce arithmetic, not a credible estimate of what an added pound of budget will return. No causal incrementality claim is supported.

## Conditional economics illustration

For arithmetic only, **assume** COGS equals exactly 45% of the defined Shopify net revenue. This denominator and rate have not been verified:

```text
Assumed COGS = £71,200 × 0.45 = £32,040
Remainder after assumed COGS and known Meta spend
  = £71,200 − £32,040 − £14,000
  = £25,160
```

£25,160 is an incomplete, assumption-dependent subtotal. It is **not** verified contribution profit after media, and the uncertain COGS input prevents calling it an actual upper bound. Under this assumption, Google Ads spend and every other applicable variable cost still need to be deducted. Any mismatch in revenue definitions, later refunds, or cost allocation also needs resolution.

Do not deduct the 20% promotion or recorded refunds again: both are already included in the supplied net revenue. New refund adjustments would need an explicit basis and reconciliation to avoid double-counting.

## Claims and unknowns

- The claim "best we've had" is contradicted by the supplied prior Meta ROAS of 4.4 versus 4.2. Neither value establishes business improvement.
- "20% is safe and does not reset learning" is an unsupported stakeholder heuristic, not an account-specific decision rule or current platform fact.
- Whether either period produced acceptable contribution profit after media is unknown.
- Cross-platform attribution overlap is one possible explanation for the £9,000 gap. Revenue definitions, windows, reporting dates, and collection defects are separate possibilities to investigate.
- The flash sale may affect comparability, but pull-forward, cannibalization, and contribution impact have not been measured.
- Three long-running ads do not establish creative fatigue, a production bottleneck, or an absence of additional eligible demand.
- Budget constraint, inventory capacity, maximum acceptable downside, guardrails, and evidence maturity remain unknown.
