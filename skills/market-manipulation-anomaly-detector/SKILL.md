---
name: market-manipulation-anomaly-detector
description: Detect suspicious or abnormal market behavior in BIST equities, crypto tokens, thinly traded assets, low float names, exchange pairs, and event driven moves. Use when price or volume looks unusual, a move may be pump and dump, wash trading, spoofing like order book pressure, news leakage, social hype, low float squeeze, fake liquidity, or abnormal pre disclosure movement.
---

# Market Manipulation Anomaly Detector

## Core Rule

Flag anomaly risk without overclaiming intent. Describe observable evidence, alternative explanations, and what would reduce or increase suspicion.

## Workflow

1. Establish normal baseline: historical volume, volatility, spread, order book depth, free float, holder concentration, and event calendar.
2. Compare the current move to baseline using price change, volume multiple, intraday pattern, liquidity, news timing, social flow, and venue fragmentation.
3. Check catalysts: KAP, filings, exchange notices, token unlocks, listings, delistings, macro events, and corporate actions.
4. Classify anomaly type: genuine catalyst, liquidity squeeze, low float move, event leakage risk, social pump, fake volume, wash trading suspicion, or leverage driven move.
5. Route to `pre-trade-checklist-controller` before acting on abnormal moves.

## Output

Return `Verified Facts`, `Anomaly Evidence`, `Alternative Explanations`, `Risk Classification`, `Action Constraints`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for anomaly checklist.
