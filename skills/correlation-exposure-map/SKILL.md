---
name: correlation-exposure-map
description: Map portfolio correlation, hidden concentration, factor exposure, sector exposure, narrative exposure, currency exposure, liquidity exposure, custody exposure, and drawdown clustering across BIST, crypto spot, US, Germany, ETFs, FX, commodities, and cash. Use when the user asks whether positions are too similar, what risks are duplicated, or how portfolio holdings may move together.
---

# Correlation Exposure Map

## Core Rule

Look for hidden single bets. Different tickers can still be the same macro, sector, liquidity, currency, custody, or crypto narrative exposure.

## Workflow

1. List positions, weights, currencies, sectors, narratives, venues, custody locations, and liquidity buckets.
2. Group exposures by market beta, sector, factor, FX, rates, commodity, crypto narrative, stablecoin, custody, and event risk.
3. Estimate correlation using observed data where available and qualitative drivers where data is weak.
4. Identify clusters that could fail together in stress.
5. Route to `portfolio-risk-manager`, `scenario-stress-tester`, `drawdown-recovery-manager`, and `capital-allocation-cash-manager`.

## Output

Return `Exposure Map`, `Correlation Clusters`, `Hidden Concentration`, `Stress Linkages`, `Risk Reduction Options`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for exposure mapping templates.
