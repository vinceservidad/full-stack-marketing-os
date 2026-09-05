"""Installer regression tests. Fixtures are synthetic; no personal runtime is used."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install-skills.py"
spec = importlib.util.spec_from_file_location("installer", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="marketing-os-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / "source with spaces"
        self.root = self.base / "runtime with spaces"
        self.repo.mkdir()
        for name in installer.CONTRACTS:
            self.write(self.repo / name, "# " + name + "\n")
        for name in installer.LIBRARIES:
            self.write(self.repo / name / "guide.md", "# Guide\n")
        self.add_skill("google-ads")
        self.add_skill("creative-strategy")
        self.write(self.repo / "CAPABILITY-REGISTRY.md", "[Google](.agents/skills/google-ads/SKILL.md)\n")
        self.write(self.repo / "frameworks" / "guide.md", "[Google](../.agents/skills/google-ads/SKILL.md)\n")

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def add_skill(self, name):
        path = self.repo / ".agents" / "skills" / name
        self.write(path / "SKILL.md", f"---\nname: {name}\ndescription: Test fixture skill for installation validation only.\n---\n\n# Test\n[Glossary](../../../GLOSSARY.md#terms)\n[Guide](../../../frameworks/guide.md)\n[Reference](references/detail.md)\n")
        self.write(path / "references" / "detail.md", "[Rules](../../../../AGENTS.md)\n[Copy](../../creative-strategy/SKILL.md)\n")

    def snapshot(self):
        if not self.root.exists():
            return None
        result = {}
        for path in sorted(self.root.rglob("*")):
            key = path.relative_to(self.root).as_posix()
            result[key] = ("symlink", os.readlink(path)) if path.is_symlink() else ("directory",) if path.is_dir() else path.read_bytes()
        return result

    def test_clean_install_and_all_skill_links(self):
        count, backup = installer.install(self.repo, self.root)
        self.assertEqual(count, 2)
        self.assertIsNone(backup)
        for name in ("AGENTS.md", "CLAUDE.md", "GLOSSARY.md", "frameworks"):
            self.assertFalse((self.root / name).exists())
        skill = self.root / "skills/google-ads/SKILL.md"
        self.assertTrue(skill.read_text().startswith("---\n"))
        self.assertIn("../../.marketing-os/AGENTS.md", skill.read_text())
        self.assertIn("../../.marketing-os/GLOSSARY.md#terms", skill.read_text())
        self.assertIn("../../../.marketing-os/AGENTS.md", (skill.parent / "references/detail.md").read_text())
        self.assertIn("../skills/google-ads/SKILL.md", (self.root / ".marketing-os/CAPABILITY-REGISTRY.md").read_text())
        self.assertIn("../../skills/google-ads/SKILL.md", (self.root / ".marketing-os/frameworks/guide.md").read_text())
        installer.check_target(self.root, ["creative-strategy", "google-ads"])

    def test_preserves_personal_files_and_unrelated_broken_links(self):
        sentinels = {"AGENTS.md": "Personal instructions\n", "CLAUDE.md": "Personal Claude instructions\n", "frameworks/my-work.md": "Keep this\n", "skills/unrelated/SKILL.md": "[Unrelated missing file](../missing.md)\n"}
        for name, text in sentinels.items():
            self.write(self.root / name, text)
        installer.install(self.repo, self.root)
        for name, text in sentinels.items():
            self.assertEqual((self.root / name).read_text(), text)

    def test_collision_refused_before_any_changes(self):
        self.write(self.root / "skills/google-ads/SKILL.md", "Unrelated Google Ads skill\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "collision"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_unmanaged_namespace_refused(self):
        self.write(self.root / ".marketing-os/notes.md", "Do not remove\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Unmanaged namespace"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_dry_run_does_not_create_runtime(self):
        count, _ = installer.install(self.repo, self.root, dry_run=True)
        self.assertEqual(count, 2)
        self.assertFalse(self.root.exists())

    def test_dry_run_still_rejects_collisions(self):
        self.write(self.root / "skills/google-ads/notes.txt", "Keep\n")
        before = self.snapshot()
        with self.assertRaises(installer.InstallError):
            installer.install(self.repo, self.root, dry_run=True)
        self.assertEqual(before, self.snapshot())

    def test_broken_skill_link_refused_before_changes(self):
        self.write(self.repo / ".agents/skills/google-ads/references/detail.md", "[Missing](missing.md)\n")
        with self.assertRaisesRegex(installer.InstallError, "Unresolved skill link"):
            installer.install(self.repo, self.root)
        self.assertFalse(self.root.exists())

    def test_missing_dependency_refused_before_changes(self):
        (self.repo / "AGENTS.md").unlink()
        with self.assertRaisesRegex(installer.InstallError, "Missing managed path"):
            installer.install(self.repo, self.root)
        self.assertFalse(self.root.exists())

    def test_reinstall_is_idempotent(self):
        installer.install(self.repo, self.root)
        before = self.snapshot()
        count, backup = installer.install(self.repo, self.root)
        self.assertEqual(count, 2)
        self.assertIsNone(backup)
        self.assertEqual(before, self.snapshot())

    def test_update_backs_up_owned_files(self):
        installer.install(self.repo, self.root)
        original = (self.root / ".marketing-os/AGENTS.md").read_bytes()
        self.write(self.repo / "AGENTS.md", "# Revised rules\n")
        _, backup = installer.install(self.repo, self.root)
        self.assertEqual((backup / ".marketing-os/AGENTS.md").read_bytes(), original)
        self.assertEqual((self.root / ".marketing-os/AGENTS.md").read_text(), "# Revised rules\n")
        installer.check_target(self.root, ["creative-strategy", "google-ads"])

    def test_local_edits_refused(self):
        installer.install(self.repo, self.root)
        self.write(self.root / "skills/google-ads/notes.txt", "Local work\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "modified locally"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_modified_managed_contract_refused(self):
        installer.install(self.repo, self.root)
        self.write(self.root / ".marketing-os/GLOSSARY.md", "Local glossary\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "modified locally"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_removed_skill_is_backed_up_not_left_active(self):
        installer.install(self.repo, self.root)
        shutil.rmtree(self.repo / ".agents/skills/google-ads")
        count, backup = installer.install(self.repo, self.root)
        self.assertEqual(count, 1)
        self.assertFalse((self.root / "skills/google-ads").exists())
        self.assertTrue((backup / "skills/google-ads/SKILL.md").is_file())

    def test_symlinked_skills_directory_refused(self):
        external = self.base / "external"
        external.mkdir()
        self.root.mkdir()
        (self.root / "skills").symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(installer.InstallError, "symlink"):
            installer.install(self.repo, self.root)
        self.assertEqual(list(external.iterdir()), [])

    def test_symlinked_source_file_refused(self):
        external = self.base / "external.md"
        self.write(external, "Keep\n")
        (self.repo / "AGENTS.md").unlink()
        (self.repo / "AGENTS.md").symlink_to(external)
        with self.assertRaisesRegex(installer.InstallError, "symlink"):
            installer.install(self.repo, self.root)
        self.assertFalse(self.root.exists())

    def test_overlapping_directories_refused(self):
        with self.assertRaisesRegex(installer.InstallError, "overlap"):
            installer.install(self.repo, self.repo / "runtime")
        with self.assertRaisesRegex(installer.InstallError, "overlap"):
            installer.install(self.repo, self.base)

    def test_corrupt_manifest_refused(self):
        installer.install(self.repo, self.root)
        self.write(self.root / ".marketing-os/manifest.json", '{"owner": "other-project"}\n')
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Invalid installation manifest"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_manifest_path_traversal_refused(self):
        installer.install(self.repo, self.root)
        marker = self.root / ".marketing-os/manifest.json"
        data = json.loads(marker.read_text())
        data["skills"] = ["../../personal"]
        self.write(marker, json.dumps(data))
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Invalid installation manifest"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_existing_lock_preserved(self):
        installer.install(self.repo, self.root)
        self.write(self.root / ".marketing-os-install.lock", "Another installer\n")
        self.write(self.repo / "AGENTS.md", "# Update\n")
        before = self.snapshot()
        with self.assertRaisesRegex(installer.InstallError, "Install lock exists"):
            installer.install(self.repo, self.root)
        self.assertEqual(before, self.snapshot())

    def test_failed_update_restores_previous_install(self):
        installer.install(self.repo, self.root)
        original = installer.inventory(self.root, installer.skill_paths(["creative-strategy", "google-ads"]))
        self.write(self.repo / "AGENTS.md", "# Update\n")
        real_replace = os.replace
        failed = False

        def fail_once(src, dst):
            nonlocal failed
            if not failed and "ready/skills/google-ads" in str(src):
                failed = True
                raise OSError("Simulated interrupted publication")
            return real_replace(src, dst)

        with mock.patch.object(installer.os, "replace", side_effect=fail_once):
            with self.assertRaisesRegex(OSError, "Simulated"):
                installer.install(self.repo, self.root)
        self.assertTrue(failed)
        self.assertEqual(original, installer.inventory(self.root, installer.skill_paths(["creative-strategy", "google-ads"])))
        self.assertFalse((self.root / ".marketing-os-install.lock").exists())
        installer.check_target(self.root, ["creative-strategy", "google-ads"])

    def test_shell_positional_interface(self):
        result = subprocess.run(["bash", str(SCRIPT.with_suffix(".sh")), str(self.repo), str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Installed 2 skills", result.stdout)

    def test_environment_target_and_dry_run(self):
        env = dict(os.environ, MARKETING_OS_INSTALL_ROOT=str(self.root))
        result = subprocess.run(["bash", str(SCRIPT.with_suffix(".sh")), str(self.repo), "--dry-run"], env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.root.exists())


if __name__ == "__main__":
    unittest.main()
