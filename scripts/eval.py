#!/usr/bin/env python3
"""Executable evaluation harness for the Marketing OS decision-behavior corpus.

Two tiers:

  --static  Deterministic. No network, no API key, no dependencies beyond the
            standard library. Verifies the evaluation corpus is a coherent,
            fully-registered specification and that the knowledge layers make
            no claim the system's own rules forbid. Runs in CI on every push.

  --live    Opt-in. Sends each case's scenario to a model with the owning
            skill loaded, grades the response against that case's own written
            pass criterion, and writes a dated scorecard to tests/RESULTS.md.
            Requires ANTHROPIC_API_KEY; skipped with a notice when absent.

The static tier proves the specification is coherent. Only the live tier
produces evidence about behavior, and it is reported as a scoped observation
of one model on one date -- never as proof that a framework guarantees an
account outcome (AGENTS.md operating principles 2, 3, and 6).
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

# --- Case parsing -------------------------------------------------------------
#
# The corpus uses two authoring shapes and both are load-bearing. Neither is
# rewritten to suit this parser.
#
#   Numbered:  `N. **Title:** Scenario. Pass only if <criterion>.`
#   Prose:     `## Title` / `Prompt: "..."` / `Pass if <criterion>.`
#
# The prose shape carries a verbatim user turn; the numbered shape carries a
# scenario that the live tier frames as a request.

NUMBERED = re.compile(r"^(\d+)\.\s+\*\*(.+?):?\*\*\s*(.+?)\s*$", re.MULTILINE)
CRITERION = re.compile(r"\bPass (?:only )?if\b", re.IGNORECASE)
SECTION = re.compile(r"^##\s+(?:\d+\.\s*)?(.+?)\s*$", re.MULTILINE)
LABELLED = re.compile(r"^\*\*(Prompt|Pass|Fail):\*\*\s*(.+?)\s*$", re.MULTILINE)
PLAIN_PROMPT = re.compile(r"^Prompt:\s*(.+?)\s*$", re.MULTILINE)
QUOTES = "\u201c\u201d\"'"


class Case:
    def __init__(self, suite, identifier, title, scenario, criterion, prompt=None, counter=""):
        self.literal_prompt = prompt is not None
        self.suite = suite
        self.identifier = identifier
        self.title = title
        # A case may carry its whole situation in the title, with the body
        # holding only the criterion. The title is then the scenario.
        self.scenario = scenario or title
        self.criterion = criterion
        self.counter = counter
        self.prompt = prompt or self.scenario

    @property
    def ref(self):
        return f"{self.suite}#{self.identifier}"

    @property
    def scorable(self):
        return bool(self.criterion)

    @property
    def verbatim(self):
        """True when the case supplies a literal user turn rather than a summary."""
        return self.literal_prompt


def split_criterion(text):
    """Return (scenario, criterion). Criterion is empty when none is written."""
    match = CRITERION.search(text)
    if not match:
        return text.strip(), ""
    return text[: match.start()].strip(), text[match.start():].strip()


def parse_cases(suite_id, path):
    """Parse one case file. Three authoring shapes are in use and all are valid.

    Numbered inline:  `N. **Title:** Scenario. Pass only if <criterion>.`
    Prose:            `## Title` / `Prompt: "..."` / `Pass if <criterion>.`
    Labelled:         `## N. Title` / `**Prompt:**` / `**Pass:**` / `**Fail:**`

    No case file is rewritten to suit the parser; the parser meets the corpus.
    """
    text = path.read_text(encoding="utf-8")

    cases = [
        Case(suite_id, number, title.strip(), *split_criterion(body))
        for number, title, body in (m.groups() for m in NUMBERED.finditer(text))
    ]
    if cases:
        return cases

    sections = list(SECTION.finditer(text))
    for index, section in enumerate(sections):
        start = section.end()
        end = sections[index + 1].start() if index + 1 < len(sections) else len(text)
        block = text[start:end].strip()
        if not block:
            continue

        labels = {key.lower(): value for key, value in LABELLED.findall(block)}
        if "pass" in labels:
            cases.append(
                Case(
                    suite_id,
                    str(index + 1),
                    section.group(1).strip(),
                    labels.get("prompt", "").strip(QUOTES),
                    labels["pass"],
                    prompt=labels.get("prompt", "").strip(QUOTES) or None,
                    counter=labels.get("fail", ""),
                )
            )
            continue

        scenario, criterion = split_criterion(block)
        if not criterion:
            continue
        prompt_match = PLAIN_PROMPT.search(block)
        cases.append(
            Case(
                suite_id,
                str(index + 1),
                section.group(1).strip(),
                scenario,
                criterion,
                prompt=prompt_match.group(1).strip().strip(QUOTES) if prompt_match else None,
            )
        )

    return cases


# --- Static tier --------------------------------------------------------------

# Claims the system's own rules forbid, anywhere in the knowledge layers.
# validate-scaling-system.sh already enforced the first group across the
# scaling subtree; these run across every layer an agent can load.
BANNED_CLAIMS = [
    (
        r"always increase (the )?budget by [0-9]+%",
        "universal budget-increase rule (optimization-scaling rejects a fixed percentage)",
    ),
    (r"guaranteed (scaling|results?|roas|revenue|growth)", "guaranteed outcome"),
    (r"platform ROAS proves", "platform attribution presented as proof"),
    (
        r"\b(google|meta|facebook) (recently )?changed (its|their|the) algorithm\b",
        "undocumented algorithm-change claim (PLATFORM-CURRENCY.md forbids it)",
    ),
    (r"\bproven to (double|triple|[0-9]+x)\b", "unsubstantiated multiplier claim"),
    (
        r"\bwill (definitely|certainly) (increase|improve|scale)\b",
        "certainty about an unobserved outcome",
    ),
]

SCANNED_LAYERS = (
    ".agents/skills",
    "frameworks",
    "playbooks",
    "templates",
    "workflows",
    "gpt-knowledge",
    "examples",
)

# Directories whose prose names skills and must not drift from the governed set.
SKILL_NAME_LAYERS = ("agents", "evaluations")
SKILL_REFERENCE = re.compile(r"\$([a-z0-9][a-z0-9-]*)")


# A disclaimer that rules a claim out is the opposite of making it. "does not
# represent guaranteed results" must not be reported as a guarantee.
NEGATION = re.compile(r"\b(not|never|no|without|nor|avoid|refus\w*|reject\w*|prohibit\w*)\b", re.IGNORECASE)


def negated(body, position, window=60):
    """True when the claim at `position` sits inside a negating clause."""
    return bool(NEGATION.search(body[max(0, position - window):position]))


def governed_skills(repo):
    root = repo / ".agents" / "skills"
    return {d.name for d in root.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()}


def load_suites(repo):
    manifest = repo / "tests" / "evaluations" / "suites.json"
    if not manifest.is_file():
        raise SystemExit("Missing suite manifest: tests/evaluations/suites.json")
    return json.loads(manifest.read_text(encoding="utf-8"))["suites"]


def resolve_case_file(repo, suite):
    """A suite's cases live in tests/evaluations/, or at a repo-relative path."""
    candidate = repo / "tests" / "evaluations" / suite["cases"]
    return candidate if candidate.is_file() else repo / suite["cases"]


def run_static(repo):
    errors, notes = [], []
    skills = governed_skills(repo)
    suites = load_suites(repo)

    eval_dir = repo / "tests" / "evaluations"
    registered = {s["cases"] for s in suites}
    on_disk = {p.name for p in eval_dir.glob("*-cases.md")}

    for orphan in sorted(on_disk - registered):
        errors.append(f"Case file not registered in suites.json: tests/evaluations/{orphan}")
    for missing in sorted(registered - on_disk):
        if not (repo / missing).is_file():
            errors.append(f"suites.json registers a missing case file: {missing}")

    total_cases = 0
    unscored = []
    seen_ids = set()

    for suite in sorted(suites, key=lambda s: s["id"]):
        suite_id = suite["id"]
        if suite_id in seen_ids:
            errors.append(f"Duplicate suite id: {suite_id}")
        seen_ids.add(suite_id)

        path = resolve_case_file(repo, suite)
        if not path.is_file():
            errors.append(f"Suite '{suite_id}' points at a missing file: {suite['cases']}")
            continue

        for owner in suite["owners"]:
            if owner not in skills:
                errors.append(f"Suite '{suite_id}' names a nonexistent skill: ${owner}")

        if "{scenario}" not in suite.get("prompt_template", ""):
            errors.append(f"Suite '{suite_id}' prompt_template does not include {{scenario}}")

        review = suite.get("review")
        if review:
            if not (eval_dir / review).is_file():
                errors.append(f"Suite '{suite_id}' points at a missing review record: {review}")
        else:
            notes.append(
                f"Suite '{suite_id}' has no human review record "
                "(predates the AGENTS.md review requirement)."
            )

        cases = parse_cases(suite_id, path)
        if not cases:
            errors.append(f"Suite '{suite_id}' parsed zero cases from {suite['cases']}")
            continue

        declared = suite.get("case_count")
        if declared is not None and declared != len(cases):
            errors.append(
                f"Suite '{suite_id}' declares {declared} cases but "
                f"{suite['cases']} parses to {len(cases)}"
            )

        for case in cases:
            if not case.title:
                errors.append(f"{case.ref}: case has no title")
            if not case.scenario:
                errors.append(f"{case.ref}: case has no scenario")
            if not case.scorable:
                unscored.append(f"{case.ref} ({case.title})")

        total_cases += len(cases)
        print(f"  {suite_id:<38} {len(cases):>3} cases  ->  ${', $'.join(suite['owners'])}")

    for case_ref in unscored:
        errors.append(f"Case has no 'Pass if' criterion and cannot be scored: {case_ref}")

    # Banned claims across every layer an agent can load.
    for layer in SCANNED_LAYERS:
        base = repo / layer
        if not base.is_dir():
            continue
        for markdown in sorted(base.rglob("*.md")):
            body = markdown.read_text(encoding="utf-8")
            for pattern, label in BANNED_CLAIMS:
                for found in re.finditer(pattern, body, re.IGNORECASE):
                    if negated(body, found.start()):
                        continue
                    errors.append(
                        f"Forbidden claim in {markdown.relative_to(repo)}: "
                        f"{label} -- {found.group(0)!r}"
                    )

    # Skill names in the documentation layers must resolve to a governed skill.
    for layer in SKILL_NAME_LAYERS:
        base = repo / layer
        if not base.is_dir():
            continue
        for markdown in sorted(base.rglob("*.md")):
            body = markdown.read_text(encoding="utf-8")
            for referenced in sorted(set(SKILL_REFERENCE.findall(body))):
                if referenced not in skills:
                    errors.append(
                        f"{markdown.relative_to(repo)} names a nonexistent skill: ${referenced}"
                    )

    print(f"\n{total_cases} cases across {len(suites)} suites; {len(skills)} governed skills.")

    for note in notes:
        print(f"note: {note}")

    if errors:
        print("\nEvaluation corpus violations:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Evaluation corpus is complete, registered, and consistent.")
    return 0


# --- Live tier ----------------------------------------------------------------

# Honors ANTHROPIC_BASE_URL so the harness works behind a gateway or proxy.
API_BASE = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
API_URL = f"{API_BASE}/v1/messages"
DEFAULT_MODEL = "claude-sonnet-5"
DEFAULT_JUDGE = "claude-sonnet-5"

JUDGE_INSTRUCTIONS = """You are grading one response against one written pass criterion.

Grade ONLY against the criterion as written. Do not apply any standard the
criterion does not state, and do not reward a response for being well written,
thorough, or agreeable. A response that reaches the right conclusion for a
reason the criterion excludes does not pass.

When a FAIL CRITERION is supplied, a response matching it fails regardless of
what else it does well.

Reply with exactly two lines:
VERDICT: PASS or FAIL
EVIDENCE: one sentence quoting the part of the response that decides it.
"""


def judge_prompt(case, answer):
    parts = [f"PASS CRITERION:\n{case.criterion}"]
    if case.counter:
        parts.append(f"FAIL CRITERION:\n{case.counter}")
    parts.append(f"RESPONSE:\n{answer}")
    return "\n\n".join(parts)


def call_api(api_key, model, system, user, max_tokens=2000):
    payload = json.dumps(
        {
            "model": model,
            "max_tokens": max_tokens,
            "system": system,
            "messages": [{"role": "user", "content": user}],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "content-type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        body = json.loads(response.read().decode("utf-8"))
    return "".join(block.get("text", "") for block in body.get("content", []))


def skill_context(repo, owners, with_references):
    parts = [(repo / "AGENTS.md").read_text(encoding="utf-8")]
    for owner in owners:
        skill_dir = repo / ".agents" / "skills" / owner
        parts.append(
            f"\n\n# Loaded skill: ${owner}\n\n"
            + (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        )
        references = skill_dir / "references"
        if with_references and references.is_dir():
            for reference in sorted(references.glob("*.md")):
                parts.append(
                    f"\n\n## Reference: {reference.name}\n\n"
                    + reference.read_text(encoding="utf-8")
                )
    return "\n".join(parts)


def run_live(repo, suite_filter, model, judge_model, limit, with_references, out_path):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY is not set; skipping the live tier.")
        print("The static tier is the one that runs without a key.")
        return 0

    suites = [s for s in load_suites(repo) if not suite_filter or s["id"] in suite_filter]
    if not suites:
        raise SystemExit(f"No suite matched: {', '.join(suite_filter)}")

    results = []

    for suite in suites:
        cases = parse_cases(suite["id"], resolve_case_file(repo, suite))
        if limit:
            cases = cases[:limit]
        system = skill_context(repo, suite["owners"], with_references)

        for case in cases:
            if not case.scorable:
                results.append((suite, case, "UNSCORED", "No written pass criterion."))
                continue
            try:
                answer = call_api(
                    api_key, model, system, suite["prompt_template"].format(scenario=case.prompt)
                )
                verdict_text = call_api(
                    api_key,
                    judge_model,
                    JUDGE_INSTRUCTIONS,
                    judge_prompt(case, answer),
                    max_tokens=400,
                )
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
                results.append((suite, case, "ERROR", str(error)))
                print(f"  {case.ref:<28} ERROR")
                continue

            if re.search(r"VERDICT:\s*PASS", verdict_text, re.IGNORECASE):
                verdict = "PASS"
            elif re.search(r"VERDICT:\s*FAIL", verdict_text, re.IGNORECASE):
                verdict = "FAIL"
            else:
                verdict = "UNSCORED"

            evidence_match = re.search(r"EVIDENCE:\s*(.+)", verdict_text, re.IGNORECASE | re.DOTALL)
            evidence = " ".join(evidence_match.group(1).split()) if evidence_match else ""
            results.append((suite, case, verdict, evidence))
            print(f"  {case.ref:<28} {verdict}")

    write_results(repo, out_path, model, judge_model, with_references, results)
    return 1 if any(verdict in {"FAIL", "ERROR"} for *_, verdict, _ in results) else 0


def write_results(repo, out_path, model, judge_model, with_references, results):
    by_suite = {}
    for suite, case, verdict, evidence in results:
        by_suite.setdefault(suite["id"], []).append((case, verdict, evidence))

    lines = [
        "# Evaluation Results",
        "",
        f"**Run:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Responder model:** `{model}`  ",
        f"**Judge model:** `{judge_model}`  ",
        f"**Skill references loaded:** {'yes' if with_references else 'no (SKILL.md only)'}",
        "",
        "This records how one model, on one date, behaved against the written pass",
        "criteria in `tests/evaluations/`. It is a scoped observation of decision",
        "behavior under test conditions. It is not evidence that any framework here",
        "produces a given result in a live advertising account, and it does not",
        "replace the human review records in this directory.",
        "",
        "## Scorecard",
        "",
        "| Suite | Cases | Pass | Fail | Unscored | Pass rate |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for suite_id, entries in sorted(by_suite.items()):
        passed = sum(1 for _, v, _ in entries if v == "PASS")
        failed = sum(1 for _, v, _ in entries if v in {"FAIL", "ERROR"})
        unscored = sum(1 for _, v, _ in entries if v == "UNSCORED")
        scored = passed + failed
        rate = f"{passed / scored:.0%}" if scored else "n/a"
        lines.append(
            f"| `{suite_id}` | {len(entries)} | {passed} | {failed} | {unscored} | {rate} |"
        )

    failures = [
        (suite_id, case, verdict, evidence)
        for suite_id, entries in sorted(by_suite.items())
        for case, verdict, evidence in entries
        if verdict != "PASS"
    ]

    lines += ["", "## Cases that did not pass", ""]
    if not failures:
        lines.append("None.")
    for suite_id, case, verdict, evidence in failures:
        lines += [
            f"### `{suite_id}` case {case.identifier} — {case.title} ({verdict})",
            "",
            f"**Criterion:** {case.criterion}",
            "",
            f"**Judge:** {evidence or 'no evidence returned'}",
            "",
        ]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        shown = out_path.relative_to(repo)
    except ValueError:
        shown = out_path
    print(f"\nWrote {shown}")


# --- Entry point --------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--repo", default=".", help="Repository root (default: .)")
    parser.add_argument("--static", action="store_true", help="Run deterministic checks (default)")
    parser.add_argument("--live", action="store_true", help="Run cases against a model and score them")
    parser.add_argument("--suite", action="append", default=[], help="Limit --live to this suite id (repeatable)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Responder model (default: {DEFAULT_MODEL})")
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE, help=f"Judge model (default: {DEFAULT_JUDGE})")
    parser.add_argument("--limit", type=int, default=0, help="Cap cases per suite (smoke runs)")
    parser.add_argument("--with-references", action="store_true", help="Load each skill's references too")
    parser.add_argument("--out", default="tests/RESULTS.md", help="Scorecard path (default: tests/RESULTS.md)")
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()

    if args.live:
        return run_live(
            repo, args.suite, args.model, args.judge_model,
            args.limit, args.with_references, repo / args.out,
        )

    return run_static(repo)


if __name__ == "__main__":
    raise SystemExit(main())
