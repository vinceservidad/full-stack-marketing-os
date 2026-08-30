<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->


# Terminology and Governance Contracts

## Canonical Marketing Glossary

This glossary defines Marketing OS terminology. Platform interface labels may change; preserve the strategic concept and map the current product label explicitly. When a client's source system uses a different definition, record that definition before comparing metrics.

### Commercial outcomes

- **Gross sales:** Sales before discounts, refunds, and other revenue deductions.
- **Net revenue:** Gross sales minus discounts, refunds, and explicitly defined revenue deductions. State whether tax and shipping revenue are included.
- **Gross profit:** Net revenue minus cost of goods sold (COGS).
- **Contribution profit before media:** Gross profit minus variable fulfillment, payment, marketplace, and servicing costs included in scope.
- **Contribution profit after media:** Contribution profit before media minus media spend.
- **Contribution margin:** The defined contribution profit divided by net revenue. Always state whether it is before or after media.
- **Operating profit:** Revenue minus the defined variable and fixed operating expenses. Do not use this term when fixed costs are unavailable.
- **Return on ad spend (ROAS):** Attributed revenue divided by media spend. ROAS is not profit.
- **Customer acquisition cost (CAC):** Acquisition costs divided by newly acquired customers under a stated cost and customer definition.
- **Realized revenue:** Revenue actually recorded under the business's defined recognition rule, not merely attributed or forecast.
- **Qualified pipeline:** Opportunity value meeting the business's explicit qualification and stage rules.

Use one of these formulas, according to the available source definition:

`Contribution profit after media = gross sales - discounts - refunds - COGS - variable fulfillment - payment fees - media spend`

`Contribution profit after media = net revenue - COGS - variable fulfillment - payment fees - media spend`

Never subtract discounts or refunds again when they are already reflected in net revenue.

### Measurement and causality

- **Business source of truth:** The authoritative system for the outcome in question, such as paid orders, fulfilled revenue, qualified opportunities, or closed-won revenue.
- **Event:** A recorded occurrence with a defined trigger and parameters.
- **Conversion:** A context-dependent desired action. Name the exact action rather than relying on this word alone.
- **Primary business outcome:** The main commercial or qualified result for an analysis. This is not the Google Ads setting “Primary conversion action.”
- **Google Ads conversion action:** A specific measured action in Google Ads.
- **Google Ads conversion goal:** A grouping of related conversion actions used in campaign optimization settings.
- **Primary conversion action:** Google Ads action-optimization status eligible for bidding and the Conversions columns when the campaign uses its containing goal.
- **Secondary conversion action:** Google Ads observation-oriented status reported outside the primary Conversions columns, subject to custom-goal behavior.
- **Meta performance goal / optimization event:** State the campaign objective, conversion location, dataset or pixel, selected event, and performance goal separately; do not collapse them into one setting.
- **Bidding signal:** A measured input that can influence automated bidding. A tracked event is not necessarily a bidding signal.
- **Collection:** Capture and transmission of data.
- **Receipt:** Confirmation that the destination received the event; receipt does not prove correctness.
- **Deduplication:** Identification and suppression of duplicate representations of the same event.
- **Attribution:** A rule or model that assigns credit for an outcome.
- **Reconciliation:** Explanation of differences between systems after scope and definitions are aligned.
- **Incrementality:** Additional outcomes caused by an intervention compared with what would otherwise have happened.
- **Causality:** A supported claim that changing one factor produced a change in another; timing or correlation alone is insufficient.

### Audience, journey, and research

- **Market:** The broader demand environment in which customers and competitors participate.
- **Segment:** A distinguishable group sharing decision-relevant needs, situations, economics, or reachability.
- **Ideal Customer Profile (ICP):** The economically and operationally attractive customer or account profile. For consumer contexts, “priority customer segment” may be clearer.
- **Persona:** A research-backed representation of a customer type; never a substitute for evidence or economics.
- **Buying situation:** The context and trigger in which progress becomes important.
- **Jobs-to-be-Done (JTBD):** The progress a customer seeks in a situation, not the act of using a product.
- **Funnel or journey stage:** Relationship to the buying process.
- **Awareness level:** What the audience understands about the problem, solutions, product, and offer.
- **Audience temperature:** Degree of prior exposure or engagement.
- **Lifecycle stage:** CRM or customer-state classification, such as lead, opportunity, customer, or lapsed customer.
- **Voice of Customer (VoC):** Traceable customer language from supplied research. Model-generated language is a synthesis or hypothesis, not VoC.
- **Research provenance:** The source, date, segment, method, context, and limitations attached to evidence.

### Paid media and creative

- **New-customer acquisition / prospecting:** Strategic category for reaching eligible potential customers without a qualifying prior relationship. “Prospecting” may not be a platform interface label.
- **Retargeting / remarketing:** Strategic category for reaching eligible people based on prior engagement, visit, customer, or behavioral signals. Name the exact audience source, window, and exclusions.
- **Creative strategy:** System of insights, angles, messages, concepts, formats, and tests.
- **Angle:** Strategic reason the audience should care.
- **Hook:** Opening expression used to earn attention.
- **Creative concept:** Central advertising idea or execution.
- **Creative asset:** The produced image, video, copy, audio, or component.
- **Ad:** The configured platform entity combining identity, creative assets, copy, CTA, destination, and delivery settings.
- **Format:** Delivery form such as video, static image, carousel, or collection.
- **Adaptation:** Placement- or aspect-ratio-specific version; not automatically a distinct strategic test.
- **Message scent:** Continuity between the promise in an ad, query, or link and the destination's immediate message.
- **Full-funnel:** Demand/awareness through consideration, conversion, qualified or purchased outcome, and retention or realized customer value—not merely a set of campaign objectives.

### Lead lifecycle

Use the client's actual CRM stages, then map them where applicable:

`inquiry -> lead -> contacted lead -> qualified lead -> sales-qualified opportunity -> appointment or proposal -> closed-won customer -> realized revenue`

Define qualification, stage-entry rules, date basis, and value basis before comparing CPL, cost per qualified lead, pipeline, close rate, or CAC.

### Optimization and scaling

- **Scaling:** Increasing a verified primary business outcome while keeping named economics, quality, capacity, measurement, and risk guardrails acceptable.
- **Spend growth:** An increase in advertising spend; not automatically scaling.
- **Profitable scaling:** Increasing contribution profit after media under explicitly defined revenue and cost inputs.
- **Qualified scaling:** Increasing qualified pipeline or realized customer value while preserving defined quality and capacity thresholds.
- **Vertical scaling:** Increasing budget or bidding pressure within existing eligible coverage.
- **Horizontal scaling:** Expanding products, queries, audiences, placements, markets, creatives, or other eligible coverage.
- **Creative scaling:** Increasing evidence-backed creative diversity, learning, and production capacity.
- **Funnel scaling:** Increasing qualified post-click conversion capacity or reliability.
- **Operational scaling:** Increasing inventory, fulfillment, sales, service, support, onboarding, or cash capacity.
- **Blended efficiency:** Average performance across the scoped total spend and outcome.
- **Marginal efficiency:** Performance associated with the change in spend/outcome between comparable states.
- **Saturation:** Declining marginal opportunity as high-value eligible demand or capacity is increasingly exhausted.
- **Scale ceiling:** Highest currently supportable activity before a named economic, quality, capacity, measurement, or risk guardrail becomes unacceptable.
- **Scaling step:** One bounded, interpretable increase in spend, bidding pressure, exposure, or coverage with a decision and rollback contract.
- **De-scaling:** Controlled reduction in inefficient or unsustainable activity while protecting valuable coverage and evidence.
- **Recovery verification:** Source-of-truth confirmation that a breached condition has restored through the relevant lag/window.

### Evidence and experimentation

- **Observed:** Directly present in a named source and scope.
- **Calculated:** Derived with visible formula and inputs.
- **Inferred:** Supported explanation that has not been isolated.
- **Assumed:** Explicitly unverified input used to proceed.
- **Unknown:** Missing information that may change the decision.
- **Verified defect:** Reproducible failure with direct evidence.
- **Hypothesis:** Falsifiable explanation or proposed mechanism.
- **Primary metric:** Metric used for the experiment's main decision; not necessarily a platform Primary conversion action.
- **Guardrail metric:** Metric that protects against unacceptable downstream harm.
- **Stop condition:** Predefined condition for ending or containing a test.
- **Decision rule:** Predefined interpretation leading to ship, iterate, reject, or inconclusive.

### Marketing operating knowledge

Use `KNOWLEDGE-TAXONOMY.md` for the full contract and artifact metadata. The short definitions below prevent common category errors:

- **Principle:** Durable rule or constraint governing decisions.
- **Strategy:** Directional choice about where to compete, for whom, why, and how resources are allocated.
- **Framework:** Structured lens or decision map; it organizes reasoning but does not prove an outcome.
- **Model:** Simplified representation, relationship, or formula; expose variables and assumptions.
- **Methodology:** Named way of solving a class of problems with an evidence standard and decision rule.
- **Process:** Ordered repeatable workflow with inputs, outputs, owners, and handoffs.
- **Playbook / SOP:** A process adapted to a recurring business or scenario context.
- **Pattern:** Recurring shape in observed evidence; it is not automatically causal.
- **Hypothesis:** Falsifiable explanation or proposed mechanism.
- **Tactic:** Specific action selected to advance a strategy.
- **Technique:** Method for executing a tactic or process step.
- **Template:** Reusable structure for producing an artifact.
- **Checklist / QA:** Completeness and validation control.
- **Best practice:** Evidence-backed default within a defined scope; not a guarantee.
- **Heuristic:** Practical shortcut under uncertainty; label its confidence, scope, and override condition.
- **Guardrail / policy:** Limit that protects against unacceptable downside.

## Marketing OS Knowledge Taxonomy

The Marketing OS uses these terms as distinct operating layers. They are related, but they are not synonyms. Classify a deliverable by its primary purpose and state any secondary layers it contains.

### The operating stack

```text
Principles and definitions
        ↓
Strategy
        ↓
Frameworks and models
        ↓
Methodology
        ↓
Process / playbook / SOP
        ↓
Tactics and techniques
        ↓
Templates and checklists
        ↓
Measurement, experiments, and feedback
        ↓
Patterns and revised heuristics
```

The order is a dependency guide, not a mandatory writing format. A single skill can contain several layers, but the response must name the layer driving the decision.

### Definitions and decision boundaries

| Type | Meaning | Marketing example | Evidence rule |
|---|---|---|---|
| **Principle** | Durable rule or constraint that governs decisions | Protect the primary business outcome; do not call ROAS profit | State as a governance rule; revise only deliberately |
| **Definition / standard** | Contract for what a term, metric, or state means | Net revenue includes refunds under the client's stated source definition | Record source, scope, and included costs/stages |
| **Strategy** | Directional choice about where to compete, for whom, why, and how resources are allocated | Acquire profitable new customers while protecting branded demand | Tie to a business outcome, constraints, and trade-offs |
| **Framework** | Structured lens or decision map | Demand → auction → click → site → outcome decomposition | Explains how to reason; does not prove a result |
| **Model** | Simplified representation, relationship, or formula | Revenue = traffic × conversion rate × AOV | Show variables, assumptions, and limits |
| **Methodology** | Named way of solving a class of problems | Evidence-led audit, JTBD research, controlled experimentation | State steps, evidence standard, and decision rule |
| **Process** | Ordered repeatable workflow | Intake → measure → diagnose → plan → approve → test → verify | State owner, inputs, outputs, handoffs, and status |
| **Playbook / SOP** | Process adapted to a recurring context or scenario | Ecommerce Shopping diagnostic playbook | Include prerequisites, exceptions, escalation, and QA |
| **Pattern** | Recurring shape in observed evidence | Frequency rises while outbound CTR falls | Pattern is not causality; name source, scope, and sample |
| **Hypothesis** | Falsifiable explanation or proposed mechanism | Creative fatigue may be reducing qualified response | Include disconfirming evidence and test design |
| **Tactic** | Specific action chosen to advance a strategy | Add a PMax negative keyword or launch a new creative angle | State target, expected effect, risk, and approval |
| **Technique** | Method for executing one tactic or process step | Search-term mining with intent and economic thresholds | Explain how it works and when it fails |
| **Template** | Reusable structure for producing an artifact | Audit, creative brief, or experiment brief | Keep placeholders explicit; do not imply completed work |
| **Checklist / QA** | Completeness and validation control | Pre-launch event and claim checklist | Must test observable invariants, not only wording |
| **Best practice** | Evidence-backed default that is broadly useful in a defined scope | Verify post-payment purchase events before bidding on them | Scope, source, date, and exceptions are required |
| **Heuristic** | Practical shortcut used under uncertainty | Do not pause a keyword solely because a small sample has no conversion | Label as heuristic; never present as a guarantee |
| **Guardrail / policy** | Limit that protects against unacceptable downside | No budget increase while measurement integrity is unknown | State trigger, owner, and escalation or stop action |

### How to classify a response

1. Identify the decision or business outcome.
2. Select one primary type from the table. Add secondary types only when they materially help the user.
3. Separate claims from actions: a pattern or model is not a recommendation; a tactic is not a strategy.
4. Label evidence as `observed`, `calculated`, `experimentally observed`, `inferred`, `assumed`, or `unknown` using `GLOSSARY.md`.
5. For best practices and heuristics, state scope, confidence, freshness, and the condition that would override them.
6. For a live recommendation, state authorization, rollback/stop condition, and exact status.

### Artifact metadata contract

When creating or materially revising an OS artifact, record the following fields. Use templates/knowledge-artifact.md when a standalone artifact needs a header.

```yaml
artifact_type: strategy | framework | model | methodology | process | playbook | sop | pattern | hypothesis | tactic | technique | template | checklist | best-practice | heuristic | policy | standard
decision: the decision or business outcome this supports
scope: channel, funnel stage, market, business model, and exclusions
owner: the skill or role accountable for the final interpretation
inputs: required evidence or prerequisites
evidence_status: observed | calculated | officially-documented | account-visible | experimentally-observed | inferred | assumed | unknown
confidence: high | medium | low | not-assessed
freshness: stable | 180-days | 90-days | 30-days | live-check
dependencies: measurement, economics, platform access, approval, or other prerequisites
authorization: read-only | draft | approval-required | live-verified
rollback_or_stop: containment or test stopping condition when action is involved
```

Metadata is a decision aid, not a substitute for the evidence or the artifact itself. Do not mark an artifact `live-verified` without matching verification.

### OS mapping

- `AGENTS.md`, `PLATFORM-CURRENCY.md`, and policies are principles, standards, and governance.
- `GLOSSARY.md` contains definitions and metric contracts.
- `frameworks/` contains frameworks and models.
- `SKILL.md` files contain methodologies, decision rules, and QA.
- `playbooks/` contains processes, SOP-like workflows, and scenario adaptations.
- `references/` contains techniques, platform detail, patterns, and scoped best practices.
- `templates/` contains reusable output structures and checklists.
- `tests/evaluations/` validates whether the layers are being used correctly.

## Platform Currency Contract

Marketing platforms change faster than stable marketing principles. This contract keeps the Marketing OS current without pretending to know undocumented auction or recommendation-system internals.

### Evidence states

- **Officially documented:** supported by a current first-party Google or Meta source, with a verification date.
- **Account-visible:** directly observed in the relevant account or interface, with account scope and observation date.
- **Experimentally observed:** supported by a defined test or controlled comparison; state design and limitations.
- **Inferred:** a plausible explanation supported by evidence but not isolated or officially documented.
- **Unknown:** not verified, unavailable, or undisclosed.

Never describe a rumor, community report, correlation, or platform recommendation as an algorithm change. Separate product availability, default behavior, eligibility, recommended practice, and measured business impact.

### Freshness gates

| Change class | Examples | Maximum registry age | Required action when stale |
|---|---|---:|---|
| High-change | AI/automation features, campaign creation defaults, bidding or audience controls, reporting availability, experiments, interface labels | 30 days | Recheck official documentation before making a current-state claim or configuration recommendation. Confirm account visibility before an account-specific plan. |
| Medium-change | Setup workflows, policy wording, attribution options, standard reports | 90 days | Recheck first-party documentation when the detail affects the decision. |
| Stable concept | Economics, evidence states, causal inference, experiment design | 180 days | Review for conceptual or regulatory changes; do not replace with platform slogans. |

Always perform a live first-party check regardless of age when the user asks for the latest/current behavior, a documented capability may determine spend or measurement, the account contradicts the registry, or a live mutation is being proposed.

### Source rules

1. Prefer first-party product help, developer documentation, release notes, and account-visible evidence.
2. Record the source URL, page title, verification date, and the exact claim supported.
3. Treat marketing claims and platform case studies as vendor evidence, not guaranteed outcomes.
4. Do not infer access from documentation: rollouts can depend on account, country, objective, inventory, permissions, or experiment enrollment.
5. Preserve the stable strategic concept in `GLOSSARY.md`; map the current interface label separately.
6. When a material label, control, eligibility rule, or reporting capability changes, update the relevant platform registry, skill decision rules, evaluation case, and `CHANGELOG.md` together.

### Response contract

For a platform-current answer, report:

1. **Verified as of:** date and scope.
2. **Officially documented:** supported product behavior.
3. **Account-visible:** what was actually observed, or `not checked`.
4. **Business implication:** a recommendation, distinct from the platform claim.
5. **Unknowns:** undisclosed mechanics, rollout uncertainty, or missing account evidence.
6. **Status:** advice only, draft, saved, published, processing, or live-verified.

The OS can be current to its verification standard; it cannot guarantee knowledge of undisclosed algorithms or changes released after the latest verification.

## Artifact Ownership

Every substantial active marketing artifact must have an identifiable owner, a discoverable loading path, a declared evidence state, and a validation rule. Existence in the repository alone does not make a file part of the operating system.

This registry records the ownership state of root-level `frameworks/`, `playbooks/`, `templates/`, and `workflows/`. `scripts/validate-skill-architecture.sh` enforces it: a **new** file added to those directories without an entry here fails validation. Existing entries marked `migration-debt` are reported, not failed — they are tracked and eliminated release by release.

Status definitions:

- **owned** — a canonical skill loads or governs the artifact.
- **consumed** — no skill loads it directly; a documented workflow, export, or human process uses it.
- **migration-debt** — active knowledge with no owner and no loading path. Must be assigned an owner, folded into a skill reference, or archived.
- **archived** — retained for history, excluded from active retrieval.

### Frameworks

| Artifact | Status | Owner or consumer |
|---|---|---|
| `scaling-proof-standard.md` | owned | `$optimization-scaling` |
| `scale-readiness.md` | owned | `$optimization-scaling` |
| `marginal-economics.md` | owned | `$optimization-scaling` |
| `constraint-identification.md` | owned | `$optimization-scaling` |
| `controlled-scaling.md` | owned | `$optimization-scaling` |
| `scaling-mode-selector.md` | owned | `$optimization-scaling` |
| `portfolio-allocation.md` | owned | `$optimization-scaling` |
| `google-ads-full-stack.md` | owned | `$google-ads` (linked from SKILL.md) |
| `meta-ads-full-stack.md` | owned | `$meta-ads` (linked from SKILL.md) |
| `creative-strategy.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `shopify-cro.md` | owned | `$cro` (linked from SKILL.md) |
| `measurement-and-evidence.md` | owned | `$tracking-measurement` (linked from SKILL.md) |
| `experimentation.md` | owned | `$tracking-measurement` (linked from SKILL.md) |
| `decision-prioritization.md` | owned | `$marketing-router` (linked from SKILL.md) |
| `copywriting-frameworks.md` | archived | Twenty-line structure list, no evidence discipline; moved to `docs/archive/legacy-skill-stubs/copywriting-frameworks.flat.md`, superseded by `$copywriting` |
| `seo-framework.md` | archived | Ten-line phase list, no evidence discipline; moved to `docs/archive/legacy-skill-stubs/seo-framework.flat.md`, superseded by `$seo` |

### Playbooks

| Artifact | Status | Owner or consumer |
|---|---|---|
| `google-ads-scaling.md` | owned | `$optimization-scaling` |
| `meta-ads-scaling.md` | owned | `$optimization-scaling` |
| `cross-channel-scaling.md` | owned | `$optimization-scaling` |
| `ecommerce-scaling.md` | owned | `$optimization-scaling` |
| `lead-generation-scaling.md` | owned | `$optimization-scaling` |
| `creative-scaling.md` | owned | `$optimization-scaling` |
| `de-scaling-recovery.md` | owned | `$optimization-scaling` |
| `google-ads-audit.md` | owned | `$google-ads` (linked from SKILL.md) |
| `meta-ads-audit.md` | owned | `$meta-ads` (linked from SKILL.md) |
| `cross-channel-diagnostic.md` | owned | `$performance-diagnostics` (linked from SKILL.md) |
| `ecommerce.md` | owned | `$cro` (linked from SKILL.md) |
| `ecommerce-growth.md` | owned | `$cro` (linked from SKILL.md) |
| `lead-generation.md` | owned | `$icp-jtbd` (linked from SKILL.md) |
| `README.md` | consumed | Directory index |

### Templates

| Artifact | Status | Owner or consumer |
|---|---|---|
| `scale-readiness.md` | owned | `$optimization-scaling` |
| `scaling-economics.md` | owned | `$optimization-scaling` |
| `scaling-hypothesis.md` | owned | `$optimization-scaling` |
| `scaling-experiment.md` | owned | `$optimization-scaling` |
| `scaling-change-plan.md` | owned | `$optimization-scaling` |
| `scaling-decision-log.md` | owned | `$optimization-scaling` |
| `scaling-portfolio-review.md` | owned | `$optimization-scaling` |
| `de-scaling-plan.md` | owned | `$optimization-scaling` |
| `recovery-verification.md` | owned | `$optimization-scaling` |
| `knowledge-artifact.md` | consumed | `KNOWLEDGE-TAXONOMY.md` |
| `campaign-brief.md` | owned | `$google-ads / $meta-ads` (linked from SKILL.md) |
| `creative-brief.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `landing-page-review.md` | owned | `$cro` (linked from SKILL.md) |
| `experiment-plan.md` | archived | Weaker duplicate of `experiment.md`; moved to `docs/archive/legacy-skill-stubs/experiment-plan.flat.md` |
| `experiment.md` | owned | `$tracking-measurement` (linked from SKILL.md) |
| `audit.md` | owned | `$performance-diagnostics` (linked from SKILL.md) — canonical audit format |
| `audit-template.md` | archived | Weaker duplicate of `audit.md`; moved to `docs/archive/legacy-skill-stubs/audit-template.flat.md` |
| `marketing-audit.md` | owned | `$icp-jtbd` (linked from SKILL.md) — distinct scope: business/market-level, not a channel audit |
| `performance-report.md` | owned | `$marketing-reporting` (linked from SKILL.md) — canonical report format |
| `reporting-template.md` | archived | Weaker duplicate of `performance-report.md`; moved to `docs/archive/legacy-skill-stubs/reporting-template.flat.md` |
| `strategy-template.md` | owned | `$marketing-router` (linked from SKILL.md) |
| `README.md` | consumed | Directory index |

### Workflows

| Artifact | Status | Owner or consumer |
|---|---|---|
| `google-ads-optimization.md` | owned | `$google-ads` (linked from SKILL.md) |
| `meta-ads-optimization.md` | owned | `$meta-ads` (linked from SKILL.md) |
| `creative-testing.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `cro-improvement.md` | owned | `$cro` (linked from SKILL.md) |
| `reporting-analysis.md` | owned | `$marketing-reporting` (linked from SKILL.md) — data-to-decision workflow sequence |
| `README.md` | consumed | Directory index |

### Duplication resolved in v1.6.0

`audit-template.md` and `experiment-plan.md` were weaker duplicates — no evidence states, raw platform metrics with no profitability caveat — and were archived. `audit.md` and `experiment.md` are canonical and now owned. `marketing-audit.md` was not a duplicate: business/market-level scope distinct from a channel audit. It is now owned by `$icp-jtbd`.

### Migration rule

When migration debt is cleared, the artifact must either become a `references/` file under its owning skill, or remain a root artifact explicitly linked from that skill's `SKILL.md` and recorded here as `owned`. An artifact that cannot be assigned an owner is archived.

### v1.5.0 addition

`$retention-economics` (new skill, four references) and `optimization-scaling/references/budget-and-outcome-pacing.md` (new reference under the existing owner) are both owned at creation and require no entry here — the ownership rule applies to root `frameworks/`, `playbooks/`, `templates/`, and `workflows/`, not to skill-internal references, which are owned by construction.
