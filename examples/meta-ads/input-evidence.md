# Input Evidence

**Status:** Synthetic worked example

All values below are fictional teaching data. They demonstrate evidence handling; they are not benchmarks or expected Meta Ads results.

## Business context

| Item | Synthetic evidence | State |
|---|---:|---|
| Business model | DTC ecommerce | Synthetic fact |
| Primary product | Modular everyday organizer | Synthetic fact |
| Average order value | $72 | Synthetic fact |
| Gross margin before media | 62% | Synthetic fact |
| Refund/return rate | 4% | Synthetic fact |
| Primary business objective | Acquire profitable new customers while preserving contribution | Synthetic decision context |
| Market | United States | Synthetic fact |
| Analysis window | Last 14 complete days vs prior 14 complete days | Synthetic fact |

The business has not supplied a verified incrementality study. Platform attribution is therefore useful platform evidence, not proof of incremental revenue.

## Measurement state

| Evidence | Current state | Classification |
|---|---|---|
| Meta dataset/pixel events | Purchase events visible | Synthetic platform observation |
| Conversions API | Enabled | Synthetic platform observation |
| Deduplication | No known alert, but event-level reconciliation not supplied | Synthetic observation + unresolved dependency |
| Meta-attributed purchase revenue | $28,700 | Synthetic platform-attributed value |
| Store revenue from sessions tagged to Meta | $22,400 | Synthetic business analytics value |
| Difference | $6,300 | Calculated difference |
| New-customer contribution after media | Not supplied | Unknown |
| Incremental lift | Not measured | Unknown |

Do not choose the larger revenue number as “correct” without reconciling definitions, attribution, windows, and identity/session limitations.

## Account summary

| Area | Spend | Meta-attributed revenue | Platform ROAS | Notes |
|---|---:|---:|---:|---|
| Prospecting | $10,500 | $19,950 | 1.90x | Main new-customer acquisition layer |
| Retargeting | $3,500 | $8,750 | 2.50x | 30-day site-engaged pool in this synthetic setup |
| Total | $14,000 | $28,700 | 2.05x | Platform attribution only |

Prior 14-day synthetic platform ROAS was 2.42x at $11,200 spend. The current period has more spend and more attributed revenue, but lower platform efficiency. Business contribution is still unknown.

## Prospecting audience/ad-set snapshot

| Audience approach | Spend | Meta-attributed CPA | Purchase CVR after landing-page view | Notes |
|---|---:|---:|---:|---|
| Broad | $7,500 | $40 | 2.8% | Received most of the strongest static creative |
| Interest-based | $3,000 | $49 | 2.2% | Received more of the video creative |

This snapshot does **not** prove broad targeting is inherently better. Creative allocation, spend level, delivery, and audience composition differ.

## Creative snapshot

| Creative ID | Concept | Format | Spend | Outbound CTR | Landing-page-view / outbound-click rate | Purchase CVR after LPV | Meta-attributed CPA | State |
|---|---|---|---:|---:|---:|---:|---:|---|
| C01 | “Stop digging through your bag” | 4:5 static | $4,200 | 1.3% | 78% | 3.1% | $38 | Synthetic account evidence |
| C02 | “What fits inside” | Short video | $3,200 | 2.4% | 64% | 1.4% | $62 | Synthetic account evidence |
| C03 | “Organized without looking utilitarian” | 4:5 lifestyle static | $2,000 | 1.1% | 76% | 2.8% | $44 | Synthetic account evidence |
| C04 | New removable-section concept | 4:5 static | $1,100 | 1.5% | 75% | 2.5% | $47 | Early / lower spend |

CTR is not the decision metric. C02 gets attention but loses more users before/after the landing page and currently has weaker purchase economics in this synthetic snapshot.

## Delivery snapshot

| Layer | Current frequency | Prior frequency | Response note |
|---|---:|---:|---|
| Prospecting | 2.1 | 1.8 | Outbound response slightly lower |
| Retargeting | 8.4 | 6.2 | Outbound response and purchase rate both lower |

Rising retargeting frequency plus worsening response is **suggestive** of saturation/fatigue. It does not prove creative fatigue by itself; audience size, exclusions, event quality, offer, site behavior, and delivery changes remain possible explanations.

## Destination evidence

- All prospecting creatives land on the same product page.
- No verified checkout defect is supplied.
- Mobile landing-page-view to purchase conversion is lower than desktop in the synthetic analytics export.
- The video C02 uses a “what fits” promise, while the first product-page viewport emphasizes appearance and material rather than capacity/organization.

That message mismatch is a hypothesis input, not proof that the page caused C02’s weaker purchase rate.

## Recent changes

- Spend increased from $11,200 to $14,000 between comparison windows.
- Two new creatives launched during the current period.
- No verified price change.
- No verified promotion change.
- No verified product stockout.
- No official platform documentation supplied that would support an “algorithm change” explanation.

## Authorization

The user requested an audit and test plan only. No budget, audience, ad status, publishing, bid, or campaign mutation is authorized in this example.
