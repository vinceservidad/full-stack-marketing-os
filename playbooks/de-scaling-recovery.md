# De-scaling and Recovery Playbook

## Knowledge metadata

- Primary type: playbook
- Secondary type: containment / recovery process
- Decision: how to reduce exposure and verify recovery without destroying valuable coverage
- Evidence status: breach and recovery evidence required
- Freshness: incident-current

1. Identify the breached financial, quality, delivery, operations, measurement, policy, or capacity guardrail.
2. Separate measurement invalidity from genuine business harm.
3. Contain the smallest affected entity while preserving evidence and protected coverage.
4. Execute only the approved rollback or de-scaling step; document prior/current state.
5. Reconcile the business source of truth through the relevant lag/recovery window.
6. Decide `recovered`, `partially recovered`, `not recovered`, `new root cause`, or `insufficient evidence`.
7. Resume only after the failed readiness gate is restored and a new bounded plan is approved.
