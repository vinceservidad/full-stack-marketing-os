# Meta Ads Audit and Creative Testing — Worked Example

**Status:** Synthetic worked example

This walkthrough shows how Full-Stack Marketing OS audits a Meta Ads account without treating platform-attributed ROAS, CTR, frequency, audience type, or an undocumented “algorithm change” as business truth.

The example is fictional. All business names, numbers, creatives, customer evidence, and outcomes are synthetic teaching data.

## Starting request

> Meta Ads performance feels weaker even though some ads still have good CTR and retargeting ROAS. Audit the account, tell me what is actually wrong, what not to change yet, and what we should test next.

## Primary owners

```text
$marketing-intake
      ↓
$meta-ads
      ↓
$performance-diagnostics
      ↓
$tracking-measurement
      ↓
$creative-strategy
      ↓
$optimization-scaling
```

`$meta-ads` owns platform structure, delivery, audiences, placements, and ads. `$performance-diagnostics` helps localize the performance change. `$tracking-measurement` owns reconciliation and causal validity. `$creative-strategy` owns new angle/concept development. `$optimization-scaling` owns any later decision to add spend.

## Files

- [`input-evidence.md`](input-evidence.md) — synthetic account, business, creative, and measurement evidence
- [`decision-trace.md`](decision-trace.md) — auditable evidence → interpretation → action record
- [`final-output.md`](final-output.md) — example user-facing audit output

## What this example teaches

- retargeting ROAS can look strong while new-customer acquisition weakens
- high outbound CTR can coexist with poor landing-page or purchase quality
- rising frequency plus falling response is a fatigue clue, not automatic proof
- broad-vs-interest performance in one snapshot does not prove a universal audience rule
- Meta-attributed revenue must not be silently promoted to source-of-truth business revenue
- creative testing should isolate meaningful strategic variables rather than produce cosmetic variants
- scaling waits for business economics, measurement confidence, and stable evidence

This is a worked example, not a claim that the same diagnosis or action will fit another Meta account.
