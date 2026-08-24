# Authorization Register

Records what the user has and has not approved. Default is read-only: no budget, bid, campaign, conversion goal, audience, product coverage, offer, tracking, or live page changes without explicit approval.

## Record per authorization

Requested change; exact entity affected; current state; proposed state; who approved; date; scope limit; expiry; rollback condition; stopping rule; current execution state.

## Execution states

Keep these distinct in every report. Collapsing them is how a draft becomes described as live.

`draft` → `proposed` → `approved` → `saved` → `published` → `live` → `processing` → `verified`

- `saved` is not `published`. `published` is not `live`. `live` is not `verified`.
- `processing` means the platform has accepted the change but outcome data has not matured.
- `verified` requires post-change observation against the business source of truth within a stated window.

Never describe a recommendation as implemented, and never describe an implemented change as verified before its observation window closes.

## Scope discipline

An approval covers the exact entity, magnitude, and period stated — nothing adjacent. Approval to raise one campaign's budget is not approval to raise another's, to raise the same one again, or to change its bidding strategy. Approval granted in a prior engagement or period does not carry forward.

An expired or exhausted authorization returns to unapproved.

## Before proposing any change

State the exact change, expected effect, downside, the smallest reversible version, rollback condition, stopping rule, observation window, and required approver. A change without a rollback condition and stopping rule is not ready to propose.

## Scaling

Scaling authorization additionally requires the `optimization-scaling` readiness, economics, constraint, marginal-evidence, capacity, and guardrail gates. Intake records whether each gate is satisfied, unsatisfied, or unknown. Intake never satisfies a gate itself.
