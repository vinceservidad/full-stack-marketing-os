#!/usr/bin/env python3
"""Install Marketing OS without taking ownership of the user's runtime."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import uuid

OWNER = "vinceservidad/full-stack-marketing-os"
NAMESPACE = ".marketing-os"
MANIFEST = "manifest.json"
CONTRACTS = (
    "GLOSSARY.md", "KNOWLEDGE-TAXONOMY.md", "PLATFORM-CURRENCY.md",
    "CAPABILITY-REGISTRY.md", "ARTIFACT-OWNERSHIP.md", "AGENTS.md",
)
LIBRARIES = ("frameworks", "playbooks", "templates", "workflows")
LINK = re.compile(r"\]\(([^)]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class InstallError(Exception):
    """An unsafe or incomplete installation must not proceed."""


def inventory(root: Path, paths: list[str]) -> dict[str, str]:
    """Hash owned trees, including empty directories; never follow symlinks."""
    result = {}
    for relative in paths:
        base = root / relative
        if not base.exists() and not base.is_symlink():
            raise InstallError(f"Missing managed path: {base}")
        for entry in [base, *sorted(base.rglob("*"))]:
            key = entry.relative_to(root).as_posix()
            if entry.is_symlink():
                raise InstallError(f"Refusing symlink in managed files: {entry}")
            if key == f"{NAMESPACE}/{MANIFEST}":
                continue
            if entry.is_dir():
                result[key] = "directory"
            elif entry.is_file():
                result[key] = hashlib.sha256(entry.read_bytes()).hexdigest()
            else:
                raise InstallError(f"Unsupported file type: {entry}")
    return result


def skill_paths(names: list[str]) -> list[str]:
    return [NAMESPACE, *(f"skills/{name}" for name in names)]


def check_target(root: Path, names: list[str]) -> list[str]:
    """Only replace unmodified trees recorded by this installer's manifest."""
    for path in (root, root / "skills", root / NAMESPACE,
                 root / ".marketing-os-backups"):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise InstallError(f"Refusing non-directory or symlink destination: {path}")
    old_names = []
    namespace = root / NAMESPACE
    if namespace.exists():
        marker = namespace / MANIFEST
        if not marker.is_file() or marker.is_symlink():
            raise InstallError(f"Unmanaged namespace: {namespace}. Move it to a backup first.")
        try:
            data = json.loads(marker.read_text(encoding="utf-8"))
            old_names = data["skills"]
            valid = (
                data["owner"] == OWNER and data["version"] == 1
                and isinstance(old_names, list)
                and all(isinstance(n, str) and NAME.fullmatch(n) for n in old_names)
                and len(set(old_names)) == len(old_names)
                and isinstance(data["files"], dict)
            )
            if not valid:
                raise ValueError("invalid ownership manifest")
            if inventory(root, skill_paths(old_names)) != data["files"]:
                raise InstallError("Managed files were modified locally. Back up your edits before reinstalling.")
        except (KeyError, TypeError, ValueError) as exc:
            raise InstallError(f"Invalid installation manifest: {marker}") from exc
    collisions = [str(root / "skills" / name) for name in names
                  if name not in old_names and ((root / "skills" / name).exists()
                  or (root / "skills" / name).is_symlink())]
    if collisions:
        raise InstallError("Skill collision: " + ", ".join(collisions) + ". Move these existing skills to a backup first.")
    return old_names


def stage_install(repo: Path, stage: Path) -> list[str]:
    source = repo / ".agents" / "skills"
    if not source.is_dir() or source.is_symlink():
        raise InstallError(f"Missing canonical skill directory: {source}")
    names = sorted(p.name for p in source.iterdir() if p.is_dir())
    if not names or any(not NAME.fullmatch(n) for n in names):
        raise InstallError("Canonical skill names are missing or invalid.")
    required = [*CONTRACTS, *LIBRARIES,
                *(f".agents/skills/{n}" for n in names)]
    inventory(repo, required)  # Reject missing dependencies and source symlinks.
    namespace = stage / NAMESPACE
    namespace.mkdir()
    for name in CONTRACTS:
        shutil.copy2(repo / name, namespace / name)
    for name in LIBRARIES:
        shutil.copytree(repo / name, namespace / name)
    (stage / "skills").mkdir()
    for name in names:
        if not (source / name / "SKILL.md").is_file():
            raise InstallError(f"Missing SKILL.md: {name}")
        shutil.copytree(source / name, stage / "skills" / name)

    def destination(relative: Path) -> Path | None:
        parts = relative.parts
        if parts[:2] == (".agents", "skills"):
            return stage / "skills" / Path(*parts[2:])
        if parts and (parts[0] in CONTRACTS or parts[0] in LIBRARIES):
            return namespace / relative
        return None

    for output in stage.rglob("*.md"):
        relative = output.relative_to(stage)
        if relative.parts[0] == "skills":
            original = repo / ".agents" / relative
        else:
            original = repo / Path(*relative.parts[1:])
        text = output.read_text(encoding="utf-8")

        def rewrite(match: re.Match) -> str:
            target, sep, anchor = match.group(1).partition("#")
            if not target or target.startswith(("/", "http:", "https:", "mailto:")):
                return match.group(0)
            try:
                relative_target = (original.parent / target).resolve().relative_to(repo)
            except ValueError:
                return match.group(0)
            mapped = destination(relative_target)
            if mapped is None:
                return match.group(0)
            link = Path(os.path.relpath(mapped, output.parent)).as_posix()
            # Path normalization removes a directory link's trailing slash.
            # Keep the source spelling so installation does not introduce drift.
            if target.endswith("/"):
                link += "/"
            return f"]({link}{sep}{anchor})"

        text = LINK.sub(rewrite, text)
        if output.name == "SKILL.md":
            frontmatter = re.match(r"\A---\n.*?\n---\n", text, re.DOTALL)
            if not frontmatter:
                raise InstallError(f"Invalid skill frontmatter: {original}")
            note = (
                "\nBefore using this Marketing OS skill, read "
                "[Marketing OS operating rules](../../.marketing-os/AGENTS.md). "
                "Apply them to this task without replacing personal or project instructions.\n"
            )
            end = frontmatter.end()
            text = text[:end] + note + text[end:]
        output.write_text(text, encoding="utf-8")

    # Validate this package's runtime skill links, not unrelated user skills.
    for output in (stage / "skills").rglob("*.md"):
        for match in LINK.finditer(output.read_text(encoding="utf-8")):
            target = match.group(1).partition("#")[0]
            if not target or target.startswith(("http:", "https:", "mailto:")):
                continue
            resolved = (output.parent / target).resolve()
            if stage not in resolved.parents or not resolved.exists():
                raise InstallError(f"Unresolved skill link: {output.relative_to(stage)} -> {target}")
    data = {"owner": OWNER, "version": 1, "skills": names,
            "files": inventory(stage, skill_paths(names))}
    (namespace / MANIFEST).write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return names


def publish(stage: Path, root: Path, names: list[str]) -> Path | None:
    """Stage on the target volume, back up owned trees, and roll back on errors."""
    root.mkdir(parents=True, exist_ok=True)
    lock = root / ".marketing-os-install.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise InstallError(f"Install lock exists: {lock}. Check for an active or interrupted install.") from exc
    os.close(fd)
    try:
        old_names = check_target(root, names)
        (root / "skills").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".marketing-os-stage-", dir=root) as work:
            prepared = Path(work) / "ready"
            shutil.copytree(stage, prepared)
            old_paths = skill_paths(old_names) if (root / NAMESPACE).exists() else []
            backup = None
            if old_paths:
                backup = root / ".marketing-os-backups" / uuid.uuid4().hex
                backup.mkdir(parents=True)
            saved, placed = [], []
            try:
                for relative in old_paths:
                    target = backup / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(root / relative, target)
                    saved.append(relative)
                for relative in skill_paths(names):
                    os.replace(prepared / relative, root / relative)
                    placed.append(relative)
            except BaseException:
                for relative in reversed(placed):
                    shutil.rmtree(root / relative)
                for relative in reversed(saved):
                    os.replace(backup / relative, root / relative)
                raise
            return backup
    finally:
        lock.unlink()


def install(repo: Path, root: Path, dry_run: bool = False) -> tuple[int, Path | None]:
    repo = repo.expanduser().resolve()
    root = Path(os.path.abspath(root.expanduser()))
    resolved_root = root.resolve()
    if (resolved_root == repo or resolved_root in repo.parents
            or repo in resolved_root.parents):
        raise InstallError("Repository and installation directories must not overlap.")
    with tempfile.TemporaryDirectory(prefix="marketing-os-preflight-") as work:
        stage = Path(work).resolve()
        names = stage_install(repo, stage)
        check_target(root, names)
        current = root / NAMESPACE / MANIFEST
        if dry_run or (current.is_file() and current.read_bytes() == (stage / NAMESPACE / MANIFEST).read_bytes()):
            return len(names), None
        backup = publish(stage, root, names)
        return len(names), backup


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("root", nargs="?", default=os.environ.get("MARKETING_OS_INSTALL_ROOT") or str(Path.home() / ".codex"))
    parser.add_argument("--dry-run", action="store_true", help="Validate sources and conflicts without changing the runtime")
    args = parser.parse_args()
    try:
        count, backup = install(Path(args.repo), Path(args.root), args.dry_run)
    except (InstallError, OSError) as exc:
        print(f"Installation stopped: {exc}", file=sys.stderr)
        return 1
    status = "Dry run passed for" if args.dry_run else "Installed"
    print(f"{status} {count} skills at {Path(args.root).expanduser()}.")
    print("Personal instructions and unrelated skills were not changed.")
    if backup:
        print(f"Previous managed installation backed up to: {backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
