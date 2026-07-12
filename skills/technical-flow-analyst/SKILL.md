---
name: technical-flow-analyst
description: Analyze price action, trend, support/resistance, volume, momentum, volatility, breadth, relative strength, order flow proxies, positioning, options flow, liquidity zones, and trade setup structure. Use when the user asks about charts, entries, exits, trend, breakout/breakdown, technical levels, market breadth, momentum, volume confirmation, or flow-driven market behavior.
---

# Technical Flow Analyst

## Core Workflow

Use this skill for technical and positioning analysis across equities, crypto, FX, rates, commodities, and indices. If current levels, volume, futures positioning, options data, or market breadth matter, verify current data and timestamp it.

Read `references/analysis-workflow.md` for the full chart, flow, breadth, volatility, and trade-setup framework.

## Operating Rules

- Separate observed price/volume facts, derived indicators, and interpretation.
- Treat levels as zones and invalidation areas, not magic numbers.
- Confirm signals across timeframe, volume, relative strength, and market context.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.
- Use only data available as of the stated cutoff. Align signal timeframe with decision horizon and require higher-timeframe context before declaring a spot setup ready.

## Companion Skills

- Use `market-data-source-verifier` for current price, volume, adjusted history, OI, IV, funding, and breadth data.
- Use `portfolio-risk-manager` to convert setups into sizing, invalidation, gap risk, and portfolio exposure.
- Use `options-derivatives-analyst` when options, futures, funding, basis, or gamma context drives the move.
- Use `position-lifecycle-manager`, `liquidity-execution-analyst`, and `decision-quality-behavioral-analyst` before turning a chart setup into a spot action.

## Single-Idea To Portfolio Rule

Every setup should identify trigger, invalidation, position sizing implication, liquidity/gap risk, and how the setup affects existing exposure.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Trend and regime
2. Key levels
3. Momentum and volume
4. Relative strength and breadth
5. Flow/positioning
6. Setup, trigger, invalidation
