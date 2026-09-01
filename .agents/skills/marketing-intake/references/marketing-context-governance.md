# Marketing Context Governance

Use this reference when creating, updating, or relying on a project-level `.agents/marketing-context.md` built from [`templates/marketing-context.md`](../../../../templates/marketing-context.md).

The reusable template lives in the Marketing OS. The active project context lives at `.agents/marketing-context.md`. The Marketing Context is a shared decision-context artifact owned by `$marketing-intake`. It reduces repeated discovery across the Marketing OS while preserving provenance. It does not replace specialist research, product truth, the evidence register, or source systems.

## What belongs in context

Include only information that can change downstream marketing decisions:

- business model, primary business outcome, market, and strategic constraints
- verified product truth and claim boundaries
- priority segments, buying situations, JTBD, buyer/user roles, and exclusions
- customer pain, desired progress, objections, selection criteria, and evidence-backed VOC themes
- positioning, differentiators, alternatives, and competitor implications
- current offer state
- proof inventory and allowed claim use
- economics and capacity constraints
- brand, compliance, channel, and funnel constraints
- open decisions and evidence gaps

Do not turn this into a data dump, CRM export, research archive, or raw analytics repository.

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
- A generated synthesis is never promoted to VOC, proof, product truth, or a verified buyer belief.
- A specialist decision may update the context only after the decision artifact exists and its status is clear.
- Context cannot authorize a live change.

## Ownership boundaries

`$marketing-intake` owns the shared context artifact and evidence state.

Specialists own the underlying decisions:

- `$customer-research`: research patterns and traceable VOC
- `$icp-jtbd`: priority segments, buying situations, JTBD, roles, competitive alternative maps, and positioning implications
- `$offer-strategy`: offer diagnosis and approved offer design
- `$retention-economics`: LTV, payback, cohort economics
- `$tracking-measurement`: measurement integrity, causal evidence, and experiment-learning validity
- channel skills: current channel/platform mechanics

If specialist evidence and Marketing Context disagree, the source decision artifact governs until context is updated.

## Minimum QA

Before marking context `current`, confirm:

1. Decision-relevant statements have a source and evidence state.
2. Unknowns and contradictions are visible.
3. Product claims have an allowed-use boundary.
4. Customer language is traceable when treated as verbatim.
5. Economics name the revenue basis and profit level where used.
6. Current platform details are not fossilized as durable context.
7. The change log explains material revisions.
8. No unnecessary personal data was copied into the artifact.
