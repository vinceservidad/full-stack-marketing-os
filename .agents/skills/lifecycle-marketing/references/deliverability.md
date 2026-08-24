# Deliverability

Inbox placement is a prerequisite for every other lifecycle-marketing decision — a perfectly designed sequence that lands in spam has zero effect regardless of its logic or copy. Deliverability is also slow to damage and slow to repair; a decision made for short-term reach can cost weeks of placement afterward.

## What governs deliverability

Sender reputation (domain and IP), authenticated correctly (SPF, DKIM, DMARC configured and aligned); list hygiene (bounce rate, spam-complaint rate, engagement rate); consistency of sending volume and pattern; and recipient engagement signals (opens, clicks, and — more heavily weighted by mailbox providers — deletions without opening and spam reports).

## Rules

- Do not increase send volume or frequency sharply without a ramp; mailbox providers treat a sudden volume spike as a risk signal regardless of list quality.
- Remove or suppress chronically unengaged contacts on a stated cadence rather than continuing to send indefinitely; sending to an unengaged segment drags overall engagement metrics down and damages reputation for engaged segments sharing the same sending domain.
- Do not purchase, rent, or otherwise acquire a list from outside the business's own consented capture; it is both a consent violation and near-certain to damage deliverability immediately.
- A spike in spam complaints or bounce rate is a stop condition, not a metric to monitor passively; treat it with the same urgency as a tracking defect — pause the implicated send and diagnose before continuing.
- Warm a new sending domain or IP gradually with the most engaged segment first; do not launch a new domain directly into full-list volume.
- Authentication configuration (SPF/DKIM/DMARC) is a prerequisite check before diagnosing any other deliverability problem; verify it is correctly configured and aligned before attributing a placement issue to content or list quality.
