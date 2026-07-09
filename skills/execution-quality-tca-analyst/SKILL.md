---
name: execution-quality-tca-analyst
description: Analyze execution quality and transaction cost impact for completed or planned spot trades using slippage, spread, arrival price, VWAP, TWAP, market impact, partial fills, session timing, exchange venue, FX conversion, commissions, and liquidity conditions. Use when reviewing filled trades, improving order execution, comparing broker or exchange quality, or measuring whether trade implementation harmed performance.
---

# Execution Quality TCA Analyst

## Core Rule

Separate thesis outcome from execution outcome. A profitable trade can still have poor execution, and a losing trade can still be executed well.

## Workflow

1. Capture order plan and actual fills: timestamp, side, quantity, venue, order type, limit, fill prices, fees, FX conversion, and market context.
2. Compare fills against arrival price, mid, spread, VWAP, TWAP, day range, and post-fill drift when data is available.
3. Estimate explicit costs, spread cost, slippage, market impact, opportunity cost, and avoidable timing cost.
4. Identify execution errors: chasing, poor session, oversized order, thin book, ignored price limit, fragmented venue, or emotional modification.
5. Reconcile fills with `trade-blotter-operations-controller` and `portfolio-recordkeeping-ledger` when order status, fees, or quantities are uncertain.
6. Feed lessons into `trade-journal-reviewer`, `liquidity-execution-analyst`, and `pre-trade-checklist-controller`.

## Output

Return `Verified Facts`, `Execution Metrics`, `Cost Breakdown`, `What Worked`, `What Failed`, `Process Fixes`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for TCA fields.
