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
| `google-ads-full-stack.md` | migration-debt | Candidate: `$google-ads` |
| `meta-ads-full-stack.md` | migration-debt | Candidate: `$meta-ads` |
| `creative-strategy.md` | migration-debt | Candidate: `$creative-strategy` |
| `shopify-cro.md` | migration-debt | Candidate: `$cro` |
| `measurement-and-evidence.md` | migration-debt | Candidate: `$tracking-measurement` |
| `experimentation.md` | migration-debt | Candidate: `$tracking-measurement` |
| `decision-prioritization.md` | migration-debt | Candidate: `$marketing-router` |
| `copywriting-frameworks.md` | migration-debt | No governed owner — capability partially covered |
| `seo-framework.md` | migration-debt | No governed owner — capability unsupported |

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
| `google-ads-audit.md` | migration-debt | Candidate: `$google-ads` |
| `meta-ads-audit.md` | migration-debt | Candidate: `$meta-ads` |
| `cross-channel-diagnostic.md` | migration-debt | Candidate: `$performance-diagnostics` |
| `ecommerce.md` | migration-debt | Candidate: `$cro` |
| `ecommerce-growth.md` | migration-debt | Candidate: `$cro` |
| `lead-generation.md` | migration-debt | Candidate: `$icp-jtbd` |
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
| `campaign-brief.md` | migration-debt | Candidate: `$google-ads` / `$meta-ads` |
| `creative-brief.md` | migration-debt | Candidate: `$creative-strategy` |
| `landing-page-review.md` | migration-debt | Candidate: `$cro` |
| `experiment-plan.md` | migration-debt | Candidate: `$tracking-measurement` |
| `experiment.md` | migration-debt | Duplicate of `experiment-plan.md` — consolidate |
| `audit.md` | migration-debt | Duplicate — consolidate with `audit-template.md` |
| `audit-template.md` | migration-debt | Duplicate — consolidate with `marketing-audit.md` |
| `marketing-audit.md` | migration-debt | Duplicate — consolidate |
| `performance-report.md` | migration-debt | No governed owner — reporting partially covered |
| `reporting-template.md` | migration-debt | No governed owner — reporting partially covered |
| `strategy-template.md` | migration-debt | Candidate: `$marketing-router` |
| `README.md` | consumed | Directory index |

## Workflows

| Artifact | Status | Owner or consumer |
|---|---|---|
| `google-ads-optimization.md` | migration-debt | Candidate: `$google-ads` |
| `meta-ads-optimization.md` | migration-debt | Candidate: `$meta-ads` |
| `creative-testing.md` | migration-debt | Candidate: `$creative-strategy` |
| `cro-improvement.md` | migration-debt | Candidate: `$cro` |
| `reporting-analysis.md` | migration-debt | No governed owner — reporting partially covered |
| `README.md` | consumed | Directory index |

## Known duplication to resolve

Three audit templates (`audit.md`, `audit-template.md`, `marketing-audit.md`) and two experiment templates (`experiment.md`, `experiment-plan.md`) overlap. Consolidation is deferred to the migration release so this consolidation stays architectural rather than editorial.

## Migration rule

When migration debt is cleared, the artifact must either become a `references/` file under its owning skill, or remain a root artifact explicitly linked from that skill's `SKILL.md` and recorded here as `owned`. An artifact that cannot be assigned an owner is archived.

## v1.5.0 addition

`$retention-economics` (new skill, four references) and `optimization-scaling/references/budget-and-outcome-pacing.md` (new reference under the existing owner) are both owned at creation and require no entry here — the ownership rule applies to root `frameworks/`, `playbooks/`, `templates/`, and `workflows/`, not to skill-internal references, which are owned by construction.
