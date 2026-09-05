#!/usr/bin/env python3
"""Generate portable GPT knowledge from current canonical sources.

Run without arguments to rebuild gpt-knowledge/pack, or --check to detect drift.
This exports Markdown knowledge, not tools, live evidence, or proven model behavior.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys
from collections import Counter
from urllib.parse import unquote, urlsplit

BUNDLES = [
    ("00-operating-system", "Operating System and Routing", ["marketing-router"]),
    ("01-contracts", "Terminology and Governance Contracts", []),
    ("02-growth-strategy", "Business-Level Growth Strategy", ["growth-strategy"]),
    ("03-intake-and-research", "Intake, Customer Research, and ICP", ["marketing-intake", "customer-research", "icp-jtbd"]),
    ("04-google-ads", "Google Ads", ["google-ads"]),
    ("05-meta-ads", "Meta Ads", ["meta-ads"]),
    ("06-video-and-social-ads", "YouTube and TikTok Advertising", ["youtube-ads", "tiktok-ads"]),
    ("07-b2b-and-programmatic", "LinkedIn and Programmatic", ["linkedin-ads", "programmatic"]),
    ("08-partnerships", "Influencer and Affiliate Marketing", ["influencer-marketing", "affiliate-marketing"]),
    ("09-organic-social-and-pr", "Organic Social and Public Relations", ["organic-social", "public-relations"]),
    ("10-creative-and-copy", "Creative Strategy and Copywriting", ["creative-strategy", "copywriting"]),
    ("11-conversion-offer-pricing", "Conversion, Offer, and Pricing", ["cro", "offer-strategy", "pricing-monetization"]),
    ("12-seo", "Search Engine Optimization", ["seo"]),
    ("13-lifecycle-marketing", "Lifecycle and Email Marketing", ["lifecycle-marketing"]),
    ("14-measurement", "Tracking, Attribution, and Incrementality", ["tracking-measurement"]),
    ("15-diagnostics-reporting-operations", "Diagnostics, Reporting, and Operations", ["performance-diagnostics", "marketing-reporting", "marketing-operations"]),
    ("16-activation-and-retention", "Activation, Retention, and Customer Economics", ["activation", "retention-strategy", "retention-economics"]),
    ("17-optimization-scaling", "Optimization and Scaling", ["optimization-scaling"]),
]
BUNDLES.append(("18-supporting-library", "Frameworks, Playbooks, Workflows, and Templates", []))
CONTRACTS = ["GLOSSARY.md", "KNOWLEDGE-TAXONOMY.md", "PLATFORM-CURRENCY.md", "ARTIFACT-OWNERSHIP.md"]
LIBRARIES = ("frameworks", "playbooks", "workflows", "templates")
HEADER = "<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->\n"
# Canonical sources use inline Markdown links without whitespace in their targets.
# Code examples are excluded from this transformation.
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


class ExportError(ValueError):
    """Source or output violates the export contract."""


def reject_symlink_ancestors(path):
    for candidate in [path, *path.parents]:
        if candidate.is_symlink():
            raise ExportError(f"Refusing symlink path: {candidate}")


def reject_source_symlinks(root):
    # rglob('*.md') does not visit a symlinked references directory. Inspect
    # every entry first so an apparently complete export cannot omit it.
    reject_symlink_ancestors(root)
    for candidate in root.rglob("*"):
        if candidate.is_symlink():
            raise ExportError(f"Symlink source is not supported: {candidate}")


def source_layout(repo):
    """Assign every skill exactly once and include all supporting Markdown."""
    skills_dir = repo / ".agents" / "skills"
    for root in [skills_dir, *(repo / library for library in LIBRARIES)]:
        reject_source_symlinks(root)
    governed = {p.parent.name for p in skills_dir.glob("*/SKILL.md") if p.is_file()}
    assigned = [name for _, _, names in BUNDLES for name in names]
    duplicates = sorted(name for name, count in Counter(assigned).items() if count > 1)
    if duplicates:
        raise ExportError("Skill assigned to more than one bundle: " + ", ".join(duplicates))
    missing, unknown = governed - set(assigned), set(assigned) - governed
    if missing:
        raise ExportError("Governed skills with no export bundle: " + ", ".join(sorted(missing)))
    if unknown:
        raise ExportError("Bundle names a nonexistent skill: " + ", ".join(sorted(unknown)))
    ids = [bundle_id for bundle_id, _, _ in BUNDLES]
    if len(ids) != len(set(ids)):
        raise ExportError("Duplicate export bundle id")

    layout = []
    for bundle_id, title, names in BUNDLES:
        sources = []
        if bundle_id == "00-operating-system":
            sources += [repo / "AGENTS.md", repo / "CAPABILITY-REGISTRY.md"]
        if bundle_id == "01-contracts":
            sources += [repo / name for name in CONTRACTS]
        for name in names:
            skill = skills_dir / name
            sources.append(skill / "SKILL.md")
            # Include nested references and future Markdown support files, not
            # just references/*.md. Non-Markdown assets remain outside scope.
            sources += sorted(p for p in skill.rglob("*.md") if p != skill / "SKILL.md")
        if bundle_id == "18-supporting-library":
            for library in LIBRARIES:
                directory = repo / library
                if not directory.is_dir():
                    raise ExportError(f"Missing supporting library: {library}")
                sources += sorted(directory.rglob("*.md"))
        for source in sources:
            if not source.is_file():
                raise ExportError(f"Missing source: {source.relative_to(repo)}")
            # Source symlinks can import unversioned or out-of-repo content.
            if source.resolve() != source.absolute():
                raise ExportError(f"Symlink source is not supported: {source.relative_to(repo)}")
        layout.append((bundle_id, title, names, sources))
    return layout


def portable_text(repo, source, included):
    """Preserve source prose; replace local links with traceable source labels."""
    text = source.read_text(encoding="utf-8")

    def replace(match):
        label, target = match.groups()
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            return match.group(0)
        resolved = (source.parent / unquote(url.path)).resolve()
        if resolved.is_dir() and (resolved / "SKILL.md").is_file():
            resolved /= "SKILL.md"
        if resolved not in included:
            raise ExportError(f"Local link is not exported: {source.relative_to(repo)} -> {target}")
        identifier = resolved.relative_to(repo).as_posix()
        if url.fragment:
            identifier += "#" + url.fragment
        return f"{label} (source: `{identifier}`)"

    lines, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = FENCE.match(line)
        if marker:
            delimiter = marker.group(1)
            if fence is None:
                fence = delimiter
            elif delimiter[0] == fence[0] and len(delimiter) >= len(fence):
                fence = None
            lines.append(line)
        elif fence:
            lines.append(line)
        else:
            lines.append(LINK.sub(replace, line))
    return "".join(lines)


def instructions():
    # Avoid creating a second, hand-summarized set of marketing decision rules.
    return HEADER + """
# Custom GPT instructions

Paste the text below the separator into the GPT's Instructions field. The
numbered Markdown files are Knowledge uploads; this file and MANIFEST.md are
setup and provenance material, not Knowledge uploads.

---

You use the Full-Stack Marketing OS knowledge pack to answer marketing requests.
Apply the Contributor Instructions and Capability Registry in
00-operating-system.md, the contracts in 01-contracts.md, and the owning skill's
required inputs, method, quality checks, and output shape. Route substantial
requests with marketing-router and appoint one owner as that skill requires.
The canonical source text governs; this setup layer adds no marketing rules.

Each source section identifies its original repository path. A reference to a
repository path means consult that source section in the uploaded pack, not a
file on a local runtime. Consult the supporting-library file for frameworks,
playbooks, workflows, and templates. If required material is unavailable, say
so and preserve the owning skill's missing-input and evidence boundaries.

The pack is a versioned knowledge snapshot. It does not provide live account
access, runtime tools, project context, current platform verification, or
background execution. Ask for decision-relevant project context and evidence
when needed. Apply PLATFORM-CURRENCY.md before current platform claims; do not
present the pack's presence or a generated output as proof of current behavior.
Follow the canonical authorization requirements and report the actual action
state. Never claim an external change, upload, schedule, or verification that
did not occur. Apply optional voice guidance only within the canonical rules.
"""


def render(repo):
    layout = source_layout(repo)
    included = {source.resolve() for *_, sources in layout for source in sources}
    output, manifest, inventory = {}, [], []
    for bundle_id, title, names, sources in layout:
        parts = [HEADER, f"# {title}", "",
                 "Source paths identify the bundled repository documents. Local links are",
                 "rendered as source labels; external URLs and fenced examples are preserved.", ""]
        for source in sources:
            relative = source.relative_to(repo).as_posix()
            parts += [f"## Source: `{relative}`", "", portable_text(repo, source, included).rstrip(), ""]
            digest = hashlib.sha256(source.read_bytes()).hexdigest()
            inventory.append((relative, bundle_id + ".md", digest))
        contents = "\n".join(parts).rstrip() + "\n"
        output[bundle_id + ".md"] = contents
        manifest.append((bundle_id, title, names, len(contents.split())))
    output["INSTRUCTIONS.md"] = instructions()
    lines = [HEADER, "# Pack manifest", "",
             f"{len(layout)} knowledge files; {sum(len(names) for _, _, names, _ in layout)} governed skills; "
             f"{len(inventory)} source documents.", "",
             "Upload the numbered Markdown files as Knowledge. Paste the instruction body",
             "from INSTRUCTIONS.md into Instructions. Keep this manifest for provenance.", "",
             "## Coverage and limits", "",
             "Included: every governed SKILL.md and Markdown support file under its directory;",
             "AGENTS.md, CAPABILITY-REGISTRY.md, the four governance contracts; and every",
             "Markdown document in frameworks/, playbooks/, workflows/, and templates/.", "",
             "Not included: runtime tools or scripts, non-Markdown assets, local project",
             "context, client evidence, examples, evaluations, archive material, and optional",
             "voice files. Local Markdown links outside the export fail generation. Bare",
             "paths and URLs are not dependency discovery; the named source directories",
             "define coverage. Export integrity does not prove retrieval or decision quality.", "",
             "## Upload files", "",
             "| File | Covers | Skills | Words |", "|---|---|---|---:|"]
    for bundle_id, title, names, words in manifest:
        skills = ", ".join(f"`${name}`" for name in names) or "supporting documents"
        lines.append(f"| `{bundle_id}.md` | {title} | {skills} | {words:,} |")
    lines += ["", f"**Total: {sum(words for *_, words in manifest):,} words.**", "",
              "## Source inventory", "",
              "SHA-256 hashes refer to original source bytes before local-link presentation changes.", "",
              "| Source | Export file | SHA-256 |", "|---|---|---|"]
    lines += [f"| `{path}` | `{bundle}` | `{digest}` |" for path, bundle, digest in sorted(inventory)]
    output["MANIFEST.md"] = "\n".join(lines) + "\n"
    return output


def tree_bytes(directory):
    """Read recursively and byte-exactly; metadata equality is never proof."""
    reject_symlink_ancestors(directory)
    if not directory.is_dir():
        return {".": ("missing", b"")}
    contents = {}
    for path in sorted(directory.rglob("*")):
        name = path.relative_to(directory).as_posix()
        if path.is_symlink():
            contents[name] = ("symlink", str(path.readlink()))
        elif path.is_file():
            contents[name] = ("file", path.read_bytes())
        elif path.is_dir():
            contents[name + "/"] = ("directory", b"")
        else:
            contents[name] = ("unsupported", b"")
    return contents


def drift(committed, expected):
    actual = tree_bytes(committed)
    wanted = {name: ("file", text.encode("utf-8")) for name, text in expected.items()}
    return sorted(name for name in actual.keys() | wanted.keys() if actual.get(name) != wanted.get(name))


def write_pack(out_dir, output):
    # Do not follow output symlinks or silently erase unrecognized user files.
    reject_symlink_ancestors(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for path in out_dir.rglob("*"):
        if path.is_symlink():
            raise ExportError(f"Refusing symlink in generated pack: {path}")
        if path.is_dir():
            raise ExportError(f"Unexpected directory in generated pack; review manually: {path}")
        if path.is_file():
            if path.parent != out_dir or not path.read_bytes().startswith(HEADER.encode("utf-8")):
                raise ExportError(f"Unrecognized file in generated pack; review manually: {path}")
    for path in out_dir.iterdir():
        if path.is_file() and path.name not in output:
            path.unlink()  # Only a file carrying our exact generated-file header.
    for name, contents in output.items():
        (out_dir / name).write_text(contents, encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--check", action="store_true", help="Fail on generated-output drift")
    args = parser.parse_args(argv)
    repo = pathlib.Path(args.repo).resolve()
    committed = repo / "gpt-knowledge" / "pack"
    try:
        output = render(repo)
        if args.check:
            changed = drift(committed, output)
            if changed:
                print("GPT pack differs from current canonical sources:", file=sys.stderr)
                for name in changed:
                    print(f"- {name}", file=sys.stderr)
                print("Run python3 scripts/build-gpt-knowledge.py and review the result.", file=sys.stderr)
                return 1
            print("GPT knowledge pack is in sync with current canonical sources.")
        else:
            write_pack(committed, output)
            print(f"Built {len(BUNDLES)} knowledge files in {committed}.")
    except (ExportError, OSError, UnicodeError) as error:
        print(f"GPT export error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
