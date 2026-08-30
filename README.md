# Full-Stack Marketing OS

![GitHub](https://img.shields.io/badge/status-public-brightgreen)
![Version](https://img.shields.io/badge/version-v1.18.0-blue)
![Focus](https://img.shields.io/badge/focus-AI%20Marketing-purple)

An evidence-led full-stack marketing skills and operating system for planning, auditing, diagnosing, and improving full-funnel marketing.

Built to help AI agents and modern marketing teams work with structured marketing knowledge instead of isolated prompts.

GitHub is the versioned source of truth. The system brings together governed skills, frameworks, playbooks, templates, workflows, and evaluations for Google Ads, Meta Ads, creative strategy, CRO, SEO, lifecycle marketing, and measurement.

## Quickstart

**Claude Code** — install all 24 skills as a plugin:

```
/plugin marketplace add vinceservidad/full-stack-marketing-os
/plugin install full-stack-marketing-os@full-stack-marketing-os
```

**Codex, Claude Code, or any agent that reads a local skills directory** — clone and install:

```bash
git clone https://github.com/vinceservidad/full-stack-marketing-os.git
cd full-stack-marketing-os
scripts/install-skills.sh                 # installs to every runtime found (~/.claude, ~/.codex)
scripts/install-skills.sh --target codex  # or name one
scripts/install-skills.sh --dry-run       # or see what it would do first
```

The script copies the canonical skills, installs the root contracts and libraries
they link to, rewrites link depth for the install location, and fails if any link
does not resolve. It is verified on Linux and macOS in CI.

**Then ask for something:**

```text
Audit this Google Ads account. Business is DTC skincare, £40k/month spend,
I have the search terms export and Shopify revenue but no COGS yet.
```

The system will route to `$marketing-intake` before it audits anything, because
profitability cannot be concluded without a cost structure. That refusal is the
product working, not failing — see [`examples/`](examples/) for three worked runs.

**Verify it yourself:**

```bash
python3 scripts/eval.py --static   # 415 decision cases parse, register, and resolve
```

## System Map

```text
Marketing Request
        ↓
Marketing Router
        ↓
Specialist Skill
        ↓
Framework
        ↓
Playbook
        ↓
Template
        ↓
Workflow
        ↓
Evaluation
        ↓
Final Deliverable
```

## What it covers

Twenty-four governed skills live in [`.agents/skills/`](.agents/skills/) — the canonical executable layer:

- Request routing and owner appointment
- Engagement intake: scope, evidence grading, metric definitions, access, authorization
- Google Ads: Search, Shopping, Performance Max
- Meta Ads: structure, audiences, delivery, placements
- Creative strategy: angles, hooks, concepts, briefs, tests
- Conversion Rate Optimization: pages, forms, checkout, friction
- Performance diagnosis: metric change, anomaly, causal triage
- Tracking and measurement: event integrity, attribution reconciliation
- Customer research: interviews, reviews, surveys, evidence synthesis
- Ideal Customer Profile and Jobs-to-be-Done
- Retention economics: lifetime value, payback period, cohort retention, churn
- Marketing reporting: cross-channel executive report, recurring cadence, stakeholder scorecard
- Search Engine Optimization: visibility audit, technical health, content strategy, ranking-change diagnosis
- Copywriting: email, lifecycle, website, sales-page, long-form, brand
- Lifecycle marketing: email/lifecycle segmentation, trigger logic, cadence, deliverability
- YouTube Ads: video format selection, targeting, view-through measurement fit
- TikTok Ads: native creative fit, Spark Ads vs in-feed, creative-fatigue cadence
- LinkedIn Ads: account/firmographic targeting, format selection, Lead Gen Forms, B2B economics
- Influencer Marketing: creator vetting, compensation structure, usage rights, disclosure compliance
- Affiliate Marketing: commission structure, attribution integrity, fraud/brand-bidding screening
- Organic Social: content strategy, cadence, algorithm-distribution fit, community management
- Programmatic: supply-path optimization, inventory verification, fraud screening
- Public Relations: media relations, pitch strategy, crisis communications
- Evidence-led optimization and scaling across channels, portfolios, creative, ecommerce, and lead generation

Analytics is **partially covered** — specific tasks are owned, others are not. Every other capability originally listed as unsupported is now governed, including reporting (by `$marketing-reporting` for cross-channel/recurring work and by each channel's owning skill for bounded reports), Search Engine Optimization, copywriting, email and lifecycle marketing, YouTube, TikTok, LinkedIn, influencer and affiliate partnerships, organic social, programmatic buying, and public relations.

[`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative on exactly which tasks are governed, partially covered, planned, or unsupported. The Marketing Router declares the gap rather than substituting an adjacent channel skill.

## Repository Structure

`.agents/skills/` is the **canonical executable layer**. Everything else is knowledge, documentation, or export material — no other directory contains runnable skills.

```text
.agents/skills/        CANONICAL — governed, agent-loadable operating skills
skills/                Index only — points to .agents/skills/, no instructions
frameworks/            Decision models and methods (knowledge library)
playbooks/             Scenario workflows (knowledge library)
templates/             Reusable deliverable formats (artifact library)
workflows/             Execution sequences (workflow library)
agents/                Agent-role documentation (non-executable)
gpt-knowledge/         Custom GPT export layer (derived, not a skill layer)
evaluations/           Routing cases and reviewer checklists
tests/evaluations/     Versioned decision-behavior cases (415, all executable)
examples/              Worked runs with reproducible input fixtures
scripts/               Installer and validation harnesses
.claude-plugin/        Claude Code plugin and marketplace manifests
docs/                  Guides; docs/archive/ is excluded from active retrieval
```

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for each layer's consumer and canonical status, and [`ARTIFACT-OWNERSHIP.md`](ARTIFACT-OWNERSHIP.md) for which artifacts have owners.

A file's presence in this repository does not make it part of the operating system. An artifact is operational when a skill owns it, its evidence state is declared, and validation covers it.

## Creator

Built by Vince Servidad, a Paid Acquisition Specialist focused on Google Ads, Meta Ads, Shopify growth, CRO, and AI marketing systems.

The goal is to organize practical marketing knowledge into reusable systems that help marketers and AI agents make better decisions.

## Example Usage

```text
Use the Google Ads skill to audit campaign performance.

Use the Creative Strategy skill to build testing ideas.

Use the CRO skill to review a Shopify product page.

Use the Performance Diagnostics skill to analyze a metric change and next actions.

Use the Optimization and Scaling skill to decide whether, where, how, and by how much to scale while protecting commercial outcomes.
```

Scaling is not defined as spending more. The system requires a scoped proof level, source-of-truth business economics, marginal efficiency, a diagnosed binding constraint, an appropriate scaling mode, capacity, guardrails, and explicit approval before any live change. It rejects universal budget-increase percentages and does not treat platform attribution or recommendations as proof.

## Design Principles

- Evidence before assumptions
- Strategy before tactics
- Business goals before platform settings
- Frameworks before random execution
- Human judgment before automation

## Roadmap

- Publish a scored `tests/RESULTS.md` from a full live evaluation run. The harness is built and the corpus is registered; **no behavioral pass rate is claimed anywhere in this repository until that run is committed.**
- Normalize `cro`, `marketing-router`, and `performance-diagnostics` to a dedicated required-inputs heading (currently satisfied in prose; tracked as skill-content debt, not a structural gap)
- Validate against anonymized real-world cases, as distinct from the synthetic fixtures in `examples/`
- More industry playbooks and worked examples

See [`ROADMAP.md`](ROADMAP.md) for the full history.
