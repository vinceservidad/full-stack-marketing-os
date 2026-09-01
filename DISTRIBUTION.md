# Cross-Agent Distribution

Full-Stack Marketing OS is a **portable skill and marketing operating system**, not currently a packaged marketplace plugin.

The canonical source of behavior is always [`.agents/skills/`](.agents/skills/). Runtime installs, knowledge exports, and future plugin packages are distribution layers. They must not become competing sources of truth.

Platform notes below were verified against current OpenAI and Anthropic documentation on **2026-09-01**. Reverify platform-specific packaging and paths before changing this contract.

## Current support matrix

| Consumer | Current support | Path / method | Canonical? |
|---|---|---|---|
| OpenAI Codex | **Supported as skills** | `bash scripts/install-skills.sh . "$HOME/.codex"` → `~/.codex/skills/` | No, generated from `.agents/skills/` |
| Claude Code | **Supported as skills** | `bash scripts/install-claude-skills.sh` → `~/.claude/skills/` | No, generated from `.agents/skills/` |
| Claude Code repo instructions | **Supported** | Root `CLAUDE.md` imports `AGENTS.md` | Bridge only |
| Custom GPT knowledge | **Supported as derived knowledge** | `gpt-knowledge/` | No, non-executable export |
| ChatGPT/OpenAI installable plugin | **Not packaged yet** | Future plugin package may bundle skills and optional connectors/MCP/UI | No |
| Claude installable plugin | **Not packaged yet** | Future Claude plugin may bundle skills and optional agents/hooks/MCP | No |

## Terminology

Use **skill** when referring to a reusable task/workflow instruction package.

Use **plugin** only when an actual installable plugin package/manifest exists for the target platform. A repository containing skills is not automatically a plugin.

Use **Custom GPT knowledge export** for `gpt-knowledge/`. Knowledge files can inform a GPT but do not become governed executable skills merely because they are uploaded.

## OpenAI / Codex

OpenAI currently distinguishes skills from plugins: skills package reusable instructions/resources for ChatGPT and Codex, while plugins are installable bundles that can combine skills with connected tools such as MCP-backed connectors and optional UI.

This repository currently supports the **skill** path for local Codex:

```bash
bash scripts/install-skills.sh . "$HOME/.codex"
```

The installer copies the canonical skills plus the root contracts and governed libraries they reference, rewrites installed relative links, and verifies those links resolve.

The repository is **not yet an OpenAI plugin package**. Do not describe it as published, installed, marketplace-listed, or plugin-enabled unless a real package has been created and verified in the target OpenAI environment.

## Claude Code

Claude Code currently discovers personal skills from `~/.claude/skills/<skill-name>/SKILL.md` and project skills from `.claude/skills/<skill-name>/SKILL.md`. Its skills use `SKILL.md` with YAML frontmatter and may load supporting files when relevant.

Install the canonical Marketing OS skills as personal Claude Code skills with:

```bash
bash scripts/install-claude-skills.sh
```

This delegates to the same canonical installer and writes generated copies to `~/.claude/skills/`. Do not edit those installed copies as source material; change `.agents/skills/` in the repository and reinstall.

When Claude Code works inside this repository, root [`CLAUDE.md`](CLAUDE.md) imports [`AGENTS.md`](AGENTS.md), so contributor and evidence rules remain shared rather than duplicated.

Local personal skills are not the same as a Claude plugin or a cloud-distributed skill. Do not claim Claude plugin/cloud installation unless that distribution has actually been configured and verified.

## Custom GPT

[`gpt-knowledge/`](gpt-knowledge/) is a derived knowledge-export layer for Custom GPT-style retrieval/use. It is useful for providing reference material but is not the canonical skill layer and does not prove runtime behavior.

Capability claims must come from [`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md), not from whatever files happen to exist in `gpt-knowledge/`.

## Canonical-source rule

```text
.agents/skills/
      ↓
Canonical governed skills
      ↓
Install/export/package
      ├─ ~/.codex/skills/
      ├─ ~/.claude/skills/
      ├─ gpt-knowledge/
      └─ future plugin packages
```

Never edit a generated runtime copy and then treat it as the new source of truth.

## Future plugin packaging

A future plugin release should be treated as a separate distribution milestone, not a rename of the repository. Before calling a package a plugin:

1. Create the target platform's required package/manifest structure.
2. Bundle only governed skills and explicitly required resources/tools.
3. Preserve capability ownership and authorization boundaries.
4. Validate links/resources after packaging.
5. Test skill discovery and invocation in the real target runtime.
6. Verify exact install/publish/listing state before claiming the plugin is available.

Plugin packaging must not introduce a second editable skill hierarchy.

## Official platform references

- OpenAI skills/plugins documentation: https://learn.chatgpt.com/docs/skills-and-plugins
- OpenAI Skills API: https://developers.openai.com/api/reference/go/resources/skills
- Claude Code skills documentation: https://code.claude.com/docs/en/skills
