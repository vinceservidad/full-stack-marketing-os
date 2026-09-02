#!/usr/bin/env python3
"""Build the Custom GPT knowledge pack from the canonical skills.

`gpt-knowledge/pack/` is generated, never hand-edited. It exists because a
Custom GPT cannot load `.agents/skills/` directly: it takes a bounded number of
uploaded knowledge files. This compiles the 24 governed skills, their
references, and the root contracts into 18 bundles that fit that limit, so the
GPT runs the same governed system a local agent runtime does.

  build                 regenerate the pack
  --check               regenerate to a temporary directory and fail on drift
                        (CI: catches a skill added without an export entry, and
                        any hand-edit of generated output)

Every governed skill must appear in exactly one bundle. Adding a skill without
assigning it here fails the build rather than silently shipping a pack that is
missing a capability -- the failure this whole script exists to prevent.
"""

from __future__ import annotations

import argparse
import filecmp
import pathlib
import re
import shutil
import sys
import tempfile

# Bundle id -> (title, [skill names]). Order is the reading order for the GPT.
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

CONTRACTS = ["GLOSSARY.md", "KNOWLEDGE-TAXONOMY.md", "PLATFORM-CURRENCY.md", "ARTIFACT-OWNERSHIP.md"]

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
# A relative Markdown link is meaningless once the file is uploaded to a GPT.
# Keep the label, drop the path, so the model is never told to open a file that
# does not exist in its knowledge base.
RELATIVE_LINK = re.compile(r"\[([^\]]+)\]\((?!https?://|mailto:)[^)]+\)")


def flatten(text):
    return RELATIVE_LINK.sub(r"\1", text)


def demote(text, levels=1):
    """Push Markdown headings down so a bundled document nests correctly."""
    return re.sub(r"^(#{1,5}) ", lambda m: "#" * (len(m.group(1)) + levels) + " ", text, flags=re.MULTILINE)


def skill_block(repo, name):
    skill_dir = repo / ".agents" / "skills" / name
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    description = ""
    match = FRONTMATTER.match(text)
    if match:
        for line in match.group(1).splitlines():
            if line.startswith("description:"):
                description = line.partition(":")[2].strip()
        text = text[match.end():]

    # Drop the skill's own H1; "## Skill: $name" already titles this section.
    body = re.sub(r"\A#\s+.+?\n+", "", text.strip())

    parts = [f"## Skill: ${name}", ""]
    if description:
        parts += [f"**Use when:** {description}", ""]
    parts.append(flatten(demote(body, 1)))

    references = skill_dir / "references"
    if references.is_dir():
        for reference in sorted(references.glob("*.md")):
            parts += [
                "",
                f"### Reference: {reference.stem.replace('-', ' ')} (${name})",
                "",
                flatten(demote(reference.read_text(encoding="utf-8").strip(), 2)),
            ]
    return "\n".join(parts)


HEADER = """<!-- GENERATED FILE — DO NOT EDIT.
     Built from .agents/skills/ by scripts/build-gpt-knowledge.py.
     Edit the canonical skill and rebuild; CI fails if this file is hand-edited. -->

"""


def build(repo, out_dir):
    skills_dir = repo / ".agents" / "skills"
    governed = {d.name for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()}

    assigned = [name for _, _, names in BUNDLES for name in names]
    duplicates = {n for n in assigned if assigned.count(n) > 1}
    if duplicates:
        raise SystemExit(f"Skill assigned to more than one bundle: {', '.join(sorted(duplicates))}")

    missing = governed - set(assigned)
    if missing:
        raise SystemExit(
            "Governed skills with no export bundle: "
            + ", ".join(f"${s}" for s in sorted(missing))
            + "\nAssign each in BUNDLES in scripts/build-gpt-knowledge.py."
        )

    unknown = set(assigned) - governed
    if unknown:
        raise SystemExit(f"Bundle names a nonexistent skill: {', '.join(f'${s}' for s in sorted(unknown))}")

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []

    for bundle_id, title, names in BUNDLES:
        body = [HEADER, f"# {title}", ""]

        if bundle_id == "00-operating-system":
            body += [
                "These are the operating principles every response in this system follows.",
                "They take precedence over any tactic in the other knowledge files.",
                "",
                flatten(demote((repo / "AGENTS.md").read_text(encoding="utf-8").strip(), 1)),
                "",
                flatten(demote((repo / "CAPABILITY-REGISTRY.md").read_text(encoding="utf-8").strip(), 1)),
                "",
            ]
        if bundle_id == "01-contracts":
            for contract in CONTRACTS:
                body += [flatten(demote((repo / contract).read_text(encoding="utf-8").strip(), 1)), ""]

        for name in names:
            body += [skill_block(repo, name), ""]

        path = out_dir / f"{bundle_id}.md"
        path.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
        words = len(path.read_text(encoding="utf-8").split())
        manifest.append((bundle_id, title, names, words))

    write_instructions(repo, out_dir, governed)
    write_manifest(out_dir, manifest)

    # Remove files from a previous bundle layout. Renumbering or regrouping
    # bundles would otherwise leave stale duplicates in the pack, and a GPT
    # would load both the old and the new copy of the same skill.
    expected = {f"{bundle_id}.md" for bundle_id, *_ in manifest} | {"INSTRUCTIONS.md", "MANIFEST.md"}
    for stale in sorted(out_dir.glob("*.md")):
        if stale.name not in expected:
            stale.unlink()
            print(f"removed stale bundle: {stale.name}")

    return manifest


def write_instructions(repo, out_dir, governed):
    """The Custom GPT instruction box, not a knowledge upload."""
    text = f"""<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->

# Custom GPT instructions

Paste into the GPT's **Instructions** field. Upload every `*.md` in this
directory except this file and `MANIFEST.md` as **Knowledge**.

---

You are a full-stack marketing operator running the Full-Stack Marketing OS.
Your knowledge files contain {len(governed)} governed skills and the contracts
that govern them. `00-operating-system.md` outranks every other file.

**Before answering any substantial request:**

1. Route it. Identify the business outcome, funnel stage, and requested action,
   then name the one skill that owns the response. Consult the capability
   registry in `00-operating-system.md`. If no skill owns it, say so plainly —
   never substitute an adjacent channel skill for a capability that does not
   exist.
2. Establish the evidence state. Label each input observed, asserted,
   reconciled, contradicted, or unknown. A confident speaker does not upgrade an
   asserted figure. An unknown is not zero.
3. Check the authorization boundary. You draft; you do not change budgets, bids,
   campaigns, audiences, tracking, or live pages. Any live change is a proposal
   with the exact entity, current and proposed state, risk, a rollback rule, and
   an explicit approval request.

**Non-negotiable rules:**

- Never fabricate benchmarks, results, customer language, credentials, margins,
  or causality. If you do not have it, say you do not have it.
- Prefer profit, realized revenue, or qualified pipeline. Never substitute ROAS,
  CTR, or platform attribution for a business outcome.
- Never state a profit figure without naming the profit level and the costs
  included. Never deduct discounts or refunds already inside net revenue.
- Do not claim an undocumented platform algorithm change. Separate officially
  documented capability, account-visible behavior, experimentally observed
  impact, inference, and unknowns.
- Scaling is not spending more. It requires scoped proof, source-of-truth
  economics, marginal efficiency, a diagnosed binding constraint, capacity,
  guardrails, and explicit approval. Reject universal budget-increase
  percentages.
- Separate observed facts, calculations, inferences, assumptions, and unknowns
  in every answer.

**Output shape:** state the owning skill, then the deliverable that skill
defines, then the unknowns that could reverse your conclusion. End with an exact
status line saying what is done, what is drafted, and what needs approval.

When a decision-changing input is missing, continue only where it is safe to do
so, label the assumption, and say plainly what is blocked.
"""
    (out_dir / "INSTRUCTIONS.md").write_text(text, encoding="utf-8")


def write_manifest(out_dir, manifest):
    lines = [
        "<!-- GENERATED FILE — DO NOT EDIT. Built by scripts/build-gpt-knowledge.py. -->",
        "",
        "# Pack manifest",
        "",
        f"{len(manifest)} knowledge files, generated from the canonical skills in `.agents/skills/`.",
        "Upload all of them as Knowledge; paste `INSTRUCTIONS.md` into the Instructions field.",
        "",
        "| File | Covers | Skills | Words |",
        "|---|---|---|---:|",
    ]
    for bundle_id, title, names, words in manifest:
        skills = ", ".join(f"`${n}`" for n in names) if names else "root contracts"
        lines.append(f"| `{bundle_id}.md` | {title} | {skills} | {words:,} |")
    total = sum(w for *_, w in manifest)
    lines += ["", f"**Total: {total:,} words across {len(manifest)} files.**", ""]
    (out_dir / "MANIFEST.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--check", action="store_true", help="Fail if the committed pack differs from a fresh build")
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    committed = repo / "gpt-knowledge" / "pack"

    if not args.check:
        manifest = build(repo, committed)
        print(f"Built {len(manifest)} knowledge files to gpt-knowledge/pack/ "
              f"({sum(w for *_, w in manifest):,} words).")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        fresh = pathlib.Path(tmp) / "pack"
        build(repo, fresh)
        if not committed.is_dir():
            print("gpt-knowledge/pack/ is missing. Run scripts/build-gpt-knowledge.py.", file=sys.stderr)
            return 1
        comparison = filecmp.dircmp(str(committed), str(fresh))
        drift = sorted(comparison.diff_files + comparison.left_only + comparison.right_only)
        if drift:
            print("The committed GPT pack has drifted from the canonical skills:", file=sys.stderr)
            for item in drift:
                print(f"- {item}", file=sys.stderr)
            print("\nRun scripts/build-gpt-knowledge.py and commit the result.", file=sys.stderr)
            return 1

    print("GPT knowledge pack is in sync with the canonical skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
