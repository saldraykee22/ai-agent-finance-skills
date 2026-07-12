---
name: relative-strength-momentum-ranker
description: Rank assets, sectors, watchlists, or portfolios by relative strength, momentum, trend quality, volume confirmation, volatility, drawdown, liquidity, and benchmark outperformance across BIST, crypto, US equities, German equities, ETFs, FX, commodities, and sectors. Use when the user asks which names are strongest, which candidates to prioritize, or how to compare leaders and laggards.
---

# Relative Strength Momentum Ranker

## Core Rule

Rank on adjusted, comparable, liquid data. Do not compare assets with mismatched currencies, stale prices, or unadjusted corporate actions without labeling the distortion.

## Workflow

1. Define universe, benchmark, base currency, lookback windows, and liquidity filters.
2. Calculate or reason through absolute return, benchmark relative return, trend slope, breakout quality, volume confirmation, drawdown, volatility, and distance from invalidation.
3. Penalize poor liquidity, extreme gap risk, stale data, one-day spikes, corporate action distortions, and token unlock overhang.
4. Group results by market, sector, narrative, and portfolio exposure.
5. Route top candidates to market-specific analysts and `pre-trade-checklist-controller`.

## Output

Return `Verified Facts`, `Ranking Table`, `Leader Group`, `Lagging Group`, `Signal Quality`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for scoring and table format.

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
