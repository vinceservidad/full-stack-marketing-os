---
name: marketing-operations
description: Design and govern recurring marketing operating loops that coordinate existing Marketing OS skills across cadence or trigger, source checks, state, approval, execution handoff, verification, escalation, and learning; not for stealing specialist decisions, choosing the strategic portfolio, or implying an unscheduled process is already running.
---

# Marketing Operations

Marketing Operations turns one-off governed decisions into repeatable operating loops. It owns the loop contract and cross-skill coordination. It does not own the underlying growth strategy, channel, research, measurement, offer, CRO, reporting, or scaling decision.

Classify loop artifacts with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). A loop is a process/workflow with explicit state and control boundaries, not proof that recurring activity improves performance.

## Inputs

Before designing a loop, confirm:

- business objective and decision the loop serves
- current strategic priority from `$growth-strategy` when the loop exists to operate a governed growth plan
- primary business outcome and relevant guardrails
- cadence, event trigger, or condition that justifies a run
- source systems/artifacts and freshness requirements
- domain decision owner for every substantive step
- authorization boundary for any live mutation
- runtime or tool that can actually schedule/trigger execution, if automation is requested
- stop, pause, escalation, and retirement conditions
- state/checkpoint needed to distinguish new work from already-processed work

Use decision-relevant sections of `.agents/marketing-context.md` when available, without upgrading evidence.

## Method

1. **Define the loop job.** State the recurring decision or operating burden being reduced. A loop without a repeated decision, recurring risk, or meaningful trigger is unnecessary automation.
2. **Choose the trigger model.** Use [Loop design and governance](references/loop-design-and-governance.md) to distinguish fixed cadence, event-triggered, condition-watch, and state-change loops. Do not invent a frequency from habit when the decision changes slower or faster than the schedule.
3. **Map the owner chain.** Appoint one loop owner and name each domain skill that owns a substantive decision. Marketing Operations coordinates; the domain skill decides. If the loop exists because of a growth plan, `$growth-strategy` still owns whether that initiative remains strategically prioritized.
4. **Specify source and freshness gates.** State which inputs must be checked on every run, which can be cached, and when stale/contradicted context blocks or downgrades the run.
5. **Define state and idempotency.** Use [Loop state, idempotency, and escalation](references/loop-state-idempotency-and-escalation.md). Record the checkpoint/dedupe key needed to prevent reprocessing the same event, repeating the same mutation, or issuing duplicate alerts.
6. **Build the run sequence.** Default shape: `Trigger → Read state → Validate inputs → Route specialist checks → Diagnose/decide → Approval gate if needed → Execute/hand off → Verify → Record state → Record learning → Escalate/stop/continue`.
7. **Separate read-only from mutating steps.** A loop may always produce a read-only recommendation when evidence is sufficient; a live change still requires the authorization owned by `$marketing-intake` and the executing domain skill/runtime.
8. **Define output and notification rules.** State when the loop should emit a report, alert, decision request, or no output. “Nothing changed” should not create noise unless the user explicitly wants heartbeat reporting.
9. **Close the learning loop.** Send valid experiment outcomes to `$tracking-measurement`, reusable context changes to `$marketing-intake`, specialist learning to the owner that produced it, and material priority-changing evidence to `$growth-strategy`. Do not turn repeated observations into causal proof without valid evidence.
10. **Verify runtime state.** A written loop specification is `designed`, not `scheduled`, `active`, or `running`. Only describe it as scheduled/active when the actual automation/runtime confirms that state.

## Rules

- Do not create a loop merely because a task can recur. Recurrence must reduce a real decision burden, risk, or latency.
- Do not replace domain ownership with a generic operations decision. `$growth-strategy` still owns strategic portfolio priority; Google Ads still owns Google Ads decisions; CRO still owns CRO decisions; `$tracking-measurement` still owns experiment validity; `$optimization-scaling` still owns scaling.
- Do not let a recurring plan review become a hidden strategy engine. Marketing Operations may trigger and coordinate the review; `$growth-strategy` owns strategic rebalancing.
- Do not let a recurring report become a hidden decision engine. `$marketing-reporting` owns recurring communication; `$marketing-operations` owns recurring operational coordination.
- Do not imply background execution, monitoring, or scheduling exists unless an actual runtime/tool has been configured and verified.
- Do not use a loop to bypass approval. A prior approval must state its scope, allowed action, limits, and expiry before a mutating run can rely on it.
- Do not repeat a live mutation when state cannot prove whether it already happened. Stop or escalate instead.
- Do not fire repeated alerts for the same unchanged condition unless the notification policy explicitly requires reminders.
- Do not overwrite prior state to make the current run look clean. Preserve run history, skipped runs, failures, invalid data, and unresolved contradictions.
- Do not turn an arbitrary daily/weekly/monthly cadence into a best practice. Match cadence to decision latency, data lag, operational cost, and risk.
- Do not call a loop successful because it ran. Judge it by whether it produced timely, valid, correctly authorized decisions with acceptable operational cost and error rate.
- A loop spec is not a task scheduler, webhook, cron job, or agent runtime. Those are implementation mechanisms and must be verified separately.

## Output

Return: loop objective; strategic-plan dependency when relevant; trigger/cadence; scope; primary business outcome and guardrails; loop owner; domain owners; source/freshness gates; state/checkpoint; idempotency rule; run sequence; approval boundary; execution handoff; verification step; output/notification rule; escalation/stop/retirement conditions; learning handoff; runtime requirement; exact status.

## Library references

- [Marketing operations loop](../../../workflows/marketing-operations-loop.md) — canonical recurring operating sequence.
- [Marketing loop template](../../../templates/marketing-loop.md) — reusable loop contract.
- [Loop design and governance](references/loop-design-and-governance.md) — trigger, cadence, ownership, and lifecycle rules.
- [Loop state, idempotency, and escalation](references/loop-state-idempotency-and-escalation.md) — safe repeated execution and duplicate-prevention rules.

## Related owners

- `$growth-strategy`: strategic portfolio, initiative priority, sequencing, and plan review/rebalancing.
- `$marketing-router`: chooses the smallest useful set of specialists for each run.
- `$marketing-intake`: evidence state, shared context, authorization register.
- `$marketing-reporting`: recurring communication and stakeholder scorecards.
- `$tracking-measurement`: experiment validity and reusable experiment learning.
- `$optimization-scaling`: scaling/de-scaling decisions and pacing inside approved plans.
- domain/channel skills: own the substantive decision and live implementation in their scope.

## QA

Confirm the loop solves a real recurring decision; any strategic priority comes from `$growth-strategy` rather than the loop itself; trigger/cadence is justified; each substantive decision has a domain owner; sources and freshness gates are explicit; state prevents duplicate processing; mutating steps have an approval gate; repeated alerts are controlled; stop/escalation/retirement conditions exist; learning has an owner; and the exact status does not imply scheduling or background execution that has not been verified.
