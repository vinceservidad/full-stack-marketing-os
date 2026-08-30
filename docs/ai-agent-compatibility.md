# AI Agent Compatibility

Full-Stack Marketing OS is a knowledge and workflow layer. The canonical skills in
`.agents/skills/` are plain Markdown with YAML frontmatter, so any agent runtime that
reads a skills directory can load them.

## Claude Code

Two routes. The plugin is the shorter one:

```
/plugin marketplace add vinceservidad/full-stack-marketing-os
/plugin install full-stack-marketing-os@full-stack-marketing-os
```

`.claude-plugin/plugin.json` points `skills` at `./.agents/skills/`, so the canonical
layer is loaded directly and never duplicated. `agents`, `commands`, and `workflows`
are explicitly empty — the root `agents/` and `workflows/` directories are
documentation, not plugin components, and must not be auto-discovered as such.

Or install into the runtime directory:

```bash
scripts/install-skills.sh --target claude   # ~/.claude/skills
```

## Codex and other coding agents

```bash
scripts/install-skills.sh --target codex    # ~/.codex/skills
scripts/install-skills.sh --target /path    # any runtime root
```

With no `--target`, the installer writes to every runtime it finds (`~/.claude`,
`~/.codex`) and tells you if it finds none.

The installer also copies the root contracts (`GLOSSARY.md`,
`KNOWLEDGE-TAXONOMY.md`, `PLATFORM-CURRENCY.md`, `CAPABILITY-REGISTRY.md`,
`ARTIFACT-OWNERSHIP.md`, `AGENTS.md`) and the `frameworks/`, `playbooks/`,
`templates/`, and `workflows/` libraries, then rewrites relative link depth so a
skill's links resolve from where it was installed. It fails if any link does not
resolve, rather than installing a broken tree.

## ChatGPT and Custom GPTs

`gpt-knowledge/` is an export package for Custom GPT instructions and knowledge
files. It is **derived and hand-maintained** — not generated from `.agents/skills/`
and not validated against them, so it can describe a capability at a different depth
or vintage than the skill that governs it. `CAPABILITY-REGISTRY.md` is authoritative
on what is actually governed.

Recommended flow: Request → Router → Skill → Framework → Playbook → Template → Evaluation

## Any other runtime

Point it at `.agents/skills/`. Each skill is a directory holding a `SKILL.md` with
`name` and `description` frontmatter, plus a `references/` directory loaded
conditionally. Relative links from a `SKILL.md` reach the repository root at
`../../../`; if your runtime installs skills at a different depth, use
`scripts/install-skills.sh` rather than copying by hand, so link depth is rewritten
and verified.

## General agent rules

- Choose the correct skill before giving tactics; `$marketing-router` owns that choice.
- Use evidence before assumptions, and label facts, hypotheses, and recommendations separately.
- Do not invent client results or platform behavior.
- Declare a capability gap rather than substituting an adjacent skill.
- Review output quality before delivery.
