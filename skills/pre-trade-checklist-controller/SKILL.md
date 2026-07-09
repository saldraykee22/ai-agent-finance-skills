---
name: pre-trade-checklist-controller
description: Run a final pre-trade gate for spot trades and investments across BIST, crypto, US, Germany, ETFs, FX, and commodities. Use before entering, adding, trimming, or exiting when the agent must verify data freshness, catalyst risk, liquidity, spread, slippage, position size, portfolio impact, invalidation, order plan, and post-trade monitoring.
---

# Pre-Trade Checklist Controller

## Core Rule

Block a trade plan when key facts are stale, the instrument is ambiguous, the invalidation is missing, or the position size cannot survive a realistic gap or liquidity shock.

## Workflow

1. Confirm the exact instrument with `asset-master-data-manager` when ambiguity exists.
2. Confirm current price, volume, event calendar, corporate actions, and token unlocks with source timestamps.
3. Check portfolio impact: size, concentration, correlation, cash use, FX bucket, liquidity, and downside scenario.
4. Check execution quality: spread, order book or volume, session timing, partial fill risk, slippage, and order type.
5. Define entry trigger, invalidation, add rule, trim rule, exit rule, and review date.
6. Define post-trade route: blotter, ledger, TCA, journal, and dashboard update.
7. Return `Pass`, `Conditional Pass`, or `Do Not Execute Yet`.

## Use Together

Use with `spot-trading-playbook`, `position-lifecycle-manager`, `liquidity-execution-analyst`, `portfolio-risk-manager`, `economic-calendar-monitor`, `corporate-actions-analyst`, `market-manipulation-anomaly-detector`, `trade-blotter-operations-controller`, and `portfolio-recordkeeping-ledger`.

## Output

Return `Verified Facts`, `Checklist`, `Blocking Issues`, `Execution Plan`, `Position Impact`, `Post-Trade Route`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for the full gate.
