---
name: linkedin-ads
description: Plan, audit, or diagnose LinkedIn B2B advertising — account-based and firmographic targeting, format selection, Lead Gen Forms, and cost-structure economics; not for consumer/demographic-targeted channels, and not for the underlying sales-cycle or CRM ownership.
---

# LinkedIn Ads

Classify each model, targeting decision, or economics claim with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). LinkedIn's targeting unit is frequently the buying account or the buying committee, not the individual consumer — a fundamentally different targeting logic than Meta, TikTok, or YouTube, and one that should be built from `$icp-jtbd` evidence about buying situations and buyer roles, not demographic proxies.

## Context

Primary business outcome and lead-stage definitions per `$marketing-intake`, since LinkedIn's cost per click and cost per lead run materially higher than consumer platforms and a cost conclusion is meaningless without the qualified-lead or pipeline economics behind it; target account list or firmographic criteria if account-based marketing is in use; buyer roles and buying-committee structure per `$icp-jtbd`; available formats (Sponsored Content, Message/Conversation Ads, Lead Gen Forms, Text/Dynamic Ads) and creative fit for each; and sales-cycle length, since a lead generated today frequently will not show revenue for months.

## Method

1. Establish whether targeting is account-based (a defined target account list, matched via account targeting) or attribute-based (job title, seniority, function, industry, company size) — state which and why; see [Account and firmographic targeting](references/account-and-firmographic-targeting.md).
2. Select ad format to fit the funnel stage and buying-committee role being reached; a Message/Conversation Ad to a senior decision-maker and a Lead Gen Form to a research-stage individual contributor are different mechanisms for different roles, not interchangeable defaults.
3. Assess Lead Gen Forms (native, pre-filled, lower-friction) against an off-platform landing page (higher friction, potentially higher intent signal) for the specific offer; the friction/quality tradeoff is a real decision, not a default.
4. Set cost expectations against the account's own economics, not a consumer-platform benchmark; LinkedIn's cost per click and cost per lead are structurally higher, and evaluating them against a Meta or Google benchmark produces a false efficiency conclusion.
5. Define the measurement plan against the actual sales cycle: lead volume and immediate cost-per-lead are early, weak signals; route to `$retention-economics`'s lead-to-revenue cohort method for a maturity-honest read, and do not treat an early cohort's incomplete pipeline as a final quality verdict. See [Lead quality and sales cycle](references/lead-quality-and-sales-cycle.md) for format- and role-segmented quality discipline.
6. Rank actions by expected pipeline impact, confidence, reversibility, and the account's actual budget tolerance for this channel's cost structure.

## Rules

- Do not evaluate LinkedIn cost-per-click or cost-per-lead against a consumer-platform benchmark; the platforms serve structurally different audiences and buying contexts, and the comparison produces a false conclusion about efficiency.
- Do not treat lead volume as the business outcome; for a long sales cycle, immediate lead metrics are a weak, early signal and a business-outcome conclusion requires the lead-to-revenue cohort maturity check `$retention-economics` provides.
- Do not build attribute-based targeting from an assumed persona when `$icp-jtbd` has actual buying-committee and buyer-role evidence available; use the evidence.
- Do not treat every buyer role identically; a campaign reaching only one role in a multi-stakeholder buying committee is reaching part of the decision, and the plan should state which role or roles it targets and which it does not.
- Do not claim account-based targeting reached a target account without confirming the platform's actual match rate for that account list; a low match rate means the campaign is reaching a different, broader audience than the plan states.
- Do not conflate Lead Gen Form volume with off-platform landing-page volume when comparing cost per lead; the two carry different friction and typically different downstream qualification rates, and a raw comparison without that context misleads.

## Output

Plan: targeting approach (account-based or attribute-based) with rationale; format selection matched to buying-committee role and funnel stage; Lead Gen Form versus landing-page decision; cost expectations against this account's own economics; measurement plan matched to sales-cycle length; capacity required; exact status.

Diagnosis: observed change; competing explanations (targeting-match-rate shift, format change, seasonality tied to B2B budget cycles, sales-cycle-stage immaturity misread as a decline) considered before attributing a cause; evidence level; recommended action.

## QA

Confirm targeting approach and its rationale are stated; format matches the buying-committee role and funnel stage rather than defaulting to one format; cost conclusions are checked against this account's own economics rather than a consumer-platform benchmark; lead-quality claims route through `$retention-economics`'s maturity-honest cohort method rather than asserting a final read on an immature cohort; and account-based match rate is confirmed rather than assumed.
