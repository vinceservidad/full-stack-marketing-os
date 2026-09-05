# Evaluation system

The case corpus specifies expected decision behavior. `scripts/eval.py` makes its
registration and parsing executable, and can run an explicitly requested model
sample. Structural validation, provisional model grading, and reviewed behavior
are different evidence states. None demonstrates commercial effectiveness.

## Offline checks

From the repository root:

```sh
python3 scripts/eval.py --static
python3 -m unittest discover -s tests -p 'test_eval.py' -v
```

The static tier uses only Python's standard library and makes no network calls.
Run from a Git checkout root. The harness discovers tracked files and nonignored
untracked files using Git's standard ignore rules, including local excludes.
Deliberately tracked files remain sources even if an ignore pattern also matches.
Source archives without Git metadata fail closed instead of scanning local files.
Source symlinks and symlinked source ancestors are rejected.

It checks every eligible `tests/evaluations/*-cases.md` file and the routing case file
against `tests/evaluations/suites.json`: source paths, format, explicit case count,
unique suite/case IDs, written input and criteria, owner skill names, and registered
review paths. The parser supports numbered cases, three-column case tables, and
cases under level-two or level-three headings. Unsupported or mixed formats fail;
a malformed case cannot be accepted by silently switching to another format.

A small claim-pattern lint also flags a limited set of suspect statements in the
knowledge layers. Negation handling is heuristic; it cannot establish truth,
causality, comprehensive safety, or compliance with every operating rule. Git
ignored scratch/output files are excluded. Existing repository validators remain
required. A green static run means these structural checks completed, **not that
any behavioral case passed**. A review file's existence does not certify its
contents or promote an old review into current evidence.

## Explicit live sample

No model name is assumed and no live evaluation runs as part of the default test
suite. Set `ANTHROPIC_API_KEY` through the execution environment or secret manager,
then explicitly choose an available provider model, suite, and new artifact path:

```sh
python3 scripts/eval.py --live \
  --suite routing \
  --model MODEL_ID \
  --limit 1 \
  --out tests/results/routing-sample.json
```

This opts in to paid Anthropic API requests. `MODEL_ID` is a placeholder, not a
model recommendation. A selected case makes at most two requests: responder and
judge. `--limit` is a positive cap **per selected suite**, defaults to one, and
selects the first eligible cases in source order. It is a deterministic smoke
sample, not a randomized or representative benchmark. Repeat `--suite` for more
suites. `--judge-model` defaults to the supplied responder model; using the same
model may introduce correlated grading errors. No requests are retried
implicitly. The adapter uses the official HTTPS endpoint and refuses redirects;
it does not read an alternate base URL from the environment.

The default context contains `AGENTS.md`, `GLOSSARY.md`, `PLATFORM-CURRENCY.md`,
`KNOWLEDGE-TAXONOMY.md`, `CAPABILITY-REGISTRY.md`, `ARTIFACT-OWNERSHIP.md`, and each
registered context owner's
`SKILL.md`. `--with-references` additionally loads Markdown under those owners'
local `references/` directories. Linked root frameworks, templates, playbooks,
workflows, external sources, other supporting skills, and installed runtime tools
are not automatically loaded. This is a **partial-context, text-only evaluation**;
it cannot test installed-agent discovery/invocation, live account access, runtime
mutations, or the complete operating system. Results must retain that scope.

Reference discovery uses the same tracked/nonignored source boundary. Ignored
scratch such as `references/work/`, ignored client notes, and locally excluded
files are omitted from both model context and its saved source provenance.
Explicitly registered cases, reviews, and required context files must also be
eligible; an ignored required source fails validation instead of being read.
An in-repository symlink cannot be used to bypass that boundary.

A literal `Prompt:` is sent as written, apart from its surrounding quotation marks.
An `Input:`/scenario summary uses the registered scenario wrapper where specified.
Written pass/fail criteria are supplied only to the judge. The judge also receives
the scenario so it can assess the response in context, and is instructed to treat
all submitted fields as data rather than follow embedded instructions. It must
return `UNSCORED` when the criterion needs actual execution, source access, or
artifact verification that the available evidence cannot demonstrate. A response
claiming an action occurred is not evidence that it occurred.

The adapter's Messages API request/response fields were checked against the
[official Create a Message reference](https://platform.claude.com/docs/en/api/messages/create)
on 2026-09-06. Model availability and future API changes still need current
verification before introducing new provider behavior.

## Evidence and exit status

A new JSON artifact preserves run timestamps, repository commit and dirty-state
listing, harness hash, requested and returned model identifiers, loaded source text
and hashes, case definition and source hash, exact responder/judge prompts, full
API response bodies, answer, judge output, quotes, and reasoning. It never includes
request headers or the API key. Existing artifacts are not overwritten. Symlinked output paths or ancestors are
rejected before paid requests and checked again before writing the artifact. The file is written when the selected sample finishes, so an
interrupted process may not produce an artifact. Keep samples bounded.

Results distinguish:

- `PASS` and `FAIL`: provisional model-judge decisions with at least one exact
  response quotation and nonempty reasoning. These still need review of the
  decision, evidence handling, and authorization boundary.
- `UNSCORED`: malformed, ambiguous, or unsubstantiated grading. A regex match to
  `PASS` alone cannot produce a pass.
- `ERROR`: provider/network errors, empty answers, or incomplete responses. These
  are operational failures, not evidence that a marketing decision failed.
- `EXCLUDED`: preserved historical criteria that conflict with current capability
  coverage, or criteria requiring actual installer execution/source traversal
  unavailable to this text-only harness. The registry records each case ID and reason; criteria are unchanged.
- `NOT_SELECTED`: eligible cases outside the requested first-N sample.

The artifact reports every case in each selected suite, including exclusions and
unsampled cases. Pass rate uses only scored `PASS` + `FAIL` cases and is null when
nothing was scored; error and unscored counts remain separate. A sample with errors
or unscored cases cannot be reported as complete. An all-excluded sample does not
pass. Exit codes are `0` for successful static checks or a nonempty live sample
whose provisional grades all pass, `1` for lint findings or a live sample with
failures/errors/unscored/no scored cases, and `2` for invalid configuration or
specification, unavailable credentials, or output failure. Missing credentials do
not silently skip a requested live run with success.

Generated response artifacts stay local under ignored `tests/results/`. Review
privacy and provenance before publishing any artifact; model responses can repeat
supplied data. A manually triggered workflow may retain the selected evidence as a
workflow artifact, but its successful status does not replace behavioral review.

## Corpus maintenance and review

Update the manifest's explicit format/count when adding cases and review the parsed
scenario and complete criterion, not just the count. Preserve case IDs and written
criteria. A case with historical capability assumptions should have a reasoned
`live_exclusions` entry rather than being silently deleted, rewritten to make a
run pass, or graded against an obsolete owner map. Current routing cases and the
capability registry govern present coverage. Case notes may record historical
wording whose behavioral boundary remains valid; they are preserved in the
artifact and supplied to the judge without changing the source criterion. For
example, v1.2 case 3 still tests diagnostic ownership, while its outdated wording
about a nonexistent reporting skill is not a required present-day assertion.

Review every claimed behavioral pass for the actual decision, evidence handling,
commercial truth, and authorization boundary. Check nulls, contradictions,
unsupported certainty, tool/context limitations, and the judge's quotation against
the full answer. Keep static results, mock-test results, provisional model grading,
and reviewed decision behavior explicitly separate. There is no live-model result
or commercial-outcome evidence supplied by this reconciliation.
