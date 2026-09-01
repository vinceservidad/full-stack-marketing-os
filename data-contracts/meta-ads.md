# Meta Ads Data Contract

**Contract ID:** `meta-ads-performance`  
**Contract version:** `1.0`  
**Primary owner for intake completeness:** `$marketing-intake`  
**Measurement semantics:** `$tracking-measurement`  
**Decision owner after validation:** `$meta-ads` or another routed owner

Use this contract for Meta Ads campaign, ad set, ad/creative, audience/delivery, and placement data used by Marketing OS.

This is a normalized decision contract, not a frozen copy of Ads Manager or the Meta API schema.

## Required envelope

Apply [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md) and preserve account timezone, currency, reporting period, source method, attribution setting, optimization event, conversion definitions, and field lineage.

## Recommended grains

Keep these separate when possible:

1. `campaign_performance` — date/period × campaign.
2. `adset_performance` — date/period × campaign × ad set.
3. `ad_performance` — date/period × campaign × ad set × ad.
4. `placement_breakdown` — declared entity grain × placement/platform/device breakdown.
5. `audience_breakdown` — only when source reporting and privacy/aggregation permit decision-valid breakdowns.

Do not duplicate campaign spend/value across ad or placement rows through careless joins.

## Normalized dimensions

Use the dimensions needed for the decision:

- `date` or `period_start` / `period_end`
- `account_id`
- `campaign_id` / `campaign_name`
- `campaign_objective` as source-defined/current label
- `campaign_status`
- `adset_id` / `adset_name`
- `ad_id` / `ad_name`
- `creative_id` where a stable creative/asset identifier is available
- `optimization_event` or performance goal semantics
- `conversion_location` when material
- `audience_mode` or source-defined audience-control context when decision-relevant
- `placement`, `publisher_platform`, `device` when breakdowns are used
- `country`/geography when decision-relevant

Current interface/control labels must pass [`PLATFORM-CURRENCY.md`](../PLATFORM-CURRENCY.md) before being treated as current platform truth.

## Normalized metrics

At the correct grain, include the strongest available base metrics required for the decision:

- `spend`
- `impressions`
- `reach` when available
- `outbound_clicks` or another explicitly named click metric
- `landing_page_views` when available
- `purchases` or other explicitly named conversion event
- `purchase_value` or conversion value
- `video_views` / attention metrics only when relevant to the creative question and their source definition is preserved

`frequency`, CTR, CPC, CPM, LPV rate, CVR, CPA, ROAS, hook/hold rates, and other ratios should preferably be calculated from base fields when the required components are available.

## Attribution and action semantics

Record:

- attribution setting/window used by the report;
- conversion event/action definition;
- optimization event;
- whether conversion value is platform-attributed;
- known modeled/estimated/aggregated limitations exposed by the source;
- whether data is prospecting, retargeting, or another declared strategic segment.

Meta-attributed revenue is not automatically commerce/accounting revenue and is not incremental revenue without stronger causal evidence.

Do not sum action fields that overlap semantically. Preserve action type and source definition when a report contains multiple action/conversion columns.

## Creative identity

A creative decision should be traceable to a stable ad/creative ID where possible.

Preserve separately:

- creative concept/angle labels created by the business or Marketing OS;
- ad/creative IDs from Meta;
- copy, format, asset, destination, and offer changes that materially differ between cells.

Two ads with similar filenames are not automatically the same concept. Two different crop/background variants are not automatically strategically different concepts.

## Audience and delivery interpretation

- Broad, interest, lookalike, retargeting, Advantage+ or other source-defined audience modes must retain the current source meaning.
- One audience outperforming another does not prove audience causality when creative, budget, optimization, placement, timing, or delivery differs.
- Rising frequency plus worsening response is a fatigue/saturation hypothesis, not automatic proof.
- Delivery allocation is an observed system outcome, not proof of why Meta allocated spend that way.

## Minimum decision-valid extracts

### Basic account/campaign audit

At minimum:

- campaign/ad set/ad stable IDs and names at the requested grain
- objective/performance-goal context
- period/date
- spend
- impressions
- outbound clicks or clearly named click metric
- landing-page views when available
- conversion event + count/value
- attribution setting
- account timezone/currency

### Creative audit

Add:

- ad/creative IDs
- format/asset/concept labels if available
- spend/impressions/reach/frequency
- response metrics
- LPV/post-click conversion/value metrics
- destination/offer context if changed across creatives

### Audience/delivery audit

Add:

- audience-control context or audience-group label
- placement/device/geography breakdown only when sample/privacy limits support use
- creative allocation by audience where audience conclusions are being considered

## Rejection/degradation examples

Mark the dataset `degraded` or `rejected` for the scoped decision when, for example:

- Meta-attributed revenue is the only revenue source but the request asks for verified business profitability;
- click type is ambiguous and CTR conclusions depend on it;
- ad names are used as the only creative identity while names were reused/changed;
- audience comparisons are heavily confounded but presented as causal;
- campaign totals are duplicated across ad/placement rows;
- attribution settings changed mid-period without a represented boundary;
- current-platform control recommendations depend on stale or unknown interface state.
