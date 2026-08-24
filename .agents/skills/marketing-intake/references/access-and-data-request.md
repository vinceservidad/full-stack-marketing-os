# Access and Data Request

Request the minimum evidence that could change a decision. A long request list delays work and lowers response quality; an incomplete one produces confident wrong answers.

## Ranking rule

Request in order of decision impact, not convenience:

1. Evidence whose absence blocks the primary decision.
2. Evidence that would change the recommended action.
3. Evidence that would change confidence but not direction.
4. Evidence that improves reporting only — request last or not at all.

State for each request what remains blocked without it. A request without a stated consequence reads as optional and is treated that way.

## Common requests by decision

| Decision | Minimum evidence |
|---|---|
| Profitability or scaling | Cost of goods sold, variable costs, refund rate, revenue basis, source-of-truth revenue for the period |
| Google Ads audit | Campaign, ad group, search term, and asset exports; conversion goal and action configuration; change history |
| Shopping or Performance Max | Item-level performance, feed status, price and availability, asset-group structure |
| Meta audit | Campaign to ad-level export, dataset and event configuration, attribution setting, creative assets |
| Measurement integrity | Tag or dataset configuration, event parameters, consent configuration, duplicate-event evidence, platform-versus-business reconciliation |
| Lead quality | Customer Relationship Management outcomes joined to source, stage definitions, lag distribution |
| Conversion Rate Optimization | Segmented analytics, recordings, funnel errors, page speed, support and sales objections |
| Diagnosis of a change | Both periods at the same grain, change history, and any promotion or outage calendar |

## Access states

Record each as: `granted`, `pending`, `read-only`, `refused`, or `not requested`. Read-only access is sufficient for audit and diagnosis and is the default to request. Do not request change access before a change is authorized.

## Privacy

Request the minimum personal data any decision requires, and prefer aggregates. Do not request customer contact records, payment details, or identifiable session data unless a named decision requires them. Record research provenance — source, date, method — without reproducing identifying detail. A quotation requires a traceable supplied source; do not reconstruct or paraphrase customer language from memory and present it as evidence.

## Handling a refusal or delay

Record the refusal, the decisions it blocks, and the nearest weaker evidence that could substitute at lower confidence. Proceed on the unblocked work. Do not substitute a benchmark for refused data.
