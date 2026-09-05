# Harness reconciliation review

Scope: focused port of PR #27's evaluation tooling and role documentation onto
current main after the installation-safety changes. Canonical marketing skills,
contracts, installer behavior, and existing case criteria remain unchanged.

## Reviewed decisions

- The registry covers 41 current case suites, including the revised routing cases.
  Counts and declared formats are mandatory. Duplicate IDs, malformed cases,
  unsupported mixed formats, missing criteria, unknown owners, path escapes, and
  unregistered case files fail validation instead of disappearing from the sample.
- Four historical cases remain in the corpus and its static count, with explicit
  exclusions from current live scoring: v1.2 cases 1, 5, and 7 assume absent
  SEO/reporting/lifecycle coverage; v1.6 case 4 assumes old unowned flat frameworks.
  Current governed skills and the archive/ownership records supersede those
  assumptions. v1.2 case 3 remains eligible: diagnostic ownership is still valid;
  its case note records that obsolete reporting-absence wording is not a required
  present-day assertion. Five additional cases require actual installer execution/link
  verification or loading-path traversal absent from the text-only harness:
  cross-agent distribution 3, 4, 13, 14 and v1.6 case 3. These remain available to
  installer tests and manual/runtime review. Original criteria were preserved.
- Role documents defer to canonical skills and shared contracts. Integrated growth
  priorities map to the current growth-strategy skill. The descriptive router map
  does not create a second intake, routing, or approval decision rule.
- The new routing case covers current integrated growth ownership. Budget routing
  distinguishes a proposed review/test from a live mutation and does not demand
  repeat approval when authorization already exists; evidence and scope gates
  still govern execution. These restate current contracts, not new decision rules.
- Live execution requires an explicit suite, model, new output path, and available
  API key. Limits are positive and default to a one-case sample per selected suite.
  The fixed official endpoint refuses redirects. No network or paid model run was
  performed during this reconciliation.
- A grade requires strict JSON, an allowed verdict, reasoning, and exact response
  quotations for PASS/FAIL. Duplicate fields, contradictory prose verdicts,
  fabricated quotes, truncated outputs, and provider errors cannot become passes.
  Operational errors remain separate from behavioral failures and scored rates.
  The judge must return UNSCORED when an execution/source-verification criterion
  lacks the actual evidence; a claimed action is not evidence of execution.
- The evidence artifact retains raw answers, grades, prompts, model identifiers,
  source/context text and hashes, repository state, and sample limitations. It does
  not contain the API key. Existing evidence is never overwritten. Interrupted
  runs may have no artifact because output is written at sample completion.

## Offline validation

`python3 scripts/eval.py --static` parsed 874 registered cases across 41 suites and
30 governed skills. Nine cases were explicitly excluded from current live scoring:
four historical assumptions and five runtime/source-traversal requirements. This validates specification structure and narrow lint only.

`python3 -m unittest discover -s tests -p 'test_eval.py' -v` completed 29 offline
regression tests. They cover parser loss modes, registration drift, case/source
identity, path boundaries, exact quote validation, malformed grading, incomplete
API responses, no-key and no-network behavior, overwrite refusal, context/source
provenance, sample exclusions, and scored-rate denominators. The provider is mocked
and environment credentials are cleared in these tests. Mock PASS fixtures test
software behavior and are not marketing behavioral evidence.

Status: implementation reviewed and offline checks completed. No live-model
benchmark, installed-agent invocation result, human adjudication of model outputs,
or business-outcome improvement is claimed. All provisional live grades still
require review under the repository's existing evaluation principles.
