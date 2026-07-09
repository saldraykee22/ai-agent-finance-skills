---
name: fixed-income-fx-analyst
description: Analyze fixed income, interest rates, yield curves, duration, credit spreads, sovereign bonds, corporate bonds, CDS, central bank pricing, inflation breakevens, real yields, FX pairs, carry, balance of payments, and currency risk. Use when the user asks about bonds, rates, credit, yield curve moves, central bank pricing, sovereign risk, USD/EUR/TRY or other FX pairs, carry trades, or currency impact on assets.
---

# Fixed Income FX Analyst

## Core Workflow

Use this skill for rates, credit, sovereign, and FX analysis. If the task depends on current yields, spreads, curves, central bank expectations, CDS, FX levels, inflation data, or bond prices, verify current data and timestamp it.

Read `references/analysis-workflow.md` for the full rates/credit/FX workflow, source hierarchy, curve analysis, and output format.

## Operating Rules

- Separate market levels, macro drivers, policy expectations, and risk interpretation.
- Always identify currency, maturity, duration, issuer, seniority, and benchmark.
- Think in real yields, rate differentials, credit risk, liquidity, and external balances.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Companion Skills

- Use `market-data-source-verifier` for yields, curves, FX, CDS, inflation, policy rates, and auction data.
- Use `macro-market-strategist` for regime context and `portfolio-risk-manager` for duration, FX, and credit exposure.
- Use `economic-calendar-monitor` for central bank, auction, and macro release dates.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Market snapshot
2. Rates and curve view
3. Credit or sovereign risk
4. FX drivers
5. Carry, duration, and liquidity
6. Scenarios and watchpoints
