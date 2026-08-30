# Skills — index only (not an execution layer)

This directory is a **compatibility index**. It contains no executable skills and no operating instructions.

## Canonical source

Executable, governed operating skills live in:

```text
.agents/skills/
```

That is the only canonical skill layer. Local runtime copies are installed at `~/.claude/skills/` and `~/.codex/skills/` by `scripts/install-skills.sh` and are generated from the canonical source — never edited directly.

Capability status — governed, partially covered, planned, or unsupported — is declared in [`CAPABILITY-REGISTRY.md`](../CAPABILITY-REGISTRY.md).

## Governed skills

| Skill | Scope |
|---|---|
| [`marketing-router`](../.agents/skills/marketing-router/) | Routes ambiguous or multi-discipline requests; appoints one owner |
| [`marketing-intake`](../.agents/skills/marketing-intake/) | Engagement scope, evidence grading, metric definitions, access, authorization |
| [`google-ads`](../.agents/skills/google-ads/) | Search, Shopping, Performance Max audit, diagnosis, change planning |
| [`meta-ads`](../.agents/skills/meta-ads/) | Structure, audiences, delivery, placements, prospecting, retargeting |
| [`creative-strategy`](../.agents/skills/creative-strategy/) | Angles, hooks, concepts, formats, briefs, creative tests |
| [`cro`](../.agents/skills/cro/) | Landing page, product page, form, checkout, persuasion friction |
| [`performance-diagnostics`](../.agents/skills/performance-diagnostics/) | Metric change, spend/sales anomaly, causal triage |
| [`tracking-measurement`](../.agents/skills/tracking-measurement/) | Event integrity, attribution reconciliation, conversion architecture |
| [`customer-research`](../.agents/skills/customer-research/) | Interviews, reviews, surveys, customer language, evidence synthesis |
| [`icp-jtbd`](../.agents/skills/icp-jtbd/) | Priority segments, buying situations, buyer roles, Jobs-to-be-Done |
| [`optimization-scaling`](../.agents/skills/optimization-scaling/) | Scale readiness, marginal economics, portfolio allocation, de-scaling, budget/outcome pacing |
| [`retention-economics`](../.agents/skills/retention-economics/) | Lifetime value, payback period, cohort retention, churn, lead-to-revenue cohorts |
| [`marketing-reporting`](../.agents/skills/marketing-reporting/) | Cross-channel executive report, recurring cadence, stakeholder scorecard |
| [`seo`](../.agents/skills/seo/) | Organic visibility audit, technical health, content strategy, ranking-change diagnosis |
| [`copywriting`](../.agents/skills/copywriting/) | Email, lifecycle, website, sales-page, long-form, brand copywriting |
| [`lifecycle-marketing`](../.agents/skills/lifecycle-marketing/) | Email/lifecycle segmentation, trigger logic, cadence, deliverability |
| [`youtube-ads`](../.agents/skills/youtube-ads/) | YouTube video ad format, targeting, view-through measurement fit |
| [`tiktok-ads`](../.agents/skills/tiktok-ads/) | TikTok native creative fit, Spark Ads vs in-feed, creative-fatigue cadence |
| [`linkedin-ads`](../.agents/skills/linkedin-ads/) | LinkedIn account/firmographic targeting, format selection, Lead Gen Forms, B2B economics |
| [`influencer-marketing`](../.agents/skills/influencer-marketing/) | Influencer/creator vetting, compensation structure, usage rights, disclosure compliance |
| [`affiliate-marketing`](../.agents/skills/affiliate-marketing/) | Affiliate commission structure, attribution integrity, fraud/brand-bidding screening |
| [`organic-social`](../.agents/skills/organic-social/) | Organic content strategy, cadence, algorithm-distribution fit, community management |
| [`programmatic`](../.agents/skills/programmatic/) | Supply-path optimization, inventory verification, fraud screening |
| [`public-relations`](../.agents/skills/public-relations/) | Media relations, pitch strategy, crisis communications |

## Skill structure

Every canonical skill is a directory containing `SKILL.md` with YAML frontmatter (`name`, `description`), and optional `references/` for conditional detail loaded only when relevant.

Each `SKILL.md` must supply a discriminating trigger description, required context, method, decision rules, output contract, and quality assurance — per `AGENTS.md`.

## Validation

`scripts/validate-skill-architecture.sh` enforces packaging, unique names, folder/frontmatter agreement, reference reachability, and the prohibition on any file outside `.agents/skills/` impersonating a canonical skill.

## Proposing a skill

Open a skill proposal issue. New capabilities must arrive as governed skills in `.agents/skills/`, not as Markdown added here.

Historical v1.0 placeholders are retained in [`docs/archive/legacy-skill-stubs/`](../docs/archive/legacy-skill-stubs/) for release history only.
