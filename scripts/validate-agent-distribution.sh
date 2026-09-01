#!/usr/bin/env bash

set -euo pipefail

repo_dir=$(cd "${1:-.}" && pwd)
tmp_root=$(mktemp -d)
trap 'rm -rf "$tmp_root"' EXIT

canonical_count=$(find "$repo_dir/.agents/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -type f | wc -l | tr -d ' ')
if [[ "$canonical_count" -eq 0 ]]; then
  printf 'No canonical skills found.\n' >&2
  exit 1
fi

for runtime in codex claude; do
  runtime_root="$tmp_root/$runtime"
  bash "$repo_dir/scripts/install-skills.sh" "$repo_dir" "$runtime_root" >/dev/null

  installed_count=$(find "$runtime_root/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -type f | wc -l | tr -d ' ')
  if [[ "$installed_count" -ne "$canonical_count" ]]; then
    printf '%s install count mismatch: canonical=%s installed=%s\n' "$runtime" "$canonical_count" "$installed_count" >&2
    exit 1
  fi

  for contract in GLOSSARY.md KNOWLEDGE-TAXONOMY.md PLATFORM-CURRENCY.md CAPABILITY-REGISTRY.md ARTIFACT-OWNERSHIP.md DATA-CONTRACTS.md AGENTS.md; do
    test -f "$runtime_root/$contract" || { printf '%s missing contract: %s\n' "$runtime" "$contract" >&2; exit 1; }
  done

  for library in frameworks playbooks templates workflows data-contracts; do
    test -d "$runtime_root/$library" || { printf '%s missing library: %s\n' "$runtime" "$library" >&2; exit 1; }
  done

  test -f "$runtime_root/data-contracts/google-ads.md" || { printf '%s missing Google Ads data contract.\n' "$runtime" >&2; exit 1; }
  test -f "$runtime_root/data-contracts/meta-ads.md" || { printf '%s missing Meta Ads data contract.\n' "$runtime" >&2; exit 1; }
  test -f "$runtime_root/templates/data-intake-manifest.md" || { printf '%s missing data intake manifest.\n' "$runtime" >&2; exit 1; }

  if find "$runtime_root" -name '*.bak' -type f | grep -q .; then
    printf '%s install left sed backup files behind.\n' "$runtime" >&2
    exit 1
  fi
done

# Exercise the public Claude wrapper too. This catches wrapper-to-installer
# permission/invocation regressions that the generic runtime loop cannot see.
claude_home="$tmp_root/claude-wrapper-home"
mkdir -p "$claude_home"
HOME="$claude_home" bash "$repo_dir/scripts/install-claude-skills.sh" "$repo_dir" >/dev/null
wrapper_root="$claude_home/.claude"
wrapper_count=$(find "$wrapper_root/skills" -mindepth 2 -maxdepth 2 -name SKILL.md -type f | wc -l | tr -d ' ')
if [[ "$wrapper_count" -ne "$canonical_count" ]]; then
  printf 'Claude wrapper install count mismatch: canonical=%s installed=%s\n' "$canonical_count" "$wrapper_count" >&2
  exit 1
fi
test -f "$wrapper_root/DATA-CONTRACTS.md" || { printf 'Claude wrapper missing DATA-CONTRACTS.md.\n' >&2; exit 1; }
test -d "$wrapper_root/data-contracts" || { printf 'Claude wrapper missing data-contracts library.\n' >&2; exit 1; }

if [[ ! -f "$repo_dir/CLAUDE.md" ]] || ! grep -Fxq '@AGENTS.md' "$repo_dir/CLAUDE.md"; then
  printf 'CLAUDE.md must import AGENTS.md exactly for the repository instruction bridge.\n' >&2
  exit 1
fi

printf 'Cross-agent distribution valid: %s canonical skills plus shared data contracts install cleanly into Codex- and Claude-style runtime roots, including the Claude wrapper.\n' "$canonical_count"
