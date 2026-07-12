---
name: scenario-stress-tester
description: Stress test positions and portfolios across market, macro, liquidity, FX, rate, drawdown, crypto crash, BIST selloff, policy shock, exchange risk, and idiosyncratic scenarios. Use when the user asks what happens if markets fall, TRY moves, BTC drops, BIST gaps down, liquidity vanishes, or a thesis faces a severe adverse scenario.
---

# Scenario Stress Tester

## Core Workflow

Use this skill to quantify or structure downside before action. Read `references/analysis-workflow.md` for scenario templates, loss mapping, and action thresholds.

## Operating Rules

- Separate scenario definition, portfolio impact, liquidity impact, and action threshold.
- Use ranges when exact holdings or prices are missing.
- For BIST/crypto spot, prioritize gap risk, liquidity, FX, exchange/custody, and correlated selloffs.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Scenario set
2. Exposure affected
3. Estimated impact
4. Liquidity and execution constraints
5. Action thresholds

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
