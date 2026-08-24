#!/usr/bin/env bash

set -euo pipefail

repo_dir=${1:-.}
skill_dir="$repo_dir/work/skill-src"
if [[ ! -d "$skill_dir" ]]; then
  skill_dir="$repo_dir/.agents/skills"
fi

required=(
  "$skill_dir/optimization-scaling/SKILL.md"
  "$skill_dir/optimization-scaling/references/proof-standard.md"
  "$skill_dir/optimization-scaling/references/readiness.md"
  "$skill_dir/optimization-scaling/references/economics.md"
  "$skill_dir/optimization-scaling/references/constraints-and-modes.md"
  "$skill_dir/optimization-scaling/references/controlled-steps.md"
  "$skill_dir/optimization-scaling/references/portfolio-allocation.md"
  "$skill_dir/optimization-scaling/references/creative-capacity.md"
  "$skill_dir/optimization-scaling/references/google-scaling.md"
  "$skill_dir/optimization-scaling/references/meta-scaling.md"
  "$skill_dir/optimization-scaling/references/business-overlays.md"
  "$skill_dir/optimization-scaling/references/guardrails-and-recovery.md"
  "$repo_dir/frameworks/scaling-proof-standard.md"
  "$repo_dir/frameworks/scale-readiness.md"
  "$repo_dir/frameworks/marginal-economics.md"
  "$repo_dir/frameworks/constraint-identification.md"
  "$repo_dir/frameworks/controlled-scaling.md"
  "$repo_dir/frameworks/scaling-mode-selector.md"
  "$repo_dir/frameworks/portfolio-allocation.md"
  "$repo_dir/playbooks/google-ads-scaling.md"
  "$repo_dir/playbooks/meta-ads-scaling.md"
  "$repo_dir/playbooks/cross-channel-scaling.md"
  "$repo_dir/playbooks/ecommerce-scaling.md"
  "$repo_dir/playbooks/lead-generation-scaling.md"
  "$repo_dir/playbooks/creative-scaling.md"
  "$repo_dir/playbooks/de-scaling-recovery.md"
  "$repo_dir/templates/scale-readiness.md"
  "$repo_dir/templates/scaling-economics.md"
  "$repo_dir/templates/scaling-hypothesis.md"
  "$repo_dir/templates/scaling-experiment.md"
  "$repo_dir/templates/scaling-change-plan.md"
  "$repo_dir/templates/scaling-decision-log.md"
  "$repo_dir/templates/scaling-portfolio-review.md"
  "$repo_dir/templates/de-scaling-plan.md"
  "$repo_dir/templates/recovery-verification.md"
  "$repo_dir/tests/evaluations/v0.4-scaling-cases.md"
  "$repo_dir/tests/evaluations/v0.4-review.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { printf 'Missing scaling-system file: %s\n' "$file" >&2; exit 1; }
done

for phrase in "Scaling means" "marginal" "binding constraint" "universal budget-increase" "explicit approval" "business source of truth"; do
  grep -Fiq -- "$phrase" "$skill_dir/optimization-scaling/SKILL.md" || { printf 'Missing scaling invariant: %s\n' "$phrase" >&2; exit 1; }
done

grep -Fq -- 'optimization-scaling' "$skill_dir/marketing-router/SKILL.md"
grep -Fq -- '30. **Replication:**' "$repo_dir/tests/evaluations/v0.4-scaling-cases.md"
grep -Fq -- '| 21–30 |' "$repo_dir/tests/evaluations/v0.4-review.md"
grep -Fq -- 'Contribution profit after media' "$skill_dir/optimization-scaling/references/economics.md"
grep -Fq -- 'There is no universal safe percentage or cadence' "$skill_dir/optimization-scaling/references/controlled-steps.md"

if grep -ERiq -- 'always increase (the )?budget by [0-9]+%|guaranteed scaling|platform ROAS proves' "$skill_dir/optimization-scaling" "$repo_dir/frameworks" "$repo_dir/playbooks"; then
  printf '%s\n' 'Found an unsafe universal scaling claim.' >&2
  exit 1
fi

printf '%s\n' 'Optimization and scaling system is structurally complete and linked.'
