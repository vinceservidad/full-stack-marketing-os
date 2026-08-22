---
name: tracking-measurement
description: Audit, design, or diagnose marketing conversion measurement, attribution reconciliation, event integrity, and business-source alignment; not for changing production tracking without approval.
---

# Tracking and Measurement

Classify architecture maps, models, methodologies, processes, checklists, and recommendations with [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md). Keep a collection defect, attribution difference, and business-performance change as distinct evidence categories.

Establish whether the available data can support the requested decision before optimizing against it.

## Scope

Define the primary business outcome, platforms and properties, conversion journey, reporting timezone and currency, consent environment, attribution question, source of truth, and requested level of assurance. Reserve “Primary conversion action” for Google Ads' action-optimization status.

## Method

1. Map the event chain from user action to browser/server collection, platform receipt, deduplication, attribution, reporting, and business-system outcome.
2. Inventory each event's name, trigger, parameters, identifiers, value/currency, counting rule, destination, and primary/secondary role.
3. Test integrity across coverage, correctness, uniqueness, ordering, timeliness, identity continuity, consent behavior, and reconciliation.
4. Separate collection failures from attribution differences and reporting lag.
5. Reconcile using matched definitions and cohorts; explain expected gaps instead of forcing equality.
6. Rank fixes by decision risk, affected volume/value, confidence, reversibility, and validation cost.

Read [references/event-integrity.md](references/event-integrity.md) for event-level QA. Read [references/attribution-reconciliation.md](references/attribution-reconciliation.md) when totals differ across platforms or business systems.

## Rules

- Do not declare tracking healthy from a tag firing once; verify payload quality, receipt, deduplication, downstream reporting, and business reconciliation.
- Do not make several production tagging changes at once when one controlled change can isolate the failure.
- Never expose secrets, raw personal data, or persistent identifiers in reports.
- Do not change primary conversion goals or bidding signals without explicit approval and a dependency analysis.
- For Google Ads, distinguish conversion goals from their conversion actions and each action's Primary/Secondary status. For Meta, distinguish objective, conversion location, performance goal, dataset/pixel, selected event, and attribution setting.
- Treat consented and non-consented coverage explicitly; do not recommend bypassing consent or privacy controls.

## Output

Return: decision supported; architecture map; integrity status by event; reconciliation table; confirmed defects; expected discrepancies; risk-ranked actions; validation plan; exact implementation status.

## QA

Confirm event definitions and timezones match, test and production traffic are separated, duplicate paths are checked, values/currency are verified, attribution windows are visible, privacy boundaries are preserved, and “received” is not confused with “correct.”
