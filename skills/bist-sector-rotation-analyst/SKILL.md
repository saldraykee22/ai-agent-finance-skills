---
name: bist-sector-rotation-analyst
description: Analyze BIST sector leadership, weekly or daily sector-index relative strength, breadth, liquidity, macro sensitivity, catalysts, valuation dispersion, and rotation among banks, holdings, industrials, aviation, defense, energy, retail, real estate, technology, and exporters. Use when the user asks which BIST sectors are gaining strength, leading or lagging, where money is rotating, or how sector leadership should change stock selection.
---

# BIST Sector Rotation Analyst

## Core Rule

Separate index-heavy leadership from broad sector participation. A sector is healthier when relative strength, breadth, volume, catalysts, and valuation support point in the same direction.

## Workflow

1. Define benchmark: XU100, XU030, sector index, or custom BIST universe.
2. Map sector performance, relative strength, breadth, volume, and liquidity.
3. Check macro drivers: rates, TRY, inflation, regulation, credit, exports, commodities, and domestic demand.
4. Check KAP and event catalysts for sector leaders and laggards.
5. Identify leaders, emerging turnarounds, overextended areas, and avoid zones.
6. Route candidate names to `bist-market-analyst`, `financial-statement-analyst`, `valuation-modeling-analyst`, `technical-flow-analyst`, and `pre-trade-checklist-controller`.

## Output

Return `Verified Facts`, `Sector Map`, `Leaders and Laggards`, `Rotation Evidence`, `Watchlist Actions`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for sector rotation scoring.

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
