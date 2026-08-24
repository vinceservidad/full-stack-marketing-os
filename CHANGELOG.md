# Changelog

Notable changes follow semantic versioning.

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
