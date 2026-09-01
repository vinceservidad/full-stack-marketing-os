---
name: marketing-reporting
description: Build a cross-channel executive report, recurring reporting cadence, or stakeholder scorecard by combining findings already owned by other skills; not for producing the underlying channel audit, diagnosis, economics analysis, or recurring operational loop itself.
---

# Marketing Reporting

Classify each report with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A report is a communication artifact. It carries the evidence states, profit levels, and exact status of the analysis it summarizes — it does not create new evidence and does not upgrade any finding's state by restating it.

This skill does not perform channel audits, diagnosis, tracking reconciliation, incrementality testing, economics modeling, or cross-skill operational automation. Per [`CAPABILITY-REGISTRY.md`](../../../CAPABILITY-REGISTRY.md), a bounded single-channel or single-decision report stays owned by the skill that owns that decision — `$google-ads`, `$meta-ads`, `$cro`, `$tracking-measurement`, `$optimization-scaling`, `$retention-economics`. This skill owns what those individually cannot: combining their outputs across channels, and the recurring cadence that keeps a report trustworthy over time. `$marketing-operations` owns recurring decision operations, state/checkpoints, approval gates, execution handoffs, and escalation when the recurring process does more than communicate findings.

## Context

Reporting audience and decision they need to make; cadence (one-time, weekly, monthly, quarterly); channels and skills whose findings are being combined; the primary business outcome and its profit level per `$marketing-intake`; the period and comparison; and whether this report authorizes any action or is read-only.

## Method

1. Confirm each combined finding still carries its original evidence state, source skill, and exact status. Do not flatten a `provisional` finding and a `verified` one into equal-weight bullets.
2. Build the scorecard at the correct profit level and revenue basis, named once and applied consistently across every channel shown. See [Scorecard construction](references/scorecard-construction.md).
3. Separate confirmed drivers from hypotheses, and quantify contribution only where the underlying skill actually quantified it — do not infer a magnitude the source analysis did not state.
4. When channels disagree or overlap (platform attribution summed across two platforms, a channel's contribution unclear against another's), route the reconciliation question to `$tracking-measurement`; do not resolve it inside the report by picking the more favorable number.
5. State the single most decision-relevant action, its owner, its evidence, and its current authorization state — never described as implemented unless `$marketing-intake`'s authorization register confirms it.
6. For a recurring report, apply [cadence and governance](references/cadence-and-governance.md): what triggers a mid-cycle update, what stays fixed period to period, and how a definition change is disclosed rather than silently changing the trend line.
7. If the recurring process also monitors conditions, coordinates several specialist decisions, manages durable state, requests approvals, or hands off live actions, route that operating-loop layer to `$marketing-operations` while this skill continues to own the report artifact.
8. For a stakeholder audience without channel-level context, translate without misrepresenting — see [Stakeholder communication](references/stakeholder-communication.md).

## Library references

Owned root artifacts, read when their scope applies:

- [performance-report.md](../../../templates/performance-report.md) — canonical report format this skill produces.
- [reporting-analysis.md](../../../workflows/reporting-analysis.md) — data-to-decision workflow sequence.

## Rules

- Never re-derive a finding this skill is not qualified to produce; route to the owning skill instead of guessing at a diagnosis, audit, or economics conclusion.
- Never sum platform-attributed conversions or revenue across channels to produce a combined total; that is `$tracking-measurement`'s reconciliation question, not a reporting arithmetic step.
- Do not smooth a period-over-period comparison by silently changing a metric definition, date range, or attribution window; disclose the change and show both bases if the trend depends on it.
- Do not upgrade an evidence state by restating a finding in report language. A `documented` claim from a source skill remains `documented` here.
- Do not describe a recommendation as implemented, and do not describe an implemented change as verified before its observation window closes, per `$marketing-intake`'s authorization register.
- Preserve the unknowns a source skill flagged; do not drop them for a cleaner narrative.
- A forecast or trend line is an input for planning, not a guarantee; label it as such per the causal evidence ladder.
- A recurring report cadence is not automatically an operational loop. If the process requires cross-skill decision orchestration, persistent run state, mutating actions, approval reuse, duplicate prevention, or condition-triggered escalation, `$marketing-operations` owns that layer.

## Output

Return: audience and decision; cadence; combined scorecard with profit level and revenue basis named; drivers separated from hypotheses with source skill cited; single most decision-relevant action with owner, evidence, and authorization state; unresolved cross-channel disagreements routed to their owner; unknowns carried forward from source skills; exact status.

## QA

Confirm every combined finding retains its source skill and original evidence state; no cross-platform total was produced by summing attribution; profit level and revenue basis are named once and applied consistently; no recommendation is described as implemented without a confirmed authorization state; any metric-definition change between periods is disclosed rather than smoothed over; and any recurring decision-operation layer has been routed to `$marketing-operations` rather than hidden inside reporting.
