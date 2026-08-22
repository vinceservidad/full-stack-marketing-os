# Experimentation Framework

## Knowledge metadata

- Primary type: framework
- Secondary type: methodology / process
- Decision: whether a test can produce a valid decision
- Evidence status: stable operating method
- Freshness: stable; confirm platform-specific implementation separately

A valid experiment connects one decision to one falsifiable hypothesis.

## Minimum specification

- Problem and evidence
- Hypothesis and expected mechanism
- Control and variant
- Population and allocation
- Primary metric and business guardrails
- Instrumentation and QA
- Minimum practical effect or decision threshold
- Duration covering relevant cycles and conversion lag
- Stop conditions for harm or invalid data
- Decision rule: ship, iterate, reject, or inconclusive

Avoid repeated peeking, changing several major variables without accepting ambiguity, or declaring a winner from directional noise. Record surprises and downstream effects, not just the headline metric.
