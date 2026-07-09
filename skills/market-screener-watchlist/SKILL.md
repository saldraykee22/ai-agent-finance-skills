---
name: market-screener-watchlist
description: Build market screeners and watchlists across BIST, US equities, German equities, crypto, FX, fixed income, commodities, and sectors. Use when the user asks to find candidates, create a watchlist, filter by value, quality, growth, momentum, volume, catalysts, technical breakouts, risk, liquidity, factor exposure, or event calendars.
---

# Market Screener Watchlist

## Core Workflow

Use this skill to design and apply screening logic. Read `references/analysis-workflow.md` for screen design, filter templates, ranking logic, and watchlist output.

## Operating Rules

- Define universe, horizon, filters, ranking, and exclusions before listing names.
- Use `asset-master-data-manager` when a screen mixes tickers across BIST, US, Germany, crypto, ETFs, currencies, or chains.
- Use `market-data-source-verifier` for current screen inputs.
- Use `data-quality-reconciliation-engine` when screen inputs conflict or adjusted and unadjusted series may change ranks.
- Use `bist-sector-rotation-analyst`, `crypto-narrative-rotation-analyst`, `market-breadth-internals-analyst`, and `relative-strength-momentum-ranker` to prioritize leaders, sector/narrative rotation, participation quality, and watchlist tiers.
- Use `alternative-data-sentiment-analyst` when the screen includes narrative, adoption, social, app, developer, or product traction signals.
- Use `market-manipulation-anomaly-detector` before promoting a thin, low float, or abnormal volume name into the active list.
- For BIST/crypto spot watchlists, include optional filters for liquidity, custody/venue risk, ownership/on-chain flow, event risk, and crowding.
- Use `watchlist-alert-monitor` after screening when the user needs triggers, alert states, and review cadence.
- Use `daily-spot-market-briefing` when watchlist priorities depend on today's BIST/crypto regime and calendar.
- Use `signal-scoring-decision-engine` when the screen must become a decision-ready ranked shortlist.
- Separate inclusion logic from final interpretation.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Universe and objective
2. Filters and ranking
3. Candidate table
4. Watchlist tiers
5. Follow-up checks
