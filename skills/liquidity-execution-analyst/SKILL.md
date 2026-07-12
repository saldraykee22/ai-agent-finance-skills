---
name: liquidity-execution-analyst
description: Plan pre-trade liquidity and execution for a proposed spot order using intended size, bid-ask spread, volume, order-book depth, expected market impact, partial fills, session timing, venue, fees, and slippage. Use before a BIST, crypto, equity, ETF, FX, or commodity order when the user asks how to execute, whether the planned order is too large, which order type/session to use, or what slippage to expect. Use execution TCA after a fill is completed.
---

# Liquidity Execution Analyst

## Core Workflow

Use this skill before spot entry/exit decisions. Read `references/analysis-workflow.md` for liquidity checks, order planning, BIST/crypto differences, and output format.

## Operating Rules

- Check liquidity before sizing confidence.
- Treat BIST small/mid caps and crypto altcoins as liquidity-sensitive by default.
- Prefer staged execution when order size is meaningful versus volume or depth.
- Use `market-session-microstructure-analyst` when session timing, auction, order book, maintenance, circuit breaker, or venue microstructure changes execution risk.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Liquidity snapshot
2. Trade size vs market
3. Execution risks
4. Suggested execution plan
5. Post-trade review metrics

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
