# Marketing Context

Shared decision context for the Marketing OS.

Owner: `$marketing-intake`.

This artifact reduces repeated intake across skills. It is a curated context layer, not a replacement for source evidence, the evidence register, or specialist analysis. Every decision-relevant statement must preserve its source and evidence state. Unknowns remain unknown; contradictions remain visible.

## Document State

- Context version:
- Last updated:
- Scope / business:
- Status: draft | partial | current | stale
- Source-of-truth system(s):
- Evidence register:
- Known freshness limits:

## Business and Goals

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Business model |  |  |  |
| Primary business outcome |  |  |  |
| Market / geography |  |  |  |
| Time horizon |  |  |  |
| Strategic constraints |  |  |  |

## Product Truth and Claim Boundaries

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Product / service |  |  |  |
| Core use case |  |  |  |
| Verified capabilities |  |  |  |
| Claim boundaries |  |  |  |
| Known limitations |  |  |  |

## Market, Segment, and JTBD

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Category / market frame |  |  |  |
| Priority segment |  |  |  |
| Secondary / experimental segment |  |  |  |
| Buying situation |  |  |  |
| JTBD / desired progress |  |  |  |
| Buyer / user roles |  |  |  |
| Exclusions / poor-fit segment |  |  |  |

## Customer Evidence and VOC

Record patterns here; keep traceable quotations in the underlying research source.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Pain / friction |  |  |  |
| Desired outcome |  |  |  |
| Trigger moments |  |  |  |
| Objections / anxieties |  |  |  |
| Selection criteria |  |  |  |
| Repeated language / themes |  |  |  |
| Contradictions / segment differences |  |  |  |

## Positioning and Differentiation

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Positioning hypothesis / decision |  |  |  |
| Differentiators |  |  |  |
| Reason to believe |  |  |  |
| Alternatives / status quo |  |  |  |
| Competitor implications |  |  |  |

## Current Offer

This section records the current offer state. `$offer-strategy` owns diagnosis or redesign of the proposition itself.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Core deliverable |  |  |  |
| Promised outcome |  |  |  |
| Offer components / bundle |  |  |  |
| Risk reversal |  |  |  |
| Real urgency / scarcity |  |  |  |

## Current Pricing and Monetization

This section records the current commercial exchange state. `$pricing-monetization` owns pricing architecture and price-change decisions. Preserve exact state: proposed, approved, configured, live, observed, or verified.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Base / list price |  |  |  |
| Realized price / discount mix |  |  |  |
| Value metric |  |  |  |
| Packages / tiers |  |  |  |
| Payment model / terms |  |  |  |
| Fees / credits |  |  |  |
| Existing-customer / renewal treatment |  |  |  |
| Commercial state |  |  |  |

## Activation and First Value

Record this section only when a distinct post-conversion activation stage is decision-relevant. `$activation` owns the first meaningful value definition, path-to-value, time-to-value, and activation diagnosis. Do not invent an activation event just to fill the template.

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Conversion boundary |  |  |  |
| Distinct activation stage exists? |  |  |  |
| First meaningful value definition |  |  |  |
| Definition status | hypothesis / provisional / supported / contradicted |  |  |
| Eligible denominator / segment |  |  |  |
| Activation window |  |  |  |
| Activation baseline |  |  |  |
| Time-to-value baseline |  |  |  |
| First binding barrier |  |  |  |
| Instrumentation state |  |  |  |
| Current intervention / test state |  |  |  |

## Proof Inventory

| Proof type | Available evidence | Source | Evidence state | Allowed use / limit |
|---|---|---|---|---|
| Product demonstration |  |  |  |  |
| Customer-reported experience |  |  |  |  |
| Case study / business result |  |  |  |  |
| Independent / third-party proof |  |  |  |  |
| Credentials / authority |  |  |  |  |

## Economics and Commercial Constraints

| Field | Current context | Source | Evidence state |
|---|---|---|---|
| Revenue basis |  |  |  |
| Profit level |  |  |  |
| Margin / variable-cost constraints |  |  |  |
| Refund / cancellation considerations |  |  |  |
| Capacity / inventory / service limits |  |  |  |

## Brand and Message Constraints

- Brand voice:
- Required terminology:
- Prohibited / unsupported claims:
- Legal / compliance constraints:
- Visual / production constraints:

## Channel and Funnel Context

| Channel / surface | Current role | Known constraint | Evidence / source |
|---|---|---|---|
|  |  |  |  |

## Open Decisions and Evidence Gaps

| Open item | Why it matters | Evidence needed | Owner | Status |
|---|---|---|---|---|
|  |  |  |  |  |

## Change Log

Newest first. Preserve prior entries rather than rewriting history.

- vX — YYYY-MM-DD — What changed, why, source or decision that changed it.

## Usage Rules

- Downstream skills read only the sections relevant to their decision; this is not a requirement to load the whole file for every trivial task.
- A context entry inherits the evidence state of its underlying source; summarizing it here never upgrades confidence.
- Customer language is not verbatim VOC unless it remains traceable to the supplied source.
- A model-generated synthesis is labeled synthesis or hypothesis, not customer evidence, willingness-to-pay, or an activation fact.
- A proposed/configured price remains proposed/configured here until the source pricing artifact verifies a later state.
- An activation event remains hypothesis/provisional here until the `$activation` artifact supports a stronger state; onboarding completion or email engagement is not silently promoted to first value.
- Do not silently overwrite a contradiction. Record the competing evidence and the segment, date, or source difference.
- Do not place unnecessary personal data in this artifact.
- When a decision materially changes the context, increment the context version and prepend a change-log entry.
- If a decision-relevant section is stale or contradicted, mark the context partial or stale rather than letting downstream skills treat it as current.
