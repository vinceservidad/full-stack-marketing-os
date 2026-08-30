#!/usr/bin/env bash

# Installs the canonical skills into a local agent runtime.
#
# Root contracts are linked as ../../../FILE.md from a SKILL.md and
# ../../../../FILE.md from a reference. That depth reaches the repository root
# from .agents/skills/<name>/, but overshoots the install root by one level from
# <install>/skills/<name>/. This script copies the skills and rewrites those
# links so the contracts resolve where they are installed.
#
# Usage:
#   scripts/install-skills.sh                      # auto-detect every runtime present
#   scripts/install-skills.sh --target claude      # ~/.claude
#   scripts/install-skills.sh --target codex       # ~/.codex
#   scripts/install-skills.sh --target /some/root  # arbitrary install root
#   scripts/install-skills.sh --dry-run            # report without writing
#   scripts/install-skills.sh [repo_dir] [root]    # legacy positional form

set -euo pipefail

usage() {
  sed -n '3,17p' "$0" | sed 's|^# \{0,1\}||'
}

repo_dir=""
dry_run=0
targets=()

add_target() {
  case "$1" in
    claude) targets+=("$HOME/.claude") ;;
    codex) targets+=("$HOME/.codex") ;;
    *) targets+=("$1") ;;
  esac
}

while (($#)); do
  case "$1" in
    --target) shift; [[ $# -gt 0 ]] || { printf 'error: --target needs a value\n' >&2; exit 2; }; add_target "$1" ;;
    --target=*) add_target "${1#*=}" ;;
    --repo) shift; [[ $# -gt 0 ]] || { printf 'error: --repo needs a value\n' >&2; exit 2; }; repo_dir="$1" ;;
    --repo=*) repo_dir="${1#*=}" ;;
    --dry-run) dry_run=1 ;;
    -h|--help) usage; exit 0 ;;
    -*) printf 'error: unknown option %s\n' "$1" >&2; usage >&2; exit 2 ;;
    *)
      # Legacy positional form: repo_dir first, install root second.
      if [[ -z "$repo_dir" ]]; then repo_dir="$1"; else add_target "$1"; fi
      ;;
  esac
  shift
done

repo_dir=$(cd "${repo_dir:-.}" && pwd)
source_dir="$repo_dir/.agents/skills"

test -d "$source_dir" || { printf 'No canonical skill directory: %s\n' "$source_dir" >&2; exit 1; }

# No explicit target: install into every agent runtime that already exists.
if ((${#targets[@]} == 0)); then
  for candidate in "$HOME/.claude" "$HOME/.codex"; do
    [[ -d "$candidate" ]] && targets+=("$candidate")
  done
fi

if ((${#targets[@]} == 0)); then
  cat >&2 <<'EOF'
No agent runtime found at ~/.claude or ~/.codex.

Install to one explicitly:
  scripts/install-skills.sh --target claude
  scripts/install-skills.sh --target codex
  scripts/install-skills.sh --target /path/to/runtime
EOF
  exit 1
fi

contracts=(GLOSSARY.md KNOWLEDGE-TAXONOMY.md PLATFORM-CURRENCY.md CAPABILITY-REGISTRY.md ARTIFACT-OWNERSHIP.md AGENTS.md)

# Root libraries linked from a skill's "Library references" section as
# ../../../<dir>/FILE.md. Installed alongside the contracts, at the same
# rewritten depth, so those links resolve too.
libraries=(frameworks playbooks templates workflows)

# Rewrites root-contract link depth one level shallower. Both patterns are
# rewritten in a single pass via a placeholder: applied sequentially, the
# four-level result would match the three-level pattern and shift twice.
#
# Python rather than sed: in-place editing is spelled differently by GNU sed
# (-i) and BSD/macOS sed (-i ''), and no single invocation works on both.
# Python 3 is already required by the repository's other validation scripts.
rewrite_link_depth() {
  python3 - "$1" <<'PY'
import pathlib
import sys

root = pathlib.Path(sys.argv[1])
for markdown in root.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    rewritten = (
        text.replace("(../../../../", "(@@D@@")
        .replace("(../../../", "(../../")
        .replace("(@@D@@", "(../../../")
    )
    if rewritten != text:
        markdown.write_text(rewritten, encoding="utf-8")
PY
}

status=0

for install_root in "${targets[@]}"; do
  target_dir="$install_root/skills"

  if ((dry_run)); then
    count=$(find "$source_dir" -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')
    printf 'dry run: would install %s skills to %s\n' "$count" "$target_dir"
    continue
  fi

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

    installed=$((installed + 1))
  done

  rewrite_link_depth "$target_dir"

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

  if ((broken > 0)); then
    printf '%d unresolved link(s) after install to %s.\n' "$broken" "$target_dir" >&2
    status=1
    continue
  fi

  printf 'Installed %d skills to %s with resolvable root contracts.\n' "$installed" "$target_dir"
done

exit "$status"
