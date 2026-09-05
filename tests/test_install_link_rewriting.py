"""Regression tests for the directory-link drift found by the full install check."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install-skills.py"
spec = importlib.util.spec_from_file_location("installer_link_tests", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class LinkRewritingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="marketing-os-links-")
        self.addCleanup(temporary.cleanup)
        base = Path(temporary.name).resolve()
        self.repo = base / "source"
        self.runtime = base / "runtime"
        self.repo.mkdir()
        for name in installer.CONTRACTS:
            (self.repo / name).write_text("# Fixture\n", encoding="utf-8")
        for name in installer.LIBRARIES:
            (self.repo / name).mkdir()
        self.skills = self.repo / ".agents" / "skills"
        for name in ("retention-economics", "marketing-intake"):
            directory = self.skills / name
            directory.mkdir(parents=True)
            (directory / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Synthetic installation test fixture.\n---\n\n# Fixture\n",
                encoding="utf-8",
            )
        self.skill = self.skills / "retention-economics" / "SKILL.md"

    def test_directory_links_keep_trailing_slashes(self):
        with self.skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[Intake](../marketing-intake/)\n[Library](../../../frameworks/)\n")
        installer.install(self.repo, self.runtime)
        installed = (self.runtime / "skills/retention-economics/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("[Intake](../marketing-intake/)", installed)
        self.assertIn("[Library](../../.marketing-os/frameworks/)", installed)
        # An identical reinstall must not turn link formatting into an update.
        _, backup = installer.install(self.repo, self.runtime)
        self.assertIsNone(backup)
        self.assertFalse((self.runtime / ".marketing-os-backups").exists())

    def test_reference_directory_fragments_and_file_links_are_preserved(self):
        references = self.skill.parent / "references"
        references.mkdir()
        (references / "details.md").write_text(
            "[Intake](../../marketing-intake/#inputs)\n"
            "[Library](../../../../frameworks/#overview)\n"
            "[File](../../../../GLOSSARY.md#terms)\n",
            encoding="utf-8",
        )
        with self.skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[Details](references/details.md)\n")
        installer.install(self.repo, self.runtime)
        installed = (self.runtime / "skills/retention-economics/references/details.md").read_text(encoding="utf-8")
        self.assertIn("[Intake](../../marketing-intake/#inputs)", installed)
        self.assertIn("[Library](../../../.marketing-os/frameworks/#overview)", installed)
        self.assertIn("[File](../../../.marketing-os/GLOSSARY.md#terms)", installed)
        installer.check_target(self.runtime, ["marketing-intake", "retention-economics"])


if __name__ == "__main__":
    unittest.main()
