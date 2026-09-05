# AI Agent Guide

## Purpose

This guide defines how an AI agent should operate Full-Stack Marketing OS after the skills are available in its runtime.

For installation and GitHub onboarding, start with [`GETTING_STARTED.md`](GETTING_STARTED.md). For the exact runtime/distribution model, see [`DISTRIBUTION.md`](DISTRIBUTION.md).

The canonical executable source is [`.agents/skills/`](.agents/skills/). This guide explains orchestration; it does not replace any owning `SKILL.md`.

## Marketing decision lifecycle

Full-Stack Marketing OS uses one stateful operating lifecycle for marketing decisions and initiatives:

```text
CONTEXT
   ↓
GOAL
   ↓
STRATEGY
   ↓
PLAN
   ↓
EXECUTE
   ↓
REVIEW
   ↓
OPTIMIZE
   ↺
```

The canonical contract is [`workflows/marketing-decision-lifecycle.md`](workflows/marketing-decision-lifecycle.md).

This lifecycle is **not a mandatory seven-step checklist**. Start at the earliest unresolved stage that can materially change the requested decision. Skip stages already satisfied by the request, current Marketing Context, an approved specialist artifact, or verified implementation state.

Examples:

- a simple bounded copy rewrite may start at `execute`
- a performance drop after a campaign change may start at `review`
- an integrated growth-priority request with context and objective already established may start at `strategy`
- an approved creative concept ready for production may start at `execute`
- a proven paid-media system asking for more budget may start at `optimize`, but missing economics can move it back to `context`

Runtimes may expose `/context`, `/goal`, `/strategy`, `/plan`, `/execute`, `/review`, or `/optimize` as interface aliases. They are not canonical skills. They must route to the existing governed owner instead of creating a second instruction hierarchy.

### Stage ownership

| Stage | Question | Default owner |
|---|---|---|
| `context` | What do we know, how do we know it, and what is missing? | `$marketing-intake` when evidence, definitions, economics, scope, or authorization are materially unclear |
| `goal` | What outcome or decision must change? | `$growth-strategy` for business-level objectives; preserve an already-bounded specialist objective when adequate |
| `strategy` | Where will we focus and why? | `$growth-strategy` for integrated business direction; the domain owner for bounded specialist strategy |
| `plan` | Who does what, in what order, with what dependencies? | `$marketing-router` coordinates multi-owner decomposition; specialists retain their decisions |
| `execute` | What should be created, configured, published, or changed now? | Owning specialist plus the actually available authorized runtime/tool |
| `review` | What actually happened relative to the goal and guardrails? | Domain owner, `$performance-diagnostics`, `$tracking-measurement`, `$marketing-reporting`, or `$growth-strategy` as appropriate |
| `optimize` | What should change next given the learning? | Domain owner; `$optimization-scaling` for paid-media scale/de-scale and allocation/coverage expansion |

Use [`templates/marketing-decision-record.md`](templates/marketing-decision-record.md) when continuity across several stages, agents, or sessions matters. Do not create a lifecycle record for every tiny task.

## Operating flow

```text
Request / current initiative state
  ↓
Identify the earliest materially unresolved lifecycle stage
  ↓
Load only decision-relevant Marketing Context / specialist evidence
  ↓
Route to one primary owner
  ↓
Validate evidence, definitions, freshness, economics, and access as required
  ↓
Apply the owner's method and relevant references
  ↓
Route supporting decisions to supporting owners
  ↓
Produce recommendation / artifact / controlled action plan
  ↓
Approval gate for material live mutation
  ↓
Execute through the owning specialist + available runtime when authorized
  ↓
Verify exact implementation state
  ↓
Review mature evidence against the goal and guardrails
  ↓
Continue / hold / revise / kill / reprioritize / route to scaling
  ↓
Record scoped learning / context / lifecycle state when useful
```

A recurring operational process uses [`workflows/marketing-operations-loop.md`](workflows/marketing-operations-loop.md). The decision lifecycle answers **where this decision is**; Marketing Operations answers **how repeated runs are safely triggered and coordinated**.

## 1. Detect the current stage and route before solving

If the owning capability and lifecycle stage are obvious, use that skill directly. If the request is ambiguous, continues prior work, or spans several domains, use `$marketing-router` to identify the current stage, appoint one primary owner, and select only the supporting skills needed for distinct dependencies.

Do not turn a cross-skill task into an ownerless committee. One decision should have one primary owner.

Do not restart at `context` merely because the lifecycle begins there. Conversely, do not skip a blocking earlier stage: a scaling request without decision-grade economics may need `$marketing-intake` before `$optimization-scaling` can decide.

Examples:

- business-level growth priorities → `strategy` or `plan` depending current state → `$growth-strategy`
- Google Ads campaign decision → owning stage → `$google-ads`
- static paid creative ready to produce → `execute` → `$creative-strategy`
- price/package/payment structure → `$pricing-monetization`
- experiment validity / result interpretation → `review` → `$tracking-measurement`
- paid-media scaling readiness → `optimize` → `$optimization-scaling`

[`CAPABILITY-REGISTRY.md`](CAPABILITY-REGISTRY.md) is authoritative when ownership is uncertain.

## 2. Load only relevant context

For substantial downstream work, read the decision-relevant sections of shared Marketing Context when available. Do not load unrelated context merely because it exists.

Marketing Context is a reusable handoff layer, not a competing source of truth. When it conflicts with the underlying specialist artifact or source system, the source decision artifact wins and the contradiction must remain visible until resolved.

A bounded task can treat context as already satisfied when the request itself contains enough safe information. Do not create intake bureaucracy where no decision-relevant gap exists.

## 3. Preserve evidence state

Keep these distinct:

- **Observed:** directly present in a source or system
- **Calculated:** derived from stated inputs/formulas
- **Inferred:** reasoned interpretation of evidence
- **Assumed:** placeholder used because evidence is missing
- **Unknown:** not established

Do not upgrade an inference, competitor observation, customer anecdote, platform recommendation, benchmark, or model-generated statement into verified evidence.

Lifecycle progression never upgrades evidence by itself. Moving from `plan` to `execute`, or from `execute` to `review`, does not make an assumption true.

## 4. Use frameworks as decision aids, not proof

Frameworks organize reasoning. They do not prove that an outcome will occur.

Examples:

- an AIDA structure does not prove copy will convert
- a persuasion principle does not prove an audience will respond
- a competitor tactic does not prove the tactic works
- one experiment does not create a universal best practice
- a 4:5 → 1:1 creative safe-zone rule protects crop resilience; it does not prove platform compliance or performance

When the evidence is insufficient, return the smallest meaningful validation step instead of manufacturing certainty.

Strategy and plan are also not proof. A well-structured strategic choice still needs execution and review evidence before it can be called effective.

## 5. Respect specialist boundaries

Examples of important boundaries:

- `$growth-strategy` decides where the business should focus; `$optimization-scaling` decides whether a proven paid-media system is ready for controlled expansion.
- `$offer-strategy` decides the proposition; `$pricing-monetization` decides the exchange structure.
- `$cro` owns pre-conversion friction; `$activation` owns the path from conversion to first meaningful value.
- `$retention-strategy` chooses cause-matched interventions; `$retention-economics` measures realized cohort behavior and economics.
- `$creative-strategy` owns paid-ad concept/message/visual direction; channel skills own current placement-specific creative-fit requirements.
- `$marketing-reporting` owns recurring communication; `$marketing-operations` owns stateful recurring decision operations.
- `$marketing-router` owns cross-skill routing and lifecycle coordination; it does not inherit the specialist decisions inside a plan.

Do not silently absorb a neighboring capability because it is convenient.

## 6. Distinguish strategy, plan, execution, and implementation state

These are different lifecycle concepts:

- **Strategy:** the chosen direction and why it deserves priority
- **Plan:** owned workstreams, sequence, dependencies, measurement, and decision rules
- **Execute:** create/configure/publish/change through the owning specialist and runtime
- **Review:** compare mature evidence with the goal and guardrails
- **Optimize:** choose the next change from what was learned

Implementation itself also has exact states:

```text
draft → saved/configured → published → live → processing → verified
```

Use only the state that the available evidence supports.

A generated creative is not a live ad. A drafted campaign is not published. A saved setting is not verified in delivery. A recommendation or plan is not implementation.

## 7. Require authorization for material live mutations

A skill may recommend or prepare a change without having permission to execute it.

Before a material live mutation such as spend, publishing, tracking, offer, pricing, or another externally consequential change, check the owning skill's authorization requirements and the current approval scope.

Never reuse approval for a materially changed action, scope, account, amount, or condition unless the authorization explicitly covers it.

The lifecycle does not authorize anything merely by reaching `execute`.

## 8. Do not assume external access

Skills provide decision logic. They do not automatically provide access to external accounts.

If the task needs live Google Ads, Meta, Shopify, GA4, Search Console, Klaviyo, CRM, or another system, use only tools/connectors/MCP/API/browser access that is actually available and authorized. Otherwise work from supplied exports or clearly state the access limitation.

Never fabricate a live read, saved change, publication state, or verification result.

## 9. Review business outcomes, not convenient proxies

Prefer the primary business outcome and relevant economics over isolated platform metrics.

Do not declare success from CTR, CPC, engagement, activation proxy, AOV, ARPU, save acceptance, or another supporting metric when the owning method requires downstream business outcomes or guardrails.

Keep cross-platform attribution claims separate unless a valid deduplicated measurement layer supports aggregation.

At `review`, separate observed result from mechanism interpretation. At `optimize`, choose the next action from the evidence rather than from a generic “best practice.”

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
- lifecycle stage transition when continuity matters

Local evidence may support a local action without becoming doctrine for every client, channel, market, or account.

Optimization may move the work backward as well as forward. New evidence can return the initiative to `context`, `goal`, `strategy`, or `plan` without rewriting prior history.

## Recommended starting prompts

### Unsure which skill or stage to use

```text
$marketing-router Identify the current marketing decision-lifecycle stage, decide which Marketing OS capability should own this request, select only required supporting skills, and name any evidence that blocks the requested decision.
```

### New business growth planning

```text
$growth-strategy Using the decision-relevant context already established, define the business objective if still unresolved, diagnose the current constraint or constraint set, build a prioritized opportunity portfolio, name non-priorities, and route specialist work to the correct owners.
```

### Continue an existing initiative

```text
$marketing-router Continue this initiative from its current verified state. Do not restart completed lifecycle stages. Identify the earliest unresolved stage that can change the next decision, then route it to the correct owner.
```

### Creative strategy

```text
$creative-strategy Turn this verified product/customer evidence into distinct paid-media concepts with explicit hypotheses, proof requirements, production direction, and controlled tests.
```

### Performance change

```text
$performance-diagnostics Review what changed, separate measurement issues from business-performance changes, rank plausible explanations by evidence, and name the next decision-changing check or optimization handoff.
```

### Paid-media scaling

```text
$optimization-scaling Decide whether this paid-media system is ready to scale or de-scale using marginal economics, evidence maturity, capacity, guardrails, and authorization. Reject fixed percentage rules that are not supported by the account evidence.
```

## QA before final output

Before returning a substantial Marketing OS result, check:

- Is the current decision-lifecycle stage correct, and was the workflow kept stateful rather than forced through all seven stages?
- Is there one clear primary decision owner?
- Are facts, calculations, inference, assumptions, and unknowns separated?
- Are current platform claims verified when freshness matters?
- Are relevant business economics and guardrails included?
- Did the answer avoid unsupported benchmarks and universal claims?
- Did any neighboring skill's boundary get crossed without a handoff?
- Are strategy, plan, execution, review, and optimization kept distinct?
- Is implementation state described exactly?
- Is authorization explicit before material live action?
- Does paid-media scaling route to `$optimization-scaling`?
- Is the result scoped enough that another agent could understand what was actually learned and where the initiative should resume?

## Contributor note

Do not edit generated runtime copies in `~/.codex/skills/` or `~/.claude/skills/` as source material. Governed behavior changes belong under [`.agents/skills/`](.agents/skills/), with references/evaluations updated according to [`AGENTS.md`](AGENTS.md).