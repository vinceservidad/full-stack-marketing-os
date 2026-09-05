<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Google Ads

Source paths identify the bundled repository documents. Local links are
rendered as source labels; external URLs and fenced examples are preserved.

## Source: `.agents/skills/google-ads/SKILL.md`

---
name: google-ads
description: Audit, diagnose, or plan Google Ads Search, Shopping, and Performance Max work using business outcomes and query or product evidence; not for unsupported live changes.
---

# Google Ads

Covers Search, Shopping, and Performance Max structure, bidding, and account mechanics. YouTube video advertising is a distinct discipline with different attention economics, format constraints, and measurement norms — route to `$youtube-ads` for format selection, video-specific targeting, and view-through measurement fit; this skill covers the shared Google Ads account and bidding layer YouTube campaigns also run through.

Classify each audit, model, methodology, process, tactic, technique, best practice, or heuristic with `KNOWLEDGE-TAXONOMY.md` (source: `KNOWLEDGE-TAXONOMY.md`). Name the primary type and keep platform evidence separate from recommendations.

## Context

Collect business goal, account and market scope, date range and comparison, budget, bidding strategy, campaign type, conversion goals, conversion actions, action-optimization status, revenue or qualified-lead definition, and available exports. For ecommerce profitability, request price, COGS, variable fulfillment, payment fees, discounts, refunds, revenue basis, and feed status.

## Method

1. Verify conversion goals, their included conversion actions, each action's Primary/Secondary status, campaign goal selection, counting, values, attribution windows, consent gaps, and agreement with the business source of truth. A Primary action influences bidding only when the campaign uses its containing goal.
2. Decompose demand and eligibility → auctions and spend → clicks → site behavior → conversions → revenue, margin, or lead quality.
3. Inspect the correct unit:
   - Search: queries, match type, intent, ad relevance, landing alignment, geography, device, and schedule.
   - Shopping/PMax: item ID, product type, price, feed quality, availability, asset-group segmentation, and available channel-mix evidence.
4. Compare like-for-like periods and separate volume, efficiency, mix, and measurement effects.
5. Rank actions by expected business impact, confidence, reversibility, and learning value.

For substantial mode-specific work, read only the relevant reference: Search (source: `.agents/skills/google-ads/references/search.md`), Shopping (source: `.agents/skills/google-ads/references/shopping.md`), or Performance Max (source: `.agents/skills/google-ads/references/pmax.md`). For current AI, automation, control, reporting, or interface claims, read Platform Registry (source: `.agents/skills/google-ads/references/platform-current.md`) and apply the root `PLATFORM-CURRENCY.md` freshness gate.

## Rules

- Never add a negative solely because a query did not convert in a small sample; consider intent, spend against allowable CPA, assisted value, and protected brand/product coverage.
- Do not increase budgets while measurement integrity or unit economics are unknown.
- Avoid structural rebuilds when the issue is isolated to measurement, feed eligibility, landing experience, or a small set of queries/items.
- Do not infer unseen PMax channel allocation.
- Use profit or qualified-lead economics when available. Label ROAS/CPA conclusions provisional otherwise.
- Use “conversion goal” for the Google Ads grouping and “conversion action” for the measured action. Do not call the main commercial result a Primary conversion action; call it the primary business outcome.
- Do not claim an undocumented “Google algorithm change.” Separate officially documented capability, account-visible behavior, experimentally observed impact, inference, and unknowns. Confirm account availability before recommending a current control.

## Output

Audit: scope; measurement status; findings with evidence, impact, and confidence; protected coverage; prioritized actions; tests; unknowns.

Change plan: exact entity; current and proposed state; rationale; risk; rollback/stop rule; approval required.


## Library references

Owned root artifacts, read when their scope applies:

- google-ads-full-stack.md (source: `frameworks/google-ads-full-stack.md`) — full-account decision model beyond a single audit or diagnosis.
- google-ads-audit.md (source: `playbooks/google-ads-audit.md`) — step-by-step audit workflow.
- google-ads-optimization.md (source: `workflows/google-ads-optimization.md`) — recurring optimization cadence.
- campaign-brief.md (source: `templates/campaign-brief.md`) — campaign brief format, shared with $meta-ads.

## QA

Check date and attribution consistency, conversion scope, sample size, query/item evidence, margin or lead-quality caveats, preservation of valuable coverage, platform-registry freshness, and account-visible availability for current controls.

## Source: `.agents/skills/google-ads/references/platform-current.md`

# Google Ads Platform Registry

**Last verified:** 2026-08-22  
**Freshness class:** High-change; recheck within 30 days or whenever current behavior affects a decision.

Read this reference for current Google Ads AI, automation, controls, reporting, or interface terminology. Apply the root `PLATFORM-CURRENCY.md` contract.

## Current mappings

| Stable concept | Current official product label or capability | Verified scope |
|---|---|---|
| Search automation layer | **AI Max for Search campaigns** | An optimization layer inside eligible Search campaigns, not a separate campaign type. Its documented core features include search term matching and asset optimization. |
| Automated text adaptation | **Text customization** | Google documents this as the current name for the capability formerly called automatically created assets within AI Max. |
| Dynamic landing-page selection | **Final URL expansion** | A documented asset-optimization feature; dependencies and URL controls must be checked in the current account. |
| Cross-inventory automated campaign | **Performance Max** | Campaign type using Google inventory and automated optimization toward configured conversion goals. |
| PMax channel visibility | **Channel performance report** | Google documents campaign-level channel and ad-format reporting. Confirm account availability and metric scope before claiming visibility. |
| PMax query exclusion | **Performance Max campaign negative keywords** | Google documents campaign- and account-level negative-keyword controls for Search and Shopping inventory. Brand exclusions remain a separate control. |

## First-party sources

- [Set up AI Max for Search campaigns](https://support.google.com/google-ads/answer/15909989?hl=en) — product type, settings, dependencies, and setup.
- [How AI Max for Search campaigns works](https://support.google.com/google-ads/answer/15910187?hl=en) — feature composition and renamed controls.
- [About AI Max experiments](https://support.google.com/google-ads/answer/16450159?hl=en) — controlled trial capability and limitations.
- [About the channel performance report for Performance Max](https://support.google.com/google-ads/answer/16260130?hl=en) — documented channel-reporting scope.
- [Negative keywords in Performance Max campaigns](https://support.google.com/google-ads/answer/15726455?hl=en) — campaign/account control and inventory scope.
- [Search targeting and controls for Performance Max](https://support.google.com/google-ads/answer/16672776) — current control family.

## Watchlist

Reverify AI Max defaults and eligibility, feature dependencies, DSA migration timelines, PMax reporting columns and availability, negative-keyword limits/scope, search-theme behavior, brand controls, conversion-goal behavior, bidding strategies, attribution options, and policy/consent requirements.

Do not convert Google product claims into expected client impact. Confirm the current account, measurement integrity, economics, and a reversible test design.

## Source: `.agents/skills/google-ads/references/pmax.md`

# Performance Max

Use for PMax diagnosis or architecture.

## Inspect

- Conversion-goal and value integrity before automated bidding conclusions
- Shopping-only (commonly “feed-only”) versus asset-supported scope, asset groups, listing groups, search themes, audience signals, Final URL expansion within asset optimization, text customization, and brand controls
- Product/item results, asset evidence, placement or category evidence when available, and overlap with Search/Shopping
- Budget sufficiency, learning maturity, seasonality, promotions, inventory, and value rules

## Decisions

Do not infer channel allocation, incrementality, or query coverage that the available reporting does not reveal. Avoid splitting asset groups without a distinct product, message, landing, market, or operational hypothesis. Brand exclusions and URL controls can protect intent, but assess coverage loss before applying them.

## Source: `.agents/skills/google-ads/references/search.md`

# Google Search

Use for query-led Search campaign audits or plans.

## Inspect

- Search demand and seasonality versus account delivery
- Query intent, match type, keyword/ad-group mapping, and close variants
- Eligibility, impression share components, auction cost, and budget constraint
- Ad promise, asset coverage, and query-to-landing message scent
- Geography, device, schedule, audience observation, and partner/network scope
- Query-level conversion quality, profit, and protected brand or strategic terms

## Decisions

Add negatives only with adequate intent and economic evidence; distinguish exact exclusion from broader blocking risk. Consolidate when fragmentation prevents learning, but preserve materially different intent, economics, geography, or landing experience. Treat ad strength and quality diagnostics as clues, not business outcomes.

## Source: `.agents/skills/google-ads/references/shopping.md`

# Google Shopping

Use for Standard Shopping or product-level commerce analysis.

## Inspect

- Merchant eligibility, policy status, destinations, and country/feed scope
- Item ID continuity, title, product type, Google category, GTIN/brand, image, price, availability, shipping, and promotions
- Product-level spend, clicks, conversion value, margin, refunds, and stock
- Query/product fit, price competitiveness, landing consistency, and variant handling
- Campaign priority or listing-group logic where applicable

## Decisions

Do not interpret issue-record counts as unique affected products without confirming scope. Protect commercially important item coverage while fixing source data. Segment products only when economics, intent, inventory, or control requirements differ enough to justify it.
