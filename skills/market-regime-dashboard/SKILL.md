---
name: market-regime-dashboard
description: Summarize the current market regime for BIST, crypto, US/Germany equities, FX, rates, commodities, liquidity, volatility, breadth, and risk appetite. Use when the user asks what kind of market we are in, whether conditions favor spot entries, how BIST and crypto regimes compare, or how to adjust watchlists and exposure to regime.
---

# Market Regime Dashboard

## Core Workflow

Use this skill to create a concise top-down regime panel before spot decisions. Read `references/analysis-workflow.md` for dashboard components, regime labels, and action translation.

## Operating Rules

- Separate BIST regime, crypto regime, global risk regime, and portfolio implications.
- Use current data sources when regime depends on live prices, rates, FX, breadth, or volatility.
- Translate regime into watchlist posture, size posture, liquidity caution, and review cadence.
- Use `market-breadth-internals-analyst` for breadth confirmation and leadership concentration.
- Use `correlation-exposure-map` when regime changes may affect several portfolio positions through the same hidden driver.
- Use `daily-spot-market-briefing` when the user wants a day plan and `capital-allocation-cash-manager` when regime should change cash/deployment.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Regime label
2. BIST panel
3. Crypto panel
4. Global cross-asset panel
5. Spot posture
6. Watch next
