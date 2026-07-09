---
name: alert-automation-runbook
description: Define market alert automation, trigger logic, severity, cadence, escalation, stale-data checks, and review workflows for BIST equities, KAP disclosures, crypto prices, token unlocks, on-chain flows, stablecoins, watchlists, portfolio risk, macro events, and trade lifecycle states. Use when the user wants alerts, monitors, reminders, trigger rules, or watchlist automation design.
---

# Alert Automation Runbook

## Core Rule

Every alert must have a purpose, severity, source, freshness rule, action owner, and false-positive handling. Avoid noisy alerts that do not change decisions.

## Workflow

1. Define alert objective: price, volume, disclosure, event, risk, portfolio drift, thesis break, or execution.
2. Define trigger logic with threshold, source, timestamp, cadence, and cool-down.
3. Assign severity: info, watch, action, urgent, or block.
4. Define response: ignore, review, run specialist skill, update watchlist, pre-trade gate, trim, or journal.
5. Add stale-data and source-conflict handling with `market-data-source-verifier` and `data-quality-reconciliation-engine`.

## Use Together

Use with `watchlist-alert-monitor`, `economic-calendar-monitor`, `portfolio-dashboard-designer`, `thesis-risk-register`, and `pre-trade-checklist-controller`.

## Output

Return `Alert Map`, `Trigger Rules`, `Severity`, `Response Workflow`, `False Positive Controls`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for alert templates.
