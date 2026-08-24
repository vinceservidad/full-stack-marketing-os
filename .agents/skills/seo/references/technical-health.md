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
