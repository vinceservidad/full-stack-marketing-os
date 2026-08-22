#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path


def skill_root(repo: Path) -> Path:
    staging = repo / "work" / "skill-src"
    return staging if staging.is_dir() else repo / ".agents" / "skills"


def verified_date(path: Path) -> date:
    match = re.search(r"^\*\*Last verified:\*\* (\d{4}-\d{2}-\d{2})", path.read_text(), re.MULTILINE)
    if not match:
        raise ValueError(f"Missing Last verified date: {path}")
    return date.fromisoformat(match.group(1))


def main() -> int:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    today = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date.today()
    maximum_age = 30
    stale: list[str] = []

    for platform in ("google-ads", "meta-ads"):
        registry = skill_root(repo) / platform / "references" / "platform-current.md"
        age = (today - verified_date(registry)).days
        if age < 0:
            stale.append(f"{platform}: verification date is {abs(age)} days in the future")
        elif age > maximum_age:
            stale.append(f"{platform}: registry is {age} days old (maximum {maximum_age})")
        else:
            print(f"{platform}: current ({age} days old)")

    if stale:
        print("Platform currency review required:", file=sys.stderr)
        for problem in stale:
            print(f"- {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
