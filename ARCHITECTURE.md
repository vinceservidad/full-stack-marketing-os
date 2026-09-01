# Full-Stack Marketing OS Architecture

## Overview

Full-Stack Marketing OS is organized as a governed knowledge, skill, workflow, and data-contract system for AI-assisted marketing decisions and execution.

```text
Business Goal
      ↓
Marketing Router / Growth Strategy
      ↓
Evidence + Data Contracts
      ↓
Specialist Skill
      ↓
Framework / Method
      ↓
Playbook / Template / Workflow
      ↓
Measurement + Evaluation
      ↓
Improved Decision + Scoped Learning
```

Structured data follows a separate provenance path before a specialist decision:

```text
Raw source export / query
      ↓
DATA-CONTRACTS.md envelope
      ↓
Source-specific mapping + field lineage
      ↓
Scoped validation / reconciliation
      ↓
Owning skill decision
```

The normalized layer never replaces the raw source and never upgrades platform attribution into business truth.

## Distribution layers

The system has one canonical skill source and several runtime/export layers. Runtime compatibility does not make those generated copies canonical.

| Layer | Role | Executable by an agent runtime | Canonical status |
|---|---|---:|---|
| `.agents/skills/` | Portable governed operating skills | Yes, when discovered/installed by a compatible runtime | **Canonical skill source** |
| `~/.codex/skills/` | Local Codex runtime copy | Yes | Generated from canonical, never edited as source |
| `~/.claude/skills/` | Local Claude Code personal-skill copy | Yes | Generated from canonical, never edited as source |
| `CLAUDE.md` | Claude Code project-instruction bridge to `AGENTS.md` | Instructions, not a skill layer | Compatibility bridge |
| `skills/` | Compatibility/index layer | No | Must contain no competing instructions |
| `DATA-CONTRACTS.md` | Canonical structured-data provenance, semantics, and decision-validity contract | Loaded by governed skills | **Canonical data contract** |
| `data-contracts/` | Source/domain-specific normalized data contracts | Loaded by governed skills | Governed contract library |
| `frameworks/` | Shared decision artifacts | Loaded by governed skills | Governed knowledge library |
| `playbooks/` | Scenario-specific workflows | Loaded by governed skills | Governed knowledge library |
| `templates/` | Reusable deliverable structures | Loaded by governed skills | Governed artifact library |
| `workflows/` | Execution sequences | Loaded by governed skills | Governed workflow library |
| `agents/` | Agent-role documentation | No | Documentation, not a skill layer |
| `gpt-knowledge/` | Custom GPT knowledge export | Retrieval/knowledge only | Derived, non-canonical export |
| future OpenAI/Claude plugin packages | Installable distribution bundles | Only after actually packaged/installed | Derived distribution, never canonical |
| `evaluations/`, `tests/evaluations/` | Quality and decision-behavior checks | No | Governed |
| `docs/archive/` | Historical material | No | Excluded from active retrieval |

See [`DISTRIBUTION.md`](DISTRIBUTION.md) for current OpenAI/Codex/Claude support and exact installation status.

A Custom GPT export file does not imply a governed executable skill exists, and absence from the export does not imply a capability is unsupported. [`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative on governed capability coverage. Export/runtime coverage and governance coverage are separate claims.

Likewise, a directory of skills is not automatically a plugin. Use the term **plugin** only after the target platform's actual installable package/manifest exists and its install state has been verified.

## Core layers

### Skills

Governed instructions defining how an AI agent performs a marketing decision or workflow. Canonical source: `.agents/skills/`.

Each skill is a directory holding `SKILL.md` with YAML frontmatter (`name`, `description`) and optional `references/` loaded conditionally. Per `AGENTS.md`, every `SKILL.md` supplies a discriminating trigger description, required context, method, decision rules, output contract, and quality assurance.

The canonical structure is intentionally portable: Codex and Claude Code both support skill-style `SKILL.md` packages, while runtime-specific packaging remains a distribution concern rather than a second source hierarchy.

Capability status, governed, partially covered, planned, or unsupported, is declared in `CAPABILITY-REGISTRY.md`. The Marketing Router will not route to a capability absent from it.

### Data contracts

`DATA-CONTRACTS.md` governs structured evidence handed to the OS. `data-contracts/` contains stable normalized decision contracts for Google Ads, Meta Ads, commerce/orders, web analytics, business economics, and cross-source validation.

The data-contract layer preserves:

- source/provenance;
- represented period and timezone;
- currency and monetary basis;
- row grain and stable keys;
- conversion/event semantics;
- attribution, revenue, and named profit basis;
- field lineage from normalized fields to raw source fields/calculations;
- missingness and known source limitations;
- a validity state tied to the named decision.

`$marketing-intake` owns the data-intake record and completeness. `$tracking-measurement` owns measurement/reconciliation validity when required. Specialist skills consume validated/degraded data only within its stated scope.

Raw source data remains preserved. A normalized dataset does not make incompatible attribution systems equal, does not authorize a live mutation, and does not prove causality.

### Shared context

Project-level `.agents/marketing-context.md`, when present, is a versioned shared context summary owned by `$marketing-intake`. It reduces repeated intake but never overrides stronger specialist evidence or becomes a second source of truth.

### Frameworks

Decision models and methods that help analyze situations and choose actions. A framework organizes reasoning; it does not prove an outcome.

### Playbooks

Repeatable processes for specific business cases. Playbooks retain the decision ownership of the skill that governs them.

### Templates

Reusable formats for reports, audits, briefs, strategies, tests, data-intake records, and decision records.

### Workflows

Execution/coordination sequences. A documented workflow does not prove a runtime is scheduled or active.

### Evaluations

Behavioral and quality checks that reduce unsupported assumptions, ownership drift, state confusion, unsafe automation, data-semantic errors, and false certainty.

## Runtime installation

### Codex

`scripts/install-skills.sh` defaults to `~/.codex` and installs generated skill copies plus the contracts/libraries their relative links require, including `DATA-CONTRACTS.md` and `data-contracts/`.

### Claude Code

`scripts/install-claude-skills.sh` delegates to the same canonical installer with `~/.claude` as the runtime root. Claude Code then discovers personal skills under `~/.claude/skills/` and receives the same shared data-contract library.

Root `CLAUDE.md` imports `AGENTS.md` for repository-level contributor instructions. The runtime skill install and the project instruction bridge solve different problems and should not be conflated.

### Custom GPT / ChatGPT

`gpt-knowledge/` is a derived reference export, not the executable source. An installable OpenAI plugin or uploaded ChatGPT skill package is a future distribution artifact and must be validated separately before the repository is described as plugin-enabled.

## Ownership rule

Every substantial active marketing artifact must have an identifiable owner, a discoverable loading path, a declared evidence state, and a validation rule. Existence in the repository alone does not make a file part of the operating system.

`ARTIFACT-OWNERSHIP.md` records ownership for root artifacts. `scripts/validate-skill-architecture.sh` enforces canonical packaging, unique skill names, folder/frontmatter agreement, reference reachability, the prohibition on cross-layer skill impersonation, and the ownership contract for new root artifacts.

`DATA-CONTRACTS.md` and `data-contracts/` are system contracts rather than framework/playbook/template/workflow knowledge types; their own deterministic validator enforces required contract structure and loading paths.

Generated runtime copies must never be edited into a competing owner layer. Change the canonical artifact, validate it, then reinstall/export.

## Design principles

- Strategy before execution
- Evidence before assumptions
- Business outcomes before platform metrics
- Preserve raw source before normalized data
- One owner per decision
- Canonical source before runtime copies
- Human judgment before automation
