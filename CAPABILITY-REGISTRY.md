# Capability Registry

Declares what the Marketing OS governs, what it partially covers, and what it does not cover. The Marketing Router applies this registry before routing. A capability absent from the `Governed` table has no governed specialist, regardless of any framework, playbook, template, or export file that discusses the topic.

Status definitions:

- **Governed** — a canonical skill in `.agents/skills/` owns the capability end to end.
- **Partially covered** — a canonical skill owns a defined portion. Work outside that boundary has no specialist and must be labeled.
- **Planned** — accepted on `ROADMAP.md`, not yet built. Not available.
- **Unsupported** — no governed specialist and none currently scheduled.

Existence of a document is not coverage. A capability is governed only when a skill owns it, declares its evidence requirements, states its authorization boundary, and defines its output contract.

## Governed

| Capability | Owner |
|---|---|
| Request routing and owner appointment | `$marketing-router` |
| Engagement intake: scope, evidence grading, metric definitions, access, authorization | `$marketing-intake` |
| Google Ads: Search, Shopping, Performance Max | `$google-ads` |
| Meta Ads: structure, audiences, delivery, placements | `$meta-ads` |
| Creative strategy: angles, hooks, concepts, briefs, tests | `$creative-strategy` |
| Conversion Rate Optimization: pages, forms, checkout, friction | `$cro` |
| Performance diagnosis: metric change, anomaly, causal triage | `$performance-diagnostics` |
| Tracking and measurement: event integrity, attribution reconciliation | `$tracking-measurement` |
| Measurement validity: causal evidence grading, incrementality method selection, holdouts, geo experiments, lift studies, Marketing Mix Modeling, triangulation | `$tracking-measurement` |
| Customer research: interviews, reviews, surveys, evidence synthesis | `$customer-research` |
| Ideal Customer Profile and Jobs-to-be-Done | `$icp-jtbd` |
| Optimization and scaling: readiness, marginal economics, portfolio, de-scaling, budget/outcome pacing | `$optimization-scaling` |
| Retention economics: lifetime value, payback period, cohort retention, churn, lead-to-revenue cohorts | `$retention-economics` |
| Search Engine Optimization: visibility audit, technical health, content and topic strategy, ranking-change diagnosis | `$seo` |
| Copywriting: email, lifecycle, website, sales-page, long-form, brand — with paid-ad hooks staying under `$creative-strategy` and conversion-page copy under `$cro` | `$copywriting` |
| Email and lifecycle program strategy: segmentation, trigger logic, cadence, deliverability | `$lifecycle-marketing` |
| YouTube video advertising: format selection, targeting, view-through measurement fit | `$youtube-ads` |
| TikTok advertising: native creative fit, Spark Ads vs in-feed, targeting breadth, creative-fatigue cadence | `$tiktok-ads` |
| LinkedIn advertising: account/firmographic targeting, format selection, Lead Gen Forms, B2B cost-structure economics | `$linkedin-ads` |
| Influencer and creator marketing: audience authenticity/fit vetting, compensation structure, usage rights, disclosure compliance | `$influencer-marketing` |
| Affiliate and partner marketing: commission structure, attribution integrity, fraud/brand-bidding screening | `$affiliate-marketing` |
| Organic social: content strategy, cadence, algorithm-distribution fit, community management | `$organic-social` |
| Programmatic: supply-path optimization, inventory verification, fraud screening | `$programmatic` |
| Cross-channel executive reporting, recurring cadence, stakeholder scorecards | `$marketing-reporting` |

## Partially covered

### Analytics

| In scope | Owner |
|---|---|
| Tracking architecture, event integrity, attribution differences, source reconciliation | `$tracking-measurement` |
| Performance analysis, segmentation, anomaly diagnosis, competing explanations | `$performance-diagnostics` |
| Marginal business evidence and allocation analysis | `$optimization-scaling` |

Not covered: business-intelligence engineering, data-warehouse or pipeline design, dashboard implementation, and analytics deliverables outside the three owners above.

### Reporting

| In scope | Owner |
|---|---|
| Google Ads audit report | `$google-ads` |
| Meta Ads audit report | `$meta-ads` |
| Diagnostic performance report | `$performance-diagnostics` |
| Measurement integrity report | `$tracking-measurement` |
| Scaling review and decision log | `$optimization-scaling` |
| Cross-channel executive report, scorecard, recurring cadence, stakeholder translation | `$marketing-reporting` |

A bounded single-channel or single-decision report stays owned by the skill that owns that decision. `$marketing-reporting` combines their outputs across channels — it does not perform the underlying audit, diagnosis, reconciliation, or economics analysis. Budget and outcome pacing remain owned by `$optimization-scaling`. Not covered: report-production systems and data-warehouse/dashboard implementation.



## Planned

| Capability | Reference |
|---|---|

## Unsupported

No governed specialist. Do not substitute an adjacent channel skill.

- Public relations

See `ARTIFACT-OWNERSHIP.md` for artifacts awaiting a specialist in the disciplines above.

## Handling an uncovered request

1. Do not silently substitute the nearest channel skill.
2. Name the capability gap explicitly in the response.
3. Apply platform-agnostic frameworks only where they genuinely address a distinct part of the request.
4. Label any platform-specific guidance as ungoverned and unverified by this system.
5. Do not invent a skill name that does not exist.
6. State the gap in the response's exact-status line.
