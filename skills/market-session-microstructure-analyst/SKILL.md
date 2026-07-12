---
name: market-session-microstructure-analyst
description: Analyze market sessions, auctions, order types, circuit breakers, price limits, volatility interruptions, order book depth, settlement, liquidity windows, crypto 24/7 trading, BIST session behavior, and execution microstructure. Use when the user asks when to trade, why price moved at open/close, how session structure affects spot execution, or how microstructure changes risk.
---

# Market Session Microstructure Analyst

## Core Workflow

Use this skill before timing entries/exits where session structure matters. Read `references/analysis-workflow.md` for BIST and crypto microstructure checks.

## Operating Rules

- Identify venue, session, order type, liquidity window, and market status.
- For BIST, check opening/closing behavior, volatility measures, regulatory trading restrictions, and settlement context.
- For crypto, check 24/7 liquidity cycles, exchange maintenance, weekend liquidity, and order book depth.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Venue/session context
2. Liquidity window
3. Order book and execution risk
4. Microstructure constraints
5. Execution timing suggestion

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
