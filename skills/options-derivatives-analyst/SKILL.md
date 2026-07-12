---
name: options-derivatives-analyst
description: Analyze options, futures, perpetuals, implied volatility, skew, term structure, open interest, gamma, delta, hedging, spreads, collars, covered calls, protective puts, funding, basis, roll yield, and derivatives positioning. Use when the user asks about options before earnings, hedging, futures curves, crypto perps, leverage, implied move, volatility trades, or derivative-based market signals.
---

# Options Derivatives Analyst

## Core Workflow

Use this skill for derivative structure and positioning analysis. Read `references/analysis-workflow.md` for option/futures/perp data checks, strategy mapping, and output format.

## Operating Rules

- Identify underlying, venue, expiry, strike, contract size, settlement, and currency.
- Timestamp IV, OI, funding, basis, and futures curve data.
- Separate directional view, volatility view, and hedge objective.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Instrument and objective
2. Volatility and positioning
3. Strategy or hedge map
4. Greeks/risk
5. Scenarios and failure modes

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
