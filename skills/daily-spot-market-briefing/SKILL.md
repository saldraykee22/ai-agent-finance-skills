---
name: daily-spot-market-briefing
description: Prepare a daily BIST and crypto spot market briefing with regime, catalysts, calendar, watchlist triggers, risk alarms, liquidity, macro context, and action priorities. Use when the user asks for today's market prep, morning briefing, daily plan, what to watch, BIST/crypto agenda, or how to approach spot markets for the day.
---

# Daily Spot Market Briefing

## Core Workflow

Use this skill for the user's daily BIST and crypto preparation. Read `references/analysis-workflow.md` for briefing structure, data checks, and output format.

## Operating Rules

- Verify current-sensitive market facts with timestamps.
- Lead with BIST and crypto, then include global macro only if it affects the day.
- Convert events into watchlist triggers and posture, not just headlines.
- Use `market-breadth-internals-analyst` when rally quality, participation, leadership concentration, or breadth divergence affects today's posture.
- Use `sell-discipline-exit-manager` when the daily plan includes trims, exits, or profit protection for extended positions.
- Use `drawdown-recovery-manager` when recent losses require a reduced-risk day plan.
- Do not add generic boilerplate caveats. Keep output concise, sourced, and action-oriented.
- Match the user's language.

## Default Output Shape

1. Daily regime
2. BIST agenda
3. Crypto agenda
4. Watchlist triggers
5. Risk alarms
6. Today’s posture
