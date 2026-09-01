# Marketing Context Governance

Use this reference when creating, updating, or relying on a project-level `.agents/marketing-context.md` built from [`templates/marketing-context.md`](../../../../templates/marketing-context.md).

The reusable template lives in the Marketing OS. The active project context lives at `.agents/marketing-context.md`. The Marketing Context is a shared decision-context artifact owned by `$marketing-intake`. It reduces repeated discovery across the Marketing OS while preserving provenance. It does not replace specialist research, product truth, the evidence register, or source systems.

## What belongs in context

Include only information that can change downstream marketing decisions:

- business model, primary business outcome, market, and strategic constraints
- current growth-strategy state when a governed cross-functional plan exists: plan version/horizon, priority constraints, strategic priorities, explicit non-priorities, dependencies, review triggers, exact plan state
- verified product truth and claim boundaries
- priority segments, buying situations, JTBD, buyer/user roles, and exclusions
- customer pain, desired progress, objections, selection criteria, and evidence-backed VOC themes
- positioning, differentiators, alternatives, and competitor implications
- current offer state
- current pricing/monetization state when decision-relevant
- current activation definition/path state when a distinct post-conversion activation layer exists
- current retention-strategy state when repeat/renewal/continuation, lapse, recovery, or win-back is decision-relevant
- proof inventory and allowed claim use
- economics and capacity constraints
- brand, compliance, channel, and funnel constraints
- open decisions and evidence gaps

Do not turn this into a data dump, CRM export, research archive, raw analytics repository, or duplicate roadmap.

## Context lifecycle

### Create

Create `.agents/marketing-context.md` after enough intake exists to support reusable downstream decisions. A partial artifact is allowed when important gaps remain, but it must be labeled `partial` and list the gaps.

### Read

Downstream skills should read the smallest relevant portion. Context is a convenience layer, not a mandatory token tax on every task.

### Update

Update when a decision-relevant fact, verified hypothesis, constraint, or approved strategy materially changes. Preserve the source and evidence state, increment the version, and prepend the change log.

### Stale

Mark the context `stale` when a decision-relevant section is likely outdated and no current source has confirmed it. Current-platform behavior belongs under the relevant platform skill and `PLATFORM-CURRENCY.md`, not here as durable truth.

### Contradicted

Do not silently resolve conflicts. Preserve the competing sources and state what is contradicted. Route the underlying dispute to the skill that owns the decision.

## Evidence rules

- A summary inherits the weakest decision-relevant evidence state beneath it.
- User assertions stay asserted until observed in a named source.
- Customer-reported outcomes remain customer-reported outcomes unless business evidence verifies them.
- A generated synthesis is never promoted to VOC, proof, product truth, willingness-to-pay, activation, retention causality, a verified growth constraint, or a verified buyer belief.
- A strategic priority records a decision under current evidence; it does not prove the mechanism, implement the initiative, or authorize its live mutations.
- A specialist decision may update the context only after the decision artifact exists and its status is clear.
- Context cannot authorize a live change.

## Ownership boundaries

`$marketing-intake` owns the shared context artifact and evidence state.

Specialists own the underlying decisions:

- `$growth-strategy`: cross-functional growth-system map, strategic constraint/opportunity portfolio, prioritization, sequencing, non-priorities, and review/rebalancing decisions
- `$customer-research`: research patterns and traceable VOC
- `$icp-jtbd`: priority segments, buying situations, JTBD, roles, competitive alternative maps, and positioning implications
- `$offer-strategy`: offer diagnosis and approved offer design
- `$pricing-monetization`: base/realized price, value metric, package/tier commercial structure, payment model, discounts, pricing evidence, and price-change state
- `$activation`: whether a distinct activation layer exists, first meaningful value definition, path-to-value, time-to-value, activation barrier, and intervention state
- `$retention-strategy`: retention-state/reason diagnosis, voluntary/involuntary/lapse classification, cause-matched intervention, and durable save/recovery/win-back state
- `$retention-economics`: LTV, payback, cohort retention/churn/repeat economics
- `$tracking-measurement`: measurement integrity, causal evidence, and experiment-learning validity
- channel skills: current channel/platform mechanics

If specialist evidence and Marketing Context disagree, the source decision artifact governs until context is updated.

## Minimum QA

Before marking context `current`, confirm:

1. Decision-relevant statements have a source and evidence state.
2. Unknowns and contradictions are visible.
3. Growth-strategy state, when present, points to the governing plan; priorities/non-priorities keep their evidence state and exact plan status rather than being promoted to proven/implemented.
4. Product claims have an allowed-use boundary.
5. Customer language is traceable when treated as verbatim.
6. Economics name the revenue basis and profit level where used.
7. Pricing terms name their source and exact state rather than treating proposed/configured terms as live.
8. Activation is included only when a distinct layer is decision-relevant; the value event, denominator/window, and definition status come from `$activation`, not from a convenience metric.
9. Retention strategy is included only when continuation behavior is decision-relevant; customer-stated reasons are not promoted to causal facts and short-term saves are not labeled durable before the required window.
10. Current platform details are not fossilized as durable context.
11. The change log explains material revisions.
12. No unnecessary personal data was copied into the artifact.
