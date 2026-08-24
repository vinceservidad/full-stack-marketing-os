# Legacy skill stubs (archived)

These files are historical v1.0 placeholders. They are **not** executable skills, **not** current operating instructions, and **must not** be used as canonical guidance.

Canonical executable skills live in [`.agents/skills/`](../../../.agents/skills/). Capability status is declared in [`CAPABILITY-REGISTRY.md`](../../../CAPABILITY-REGISTRY.md).

## Why these were archived

Each file below either duplicated a canonical skill with weaker and conflicting instructions, or described a capability that has no governed specialist. Both conditions caused retrieval failure: an agent reading `README.md` was directed to `skills/`, found these stubs, and concluded the operating system was unfinished.

| Archived file | Reason | Current status |
|---|---|---|
| `google-ads.flat.md`, `google-ads.SKILL.md` | Conflicting duplicate | Superseded by `.agents/skills/google-ads/` |
| `meta-ads.flat.md`, `meta-ads.SKILL.md` | Conflicting duplicate | Superseded by `.agents/skills/meta-ads/` |
| `creative-strategy.flat.md`, `creative-strategy.SKILL.md` | Conflicting duplicate | Superseded by `.agents/skills/creative-strategy/` |
| `cro.flat.md`, `cro.SKILL.md` | Conflicting duplicate | Superseded by `.agents/skills/cro/` |
| `paid-acquisition.flat.md` | Conflicting duplicate | Split across `.agents/skills/google-ads/` and `.agents/skills/meta-ads/` |
| `analytics.SKILL.md` | No governed specialist | Partially covered — see capability registry |
| `reporting.SKILL.md` | No governed specialist | Partially covered — see capability registry |
| `copywriting.SKILL.md` | No governed specialist | Partially covered — see capability registry |
| `seo.SKILL.md` | No governed specialist | Unsupported — see capability registry |

Archiving a stub did not remove a capability. It removed a claim that the capability was governed. Where portions of the work are genuinely owned by a canonical skill, the capability registry and the Marketing Router record which owner and which boundary.

Retained for release history only. Excluded from active retrieval and from architecture validation.

## v1.6.0 additions

| Archived file | Reason | Current status |
|---|---|---|
| `audit-template.flat.md` | Weaker duplicate — used raw ROAS/CPA with no evidence states, conflicting with `templates/audit.md` | Superseded by `templates/audit.md`, owned by `$performance-diagnostics` |
| `experiment-plan.flat.md` | Weaker duplicate — no evidence states, no guardrails, conflicting with `templates/experiment.md` | Superseded by `templates/experiment.md`, owned by `$tracking-measurement` |
