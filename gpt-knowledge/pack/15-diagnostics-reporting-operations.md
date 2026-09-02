<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Diagnostics, Reporting, and Operations

## Skill: $performance-diagnostics

**Use when:** Diagnose why marketing revenue, profit, conversions, spend, or lead quality changed by decomposing metrics and testing competing explanations; use for anomalies and cross-channel questions.

Classify each decomposition, pattern, hypothesis, model, tactic, or test plan with `KNOWLEDGE-TAXONOMY.md`. A pattern or correlation remains a hypothesis until evidence supports the mechanism.

### Required inputs

For the anomaly being diagnosed, collect or explicitly mark missing:

- the changed business/marketing metric, its exact definition, absolute values, baseline/comparison, date range, timezone, and scope
- source systems and freshness for spend, traffic, conversions, revenue, profit, lead quality, or other relevant outcomes
- attribution/window/lag state and any known tracking, tagging, deduplication, currency, tax, refund, or denominator changes
- useful breakdowns such as channel, campaign, product/service, geography, device, audience, creative, landing page, customer type, and time
- economics needed to interpret the change, including the named profit level and included costs when profitability is in scope
- material business/marketing changes during the period: budgets, bids, targeting, creative, offer, price, promotion, site, inventory, fulfillment, policy, seasonality, or external demand shifts
- the decision or business significance the diagnosis must support, including any urgent containment need
- authorization boundary if the request extends from diagnosis into a live mutation

Do not fill missing history, attribution settings, economics, or change events with invented assumptions. State which missing input could reverse the diagnosis.

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

**Use when:** Build a cross-channel executive report, recurring reporting cadence, or stakeholder scorecard by combining findings already owned by other skills; not for producing the underlying channel audit, diagnosis, economics analysis, or recurring operational loop itself.

Classify each report with `KNOWLEDGE-TAXONOMY.md`. A report is a communication artifact. It carries the evidence states, profit levels, and exact status of the analysis it summarizes — it does not create new evidence and does not upgrade any finding's state by restating it.

This skill does not perform channel audits, diagnosis, tracking reconciliation, incrementality testing, economics modeling, or cross-skill operational automation. Per `CAPABILITY-REGISTRY.md`, a bounded single-channel or single-decision report stays owned by the skill that owns that decision — `$google-ads`, `$meta-ads`, `$cro`, `$tracking-measurement`, `$optimization-scaling`, `$retention-economics`. This skill owns what those individually cannot: combining their outputs across channels, and the recurring cadence that keeps a report trustworthy over time. `$marketing-operations` owns recurring decision operations, state/checkpoints, approval gates, execution handoffs, and escalation when the recurring process does more than communicate findings.

### Context

Reporting audience and decision they need to make; cadence (one-time, weekly, monthly, quarterly); channels and skills whose findings are being combined; the primary business outcome and its profit level per `$marketing-intake`; the period and comparison; and whether this report authorizes any action or is read-only.

### Method

1. Confirm each combined finding still carries its original evidence state, source skill, and exact status. Do not flatten a `provisional` finding and a `verified` one into equal-weight bullets.
2. Build the scorecard at the correct profit level and revenue basis, named once and applied consistently across every channel shown. See Scorecard construction.
3. Separate confirmed drivers from hypotheses, and quantify contribution only where the underlying skill actually quantified it — do not infer a magnitude the source analysis did not state.
4. When channels disagree or overlap (platform attribution summed across two platforms, a channel's contribution unclear against another's), route the reconciliation question to `$tracking-measurement`; do not resolve it inside the report by picking the more favorable number.
5. State the single most decision-relevant action, its owner, its evidence, and its current authorization state — never described as implemented unless `$marketing-intake`'s authorization register confirms it.
6. For a recurring report, apply cadence and governance: what triggers a mid-cycle update, what stays fixed period to period, and how a definition change is disclosed rather than silently changing the trend line.
7. If the recurring process also monitors conditions, coordinates several specialist decisions, manages durable state, requests approvals, or hands off live actions, route that operating-loop layer to `$marketing-operations` while this skill continues to own the report artifact.
8. For a stakeholder audience without channel-level context, translate without misrepresenting — see Stakeholder communication.

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
- A recurring report cadence is not automatically an operational loop. If the process requires cross-skill decision orchestration, persistent run state, mutating actions, approval reuse, duplicate prevention, or condition-triggered escalation, `$marketing-operations` owns that layer.

### Output

Return: audience and decision; cadence; combined scorecard with profit level and revenue basis named; drivers separated from hypotheses with source skill cited; single most decision-relevant action with owner, evidence, and authorization state; unresolved cross-channel disagreements routed to their owner; unknowns carried forward from source skills; exact status.

### QA

Confirm every combined finding retains its source skill and original evidence state; no cross-platform total was produced by summing attribution; profit level and revenue basis are named once and applied consistently; no recommendation is described as implemented without a confirmed authorization state; any metric-definition change between periods is disclosed rather than smoothed over; and any recurring decision-operation layer has been routed to `$marketing-operations` rather than hidden inside reporting.

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

## Skill: $marketing-operations

**Use when:** Design and govern recurring marketing operating loops that coordinate existing Marketing OS skills across cadence or trigger, source checks, state, approval, execution handoff, verification, escalation, and learning; not for stealing specialist decisions or implying an unscheduled process is already running.

Marketing Operations turns one-off governed decisions into repeatable operating loops. It owns the loop contract and cross-skill coordination. It does not own the underlying channel, research, measurement, offer, CRO, reporting, or scaling decision.

Classify loop artifacts with `KNOWLEDGE-TAXONOMY.md`. A loop is a process/workflow with explicit state and control boundaries, not proof that recurring activity improves performance.

### Inputs

Before designing a loop, confirm:

- business objective and decision the loop serves
- primary business outcome and relevant guardrails
- cadence, event trigger, or condition that justifies a run
- source systems/artifacts and freshness requirements
- domain decision owner for every substantive step
- authorization boundary for any live mutation
- runtime or tool that can actually schedule/trigger execution, if automation is requested
- stop, pause, escalation, and retirement conditions
- state/checkpoint needed to distinguish new work from already-processed work

Use decision-relevant sections of `.agents/marketing-context.md` when available, without upgrading evidence.

### Method

1. **Define the loop job.** State the recurring decision or operating burden being reduced. A loop without a repeated decision, recurring risk, or meaningful trigger is unnecessary automation.
2. **Choose the trigger model.** Use Loop design and governance to distinguish fixed cadence, event-triggered, condition-watch, and state-change loops. Do not invent a frequency from habit when the decision changes slower or faster than the schedule.
3. **Map the owner chain.** Appoint one loop owner and name each domain skill that owns a substantive decision. Marketing Operations coordinates; the domain skill decides.
4. **Specify source and freshness gates.** State which inputs must be checked on every run, which can be cached, and when stale/contradicted context blocks or downgrades the run.
5. **Define state and idempotency.** Use Loop state, idempotency, and escalation. Record the checkpoint/dedupe key needed to prevent reprocessing the same event, repeating the same mutation, or issuing duplicate alerts.
6. **Build the run sequence.** Default shape: `Trigger → Read state → Validate inputs → Route specialist checks → Diagnose/decide → Approval gate if needed → Execute/hand off → Verify → Record state → Record learning → Escalate/stop/continue`.
7. **Separate read-only from mutating steps.** A loop may always produce a read-only recommendation when evidence is sufficient; a live change still requires the authorization owned by `$marketing-intake` and the executing domain skill/runtime.
8. **Define output and notification rules.** State when the loop should emit a report, alert, decision request, or no output. “Nothing changed” should not create noise unless the user explicitly wants heartbeat reporting.
9. **Close the learning loop.** Send valid experiment outcomes to `$tracking-measurement`, reusable context changes to `$marketing-intake`, and specialist learning to the owner that produced it. Do not turn repeated observations into causal proof without valid evidence.
10. **Verify runtime state.** A written loop specification is `designed`, not `scheduled`, `active`, or `running`. Only describe it as scheduled/active when the actual automation/runtime confirms that state.

### Rules

- Do not create a loop merely because a task can recur. Recurrence must reduce a real decision burden, risk, or latency.
- Do not replace domain ownership with a generic operations decision. Google Ads still owns Google Ads decisions; CRO still owns CRO decisions; `$tracking-measurement` still owns experiment validity; `$optimization-scaling` still owns scaling.
- Do not let a recurring report become a hidden decision engine. `$marketing-reporting` owns recurring communication; `$marketing-operations` owns recurring operational coordination.
- Do not imply background execution, monitoring, or scheduling exists unless an actual runtime/tool has been configured and verified.
- Do not use a loop to bypass approval. A prior approval must state its scope, allowed action, limits, and expiry before a mutating run can rely on it.
- Do not repeat a live mutation when state cannot prove whether it already happened. Stop or escalate instead.
- Do not fire repeated alerts for the same unchanged condition unless the notification policy explicitly requires reminders.
- Do not overwrite prior state to make the current run look clean. Preserve run history, skipped runs, failures, invalid data, and unresolved contradictions.
- Do not turn an arbitrary daily/weekly/monthly cadence into a best practice. Match cadence to decision latency, data lag, operational cost, and risk.
- Do not call a loop successful because it ran. Judge it by whether it produced timely, valid, correctly authorized decisions with acceptable operational cost and error rate.
- A loop spec is not a task scheduler, webhook, cron job, or agent runtime. Those are implementation mechanisms and must be verified separately.

### Output

Return: loop objective; trigger/cadence; scope; primary business outcome and guardrails; loop owner; domain owners; source/freshness gates; state/checkpoint; idempotency rule; run sequence; approval boundary; execution handoff; verification step; output/notification rule; escalation/stop/retirement conditions; learning handoff; runtime requirement; exact status.

### Library references

- Marketing operations loop — canonical recurring operating sequence.
- Marketing loop template — reusable loop contract.
- Loop design and governance — trigger, cadence, ownership, and lifecycle rules.
- Loop state, idempotency, and escalation — safe repeated execution and duplicate-prevention rules.

### Related owners

- `$marketing-router`: chooses the smallest useful set of specialists for each run.
- `$marketing-intake`: evidence state, shared context, authorization register.
- `$marketing-reporting`: recurring communication and stakeholder scorecards.
- `$tracking-measurement`: experiment validity and reusable experiment learning.
- `$optimization-scaling`: scaling/de-scaling decisions and pacing inside approved plans.
- domain/channel skills: own the substantive decision and live implementation in their scope.

### QA

Confirm the loop solves a real recurring decision; trigger/cadence is justified; each substantive decision has a domain owner; sources and freshness gates are explicit; state prevents duplicate processing; mutating steps have an approval gate; repeated alerts are controlled; stop/escalation/retirement conditions exist; learning has an owner; and the exact status does not imply scheduling or background execution that has not been verified.

### Reference: loop design and governance ($marketing-operations)

### Loop Design and Governance

Use this reference to decide whether recurring work should exist at all, what should trigger it, and how ownership stays clear across repeated runs.

#### When a loop is justified

A recurring loop should reduce at least one real operating burden:

- repeated decision work with stable inputs and rules
- meaningful delay between a change occurring and someone noticing it
- recurring quality-control or compliance risk
- repeated reconciliation or review that must preserve definitions over time
- a condition that should trigger a bounded response when it changes
- a learning cycle where prior results should inform the next run

Do not automate a task merely because it is repetitive if the decision itself is rare, highly bespoke, or cheaper to handle manually.

#### Trigger models

##### Fixed cadence

Run at a defined interval when the decision is inherently periodic, such as a weekly account review or monthly cohort review.

Choose cadence from:

- how quickly the underlying state can meaningfully change
- data/reporting lag
- minimum sample needed for a valid decision
- operational risk of waiting
- cost of reviewing too often

A daily cadence is not automatically more responsive; it can create noisy reversals when the metric needs a longer window.

##### Event-triggered

Run after a specific verified event, such as:

- campaign launched
- experiment completed
- product price changed
- landing page published
- tracking configuration changed

The event must have a dedupe key or durable identifier so the same event is not processed repeatedly.

##### Condition-watch

Run checks on a schedule but emit/escalate only when a defined condition becomes true. The condition must specify:

- metric/state evaluated
- evidence source
- threshold or logical rule
- minimum persistence/window if needed
- reset/re-arm behavior
- alert dedupe rule

Do not use a volatile single-point threshold where a persistence rule is required to avoid false alerts.

##### State-change

Run when an entity moves from one verified state to another, such as `approved → live`, `processing → verified`, or `healthy → degraded`.

Do not infer a state transition merely because time passed. Confirm it from the source system.

#### Loop ownership

Separate three roles:

1. **Loop owner** — owns the recurring process contract, state, cadence/trigger, handoffs, and run history. Usually `$marketing-operations`.
2. **Decision owner** — owns the substantive decision for a step. This remains the relevant domain skill.
3. **Execution/runtime owner** — system, user, or authorized integration that actually schedules, mutates, or sends output.

These can be different. A loop can be well-designed while not yet having a runtime capable of executing it.

#### Run classes

##### Read-only review loop

Collects evidence, invokes specialists, records findings, and produces an output. No live mutation.

##### Decision loop

Produces a decision or recommendation at each run. If execution is not authorized, the run ends at `proposed` or `approval required`.

##### Mutating loop

May make a bounded live change only when all of these are explicit:

- allowed mutation class
- exact scope/entities
- hard limits
- approval source and expiry
- rollback/stop rule
- post-change verification
- durable state proving what was changed

If any are missing, downgrade to a decision loop.

#### Cadence governance

Every loop needs:

- normal cadence or trigger
- earliest useful next run
- maximum acceptable delay
- blackout/quiet windows when relevant
- trigger priority if several conditions occur together
- backoff behavior after failure
- retirement review

Do not let the schedule become independent of the decision. If the signal is only decision-ready monthly, a daily decision loop should not manufacture daily actions.

#### Lifecycle states

Use exact status language:

- `designed` — specification exists
- `approved-to-configure` — configuration authorized, not yet confirmed
- `configured` — runtime/schedule exists but execution not yet verified
- `active-verified` — at least one expected run was observed successfully
- `paused` — configured but intentionally prevented from running or acting
- `degraded` — runtime works incompletely or required inputs are unavailable
- `retired` — intentionally ended; no further runs expected

Do not use `active` or `running` merely because a file or schedule definition exists.

#### Loop health

Judge the loop itself on operational quality, not marketing vanity metrics:

- eligible runs completed
- stale/invalid-input runs correctly blocked
- duplicate actions prevented
- authorization failures correctly stopped
- false/duplicate alerts
- median detection-to-decision latency
- execution verification rate
- unresolved escalations
- operator effort/cost

Business performance remains owned by the domain skills; loop health measures whether the operating mechanism is trustworthy.

#### Minimum governance record

For every governed loop, preserve:

- loop ID/version
- objective
- owner
- trigger/cadence
- sources and freshness limits
- state/checkpoint
- specialist routing map
- authorization boundary
- execution mechanism if any
- output/notification rule
- stop/escalation/retirement rules
- last successful run
- last failed/skipped run and why
- change log

### Reference: loop state idempotency and escalation ($marketing-operations)

### Loop State, Idempotency, and Escalation

Repeated work becomes unsafe when the system cannot tell what already happened. Use this reference for durable state, duplicate prevention, retries, approvals, and escalation.

#### State model

At minimum, persist enough state to answer:

- what entity/event/window this run is processing
- last successful checkpoint
- last attempted checkpoint
- inputs/source versions used
- decision produced
- approval state and scope
- mutation attempted or completed
- verification result
- alert/output emitted
- unresolved failure or escalation

State should be durable enough that a retry can resume safely rather than guessing.

#### Idempotency

An idempotent run can be retried without causing an unintended second effect.

For each mutating or notifying step define a dedupe key, for example:

`loop_id + entity_id + decision_window + action_type + approved_change_version`

The exact shape depends on the system, but it must distinguish a genuinely new action from a retry of the same action.

##### Before a mutation

Check:

1. Has this action/version already been applied?
2. Is the prior result verified, unknown, failed, or still processing?
3. Is the current approval still valid for this exact action?
4. Did any decision-relevant input change since approval?

If state is ambiguous, do not repeat the mutation. Verify or escalate.

##### Before a notification

Check:

- has this condition already been reported?
- has the condition materially changed?
- has the reset/re-arm rule been met?
- is a reminder interval explicitly configured?

Suppress duplicate alerts by default.

#### Retry behavior

Separate retryable failures from decision failures.

Retryable examples:

- temporary source timeout
- transient API/service error
- runtime interruption before mutation was attempted

Do not blindly retry:

- unknown mutation state
- expired approval
- contradicted inputs
- measurement integrity failure
- guardrail breach
- source schema/definition change

Use bounded retries and backoff where the runtime supports them. Escalate when the failure type cannot be safely retried.

#### Approval scope

A reusable approval must state:

- loop/action it covers
- entity scope
- allowed mutation types
- quantitative limits where relevant
- valid period or expiry
- stop/rollback conditions
- who/what granted approval

Approval for one run is not automatically approval for future runs. Approval for a budget pacing correction is not approval for scaling beyond the authorized plan.

#### Verification

Never equate an API success or saved state with business verification.

Use staged status where relevant:

`proposed → approved → submitted/saved → live/processing → observed → verified`

Post-action verification should confirm the source system reflects the intended change and, when necessary, that the downstream effect can be measured. Marketing performance verification may require a later observation window owned by the relevant specialist.

#### Escalation classes

##### Data escalation

Trigger when:

- source unavailable beyond allowed delay
- metric definition changed
- data contradicts the current context
- measurement integrity is unresolved

Route to `$marketing-intake`, `$tracking-measurement`, or the source owner as appropriate.

##### Decision escalation

Trigger when:

- evidence falls below the required threshold
- several specialists disagree on a decision-relevant premise
- a new condition falls outside the loop's approved rules
- the decision would expand scope beyond the loop contract

End the automated path at a human/specialist decision request rather than improvising.

##### Authorization escalation

Trigger when:

- approval missing, expired, ambiguous, or narrower than the proposed action
- a mutating step has no rollback/stop rule
- current conditions differ materially from those approved

Do not act.

##### Safety/commercial escalation

Trigger when:

- business guardrail breached
- spend/revenue risk exceeds approved bound
- customer/legal/compliance risk appears
- repeated failures suggest the loop itself is unsafe

Pause the mutating path until the owning specialist resolves the issue.

#### Stop and retirement

A loop needs explicit conditions that stop normal runs or end the loop entirely.

Possible stop conditions:

- source becomes invalid
- operating assumption is contradicted
- threshold is breached
- authorized action limit reached
- runtime repeatedly fails
- required specialist is unavailable

Possible retirement conditions:

- business objective no longer exists
- campaign/product/channel is retired
- the decision moved into another governed process
- marginal value of the loop no longer exceeds operating cost
- the condition is no longer expected to recur

Retirement should preserve history rather than deleting evidence of prior runs.

#### Failure-safe rule

When the system cannot establish whether a live action already occurred, prefer verification/escalation over repetition. Duplicate live mutations can be more damaging than a delayed action.
