#!/usr/bin/env python3
"""Validate the common skill contract used by supported agent platforms."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)


def parse_fields(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    result = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def main() -> int:
    errors = []
    skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    for folder in skills:
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        fields = parse_fields(skill_file.read_text(encoding="utf-8"))
        if set(fields) != {"name", "description"}:
            errors.append(f"{folder.name}: non-portable frontmatter fields {sorted(fields)}")
        if fields.get("name") != folder.name:
            errors.append(f"{folder.name}: name does not match folder")
        if len(fields.get("description", "")) < 40:
            errors.append(f"{folder.name}: description is too short for semantic discovery")
        for reference in re.findall(r"`(references/[^`]+)`", skill_file.read_text(encoding="utf-8")):
            if not (folder / reference).is_file():
                errors.append(f"{folder.name}: missing progressive-disclosure file {reference}")

    setup = (ROOT / "docs" / "platform-setup.md").read_text(encoding="utf-8")
    setup_requirements = {
        "Codex skill directory": "~/.codex/skills",
        "Hermes skill directory": "~/.hermes/skills",
        "Antigravity global skill directory": "~/.gemini/config/skills",
        "Antigravity workspace skill directory": ".agents/skills",
        "Codex MCP config": "~/.codex/config.toml",
        "Hermes MCP config": "~/.hermes/config.yaml",
        "Antigravity MCP config": "~/.gemini/config/mcp_config.json",
        "BIST source": "saidsurucu/borsa-mcp",
        "crypto source": "saldraykee22/binance-trader-mcp",
        "safe execution default": "BINANCE_DRY_RUN = \"true\"",
    }
    for label, needle in setup_requirements.items():
        if needle not in setup:
            errors.append(f"platform setup: missing {label} ({needle})")

    if errors:
        print("\n".join(errors))
        return 1
    print(
        f"Validated {len(skills)} portable skills and {len(setup_requirements)} platform setup contracts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
