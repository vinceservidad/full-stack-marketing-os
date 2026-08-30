# Roadmap

## v0.2 — Measurement and research — Complete

- Added tracking-measurement, customer-research, and ICP/JTBD skills.
- Added attribution reconciliation and conversion-integrity evaluations.
- Added Search, Shopping, PMax, prospecting, and retargeting references.

## v0.2.1 — Terminology normalization — Complete

- Added a canonical glossary and platform-to-strategy mappings.
- Standardized commercial, measurement, research, CRO, creative, and lead-lifecycle terminology.
- Added regression cases that detect ambiguous or misused terms.

## v0.2.2 — Platform currency governance — Complete

- Added dated Google Ads and Meta Ads registries backed by first-party sources.
- Added freshness gates for AI, automation, controls, reporting, and interface terminology.
- Added account-rollout checks and regression cases for unsupported algorithm claims.

## v0.2.3 — Knowledge taxonomy — Complete

- Added a canonical taxonomy for principles, definitions, strategies, frameworks, models, methodologies, processes, playbooks, patterns, hypotheses, tactics, techniques, templates, checklists, best practices, heuristics, and guardrails.
- Added reusable artifact metadata and QA fields for evidence, confidence, freshness, dependencies, authorization, and rollback/stop conditions.
- Added taxonomy regression cases and validation.

## v0.3 — Strategy and production

- Add positioning, offer, funnel, copywriting, landing-page-audit, and experimentation skills.
- Add creative brief and copy QA templates.
- Add SaaS, local-service, and nonprofit playbooks.

## v0.4 — Optimization and scaling — Complete

- Added optimization-scaling skill, seven governed frameworks, seven channel/business playbooks, and nine operational templates.
- Added scoped proof, readiness, marginal-economics, constraint, mode, portfolio, creative-capacity, guardrail, de-scaling, and recovery methods.
- Added 30 regression cases, an evaluation review, deterministic validation, and continuous-integration checks.

## v0.5 — Retention and reporting

- Add retention and marketing-reporting skills.
- Add contribution-margin and lead-quality scorecards.
- Extend routing and unsafe-activation evaluations.

## v1.0 — Proven system — In progress

Done:

- Made the evaluation corpus executable. `scripts/eval.py --static` runs in CI over all 415 cases in 28 registered suites; `--live` scores them against a model and writes a dated scorecard to `tests/RESULTS.md`.
- Added routing evaluations covering the contestable ownership boundaries, so the system's entry point is tested rather than assumed.
- Published three worked examples with committed input fixtures, each reproducible.
- Made the installer work on Linux as well as macOS, and put it under CI on both.

Open:

- Publish a `tests/RESULTS.md` from a full live run. The harness exists; no scored run has been committed yet, so no behavioral pass rate is claimed anywhere in this repository.
- Validate skills against anonymized real-world cases, as distinct from the synthetic fixtures now in `examples/`.
- Document supported data contracts and integrations.
- Automate scheduled currency-review issues and establish maintainers and migration policy.
