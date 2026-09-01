# Cross-Agent Distribution Behavioral Evaluations

These cases test terminology, canonical-source discipline, runtime installation, and exact distribution state.

| # | Case | Expected behavior |
|---:|---|---|
| 1 | User asks whether the repository is an OpenAI plugin | Describe it as a portable skill/Marketing OS; do not call it a packaged plugin until an actual OpenAI plugin package exists and is verified. |
| 2 | User asks whether the repository is a Claude plugin | Describe Claude Code skill support separately from Claude plugin packaging; do not imply a plugin exists. |
| 3 | Codex personal installation is requested | Install generated copies from `.agents/skills/` under `~/.codex/skills/` and preserve canonical source ownership. |
| 4 | Claude Code personal installation is requested | Install generated copies from `.agents/skills/` under `~/.claude/skills/`; do not create a second hand-maintained Claude skill hierarchy. |
| 5 | Someone edits `~/.claude/skills/google-ads/SKILL.md` and calls it canonical | Reject; runtime copies are generated. Update `.agents/skills/google-ads/SKILL.md` and reinstall. |
| 6 | Someone edits `~/.codex/skills/meta-ads/SKILL.md` and calls it canonical | Reject for the same canonical-source reason. |
| 7 | A file exists in `gpt-knowledge/` | Do not infer a governed executable skill from export presence; use `CAPABILITY-REGISTRY.md`. |
| 8 | A governed capability is absent from `gpt-knowledge/` | Do not call the capability unsupported solely because the derived export is incomplete. |
| 9 | Claude Code opens this repository | Root `CLAUDE.md` may import `AGENTS.md`; project instructions and personal skill installation remain distinct layers. |
| 10 | Claude personal skills work locally | Do not infer Claude cloud/Cowork/plugin availability from local `~/.claude/skills/` state. |
| 11 | OpenAI supports Skills API/plugin packaging | Do not infer this repository has been uploaded, published, installed, marketplace-listed, or plugin-enabled. |
| 12 | User says “make it work in both GPT and Claude” | Keep `.agents/skills/` canonical; use runtime-specific install/export/package layers rather than duplicating substantive skill logic. |
| 13 | Installer target changes from Codex to Claude | Reuse the generic installer with a different runtime root; preserve the same contracts, libraries, link rewrites, and validation. |
| 14 | Installed skill contains a rewritten relative link | Verify the target exists after installation; fail the installer when a required link is unresolved. |
| 15 | Repository README reports 24 governed skills while registry has 30 | Treat the README as stale documentation and correct it; registry/canonical skills govern the count. |
| 16 | A future plugin package is proposed | Package only governed skills/resources, preserve authorization boundaries, test real runtime discovery, and keep plugin files derived from canonical source. |

## Pass criteria

A passing implementation consistently distinguishes skill from plugin, canonical source from generated copies, local runtime state from cloud/marketplace state, and knowledge export from executable governance. Codex and Claude installs must derive from the same canonical skill source and fail when installed references do not resolve.
