# Web Analytics Data Contract

**Contract ID:** `web-analytics`  
**Contract version:** `1.0`  
**Primary owner for intake completeness:** `$marketing-intake`  
**Measurement semantics:** `$tracking-measurement`  
**Decision owners:** `$performance-diagnostics`, `$cro`, `$growth-strategy`, or another routed owner

Use this contract for GA4 or another web/product analytics source used to understand traffic, landing behavior, events, funnels, and analytics-attributed outcomes.

Do not freeze one vendor UI vocabulary as the Marketing OS semantic model. Preserve the source label and map it to the business meaning required for the decision.

## Required envelope

Apply [`DATA-CONTRACTS.md`](../DATA-CONTRACTS.md) and record property/source scope, timezone, currency where relevant, report/query generation time, date range, attribution/reporting identity, privacy/thresholding/sampling/modeling limitations when known, and field lineage.

## Recommended grains

Use separate datasets or explicit grain declarations for:

1. `traffic_daily` — date × source/medium/campaign or another declared acquisition grain.
2. `landing_page_daily` — date × landing page × acquisition/device context.
3. `event_daily` — date × event name × declared segments.
4. `funnel_steps` — cohort/period × defined funnel step when funnel analysis is required.
5. `ecommerce_summary` — date/period × declared analytics attribution dimensions.

Do not join event-level counts, session-level counts, and user-level counts as if they share the same denominator.

## Normalized dimensions

Use the dimensions needed for the decision:

- `date` or `period_start` / `period_end`
- `source`
- `medium`
- `campaign`
- `campaign_id` when the source reliably exposes it
- `landing_page`
- `page_path` / page location when needed
- `device_category`
- `country`/region where appropriate
- `new_returning` or source-defined user type when decision-relevant
- `event_name` or normalized business-event label with source lineage

Preserve source-defined channel-grouping logic if used. Do not silently treat source/medium, default channel group, paid-platform campaign, and business channel as interchangeable dimensions.

## Normalized metrics

Use only metrics whose denominator/entity is clear:

- `sessions`
- `users` / `active_users` or another explicitly source-defined user metric
- `engaged_sessions` when available and relevant
- `views` / pageviews where relevant
- `event_count`
- business-event/key-event/conversion count with the exact source meaning recorded
- `transactions` / purchases when available
- `analytics_revenue` with its source attribution/revenue basis

Derived rates such as engagement rate, session CVR, user CVR, landing-page CVR, and funnel completion rate must name their numerator and denominator.

## Event semantics

For every decision-critical event, preserve:

- source event name;
- business meaning;
- trigger definition if known;
- whether it is client-side/server-side/imported/derived when relevant;
- whether the definition changed during the period;
- expected deduplication/uniqueness behavior;
- known implementation gaps.

A source label such as “key event,” “conversion,” or another current UI term is not enough by itself. State the actual customer/business action represented.

## Attribution and revenue

Analytics attribution is a source-specific view of contribution, not universal business truth.

- Keep analytics-attributed revenue separate from Google Ads/Meta attributed value and commerce/accounting revenue.
- Do not sum those sources together.
- Preserve the attribution/reporting model and lookback/window where the source exposes them or the analysis depends on them.
- If direct/organic/referral classification changes because of tagging or consent behavior, treat mix shifts cautiously.

## Landing-page and funnel analysis

- Keep page/session/user denominators distinct.
- A landing page with low CVR is not automatically defective when traffic intent/mix differs.
- A funnel step drop-off is an observation, not proof of the mechanism.
- When checkout/purchase events disagree with commerce orders, reconcile with `$tracking-measurement` before claiming a true business conversion change.

## Minimum decision-valid extracts

### Acquisition/traffic diagnosis

At minimum:

- date/period
- source/medium/campaign or declared channel dimension
- sessions or another clearly defined traffic metric
- business-event/transaction metric when available
- property timezone
- attribution/reporting identity

### Landing-page CRO diagnosis

Add:

- landing page
- device/source/intent segments as available
- sessions/users with clear denominator
- defined conversion/business event
- technical/error evidence from another source when a defect is being claimed

### Cross-platform reconciliation

Add:

- campaign/source identifiers where reliable
- transaction/event counts and analytics revenue basis
- tagging/UTM conventions
- known consent/modeling/privacy limitations

## Rejection/degradation examples

Mark the dataset `degraded` or `rejected` for the scoped decision when, for example:

- session and user metrics are mixed without clear denominators;
- conversion event definitions changed mid-period but the boundary is unknown;
- analytics revenue is presented as accounting revenue without reconciliation;
- UTM/tagging changes make source-mix comparisons non-comparable;
- a page defect is claimed from CVR alone without evidence of the mechanism;
- privacy/thresholding/sampling/modeling behavior materially limits a segment but is ignored.
