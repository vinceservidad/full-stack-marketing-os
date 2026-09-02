# Full-Stack Marketing OS

![GitHub](https://img.shields.io/badge/status-public-brightgreen)
![Version](https://img.shields.io/badge/version-v1.18.0-blue)
![Focus](https://img.shields.io/badge/focus-AI%20Marketing-purple)

An evidence-led full-stack marketing skill and operating system for planning, auditing, diagnosing, creating, testing, and improving full-funnel marketing.

Built to help AI agents and modern marketing teams work from governed marketing knowledge instead of isolated prompts, copied playbooks, or unsupported “best practices.”

GitHub is the versioned source of truth. The system combines governed skills, frameworks, playbooks, templates, workflows, shared context, and behavioral evaluations.

## Start here

New to the repository? Read **[`GETTING_STARTED.md`](GETTING_STARTED.md)** first.

It covers the complete path:

```text
GitHub
  ↓
Clone / download
  ↓
Install to Codex or Claude Code
  ↓
Verify
  ↓
Choose a skill or use $marketing-router
  ↓
Provide evidence
  ↓
Run the governed workflow
  ↓
Update from GitHub when the OS changes
```

For AI-agent orchestration rules after installation, see [`AGENT_GUIDE.md`](AGENT_GUIDE.md). For runtime, plugin, MCP, connector, and Custom GPT distinctions, see [`DISTRIBUTION.md`](DISTRIBUTION.md).

## What this is

Full-Stack Marketing OS is currently a **portable skill system**, not a packaged marketplace plugin.

- **OpenAI Codex:** supported as installable local skills.
- **Claude Code:** supported as installable personal skills, with `CLAUDE.md` importing the repository-wide `AGENTS.md` rules.
- **Custom GPT:** supported through the derived `gpt-knowledge/` knowledge-export layer.
- **OpenAI plugin / Claude plugin:** not packaged yet. A future plugin can bundle the governed skills with tools/connectors while keeping `.agents/skills/` canonical.

See [`DISTRIBUTION.md`](DISTRIBUTION.md) for exact install paths, terminology, current support state, and plugin boundaries.

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
python3 scripts/eval.py --static   # 873 decision cases parse, register, and resolve
```

## System Map

```text
Business / Marketing Request
        ↓
Marketing Router
        ↓
Growth Strategy or Specialist Owner
        ↓
Framework / Method
        ↓
Playbook / Template / Workflow
        ↓
Measurement + Evaluation
        ↓
Decision / Deliverable / Learning
```

## Governed capabilities

Thirty governed skills currently live in [`.agents/skills/`](.agents/skills/), the canonical executable layer.

### Strategy, context, commercial, and customer system

- `$marketing-router` — request routing and owner appointment
- `$marketing-intake` — scope, evidence state, metric definitions, access, authorization, shared Marketing Context
- `$growth-strategy` — business-level growth priorities, constraint/constraint-set diagnosis, opportunity portfolio, sequencing, learning roadmap
- `$customer-research` — interviews, reviews, surveys, evidence synthesis
- `$icp-jtbd` — ICP, Jobs-to-be-Done, buying situations, alternatives, competitive intelligence
- `$offer-strategy` — proposition, value architecture, bundle, proof requirements, risk reversal, legitimate urgency/scarcity
- `$pricing-monetization` — price, value metric, packages/tiers, payment model, discount architecture, willingness-to-pay evidence

### Acquisition, creative, and conversion

- `$google-ads` — Search, Shopping, Performance Max
- `$meta-ads` — structure, audiences, delivery, placements
- `$youtube-ads` — paid-video format, targeting, measurement fit
- `$tiktok-ads` — native creative fit, Spark Ads vs in-feed, targeting/cadence
- `$linkedin-ads` — firmographic/account targeting, Lead Gen Forms, B2B economics
- `$programmatic` — supply-path optimization, inventory verification, fraud screening
- `$influencer-marketing` — creator vetting, compensation, rights, disclosure
- `$affiliate-marketing` — commission structure, attribution integrity, fraud/brand-bidding screening
- `$organic-social` — content strategy, cadence, distribution fit, community management
- `$public-relations` — media relations, pitch strategy, crisis communications
- `$seo` — technical health, organic visibility, content/topic strategy, ranking diagnosis
- `$creative-strategy` — angles, mechanics, hooks, concepts, visual formats, static creative direction, testing
- `$copywriting` — lifecycle, website, sales-page, long-form, and brand copy
- `$cro` — landing/product pages, forms, checkout, and pre-conversion friction

### Activation, retention, measurement, scaling, and operations

- `$activation` — first meaningful value, path-to-value, time-to-value, activation friction
- `$retention-strategy` — churn/lapse reason diagnosis, save/recovery/repeat/renewal/win-back strategy
- `$retention-economics` — LTV, payback, cohort retention/churn, lead-to-revenue maturation
- `$lifecycle-marketing` — segmentation, trigger logic, cadence, suppression, deliverability
- `$tracking-measurement` — event integrity, attribution reconciliation, causal validity, experiment learning
- `$performance-diagnostics` — metric change, anomaly, competing explanations, causal triage
- `$optimization-scaling` — paid-media readiness, marginal economics, controlled scaling/de-scaling, pacing
- `$marketing-operations` — recurring cross-skill loops, state, idempotency, approval, verification, escalation
- `$marketing-reporting` — cross-channel executive reporting, recurring reporting cadence, stakeholder scorecards

Analytics remains **partially covered** where work becomes business-intelligence engineering, warehouse/pipeline design, or dashboard implementation outside the governed analytics owners.

[`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative. A file existing in the repository does not make a capability governed.

## Cross-agent installation

### Codex

```bash
bash scripts/install-skills.sh . "$HOME/.codex"
```

This installs generated runtime copies to `~/.codex/skills/` plus the contracts and libraries needed by those skills.

### Claude Code

```bash
bash scripts/install-claude-skills.sh
```

This installs the same canonical skill set to `~/.claude/skills/`. Do not maintain a second Claude-specific skill hierarchy.

For clone, verification, updating, troubleshooting, skill selection, and concrete usage examples, use [`GETTING_STARTED.md`](GETTING_STARTED.md).

## Repository structure

`.agents/skills/` is the **canonical executable source**. Runtime copies and exports are derived.

```text
.agents/skills/        CANONICAL — governed portable operating skills
~/.codex/skills/       GENERATED — local Codex runtime install
~/.claude/skills/      GENERATED — local Claude Code personal-skill install
.claude-plugin/        Claude Code plugin and marketplace manifests
skills/                Index only — no competing instructions
frameworks/            Governed decision models and methods
playbooks/             Governed scenario workflows
templates/             Governed reusable deliverable structures
workflows/             Governed execution sequences
agents/                Agent-role documentation, non-executable
gpt-knowledge/         Derived Custom GPT export, generated from .agents/skills/
evaluations/           Routing cases and reviewer checklists
tests/evaluations/     Versioned decision-behavior cases, all executable
examples/              Worked walkthroughs to WORKED-EXAMPLE-STANDARD.md
scripts/               Installer, validation, and evaluation harnesses
docs/                  Guides; docs/archive/ excluded from active retrieval
```

See [`ARCHITECTURE.md`](ARCHITECTURE.md), [`ARTIFACT-OWNERSHIP.md`](ARTIFACT-OWNERSHIP.md), and [`DISTRIBUTION.md`](DISTRIBUTION.md).

## Example usage

```text
$growth-strategy Decide where the business should focus next from the evidence I provide.

$google-ads Audit current campaign performance and separate observations from assumptions.

$creative-strategy Turn verified research into testable ad concepts and production-ready static directions.

$marketing-router Decide which Marketing OS skill should own this request when I am not sure.
```

More worked prompts and a skill-selection table are in [`GETTING_STARTED.md`](GETTING_STARTED.md).

## Worked examples

Want to see the OS make a decision end-to-end? Start in [`examples/`](examples/).

Flagship walkthroughs:

- [`Ecommerce Growth Diagnosis`](examples/ecommerce-growth/) — business objective → evidence → constraint set → specialist handoffs → non-priorities → measurement
- [`Google Ads Audit`](examples/google-ads-audit/) — query/product/margin/marginal-efficiency diagnosis without blanket channel rules
- [`Meta Ads Audit & Creative Testing`](examples/meta-ads/) — attribution reconciliation → prospecting/retargeting → creative quality → frequency/audience diagnosis → controlled testing → scaling gate
- [`DTC Creative Strategy`](examples/creative-strategy/) — synthetic VOC → JTBD → angle → mechanic → concept → 4:5 production direction → centered 1:1 cross-crop validation
- [`Shopify CRO Audit`](examples/shopify-cro/) — funnel evidence → mobile checkout diagnosis → focused hypothesis instead of full-site redesign

These are **worked examples**, not performance case studies. Synthetic/anonymized examples demonstrate how the system decides; verified public case studies require real publishable evidence. See [`examples/WORKED-EXAMPLE-STANDARD.md`](examples/WORKED-EXAMPLE-STANDARD.md).

Scaling is not defined as spending more. The system requires source-of-truth business evidence, economics, marginal efficiency, readiness, constraints, capacity, guardrails, and explicit authorization before any live change. It rejects universal budget-increase percentages and does not treat platform attribution or recommendations as proof.

## Design principles

- Evidence before assumptions
- Strategy before tactics
- Business outcomes before platform metrics
- One owner per decision
- Frameworks organize thinking; they do not prove outcomes
- Reversible learning before large irreversible commitments
- Human judgment before automation
- Canonical source before runtime/export copies

## Roadmap

The detailed, reconciled roadmap is in [`ROADMAP.md`](ROADMAP.md). Current priorities are:

- publish a scored `tests/RESULTS.md` from a full live evaluation run — the harness is built and the corpus registered, so **no behavioral pass rate is claimed anywhere in this repository until that run is committed**
- validate high-value skills against anonymized real-world cases where permission and evidence allow
- document data contracts and define MCP/connector approval, rollback, and verification boundaries before adding live integrations
- add maintainability checks that prevent stale capability counts, roadmap claims, and public-navigation drift
- expand behavioral evaluations and worked examples only when real usage exposes a decision-quality gap

## Creator

Built by Vince Servidad, a Paid Acquisition Specialist focused on Google Ads, Meta Ads, Shopify growth, CRO, creative strategy, and AI marketing systems.
