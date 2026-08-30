# Evaluation System

Two things live under the name "evaluation" in this repository, and they answer
different questions.

| | `evaluations/` (this directory) | `tests/evaluations/` |
|---|---|---|
| Holds | Routing cases and reviewer checklists | Versioned decision-behavior cases, one suite per capability |
| Question | Did the request reach the right owner, and is the output usable? | Does the skill make the right decision under a specific evidence state? |
| Executable | `routing-tests.md` is, via `scripts/eval.py` | Yes, via `scripts/eval.py` |

Every case file in both directories is registered in
[`tests/evaluations/suites.json`](../tests/evaluations/suites.json) and parsed by
[`scripts/eval.py`](../scripts/eval.py). An unregistered case file fails validation,
so a suite cannot quietly stop being checked.

## Running them

```bash
python3 scripts/eval.py --static     # deterministic; no API key; runs in CI
python3 scripts/eval.py --live --suite routing   # scores against a model; needs ANTHROPIC_API_KEY
```

The static tier proves the corpus is a coherent, fully-registered specification:
every case parses, carries a pass criterion, and names a skill that exists. The
live tier is the only one that produces evidence about behavior, and it writes a
dated scorecard to `tests/RESULTS.md`.

## What a passing evaluation does and does not mean

A pass means one model, on one date, made the decision the criterion required
under test conditions. It is not evidence that a framework here produces a given
result in a live advertising account. Per `AGENTS.md`, an evaluation is not marked
passed without reviewing the decision, the evidence handling, and the
authorization boundary — a wording match is not a pass.

## Reviewer checklists

- [`ai-agent-evaluation.md`](ai-agent-evaluation.md) — whether a workflow produces reliable decisions
- [`campaign-quality-checklist.md`](campaign-quality-checklist.md) — campaign output review
- [`decision-quality-check.md`](decision-quality-check.md) — decision review
- [`output-quality-tests.md`](output-quality-tests.md) — output review
