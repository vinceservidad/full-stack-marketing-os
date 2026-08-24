#!/usr/bin/env bash

set -euo pipefail

repo_dir=${1:-.}

python3 - "$repo_dir" <<'PY'
import pathlib
import re
import sys

repo = pathlib.Path(sys.argv[1]).resolve()
skills_dir = repo / ".agents" / "skills"
errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def rel(path):
    try:
        return str(path.relative_to(repo))
    except ValueError:
        return str(path)


if not skills_dir.is_dir():
    print(f"Missing canonical skill directory: {rel(skills_dir)}", file=sys.stderr)
    sys.exit(1)

# --- Canonical skill packaging -------------------------------------------------

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")

# A contract element is satisfied by any of several accepted headings. Skills may
# name a section "Context", "Inputs", or "Scope" and still satisfy the input
# requirement; the contract is semantic, not a fixed vocabulary.
# Hard-failed. Every governed skill currently satisfies these.
CONTRACT = {
    "method": ("method", "route", "process", "procedure", "steps", "workflow"),
    "decision rules": ("rules", "decision rules", "constraints"),
    "output contract": ("output", "outputs", "output contract", "deliverable"),
    "quality assurance": ("qa", "quality assurance", "checks", "quality checks"),
}

# Warned, not failed. Some skills declare required inputs in the preamble or in
# the first method step instead of a dedicated section. The contract is satisfied
# semantically; heading normalization is tracked as skill-content debt.
CONTRACT_SOFT = {
    "required inputs": ("context", "inputs", "required context", "required inputs", "scope", "frame the decision"),
}

SCAFFOLD = re.compile(r"\b(TODO|TBD|FIXME|Lorem ipsum|Coming soon|placeholder)\b", re.IGNORECASE)

names = {}
skill_dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir())

if not skill_dirs:
    fail("Canonical skill directory contains no skills.")

for d in skill_dirs:
    skill_md = d / "SKILL.md"
    if not skill_md.is_file():
        fail(f"Skill directory without SKILL.md: {rel(d)}")
        continue

    text = skill_md.read_text(encoding="utf-8")

    m = FRONTMATTER.match(text)
    if not m:
        fail(f"Missing or malformed YAML frontmatter: {rel(skill_md)}")
        continue

    front = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-")):
            k, _, v = line.partition(":")
            front[k.strip()] = v.strip()

    name = front.get("name", "")
    description = front.get("description", "")

    if not name:
        fail(f"Frontmatter missing 'name': {rel(skill_md)}")
    elif name != d.name:
        fail(f"Frontmatter name '{name}' does not match folder '{d.name}': {rel(skill_md)}")

    if not description:
        fail(f"Frontmatter missing 'description': {rel(skill_md)}")
    elif len(description) < 40:
        fail(f"Description is too short to discriminate ({len(description)} chars): {rel(skill_md)}")

    if name:
        if name in names:
            fail(f"Duplicate skill name '{name}': {rel(skill_md)} and {rel(names[name])}")
        names[name] = skill_md

    body = text[m.end():]
    headings = {h.strip().lower().rstrip(":") for h in re.findall(r"^#{2,3}\s+(.+)$", body, re.MULTILINE)}
    for element, accepted in CONTRACT.items():
        if not headings & set(accepted):
            fail(f"Skill '{d.name}' has no {element} section (accepted: {', '.join(accepted)}).")

    for element, accepted in CONTRACT_SOFT.items():
        if not headings & set(accepted):
            warnings.append(f"Skill '{d.name}' declares {element} without a dedicated section.")

    if SCAFFOLD.search(body):
        fail(f"Unfinished scaffold text in {rel(skill_md)}")

    # --- Reference reachability ------------------------------------------------

    ref_dir = d / "references"
    on_disk = {p.resolve() for p in ref_dir.glob("*.md")} if ref_dir.is_dir() else set()

    reachable = set()
    queue = [skill_md]
    seen_files = set()
    while queue:
        current = queue.pop()
        if current in seen_files:
            continue
        seen_files.add(current)
        for target in LINK.findall(current.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (current.parent / target).resolve()
            if not resolved.exists():
                fail(f"Broken link '{target}' in {rel(current)}")
                continue
            if resolved in on_disk:
                reachable.add(resolved)
                queue.append(resolved)

    for orphan in sorted(on_disk - reachable):
        fail(f"Orphaned reference never loaded by its skill: {rel(orphan)}")

# --- Cross-layer impersonation -------------------------------------------------

def walk(directory):
    """Yield files, pruning archives and any nested Git repository."""
    for child in sorted(directory.iterdir()):
        if child.is_dir():
            if child.name in {".git", "node_modules"}:
                continue
            if child != repo and (child / ".git").exists():
                warnings.append(f"Skipping nested Git repository: {rel(child)}")
                continue
            if child == repo / "docs" / "archive":
                continue
            yield from walk(child)
        else:
            yield child


for candidate in walk(repo):
    if candidate.name != "SKILL.md":
        continue
    if skills_dir in candidate.parents:
        continue
    fail(f"SKILL.md outside the canonical layer: {rel(candidate)}")

legacy = repo / "skills"
if legacy.is_dir():
    for stray in legacy.iterdir():
        if stray.name == "README.md":
            continue
        fail(f"'skills/' must contain only README.md; found {rel(stray)}")

for name in names:
    for impostor in (legacy / f"{name}.md", legacy / name / "SKILL.md"):
        if impostor.exists():
            fail(f"Competing definition of canonical skill '{name}': {rel(impostor)}")

# --- Documentation must name the canonical layer -------------------------------

for doc in ("README.md", "ARCHITECTURE.md", "skills/README.md"):
    path = repo / doc
    if not path.is_file():
        fail(f"Missing required document: {doc}")
    elif ".agents/skills" not in path.read_text(encoding="utf-8"):
        fail(f"{doc} does not identify '.agents/skills/' as the canonical skill layer.")

# --- Router may not name a skill that does not exist ---------------------------

router = skills_dir / "marketing-router" / "SKILL.md"
if router.is_file():
    router_text = router.read_text(encoding="utf-8")
    for referenced in sorted(set(re.findall(r"`\$([a-z0-9-]+)`", router_text))):
        if referenced not in names:
            fail(f"Router routes to a nonexistent skill: ${referenced}")
    if "CAPABILITY-REGISTRY.md" not in router_text:
        fail("Router does not consult CAPABILITY-REGISTRY.md.")
else:
    fail("Missing marketing-router skill.")

registry = repo / "CAPABILITY-REGISTRY.md"
if not registry.is_file():
    fail("Missing CAPABILITY-REGISTRY.md.")
else:
    registry_text = registry.read_text(encoding="utf-8")
    for name in sorted(names):
        if f"${name}" not in registry_text:
            fail(f"Capability registry does not declare governed skill: ${name}")

# --- Root artifact ownership ---------------------------------------------------

ownership = repo / "ARTIFACT-OWNERSHIP.md"
if not ownership.is_file():
    fail("Missing ARTIFACT-OWNERSHIP.md.")
else:
    ownership_text = ownership.read_text(encoding="utf-8")
    unowned = []
    for directory in ("frameworks", "playbooks", "templates", "workflows"):
        target = repo / directory
        if not target.is_dir():
            continue
        for artifact in sorted(target.glob("*.md")):
            if f"`{artifact.name}`" not in ownership_text:
                unowned.append(f"{directory}/{artifact.name}")
    for item in unowned:
        fail(f"Root artifact has no ownership entry: {item} (add it to ARTIFACT-OWNERSHIP.md)")

    debt = ownership_text.count("| migration-debt |")
    if debt:
        warnings.append(f"{debt} root artifacts are tracked migration debt awaiting an owner.")

# --- Report --------------------------------------------------------------------

for warning in warnings:
    print(f"note: {warning}")

if errors:
    for error in errors:
        print(f"Architecture violation: {error}", file=sys.stderr)
    sys.exit(1)

print(f"Skill architecture is canonical and consistent ({len(names)} governed skills).")
PY
