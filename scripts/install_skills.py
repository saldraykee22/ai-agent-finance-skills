#!/usr/bin/env python3
"""Install the skill collection into Codex, Hermes, or Antigravity."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"


def default_target(platform: str) -> Path:
    home = Path.home()
    return {
        "codex": home / ".codex" / "skills",
        "hermes": home / ".hermes" / "skills",
        "antigravity": home / ".gemini" / "config" / "skills",
        "shared": home / ".agents" / "skills",
    }[platform]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--platform",
        choices=("codex", "hermes", "antigravity", "shared"),
        required=True,
    )
    parser.add_argument(
        "--target",
        type=Path,
        help="Override the platform default, for example <workspace>/.agents/skills",
    )
    parser.add_argument("--force", action="store_true", help="Replace existing skill folders")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    return parser.parse_args()


def install(target: Path, force: bool, dry_run: bool) -> tuple[int, int]:
    skills = sorted(path for path in SOURCE.iterdir() if path.is_dir())
    conflicts = [target / skill.name for skill in skills if (target / skill.name).exists()]
    if conflicts and not force:
        preview = "\n".join(f"- {path}" for path in conflicts[:10])
        suffix = f"\n... and {len(conflicts) - 10} more" if len(conflicts) > 10 else ""
        raise SystemExit(
            "Existing skill folders found; no files changed. Use --force to replace them:\n"
            f"{preview}{suffix}"
        )

    if dry_run:
        for skill in skills:
            action = "replace" if (target / skill.name).exists() else "install"
            print(f"{action}: {skill.name} -> {target / skill.name}")
        return len(skills), len(conflicts)

    target.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        destination = target / skill.name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(skill, destination)
    return len(skills), len(conflicts)


def main() -> int:
    args = parse_args()
    target = (args.target or default_target(args.platform)).expanduser().resolve()
    count, replaced = install(target, args.force, args.dry_run)
    mode = "Would install" if args.dry_run else "Installed"
    print(f"{mode} {count} skills to {target} ({replaced} replacements)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
