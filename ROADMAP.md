# Roadmap

This file describes the current maturity state and next system-level milestones. Historical implementation details live in [`CHANGELOG.md`](CHANGELOG.md); capability ownership lives in [`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md).

Last reconciled: **2026-09-01**.

## Current state — Governed full-stack Marketing OS

The repository currently has **30 governed skills** in [`.agents/skills/`](.agents/skills/) with one canonical ownership model, shared evidence/governance contracts, behavioral evaluations, and CI validation.

Completed capability areas include:

- marketing routing, intake, shared Marketing Context, and growth strategy
- customer research, ICP/JTBD, competitive intelligence, offer strategy, and pricing/monetization
- Google Ads, Meta Ads, YouTube Ads, TikTok Ads, LinkedIn Ads, programmatic, influencer, affiliate, organic social, PR, and SEO
- creative strategy, copywriting, CRO, static DTC creative direction, and governed 4:5 → centered 1:1 cross-crop safety
- activation, retention strategy, retention economics, and lifecycle marketing
- tracking/measurement, experiment learning, performance diagnostics, marketing reporting, marketing operations, and optimization/scaling
- cross-agent distribution for Codex and Claude Code from one canonical skill source
- public GitHub onboarding and truth-governed worked-example standards

The capability registry remains authoritative. Analytics is still only **partially covered** where work becomes BI engineering, warehouse/pipeline design, or dashboard implementation outside existing measurement/diagnostic/reporting owners.

## Completed maturity milestones

### Evidence and terminology governance

- Canonical glossary and knowledge taxonomy.
- Observed / calculated / inferred / assumed / unknown evidence separation.
- Platform-currency registry and freshness validation for fast-changing platform claims.
- Exact implementation-state language for proposed, configured, live, observed, verified, and related states.

### Strategy and commercial system

- Growth Strategy with evidence-grounded constraint or constraint-set handling, opportunity portfolio, priorities, non-priorities, sequencing, and learning roadmap.
- Offer Strategy separated from Pricing & Monetization.
- Pricing decisions separated from competitor context, stated preference, modeled economics, and realized commercial evidence.

### Acquisition, creative, and conversion system

- Governed channel owners for the active acquisition/distribution disciplines in the capability registry.
- Creative ideation from research → insight → angle → mechanic → concept → hook → format → proof → test.
- Static creative production direction with placement/crop preflight and cross-crop resilience rules.
- CRO ownership limited to the pre-conversion boundary; Activation owns post-conversion first-value decisions.

### Activation and retention system

- Activation owns first meaningful value, path-to-value, time-to-value, and activation intervention strategy.
- Retention Strategy owns reason diagnosis and cause-matched save/recovery/repeat/renewal/win-back interventions.
- Retention Economics owns realized/predictive cohort economics, LTV, payback, and churn/retention measurement.
- Lifecycle Marketing owns communication segmentation, trigger logic, cadence, suppression, and deliverability.

### Measurement, operations, and scaling system

- Tracking & Measurement owns event integrity, attribution reconciliation, causal evidence, and experiment learning.
- Performance Diagnostics owns anomaly decomposition and competing-cause diagnosis.
- Marketing Operations owns recurring cross-skill loops, state, idempotency, approvals, verification, escalation, and retirement.
- Optimization & Scaling owns paid-media readiness, marginal economics, controlled expansion/de-scaling, pacing, and guardrails.
- Marketing Reporting owns cross-channel executive reporting and recurring stakeholder communication.

### Distribution and usability

- `.agents/skills/` remains the canonical skill source.
- Codex and Claude Code installers generate runtime copies without creating competing skill hierarchies.
- `GETTING_STARTED.md`, `AGENT_GUIDE.md`, `DISTRIBUTION.md`, and root README provide public onboarding.
- Worked examples distinguish synthetic, anonymized, and verified public case studies and prohibit fabricated achieved results.

## Current cleanup — System consistency

- Normalize remaining legacy `SKILL.md` files to explicit `## Required inputs` contracts without changing ownership.
- Keep README, roadmap, architecture, capability registry, examples, and distribution docs synchronized with the actual governed system.
- Remove or replace stale compact examples when a stronger governed walkthrough exists.

## Next milestone — Real-world validation

Priority is **validation, not adding skills for the sake of count**.

- Publish a scored `tests/RESULTS.md` from a full live evaluation run. `scripts/eval.py --live` exists and the corpus is registered, but no scored run has been committed, so **no behavioral pass rate is claimed anywhere in this repository**.
- Validate high-value skills against anonymized real-world cases where permission and evidence allow.
- Preserve the difference between a worked example and a verified case study.
- Record contradictions, failed hypotheses, negative outcomes, and scope limits rather than publishing only wins.
- Use experiment-learning records to promote only replicated scoped patterns, never one-off results as universal best practices.

## Next milestone — Data contracts and integrations

Add integration work only when it improves real workflows without moving marketing intelligence out of the skill layer.

- Document supported data contracts for common platform/account exports.
- Define connector/MCP boundaries for read access, live mutations, approval, rollback, and verification.
- Keep Skills as the decision system; treat MCP/connectors/APIs as optional data/action layers.
- Build an installable OpenAI or Claude plugin only when the target manifest, runtime behavior, permissions, resources, and actual install/publish state can be verified.

## Next milestone — Operational maintainability

- Add automated checks that prevent stale capability counts, unsupported roadmap claims, and broken public-navigation links where practical.
- Automate scheduled platform-currency review issues only when a real runtime is configured and verified.
- Establish maintainers, migration policy, and deprecation rules before broader external contribution creates compatibility obligations.
- Continue expanding behavioral evaluations from observed failure modes rather than arbitrary coverage quotas.

## Deliberate non-goals

Do not add a new skill merely because another repository has one. External systems are idea sources only.

Do not duplicate a capability that already has an owner. Improve the existing owner when the gap belongs there.

Do not turn the Marketing OS into one giant MCP server or connector. The governed skill layer remains the marketing intelligence source of truth.

Do not claim a plugin, integration, scheduled loop, live mutation, case-study result, or platform behavior exists until its real state is verified.
