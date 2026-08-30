# Full-Stack Marketing OS Architecture

## Overview

Full-Stack Marketing OS is organized as a knowledge and workflow system for AI-assisted marketing execution.

The architecture moves from business context to repeatable execution:

```text
Business Goal
      ↓
Marketing Router
      ↓
Specialist Skill
      ↓
Framework / Method
      ↓
Playbook
      ↓
Template
      ↓
Evaluation
      ↓
Improved Decision
```

## Distribution layers

The repository contains several layers with different consumers. Only one is executable. Confusing them is the failure this table exists to prevent.

| Layer | Role | Executable | Canonical status |
|---|---|---|---|
| `.agents/skills/` | Agent-discoverable operating skills | Yes | **Canonical skill source** |
| `~/.claude/skills/`, `~/.codex/skills/` | Installed local runtime copies | Yes | Generated from canonical by `scripts/install-skills.sh` — never edited directly |
| `.claude-plugin/` | Claude Code plugin and marketplace manifests | No | Points at `.agents/skills/`; declares no skills of its own |
| `skills/` | Compatibility index | No | Must contain no competing instructions |
| `frameworks/` | Shared decision artifacts | No | Governed knowledge library |
| `playbooks/` | Scenario-specific workflows | No | Governed knowledge library |
| `templates/` | Reusable deliverable structures | No | Governed artifact library |
| `workflows/` | Execution sequences | No | Governed workflow library |
| `agents/` | Agent-role documentation | No | Documentation; not a skill layer |
| `gpt-knowledge/` | Custom GPT export package | No | Derived export layer |
| `evaluations/`, `tests/evaluations/` | Quality and decision-behavior checks | No | Governed |
| `docs/archive/` | Historical material | No | Excluded from active retrieval |

A Custom GPT export file does not imply a governed executable skill exists. `gpt-knowledge/` is a derived, hand-maintained export: it is not generated from `.agents/skills/`, is not validated against them, and can describe a capability at a different depth — or a different vintage — than the skill that governs it. Export coverage and runtime skill coverage are separate claims, and `CAPABILITY-REGISTRY.md` settles the second one.

## Core Layers

### Skills

Governed instructions defining how an AI agent performs a marketing task. Canonical source: `.agents/skills/`.

Each skill is a directory holding `SKILL.md` with YAML frontmatter (`name`, `description`) and optional `references/` loaded conditionally. Per `AGENTS.md`, every `SKILL.md` supplies a discriminating trigger description, required context, method, decision rules, output contract, and quality assurance.

Capability status — governed, partially covered, planned, unsupported — is declared in `CAPABILITY-REGISTRY.md`. The Marketing Router will not route to a capability absent from it.

### Frameworks

Decision models that help analyze situations and choose actions.

### Playbooks

Repeatable workflows for specific business cases.

### Templates

Reusable formats for reports, audits, briefs, and strategies.

### Evaluations

Quality checks to reduce unsupported assumptions and improve consistency.

## Ownership rule

Every substantial active marketing artifact must have an identifiable owner, a discoverable loading path, a declared evidence state, and a validation rule. Existence in the repository alone does not make a file part of the operating system.

`ARTIFACT-OWNERSHIP.md` records ownership for root artifacts. `scripts/validate-skill-architecture.sh` enforces canonical packaging, unique skill names, folder/frontmatter agreement, reference reachability, the prohibition on cross-layer skill impersonation, and the ownership contract for new root artifacts.

`scripts/eval.py --static` covers what that validator cannot see: every evaluation case parses and carries a pass criterion, every case file is registered in `tests/evaluations/suites.json` and names a skill that exists, no knowledge layer makes a claim the system's own rules forbid, and the skill names written in `agents/` and `evaluations/` resolve to governed skills.

## Design Principles

- Strategy before execution
- Evidence before assumptions
- Business goals before platform settings
- Human judgment before automation
