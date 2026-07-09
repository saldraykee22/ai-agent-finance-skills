---
name: market-breadth-internals-analyst
description: Analyze market breadth and internals including advance decline, new highs and lows, participation, sector breadth, volume breadth, equal weight versus cap weight, crypto market cap breadth, BTC or ETH dominance, stablecoin liquidity, and leadership concentration. Use when the user asks whether a BIST or crypto rally is healthy, broad, narrow, fragile, or rotating.
---

# Market Breadth Internals Analyst

## Core Rule

A market move is stronger when participation expands. Narrow leadership can still work, but it raises concentration and reversal risk.

## Workflow

1. Define market universe: BIST index, BIST sectors, crypto majors, altcoin universe, or watchlist.
2. Check participation: advancers, decliners, highs, lows, breadth thrust, volume breadth, equal-weight strength, and sector/narrative spread.
3. Check leadership concentration and whether gains depend on a few large names.
4. Compare breadth to regime, liquidity, stablecoin flows, FX/rates, and risk appetite.
5. Route to `bist-sector-rotation-analyst`, `crypto-narrative-rotation-analyst`, `relative-strength-momentum-ranker`, and `market-regime-dashboard`.

## Output

Return `Verified Facts`, `Breadth Map`, `Participation Quality`, `Leadership Concentration`, `Regime Implication`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for breadth indicators.
