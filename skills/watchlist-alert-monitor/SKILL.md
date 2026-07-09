---
name: watchlist-alert-monitor
description: Define alerts, triggers, monitoring cadence, watchlist states, event reminders, price/volume/liquidity thresholds, KAP/filing/news checks, token unlock checks, on-chain alerts, and review workflows. Use when the user asks to monitor BIST or crypto watchlists, define alert levels, know when to revisit a thesis, or turn research into a monitoring system.
---

# Watchlist Alert Monitor

## Core Workflow

Use this skill to convert watchlists into actionable monitoring. Read `references/analysis-workflow.md` for alert types, watchlist states, cadence, and output format.

## Operating Rules

- Every watchlist item needs a state: research, waiting for trigger, active, review, remove.
- Alerts must map to actions, not just notifications.
- Use `alert-automation-runbook` when alerts need severity, cadence, cool-down, stale-data handling, or response workflow.
- Use `portfolio-dashboard-designer` when watchlist states and alerts should appear in a recurring dashboard.
- For BIST and crypto, include price, volume, liquidity, news/KAP, token unlock, on-chain, and custody/venue alerts where relevant.
- Do not add generic boilerplate caveats. Keep output analytical, direct, and operational.
- Match the user's language.

## Default Output Shape

1. Watchlist objective
2. States and triggers
3. Alert table
4. Review cadence
5. Action map
