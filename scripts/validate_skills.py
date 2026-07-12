#!/usr/bin/env python3
"""Validate repository skill structure without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
REFERENCE_RE = re.compile(r"`(references/[^`]+)`")


def fields(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    result = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate(root: Path) -> list[str]:
    errors = []
    for folder in sorted(path for path in root.iterdir() if path.is_dir()):
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        metadata = fields(text)
        if set(metadata) != {"name", "description"}:
            errors.append(f"{folder.name}: frontmatter must contain only name and description")
        if metadata.get("name") != folder.name:
            errors.append(f"{folder.name}: frontmatter name does not match folder")
        if not NAME_RE.fullmatch(folder.name):
            errors.append(f"{folder.name}: invalid skill name")
        if not metadata.get("description"):
            errors.append(f"{folder.name}: empty description")
        if len(text.splitlines()) > 500:
            errors.append(f"{folder.name}: SKILL.md exceeds 500 lines")
        agent_yaml = folder / "agents" / "openai.yaml"
        if not agent_yaml.is_file():
            errors.append(f"{folder.name}: missing agents/openai.yaml")
        elif f"${folder.name}" not in agent_yaml.read_text(encoding="utf-8"):
            errors.append(f"{folder.name}: default prompt does not invoke the skill")
        for reference in REFERENCE_RE.findall(text):
            if not (folder / Path(reference)).is_file():
                errors.append(f"{folder.name}: broken reference {reference}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "skills"
    errors = validate(root)
    if errors:
        print("\n".join(errors))
        return 1
    count = sum(path.is_dir() for path in root.iterdir())
    print(f"Validated {count} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
