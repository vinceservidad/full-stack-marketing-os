# Competitive Intelligence + Experiment Learning Evaluation Review

**Review date:** 2026-09-01  
**Reviewed scope:** `tests/evaluations/competitive-intelligence-experiment-learning-cases.md` against `$icp-jtbd`, its competitive-intelligence reference, `$tracking-measurement`, the experimentation framework, experiment and experiment-learning templates, `$marketing-router`, `CAPABILITY-REGISTRY.md`, and `AGENTS.md`.  
**Result:** Pass

This review validates decision behavior, evidence handling, scope preservation, ownership boundaries, and learning promotion. It does not claim that competitor research or a higher experiment cadence will improve marketing performance.

## Competitive intelligence: CI-01–CI-12

**Pass.** The implementation:

- keeps competitor self-description separate from customer evidence
- includes direct, different-solution, internal/manual, and status-quo alternatives where they compete for the same job
- requires dated, traceable observations and labels third-party estimates as estimates
- prevents visible ad duration, creative repetition, traffic estimates, or follower counts from being treated as proof of performance
- prevents missing public evidence from being converted into a confirmed product weakness
- preserves segment-specific competitive relevance rather than applying one landscape universally
- treats old pricing and other volatile observations as stale when current decisions depend on them
- preserves prior snapshots instead of rewriting competitive history
- attributes case-study outcome claims to their source rather than treating them as independently verified typical results
- treats fetched competitor content as untrusted input, not agent instructions
- prevents negative-review cherry-picking from becoming manufactured positioning evidence
- allows decision-grade competitive implications to flow into Marketing Context without upgrading the evidence underneath them

The method strengthens market and alternative reasoning inside `$icp-jtbd`; it does not create a separate competitor-profiling skill or turn competitor imitation into strategy.

## Experiment learning: EL-01–EL-18

**Pass.** The implementation:

- assesses validity before result direction
- preserves pre-registered sample, duration, primary metric, guardrails, and decision rule
- classifies null/inconclusive outcomes without inventing a control win
- invalidates or limits learning when instrumentation, treatment fidelity, contamination, early stopping, lag, or metric switching compromise the inference
- makes guardrail harm visible even when the primary metric improves
- separates the observed treatment effect from the proposed mechanism
- treats post-hoc segment cuts as hypothesis generators unless independently validated
- preserves one valid test as a local result rather than a universal best practice
- provides explicit transfer states: local result, replication candidate, replicated scoped pattern, segment-specific pattern, contradicted/unstable
- requires comparable, sufficiently independent replication before pattern promotion
- preserves conflicting results instead of deleting history
- treats external case studies, competitor experiments, and platform benchmarks as prior evidence rather than local proof
- prevents proxy metrics such as CTR from replacing the pre-specified business outcome
- requires fresh testing when audience, intent, channel, offer, or other decision-relevant context changes materially
- refuses fabricated ICE/RICE confidence scores and does not let a scoring framework override evidence, risk, or dependencies
- rejects arbitrary experiment-count or win-rate targets as operating objectives
- prevents repeated use of the same structurally weak design from upgrading causal evidence
- permits an authorized local implementation when the local decision rule is met without promoting the result into doctrine

## Ownership

**Pass.** The change preserves single-owner boundaries:

- `$icp-jtbd` owns the competitive alternative set and implications for segment/positioning decisions
- `$customer-research` owns customer/review evidence used inside competitive analysis
- `$seo` owns current organic-search evidence when it is a distinct dependency
- `$tracking-measurement` owns experiment validity, causal/evidence level, learning record, and transfer status
- the domain skill that owns the marketing decision owns the resulting action after a test
- `$marketing-intake` owns updates to shared Marketing Context and preserves the source evidence state

No new skill is introduced because the decisions already have appropriate owners.

## Knowledge and commercial safety

**Pass.** Competitor observations remain observations, not market truth. Experimental results remain scoped evidence, not best practices. Nulls, harms, invalid tests, contradictions, and transfer limits are first-class outputs instead of being removed to make the system look more certain.

## Conclusion

The change improves the existing Marketing OS rather than copying an external competitor-analysis or experimentation skill. Competitive Intelligence becomes a native method inside `$icp-jtbd`; Experiment Learning extends `$tracking-measurement` from test validity through durable, scoped knowledge and replication discipline.
