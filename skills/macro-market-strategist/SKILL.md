---
name: macro-market-strategist
description: Build macro regime analysis and cross-asset strategy across growth, inflation, central banks, liquidity, fiscal policy, rates, FX, equities, credit, commodities, and risk appetite. Use when the user asks about macro outlook, market regimes, central bank decisions, inflation, recession risk, liquidity, country risk, cross-asset positioning, or how macro variables affect portfolios and markets.
---

# Macro Market Strategist

## Core Workflow

Use this skill for top-down macro and cross-asset analysis. If the request depends on current inflation, labor, GDP, PMI, central bank decisions, yield curves, FX, commodities, liquidity, fiscal policy, or geopolitical events, verify current data before forming the view.

Read `references/analysis-workflow.md` for the full macro regime workflow, source hierarchy, indicator checklist, cross-asset map, and output format.

## Operating Rules

- Separate data, policy interpretation, market pricing, and scenario judgment.
- Track level, direction, rate of change, and surprise versus expectations.
- Prefer official macro releases and central bank communications for primary facts.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Companion Skills

- Use `market-data-source-verifier` for current macro releases, central bank decisions, yields, FX, commodities, and risk assets.
- Use `fixed-income-fx-analyst`, `commodities-market-analyst`, and `portfolio-risk-manager` for cross-asset implications.
- Use `economic-calendar-monitor` for upcoming macro events and central bank calendars.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Macro regime
2. Fresh data checks
3. Central bank and liquidity view
4. Cross-asset implications
5. Scenario map
6. Indicators to watch next
