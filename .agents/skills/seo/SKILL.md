---
name: seo
description: Audit or plan organic search visibility, content strategy, and technical health using search-console and crawl evidence; not for paid search, and not for claiming a ranking cause without isolating other concurrent changes.
---

# Search Engine Optimization

Classify each model, pattern, or recommendation with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A ranking or traffic change coinciding with a content or technical change is a hypothesis, not a confirmed cause, until competing explanations are ruled out.

Organic search has no equivalent to a Google Ads conversion goal or Meta dataset — there is no platform-native attribution to lean on and no bid lever to pull. Every claim here rests on search-console data, crawl evidence, and the business source of truth; do not borrow paid-media attribution language or assume paid-media capacity levers apply.

## Context

Primary business outcome from organic search and its profit level per `$marketing-intake`; site or subdomain scope; date range and comparison, noting algorithm updates or known volatility windows inside either period; search-console and analytics access; current indexation and crawl status; competitive and category context; content production and technical/engineering capacity; and whether the request is an audit, a content or architecture plan, or a technical health diagnosis.

## Method

1. Establish the primary business outcome from organic search — qualified traffic, revenue, or leads at the correct profit level — not raw ranking position or impression count alone.
2. Map current visibility: ranking distribution, click-through by position and query, indexation coverage, and crawl health, from search-console and log data rather than a third-party rank tracker alone.
3. Segment by search intent — informational, commercial, transactional, navigational — before proposing content or architecture changes; a technically sound page targeting the wrong intent will not convert.
4. Diagnose technical health: crawlability, indexation, page experience, structured data, and canonicalization. See [Technical health](references/technical-health.md).
5. Build content and information-architecture recommendations from evidence of demand and existing coverage gaps, not from keyword volume alone. See [Content and topic strategy](references/content-and-topic-strategy.md).
6. When a ranking or traffic change is observed, rule out algorithm updates, seasonality, competitive entry, technical regressions, and measurement changes before attributing it to a specific content or link action. See [Ranking change diagnosis](references/ranking-change-diagnosis.md).
7. Rank actions by expected business impact, confidence, reversibility, and the content or engineering capacity actually available.

## Rules

- Do not claim a ranking or traffic change was caused by a specific action when a concurrent algorithm update, seasonal pattern, or technical regression offers a competing explanation; grade the claim on the causal evidence ladder in `$tracking-measurement` rather than asserting it.
- Do not present a documented Google algorithm behavior as a fact without applying `PLATFORM-CURRENCY.md`; distinguish official documentation, observed account behavior, industry inference, and unknowns.
- Do not recommend content or technical changes solely from search volume; require intent match and existing coverage evidence.
- Do not propose a content plan that exceeds stated production capacity; a plan that cannot be executed is not a plan.
- Do not recommend a technique that risks a manual action or algorithmic penalty — content designed primarily to manipulate ranking rather than serve intent, undisclosed paid links, cloaking, or doorway pages.
- Preserve indexed, ranking, and linked-to content unless evidence supports removal or consolidation; a redirect or removal is a change requiring the same rollback discipline as any other live change.
- Do not conflate organic and paid search performance; a page's Google Ads performance does not establish anything about its organic potential and vice versa.

## Output

Audit: scope; current visibility and technical health; findings with evidence, impact, and confidence; content and technical gaps; prioritized actions with capacity check; unknowns; exact status.

Content or architecture plan: proposed structure or content set; intent mapping; existing coverage addressed; production capacity required; expected impact and confidence; measurement plan.

Ranking change diagnosis: observed change; competing explanations considered and ruled out or confirmed; remaining hypothesis; evidence level; recommended next step.

## QA

Confirm the primary business outcome and profit level are stated, visibility evidence comes from search-console or crawl data rather than a third-party estimate alone, intent match precedes any content or architecture recommendation, algorithm and platform-currency claims are separated from inference, content and technical plans respect stated production capacity, and no ranking-change claim is presented as confirmed without ruling out competing explanations.
