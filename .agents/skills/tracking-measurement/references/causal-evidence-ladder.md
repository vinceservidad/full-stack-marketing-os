# Causal Evidence Ladder

Ranks how strongly a body of evidence supports the claim that marketing activity *caused* a business result. Use it to state what a conclusion may be used for — not to reject weaker evidence outright.

Classify with [`KNOWLEDGE-TAXONOMY.md`](../../../../KNOWLEDGE-TAXONOMY.md). A ladder position is an evidence grade, never proof of an outcome.

## Levels

| Level | Evidence | Supports |
|---|---|---|
| C0 | Platform-attributed conversions or revenue | Delivery and efficiency observations only. Never a causal claim |
| C1 | Multi-source correlation; before-and-after without a control | Hypotheses and prioritization |
| C2 | Modeled attribution or Marketing Mix Modeling with stated assumptions | Directional allocation, revisable |
| C3 | Quasi-experiment with a non-randomized comparison — matched markets, synthetic control, interrupted time series | Provisional causal estimate within the observed scope |
| C4 | Randomized experiment with a control group — user holdout, geo experiment, platform lift study, switchback | Causal estimate within the tested scope, population, and period |
| C5 | Replicated randomized evidence across periods, geographies, or accounts | Causal claim with an established scope of generalization |

## Rules

- Platform attribution never exceeds C0 regardless of volume, consistency, or confidence. Sample size does not convert correlation into causality.
- A result's level is set by its weakest structural element. A randomized test with a contaminated control is not C4.
- State the scope with the level: population, geography, period, spend range, creative set, and seasonality. A C4 result is causal *inside that scope only*.
- Do not generalize across business models, funnel stages, or spend ranges without evidence at the new scope. A tactic proven in one scope is not proven.
- Scaling decisions require the level demanded by the `optimization-scaling` proof standard. Do not substitute a lower level and describe it as sufficient.
- Record the level in the output. An unlabeled causal claim is treated as C0.
- A negative result carries the same level as a positive one. Do not discount a null finding because it is unwelcome.

## Choosing a target level

Match the level to the cost of being wrong, not to what is convenient:

- Reversible, low-spend, easily monitored change: C1–C2 may be enough.
- Sustained budget increase, channel entry or exit, or a structural rebuild: C3 minimum, C4 preferred.
- A claim that will be reused as a rule across accounts or periods: C5.

If the achievable level is below what the decision needs, say so and either lower the commitment, make the change reversible, or run the test first.
