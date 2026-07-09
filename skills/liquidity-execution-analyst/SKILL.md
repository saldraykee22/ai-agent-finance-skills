---
name: liquidity-execution-analyst
description: Analyze liquidity and execution quality for spot trades, including order size, bid-ask spread, average daily volume, order book depth, market impact, partial fills, session timing, BIST liquidity, crypto exchange liquidity, and execution plan design. Use when the user asks how to enter or exit a spot position, whether a trade size is too large, how to reduce slippage, or how liquidity affects risk.
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
