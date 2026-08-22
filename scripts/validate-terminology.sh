#!/bin/zsh

set -eu

repo_dir=${1:-.}
skill_dir="$repo_dir/work/skill-src"
if [[ ! -d "$skill_dir" ]]; then
  skill_dir="$repo_dir/.agents/skills"
fi

required_glossary_terms=(
  "Contribution profit after media"
  "Primary business outcome"
  "Google Ads conversion goal"
  "Primary conversion action"
  "Meta performance goal / optimization event"
  "Attribution"
  "Reconciliation"
  "Incrementality"
  "New-customer acquisition / prospecting"
  "Retargeting / remarketing"
  "Voice of Customer"
  "Message scent"
)

for term in "${required_glossary_terms[@]}"; do
  rg -Fq -- "$term" "$repo_dir/GLOSSARY.md" || {
    print -u2 "Missing canonical glossary term: $term"
    exit 1
  }
done

if rg -Fq -- 'Contribution = net sales - COGS - fulfillment - payment fees - refunds - media spend' \
  "$repo_dir/README.md" "$repo_dir/AGENTS.md" "$repo_dir/GLOSSARY.md" \
  "$repo_dir/frameworks" "$repo_dir/playbooks" "$repo_dir/templates" "$skill_dir"; then
  print -u2 "Found obsolete contribution formula that can double-count refunds"
  exit 1
fi

rg -Fq -- 'conversion goals, their included conversion actions' "$skill_dir/google-ads/SKILL.md"
rg -Fq -- 'campaign objective, conversion location, performance goal' "$skill_dir/meta-ads/SKILL.md"
rg -Fq -- 'primary business outcome' "$skill_dir/cro/SKILL.md"
rg -Fq -- 'Never subtract discounts or refunds twice' "$skill_dir/performance-diagnostics/SKILL.md"
rg -Fq -- 'Voice of Customer' "$skill_dir/customer-research/SKILL.md"
rg -Fq -- 'angle = strategic reason to care' "$skill_dir/creative-strategy/SKILL.md"
rg -Fq -- 'v0.2.1 Terminology Evaluations' "$repo_dir/tests/evaluations/v0.2.1-terminology-cases.md"

print "Terminology contract is internally consistent."
