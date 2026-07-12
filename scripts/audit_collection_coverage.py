#!/usr/bin/env python3
"""Audit explicit collection coverage against the repository's product objective."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

REQUIRED_GROUPS = {
    "BIST priority": {
        "bist-crypto-spot-command-center",
        "bist-market-analyst",
        "bist-kap-disclosure-analyst",
        "bist-sector-rotation-analyst",
    },
    "crypto priority": {
        "crypto-market-analyst",
        "crypto-onchain-flow-analyst",
        "crypto-tokenomics-supply-analyst",
        "crypto-narrative-rotation-analyst",
        "stablecoin-liquidity-risk-analyst",
        "security-wallet-operations-analyst",
    },
    "spot lifecycle": {
        "personal-investment-policy",
        "spot-trading-playbook",
        "pre-trade-checklist-controller",
        "position-lifecycle-manager",
        "sell-discipline-exit-manager",
        "liquidity-execution-analyst",
        "execution-quality-tca-analyst",
        "portfolio-risk-manager",
        "trade-blotter-operations-controller",
        "portfolio-recordkeeping-ledger",
    },
    "global markets": {
        "us-equity-market-analyst",
        "germany-equity-market-analyst",
        "fixed-income-fx-analyst",
        "commodities-market-analyst",
        "macro-market-strategist",
        "options-derivatives-analyst",
        "etf-fund-flow-analyst",
    },
    "professional controls": {
        "finance-agent-orchestrator",
        "market-data-source-verifier",
        "data-quality-reconciliation-engine",
        "finance-research-quality-auditor",
        "signal-scoring-decision-engine",
        "investment-committee-simulator",
        "scenario-stress-tester",
        "financial-report-writer",
    },
}

REQUIRED_TEXT = {
    "skills/bist-crypto-spot-command-center/SKILL.md": (
        "Prioritize BIST equities and crypto spot",
        "borsa-mcp",
        "binance-trader-mcp",
    ),
    "skills/api-source-integration-planner/references/mcp-tool-routing.md": (
        "saidsurucu/borsa-mcp",
        "saldraykee22/binance-trader-mcp",
        "Hermes Agent, Codex, and Antigravity",
        "Public research tier",
        "Private read tier",
        "Mutation tier",
    ),
    "skills/pre-trade-checklist-controller/SKILL.md": (
        "it is not permission to trade",
        "explicit current-conversation instruction",
        "Never blindly resubmit",
    ),
    "docs/platform-setup.md": (
        "--platform codex",
        "--platform hermes",
        "--platform antigravity",
        "BINANCE_DRY_RUN",
    ),
}


def main() -> int:
    failures = []
    installed = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    for group, required in REQUIRED_GROUPS.items():
        missing = sorted(required - installed)
        if missing:
            failures.append(f"{group}: missing {', '.join(missing)}")

    for relative, needles in REQUIRED_TEXT.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing artifact: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                failures.append(f"{relative}: missing {needle!r}")

    if failures:
        print("\n".join(failures))
        return 1
    print(
        f"Audited {len(REQUIRED_GROUPS)} capability groups, {sum(map(len, REQUIRED_GROUPS.values()))} "
        f"required skill roles, and {sum(map(len, REQUIRED_TEXT.values()))} objective clauses"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
