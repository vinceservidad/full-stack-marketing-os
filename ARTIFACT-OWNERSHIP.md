# Artifact Ownership

Every substantial active marketing artifact must have an identifiable owner, a discoverable loading path, a declared evidence state, and a validation rule. Existence in the repository alone does not make a file part of the operating system.

This registry records the ownership state of root-level `frameworks/`, `playbooks/`, `templates/`, and `workflows/`. `scripts/validate-skill-architecture.sh` enforces it: a **new** file added to those directories without an entry here fails validation. Existing entries marked `migration-debt` are reported, not failed — they are tracked and eliminated release by release.

Status definitions:

- **owned** — a canonical skill loads or governs the artifact.
- **consumed** — no skill loads it directly; a documented workflow, export, or human process uses it.
- **migration-debt** — active knowledge with no owner and no loading path. Must be assigned an owner, folded into a skill reference, or archived.
- **archived** — retained for history, excluded from active retrieval.

## Frameworks

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

## Playbooks

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

## Templates

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
| `creative-idea-matrix.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `marketing-context.md` | owned | `$marketing-intake` (linked from SKILL.md; copied into active projects as `.agents/marketing-context.md`) |
| `marketing-loop.md` | owned | `$marketing-operations` (linked from SKILL.md) — recurring loop contract with trigger, state, idempotency, authorization, verification, escalation, and retirement |
| `pricing-decision.md` | owned | `$pricing-monetization` (linked from SKILL.md) — pricing, value metric, packaging, scenario, rollout, migration, and verification decision record |
| `activation-plan.md` | owned | `$activation` (linked from SKILL.md) — first-value definition, path-to-value, diagnosis, intervention, measurement, handoffs, and learning record |
| `landing-page-review.md` | owned | `$cro` (linked from SKILL.md) |
| `experiment-plan.md` | archived | Weaker duplicate of `experiment.md`; moved to `docs/archive/legacy-skill-stubs/experiment-plan.flat.md` |
| `experiment.md` | owned | `$tracking-measurement` (linked from SKILL.md) |
| `experiment-learning.md` | owned | `$tracking-measurement` (linked from SKILL.md) — post-test validity, scoped learning, transfer, contradiction, and follow-up record |
| `audit.md` | owned | `$performance-diagnostics` (linked from SKILL.md) — canonical audit format |
| `audit-template.md` | archived | Weaker duplicate of `audit.md`; moved to `docs/archive/legacy-skill-stubs/audit-template.flat.md` |
| `marketing-audit.md` | owned | `$icp-jtbd` (linked from SKILL.md) — distinct scope: business/market-level, not a channel audit |
| `performance-report.md` | owned | `$marketing-reporting` (linked from SKILL.md) — canonical report format |
| `reporting-template.md` | archived | Weaker duplicate of `performance-report.md`; moved to `docs/archive/legacy-skill-stubs/reporting-template.flat.md` |
| `strategy-template.md` | owned | `$marketing-router` (linked from SKILL.md) |
| `README.md` | consumed | Directory index |

## Workflows

| Artifact | Status | Owner or consumer |
|---|---|---|
| `marketing-operations-loop.md` | owned | `$marketing-operations` (linked from SKILL.md) — canonical recurring operating sequence |
| `google-ads-optimization.md` | owned | `$google-ads` (linked from SKILL.md) |
| `meta-ads-optimization.md` | owned | `$meta-ads` (linked from SKILL.md) |
| `creative-ideation-engine.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `creative-testing.md` | owned | `$creative-strategy` (linked from SKILL.md) |
| `cro-improvement.md` | owned | `$cro` (linked from SKILL.md) |
| `reporting-analysis.md` | owned | `$marketing-reporting` (linked from SKILL.md) — data-to-decision workflow sequence |
| `README.md` | consumed | Directory index |

## Duplication resolved in v1.6.0

`audit-template.md` and `experiment-plan.md` were weaker duplicates — no evidence states, raw platform metrics with no profitability caveat — and were archived. `audit.md` and `experiment.md` are canonical and now owned. `marketing-audit.md` was not a duplicate: business/market-level scope distinct from a channel audit. It is now owned by `$icp-jtbd`.

## Migration rule

When migration debt is cleared, the artifact must either become a `references/` file under its owning skill, or remain a root artifact explicitly linked from that skill's `SKILL.md` and recorded here as `owned`. An artifact that cannot be assigned an owner is archived.

## v1.5.0 addition

`$retention-economics` (new skill, four references) and `optimization-scaling/references/budget-and-outcome-pacing.md` (new reference under the existing owner) are both owned at creation and require no entry here — the ownership rule applies to root `frameworks/`, `playbooks/`, `templates/`, and `workflows/`, not to skill-internal references, which are owned by construction.
