# Google Ads Audit — Worked Example

**Status:** Synthetic worked example

This example shows how `$google-ads` audits a mixed ecommerce account without treating average ROAS, platform recommendations, or one bad day as sufficient evidence for a major change.

## Starting request

> Google Ads spend increased but profit did not. Audit the account, tell me what to change, what to keep, and whether it is ready to scale.

## Business

Fictional brand: **Fieldcraft Supply**

Category: outdoor storage and organization products

Market: United Kingdom

Business model: ecommerce with materially different product margins.

All figures are synthetic.

## Owner chain

```text
$marketing-intake
→ $google-ads
→ $performance-diagnostics when a movement needs causal triage
→ $tracking-measurement for measurement validity
→ $optimization-scaling for readiness, only after channel diagnosis
```

## Files

- [`input-evidence.md`](input-evidence.md)
- [`decision-trace.md`](decision-trace.md)
- [`final-output.md`](final-output.md)

## Learning objective

Show that account-level efficiency can hide product, query, campaign, and marginal-spend differences. The correct decision may be to protect strong demand capture while reducing or restructuring only the weak marginal area.
