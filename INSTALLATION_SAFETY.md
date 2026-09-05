# Safe installation and updates

The installer writes generated skills to `<runtime>/skills/<name>/` and shared Marketing OS contracts and libraries to `<runtime>/.marketing-os/`. It never writes global `AGENTS.md` or `CLAUDE.md`, and never replaces runtime-root `frameworks/`, `playbooks/`, `templates/`, or `workflows/` directories.

Each generated skill links explicitly to `.marketing-os/AGENTS.md`. The repository's operating rules remain available without replacing the user's personal or project instructions. Canonical source stays in `.agents/skills/`; generated copies are not a second source of truth.

## Install or preview

Python 3 is required. Existing positional commands remain supported:

```bash
bash scripts/install-skills.sh . "$HOME/.codex" --dry-run
bash scripts/install-skills.sh . "$HOME/.codex"
bash scripts/install-claude-skills.sh
```

`MARKETING_OS_INSTALL_ROOT` still supplies the default destination when the second positional argument is omitted. `--dry-run` validates sources, required skill links, and destination conflicts without creating or changing the destination runtime.

## What is protected

- Existing personal instructions, shared root libraries, and unrelated skills are left untouched. An unrelated skill's broken link does not make this package's installation fail.
- An existing skill with the same name is refused unless a valid Marketing OS ownership manifest records it. The installer does not guess that a familiar name grants overwrite permission.
- Managed files are hashed. Locally modified files, added files, missing dependencies, invalid manifests, symlink destinations, and source/destination overlap stop the install rather than silently discard work.
- Sources and skill links are validated in temporary staging before publication. A repeated install of identical content is a no-op. Changed installations back up the previous managed trees before replacing them. Retired skills leave the active skill directory but remain in the backup.

## Migrate an older installation

Earlier installers did not record ownership. Consequently, an older installation may stop with a skill-collision message. This is deliberate.

Back up only the old Marketing OS skill directories named in the collision message and move those directories outside the runtime's `skills/` directory. Preserve unrelated skills and personal instruction files. Then rerun the installer. Do not move the entire `skills/` directory or automatically remove shared files from the runtime root.

The new installer does not delete or adopt legacy root contracts and libraries. Review those separately. It cannot reconstruct personal files overwritten by an earlier installer; recovery requires a backup made before that overwrite.

## Backups and failure recovery

A changed installation retains the previous managed trees under `<runtime>/.marketing-os-backups/<run-id>/`. That backup includes its ownership manifest. Successful installation prints the exact backup path.

An ordinary publication error triggers restoration of the previous managed trees. The exclusive `.marketing-os-install.lock` prevents cooperating installers from publishing concurrently. Do not remove the lock while an installer is running.

A process kill, machine crash, disk failure, or failure during rollback itself is not covered by a crash-safe transaction guarantee. In that situation, inspect the reported error, retained backup, and lock before running the installer again. Do not delete backups until recovery is verified. There is no automatic rollback CLI in this change.

## Verification and scope

Run the isolated regression suite:

```bash
python3 -m unittest discover -s tests -p 'test_install_skills.py' -v
```

The `Installer safety` workflow runs the suite, a full-repository installation, a repeat-install check, and the Claude wrapper using temporary runtimes on Ubuntu and macOS. The skill-link check covers this package's generated skill files and their references, not every link in all repository documentation. These tests validate installation mechanics, not model decision quality or live agent discovery.

This is a focused reliability change. It does not add skills, generate GPT exports, merge PR #27, or claim a measured improvement in marketing outcomes. PR #27 must preserve this installation-safety contract when its broader distribution work is reconciled.
