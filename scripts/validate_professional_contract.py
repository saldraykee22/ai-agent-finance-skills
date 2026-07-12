#!/usr/bin/env python3
"""Check cross-skill professional research and spot-decision invariants."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIREMENTS = {
    "skills/finance-research-quality-auditor/references/analysis-workflow.md": [
        "Professional evidence contract",
        "Calculation reproducibility",
        "Hard gates",
        "Confidence describes evidence strength",
        "inflation-accounting basis",
        "circulating market cap, FDV",
    ],
    "skills/signal-scoring-decision-engine/references/analysis-workflow.md": [
        "Thesis Attractiveness",
        "Execution Readiness",
        "normalized score = 50 + 25",
        "BIST/equity spot thesis weights",
        "Crypto spot thesis weights",
        "Execution-readiness weights",
        "pre-trade verdict is `Pass`",
    ],
    "skills/pre-trade-checklist-controller/SKILL.md": [
        "it is not permission to trade",
        "explicit current-conversation instruction",
        "Never blindly resubmit",
    ],
    "skills/api-source-integration-planner/references/mcp-tool-routing.md": [
        "Hermes Agent, Codex, and Antigravity",
        "Public research tier",
        "Private read tier",
        "Mutation tier",
        "Do not automatically retry a mutation",
    ],
    "skills/valuation-modeling-analyst/references/analysis-workflow.md": [
        "Crypto/token valuation",
        "token-holder value-accrual mechanism",
        "fully diluted outcomes",
    ],
    "skills/portfolio-risk-manager/references/analysis-workflow.md": [
        "adverse-gap scenario loss",
        "exit capacity",
        "Required sizing disclosure",
    ],
    "skills/financial-report-writer/SKILL.md": [
        "data cutoff",
        "execution authorization",
    ],
}


def decision(thesis: float, readiness: float, hard_gates: list[str], pretrade: str) -> str:
    """Mirror the documented deterministic decision mapping for scenario tests."""
    fatal = {"identity", "liquidity", "portfolio_loss"}
    if thesis < 40 or fatal.intersection(hard_gates):
        return "Reject"
    if thesis >= 60 and readiness >= 75 and not hard_gates and pretrade == "Pass":
        return "Ready"
    if thesis >= 60 and 60 <= readiness < 75:
        return "Wait for Trigger"
    if thesis >= 60:
        return "Watch"
    return "Watch"


SCENARIOS = [
    {
        "name": "BIST quality setup with fresh KAP and executable liquidity",
        "result": decision(72, 82, [], "Pass"),
        "expected": "Ready",
    },
    {
        "name": "BIST attractive valuation but unresolved identity",
        "result": decision(78, 80, ["identity"], "Pass"),
        "expected": "Reject",
    },
    {
        "name": "Crypto strong narrative but stale order book",
        "result": decision(76, 55, ["freshness"], "Conditional Pass"),
        "expected": "Watch",
    },
    {
        "name": "Crypto valid thesis waiting for unlock resolution",
        "result": decision(68, 66, ["event_conflict"], "Conditional Pass"),
        "expected": "Wait for Trigger",
    },
    {
        "name": "Crypto liquid setup without pre-trade Pass",
        "result": decision(70, 79, [], "Conditional Pass"),
        "expected": "Watch",
    },
]


def main() -> int:
    failures = []
    for relative, needles in REQUIREMENTS.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{relative}: missing contract clause {needle!r}")

    score = (ROOT / "skills/signal-scoring-decision-engine/references/analysis-workflow.md").read_text(
        encoding="utf-8"
    )
    for heading in (
        "BIST/equity spot thesis weights",
        "Crypto spot thesis weights",
        "Execution-readiness weights",
    ):
        section = score.split(f"## {heading}", 1)[1].split("## ", 1)[0]
        weights = [int(line.rsplit("|", 2)[1].strip()) for line in section.splitlines() if line.startswith("|") and line.rsplit("|", 2)[1].strip().isdigit()]
        if sum(weights) != 100:
            failures.append(f"{heading}: weights sum to {sum(weights)}, expected 100")

    for scenario in SCENARIOS:
        if scenario["result"] != scenario["expected"]:
            failures.append(
                f"scenario {scenario['name']!r}: got {scenario['result']}, expected {scenario['expected']}"
            )

    if failures:
        print("\n".join(failures))
        return 1
    print(
        f"Validated {len(REQUIREMENTS)} professional contracts, 3 weight tables, "
        f"and {len(SCENARIOS)} BIST/crypto spot scenarios"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
