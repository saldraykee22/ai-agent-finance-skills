---
name: economic-calendar-monitor
description: Build and interpret market event calendars covering macro releases, central bank meetings, earnings, dividends, corporate actions, token unlocks, index rebalances, futures expiries, option expiries, auctions, regulatory dates, and geopolitical catalysts. Use when the user asks what events matter this week/month, what to watch before trading, or how upcoming catalysts affect assets.
---

# Economic Calendar Monitor

## Core Workflow

Use this skill to structure upcoming catalysts and event risk. Read `references/analysis-workflow.md` for calendar categories, source hierarchy, prioritization, and output format.

## Operating Rules

- Verify dates, time zones, and release times with current sources.
- Separate scheduled events from tentative or rumored events.
- Rank events by likely asset impact.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Calendar window
2. High-impact events
3. Asset exposure
4. Scenario risks
5. Preparation checklist
