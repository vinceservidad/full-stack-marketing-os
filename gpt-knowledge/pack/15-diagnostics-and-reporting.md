<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Performance Diagnostics and Reporting

## Skill: $performance-diagnostics

**Use when:** Diagnose why marketing revenue, profit, conversions, spend, or lead quality changed by decomposing metrics and testing competing explanations; use for anomalies and cross-channel questions.

Classify each decomposition, pattern, hypothesis, model, tactic, or test plan with `KNOWLEDGE-TAXONOMY.md`. A pattern or correlation remains a hypothesis until evidence supports the mechanism.

### Method

1. Restate the anomaly with metric definition, absolute values, baseline, date range, scope, and business significance.
2. Validate timezone, attribution, lag, currency, duplicate/missing events, freshness, and denominator changes.
3. Decompose the relevant identity:
   - Ecommerce revenue = traffic × conversion rate × AOV.
   - From gross sales: contribution profit after media = gross sales − discounts − refunds − COGS − variable fulfillment − payment fees − media spend.
   - From net revenue already reflecting discounts/refunds: contribution profit after media = net revenue − COGS − variable fulfillment − payment fees − media spend.
   - Lead value = leads × qualification rate × close rate × realized value.
   - Ad spend = impressions / 1,000 × CPM; conversions = impressions × CTR × post-click conversion rate.
4. Localize the break by channel, campaign, product/service, geography, device, audience, creative, page, and time.
5. Maintain competing hypotheses across measurement, demand, auction, delivery, creative, offer, site, inventory, operations, and mix.
6. Seek disconfirming evidence and rank causes by evidence strength and estimated contribution.

### Rules

- Correlation and timing are clues, not proof.
- Do not compare periods with different promotions, weekday mix, attribution maturity, or inventory without adjustment.
- Separate observed fact, inference, and recommended test.
- Never use “profit” without naming the level and included costs. Never subtract discounts or refunds twice.
- When changes overlap, propose the cheapest reversible data cut or test that distinguishes them.
- Escalate verified checkout, tracking, disapproval, stock, or destination failures while preserving an evidence trail.

### Output

Return: anomaly; data-integrity status; decomposition; confirmed findings; ranked hypotheses with supporting and contradicting evidence; estimated impact where possible; next checks; safe containment; exact status and confidence.


### Library references

Owned root artifacts, read when their scope applies:

- cross-channel-diagnostic.md — cross-channel diagnostic workflow.
- audit.md — evidence-graded audit format.

### QA

Reconcile totals, keep definitions and windows consistent, account for lag and mix, show arithmetic, avoid double-counting, and do not call the issue resolved until the source of truth recovers or the root cause is verified.

## Skill: $marketing-reporting

**Use when:** Build a cross-channel executive report, recurring reporting cadence, or stakeholder scorecard by combining findings already owned by other skills; not for producing the underlying channel audit, diagnosis, or economics analysis itself.

Classify each report with `KNOWLEDGE-TAXONOMY.md`. A report is a communication artifact. It carries the evidence states, profit levels, and exact status of the analysis it summarizes — it does not create new evidence and does not upgrade any finding's state by restating it.

This skill does not perform channel audits, diagnosis, tracking reconciliation, incrementality testing, or economics modeling. Per `CAPABILITY-REGISTRY.md`, a bounded single-channel or single-decision report stays owned by the skill that owns that decision — `$google-ads`, `$meta-ads`, `$cro`, `$tracking-measurement`, `$optimization-scaling`, `$retention-economics`. This skill owns what those individually cannot: combining their outputs across channels, and the recurring cadence that keeps a report trustworthy over time.

### Context

Reporting audience and decision they need to make; cadence (one-time, weekly, monthly, quarterly); channels and skills whose findings are being combined; the primary business outcome and its profit level per `$marketing-intake`; the period and comparison; and whether this report authorizes any action or is read-only.

### Method

1. Confirm each combined finding still carries its original evidence state, source skill, and exact status. Do not flatten a `provisional` finding and a `verified` one into equal-weight bullets.
2. Build the scorecard at the correct profit level and revenue basis, named once and applied consistently across every channel shown. See Scorecard construction.
3. Separate confirmed drivers from hypotheses, and quantify contribution only where the underlying skill actually quantified it — do not infer a magnitude the source analysis did not state.
4. When channels disagree or overlap (platform attribution summed across two platforms, a channel's contribution unclear against another's), route the reconciliation question to `$tracking-measurement`; do not resolve it inside the report by picking the more favorable number.
5. State the single most decision-relevant action, its owner, its evidence, and its current authorization state — never described as implemented unless `$marketing-intake`'s authorization register confirms it.
6. For a recurring report, apply cadence and governance: what triggers a mid-cycle update, what stays fixed period to period, and how a definition change is disclosed rather than silently changing the trend line.
7. For a stakeholder audience without channel-level context, translate without misrepresenting — see Stakeholder communication.

### Library references

Owned root artifacts, read when their scope applies:

- performance-report.md — canonical report format this skill produces.
- reporting-analysis.md — data-to-decision workflow sequence.

### Rules

- Never re-derive a finding this skill is not qualified to produce; route to the owning skill instead of guessing at a diagnosis, audit, or economics conclusion.
- Never sum platform-attributed conversions or revenue across channels to produce a combined total; that is `$tracking-measurement`'s reconciliation question, not a reporting arithmetic step.
- Do not smooth a period-over-period comparison by silently changing a metric definition, date range, or attribution window; disclose the change and show both bases if the trend depends on it.
- Do not upgrade an evidence state by restating a finding in report language. A `documented` claim from a source skill remains `documented` here.
- Do not describe a recommendation as implemented, and do not describe an implemented change as verified before its observation window closes, per `$marketing-intake`'s authorization register.
- Preserve the unknowns a source skill flagged; do not drop them for a cleaner narrative.
- A forecast or trend line is an input for planning, not a guarantee; label it as such per the causal evidence ladder.

### Output

Return: audience and decision; cadence; combined scorecard with profit level and revenue basis named; drivers separated from hypotheses with source skill cited; single most decision-relevant action with owner, evidence, and authorization state; unresolved cross-channel disagreements routed to their owner; unknowns carried forward from source skills; exact status.

### QA

Confirm every combined finding retains its source skill and original evidence state; no cross-platform total was produced by summing attribution; profit level and revenue basis are named once and applied consistently; no recommendation is described as implemented without a confirmed authorization state; and any metric-definition change between periods is disclosed rather than smoothed over.

### Reference: cadence and governance ($marketing-reporting)

### Cadence and Governance

Governs what makes a *recurring* report trustworthy across many editions, which a one-time report does not need to solve: consistent definitions over time, and a disclosed process for when they must change.

#### Set at first publication, then hold fixed

Report cadence (weekly, monthly, quarterly); the primary business outcome and its profit level; the comparison convention (prior period, prior year, both); the channels and skills included; and the scorecard's metric definitions.

Changing any of these mid-series breaks the trend line's comparability. If a change is necessary — a tracking migration, a new profit-level agreement, a channel added — disclose it explicitly in the edition where it happens, and show the metric under both the old and new definition for at least one transition period so the trend is not silently discontinuous.

#### Mid-cycle triggers

A recurring report's fixed cadence does not override a decision-relevant event. Publish an out-of-cycle update when: a tracking defect is confirmed that changes a previously reported figure's evidence state; a guardrail defined in `optimization-scaling` or `retention-economics` is breached; or a reforecast from `budget-and-outcome-pacing` materially changes the period's expected outcome.

#### Revision discipline

If a past edition's figure is later corrected — a tracking fix reconciles a number, a modeled figure is replaced by a realized one — record the revision in the current edition rather than silently editing history. State what changed, why, and which edition it corrects.

#### Rules

- Do not add a new channel or metric to a recurring report without noting the addition in that edition; a scorecard that silently grows makes prior editions non-comparable.
- Do not drop a metric that turned unfavorable without disclosing the removal; that reads as concealment even when unintentional.
- A cadence exists to prevent noise from being read as trend; do not shorten it reactively because a single period looked bad.

### Reference: scorecard construction ($marketing-reporting)

### Scorecard Construction

Builds the comparable, decision-grade table a cross-channel report is built around. The scorecard is where mismatched definitions most often slip into a report unnoticed — one channel's "conversion" is not another's.

#### Method

1. Name the primary business outcome once, at the profit level and revenue basis `$marketing-intake` recorded, and use it consistently for every channel and every period shown.
2. For each row: current value, comparison value, absolute delta, relative delta, target (if one exists), and the exact metric definition — source system, counting rule, attribution window.
3. Where a channel's native metric differs from the business outcome (platform ROAS versus contribution margin, lead volume versus qualified pipeline), show both, labeled, rather than presenting the platform metric as the outcome.
4. Mark each row's evidence state per the intake evidence ladder — `observed`, `reconciled`, `verified` — visibly, not only in a footnote a reader will skip.
5. Where a period comparison is invalid per `$marketing-intake`'s comparability check (definition changed, promotion overlapped, incomplete period), mark the row rather than showing a misleading delta.

#### Rules

- One profit level and one revenue basis per scorecard. Switching mid-table to make a number look better is a definitional violation, not a formatting choice.
- Do not compute a blended or portfolio-level total by summing rows whose underlying definitions differ; reconcile first or show the components unsummed.
- A target without a stated source (business plan, prior period, industry reference) is not a target — label it as an unverified benchmark or omit it.
- Do not backfill a missing comparison period with an estimate; mark it unavailable.
- Currency and timezone must match across every row in a single scorecard; state the conversion basis if they do not natively.

### Reference: stakeholder communication ($marketing-reporting)

### Stakeholder Communication

Translates a channel-level or technical finding for an audience without that context, without letting the translation misrepresent what the underlying analysis actually supports.

#### Method

1. Lead with the business decision, not the channel mechanism. State what changed in commercial terms before explaining why in platform terms.
2. Preserve the evidence state in plain language: "confirmed by [source]" for `verified`/`reconciled`, "likely, based on [source]" for `observed`/`documented`, "a working theory, not yet confirmed" for `asserted`. Do not collapse these into one confident tone.
3. Translate platform jargon to the glossary term the stakeholder actually cares about — "the primary business outcome," not "the Primary conversion action" — while keeping the precise term available in a footnote or appendix for anyone who needs it.
4. State the recommended action and its authorization state in one sentence a non-specialist can act on: what is being asked of them, and what happens if they approve it.

#### Rules

- Do not simplify a caveat into confidence. If the source analysis called a result provisional, the stakeholder version says so — in plainer words, not stronger ones.
- Do not present a forecast, model output, or platform recommendation as a guarantee because the audience does not read causal-ladder labels; translate the label into a sentence, do not delete it.
- Do not omit a named risk or unknown because it complicates the narrative; a shorter caveat is acceptable, a missing one is not.
- Do not use a stakeholder summary to imply approval was requested and granted when `$marketing-intake`'s authorization register shows otherwise.
