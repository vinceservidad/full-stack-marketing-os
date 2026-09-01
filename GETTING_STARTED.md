# Getting Started

This guide is the shortest path from the GitHub repository to using Full-Stack Marketing OS in an AI agent.

Full-Stack Marketing OS is a **portable skill system**. GitHub is the versioned source of truth; GitHub itself does not execute the skills. The canonical skill source is [`.agents/skills/`](.agents/skills/).

## 1. Get the repository

Clone it with Git:

```bash
git clone https://github.com/vinceservidad/full-stack-marketing-os.git
cd full-stack-marketing-os
```

Or download the repository ZIP from GitHub, extract it, and open a terminal in the extracted folder.

Do not copy individual `SKILL.md` files out of context unless you also preserve the references and root contracts they depend on. The supplied installers handle those dependencies.

## 2. Choose where you want to use it

### OpenAI Codex

Install the complete governed skill set:

```bash
bash scripts/install-skills.sh . "$HOME/.codex"
```

Generated runtime copies are installed under:

```text
~/.codex/skills/
```

The installer also copies the root contracts and governed libraries needed by the skills, rewrites installed relative links, and fails if required links do not resolve.

### Claude Code

Install the same canonical skill set:

```bash
bash scripts/install-claude-skills.sh
```

Generated runtime copies are installed under:

```text
~/.claude/skills/
```

When Claude Code works inside this repository, root [`CLAUDE.md`](CLAUDE.md) imports [`AGENTS.md`](AGENTS.md) so repository-wide governance stays shared instead of being duplicated.

### Custom GPT knowledge

[`gpt-knowledge/`](gpt-knowledge/) is a derived knowledge-export layer. It can provide reference material to a Custom GPT, but it is **not** the canonical executable skill layer and does not replace [`.agents/skills/`](.agents/skills/).

See [`DISTRIBUTION.md`](DISTRIBUTION.md) for the current support matrix and the distinction between skills, knowledge exports, connectors/MCP, and future plugin packages.

## 3. Verify the install

A successful installer prints the number of installed skills and confirms that linked root contracts resolve.

You can also check that representative skills exist:

### Codex

```bash
test -f "$HOME/.codex/skills/marketing-router/SKILL.md" && echo "marketing-router installed"
test -f "$HOME/.codex/skills/creative-strategy/SKILL.md" && echo "creative-strategy installed"
test -f "$HOME/.codex/skills/google-ads/SKILL.md" && echo "google-ads installed"
```

### Claude Code

```bash
test -f "$HOME/.claude/skills/marketing-router/SKILL.md" && echo "marketing-router installed"
test -f "$HOME/.claude/skills/creative-strategy/SKILL.md" && echo "creative-strategy installed"
test -f "$HOME/.claude/skills/google-ads/SKILL.md" && echo "google-ads installed"
```

If the installer reports an unresolved link, treat the installation as failed instead of using a partial skill copy.

## 4. Use the Marketing Router when you are unsure

You do not need to memorize all governed skills.

If you know the owner, name it directly. In Codex, an explicit skill invocation can use the `$skill-name` form supported by the runtime. For example:

```text
$creative-strategy Build a static-ad testing plan from these customer reviews and product facts.
```

```text
$google-ads Audit this campaign data and tell me what to change, what not to change, and why.
```

If you do not know the owner, start with the router:

```text
$marketing-router I need to improve ecommerce growth. Decide which Marketing OS skills should own the diagnosis and in what order.
```

In other compatible agents, ask for the skill by its governed name when explicit `$` invocation is not supported.

## 5. Pick the right skill

Use this quick map for common jobs:

| Need | Primary owner |
|---|---|
| Decide where the business should focus | `$growth-strategy` |
| Decide which skill owns a request | `$marketing-router` |
| Establish scope, evidence, metrics, access, and shared context | `$marketing-intake` |
| Google Ads | `$google-ads` |
| Meta Ads | `$meta-ads` |
| Paid creative angles, hooks, concepts, static direction | `$creative-strategy` |
| Website, lifecycle, sales-page, or long-form copy | `$copywriting` |
| Landing page, PDP, form, checkout, pre-conversion friction | `$cro` |
| Customer interviews, surveys, reviews, VOC | `$customer-research` |
| ICP, JTBD, buying situations, competitive alternatives | `$icp-jtbd` |
| Offer proposition and value architecture | `$offer-strategy` |
| Price, packages, tiers, payment model | `$pricing-monetization` |
| First meaningful post-conversion value | `$activation` |
| Churn, saves, repeat purchase, renewal, win-back | `$retention-strategy` |
| LTV, payback, cohort retention/churn | `$retention-economics` |
| Tracking, attribution, experiment validity | `$tracking-measurement` |
| Diagnose a performance change | `$performance-diagnostics` |
| Decide whether/how paid media is ready to scale | `$optimization-scaling` |
| Stateful recurring marketing checks/actions | `$marketing-operations` |
| Cross-channel reporting and scorecards | `$marketing-reporting` |

[`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative when a task is not obvious from this table.

## 6. Give the skill evidence, not just a request

The OS is designed to separate observed facts, calculated values, inference, assumptions, and unknowns. Better inputs produce better decisions.

Useful inputs can include:

- the business objective and decision to make
- current product/offer/pricing truth
- target segment, geography, and buying situation
- campaign or funnel data with date ranges and metric definitions
- customer research or traceable reviews
- current creative, landing pages, or screenshots
- unit economics and operational constraints
- what the agent is authorized to change

Do not invent missing data just to complete a framework. A valid output may identify an evidence gap or recommend a smaller validation step first.

## 7. Understand what Skills do not provide by themselves

Installing the Marketing OS gives the agent the **decision system**. It does not automatically give the agent credentials or live access to Google Ads, Meta, Shopify, GA4, Search Console, Klaviyo, or another external platform.

Without a connected tool, MCP server, connector, API, browser session, or supplied export, the skill works from the evidence actually available to the agent.

The intended separation is:

```text
Marketing OS Skills = reasoning / decision system
MCP / connector / API = optional live data and action layer
Plugin = optional future distribution bundle
```

## 8. Approval and live changes

The repository defaults to evidence-led, reviewable work.

A recommendation, draft, saved configuration, published change, live state, processing state, and verified result are different states. Do not describe a live mutation as completed unless the relevant system confirms it.

Changes involving spend, publishing, tracking, offers, pricing, or another material live mutation require the authorization defined by the owning skill and repository governance.

## 9. Update your installed skills

The GitHub repository remains the source of truth. To update a clone:

```bash
git pull
```

Then reinstall the runtime copy.

### Codex

```bash
bash scripts/install-skills.sh . "$HOME/.codex"
```

### Claude Code

```bash
bash scripts/install-claude-skills.sh
```

Do not edit `~/.codex/skills/` or `~/.claude/skills/` and treat those generated copies as the new source. Make governed changes under [`.agents/skills/`](.agents/skills/) and reinstall.

## 10. If you are contributing through GitHub

Read these before changing governed behavior:

1. [`AGENTS.md`](AGENTS.md) — repository-wide operating rules
2. [`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) — capability ownership and support state
3. [`KNOWLEDGE-TAXONOMY.md`](KNOWLEDGE-TAXONOMY.md) — artifact classification
4. [`ARTIFACT-OWNERSHIP.md`](ARTIFACT-OWNERSHIP.md) — root artifact ownership
5. [`PLATFORM-CURRENCY.md`](PLATFORM-CURRENCY.md) — current platform-claim governance
6. [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow

Before a behavior-changing PR, run the repository validators and add or update behavioral evaluations when required.

## Example workflows

### Ecommerce growth diagnosis

```text
$growth-strategy Diagnose the current growth constraint or constraint set from the evidence I provide. Build a prioritized opportunity portfolio, name non-priorities, and route specialist work to the correct Marketing OS owners.
```

### Static paid creative

```text
$creative-strategy Use the verified customer and product evidence to create distinct paid-social concepts. For 4:5 static assets that must survive a square crop, keep critical meaning inside the governed centered 1:1 cross-crop core and validate the actual derivative crop.
```

### Paid-media scaling

```text
$optimization-scaling Decide whether this campaign is ready to scale from the supplied economics, marginal performance, capacity, and evidence. Do not invent a universal budget-increase percentage.
```

### Cross-channel reporting

```text
$marketing-reporting Build an executive report that keeps platform-reported attribution separate instead of summing incompatible conversion claims.
```

## Where to go next

- New user: start here, then use `$marketing-router` when ownership is unclear.
- Runtime/distribution question: read [`DISTRIBUTION.md`](DISTRIBUTION.md).
- Architecture question: read [`ARCHITECTURE.md`](ARCHITECTURE.md).
- Skill-specific behavior: open the owning [`.agents/skills/<skill>/SKILL.md`](.agents/skills/) and load its references only when their scope applies.
