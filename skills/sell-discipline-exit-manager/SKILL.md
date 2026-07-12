---
name: sell-discipline-exit-manager
description: Manage sell discipline, exit rules, trims, invalidation, profit protection, thesis break handling, time stops, catalyst exits, liquidity exits, and post-entry risk controls for BIST, crypto spot, US, Germany, ETFs, FX, and commodities. Use when the user asks whether to sell, trim, hold, reduce risk, define exit levels, protect gains, or avoid emotional exits.
---

# Sell Discipline Exit Manager

## Core Rule

Separate thesis exit, risk exit, liquidity exit, and profit-taking. Do not let a winning position drift without an updated invalidation and trim plan.

## Workflow

1. Classify the position state: new, working, extended, thesis impaired, event risk, drawdown, or exit candidate.
2. Recheck thesis, price action, liquidity, catalyst calendar, portfolio concentration, and opportunity cost.
3. Define exit types: hard invalidation, time stop, event stop, partial trim, rebalance trim, liquidity exit, or full thesis exit.
4. Compare hold versus trim versus exit using scenarios and portfolio impact.
5. Route final action through `pre-trade-checklist-controller` and record through `trade-blotter-operations-controller`.

## Use Together

Use with `position-lifecycle-manager`, `portfolio-risk-manager`, `technical-flow-analyst`, `signal-scoring-decision-engine`, `investment-committee-simulator`, and `trade-journal-reviewer`.

## Output

Return `Verified Facts`, `Position State`, `Exit Triggers`, `Trim Plan`, `Hold Conditions`, `Portfolio Impact`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for exit templates.

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
