---
name: affiliate-marketing
description: Manage or evaluate affiliate and partner programs — commission structure, attribution integrity, fraud and brand-bidding detection, and network versus direct-partner decisions; not for influencer relationship vetting, and not for the underlying paid-search brand-protection enforcement.
---

# Affiliate Marketing

Classify each commission model, attribution method, or fraud-detection heuristic with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). This is a performance-based, publisher-network channel: the defining risk is not creative or targeting quality but attribution integrity — whether the commission paid actually reflects incremental value the affiliate created, and whether the tracked conversion was legitimately earned.

Related but distinct: `$influencer-marketing` covers vetting an individual creator relationship and its compensation; this skill covers a publisher/partner network paying commission on tracked conversions, where fraud and attribution-gaming risk is structurally higher because the incentive is directly tied to the tracked action.

## Context

Primary business outcome and commission budget or acceptable cost-of-sale ceiling; program structure under consideration (in-house direct partners, third-party affiliate network, or both); attribution window and cookie/tracking method in use; current partner mix (content/review sites, coupon/deal sites, comparison sites, loyalty/cashback sites, sub-affiliate networks); and whether the business's branded search terms are being bid on by any partner.

## Method

1. Confirm the attribution mechanism (cookie duration, last-click versus another model, cross-device handling) and its known integrity gaps before evaluating any commission report; a broken or gameable attribution mechanism invalidates the payout logic built on top of it. See [Attribution integrity](references/attribution-integrity.md).
2. Screen the partner mix for the specific fraud and gaming patterns common to this channel — brand bidding, cookie stuffing, coupon-code leakage, incentivized or fake traffic. See [Fraud and brand-bidding detection](references/fraud-and-brand-bidding-detection.md).
3. Structure commission to reward genuinely incremental value: differentiate content/influence partners from coupon/loyalty partners whose typical role is capturing a conversion already in motion rather than creating it, and do not pay both the same rate for structurally different contribution.
4. Assess whether direct partnership or a third-party network fits the program's scale and oversight capacity; a network provides reach and infrastructure but adds a layer between the business and partner behavior, including sub-affiliates the business may never directly vet.
5. Confirm disclosure compliance for affiliate links per current requirements, consistent with `$influencer-marketing`'s disclosure discipline where a partner is also a content creator.
6. Rank program changes by expected business impact, confidence, reversibility, and the oversight capacity actually available to monitor partner behavior on an ongoing basis.

## Rules

- Do not treat a tracked affiliate conversion as automatically incremental; a last-click attribution model routinely credits a coupon or cashback partner for a sale the customer was already going to complete, and a commission-structure decision should reflect that risk rather than assume every tracked conversion was caused by the affiliate.
- Do not allow a partner to bid on the business's own branded search terms without an explicit, monitored policy; unrestricted brand bidding by affiliates typically captures spend the business would have received directly at zero incremental cost, and frequently raises the business's own paid-search costs by adding a competing bidder on its own brand.
- Do not accept a sudden spike in a partner's conversion volume as a positive signal without checking for cookie-stuffing or other attribution-gaming patterns; an unexplained spike is a fraud-screening trigger, not a reason to increase that partner's commission.
- Do not pay identical commission rates to structurally different partner types (a content partner that genuinely influences a purchase decision versus a coupon-code partner that intercepts an already-decided purchase) without deliberately deciding that is the intended structure; the default should be evaluated, not assumed.
- Do not onboard a sub-affiliate network's full downstream partner list without a stated oversight or audit mechanism; a business is typically still responsible for its overall program's compliance and fraud exposure even when a sub-affiliate's specific behavior was not directly visible.
- Route a causal or incrementality claim about the program's overall contribution to `$tracking-measurement`; this skill screens for attribution-integrity defects at the partner level, it does not itself establish the program's incremental business value.

## Output

Program review: attribution mechanism and known integrity gaps; partner mix by type; fraud/brand-bidding screening findings; commission structure and its incentive alignment; network versus direct-partner assessment; disclosure compliance status; oversight capacity; recommended actions; exact status.

Partner-level flag: partner identity; observed anomaly or gaming pattern; evidence; recommended action (monitor, restrict, suspend, terminate); confidence.

## QA

Confirm the attribution mechanism's integrity gaps are stated before any commission conclusion; brand-bidding policy is explicit and monitored; a conversion-volume spike triggers fraud screening before a commission increase; commission structure differentiates partner types deliberately rather than by default; sub-affiliate exposure is acknowledged with a stated oversight mechanism; and any incrementality claim about the program is routed to `$tracking-measurement` rather than asserted here.
