# Canonical Marketing Glossary

This glossary defines Marketing OS terminology. Platform interface labels may change; preserve the strategic concept and map the current product label explicitly. When a client's source system uses a different definition, record that definition before comparing metrics.

## Commercial outcomes

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

## Measurement and causality

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

## Audience, journey, and research

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

## Paid media and creative

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

## Lead lifecycle

Use the client's actual CRM stages, then map them where applicable:

`inquiry -> lead -> contacted lead -> qualified lead -> sales-qualified opportunity -> appointment or proposal -> closed-won customer -> realized revenue`

Define qualification, stage-entry rules, date basis, and value basis before comparing CPL, cost per qualified lead, pipeline, close rate, or CAC.

## Optimization and scaling

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

## Evidence and experimentation

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

## Marketing operating knowledge

Use [`KNOWLEDGE-TAXONOMY.md`](KNOWLEDGE-TAXONOMY.md) for the full contract and artifact metadata. The short definitions below prevent common category errors:

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
