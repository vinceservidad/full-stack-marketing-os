# Decision Record

**Status:** Synthetic worked example

## Audit flow

```text
Business objective
→ measurement integrity
→ delivery decomposition
→ creative and destination quality
→ audience/structure evidence
→ competing explanations
→ ranked actions
→ controlled test plan
→ scaling handoff only if ready
```

## 1. Do not start with platform ROAS

**Observed:** Meta-attributed revenue is $28,700 while tagged store analytics reports $22,400 from Meta sessions.

**Interpretation:** The sources answer different attribution questions and are not reconciled.

**Decision:** `$tracking-measurement` must reconcile definitions/windows before platform-attributed revenue is used as business truth. The audit can still use Meta entity-level data directionally.

**Do not do:** choose the larger number, sum the two sources, or claim Meta generated $28,700 incrementally.

## 2. Separate prospecting from retargeting

**Observed:** Prospecting platform ROAS is 1.90x; retargeting is 2.50x.

**Interpretation:** Blended 2.05x hides different jobs and audiences. Retargeting can capture demand already created elsewhere and does not prove acquisition strength.

**Decision:** Judge prospecting against new-customer business economics when available. Keep retargeting as a separate decision layer.

**Unknown:** new-customer contribution after media.

## 3. High CTR is not the winner

| Creative | Observed pattern | Interpretation | Decision |
|---|---|---|---|
| C01 | Lower CTR than C02, stronger LPV rate, stronger purchase CVR, lower platform CPA | The message currently produces better downstream quality in this synthetic account | Keep as control; do not pause because CTR is not highest |
| C02 | Highest outbound CTR, weaker LPV rate, weaker post-LPV purchase CVR, higher CPA | Attention is not translating into comparable visit/purchase quality | Diagnose message-to-destination continuity before scaling |
| C03 | Moderate response and purchase quality | Useful alternate angle, not a proven universal winner | Retain as evidence-backed challenger/control candidate |
| C04 | Early results on lower spend | Insufficient evidence for a strong conclusion | Continue only within the approved test plan; do not call it a winner/loser yet |

## 4. Message scent is a plausible C02 mechanism, not a proven cause

**Observed:** C02 promises “what fits inside,” while the first page viewport emphasizes appearance/material.

**Observed:** C02 has a lower landing-page-view/outbound-click rate and lower post-LPV purchase CVR.

**Hypothesis:** The creative attracts capacity/organization intent that the page does not immediately continue.

**Alternative explanations:** slower video-click quality, audience mix, placement mix, mobile experience, accidental/low-intent clicks, delivery differences, or normal variance.

**Decision:** `$cro` can support a bounded message-scent test if page evidence confirms the mismatch. Do not order a full PDP redesign from this observation alone.

## 5. Frequency is a clue, not the diagnosis

**Observed:** Retargeting frequency rose from 6.2 to 8.4 while outbound response and purchase rate fell.

**Inference:** Saturation or creative fatigue is plausible.

**Competing explanations:** audience pool changed, exclusions/eligibility changed, site demand weakened, offer relevance changed, tracking changed, or spend pressure increased faster than audience replenishment.

**Decision:** Inspect audience size/eligibility, delivery, exclusions, creative distribution, and conversion integrity before labeling “fatigue.” If fatigue remains the best-supported explanation, Creative Strategy owns the refresh hypothesis.

## 6. Broad versus interest is confounded

**Observed:** Broad has lower platform CPA ($40 vs $49).

**Observed:** Broad also received more C01 exposure, while interest-based targeting received more C02 exposure.

**Interpretation:** Audience and creative are not isolated.

**Decision:** Do not publish “broad targeting wins.” If audience strategy matters enough to test, rebalance creative exposure or design a cleaner comparison while protecting delivery stability.

## 7. The spend increase may be exposing marginal weakness

**Observed:** Spend increased 25% from $11,200 to $14,000 while platform ROAS fell from 2.42x to 2.05x.

**Calculated:** attributed revenue still increased, but efficiency weakened.

**Unknown:** contribution after media and incremental new-customer value.

**Interpretation:** The account may be moving into weaker marginal inventory/audiences/creative capacity, but platform ROAS alone cannot prove the mechanism or whether the higher spend is commercially bad.

**Decision:** `$optimization-scaling` does not authorize further spend expansion until new-customer economics, measurement confidence, and marginal evidence are adequate.

## 8. Ranked action set

### Priority 1 — Reconcile measurement used for business decisions

Owner: `$tracking-measurement`

- align attribution windows/definitions and revenue basis
- inspect event/deduplication integrity
- identify the business source of truth for realized revenue/contribution
- keep Meta attribution as platform evidence rather than silent ground truth

### Priority 2 — Preserve C01 as a control and diagnose C02 quality loss

Owners: `$meta-ads` + `$creative-strategy`; `$cro` supports if destination mismatch is evidenced.

- keep C01 available as the current local control
- do not select C02 from CTR alone
- test whether the “what fits” concept needs a better destination continuation or a different creative execution

### Priority 3 — Diagnose retargeting saturation before refreshing blindly

Owner: `$meta-ads`

- inspect eligible audience size and delivery concentration
- verify exclusions and customer-state logic
- connect creative IDs to response deterioration
- refresh only after the likely mechanism is stated

### Priority 4 — Deconfound audience conclusions

Owner: `$meta-ads`

- do not make broad-vs-interest a strategic rule from this snapshot
- compare with more balanced creative allocation if the question is decision-relevant
- keep platform automation/broad targeting decisions tied to business outcome and control needs

### Priority 5 — Hold further scaling until evidence improves

Owner: `$optimization-scaling`

- require contribution/new-customer economics
- inspect marginal performance rather than blended average only
- define guardrails and rollback before any approved increase

## 9. Controlled creative test

`$creative-strategy` receives the local evidence and produces strategically distinct cells rather than cosmetic edits.

### Control

**C01 — Retrieval Relief**

Hook: “Stop digging through your bag.”

Reason to keep: strongest current downstream purchase quality in this synthetic snapshot.

### Challenger A — Capacity Clarity

**Angle:** See exactly what your everyday carry can hold without turning into a pile.

**Mechanic:** Direct demonstration.

**Format:** 4:5 static or short demonstration designed around the same capacity promise.

**Destination dependency:** first viewport should continue capacity/organization meaning if that is the tested mechanism.

### Challenger B — Flexible Organization

**Angle:** Organize it your way instead of forcing your routine into fixed compartments.

**Mechanic:** Reconfiguration demonstration.

**Format:** 4:5 static sequence or short video.

This tests a different reason to care, not merely a new hook for C01.

## 10. Pre-specified learning

Primary business outcome should be defined from source-of-truth new-customer economics before a real test.

Useful supporting signals can include:

- landing-page-view quality
- purchase conversion rate
- qualified/new-customer mix
- realized contribution
- refund/return guardrail
- creative spend distribution

CTR is diagnostic support, not the winning criterion.

## Non-priorities

Do **not**:

- rebuild the whole account because performance softened
- duplicate many ad sets to “find winners” without distinct hypotheses
- pause C01 because its CTR is lower than C02
- declare Meta “fatigued” from frequency alone
- declare broad targeting universally superior
- scale because retargeting ROAS looks strong
- blame an undocumented Meta algorithm change
- publish, pause, edit audiences, or change budgets without explicit approval

## Exact status

**Audit and test plan drafted from synthetic evidence. No Meta Ads configuration has been changed, published, paused, scaled, or verified live.**
