# Full-Stack Marketing OS

![GitHub](https://img.shields.io/badge/status-public-brightgreen)
![Version](https://img.shields.io/badge/version-v1.1.0-blue)
![Focus](https://img.shields.io/badge/focus-AI%20Marketing-purple)

An evidence-led AI marketing operating system for planning, auditing, diagnosing, and improving full-funnel marketing.

Built to help AI agents work with structured marketing knowledge instead of isolated prompts.

GitHub is the versioned source of truth. AI agents use the system through structured skills, frameworks, playbooks, templates, workflows, and evaluations.

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

Nineteen governed skills live in [`.agents/skills/`](.agents/skills/) — the canonical executable layer:

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
- Evidence-led optimization and scaling across channels, portfolios, creative, ecommerce, and lead generation

Analytics is **partially covered** — specific tasks are owned, others are not. Reporting, Search Engine Optimization, and copywriting are governed: reporting by `$marketing-reporting` for cross-channel/recurring work and by each channel's owning skill for bounded reports, SEO by `$seo`, and copywriting by `$copywriting` outside the paid-ad and conversion-page copy `$creative-strategy` and `$cro` already own. Search Engine Optimization, email and lifecycle, TikTok, LinkedIn, affiliate, and influencer marketing are **not covered** by a governed specialist.

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
evaluations/           Quality checks
tests/evaluations/     Versioned decision-behavior cases
examples/              Practical demonstrations
docs/archive/          Historical material, excluded from active retrieval
```

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for each layer's consumer and canonical status, and [`ARTIFACT-OWNERSHIP.md`](ARTIFACT-OWNERSHIP.md) for which artifacts have owners.

A file's presence in this repository does not make it part of the operating system. An artifact is operational when a skill owns it, its evidence state is declared, and validation covers it.

## Creator

Built by Vince Servidad, a Paid Acquisition Specialist focused on Google Ads, Meta Ads, Shopify growth, CRO, and AI marketing systems.

The goal is to organize practical marketing knowledge into reusable systems that help marketers and AI agents make better decisions.

## Why Work With Me

I focus on more than launching campaigns.

I combine paid acquisition, conversion optimization, creative strategy, and AI marketing systems to build workflows that are easier to test, improve, and scale.

My approach:

- Data-driven paid acquisition with Google Ads and Meta Ads
- Conversion-focused thinking beyond clicks and traffic
- Creative testing based on customer psychology and performance data
- Shopify and ecommerce growth optimization
- Building repeatable marketing systems with AI

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

- Reporting, retention economics, and intake specialists
- Measurement validity and incrementality method selection
- Clearing artifact migration debt into skill-owned references
- More industry playbooks and evaluation scenarios
- Deliberate channel expansion, starting with email and lifecycle
