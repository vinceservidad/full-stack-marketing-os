# AI Agent Guide

## Purpose

This guide defines how an AI agent should operate Full-Stack Marketing OS after the skills are available in its runtime.

For installation and GitHub onboarding, start with [`GETTING_STARTED.md`](GETTING_STARTED.md). For the exact runtime/distribution model, see [`DISTRIBUTION.md`](DISTRIBUTION.md).

The canonical executable source is [`.agents/skills/`](.agents/skills/). This guide explains orchestration; it does not replace any owning `SKILL.md`.

## Operating flow

```text
Request
  ↓
Clarify the decision and scope
  ↓
Load relevant Marketing Context when available
  ↓
Route to one primary owner
  ↓
Validate evidence, definitions, freshness, and access
  ↓
Apply the owner's method and relevant references
  ↓
Route supporting decisions to supporting owners
  ↓
Produce recommendation / artifact / controlled action plan
  ↓
Approval gate for material live mutation
  ↓
Verify exact implementation state
  ↓
Record scoped learning / context update when appropriate
```

## 1. Route before solving

If the owning capability is obvious, use that skill directly. If it is ambiguous or spans several domains, use `$marketing-router` to appoint one primary owner and only the supporting skills needed for the decision.

Do not turn a cross-skill task into an ownerless committee. One decision should have one primary owner.

Examples:

- business-level growth priorities → `$growth-strategy`
- Google Ads campaign decision → `$google-ads`
- static paid creative → `$creative-strategy`
- price/package/payment structure → `$pricing-monetization`
- experiment validity → `$tracking-measurement`
- paid-media scaling readiness → `$optimization-scaling`

[`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative when ownership is uncertain.

## 2. Load only relevant context

For substantial downstream work, read the decision-relevant sections of shared Marketing Context when available. Do not load unrelated context merely because it exists.

Marketing Context is a reusable handoff layer, not a competing source of truth. When it conflicts with the underlying specialist artifact or source system, the source decision artifact wins and the contradiction must remain visible until resolved.

## 3. Preserve evidence state

Keep these distinct:

- **Observed:** directly present in a source or system
- **Calculated:** derived from stated inputs/formulas
- **Inferred:** reasoned interpretation of evidence
- **Assumed:** placeholder used because evidence is missing
- **Unknown:** not established

Do not upgrade an inference, competitor observation, customer anecdote, platform recommendation, benchmark, or model-generated statement into verified evidence.

## 4. Use frameworks as decision aids, not proof

Frameworks organize reasoning. They do not prove that an outcome will occur.

Examples:

- an AIDA structure does not prove copy will convert
- a persuasion principle does not prove an audience will respond
- a competitor tactic does not prove the tactic works
- one experiment does not create a universal best practice
- a 4:5 → 1:1 creative safe-zone rule protects crop resilience; it does not prove platform compliance or performance

When the evidence is insufficient, return the smallest meaningful validation step instead of manufacturing certainty.

## 5. Respect specialist boundaries

Examples of important boundaries:

- `$growth-strategy` decides where the business should focus; `$optimization-scaling` decides whether a proven paid-media system is ready for controlled expansion.
- `$offer-strategy` decides the proposition; `$pricing-monetization` decides the exchange structure.
- `$cro` owns pre-conversion friction; `$activation` owns the path from conversion to first meaningful value.
- `$retention-strategy` chooses cause-matched interventions; `$retention-economics` measures realized cohort behavior and economics.
- `$creative-strategy` owns paid-ad concept/message/visual direction; channel skills own current placement-specific creative-fit requirements.
- `$marketing-reporting` owns recurring communication; `$marketing-operations` owns stateful recurring decision operations.

Do not silently absorb a neighboring capability because it is convenient.

## 6. Distinguish recommendation from implementation

These are different states:

```text
draft → saved/configured → published → live → processing → verified
```

Use only the state that the available evidence supports.

A generated creative is not a live ad. A drafted campaign is not published. A saved setting is not verified in delivery. A recommendation is not implementation.

## 7. Require authorization for material live mutations

A skill may recommend or prepare a change without having permission to execute it.

Before a material live mutation such as spend, publishing, tracking, offer, pricing, or another externally consequential change, check the owning skill's authorization requirements and the current approval scope.

Never reuse approval for a materially changed action, scope, account, amount, or condition unless the authorization explicitly covers it.

## 8. Do not assume external access

Skills provide decision logic. They do not automatically provide access to external accounts.

If the task needs live Google Ads, Meta, Shopify, GA4, Search Console, Klaviyo, CRM, or another system, use only tools/connectors/MCP/API/browser access that is actually available and authorized. Otherwise work from supplied exports or clearly state the access limitation.

Never fabricate a live read, saved change, publication state, or verification result.

## 9. Measure business outcomes, not convenient proxies

Prefer the primary business outcome and relevant economics over isolated platform metrics.

Do not declare success from CTR, CPC, engagement, activation proxy, AOV, ARPU, save acceptance, or another supporting metric when the owning method requires downstream business outcomes or guardrails.

Keep cross-platform attribution claims separate unless a valid deduplicated measurement layer supports aggregation.

## 10. Record learning at the right scope

A valid result should retain:

- decision and hypothesis
- tested population/surface/geography/time window
- treatment/control or compared states
- primary business outcome and guardrails
- measurement validity
- observed result
- mechanism interpretation separated from observation
- transfer limits
- next decision

Local evidence may support a local action without becoming doctrine for every client, channel, market, or account.

## Recommended starting prompts

### Unsure which skill to use

```text
$marketing-router Decide which Marketing OS capability should own this request, what supporting skills are needed, and what evidence is missing before action.
```

### Business growth planning

```text
$growth-strategy Diagnose the current growth constraint or constraint set, build a prioritized opportunity portfolio, name non-priorities, and route specialist work to the correct owners.
```

### Creative strategy

```text
$creative-strategy Turn this verified product/customer evidence into distinct paid-media concepts with explicit hypotheses, proof requirements, production direction, and controlled tests.
```

### Performance change

```text
$performance-diagnostics Explain what changed, separate measurement issues from business-performance changes, rank plausible explanations by evidence, and name the next decision-changing check.
```

## QA before final output

Before returning a substantial Marketing OS result, check:

- Is there one clear primary decision owner?
- Are facts, calculations, inference, assumptions, and unknowns separated?
- Are current platform claims verified when freshness matters?
- Are relevant business economics and guardrails included?
- Did the answer avoid unsupported benchmarks and universal claims?
- Did any neighboring skill's boundary get crossed without a handoff?
- Is implementation state described exactly?
- Is authorization explicit before material live action?
- Is the result scoped enough that another agent could understand what was actually learned?

## Contributor note

Do not edit generated runtime copies in `~/.codex/skills/` or `~/.claude/skills/` as source material. Governed behavior changes belong under [`.agents/skills/`](.agents/skills/), with references/evaluations updated according to [`AGENTS.md`](AGENTS.md).
