# Agent role documentation — not an execution layer

These files describe the **human roles** a marketing team recognizes, and map each
one to the governed skills that actually own the work. These summaries are not executable skills; the canonical skills and shared
contracts govern every decision.

Routing is owned by [`$marketing-router`](../.agents/skills/marketing-router/SKILL.md),
and coverage is declared in [`CAPABILITY-REGISTRY.md`](../CAPABILITY-REGISTRY.md).
Where a role description and the registry disagree, the registry is correct.

A role is a way to talk to a team. A skill is what the system executes. The two
do not map one-to-one: several governed skills — `$lifecycle-marketing`,
`$influencer-marketing`, `$affiliate-marketing`, `$organic-social`,
`$public-relations`, `$retention-economics` — have no role file here, and one
role can draw on many skills.

| Role | Governed skills that own the work |
|---|---|
| [Marketing Strategist](marketing-strategist.md) | `$marketing-router`, `$marketing-intake`, `$growth-strategy`, `$icp-jtbd`, `$customer-research` |
| [Paid Media Specialist](paid-media-specialist.md) | `$google-ads`, `$meta-ads`, `$youtube-ads`, `$tiktok-ads`, `$linkedin-ads`, `$programmatic`, `$optimization-scaling` |
| [Creative Director](creative-director.md) | `$creative-strategy`, `$copywriting` |
| [CRO Specialist](cro-specialist.md) | `$cro` |
| [SEO Specialist](seo-specialist.md) | `$seo` |
| [Analytics Specialist](analytics-specialist.md) | `$tracking-measurement`, `$performance-diagnostics` (partial — see below) |
| [Reporting Analyst](reporting-analyst.md) | `$marketing-reporting` |

Analytics is **partially covered**. Business-intelligence engineering, data-warehouse
and pipeline design, and dashboard implementation have no governed specialist. The
role exists in a team; the capability does not exist in this system.
