# Event Integrity

Use this reference for a conversion, lead, purchase, or funnel-event audit.

## Event contract

For each event record:

- Business meaning and qualifying condition
- Trigger location and trigger owner
- Browser, server, app, CRM, or imported source
- Required parameters and accepted types
- Event ID and deduplication scope
- User/session/order/lead identifiers and privacy treatment
- Value, currency, quantity, item, and tax/shipping rules
- Timestamp and timezone
- Consent dependency
- Receiving destinations
- Counting rule and optimization role

## Tests

Cover valid completion, duplicate submission, refresh/back navigation, payment failure, cancellation/refund where relevant, cross-domain transition, consent accepted/denied, ad blocker or network loss, mobile/desktop, and delayed server delivery.

Grade each test as `verified`, `failed`, `not observed`, or `not applicable`. A debugger signal proves dispatch only; confirm receipt and reporting separately.
