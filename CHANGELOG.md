# Changelog

Notable changes follow semantic versioning.

## [Unreleased]

### Added

- `$creative-strategy` Creative Ideation Engine: adds the owned [creative ideation workflow](workflows/creative-ideation-engine.md), [creative idea matrix](templates/creative-idea-matrix.md), and two skill references for awareness/belief/desire mapping and controlled ideation expansion. The canonical reasoning flow now connects verified research → audience situation → pain/desire/JTBD → awareness → current belief → required belief shift → angle → hook → concept → format → proof → CTA → test hypothesis while preserving evidence states and allowing account learning to override default assumptions.
- Fifteen Creative Ideation Engine evaluations plus a completed review covering fabricated customer psychology, unsupported belief shifts, false strategic diversity, cosmetic expansion, proof mismatch, uncontrolled test cells, state confusion, and quantity-over-evidence generation. Generated ideas remain hypotheses and are never treated as customer evidence.

- `$creative-strategy` reference: [static DTC creative direction and reference analysis](.agents/skills/creative-strategy/references/static-dtc-creative-direction.md) — a governed production-direction methodology for static paid creative. It requires an evidence-grounded emotional job, a visual thesis, reference analysis separated into observation versus inference, a first/second/third reading order, deliberate type-overlay specification, product and composition direction, a visual-base/text-overlay split where exact text matters, and intended-placement preflight. Reference patterns are not described as proven or copied; premium positioning requires brand-specific codes rather than generic luxury styling.
- Twelve evaluations and a required human review record covering generic prompts, emotion without audience situation, copied references, unjustified performance claims, hierarchy, typography, image-model text limits, unsupported visual proof, premium stereotypes, render validation, ownership routing, and controlled learning.
- `$copywriting` now explicitly routes static paid-ad text hierarchy to `$creative-strategy`; it continues to own longer-form, lifecycle, website, sales-page, and brand copy outside the paid-ad concept.

### Added

- `$creative-strategy` reference: [angle catalog and hook types](.agents/skills/creative-strategy/references/angle-catalog-and-hook-types.md) — a coverage checklist of common angle categories (problem/pain, desired outcome, product benefit, before-after, social proof, objection handling, comparison, founder story, education, UGC/lived-experience, trend relevance) and five hook types (problem, curiosity, outcome, contrarian, proof), distinct from the archetypes reference added previously: this one checks coverage against known categories, the archetypes reference generates novel directions. A proof hook's claim is held to the skill's existing substantiation standard — no rounded-up or invented numbers.
- `$creative-strategy` reference: [iterating from a winner](.agents/skills/creative-strategy/references/iterating-from-a-winner.md) — the skill's method covered building and launching an initial matrix but not what happens after a cell wins. Requires holding the winning angle fixed and varying exactly one further dimension per round, replication before treating a single win as durable, and routes cross-platform scaling to the owning channel skill rather than assuming an execution transfers unedited.
- `$copywriting` structure-selection reference gains a UGC narrative structure (Hook → Problem → Lived experience → Proof → CTA) alongside AIDA/PAS/FAB/BAB/Rule of One, with an explicit prohibition on fabricating a testimonial for a piece drafted in this voice.
- Both additions built after the user shared a second external framework list (attributed to ChatGPT); items already covered by the system (the initial testing sequence, PAS, AIDA, FAB, BAB, Rule of One, Schwartz awareness, the creative matrix concept) were not duplicated. The source's FBA (Feature → Benefit → Advantage) ordering was checked against this system's existing documented FAB (Feature → Advantage → Benefit) — no authoritative source settles which ordering is correct, so this is recorded as a noted variant rather than silently overwritten.
- Twelve evaluations and the required review record.



### Added

- `$creative-strategy` reference: [persuasion and behavioral principles](.agents/skills/creative-strategy/references/persuasion-and-behavioral-principles.md) — documented behavioral-science research (social proof, authority, scarcity, loss aversion, anchoring, reciprocity, commitment/consistency, unity, dual-process framing, decoy/framing effects, endowment effect) to inform angle-hypothesis generation at method step 2. Added on direct request after clarifying it as a distinct knowledge type from account-specific test evidence: a principle explains a general mechanism, it does not predict this audience's response, and every resulting angle still requires the existing test matrix before it is evidence.
- Explicit guardrail against principle-driven manipulation: fabricated scarcity, invented anchors, unearned authority, constructed identity, and manufactured loss are all rejected as substantiation failures, and a technically true but manipulative framing is flagged for human judgment rather than auto-approved by factual accuracy alone.
- Ten evaluations and the required review record.
- `$creative-strategy` reference: [strategic framing and angle archetypes](.agents/skills/creative-strategy/references/strategic-framing-and-angle-archetypes.md) — structuring methods for reaching a single clear direction (problem/insight/advantage/strategy, single-minded proposition, an explicit "we believe X will move Y because Z" hypothesis format, primal-versus-learned motivation mapping) and five angle-generation archetypes (name a shared frustration, borrow cultural relevance, create a new mental model, challenge a category norm, name an overlooked truth). Added after the user shared an external framework list; overlapping items already present in the system (Schwartz awareness stages, the concept/angle/hook/format hierarchy, PAS under `$copywriting`) were not duplicated, and the source's unverifiable "ranked by importance / what top strategists use in 2026" framing was not carried forward as fact.
- Ten more evaluations and review record for the archetypes reference.

## [1.18.0] - 2026-08-25

Adds `$public-relations`, twenty-fourth governed skill. Third and final of the unordered channel-expansion batch (organic social, programmatic, public relations), closing every channel identified as unsupported since v1.9.0.

### Added

- `$public-relations` covers media relations, pitch strategy, and crisis-communications response — earned coverage with no purchased placement, no algorithm, and no message-control guarantee. The least controllable channel in the system: a journalist or outlet retains full editorial control over the resulting story.
- Two references: crisis communications (facts confirmed kept separate from what is suspected or unknown; legal-exposure review runs in parallel with communications drafting, not after; a factually accurate partial response beats both silence and a rushed inaccurate one; after-action review is held to what was actually knowable at the time, not hindsight) and measurement and evidence limits (media mentions, share of voice, and sentiment are real signals with no reliable causal path to a business outcome absent a specific attribution design — correlated timing is capped at C1 on `$tracking-measurement`'s causal ladder, the same discipline already applied to view-through and programmatic).
- Seventeen evaluations and the required review record.
- Explicitly not a substitute for legal review of a statement with real liability exposure — identifies legal-review triggers and flags them, consistent with `$influencer-marketing`'s discipline on contract review.

### Changed

- Router routes media relations and crisis response to `$public-relations`; the "unsupported channels" line is removed entirely since every previously identified channel is now governed, replaced by a standing instruction for how a genuinely new discipline should be handled if one arrives later.
- `$organic-social`'s escalation reference is firmed up: an escalating pattern of public engagement now names `$public-relations` directly rather than conditionally.
- Capability registry: public relations moves from unsupported to governed. The Unsupported section is retained as an empty contract rather than deleted, so a future genuinely new discipline has a defined home before it's built.

### Channel-expansion arc complete

Eleven capabilities moved from unsupported or unowned to governed across ten releases (v1.9.0–v1.18.0): SEO, copywriting, email/lifecycle, YouTube, TikTok, LinkedIn, influencer, affiliate, organic social, programmatic, and public relations. Twenty-four governed skills, zero migration debt, maintained continuously since v1.9.0.

## [1.17.0] - 2026-08-25

Adds `$programmatic`, twenty-third governed skill. Second of the three unordered channel-expansion releases.

### Added

- `$programmatic` covers demand-side-platform buying across the open exchange — supply-path optimization, inventory verification, and fraud screening. Distinct from every walled-garden platform skill already built: inventory is aggregated from thousands of largely unknown sites and apps through a multi-party resale chain, where the platform itself has no direct accountability for its own supply the way Meta, TikTok, LinkedIn, or YouTube do.
- Two references: supply-path optimization (the same impression can be bought through multiple resale paths, each taking a fee; made-for-advertising sites are named as inventory that can pass basic brand-safety category filters while lacking genuine audience engagement) and verification and fraud screening (independent third-party verification required for viewability, invalid traffic, and brand safety — never the DSP's or seller's self-report alone, since the reporting party has a financial interest in favorable numbers).
- Fourteen evaluations and the required review record.

### Changed

- Router routes buying method, supply-path screening, and verification to `$programmatic`; composition rule routes view-through and causal claims to `$tracking-measurement`, consistent with `$youtube-ads`'s existing discipline.
- Capability registry: programmatic advertising moves from unsupported to governed.

### Remaining unsupported (1)

Public relations — the last item in this batch of three.

## [1.16.0] - 2026-08-25

Adds `$organic-social`, twenty-second governed skill. First of three unordered channel-expansion releases (organic social, programmatic, public relations) built together at the user's direction after the ordered priority list closed at v1.15.0.

### Added

- `$organic-social` covers unpaid, algorithmically-distributed social content: platform-native format and cadence, community management, and distribution fit. Has no bid, no budget lever, and no platform-native attribution to a business outcome — the most platform-currency-sensitive discipline in the system, since the entire distribution mechanism is an undocumented algorithm the business does not control.
- Two references: algorithm distribution fit (four evidence categories — officially documented, account-observed, industry-inferred, unknown — required for any distribution claim; "the algorithm changed" is rejected as a default explanation before competing account-specific causes are checked) and cadence and community management (cadence set from actual sustainable production capacity, not a platform-suggested benchmark; community management scales with posting volume since public engagement carries reputational weight a private support ticket does not).
- Fourteen evaluations and the required review record.

### Changed

- Router routes organic content strategy to `$organic-social`; any paid-amplification decision (boosting a post, running organic content as a paid ad) routes to the owning platform skill (`$meta-ads`, `$tiktok-ads`, `$linkedin-ads`, `$youtube-ads`).
- Capability registry: organic social moves from unsupported to governed.

### Process note

- Both references were written before being linked from `SKILL.md`, producing two orphaned-reference violations. Caught by `scripts/validate-skill-architecture.sh` before commit and fixed; consistent with the v1.13.0 process note.

## [1.15.0] - 2026-08-25

Adds `$affiliate-marketing`, twenty-first governed skill — sixth channel-expansion release, closing the ordered priority list started in v1.10.0 (email/lifecycle → YouTube → TikTok → LinkedIn → influencer → affiliate).

### Added

- `$affiliate-marketing` covers commission structure, attribution integrity, and fraud/brand-bidding screening for a performance-based publisher/partner channel. Distinct from `$influencer-marketing`: commission is directly tied to a tracked action, which structurally raises the incentive to game the tracking mechanism itself.
- Two references: attribution integrity (last-click cookie tracking structurally favors checkout-adjacent partners — coupon, cashback, loyalty — over the upper-funnel content and comparison partners that may have actually built purchase intent; documents cookie duration, cross-device gaps, and coupon-code leakage as named mechanisms) and fraud and brand-bidding detection (cookie stuffing, unrestricted branded-term bidding, and incentivized/fake traffic named with detection method; an unexplained conversion spike is a screening trigger, not a success signal).
- Fifteen evaluations and the required review record.

### Changed

- Router routes commission structure, attribution integrity, and fraud screening to `$affiliate-marketing`; composition rule routes incrementality claims to `$tracking-measurement` and layers `$influencer-marketing`'s disclosure discipline where a partner is also a content creator.
- Capability registry: affiliate and partner marketing moves from unsupported to governed.

### Remaining unsupported (3)

Organic social, programmatic, public relations — these were never part of the ordered priority list and need scoping before they're well-defined skills rather than a vague label.

## [1.14.0] - 2026-08-25

Adds `$influencer-marketing`, twentieth governed skill — fifth channel-expansion release, next in the stated priority order after LinkedIn.

### Added

- `$influencer-marketing` covers creator vetting, compensation structure, usage rights, and disclosure compliance. Unlike every paid-media skill in this system, this is a relationship and contract-based channel with no auction and no platform attribution to lean on — the central risks are audience authenticity, legal compliance, and unclear usage rights rather than delivery mechanics. Explicitly not a substitute for legal review of an actual contract.
- Two references: audience authenticity and fit (follower count is named as the weakest selection signal; authenticity assessed from several signals together — engagement-to-follower ratio against category norms, growth pattern, comment quality — none individually conclusive) and compensation structure (flat fee, commission/affiliate, gifting, and hybrid each trade cost predictability against creator incentive differently; gifting is not free and usage rights are not assumed included in a base fee).
- Sixteen evaluations and the required review record.

### Changed

- Router routes creator vetting, compensation, usage rights, and disclosure to `$influencer-marketing`; composition rule states the split with `$icp-jtbd` (buyer-fit evidence) and `$tracking-measurement` (performance-claim grading).
- Capability registry: influencer and creator marketing moves from unsupported to governed.

## [1.13.0] - 2026-08-25

Adds `$linkedin-ads`, nineteenth governed skill — fourth channel-expansion release, next in the stated priority order after TikTok.

### Added

- `$linkedin-ads` covers account-based and firmographic targeting, format selection matched to buying-committee role, Lead Gen Forms versus off-platform landing pages, and B2B cost-structure economics. Built from `$icp-jtbd` buyer-role and buying-situation evidence rather than assumed personas; lead-quality claims route through `$retention-economics`'s lead-to-revenue cohort maturity method rather than reading an immature cohort as final.
- Two references: account and firmographic targeting (account-based match rate must be confirmed, not assumed; buying-committee coverage stated explicitly rather than implied by reaching one role) and lead quality and sales cycle (Lead Gen Form and landing-page leads evaluated separately, never blended; B2B fiscal-cycle seasonality checked before attributing a change to campaign performance).
- Fifteen evaluations and the required review record.

### Changed

- Router routes LinkedIn targeting, format, and B2B economics to `$linkedin-ads`; composition rule states the four-way split with `$icp-jtbd` (buyer-role evidence), `$retention-economics` (lead-to-revenue maturity), and creative/copy support.
- Capability registry: LinkedIn advertising moves from unsupported to governed.

### Process note

- `scripts/validate-skill-architecture.sh` failed this release on an orphaned reference — `lead-quality-and-sales-cycle.md` was written but not yet linked from `SKILL.md`'s method section. Caught and fixed before commit; the validator did exactly what it exists to do.

## [1.12.0] - 2026-08-25

Adds `$tiktok-ads`, eighteenth governed skill — third channel-expansion release, next in the stated priority order after YouTube.

### Added

- `$tiktok-ads` covers native-feeling creative fit, the Spark Ads (boosting an existing organic post) versus standard in-feed decision, targeting breadth held to current platform documentation, and creative-fatigue cadence. Concept, angle, and hook development stay owned by `$creative-strategy`; this skill assesses platform fit, not underlying creative concept.
- Two references: native creative fit (repurposed horizontal video and a logo-card opening are named as common native-fit mismatches; a single strong asset is a hypothesis pending replication, not a standing rule) and creative fatigue and refresh cadence (refresh cadence is driven by the account's own observed fatigue signal — frequency, click-through, cost per result at the creative level, not campaign level — never a calendar borrowed from a slower-fatiguing platform).
- Seventeen evaluations and the required review record.

### Changed

- Router routes TikTok creative fit, format, targeting, and cadence to `$tiktok-ads`; concept/hook work to `$creative-strategy`; a capacity shortfall bearing on scaling to `$optimization-scaling`'s existing creative-capacity gate.
- `$creative-strategy` now states platform-specific creative fit is owned by the channel skill (`$tiktok-ads`, `$youtube-ads`), cross-linked.
- Capability registry: TikTok advertising moves from unsupported to governed.

## [1.11.0] - 2026-08-25

Adds `$youtube-ads`, seventeenth governed skill — second channel-expansion release, next in the stated priority order after lifecycle marketing.

### Added

- `$youtube-ads` covers paid video placement: format selection, audience targeting, and measurement fit. Runs through the Google Ads platform but is a distinct discipline from Search/Shopping/PMax, which stay owned by `$google-ads`. Does not cover organic YouTube content or channel strategy.
- Two references: format selection (skippable, non-skippable, bumper, in-feed/discovery, outstream — matched to funnel objective first, creative length second; the first five seconds carry a skippable format's entire message), and measurement fit (brand lift for awareness, view-through/assisted-conversion for consideration capped at C1–C2 absent a designed incrementality test, direct conversion tracking for response — never summed together).
- Seventeen evaluations and the required review record.

### Changed

- Router routes YouTube video advertising to `$youtube-ads`; Google Ads account and bidding mechanics for YouTube campaigns stay with `$google-ads`.
- `$google-ads` now states explicitly it does not cover YouTube's format and measurement decisions, cross-linked to `$youtube-ads`.
- Capability registry: YouTube advertising as a discipline moves from unsupported to governed.

## [1.10.0] - 2026-08-25

Adds `$lifecycle-marketing`, sixteenth governed skill — the first channel-expansion release since the original v1.1.0 audit's four priorities and the v1.2.0–v1.9.0 architecture and content-gap work.

### Added

- `$lifecycle-marketing` designs email/lifecycle program strategy: segmentation, trigger logic and fallback behavior, send cadence, and deliverability. It does not write copy (`$copywriting` does) and does not run paid acquisition — lifecycle marketing develops demand already captured, it does not generate new demand.
- Two references: segmentation and triggers (a segment must predict a meaningfully different next action or it isn't a segment; every trigger requires a documented suppression condition and a fallback for late or missing data), and deliverability (slow to damage, slow to repair — volume ramps, authentication checked before content is blamed, a spam-complaint spike is a stop condition, purchased lists refused outright).
- Seventeen evaluations and the required review record.

### Changed

- Router routes email/lifecycle program strategy to `$lifecycle-marketing`, distinct from the copy itself.
- `$copywriting` cross-links to `$lifecycle-marketing` for sequence design, reinforcing it writes words, not triggers.
- Capability registry: email and lifecycle marketing as a discipline moves from unsupported to governed. Nine channels remain unsupported: TikTok, LinkedIn, YouTube as a discipline, affiliate, influencer, organic social, programmatic, public relations.

## [1.9.0] - 2026-08-25

Adds `$copywriting`, fifteenth governed skill. Migration debt: 31 → 0.

### Added

- `$copywriting` writes and evaluates email, lifecycle, website, sales-page, long-form, and brand copy. Paid-ad hooks stay owned by `$creative-strategy`; landing/product-page conversion copy stays owned by `$cro` — this skill owns what neither of those covers.
- One reference: structure selection (AIDA, PAS, FAB, BAB, Rule of One) matched to audience awareness level rather than applied by default, with sequence-level awareness tracking across multi-piece campaigns.
- Fifteen evaluations and the required review record.
- The skill's sharpest rule: a structure organizes an argument, it does not supply evidence for it. No fabricated benchmark, testimonial, or customer quotation; customer language must trace to a `$customer-research` source; regulated claims are flagged for review rather than silently softened.

### Changed

- Router routes email, lifecycle, website, sales-page, long-form, and brand copywriting to `$copywriting`; paid-ad hooks and conversion-page copy remain with their existing owners.
- Capability registry: copywriting moves from partially covered to governed. Email/lifecycle *marketing* — strategy, automation, cadence, deliverability — remains explicitly unsupported and distinct from writing the words for a sequence.
- `README.md`'s partial-coverage disclaimer, standing since v1.2.0, is now resolved for copywriting; analytics remains the one partially covered capability.

### Removed

- `frameworks/copywriting-frameworks.md`, a twenty-line structure list with no evidence discipline or ownership boundary. Archived to `docs/archive/legacy-skill-stubs/`.

### Migration debt: zero

All 31 root artifacts identified as unowned in v1.2.0 are now owned, archived, or governed by a skill. This closes the migration-debt tracking effort started in v1.2.0.

## [1.8.0] - 2026-08-25

Adds `$seo`, fourteenth governed skill, closing the second of the two capabilities the README explicitly disclaimed since v1.2.0. Migration debt: 31 → 1.

### Added

- `$seo` audits organic visibility, technical health, and content/topic strategy, and diagnoses ranking changes, using search-console and crawl evidence rather than a third-party rank tracker or paid-media attribution language.
- Three references: technical health (crawlability, indexation, canonicalization, page experience — field data governs over lab data), content and topic strategy (intent and coverage evidence before volume, capacity-bounded plans, consolidation considered over default creation), and ranking-change diagnosis (a required order of competing explanations — algorithm update, seasonality, competitive entry, technical regression, measurement change — before attributing a change to a specific action; capped at C1 on the causal ladder for a single-site observation).
- Sixteen evaluations and the required review record.

### Changed

- Router's capability-boundary section no longer lists Search Engine Optimization as unsupported; routes to `$seo`.
- Capability registry: SEO moves from unsupported to governed.
- `README.md` no longer disclaims SEO coverage — the disclaimer added in v1.2.0 is now resolved rather than merely documented.

### Removed

- `frameworks/seo-framework.md`, a ten-line phase list with no evidence discipline, decision rules, or output contract — same v1.0 shallow pattern as the skill stubs archived in v1.2.0. Archived to `docs/archive/legacy-skill-stubs/`.

### Remaining migration debt (1)

`copywriting-frameworks.md` — no governed specialist exists for general copywriting outside paid-ad hooks (`$creative-strategy`) and page copy (`$cro`).

## [1.7.0] - 2026-08-25

Adds `$marketing-reporting`, thirteenth governed skill, closing the reporting gap identified in the original v1.1.0 audit and resolving 3 of the 5 remaining migration-debt artifacts.

### Added

- `$marketing-reporting` combines findings already produced by other skills into a cross-channel executive report, recurring cadence, or stakeholder scorecard. It does not perform the underlying audit, diagnosis, reconciliation, or economics analysis — those stay with their owning skill.
- Three references: scorecard construction (one profit level and revenue basis per table, invalid comparisons marked not smoothed, no cross-platform summing), cadence and governance (definitions held fixed across a recurring series, changes disclosed not silently applied, revision discipline), and stakeholder communication (confidence level preserved in plain language, no implied approval).
- Sixteen evaluations and the required review record.

### Changed

- `templates/performance-report.md` and `workflows/reporting-analysis.md` moved from migration-debt to owned by `$marketing-reporting`.
- Capability registry: reporting moves from partially covered to governed for cross-channel and recurring work; bounded single-channel reports remain owned by their existing skill.
- Router routes cross-channel executive reports and recurring cadence work to `$marketing-reporting`.

### Removed

- `templates/reporting-template.md`, a weaker duplicate of `performance-report.md` — raw ROAS/CPA/CPL with no evidence states. Archived to `docs/archive/legacy-skill-stubs/`.

### Remaining migration debt (2)

`copywriting-frameworks.md`, `seo-framework.md` — no governed specialist exists for general copywriting or Search Engine Optimization. They wait on those specialists.

## [1.6.0] - 2026-08-25

Reduces migration debt from 31 root artifacts to 5, following the migration rule set out in `ARTIFACT-OWNERSHIP.md` in v1.2.0: fold into a skill reference, or archive.

### Changed

- 22 root artifacts moved from migration-debt to owned by adding an explicit "Library references" link from their candidate skill's `SKILL.md` — `$google-ads`, `$meta-ads`, `$creative-strategy`, `$cro`, `$tracking-measurement`, `$marketing-router`, `$performance-diagnostics`, and `$icp-jtbd` each gained two to five linked references.
- `marketing-audit.md` was reassessed, not merged: it is a business/market-level review, distinct in scope from a channel audit. Reassigned to `$icp-jtbd` rather than archived.
- `scripts/install-skills.sh` now installs `frameworks/`, `playbooks/`, `templates/`, and `workflows/` alongside skills, at the same rewritten link depth as the root contracts, so the new library references resolve at runtime.

### Removed

- `templates/audit-template.md` and `templates/experiment-plan.md`, weaker duplicates of `templates/audit.md` and `templates/experiment.md` — no evidence states, raw platform metrics with no profitability caveat. Archived to `docs/archive/legacy-skill-stubs/`.

### Remaining migration debt (5)

`copywriting-frameworks.md`, `seo-framework.md`, `performance-report.md`, `reporting-template.md`, `reporting-analysis.md` — left as debt because no governed specialist exists for Search Engine Optimization, general copywriting, or cross-channel reporting. Assigning them an owner would misrepresent the capability registry; they wait on those specialists.

## [1.5.0] - 2026-08-25

Adds customer economics and pacing (Priority 4) — the last major content gap identified in the v1.1.0 audit. Splits across a new skill and an existing owner, per the ownership model.

### Added

- `$retention-economics`, twelfth governed skill, with four references: customer lifetime value (historical versus predictive, profit-level variants), payback period (revenue versus contribution), cohort and retention analysis (curve construction, logo versus revenue churn), and lead-to-revenue cohorts (open-share discipline for long sales cycles).
- `budget-and-outcome-pacing.md` under `$optimization-scaling` — spend and outcome variance against an already-approved plan, with cause attributed before any correction, and a stated boundary distinguishing a pacing correction from a scaling decision.
- Twenty evaluations and the required review record.

### Changed

- `optimization-scaling` rules now state that a pacing correction inside an approved plan is not a scaling decision, and that predictive lifetime value informs but does not by itself satisfy the marginal-evidence gate.
- Router routes lifetime value, payback, cohort, churn, and lead-maturation requests to `$retention-economics`; pacing within an approved plan to `$optimization-scaling`.
- Capability registry: retention economics moves from planned to governed; twelve governed skills.

## [1.4.0] - 2026-08-24

Adds measurement validity and incrementality method selection under `$tracking-measurement`, and closes the v1.3.0 runtime path-depth issue.

### Added

- Seven references under `$tracking-measurement`: causal evidence ladder, incrementality method selector, holdout experiments, geo and quasi-experimental designs, platform lift studies, Marketing Mix Modeling, and triangulation.
- A six-level causal ladder — C0 platform attribution through C5 replicated randomized evidence — where a result's level is set by its weakest structural element and platform attribution never exceeds C0.
- Method selection driven by randomization unit, independence, power, contamination, lag, and platform availability, with explicit disqualifiers that stop a test rather than degrade it.
- `scripts/install-skills.sh`, which installs canonical skills to the local runtime and rewrites root-contract link depth so the contracts resolve where they are installed. It verifies every rewritten link and fails on an unresolved one.
- Twenty-eight evaluations and the required review record.

### Changed

- `$tracking-measurement` now separates three questions — is the data collected correctly, do sources agree, did the activity cause the result — and adds a causal output contract covering required level, achievable level, method, power, contamination, holdback cost, and estimate scope.
- The `optimization-scaling` proof standard links S4 to the causal ladder: a controlled comparison must reach C3 or above, and platform-attributed performance cannot raise a claim above S3.
- Router routes incrementality testing and causal evidence grading to `$tracking-measurement`, which owns method selection while `$optimization-scaling` consumes the result.
- Architecture validator normalizes link depth before comparing installed copies to canonical, and verifies installed links resolve.

### Fixed

- Root contracts were linked at a depth that resolved inside the repository but not from `~/.codex/skills/<name>/`. The install script rewrites the depth; all installed links now resolve.

## [1.3.0] - 2026-08-24

Adds the intake and evidence layer. Built as a skill-owned reference set under the ownership model from 1.2.0 rather than as floating templates.

### Added

- `$marketing-intake` governing engagement scope, evidence grading, metric and conversion definitions, access requests, and the authorization boundary, with five conditional references.
- A seven-level evidence state ladder — `asserted`, `documented`, `observed`, `reconciled`, `verified`, `unknown`, `contradicted` — where the weakest dependency governs a decision's confidence and a state is never upgraded without a named artifact.
- Metric definition register covering Google Ads conversion goals and actions, Meta configuration, revenue basis and profit level, and lifecycle stage definitions, with an explicit comparability rule.
- Authorization register distinguishing `draft`, `proposed`, `approved`, `saved`, `published`, `live`, `processing`, and `verified`, with approval scope and expiry.
- Twenty-eight evaluations and the required review record.
- Installed-runtime integrity reporting in `scripts/validate-skill-architecture.sh`: skill drift, missing installs, and root contracts that are absent or unreachable by their link depth from an installed skill. Reported as notes because the install location is machine-local and absent in continuous integration.

### Changed

- Router routes to `$marketing-intake` before a substantial audit, diagnosis, scaling decision, or live implementation when scope, evidence state, definitions, or authorization are unrecorded.
- Capability registry moves intake from planned to governed; eleven governed skills.

### Known issue

- Root contracts are linked as `../../../FILE.md`, which resolves to the repository root in the canonical layer but to the parent of the install root from `~/.codex/skills/<name>/`. `KNOWLEDGE-TAXONOMY.md` is present at the install root and unreachable by that depth; `CAPABILITY-REGISTRY.md` is not yet installed. Reported by the validator; a fix requires deciding between installing contracts at the resolved depth, inlining the rules, or rewriting paths at install time.

## [1.2.0] - 2026-08-24

Architecture consolidation. No new marketing content; this release removes a conflicting second skill layer and makes capability claims truthful.

### Added

- `CAPABILITY-REGISTRY.md` declaring every capability as governed, partially covered, planned, or unsupported, with task-level boundaries for analytics, reporting, and copywriting.
- `ARTIFACT-OWNERSHIP.md` recording the owner, loading path, and status of every root framework, playbook, template, and workflow; 31 artifacts are tracked as migration debt.
- `scripts/validate-skill-architecture.sh` enforcing skill packaging, frontmatter validity, unique names, folder/frontmatter agreement, reference reachability, broken links, orphaned references, cross-layer skill impersonation, documentation of the canonical path, router-to-registry agreement, and ownership of new root artifacts.
- Router capability-boundary section and eighteen v1.2 evaluations covering routing correctness, capability disclosure, layer distinction, and the ownership rule.
- Architecture validation in continuous integration.

### Changed

- `.agents/skills/` is now declared the canonical executable skill layer in `README.md`, `ARCHITECTURE.md`, and `skills/README.md`. It was previously undocumented in all human-facing material.
- `ARCHITECTURE.md` documents every distribution layer, its consumer, and whether it is executable. `gpt-knowledge/` is labeled a derived export layer whose contents do not imply a governed specialist.
- `skills/` is now an index that points to the canonical layer and contains no instructions.
- Router output now reports capability status and may not name a skill absent from the registry.
- `README.md` no longer claims Search Engine Optimization coverage, and states analytics, reporting, and copywriting as partially covered.

### Removed

- Thirteen shallow skill definitions moved to `docs/archive/legacy-skill-stubs/`. Four (`google-ads`, `meta-ads`, `creative-strategy`, `cro`) conflicted with stronger canonical skills; four (`seo`, `analytics`, `reporting`, `copywriting`) described capabilities with no governed specialist.

### Known variance

- `cro`, `marketing-router`, and `performance-diagnostics` declare required inputs in prose rather than a dedicated section. Reported as a validator note; heading normalization is deferred to the skill-content release.

## [1.1.0] - 2026-08-24

### Added

- Optimization and scaling skill with a scoped S0–S7 proof standard, nine readiness gates, marginal economics, constraint/mode selection, controlled steps, portfolio allocation, creative capacity, business-model overlays, channel methods, and recovery rules.
- Seven reusable scaling frameworks and seven Google, Meta, cross-channel, ecommerce, lead-generation, creative, and de-scaling/recovery playbooks.
- Nine scaling templates for readiness, economics, hypotheses, experiments, change authorization, decision logs, portfolio review, de-scaling, and recovery.
- Thirty behavioral evaluations, a documented evaluation review, and deterministic validation covering unsafe scaling, attribution/incrementality, economics, lag, capacity, coverage, forecasts, recommendations, rollback, recovery, and replication.
- Continuous-integration validation for terminology, platform currency, knowledge taxonomy, scaling structure, and platform-source freshness.

### Changed

- Router now assigns scaling and portfolio-allocation requests to `$optimization-scaling` with channel, diagnostics, and measurement support only when they resolve distinct dependencies.
- Canonical glossary and contributor rules now define scaling, marginal efficiency, saturation, scale ceilings, controlled steps, de-scaling, and recovery.

## [1.0.0] - Initial Public Release

### Added

- Public release structure
- Marketing agent architecture
- Reusable marketing skills
- Framework and playbook system
- Evaluation layer
- Documentation and examples

### Focus

Creating an AI-native marketing operating system built around evidence, frameworks, and repeatable workflows.

Core areas include:

- Meta Ads
- Google Ads
- Creative Strategy
- Copywriting
- Shopify CRO
- SEO
- Reporting systems

## [0.2.3] - 2026-08-23

### Added

- Canonical `KNOWLEDGE-TAXONOMY.md` distinguishing principles, definitions, strategies, frameworks, models, methodologies, processes, playbooks, patterns, hypotheses, tactics, techniques, templates, checklists, best practices, heuristics, and guardrails.
- Reusable knowledge-artifact metadata template covering decision, scope, owner, evidence, confidence, freshness, dependencies, authorization, and rollback/stop conditions.
- Glossary definitions, operating rules, and regression coverage for knowledge-layer boundaries.
