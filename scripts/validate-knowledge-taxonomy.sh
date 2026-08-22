#!/usr/bin/env bash

set -euo pipefail

repo_dir=${1:-.}
skill_dir="$repo_dir/work/skill-src"
if [[ ! -d "$skill_dir" ]]; then
  skill_dir="$repo_dir/.agents/skills"
fi

test -f "$repo_dir/KNOWLEDGE-TAXONOMY.md"
test -f "$repo_dir/templates/knowledge-artifact.md"
test -f "$repo_dir/tests/evaluations/v0.2.3-knowledge-taxonomy-cases.md"

for term in Principle Strategy Framework Model Methodology Process Playbook Pattern Hypothesis Tactic Technique Template Checklist "Best practice" Heuristic Guardrail; do
  grep -Fq -- "**$term**" "$repo_dir/KNOWLEDGE-TAXONOMY.md"
done

for field in artifact_type decision scope owner inputs evidence_status confidence freshness dependencies authorization rollback_or_stop; do
  grep -Fq -- "$field:" "$repo_dir/KNOWLEDGE-TAXONOMY.md"
  grep -Fq -- "$field:" "$repo_dir/templates/knowledge-artifact.md"
done

grep -Fq -- 'KNOWLEDGE-TAXONOMY.md' "$skill_dir/marketing-router/SKILL.md"
grep -Fq -- 'v0.2.3 Knowledge Taxonomy Evaluations' "$repo_dir/tests/evaluations/v0.2.3-knowledge-taxonomy-cases.md"

printf '%s\n' "Knowledge taxonomy contract is complete and linked."
