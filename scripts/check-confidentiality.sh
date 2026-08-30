#!/usr/bin/env bash

# Enforces the confidentiality rule that CONTRIBUTING.md and examples/README.md
# already state: no client confidential information, account access details, or
# personal data in this repository.
#
# Scans tracked files for the shapes that leak in practice. It cannot recognise a
# client name, so it is a guard against the mechanical mistakes, not a substitute
# for review.
#
# Usage: scripts/check-confidentiality.sh [repo_dir]

set -euo pipefail

repo_dir=$(cd "${1:-.}" && pwd)
cd "$repo_dir"

findings=0

report() {
  printf 'Possible confidential content — %s\n' "$1" >&2
  printf '%s\n' "$2" | sed 's/^/    /' >&2
  findings=$((findings + 1))
}

# scan <label> <extended-regexp> [extra git-grep flags...]
scan() {
  local label=$1 pattern=$2
  shift 2
  local hits
  # Allowlist: the maintainer's own contact details and documented placeholders.
  hits=$(git grep -InE "$@" "$pattern" -- \
      ':!docs/archive' ':!.github/FUNDING.yml' ':!scripts/check-confidentiality.sh' \
      2>/dev/null \
    | grep -viE 'example\.(com|org)|your-?(email|account|domain)|<[a-z-]+>|placeholder|vinceservidad|noreply' \
    || true)
  if [[ -n "$hits" ]]; then
    report "$label" "$hits"
  fi
  # Never let an empty result end the function non-zero; `set -e` would abort here.
  return 0
}

scan "email address"              '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
scan "Google Ads customer ID"     '\b[0-9]{3}-[0-9]{3}-[0-9]{4}\b'
scan "Meta ad account ID"         '\bact_[0-9]{8,}\b'
scan "GA4 measurement ID"         '\bG-[A-Z0-9]{10}\b'
scan "Google Tag Manager ID"      '\bGTM-[A-Z0-9]{6,}\b'
scan "API key or token"           '\b(sk-[A-Za-z0-9_-]{16,}|ghp_[A-Za-z0-9]{20,}|AIza[A-Za-z0-9_-]{20,}|EAA[A-Za-z0-9]{40,})\b'
scan "private key block"          'BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY'
scan "assignment of a secret"     '\b(api[_-]?key|secret|password|access[_-]?token)[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"']{12,}' -i

if ((findings > 0)); then
  printf '\n%d pattern(s) matched. Remove the content, or extend the allowlist in this script if it is a false positive.\n' "$findings" >&2
  exit 1
fi

printf '%s\n' "No client identifiers, credentials, or personal data found in tracked files."
