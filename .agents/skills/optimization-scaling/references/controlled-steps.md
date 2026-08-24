# Controlled Scaling Steps

1. Establish a mature comparable baseline and protected state.
2. Write one falsifiable scaling hypothesis tied to the primary business outcome.
3. Specify exact entity, current/proposed state, one major variable, maximum exposure, owner, approval, rollback path, and expected mechanism.
4. Predefine primary metric, business and quality guardrails, minimum practical effect, decision window, conversion-lag allowance, and invalidity conditions.
5. Choose the strongest feasible design: platform experiment, holdout, geo test, cohort split, campaign/creative split, portfolio allocation test, or bounded sequential step.
6. Avoid contaminating control and treatment; document unavoidable concurrent changes.
7. Wait for the predefined maturity condition; do not decide from partial lag or one unusual day.
8. Evaluate total, blended, marginal, incremental/counterfactual evidence, mix, cannibalization, downstream quality, operational cost, and uncertainty.
9. Decide `increase`, `hold`, `continue-evidence`, `apply`, `rollback`, `switch-mode`, `de-scale`, or `inconclusive`.
10. Verify the business source of truth, record proof level and scope, and replicate when risk warrants it.

There is no universal safe percentage or cadence. Step size depends on downside, volume, lag, auction/demand volatility, bid strategy, capacity, reversibility, and learning value.
