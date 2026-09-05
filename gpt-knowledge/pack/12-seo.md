<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Search Engine Optimization

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/seo/SKILL.md`

---
name: seo
description: Audit or plan organic search visibility, content strategy, and technical health using search-console and crawl evidence; not for paid search, and not for claiming a ranking cause without isolating other concurrent changes.
---

# Search Engine Optimization

Classify each model, pattern, or recommendation with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). A ranking or traffic change coinciding with a content or technical change is a hypothesis, not a confirmed cause, until competing explanations are ruled out.

Organic search has no equivalent to a Google Ads conversion goal or Meta dataset — there is no platform-native attribution to lean on and no bid lever to pull. Every claim here rests on search-console data, crawl evidence, and the business source of truth; do not borrow paid-media attribution language or assume paid-media capacity levers apply.

## Context

Primary business outcome from organic search and its profit level per `$marketing-intake`; site or subdomain scope; date range and comparison, noting algorithm updates or known volatility windows inside either period; search-console and analytics access; current indexation and crawl status; competitive and category context; content production and technical/engineering capacity; and whether the request is an audit, a content or architecture plan, or a technical health diagnosis.

## Method

1. Establish the primary business outcome from organic search — qualified traffic, revenue, or leads at the correct profit level — not raw ranking position or impression count alone.
2. Map current visibility: ranking distribution, click-through by position and query, indexation coverage, and crawl health, from search-console and log data rather than a third-party rank tracker alone.
3. Segment by search intent — informational, commercial, transactional, navigational — before proposing content or architecture changes; a technically sound page targeting the wrong intent will not convert.
4. Diagnose technical health: crawlability, indexation, page experience, structured data, and canonicalization. See Technical health (source: `.agents/skills/seo/references/technical-health.md`).
5. Build content and information-architecture recommendations from evidence of demand and existing coverage gaps, not from keyword volume alone. See Content and topic strategy (source: `.agents/skills/seo/references/content-and-topic-strategy.md`).
6. When a ranking or traffic change is observed, rule out algorithm updates, seasonality, competitive entry, technical regressions, and measurement changes before attributing it to a specific content or link action. See Ranking change diagnosis (source: `.agents/skills/seo/references/ranking-change-diagnosis.md`).
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

## Source: `.agents/skills/seo/references/content-and-topic-strategy.md`

# Content and Topic Strategy

Builds content and information-architecture recommendations from intent and coverage evidence, not from search volume alone. A high-volume query with strong existing competitive coverage and weak commercial relevance to the business is not automatically worth targeting.

## Method

1. Cluster queries by intent — informational, commercial-investigation, transactional, navigational — using search-console query data and manual review of top-ranking results for the target query, not volume alone.
2. Map existing site coverage against the intent clusters: what already ranks, what is thin or outdated, what is entirely absent.
3. Assess commercial relevance: does satisfying this intent connect to the primary business outcome, or does it only add traffic with no path to the outcome `$marketing-intake` recorded.
4. Assess competitive feasibility honestly — domain authority gap, content depth of top-ranking pages, and whether the business has a genuine expertise or data advantage to offer beyond what already ranks.
5. Size the content or architecture plan to actual production capacity; state the plan in units of work (pages, page types, structural changes) with an estimate of the capacity each requires.
6. Prioritize by expected business impact, competitive feasibility, and capacity cost — not by search volume rank alone.

## Information architecture

Content and architecture decisions are linked: a topic cluster's internal-linking structure signals topical relationship to search engines and affects how link equity flows. Evaluate whether the site's navigation and internal linking reflect the actual topic hierarchy, and whether high-priority pages are reachable in few clicks from high-authority pages.

## Rules

- Do not recommend content solely because a keyword has volume; require an intent match and a coverage gap.
- "Helpful content" is evaluated by whether it satisfies the query intent better than current top results, not by length, keyword density, or a subjective quality label.
- Do not propose a content set that exceeds stated production capacity; a phased plan sized to actual capacity is more useful than an unexecutable comprehensive one.
- Content consolidation (merging thin or duplicate pages) is a legitimate recommendation and often higher-leverage than new content; do not default to "create more" when "consolidate what exists" better fits the evidence.
- Do not claim a content change caused a ranking or traffic improvement without following the ranking-change diagnosis method; content and technical changes are frequently concurrent, and correlation with one is not proof against the other.

## Source: `.agents/skills/seo/references/ranking-change-diagnosis.md`

# Ranking Change Diagnosis

Organic search has no experimental holdout in the way `$tracking-measurement` can design one for paid media — a page either ranks or does not, for everyone. Causal claims here rest on ruling out competing explanations, not on a controlled test, and should be graded accordingly on the causal evidence ladder (rarely above C2 for a single-site observation).

## Competing explanations to rule out, in order

1. **Algorithm update.** Check documented update timing against `PLATFORM-CURRENCY.md` and the change's date. A broad-core or targeted update affecting the page's category is the most common alternative explanation and must be checked first.
2. **Seasonality.** Compare against the same period in prior years, not only the immediately preceding period; organic search has strong annual patterns in many categories.
3. **Competitive entry or exit.** Check whether a competitor newly ranks or a previously ranking competitor dropped out, which can move position independent of anything the business did.
4. **Technical regression.** Check for an unrelated deploy, robots.txt change, redirect, or canonical change around the same date — including changes made by another team not aware of the SEO impact.
5. **Measurement change.** Check for a search-console property change, a tracking-code update, or a change in how a query is categorized before concluding traffic itself changed.
6. Only after the above are checked and ruled out or explicitly could not be ruled out: attribute the change, provisionally, to the specific content or technical action taken, and state the remaining uncertainty.

## Method

1. Restate the change precisely: which queries, pages, or page groups; ranking position, click-through rate, or traffic; absolute and relative magnitude; exact date range.
2. Check each competing explanation above against the same date range, in order, before considering the specific action a cause.
3. Where multiple concurrent changes exist (a content update and a technical deploy in the same week), state that isolation was not possible and do not select the more convenient explanation.
4. Report the surviving hypothesis with its evidence level, not as a confirmed cause, and state what evidence — typically a comparable, later, isolated change — would raise confidence.

## Rules

- Do not attribute a ranking change to a specific action without checking every competing explanation in order; a partial check is not a completed diagnosis.
- An algorithm update ruled in is not further explainable — do not speculate about the update's specific mechanism beyond what is officially documented; label anything beyond that as inference per `PLATFORM-CURRENCY.md`.
- Multiple concurrent changes with no way to isolate them is itself the correct finding; do not force a single-cause narrative onto ambiguous evidence.
- A single instance of a ranking change following an action is C1 at best (correlation, no control). Do not describe it in language that implies a higher evidence level.

## Source: `.agents/skills/seo/references/technical-health.md`

# Technical Health

Crawlability, indexation, and page experience form the floor organic visibility depends on. A page with perfect content and zero technical health does not rank; diagnose technical health before recommending content work on a site with unresolved technical defects.

## Crawlability and indexation

Check robots.txt exclusions, canonical tags, noindex directives, and XML sitemap coverage against what is actually intended to rank. Compare indexed page count (search-console) against the site's actual page inventory (crawl) — a large gap in either direction is a defect, not a data quirk.

Check for crawl budget waste: faceted-navigation URL explosion, parameter duplication, and thin or near-duplicate pages competing with the canonical version for the same query.

## Canonicalization and duplication

Verify canonical tags point to the intended version and are not contradicted by internal links, sitemaps, or redirect chains. Duplicate or near-duplicate content across URLs (parameter variants, print versions, staging leakage, cross-domain syndication) dilutes ranking signal; identify the intended canonical and consolidate signal toward it.

## Page experience

Core Web Vitals, mobile usability, and interstitial or layout-shift issues affect ranking eligibility and user behavior independently. Report field data (real user measurement) over lab data alone where both are available; lab data can pass while field data fails under real network and device conditions.

## Structured data

Verify structured data validates and matches visible page content; mismatched or unsupported markup can trigger a manual action rather than a ranking benefit. Structured data earns eligibility for a rich result; it does not independently raise ranking.

## Rules

- Do not recommend a technical fix without confirming it will not break an unrelated dependency — a canonical change, redirect, or robots directive can deindex pages that were working correctly.
- A large redirect migration, robots.txt change, or sitemap overhaul is a live change requiring the same authorization and rollback discipline as any other production change: exact scope, expected effect, downside, and stop condition.
- Do not treat a page-experience score improvement as a ranking guarantee; report it as a page-experience improvement with a separately measured ranking effect, if any.
- Distinguish a crawl-budget problem (real pages not being crawled often enough) from an indexation problem (crawled pages not being indexed) — they have different causes and different fixes.
