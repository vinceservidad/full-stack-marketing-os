<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Intake, Customer Research, and ICP

## Skill: $marketing-intake

**Use when:** Capture and grade the evidence, metric definitions, access, and authorization behind a marketing engagement before substantial audit, diagnosis, planning, or scaling work; use when scope, data provenance, economics, or approval boundaries are unclear.

Record what was actually received, from whom, in what state. Intake does not establish that a claim is true — it establishes what is known, how it is known, and what would reverse the conclusion.

Classify the resulting artifact with `KNOWLEDGE-TAXONOMY.md`. An intake record is a process artifact and evidence ledger, never proof of an outcome.

### Context

Required before intake can complete: business model, primary business outcome, account and market scope, date range and comparison period, currency, reporting timezone, data sources supplied, access available, and the system treated as the business source of truth.

Required before any profitability, scaling, or lead-quality conclusion: cost and profit definitions with named profit level, cost of goods sold, discounts, refunds, fulfillment and payment costs, and — for lead generation — lifecycle stage definitions and Customer Relationship Management outcomes.

Intake may proceed with gaps. It may not present a gap as satisfied.

### Method

1. Record engagement context and scope. Separate what the user asserted from what a source system shows. See Engagement context.
2. Enter every decision-relevant claim in the evidence register with its source, collection method, and evidence state. See Evidence register.
3. Define every metric and lifecycle term before any comparison. Platform labels are not definitions. See Metric definitions.
4. Record conversion architecture: Google Ads conversion goals, their included conversion actions and Primary or Secondary status; Meta objective, conversion location, performance goal, dataset, and event. Record attribution settings, windows, conversion lag, and known tracking defects.
5. Record capacity — inventory, fulfillment, creative, sales, and service — wherever a recommendation could exceed it.
6. Request only the missing evidence that could change a decision, ranked by decision impact. See Access and data request.
7. Record the authorization boundary before proposing any change. See Authorization register.
8. State which decisions the current evidence can and cannot support, and name the gaps capable of reversing each one.

### Rules

- Never upgrade an evidence state. A user-reported figure remains user-reported until observed in a named source; an observed figure remains unverified until reconciled with the business source of truth.
- Never fill a gap with a benchmark, an assumed margin, a typical conversion rate, or a platform default. Record it as unknown.
- Do not treat platform attribution as the business outcome, and do not reconcile platforms by addition.
- Do not compare periods, accounts, or channels before their metric definitions are recorded and confirmed compatible.
- Do not request personal data that no decision requires. Record research provenance without exposing identifying detail. Quotations require a traceable supplied source.
- Absence of a supplied cost structure blocks a profitability conclusion; it does not block analysis labeled as efficiency-only.
- Intake authorizes nothing. Recording an approval is not receiving one, and no intake output may imply a live change.
- Do not declare intake complete while a gap capable of reversing the primary decision is open. Declare it partial and name the gap.

### Output

Intake record: engagement context; primary business outcome; scope and period; source-of-truth system; evidence register with states; metric and conversion definitions; capacity constraints; authorization boundary; ranked outstanding requests; decisions currently supportable; decisions blocked and what would unblock them; exact status.

Access request: named source, specific artifact or export, date range, reason it is decision-changing, and what remains blocked without it.

### QA

Confirm every decision-relevant claim carries a source and evidence state; no state was upgraded without a named source; no gap was filled by assumption; metric definitions precede comparisons; conversion goal and action language follows the glossary; personal data is minimal and provenance is traceable; the authorization boundary is explicit; and blocked decisions are listed rather than answered.

### Reference: access and data request ($marketing-intake)

### Access and Data Request

Request the minimum evidence that could change a decision. A long request list delays work and lowers response quality; an incomplete one produces confident wrong answers.

#### Ranking rule

Request in order of decision impact, not convenience:

1. Evidence whose absence blocks the primary decision.
2. Evidence that would change the recommended action.
3. Evidence that would change confidence but not direction.
4. Evidence that improves reporting only — request last or not at all.

State for each request what remains blocked without it. A request without a stated consequence reads as optional and is treated that way.

#### Common requests by decision

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

#### Access states

Record each as: `granted`, `pending`, `read-only`, `refused`, or `not requested`. Read-only access is sufficient for audit and diagnosis and is the default to request. Do not request change access before a change is authorized.

#### Privacy

Request the minimum personal data any decision requires, and prefer aggregates. Do not request customer contact records, payment details, or identifiable session data unless a named decision requires them. Record research provenance — source, date, method — without reproducing identifying detail. A quotation requires a traceable supplied source; do not reconstruct or paraphrase customer language from memory and present it as evidence.

#### Handling a refusal or delay

Record the refusal, the decisions it blocks, and the nearest weaker evidence that could substitute at lower confidence. Proceed on the unblocked work. Do not substitute a benchmark for refused data.

### Reference: authorization register ($marketing-intake)

### Authorization Register

Records what the user has and has not approved. Default is read-only: no budget, bid, campaign, conversion goal, audience, product coverage, offer, tracking, or live page changes without explicit approval.

#### Record per authorization

Requested change; exact entity affected; current state; proposed state; who approved; date; scope limit; expiry; rollback condition; stopping rule; current execution state.

#### Execution states

Keep these distinct in every report. Collapsing them is how a draft becomes described as live.

`draft` → `proposed` → `approved` → `saved` → `published` → `live` → `processing` → `verified`

- `saved` is not `published`. `published` is not `live`. `live` is not `verified`.
- `processing` means the platform has accepted the change but outcome data has not matured.
- `verified` requires post-change observation against the business source of truth within a stated window.

Never describe a recommendation as implemented, and never describe an implemented change as verified before its observation window closes.

#### Scope discipline

An approval covers the exact entity, magnitude, and period stated — nothing adjacent. Approval to raise one campaign's budget is not approval to raise another's, to raise the same one again, or to change its bidding strategy. Approval granted in a prior engagement or period does not carry forward.

An expired or exhausted authorization returns to unapproved.

#### Before proposing any change

State the exact change, expected effect, downside, the smallest reversible version, rollback condition, stopping rule, observation window, and required approver. A change without a rollback condition and stopping rule is not ready to propose.

#### Scaling

Scaling authorization additionally requires the `optimization-scaling` readiness, economics, constraint, marginal-evidence, capacity, and guardrail gates. Intake records whether each gate is satisfied, unsatisfied, or unknown. Intake never satisfies a gate itself.

### Reference: engagement context ($marketing-intake)

### Engagement Context

Establishes what the engagement is about and which numbers are comparable. Complete before any period comparison, cross-channel comparison, or profitability statement.

#### Record

| Field | Why it is decision-changing |
|---|---|
| Business model | Ecommerce, lead generation, subscription, marketplace, and retail-assisted models have different outcomes, lags, and capacity limits |
| Primary business outcome | The commercial result the work must improve — not a platform metric, and not the Google Ads Primary conversion action setting |
| Supporting outcomes | Results that matter but must not be optimized as if primary |
| Account and market scope | Accounts, brands, regions, languages, and stores in and out of scope |
| Date range | Exact start and end, and whether the range is complete |
| Comparison period | Prior period, prior year, or none — with the reason |
| Currency | Reporting currency and whether any conversion has been applied |
| Reporting timezone | Platform timezone versus business reporting timezone |
| Source of truth | The system whose numbers govern when platforms disagree |
| Seasonality and events | Promotions, launches, outages, price changes, or PR events inside either period |
| Known disruptions | Tracking changes, site migrations, account restructures, budget freezes |

#### Comparability check

A comparison is invalid until each holds, or the exception is recorded:

- Both periods use the same metric definitions.
- Both periods use the same currency and timezone.
- Both periods are complete, or the incomplete one is labeled and excluded from conclusions.
- Neither period contains an unrecorded promotion, outage, or structural change.
- Attribution settings did not change between periods.
- Conversion lag has matured in both, or the immature portion is stated.

If any fails, record the comparison as incomparable or adjusted, and say which.

#### Scope discipline

Record what is explicitly **out** of scope. An unrecorded exclusion becomes an assumed inclusion later.

Record who supplied each context field. Context supplied by a stakeholder is a claim, not an observation, and belongs in the evidence register at that state.

### Reference: evidence register ($marketing-intake)

### Evidence Register

One row per decision-relevant claim. The register records what is known and how — never what is assumed to be true.

#### Evidence states

Ordered weakest to strongest. A state is never upgraded without the named artifact that justifies it.

| State | Meaning | May support |
|---|---|---|
| `asserted` | A person stated it; no artifact seen | Hypotheses and questions only |
| `documented` | Appears in a supplied document or screenshot | Provisional analysis, labeled |
| `observed` | Seen directly in a named source system | Analysis and recommendations, labeled by source |
| `reconciled` | Agrees with the business source of truth | Profitability and commercial conclusions |
| `verified` | Reconciled and independently confirmed, or experimentally established | Causal claims within the tested scope |
| `unknown` | Required but not supplied | Nothing — blocks dependent decisions |
| `contradicted` | Two sources disagree and the conflict is unresolved | Nothing — must be resolved or declared |

#### Row fields

Claim; value; source system or person; artifact or export name; collection method; date range covered; evidence state; decisions it supports; what would change the state; date recorded.

#### Rules

- A platform export is `observed` for platform behavior and no stronger for business outcome. Reaching `reconciled` requires agreement with the source of truth.
- A stakeholder restating a platform number is `asserted`, not `observed`. The artifact, not the confidence of the speaker, sets the state.
- `contradicted` outranks convenience. Do not silently pick the more favorable source; record both and the resolution method.
- A claim used in two decisions at different confidence levels is one row, not two.
- Absence of evidence is `unknown`, never a default, benchmark, or industry figure.
- Record the collection method where it changes interpretation: modeled versus observed conversions, sampled versus complete data, survey self-report versus behavior.

#### Decision blocking

For each pending decision, list the rows it depends on and the weakest state among them. The weakest dependency governs the decision's confidence. If that state is `unknown` or `contradicted`, the decision is blocked and must be reported as blocked rather than answered with a caveat.

### Reference: metric definition register ($marketing-intake)

### Metric Definition Register

Metric names are not metric definitions. Two systems using the word "conversion" rarely count the same event. Define before comparing.

Use `GLOSSARY.md` as the canonical contract, and record client-specific variants here rather than redefining canonical terms.

#### Define per metric

Name as used by the client; canonical glossary term; source system; exact event or record counted; counting rule (every versus one); value basis; inclusion and exclusion rules; attribution model and window; timezone; currency; known defects.

#### Conversion architecture

**Google Ads.** Record each conversion goal, the conversion actions inside it, each action's Primary or Secondary status, which goal the campaign uses, counting setting, value setting, and attribution window. A Primary action influences bidding only when the campaign uses its containing goal. Reserve "Primary conversion action" for this setting; the main commercial result is the primary business outcome.

**Meta.** Record objective, conversion location, performance goal, dataset, optimization event, and attribution setting. Record whether reported conversions are modeled.

**Analytics and source of truth.** Record the equivalent definition in the analytics platform and in the business system, and whether the three agree.

#### Cost and profit

Never record "profit" without its level and included costs.

| Field | Required detail |
|---|---|
| Revenue basis | Gross, net of discounts, net of refunds, with or without tax and shipping |
| Cost of goods sold | Included costs and whether landed |
| Variable costs | Fulfillment, payment fees, packaging, returns processing |
| Profit level | Gross, contribution after media, contribution after variable costs, operating |
| Discounts and refunds | Whether already deducted from the stated revenue basis |

Do not double-count a discount or refund already inside net revenue.

#### Lifecycle and lead quality

For lead generation, define each stage — lead, marketing qualified, sales qualified, opportunity, customer — with its owning system, entry criteria, and typical lag. Keep funnel stage, awareness level, audience temperature, and lifecycle stage distinct. Record whether Customer Relationship Management outcomes are available and how they join to marketing source data.

#### Comparability

Two metrics are comparable only when name, event, counting, value basis, attribution, window, timezone, and currency all match. Record any mismatch and either normalize it or declare the comparison invalid. Never resolve a mismatch by preferring the more favorable number.

## Skill: $customer-research

**Use when:** Plan or synthesize evidence-led customer research for marketing decisions using interviews, reviews, surveys, sales/support records, and behavioral data; not for inventing customer voice.

Classify outputs with `KNOWLEDGE-TAXONOMY.md`: observed pattern, hypothesis, methodology, process, or recommendation. Patterns must retain provenance and cannot be reported as causal conclusions.

Produce decision-ready insights while preserving source provenance, segment differences, uncertainty, and the difference between what people say and do.

### Frame the decision

Define the marketing decision, target population, relevant buying situation, exclusions, current hypotheses, and evidence threshold. Ask only questions whose answers could change a decision.

### Method

1. Inventory first-party and external sources with dates, sample, collection method, and bias.
2. Prefer recent, relevant, behavior-linked evidence; use secondary sources for context, not fabricated certainty.
3. Extract atomic evidence with verbatim wording only when provided and permitted. Attach source, segment, and context.
4. Code patterns: trigger, job, desired outcome, barrier, anxiety, alternative, selection criterion, proof, language, and post-purchase result.
5. Search for contradictions, non-buyers, churn/refund evidence, and segment splits.
6. Convert patterns into implications and tests. Keep insight, inference, and recommendation distinct.

Read references/source-grading.md before combining heterogeneous sources. Read references/interview-synthesis.md for transcript or notes synthesis.

### Rules

- Never invent quotes, reviews, prevalence, or customer motivations.
- Use “Voice of Customer” only for traceable supplied customer language. Label model-created wording as synthesis, paraphrase, inference, or messaging hypothesis.
- Frequency is not importance; weight behavioral proximity, consequence, specificity, and segment fit.
- Do not treat leading survey answers as spontaneous customer language.
- Preserve negative and contradictory evidence instead of smoothing it into a persona.
- Remove or mask personal data that is unnecessary for the decision.

### Output

Return: research question; source table; segment and situation; evidence themes with counts only when valid; contradictions; language bank with provenance; implications; testable hypotheses; gaps and next research.

### QA

Check every quotation is traceable, counts use a defined denominator, sources are not double-counted, sample limitations are visible, observed behavior is separated from stated preference, and recommendations do not exceed the evidence.

### Reference: interview synthesis ($customer-research)

### Interview Synthesis

Use a consistent evidence record:

`source | segment | situation | exact evidence or close paraphrase | code | confidence | implication`

Reconstruct the timeline: trigger → prior workaround → search → alternatives → decision criteria → purchase friction → use → result. Identify switching forces: push of the old situation, pull of the new solution, anxiety about change, and habit or inertia.

Count participants, not repeated mentions, when reporting prevalence. Keep outliers that expose high-impact risk or a distinct segment. A memorable quote is evidence of phrasing, not market frequency.

### Reference: source grading ($customer-research)

### Source Grading

Grade evidence on five dimensions: relevance to the decision, recency, behavioral proximity, collection quality, and sample coverage.

#### Typical strengths and limits

- Purchase, usage, churn, refund, and CRM outcomes: behaviorally strong; may omit motive.
- Sales and support records: rich objections and context; filtered by staff and process.
- Interviews: strong for language, sequence, and causal story; weak for prevalence.
- Surveys: useful for structured comparison when sampling and wording are sound; vulnerable to leading questions and self-report bias.
- Reviews and communities: natural language and extremes; identity, representativeness, and verification may be uncertain.
- Competitor or market reports: useful context; rarely direct proof of this audience's behavior.

Do not collapse the grades into a decorative numeric score. Explain the one or two limitations that matter to the decision.

## Skill: $icp-jtbd

**Use when:** Define or refine ideal-customer segments and Jobs-to-be-Done from verified commercial and customer evidence; use for targeting and positioning choices, not fictional personas.

Classify segment outputs with `KNOWLEDGE-TAXONOMY.md`: model, methodology, process, pattern, hypothesis, or strategy. Do not turn a research pattern into a universal segment truth.

Build actionable segment choices around valuable, reachable customers in a specific buying situation.

### Inputs

Use customer and pipeline outcomes, revenue and margin, retention/refunds, sales-cycle data, product fit, use cases, customer research, channel reachability, operational capacity, and strategic constraints. If evidence is sparse, produce hypotheses and a collection plan rather than a definitive ICP.

### Method

1. Separate market, account/customer segment, buyer/user roles, and buying situation.
2. Identify the job as progress sought in context: `When [situation], help me [motivation/progress], so I can [desired outcome].`
3. Map functional, emotional, and social dimensions only when evidence supports them.
4. Identify triggers, current alternatives, switching forces, selection criteria, anxieties, and success signals.
5. Evaluate segments on outcome value, product fit, urgency, reachability, evidence strength, sales/servicing cost, retention potential, and strategic fit.
6. Choose explicit priority, secondary, experimental, and excluded segments with reasons.

### Rules

- Do not use demographics as a substitute for need, situation, economics, or reachability.
- Do not average incompatible buyers into one persona.
- Revenue alone does not define an ICP; include margin, retention, cost-to-serve, close probability, and capacity where available.
- Distinguish user, buyer, approver, and blocker in multi-stakeholder purchases.
- Treat exclusions as strategic focus, not claims about people.
- Prefer “priority customer segment” where consumer context makes account-oriented ICP language unnatural. Keep ICP, persona, buying committee, buying situation, and JTBD distinct.

### Output

Return: decision; evidence base; priority segment card; JTBD statement; trigger and switching-forces map; buying committee; value/economic fit; reachability; disqualifiers; messaging implications; evidence gaps and validation plan.


### Library references

Owned root artifacts, read when their scope applies:

- lead-generation.md — lead-generation segment and message workflow.
- marketing-audit.md — business and market-level audit format, distinct in scope from a channel audit.

### QA

Check the segment is distinguishable and reachable, the job describes progress rather than a product feature, economics are visible, roles are not conflated, exclusions are evidence-safe, and certainty matches the source quality.
