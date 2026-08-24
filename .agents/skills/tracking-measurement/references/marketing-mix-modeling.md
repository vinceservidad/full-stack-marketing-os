# Marketing Mix Modeling

Regression-based estimation of channel contribution from aggregate time-series data. Answers long-horizon allocation questions that experiments cannot cover cheaply. Caps at C2: modeled, assumption-dependent, and revisable.

## What it is for

Cross-channel allocation over months or years, including channels with no click path — offline, television, out-of-home, sponsorship — and periods where user-level measurement is unavailable. It is not a substitute for an experiment on a specific change, and not a tool for weekly optimization.

## Requirements

Sufficient history relative to the number of channels; genuine variation in spend across channels and time; recorded prices, promotions, distribution changes, competitor activity, and seasonality; and a business outcome series from the source of truth.

Without spend variation there is nothing to identify. A channel held at a constant budget cannot have its contribution estimated, and a model that reports one for it is fitting noise.

## Assumptions to state explicitly

Functional form; diminishing-returns and saturation shape; adstock or carryover length; which confounders are included; how seasonality and trend are handled; and how correlated channels are separated.

Every one of these is a modeling choice, not an observation. Two defensible specifications can produce materially different channel contributions from the same data. Report the specification alongside the result.

## Validation

- Hold out a period and test out-of-sample fit; in-sample fit alone means nothing.
- Test stability across specifications. A contribution estimate that moves sharply under a reasonable alternative is not decision-grade.
- Calibrate against experimental results where they exist. Experiments discipline the model; the model does not overrule the experiment.
- Report confidence intervals. A point estimate of channel contribution without an interval overstates precision.

## Rules

- Never present a modeled contribution as a measured outcome, and never use it to claim causality for a specific campaign or change.
- Correlated channels — often brand search and everything upstream of it — cannot be cleanly separated by a model alone. State the collinearity rather than reporting a confident split.
- Do not use a model to justify a budget increase beyond the spend range present in its data. Outside that range it extrapolates.
- Do not reconcile a model against platform attribution by adding or averaging them; they answer different questions.
- Re-estimate on a stated cadence. A model is a snapshot of a period, and it decays.
