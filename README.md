# Full-Stack Marketing OS

An evidence-led operating system for planning, auditing, diagnosing, and improving full-funnel marketing. GitHub is the versioned source of truth; Codex and ChatGPT skills are the operating interface.

## Current release: v0.2.2

- A router that selects only the skills needed for a request.
- Operating methods for Google Ads, Meta Ads, creative strategy, CRO, and performance diagnostics.
- Shared evidence and experimentation frameworks.
- Ecommerce and lead-generation playbooks.
- Reusable audit, experiment, and performance-report templates.
- Behavioral evaluations for routing, commercial truth, causality, and authorization.
- Measurement architecture, event-integrity, and attribution-reconciliation methods.
- Evidence-led customer research and ICP/JTBD decision methods.
- Progressive references for Google Search, Shopping, PMax, and Meta prospecting/retargeting.
- A canonical cross-discipline terminology contract in `GLOSSARY.md`.
- A platform-currency contract with dated Google and Meta registries, freshness gates, official-source rules, rollout checks, and regression evaluations.
- A weekly GitHub currency check that fails when either high-change platform registry is more than 30 days old.
- A knowledge taxonomy that distinguishes principles, strategies, frameworks, models, methodologies, processes, playbooks, patterns, hypotheses, tactics, techniques, templates, checklists, best practices, heuristics, and guardrails.

## Use

Ask naturally or invoke a skill explicitly:

- `Use $marketing-router to diagnose yesterday's spend spike and sales drop.`
- `Use $google-ads to audit this search terms export.`
- `Use $creative-strategy to turn these customer reviews into a creative test matrix.`
- `Use $cro to audit this product page for paid traffic.`
- `Use $tracking-measurement to reconcile Ads, analytics, and storefront purchases.`
- `Use $customer-research to synthesize these interview transcripts without inventing prevalence.`
- `Use $icp-jtbd to select the most commercially viable buying situation.`

The router may compose skills, but one skill owns the final answer. Audits begin read-only. Publishing, budget changes, tracking changes, and other external mutations require explicit approval.

For “latest,” AI, algorithm, rollout, or current-interface questions, the channel skill checks `PLATFORM-CURRENCY.md` and its dated platform registry. A documented feature is not assumed to exist in every account, and a platform claim is not treated as proof of business impact.

## Map

```text
.agents/skills/       Skill instructions
frameworks/           Shared decision models
playbooks/            Business-model workflows
templates/            Reusable deliverable structures
KNOWLEDGE-TAXONOMY.md Knowledge-layer definitions and artifact metadata
tests/evaluations/    Behavioral cases
ROADMAP.md             Planned releases
```

The system is an operational foundation, not a claim of universal expertise or access to undisclosed algorithms. Update methods from current first-party documentation, account-visible behavior, and real, anonymized postmortems.

When creating or revising a deliverable, identify its primary knowledge type, evidence status, confidence, freshness, dependencies, authorization, and rollback/stop condition. Use [templates/knowledge-artifact.md](templates/knowledge-artifact.md) for standalone artifacts.
