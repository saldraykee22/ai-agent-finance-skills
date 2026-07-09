---
name: quant-factor-analyst
description: Analyze quantitative factors, momentum, value, quality, low volatility, size, beta, correlation, drawdown, rolling returns, factor exposure, simple backtests, ranking models, and portfolio diagnostics. Use when the user asks for factor screens, performance attribution, correlation, beta, volatility, drawdown, ranking logic, signal design, or simple historical tests.
---

# Quant Factor Analyst

## Core Workflow

Use this skill for rules-based market analysis and factor diagnostics. Read `references/analysis-workflow.md` for factor definitions, data hygiene, simple test design, and output format.

## Operating Rules

- Define universe, rebalance frequency, signal formula, ranking direction, and lookback.
- Avoid overfitting; prefer simple transparent factors.
- Separate signal design, test results, and interpretation.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Universe and factor objective
2. Signal definitions
3. Data checks
4. Results or diagnostic table
5. Failure modes
