#!/usr/bin/env bash

# Installs canonical Marketing OS skills into a local agent runtime.
#
# Default target is Codex at ~/.codex. Pass another install root to reuse the
# same canonical skills with a compatible Agent Skills runtime such as Claude
# Code at ~/.claude.
#
# Root contracts are linked as ../../../FILE.md from a SKILL.md and
# ../../../../FILE.md from a reference. That depth reaches the repository root
# from .agents/skills/<name>/, but overshoots the install root by one level from
# <install>/skills/<name>/. This script copies the skills and rewrites those
# links so the contracts resolve where they are installed.
#
# Usage: scripts/install-skills.sh [repo_dir] [install_root]
# Examples:
#   scripts/install-skills.sh . "$HOME/.codex"
#   scripts/install-skills.sh . "$HOME/.claude"

set -euo pipefail

repo_dir=$(cd "${1:-.}" && pwd)
install_root=${2:-${MARKETING_OS_INSTALL_ROOT:-$HOME/.codex}}
source_dir="$repo_dir/.agents/skills"
target_dir="$install_root/skills"

contracts=(GLOSSARY.md KNOWLEDGE-TAXONOMY.md PLATFORM-CURRENCY.md CAPABILITY-REGISTRY.md ARTIFACT-OWNERSHIP.md AGENTS.md)

# Root libraries linked from a skill's "Library references" section as
# ../../../<dir>/FILE.md. Installed alongside the contracts, at the same
# rewritten depth, so those links resolve too.
libraries=(frameworks playbooks templates workflows)

test -d "$source_dir" || { printf 'No canonical skill directory: %s\n' "$source_dir" >&2; exit 1; }

mkdir -p "$target_dir"

for contract in "${contracts[@]}"; do
  if [[ -f "$repo_dir/$contract" ]]; then
    cp "$repo_dir/$contract" "$install_root/$contract"
  else
    printf 'warning: contract not found in repository: %s\n' "$contract" >&2
  fi
done

for library in "${libraries[@]}"; do
  if [[ -d "$repo_dir/$library" ]]; then
    rm -rf "${install_root:?}/$library"
    cp -R "$repo_dir/$library" "$install_root/$library"
  fi
done

installed=0
for skill_path in "$source_dir"/*/; do
  name=$(basename "$skill_path")
  test -f "$skill_path/SKILL.md" || continue

  rm -rf "${target_dir:?}/$name"
  cp -R "$skill_path" "$target_dir/$name"

  # Rewrite root-contract link depth one level shallower. -i.bak works on both
  # BSD/macOS sed and GNU sed; backup files are removed immediately afterward.
  find "$target_dir/$name" -name '*.md' -type f -exec \
    sed -i.bak \
      -e 's|(\.\./\.\./\.\./\.\./|(@@D@@|g' \
      -e 's|(\.\./\.\./\.\./|(../../|g' \
      -e 's|(@@D@@|(../../../|g' {} +
  find "$target_dir/$name" -name '*.bak' -type f -delete

  installed=$((installed + 1))
done

# Verify every rewritten root-contract link resolves from its installed location.
broken=0
while IFS= read -r -d '' file; do
  while read -r link; do
    target=$(cd "$(dirname "$file")" && cd "$(dirname "$link")" 2>/dev/null && pwd)/$(basename "$link") || true
    if [[ ! -f "$target" ]]; then
      printf 'Unresolved link after install: %s -> %s\n' "${file#"$install_root"/}" "$link" >&2
      broken=$((broken + 1))
    fi
  done < <(grep -o '(\.\./[^)]*\.md)' "$file" | tr -d '()')
done < <(find "$target_dir" -name '*.md' -type f -print0)

if (( broken > 0 )); then
  printf '%d unresolved link(s) after install.\n' "$broken" >&2
  exit 1
fi

printf 'Installed %d skills to %s with resolvable root contracts.\n' "$installed" "$target_dir"
