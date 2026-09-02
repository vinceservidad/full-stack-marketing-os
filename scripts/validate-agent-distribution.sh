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

  for contract in GLOSSARY.md KNOWLEDGE-TAXONOMY.md PLATFORM-CURRENCY.md CAPABILITY-REGISTRY.md ARTIFACT-OWNERSHIP.md AGENTS.md; do
    test -f "$runtime_root/$contract" || { printf '%s missing contract: %s\n' "$runtime" "$contract" >&2; exit 1; }
  done

  for library in frameworks playbooks templates workflows; do
    test -d "$runtime_root/$library" || { printf '%s missing library: %s\n' "$runtime" "$library" >&2; exit 1; }
  done

  if find "$runtime_root" -name '*.bak' -type f | grep -q .; then
    printf '%s install left sed backup files behind.\n' "$runtime" >&2
    exit 1
  fi
done

if [[ ! -f "$repo_dir/CLAUDE.md" ]] || ! grep -Fxq '@AGENTS.md' "$repo_dir/CLAUDE.md"; then
  printf 'CLAUDE.md must import AGENTS.md exactly for the repository instruction bridge.\n' >&2
  exit 1
fi

printf 'Cross-agent distribution valid: %s canonical skills install cleanly into Codex- and Claude-style runtime roots.\n' "$canonical_count"
