---
name: commodities-market-analyst
description: Analyze commodities including crude oil, natural gas, refined products, gold, silver, copper, industrial metals, grains, softs, freight, inventories, futures curves, supply-demand balances, seasonality, geopolitical shocks, and producer/consumer impacts. Use when the user asks about commodity prices, futures curves, inventories, OPEC, EIA, metals demand, agriculture supply, inflation pass-through, or commodity-linked equities and currencies.
---

# Commodities Market Analyst

## Core Workflow

Use this skill for commodity market analysis. If the task depends on current spot/futures prices, inventories, OPEC decisions, weather, production, shipping, curve structure, or geopolitical events, verify current data and timestamp it.

Read `references/analysis-workflow.md` for the full commodity supply-demand, curve, inventory, seasonality, and cross-asset impact workflow.

## Operating Rules

- Separate physical fundamentals, futures curve signals, positioning, and macro interpretation.
- Identify contract, delivery month, exchange, unit, currency, and roll logic.
- Treat inventories and curve structure as core evidence, not side details.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Companion Skills

- Use `market-data-source-verifier` for spot/futures prices, inventories, curve data, production, and event claims.
- Use `macro-market-strategist`, `fixed-income-fx-analyst`, and `portfolio-risk-manager` for cross-asset impact.
- Use `sector-industry-analyst` when commodity moves affect producers, consumers, or sector margins.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Market snapshot
2. Supply-demand balance
3. Inventories and curve
4. Macro/geopolitical drivers
5. Positioning and seasonality
6. Scenarios and impacted assets
