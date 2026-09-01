---
name: marketing-intake
description: Capture and grade the evidence, metric definitions, access, authorization, and reusable project context behind a marketing engagement before substantial audit, diagnosis, planning, or scaling work; use when scope, data provenance, economics, shared context, or approval boundaries are unclear.
---

# Marketing Intake

Record what was actually received, from whom, in what state. Intake does not establish that a claim is true — it establishes what is known, how it is known, and what would reverse the conclusion.

Classify the resulting artifact with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). An intake record is a process artifact and evidence ledger, never proof of an outcome.

## Context

Required before intake can complete: business model, primary business outcome, account and market scope, date range and comparison period, currency, reporting timezone, data sources supplied, access available, and the system treated as the business source of truth.

Required before any profitability, scaling, or lead-quality conclusion: cost and profit definitions with named profit level, cost of goods sold, discounts, refunds, fulfillment and payment costs, and — for lead generation — lifecycle stage definitions and Customer Relationship Management outcomes.

When structured platform, analytics, commerce, or economics data is supplied, apply [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) and the relevant contract under [`data-contracts/`](../../../data-contracts/). Preserve the raw source, record normalization/field lineage, and use [`templates/data-intake-manifest.md`](../../../templates/data-intake-manifest.md) for substantial multi-dataset work.

Intake may proceed with gaps. It may not present a gap as satisfied.

## Method

1. Record engagement context and scope. Separate what the user asserted from what a source system shows. See [Engagement context](references/engagement-context.md).
2. Enter every decision-relevant claim in the evidence register with its source, collection method, and evidence state. See [Evidence register](references/evidence-register.md).
3. When structured datasets are supplied, create a data-intake record: source, period, timezone, currency, grain, primary key, attribution/conversion/revenue/profit basis, field lineage, limitations, and dataset validity state. Preserve raw and normalized layers separately. `$tracking-measurement` owns reconciliation/measurement validity when the decision depends on cross-source agreement, event integrity, or attribution semantics.
4. Define every metric and lifecycle term before any comparison. Platform labels are not definitions. See [Metric definitions](references/metric-definition-register.md).
5. Record conversion architecture: Google Ads conversion goals, their included conversion actions and Primary or Secondary status; Meta objective, conversion location, performance goal, dataset, and event. Record attribution settings, windows, conversion lag, and known tracking defects.
6. Record capacity — inventory, fulfillment, creative, sales, and service — wherever a recommendation could exceed it.
7. Request only the missing evidence that could change a decision, ranked by decision impact. See [Access and data request](references/access-and-data-request.md).
8. Record the authorization boundary before proposing any change. See [Authorization register](references/authorization-register.md).
9. State which decisions the current evidence can and cannot support, and name the gaps capable of reversing each one.
10. When the project needs reusable cross-skill context, create or update `.agents/marketing-context.md` from [`templates/marketing-context.md`](../../../templates/marketing-context.md) using [Marketing Context governance](references/marketing-context-governance.md). Preserve provenance, evidence state, contradictions, freshness, and the change log; do not copy unnecessary raw data into it.

## Rules

- Never upgrade an evidence state. A user-reported figure remains user-reported until observed in a named source; an observed figure remains unverified until reconciled with the business source of truth.
- Never fill a gap with a benchmark, an assumed margin, a typical conversion rate, or a platform default. Record it as unknown.
- Do not treat platform attribution as the business outcome, and do not reconcile platforms by addition.
- Do not compare periods, accounts, channels, or datasets before their metric definitions, grain, date/time basis, and currency are recorded and confirmed compatible.
- A dataset is validated **for a named decision scope**, not universally. Intake can mark completeness/mapping state; `$tracking-measurement` owns measurement/reconciliation validity when required.
- Keep `0`, unknown/null, not applicable, not reported, and source-withheld values distinct. Do not turn missing rows into zeros without source support.
- Preserve raw source files/results. Normalization is a derived layer with field lineage, not a replacement for provenance.
- Do not request personal data that no decision requires. Record research provenance without exposing identifying detail. Quotations require a traceable supplied source. For cohort linkage, prefer pseudonymous stable identifiers where possible.
- Absence of a supplied cost structure blocks a profitability conclusion; it does not block analysis labeled as efficiency-only.
- Intake authorizes nothing. Recording an approval is not receiving one, and no intake output or validated dataset may imply a live change.
- Do not declare intake complete while a gap capable of reversing the primary decision is open. Declare it partial and name the gap.
- Marketing Context is a reusable summary, not evidence promotion. A statement copied into `.agents/marketing-context.md` keeps the source evidence state and specialist owner.
- Do not make every task load the entire Marketing Context. Downstream work should use only decision-relevant sections.

## Output

Intake record: engagement context; primary business outcome; scope and period; source-of-truth system; evidence register with states; metric and conversion definitions; capacity constraints; authorization boundary; ranked outstanding requests; decisions currently supportable; decisions blocked and what would unblock them; exact status.

Data Intake Manifest when structured data is material: dataset register; contract/version; source and scope; grain/key; date/time/currency; attribution/conversion/revenue/profit basis; field lineage; quality/reconciliation status; privacy restrictions; validity for the named decision; allowed/prohibited uses; handoff owner.

Marketing Context when useful: versioned `.agents/marketing-context.md` containing only reusable decision context, source/evidence state, freshness, contradictions, open decisions, and change history.

Access request: named source, specific artifact or export, date range, reason it is decision-changing, and what remains blocked without it.

## Library references

- [`DATA-CONTRACTS.md`](../../../DATA-CONTRACTS.md) — canonical structured-data provenance, grain, semantics, privacy, and validity contract.
- [`data-contracts/validation.md`](../../../data-contracts/validation.md) — data profiling, mapping, reconciliation, and decision-validity method.
- [`templates/data-intake-manifest.md`](../../../templates/data-intake-manifest.md) — reusable multi-dataset intake record.
- [`templates/marketing-context.md`](../../../templates/marketing-context.md) — reusable structure for project-level shared Marketing Context.
- [Marketing Context governance](references/marketing-context-governance.md) — creation, update, freshness, contradiction, and ownership rules.

## QA

Confirm every decision-relevant claim carries a source and evidence state; no state was upgraded without a named source; no gap was filled by assumption; structured datasets preserve raw provenance, grain, keys, date/time, currency, field lineage, and decision-validity state; missingness is not silently converted to zero; metric definitions precede comparisons; conversion goal and action language follows the glossary; personal data is minimal and provenance is traceable; the authorization boundary is explicit; blocked decisions are listed rather than answered; and any Marketing Context update preserves source, evidence state, contradictions, freshness, and version history.
