---
name: portfolio-dashboard-designer
description: Design portfolio, watchlist, risk, performance, alert, and market regime dashboards for BIST and crypto spot portfolios plus US, Germany, FX, commodities, ETFs, and macro context. Use when the user asks what dashboard to build, which metrics to show, how to organize portfolio monitoring, or how to make finance analysis visually decision-ready.
---

# Portfolio Dashboard Designer

## Core Rule

Design dashboards for decisions and exceptions. Prioritize exposure, risk, alerts, catalysts, liquidity, and next action over decorative charts.

## Workflow

1. Define dashboard user, cadence, and decisions: daily check, trade prep, portfolio review, post-trade, or research.
2. Select pages: overview, holdings, cash, watchlist, alerts, risk, performance, market regime, sector/narrative rotation, trade journal, and data quality.
3. Define each widget with metric, source, refresh cadence, threshold, owner skill, and action rule.
4. Include BIST and crypto spot first; add US, Germany, FX, commodities, and macro only when they affect decisions.
5. Route data schema needs to `market-data-pipeline-architect` and alert logic to `alert-automation-runbook`.

## Output

Return `Dashboard Objective`, `Pages`, `Widgets`, `Thresholds`, `Data Sources`, `Action Rules`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for dashboard layout and metric catalog.
