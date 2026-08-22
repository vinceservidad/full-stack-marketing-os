#!/usr/bin/env bash

set -eu

repo_dir=${1:-.}
skill_dir="$repo_dir/work/skill-src"
if [[ ! -d "$skill_dir" ]]; then
  skill_dir="$repo_dir/.agents/skills"
fi
google_registry="$skill_dir/google-ads/references/platform-current.md"
meta_registry="$skill_dir/meta-ads/references/platform-current.md"

for required in "$repo_dir/PLATFORM-CURRENCY.md" "$google_registry" "$meta_registry"; do
  test -f "$required" || {
    printf '%s\n' "Missing platform-currency file: $required" >&2
    exit 1
  }
done

grep -Fq -- '**Last verified:** ' "$google_registry"
grep -Fq -- '**Last verified:** ' "$meta_registry"
grep -Fq -- 'references/platform-current.md' "$skill_dir/google-ads/SKILL.md"
grep -Fq -- 'references/platform-current.md' "$skill_dir/meta-ads/SKILL.md"
grep -Fq -- 'PLATFORM-CURRENCY.md' "$skill_dir/marketing-router/SKILL.md"
grep -Fq -- 'Officially documented' "$repo_dir/PLATFORM-CURRENCY.md"
grep -Fq -- 'Account-visible' "$repo_dir/PLATFORM-CURRENCY.md"
grep -Fq -- 'Experimentally observed' "$repo_dir/PLATFORM-CURRENCY.md"
grep -Fq -- 'v0.2.2 Platform Currency Evaluations' "$repo_dir/tests/evaluations/v0.2.2-platform-currency-cases.md"

registry_urls=$(grep -Eho 'https://[^)]+' "$google_registry" "$meta_registry" || true)
if printf '%s\n' "$registry_urls" | grep -Ev 'https://(support\.google\.com/google-ads|www\.facebook\.com/business)' >/dev/null; then
  printf '%s\n' "Platform registry contains a non-first-party source" >&2
  exit 1
fi

printf '%s\n' "Platform currency contract is linked and source-controlled."
