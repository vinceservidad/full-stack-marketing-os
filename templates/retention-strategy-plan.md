# Retention Strategy Plan

Owner: `$retention-strategy`

Use this artifact for a retention, save, recovery, repeat-purchase, renewal, lapse-prevention, or win-back decision. Preserve evidence state and exact implementation status.

## Decision State

- Business / scope:
- Decision type: active retention | save | involuntary recovery | repeat purchase | renewal | lapse prevention | win-back
- Status: draft | proposed | approved | configured | live | observed | verified | retired
- Decision owner:
- Implementation owner(s):
- Last updated:
- Source-of-truth systems:
- Authorization record:

## Retention Definition

- Continuation behavior:
- Eligible population:
- Segment / cohort:
- Observation window:
- Retention / churn / repeat definition:
- Revenue basis / profit level:
- Current pricing/package state:
- Activation state/definition when relevant:

## Observed State

- Current state: active | at risk | voluntary cancel | involuntary loss | dormant/lapsed | recovered | won back
- Baseline rate/count:
- Cohort maturity:
- Data quality / instrumentation state:
- Recent material changes:

## Reason Evidence

| Evidence layer | Finding | Source | Evidence state | Coverage / limit |
|---|---|---|---|---|
| Customer-stated reason |  |  |  |  |
| Observed behavior |  |  |  |  |
| Operational fact |  |  |  |  |
| Commercial fact |  |  |  |  |
| Model inference |  |  |  |  |

### Leading diagnosis

- Reason family:
- Voluntary / involuntary / lapse:
- Confidence:
- Competing explanation(s):
- Evidence needed to discriminate:
- Root-cause owner:

## Intervention Hypothesis

- Intervention:
- Mechanism hypothesis:
- Why it matches the diagnosed reason:
- Who is eligible:
- Who is excluded / suppressed:
- Customer choice / cancellation implications:
- Commercial cost:
- Product/service/operations dependency:
- Pricing dependency:
- Activation dependency:
- Lifecycle communication dependency:

## Communication Handoff

Owned by `$lifecycle-marketing` when communication is required.

- Trigger/state:
- Segment:
- Consent basis:
- Suppression conditions:
- Cadence constraint:
- Copy need for `$copywriting`:

## Test / Validation

Owned validity method: `$tracking-measurement` where causal evidence is required.

- Population:
- Control / comparison:
- Treatment:
- Primary business outcome:
- Supporting metrics:
- Observation window / lag:
- Guardrails:
- Stop conditions:
- Sample/power constraint:
- Confounding / contamination risk:
- Decision rule:

## Economics

Use `$retention-economics` for realized cohort economics and `$pricing-monetization` for commercial-term changes.

- Incremental or realized revenue basis:
- Contribution / profit level:
- Incentive / discount cost:
- Support/service cost:
- Payment-recovery cost:
- Margin risk:
- Expected downstream behavior to verify:

## Durable Save / Recovery Verification

A short-term acceptance is not automatically durable retention.

- Save/recovery accepted:
- Paid/qualified status restored:
- Continued through required window:
- Next renewal/reorder observed:
- Contribution acceptable:
- Refund/cancellation acceptable:
- Complaint/support burden acceptable:
- Discount dependency acceptable:
- Root cause resolved:
- Exact verification status:

## Learning Record

- Result: supports | contradicts | inconclusive/null | guardrail harm | invalid/compromised
- Observed effect:
- Mechanism interpretation:
- Evidence level:
- Scope where learning applies:
- Contradictory evidence:
- Replication / follow-up:
- Marketing Context update needed:

## Approval and Rollback

- Exact external mutation:
- Approved by:
- Approval scope:
- Approval expiry:
- Rollback / stop trigger:
- Customer remediation if needed:

## QA

- Retention behavior and window defined before analysis.
- State is not confused with reason.
- Voluntary and involuntary loss are separated.
- Customer-stated reason is not promoted to causal fact.
- Intervention addresses the diagnosed reason.
- Cancellation and communication rights remain intact.
- Discounts include contribution and downstream-behavior guardrails.
- Product/service defects route to their actual owner.
- A short-term save is not called durable retention prematurely.
- No external change is implied without authorization and verified state.
