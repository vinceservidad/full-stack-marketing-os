#!/usr/bin/env bash

# Installs the canonical Marketing OS skill set for local Claude Code use.
# Claude Code discovers personal skills from ~/.claude/skills/<name>/SKILL.md.
# The canonical source remains .agents/skills/ in this repository.
#
# Usage: scripts/install-claude-skills.sh [repo_dir]

set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
repo_dir=$(cd "${1:-$script_dir/..}" && pwd)

"$script_dir/install-skills.sh" "$repo_dir" "$HOME/.claude"

printf 'Claude Code personal skills installed from canonical Marketing OS source.\n'
printf 'Root repository instructions remain governed by CLAUDE.md -> AGENTS.md when working inside this repository.\n'
