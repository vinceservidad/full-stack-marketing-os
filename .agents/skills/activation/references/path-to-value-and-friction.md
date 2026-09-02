# Path to Value and Friction

Use this reference to map the post-conversion journey from entry into the customer relationship to first meaningful value.

## Build the path

Start with the conversion boundary, then map only steps necessary to reach meaningful value.

For each step record:

| Field | Meaning |
|---|---|
| Step | Customer or system action |
| Why required | Value, safety, compliance, setup, qualification, or avoidable legacy process |
| Owner | Customer, product, service team, partner, system |
| Active effort | Work the customer must perform |
| Wait time | Delay outside active effort |
| Dependency | Data, approval, integration, inventory, human service, etc. |
| Failure signal | What shows the step failed or stalled |
| Evidence | Analytics, support, usability, interviews, operations |
| Removability | required / simplify / sequence / automate / uncertain |

## Friction taxonomy

Do not label every delay “UX friction.” Diagnose the mechanism.

### Comprehension
Customer does not understand what to do, why it matters, or what success looks like.

### Motivation / relevance
The customer understands the action but does not see enough value to complete it. Check poor-fit acquisition and expectation mismatch before adding reminders.

### Effort
The step requires too much work, repeated entry, complex setup, or unnecessary coordination.

### Technical defect
Error, broken integration, unavailable feature, payment/account state, performance problem, identity issue, or bad data prevents progress.

### Trust / anxiety
Customer hesitates because access, permissions, privacy, risk, quality, or consequences are unclear.

### Dependency
Value depends on another person, dataset, inventory item, approval, implementation team, or external platform.

### Operational delay
The business itself is slow: fulfillment, support, onboarding call, approval, scheduling, service delivery, or inventory.

### Qualification / fit
The customer cannot reach value because the product/service is a poor fit, required prerequisites are absent, or acquisition brought the wrong customer.

### Measurement failure
The customer may have reached value, but events are missing, duplicated, delayed, or defined incorrectly.

## First binding barrier

Prioritize the earliest barrier that materially prevents a qualified customer from reaching value. Do not optimize a later tutorial screen if customers are stalled earlier by missing data or fulfillment.

A useful diagnosis states:

`Observed stall → affected segment → evidence → plausible mechanism → competing explanations → owner → intervention hypothesis`

## Necessary versus unnecessary friction

Some friction protects the customer or business:

- identity verification
- qualification
- consent
- safety/compliance checks
- required setup for accurate results
- expectation setting
- data permissions
- service preparation

Do not remove necessary friction merely to improve activation rate or time-to-value. Instead ask whether it can be made clearer, better sequenced, more transparent, assisted, or faster without weakening its purpose.

## Journey variants

Do not blend materially different journeys:

- self-serve versus assisted
- free/trial versus paid
- mobile versus desktop when setup differs
- plan/tier/package differences
- new versus migrated customer
- market/geography where operations differ
- acquisition source when it materially changes fit or expectation

A blended activation rate can hide a broken journey or a mix shift.

## Intervention families

Use only when the diagnosed mechanism supports them:

- remove a nonessential step
- prefill or reuse known data
- reorder steps so value appears earlier
- progressive setup rather than all-at-once setup
- better expectation setting
- contextual guidance
- human assistance or escalation
- clearer permissions/trust explanation
- operational SLA/process fix
- technical fix
- qualification improvement upstream
- lifecycle reminder/trigger through `$lifecycle-marketing`
- copy clarification through `$copywriting`
- bounded surface UX improvement through `$cro`

Do not default to tooltips, checklists, gamification, email sequences, discounts, or concierge onboarding without evidence of the barrier they solve.

## Time decomposition

When useful, separate:

`Total time to value = customer active effort + system processing + business operational wait + external dependency wait`

This prevents blaming the customer journey for a fulfillment or operations problem.

## Output

Return a path-to-value map, the first binding barrier, evidence and competing explanations, the responsible owner, and the smallest meaningful intervention to validate next.
