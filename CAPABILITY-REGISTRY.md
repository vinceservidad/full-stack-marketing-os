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
| Customer research: interviews, reviews, surveys, evidence synthesis | `$customer-research` |
| Ideal Customer Profile and Jobs-to-be-Done | `$icp-jtbd` |
| Optimization and scaling: readiness, marginal economics, portfolio, de-scaling | `$optimization-scaling` |

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

A bounded report is owned by the skill that owns the underlying decision. Not covered: cross-channel executive reporting, budget and outcome pacing, forecasting and reforecasting, recurring reporting governance, and report-production systems. A dedicated reporting specialist is planned.

### Copywriting

| In scope | Owner |
|---|---|
| Paid-ad hooks, concepts, message angles, creative briefs | `$creative-strategy` |
| Conversion-page copy evaluation | `$cro`, supported by `$customer-research` and `$creative-strategy` where evidence is needed |

Not covered: email, lifecycle, website, sales-page, long-form, brand, and Search Engine Optimization copywriting. Do not route general copywriting to `$creative-strategy` as though it were governed.

## Planned

| Capability | Reference |
|---|---|
| Marketing reporting specialist | `ROADMAP.md` |
| Retention and customer economics | `ROADMAP.md` |
| Measurement validity and incrementality method selection | `ROADMAP.md` |

## Unsupported

No governed specialist. Do not substitute an adjacent channel skill.

- Search Engine Optimization and content strategy
- Email marketing and lifecycle marketing
- TikTok Ads
- LinkedIn Ads
- YouTube advertising as a dedicated discipline
- Affiliate and partnership marketing
- Influencer and creator marketing
- Organic social
- Programmatic advertising
- Public relations

Root `frameworks/seo-framework.md`, `frameworks/copywriting-frameworks.md`, and related artifacts remain in the repository as governed knowledge, but no skill loads them and they do not constitute a specialist. See `ARTIFACT-OWNERSHIP.md`.

## Handling an uncovered request

1. Do not silently substitute the nearest channel skill.
2. Name the capability gap explicitly in the response.
3. Apply platform-agnostic frameworks only where they genuinely address a distinct part of the request.
4. Label any platform-specific guidance as ungoverned and unverified by this system.
5. Do not invent a skill name that does not exist.
6. State the gap in the response's exact-status line.
