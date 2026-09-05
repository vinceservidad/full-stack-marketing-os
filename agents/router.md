# Marketing Agent Router — role view

**This file does not route.** Routing is owned by
[`$marketing-router`](../.agents/skills/marketing-router/SKILL.md), which applies
[`CAPABILITY-REGISTRY.md`](../CAPABILITY-REGISTRY.md) before answering and refuses to
route to a capability that does not exist.

This is the role-facing view of the same map: which human role a request would
land on, and which governed skill actually owns the decision.

| Request | Role | Owning skill |
|---|---|---|
| Marketing strategy, unclear scope | Marketing Strategist | `$marketing-router`, then `$marketing-intake` when evidence state is unknown |
| Integrated growth priorities with decision-ready context | Marketing Strategist | `$growth-strategy` |
| Google Ads Search, Shopping, Performance Max | Paid Media Specialist | `$google-ads` |
| Meta Ads structure, audiences, delivery | Paid Media Specialist | `$meta-ads` |
| YouTube, TikTok, LinkedIn, programmatic buying | Paid Media Specialist | `$youtube-ads`, `$tiktok-ads`, `$linkedin-ads`, `$programmatic` |
| Ad angles, hooks, concepts, creative tests | Creative Director | `$creative-strategy` |
| Email, website, sales-page, brand copy | Creative Director | `$copywriting` |
| Landing page, product page, checkout friction | CRO Specialist | `$cro` |
| Shopify conversion review | CRO Specialist | `$cro`, using `frameworks/shopify-cro.md` |
| Organic search visibility, technical health, content strategy | SEO Specialist | `$seo` |
| Tracking, attribution differences, event integrity | Analytics Specialist | `$tracking-measurement` |
| Metric change, spend or sales anomaly | Analytics Specialist | `$performance-diagnostics` |
| Cross-channel executive report, scorecard, cadence | Reporting Analyst | `$marketing-reporting` |
| Budget increase, scale readiness, de-scaling | Paid Media Specialist | `$optimization-scaling` |

The canonical router and intake contracts determine when missing context blocks a
decision and when clearly labeled provisional advice can proceed. This role view
does not add a second routing or approval rule.
