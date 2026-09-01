# Worked Example Standard

Worked examples demonstrate how Full-Stack Marketing OS applies governed skills to a realistic decision. They are teaching artifacts, not proof that the depicted strategy produced real-world results.

## Status label

Every example must declare one of these states near the top:

- **Synthetic worked example** — fictional business/data created only to demonstrate the method.
- **Anonymized worked example** — based on real work but stripped of identifying/client-confidential information; claims must still be traceable internally.
- **Verified public case study** — real business/result with publishable evidence and permission where required.

Do not present a synthetic or anonymized example as a verified public case study.

## Required structure

A full worked example should preserve this sequence:

```text
Starting request
→ Evidence supplied
→ Evidence classification
→ Skill routing / owner chain
→ Decision record
→ Specialist handoffs
→ Prioritized actions
→ Explicit non-priorities
→ Measurement / learning plan
→ Final deliverable
→ Implementation status
```

## Evidence classification

Label decision-relevant inputs as appropriate:

- **Observed** — directly present in supplied/source data.
- **Calculated** — derived from observed values with a stated calculation.
- **Inferred** — interpretation supported by evidence but not directly observed.
- **Assumed** — provisional input used only because required evidence is missing.
- **Unknown** — not established and not safely inferable.

Do not silently upgrade an assumption, competitor observation, survey response, platform attribution claim, or model inference into fact.

## Decision record format

Use a professional decision record rather than hidden chain-of-thought:

| Evidence | Evidence state | Diagnosis / interpretation | Decision implication | Validation needed |
|---|---|---|---|---|
| ... | Observed / Calculated / Inferred / Assumed / Unknown | ... | ... | ... |

The record should show enough reasoning for another practitioner to audit the decision without exposing private model scratch work.

## Skill ownership

Name the primary owner for each substantive decision. Examples may compose multiple skills, but one skill should own each decision.

Example:

```text
$marketing-intake
→ $growth-strategy
→ $performance-diagnostics
→ specialist owners such as $google-ads, $creative-strategy, $cro
→ $tracking-measurement
→ $optimization-scaling when readiness is actually established
```

Do not let a broad example turn `$growth-strategy` or `$marketing-router` into a substitute for specialist decisions.

## Required non-priorities

Every substantial example should say what **not** to do yet. This demonstrates prioritization and protects against activity bias.

Examples:

- do not scale spend before economics/readiness are established
- do not redesign the entire site when the evidence points to one narrower friction
- do not call a creative pattern proven from references alone
- do not change pricing because a competitor charges more or less

## Measurement and learning

Where a change is proposed, preserve:

```text
Hypothesis
→ primary business outcome
→ guardrails
→ evidence/measurement level
→ decision window or maturity condition
→ result classification
→ next decision
```

A polished output or completed task is not proof of business success.

## Privacy and truth rules

Do not include:

- client-confidential information
- account access details or credentials
- personal data
- identifiable private customer data
- invented performance claims
- invented testimonials/reviews presented as real
- fake platform screenshots or fake live-state claims

Synthetic data must be clearly labeled synthetic. Real case studies require publishable evidence and appropriate permission.

## Implementation states

Use exact status language where relevant:

`draft → approved → saved/submitted → published/live/processing → observed → verified`

Do not describe a recommendation or mock implementation as live.
