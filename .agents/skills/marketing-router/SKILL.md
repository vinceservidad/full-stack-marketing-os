---
name: marketing-router
description: Route ambiguous or multi-discipline marketing requests to the smallest useful set of Marketing OS skills when a task spans business-level growth planning, channels, funnel stages, activation, retention, diagnosis, operations, commercial decisions, or deliverables.
---

# Marketing Router

Turn the request into a bounded plan, select the minimum skills needed, and appoint one owner for the final response.

Use [`KNOWLEDGE-TAXONOMY.md`](../../../KNOWLEDGE-TAXONOMY.md) when the request asks for a strategy, framework, model, methodology, process, playbook, pattern, tactic, technique, template, best practice, or heuristic. Name the primary knowledge type in the response.

## Route

1. Identify the business outcome, business model, funnel/journey stage, timeframe, market, channel, and requested action.
   Keep business strategy, funnel/journey stage, awareness level, audience temperature, activation state, retention state, and lifecycle stage distinct.
2. Classify intent: `audit`, `diagnose`, `plan`, `create`, `optimize`, `report`, `operate`, `activate`, or `retain`.
3. Classify risk: read-only analysis; reversible draft; external mutation; spend, tracking, offer, pricing, activation-journey, retention/customer-state, or revenue-critical mutation.
4. Select one primary skill and only supporting skills that answer a distinct dependency.
5. Before a substantial audit, business-level growth strategy, diagnosis, offer/pricing/activation/retention decision, scaling decision, recurring mutating loop, or any live implementation, confirm scope, evidence state, metric definitions, and authorization are recorded. Route to `$marketing-intake` when they are not; it owns the response until the evidence state is known.
6. When `.agents/marketing-context.md` exists in the active project, use only the decision-relevant sections as shared context. Do not let the summary upgrade evidence or override a newer specialist artifact.
7. State missing inputs that could reverse the decision. Continue with labeled assumptions when safe.
8. When the request says current, latest, new, AI, algorithm, rollout, or interface—or depends on a fast-changing platform control—route to the channel skill and enforce `PLATFORM-CURRENCY.md` before accepting the stored label or behavior.
9. Classify the requested deliverable by its primary knowledge type; use secondary types only when they change how the artifact should be used or validated.

## Skill map

- Business-level growth strategy, integrated marketing plan, strategic priorities, growth constraint or constraint set, growth opportunity portfolio, channel-role decisions, sequencing, learning roadmap, or “where should we focus?”: `$growth-strategy`.
- Recurring cross-skill operating loops, condition watches, state/checkpoint design, idempotency, approval gates, execution handoffs, verification, escalation, or retirement: `$marketing-operations`.
- Commercial offer, promised outcome, core deliverable, value architecture, bundle, risk reversal, real urgency/scarcity, or offer diagnosis: `$offer-strategy`.
- Base price, value metric, package/tier architecture, payment model, discount architecture, willingness-to-pay evidence, price-change testing, or existing-customer price migration: `$pricing-monetization`.
- First meaningful value, activation definition, post-conversion path-to-value, time-to-value, activation friction, onboarding-to-value diagnosis, or activation intervention/testing: `$activation`.
- Retention/churn/lapse reason diagnosis, cancellation save, failed-payment recovery strategy, repeat-purchase/renewal intervention, lapse prevention, or win-back strategy: `$retention-strategy`.
- Google campaign structure, queries, Shopping/PMax, bids, or budgets: `$google-ads`.
- Meta structure, audiences, delivery, placements, or ads: `$meta-ads`.
- Angles, hooks, concepts, formats, briefs, or creative tests: `$creative-strategy`.
- Landing page, product page, pre-conversion form, checkout, or persuasion friction before the conversion boundary: `$cro`.
- Metric change, spend/sales anomaly, or causal triage: `$performance-diagnostics`.
- Event integrity, attribution differences, conversion architecture, source reconciliation, incrementality testing, causal evidence grading, experiment validity, experiment learning, or experiment backlog governance: `$tracking-measurement`.
- Interviews, reviews, surveys, customer language, objections, or evidence synthesis: `$customer-research`.
- Priority segments, buying situations, buyer roles, Jobs-to-be-Done, competitor landscape, alternatives, or competitive intelligence for positioning decisions: `$icp-jtbd`.
- Cross-channel executive report, recurring reporting cadence, or stakeholder scorecard combining findings already produced elsewhere: `$marketing-reporting`.
- Organic search visibility, ranking, content strategy, or technical SEO health: `$seo`.
- Email, lifecycle, website, sales-page, long-form, or brand copywriting: `$copywriting`.
- Email or lifecycle program strategy — segmentation, trigger logic, cadence, deliverability: `$lifecycle-marketing`.
- YouTube video ad format, targeting, or view-through measurement fit: `$youtube-ads`.
- TikTok native creative fit, Spark Ads versus in-feed, targeting breadth, or creative-fatigue cadence: `$tiktok-ads`.
- LinkedIn account-based or firmographic targeting, format selection, Lead Gen Forms, or B2B cost-structure economics: `$linkedin-ads`.
- Influencer or creator partnership vetting, compensation structure, usage rights, or disclosure compliance: `$influencer-marketing`.
- Affiliate or partner program commission structure, attribution integrity, or fraud/brand-bidding screening: `$affiliate-marketing`.
- Organic (unpaid) social content strategy, cadence, or algorithm-distribution fit: `$organic-social`.
- Programmatic display/video buying, supply-path optimization, or inventory verification and fraud screening: `$programmatic`.
- Media relations, pitch strategy, or crisis-communications response: `$public-relations`.
- Scale readiness, marginal economics, budget/coverage expansion, paid-media portfolio allocation, de-scaling, recovery, or budget/outcome pacing within an approved plan: `$optimization-scaling`.
- Undefined scope, unclear data provenance, missing economics, ambiguous conversion/lifecycle/activation/retention definitions, uncertain access, unclear shared context, or an unclear authorization boundary: `$marketing-intake`.
- Customer lifetime value, payback period, cohort retention/churn measurement, repeat/renewal economics, or lead-to-revenue maturation: `$retention-economics`.

Common compositions:

- Build a marketing/growth plan: growth strategy owns the business objective, current constraint structure, opportunity set, strategic bets, non-priorities, sequence, and learning roadmap; specialist skills own the decisions inside each chosen workstream; marketing operations may own recurring execution/review once the strategy is approved; reporting owns stakeholder summaries.
- “Where should we focus next?”: growth strategy owns the cross-business priority decision; performance diagnostics joins when a recent metric change must be localized; intake joins when economics, definitions, or evidence state are unclear; a channel skill joins only when its feasibility is a distinct dependency.
- New channel opportunity: growth strategy owns whether the channel deserves a strategic role versus existing opportunities; ICP/JTBD supplies audience/buying evidence; the channel skill owns platform-specific feasibility/execution; tracking owns causal measurement; a competitor using the channel is not proof that it is strategically attractive.
- Recurring weekly/monthly account operation: marketing operations owns trigger/cadence, run state, specialist handoffs, approval gates, verification, and run history; each channel/diagnostic/scaling skill keeps its substantive decision; marketing reporting owns the communication artifact when a report is also required.
- Condition watch such as “alert when performance crosses X”: marketing operations owns the recurring check, condition state, dedupe/re-arm logic, and escalation; the domain skill defines whether X is decision-valid; a runtime/tool must actually be configured before the loop is described as scheduled or active.
- Improve an offer that is not converting: offer strategy owns the commercial proposition; customer research and ICP/JTBD supply buying evidence; pricing joins only if the exchange structure is a distinct suspected constraint; CRO joins only if pre-conversion page/journey friction is distinct; copywriting expresses approved commercial terms rather than inventing them.
- Offer + pricing redesign: offer strategy owns the promised outcome, deliverable, bundle, proof, and risk reversal; pricing-monetization owns base price, value metric, tiers/packages as commercial exchange structures, payment model, discounts, and migration; tracking owns any causal test validity.
- Price increase/decrease: pricing-monetization owns the price decision, scenario economics, customer treatment, test/rollout, and exact commercial state; retention economics supplies mature renewal/cohort effects; retention strategy joins only when the price change creates a distinct retention intervention question; offer strategy joins only if the underlying proposition also changes; CRO/copywriting present approved terms rather than deciding them.
- Low signup-to-value or purchase-to-value performance: activation owns whether a distinct activation stage exists, the first meaningful value definition, denominator/window, path-to-value, barrier diagnosis, and intervention hypothesis; tracking owns event integrity and causal validity; lifecycle owns communication triggers/cadence; copywriting owns wording; ICP/JTBD joins when poor-fit acquisition is plausible; CRO joins only for bounded surface UX within its scope.
- Onboarding emails intended to improve activation: activation owns the value event and journey outcome; lifecycle marketing owns segmentation/trigger/cadence/suppression; copywriting owns the message; tracking owns incrementality or experiment validity.
- “What is our aha moment?”: activation owns and treats candidate events as hypotheses unless evidence supports them. Do not invent a single event from category convention or correlation alone.
- Activation rate fell: activation owns the journey diagnosis if the metric definition and instrumentation are stable; tracking joins when event integrity or definition changed; performance diagnostics may join for broader anomaly triage; ICP/JTBD joins when acquisition mix/fit changed materially.
- Activation improved but retention did not: activation owns the first-value result; retention economics owns mature repeat/renewal/churn measurement; retention strategy owns any decision about why customers still fail to continue and what intervention should be tested; tracking owns causal interpretation.
- Churn increased / repeat purchase fell: retention strategy owns state/reason diagnosis and intervention strategy; retention economics supplies cohort/maturity/economic evidence; tracking joins if measurement or causal interpretation is uncertain; activation joins if failure to reach first value is a plausible upstream cause.
- Cancellation save program: retention strategy owns reason classification, eligibility, intervention hypothesis, customer-choice boundary, and durable-save definition; lifecycle owns communication triggers/cadence; pricing owns any discount/plan/payment-model change; retention economics measures realized economics; tracking owns causal validity.
- Failed-payment recovery: retention strategy owns involuntary-loss classification and recovery objective; lifecycle owns notifications; billing/payment implementation stays with the actual system owner; pricing joins only for payment-model changes; a recovered charge is not durable retention until the required continuation window is observed.
- Win-back campaign: retention strategy owns genuine-lapse eligibility, whether the original loss reason is resolved, intervention rationale, and retained-value outcome; lifecycle owns contact eligibility/trigger/cadence/suppression; copywriting owns message; pricing owns commercial incentives; tracking owns incrementality.
- Offer + paid creative: offer strategy owns the commercial proposition; creative strategy translates it into angle, hook, concept, proof treatment, and CTA; channel skill supplies platform constraints.
- Competitive landscape for positioning: ICP/JTBD owns the alternative set and strategic implications; customer research joins only when buyer/review evidence is needed; SEO joins only when current organic-search competition is decision-relevant. Visible competitor tactics and prices remain context, not proof of performance or optimal pricing.
- Completed experiment or test archive: tracking and measurement owns validity classification, evidence level, scoped learning, and transfer status; the domain skill owns the resulting business action. A single valid result may support a local decision without becoming a universal best practice.
- Spend rose and sales fell: performance diagnostics owns; channel skill supports; CRO joins only if landing evidence suggests a site issue.
- Produce Meta concepts: creative strategy owns; Meta Ads supplies placement and delivery constraints.
- Clicks without conversions: performance diagnostics owns; channel skill and CRO support; flag measurement integrity as an unresolved dependency when needed.
- Define a new audience and message: ICP/JTBD owns the segment decision; customer research supplies evidence; creative strategy translates it into tests.
- Platforms disagree on revenue: tracking and measurement owns; performance diagnostics joins only if the business outcome itself changed.
- Is this channel actually incremental: tracking and measurement owns method selection and evidence grading; the channel skill supplies account controls; optimization and scaling consumes the result and never substitutes attribution for it.
- Is this customer base or channel worth scaling on a lifetime basis: retention economics owns the lifetime value and payback model; optimization and scaling owns the paid-media scaling decision and applies its own proof standard to the model's output; growth strategy owns the broader question of whether scaling that channel is the highest-priority business opportunity.
- Audit request with no economics, scope, or source of truth supplied: intake owns until the evidence state is recorded; the channel skill then owns the audit itself.
- Cross-channel executive report requested: reporting owns combining findings already produced by other skills; it does not perform the underlying audit, diagnosis, economics analysis, or growth-priority decision itself. If the recurring process also coordinates decisions/actions with persistent state, marketing operations owns that loop layer.
- Email or lifecycle sequence needed end to end: lifecycle marketing owns segmentation, triggers, cadence, suppression, and deliverability; copywriting owns the words for each piece; activation owns the first-value journey when that is the sequence's target; retention strategy owns retention/recovery/win-back reason and eligibility when that is the target; tracking and measurement owns any incrementality claim.
- YouTube campaign requested: YouTube ads owns format, targeting, and measurement fit; Google Ads owns account and bidding mechanics since YouTube runs through the same platform; creative strategy owns concept and hook development if the video creative itself needs work.
- TikTok campaign requested: TikTok ads owns native creative fit, format choice, and cadence; creative strategy owns concept and hook development; optimization and scaling's creative-capacity gate governs when refresh cadence becomes a scaling constraint.
- LinkedIn campaign requested: LinkedIn ads owns targeting approach, format, and cost-structure economics; ICP/JTBD supplies buyer-role and buying-committee evidence; retention economics owns the lead-to-revenue maturity read; creative strategy or copywriting supply creative and message as needed.
- Influencer partnership requested: influencer marketing owns vetting, compensation, usage rights, and disclosure; ICP/JTBD supplies buyer-fit evidence; tracking and measurement grades any performance claim; creative strategy supports if the business needs input on creative direction, though creator editorial control is typically retained by the creator.
- Affiliate program requested: affiliate marketing owns commission structure, attribution-mechanism documentation, and fraud/brand-bidding screening; tracking and measurement owns any incrementality claim about the program's true contribution; a partner who is also a content creator follows influencer marketing's disclosure discipline in addition to affiliate-link disclosure.
- Organic content requested for paid amplification: organic social owns content and distribution strategy; the paid boost or Spark Ad decision routes to the owning platform skill (`$meta-ads`, `$tiktok-ads`, `$linkedin-ads`, `$youtube-ads`).
- Programmatic campaign requested: programmatic owns buying method, supply-path screening, and verification; creative strategy or copywriting supply creative and message; tracking and measurement grades any view-through or causal claim.
- Media outreach or crisis response requested: public relations owns newsworthiness assessment, media-list fit, and crisis discipline; tracking and measurement grades any resulting business-outcome claim; a public statement with real legal exposure requires flagged legal review this skill does not itself provide.
- An escalating pattern of public engagement on organic social is identified: organic social owns routine community management; public relations owns crisis communications once it escalates beyond routine engagement.
- Scale campaigns or allocate more paid-media budget: optimization and scaling owns readiness, marginal economics, and the controlled scaling step; growth strategy joins only when the business-level question is whether paid-media scaling should outrank other growth opportunities.

## Capability boundary

Route only to a skill that exists. Check [`CAPABILITY-REGISTRY.md`](../../../CAPABILITY-REGISTRY.md) before answering a request outside the skill map. Boundaries are task-level, not discipline-level: a discipline can be partly governed and partly unsupported.

- Growth strategy versus specialist strategy: `$growth-strategy` owns the integrated business-level marketing direction, current constraint structure, opportunity portfolio, priorities, sequence, non-priorities, and learning roadmap. Specialist skills retain the technical/commercial decisions inside each chosen workstream. A marketing plan does not authorize or override specialist actions.
- Growth strategy versus optimization/scaling: `$growth-strategy` decides whether expanding a proven paid-media system is a priority relative to other growth opportunities. `$optimization-scaling` decides whether that paid-media system is ready for more investment and how to expand it through proof, marginal economics, capacity, guardrails, and rollback rules. Growth Strategy does not set live scaling budgets.
- Analytics: tracking architecture, event integrity, and attribution differences belong to `$tracking-measurement`; performance analysis, segmentation, and anomaly diagnosis to `$performance-diagnostics`; allocation and marginal evidence to `$optimization-scaling`. Business-intelligence engineering, pipeline or warehouse design, and dashboard implementation have no governed specialist.
- Reporting versus operations: a bounded single-channel or single-decision report is owned by the skill that owns the underlying decision. Cross-channel executive reporting, recurring reporting cadence, and stakeholder scorecards are owned by `$marketing-reporting`. Recurring operational coordination — trigger/cadence, state/checkpoints, condition watches, approval gates, execution handoffs, verification, duplicate prevention, escalation, and retirement — is owned by `$marketing-operations`. Budget and outcome pacing remain owned by `$optimization-scaling`; forecasting outside a strategy scenario or pacing reforecast has no governed specialist.
- CRO versus activation: `$cro` owns landing/product pages, forms, checkout, and persuasion friction leading to the conversion boundary. `$activation` owns whether meaningful value occurs after conversion, the definition of that value event, the path to it, time-to-value, and post-conversion activation diagnosis. A bounded post-conversion surface may need CRO support, but CRO does not own the activation definition.
- Activation versus retention strategy: `$activation` owns first meaningful value and the journey to it. `$retention-strategy` owns why already-converted/activated customers fail to continue, renew, repurchase, or return and which cause-matched intervention should be tested. Activation failure may be an upstream retention cause without making the two decisions identical.
- Retention strategy versus lifecycle marketing: `$retention-strategy` owns retention state/reason, eligibility, intervention objective, and durable-save/recovery/win-back definition; `$lifecycle-marketing` owns communication segmentation, triggers, cadence, suppression, and deliverability supporting that intervention. A message open, click, or save-button acceptance is not durable retention by default.
- Retention strategy versus retention economics: `$retention-strategy` owns why customers are at risk/lost and what intervention should be tested; `$retention-economics` owns realized/predictive cohort retention, churn, repeat, LTV, and payback measurement. Neither may infer causality from an exposed/unexposed cohort difference without `$tracking-measurement`.
- Copywriting: paid-ad hooks, angles, concepts, and creative briefs belong to `$creative-strategy`; conversion-page copy evaluation to `$cro`; email, lifecycle, website, sales-page, long-form, and brand copywriting to `$copywriting`. Do not route general copywriting to `$creative-strategy` or `$cro` outside their stated scope now that `$copywriting` owns the rest.
- Offer strategy versus pricing: `$offer-strategy` owns the proposition, promised outcome, core deliverable, bundle/service value architecture, proof requirements, risk reversal, and real urgency/scarcity. `$pricing-monetization` owns base/realized price, value metric, pricing packages/tiers, payment model, discount architecture, willingness-to-pay evidence, and price-change migration/testing. A tier can involve both skills: offer owns what value is delivered; pricing owns how that differentiated value is charged and structured commercially.
- Pricing versus retention economics: `$pricing-monetization` decides the exchange structure using current evidence and modeled scenarios; `$retention-economics` measures realized or predictive cohort lifetime value, renewal, churn, and payback. Pricing may consume retention evidence but may not relabel modeled LTV as realized pricing proof.
Every previously listed advertising and distribution channel is governed. If a genuinely new discipline arrives that is not in `CAPABILITY-REGISTRY.md`, declare it unsupported per the handling method there rather than substituting an adjacent skill.

When no governed specialist covers the primary discipline: do not silently substitute an adjacent skill; name the missing capability; apply platform-agnostic frameworks only where they genuinely address a distinct part of the request; label platform-specific guidance as ungoverned and unverified by this system; never name a skill that does not exist; and state the gap in the exact-status line.

## Rules

- Do not activate every plausible skill.
- Do not route a request to a skill absent from the capability registry, and do not present a partially covered discipline as fully governed.
- Do not let a channel metric define the business outcome.
- Use “primary business outcome” for the main commercial result. Reserve “Primary conversion action” for Google Ads' action-optimization setting.
- When terms differ by platform or client, preserve the strategic concept and state the current interface or source-system label separately.
- If measurement integrity is unknown, treat platform conversion, activation, retention, or growth-constraint claims as provisional.
- For live changes, first state the exact change, expected effect, downside, rollback condition, and approval boundary.
- Never describe a draft recommendation or growth strategy as implemented.
- Never treat a generic planning framework, channel mix, 90-day horizon, or allocation ratio as evidence that a priority is correct.
- Never describe a proposed/configured price as live or verified without source-of-truth evidence.
- Never describe a proposed activation definition or launched activation intervention as proven/verified without the required evidence and observation window.
- Never describe a retention save/recovery/win-back intervention as durable or proven from acceptance, delayed cancellation, recovered payment, message engagement, or one immature cohort alone.
- Never recommend hidden cancellation, deceptive friction, consent/suppression workarounds, or repeated unwanted contact to improve retention.
- Never describe a designed recurring loop as scheduled, active, or monitoring unless its runtime state is actually verified.
- Never convert an undocumented platform “algorithm change” into a fact. Label official documentation, account observation, experimental evidence, inference, and unknowns separately.
- Do not present a pattern as causality, a heuristic as a guarantee, a tactic as a strategy, or a framework/model as proof of an outcome.
- Do not treat more spend, conversions, attributed revenue, blended ROAS, conversion rate, activation rate, retention rate, save acceptance, AOV, or ARPU alone as proof of scaling/pricing/activation/retention/growth success; require the business outcome, scoped economics/value, observation window, and relevant guardrails.
- Do not treat a Marketing Context summary as stronger evidence than the source artifact it summarizes.

## Output

Return: objective; primary knowledge type; routed skills and owner; capability status (governed, partially covered, or unsupported); evidence; missing inputs; approach; findings or deliverable; recommended next action; exact status.

## QA

Confirm routing is minimal, an owner is named, every named skill exists in the capability registry, broad business-level planning routes to `$growth-strategy`, specialist decisions remain with their owners, any capability gap is disclosed, unknowns are visible, commercial/customer value outcome is explicit, current-platform claims meet the freshness gate, shared context has not upgraded evidence, pricing/activation/retention/runtime states are not invented, cancellation/consent boundaries are preserved, and no external action is implied without authorization.