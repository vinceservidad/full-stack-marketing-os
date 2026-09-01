# Cross-Agent Distribution Evaluation Review

Reviewed: 2026-09-01

Status: **Pass**

Scope reviewed: canonical `.agents/skills/`, Codex runtime installation, Claude Code personal-skill installation, root `CLAUDE.md`, Custom GPT knowledge export semantics, terminology, and the 16 cases in `cross-agent-distribution-cases.md`.

## Terminology review

Pass.

The repository is described as a portable skill and Marketing OS. The word `plugin` is reserved for a real installable plugin package in the target runtime. OpenAI/ChatGPT plugin support and Claude plugin support are future distribution states, not inferred from the existence of `SKILL.md` files.

## Canonical-source review

Pass.

`.agents/skills/` remains the only canonical executable skill source. `~/.codex/skills/`, `~/.claude/skills/`, `gpt-knowledge/`, and any future plugin packages are generated/runtime/export layers and cannot become competing sources of truth.

## Codex review

Pass.

`scripts/install-skills.sh` defaults to the Codex runtime root and supports an explicit runtime root. It copies root contracts and governed libraries, rewrites installed relative links one level shallower, removes temporary backup files, and verifies links resolve.

## Claude Code review

Pass.

Current Claude Code documentation supports personal skills at `~/.claude/skills/<skill-name>/SKILL.md` and project skills at `.claude/skills/<skill-name>/SKILL.md`. The repository uses the personal runtime path through `scripts/install-claude-skills.sh`, which delegates to the same canonical installer rather than creating hand-maintained Claude-specific copies.

Root `CLAUDE.md` imports `AGENTS.md`, preserving repository-level contributor rules independently of personal skill installation.

## Custom GPT / plugin-state review

Pass.

`gpt-knowledge/` is labeled as derived knowledge, not an executable skill layer. Capability truth comes from `CAPABILITY-REGISTRY.md`. OpenAI currently distinguishes reusable skills from installable plugins; the repository does not claim an OpenAI or Claude plugin package exists until a real manifest/package and target-runtime install are verified.

## Documentation review

Pass.

README coverage is updated from the stale twenty-four-skill description to thirty governed skills and links to the new distribution contract. Architecture no longer falsely says SEO, copywriting, and reporting lack governed specialists.

## Final verdict

**Pass.** Cross-agent distribution is explicit, runtime-specific without duplicating marketing logic, and truthful about the difference between skills, knowledge exports, and plugins.
