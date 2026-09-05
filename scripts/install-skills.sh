#!/usr/bin/env bash

# Usage: scripts/install-skills.sh [repo_dir] [install_root] [--dry-run]
# Keeps the existing Codex/Claude positional interface. Python 3 is required.
# Shared files are namespaced; personal instructions are never replaced.
set -euo pipefail
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
command -v python3 >/dev/null 2>&1 || { printf 'Python 3 is required.\n' >&2; exit 1; }
exec python3 "$script_dir/install-skills.py" "$@"
