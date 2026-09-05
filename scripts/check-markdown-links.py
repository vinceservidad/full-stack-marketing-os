#!/usr/bin/env python3
"""Check inline relative Markdown file/directory links in tracked documents.

This structural check does not validate remote URLs or heading fragments.
Untracked scratch files are deliberately outside the repository contract.
"""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


LINK = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def check(repo):
    names = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=repo
    ).decode("utf-8").split("\0")
    broken, checked = [], 0
    for name in names:
        if not name.endswith(".md"):
            continue
        path = repo / name
        if not path.is_file():
            continue  # a tracked file deleted in the working tree
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if SCHEME.match(target) or target.startswith("//"):
                continue
            checked += 1
            if not (path.parent / unquote(target)).exists():
                broken.append(f"{name} -> {target}")
    return checked, broken


def main():
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    checked, broken = check(repo)
    print(f"Checked {checked} relative Markdown file/directory links.")
    for finding in broken:
        print(f"Broken link: {finding}", file=sys.stderr)
    return int(bool(broken))


if __name__ == "__main__":
    raise SystemExit(main())
