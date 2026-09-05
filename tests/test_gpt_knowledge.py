"""Regression checks for export completeness, provenance, and drift detection."""

import hashlib
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("gpt_export", REPO / "scripts/build-gpt-knowledge.py")
EXPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXPORT)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name).resolve()
        self.skill = self.repo / ".agents/skills/owner"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("---\nname: owner\n---\n\n# Owner\n\nKeep this rule.\n")
        for name in ["AGENTS.md", "CAPABILITY-REGISTRY.md", *EXPORT.CONTRACTS]:
            (self.repo / name).write_text(f"# {name}\n\nCanonical rule.\n")
        for directory in EXPORT.LIBRARIES:
            (self.repo / directory).mkdir()
            (self.repo / directory / "sample.md").write_text(f"# {directory}\n\nSupporting content.\n")
        self.bundles = [
            ("00-operating-system", "Operating system", ["owner"]),
            ("01-contracts", "Contracts", []),
            ("18-supporting-library", "Supporting library", []),
        ]
        mock = patch.object(EXPORT, "BUNDLES", self.bundles)
        mock.start()
        self.addCleanup(mock.stop)
        self.out = self.repo / "gpt-knowledge/pack"

    def test_nested_support_and_all_libraries_are_exported_with_hashes(self):
        nested = self.skill / "references/deep/example.md"
        nested.parent.mkdir(parents=True)
        nested.write_text("# Deep support\n\nDecision-changing detail.\n")
        output = EXPORT.render(self.repo)
        self.assertIn(nested.read_text(), output["00-operating-system.md"])
        self.assertIn(hashlib.sha256(nested.read_bytes()).hexdigest(), output["MANIFEST.md"])
        for directory in EXPORT.LIBRARIES:
            self.assertIn(f"{directory}/sample.md", output["18-supporting-library.md"])
        self.assertIn((self.skill / "SKILL.md").read_text(), output["00-operating-system.md"])

    def test_new_skill_cannot_silently_miss_export(self):
        added = self.repo / ".agents/skills/new-capability"
        added.mkdir()
        (added / "SKILL.md").write_text("# New skill\n")
        with self.assertRaisesRegex(EXPORT.ExportError, "no export bundle: new-capability"):
            EXPORT.render(self.repo)

    def test_duplicate_unknown_and_duplicate_bundle_assignments_fail(self):
        for extra, message in [
            (("other", "Other", ["owner"]), "more than one bundle"),
            (("other", "Other", ["missing"]), "nonexistent skill"),
            (("01-contracts", "Other", []), "Duplicate export bundle id"),
        ]:
            with self.subTest(message=message):
                with patch.object(EXPORT, "BUNDLES", self.bundles + [extra]):
                    with self.assertRaisesRegex(EXPORT.ExportError, message):
                        EXPORT.render(self.repo)

    def test_source_labels_preserve_dependencies_urls_and_code_examples(self):
        source = self.skill / "SKILL.md"
        source.write_text(
            "# Owner\n\n[Template](../../../templates/sample.md#heading)\n"
            "[Skill](../owner/)\n[Official](https://example.org/path?q=x)\n"
            "```md\n[Example](not-a-dependency.md)\n# Keep heading\n```\n"
        )
        text = EXPORT.render(self.repo)["00-operating-system.md"]
        self.assertIn("Template (source: `templates/sample.md#heading`)", text)
        self.assertIn("Skill (source: `.agents/skills/owner/SKILL.md`)", text)
        self.assertIn("[Official](https://example.org/path?q=x)", text)
        self.assertIn("```md\n[Example](not-a-dependency.md)\n# Keep heading\n```", text)

    def test_missing_or_unexported_link_fails_before_writing(self):
        for target in ("missing.md", "../../../outside.md"):
            with self.subTest(target=target):
                (self.repo / "outside.md").write_text("# Outside coverage\n")
                (self.skill / "SKILL.md").write_text(f"# Owner\n\n[Required]({target})\n")
                with self.assertRaisesRegex(EXPORT.ExportError, "Local link is not exported"):
                    EXPORT.render(self.repo)
                self.assertFalse(self.out.exists())

    def test_source_change_changes_bundle_and_provenance(self):
        original = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, original)
        (self.repo / "templates/sample.md").write_text("# Changed template\n")
        changed = EXPORT.render(self.repo)
        self.assertEqual(
            EXPORT.drift(self.out, changed),
            ["18-supporting-library.md", "MANIFEST.md"],
        )

    def test_drift_is_byte_exact_even_when_size_and_mtime_match(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        path = self.out / "00-operating-system.md"
        before = path.stat()
        path.write_bytes(path.read_bytes().replace(b"Keep this rule.", b"Drop this rule."))
        os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns))
        self.assertEqual(path.stat().st_size, before.st_size)
        self.assertEqual(EXPORT.drift(self.out, output), [path.name])

    def test_missing_extra_nested_and_empty_directory_drift(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        (self.out / "MANIFEST.md").unlink()
        (self.out / "extra.txt").write_text("Unexpected content")
        (self.out / "nested").mkdir()
        (self.out / "nested/extra.md").write_text("Hidden drift")
        (self.out / "empty").mkdir()
        self.assertEqual(EXPORT.drift(self.out, output), [
            "MANIFEST.md", "empty/", "extra.txt", "nested/", "nested/extra.md",
        ])

    def test_repeated_build_is_deterministic_and_stale_generated_file_is_removed(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        stale = self.out / "old-bundle.md"
        stale.write_text(EXPORT.HEADER + "Old generated content\n")
        EXPORT.write_pack(self.out, EXPORT.render(self.repo))
        self.assertFalse(stale.exists())
        self.assertEqual(EXPORT.drift(self.out, output), [])

    def test_unrecognized_files_are_preserved_for_manual_review(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        personal = self.out / "notes.md"
        personal.write_text("Keep my notes\n")
        with self.assertRaisesRegex(EXPORT.ExportError, "review manually"):
            EXPORT.write_pack(self.out, output)
        self.assertEqual(personal.read_text(), "Keep my notes\n")

    def test_symlink_output_is_not_followed(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        path = self.out / "00-operating-system.md"
        target = self.repo / "personal.md"
        target.write_text("Personal content\n")
        path.unlink()
        path.symlink_to(target)
        self.assertIn(path.name, EXPORT.drift(self.out, output))
        with self.assertRaisesRegex(EXPORT.ExportError, "symlink"):
            EXPORT.write_pack(self.out, output)
        self.assertEqual(target.read_text(), "Personal content\n")

    def test_expected_name_without_generated_header_is_preserved(self):
        output = EXPORT.render(self.repo)
        EXPORT.write_pack(self.out, output)
        personal = self.out / "INSTRUCTIONS.md"
        personal.write_text("My personal instructions\n")
        stale = self.out / "old-bundle.md"
        stale.write_text(EXPORT.HEADER + "Old content\n")
        before = EXPORT.tree_bytes(self.out)
        with self.assertRaisesRegex(EXPORT.ExportError, "review manually"):
            EXPORT.write_pack(self.out, output)
        self.assertEqual(EXPORT.tree_bytes(self.out), before)

    def test_check_and_build_reject_symlinked_output_parent(self):
        output = EXPORT.render(self.repo)
        external = self.repo / "external"
        EXPORT.write_pack(external / "pack", output)
        self.out.parent.symlink_to(external, target_is_directory=True)
        before = EXPORT.tree_bytes(external)
        with self.assertRaisesRegex(EXPORT.ExportError, "symlink"):
            EXPORT.drift(self.out, output)
        with self.assertRaisesRegex(EXPORT.ExportError, "symlink"):
            EXPORT.write_pack(self.out, output)
        self.assertEqual(EXPORT.tree_bytes(external), before)

    def test_symlinked_source_directories_cannot_silently_lose_coverage(self):
        target = self.repo / "outside-references"
        target.mkdir()
        (target / "decision.md").write_text("Required decision rule\n")
        for link in (self.skill / "references", self.repo / "templates/nested"):
            with self.subTest(link=link):
                link.symlink_to(target, target_is_directory=True)
                with self.assertRaisesRegex(EXPORT.ExportError, "Symlink source"):
                    EXPORT.render(self.repo)
                self.assertFalse(self.out.exists())
                link.unlink()


class RepositoryCoverageTests(unittest.TestCase):
    def test_every_current_canonical_markdown_source_is_present_once(self):
        layout = EXPORT.source_layout(REPO)
        sources = [path for *_, paths in layout for path in paths]
        self.assertEqual(len(sources), len(set(sources)))
        expected = set((REPO / ".agents/skills").glob("*/SKILL.md"))
        for skill in (REPO / ".agents/skills").iterdir():
            if (skill / "SKILL.md").is_file():
                expected.update(skill.rglob("*.md"))
        for directory in EXPORT.LIBRARIES:
            expected.update((REPO / directory).rglob("*.md"))
        expected.update(REPO / name for name in ["AGENTS.md", "CAPABILITY-REGISTRY.md", *EXPORT.CONTRACTS])
        self.assertEqual(set(sources), expected)
        # Also resolve every current inline Markdown dependency during rendering.
        self.assertEqual(len(EXPORT.render(REPO)), len(EXPORT.BUNDLES) + 2)


if __name__ == "__main__":
    unittest.main()
