#!/usr/bin/env bash

set -euo pipefail

repo_dir=$(cd "${1:-.}" && pwd)

required_files=(
  DATA-CONTRACTS.md
  data-contracts/google-ads.md
  data-contracts/meta-ads.md
  data-contracts/commerce-orders.md
  data-contracts/web-analytics.md
  data-contracts/business-economics.md
  data-contracts/validation.md
  templates/data-intake-manifest.md
)

for file in "${required_files[@]}"; do
  test -f "$repo_dir/$file" || { printf 'Missing data-contract artifact: %s\n' "$file" >&2; exit 1; }
done

for token in contract_id contract_version dataset_id source_system source_generated_at data_start_at data_end_at timezone currency grain primary_key row_semantics attribution_basis conversion_definition revenue_basis profit_basis freshness_state normalization_state known_limitations field_lineage; do
  grep -q "$token" "$repo_dir/DATA-CONTRACTS.md" || { printf 'DATA-CONTRACTS.md missing required envelope token: %s\n' "$token" >&2; exit 1; }
done

for state in received profiled mapped validated-for-scope degraded rejected; do
  grep -q "$state" "$repo_dir/DATA-CONTRACTS.md" || { printf 'DATA-CONTRACTS.md missing dataset state: %s\n' "$state" >&2; exit 1; }
done

for file in google-ads.md meta-ads.md commerce-orders.md web-analytics.md business-economics.md validation.md; do
  grep -q 'DATA-CONTRACTS.md' "$repo_dir/data-contracts/$file" || { printf 'Data contract does not link canonical root contract: %s\n' "$file" >&2; exit 1; }
done

for skill in marketing-intake tracking-measurement google-ads meta-ads performance-diagnostics; do
  grep -q 'DATA-CONTRACTS.md' "$repo_dir/.agents/skills/$skill/SKILL.md" || { printf 'Skill missing DATA-CONTRACTS.md loading path: %s\n' "$skill" >&2; exit 1; }
done

grep -q '`data-intake-manifest.md` | owned | `$marketing-intake`' "$repo_dir/ARTIFACT-OWNERSHIP.md" || {
  printf 'data-intake-manifest.md must be registered to $marketing-intake.\n' >&2
  exit 1
}

grep -q 'DATA-CONTRACTS.md' "$repo_dir/scripts/install-skills.sh" || { printf 'Installer does not ship DATA-CONTRACTS.md.\n' >&2; exit 1; }
grep -q 'data-contracts' "$repo_dir/scripts/install-skills.sh" || { printf 'Installer does not ship data-contracts library.\n' >&2; exit 1; }

printf 'Data contracts valid: canonical envelope, platform/business contracts, skill loading paths, template ownership, and runtime distribution are present.\n'
