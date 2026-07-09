---
name: financial-news-event-analyst
description: Analyze market-moving news, filings, earnings releases, guidance changes, mergers, regulation, litigation, sanctions, central bank events, macro releases, product launches, exchange notices, and catalyst timelines. Use when the user asks what happened, why an asset moved, whether news is material, how an event affects valuation or trading, or what to watch next after a financial event.
---

# Financial News Event Analyst

## Core Workflow

Use this skill for event-driven financial analysis. Always verify current event facts with primary or high-quality sources before explaining impact.

Read `references/analysis-workflow.md` for event classification, source hierarchy, impact mapping, timeline reconstruction, and output format.

## Operating Rules

- Separate confirmed facts, market reaction, likely mechanism, and unknowns.
- Prefer the original filing, announcement, transcript, regulator release, or exchange notice over summaries.
- Timestamp fast-moving claims.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Companion Skills

- Use `market-data-source-verifier` for event source, timestamp, confirmation status, and market reaction data.
- Use `corporate-actions-analyst` for dividends, splits, mergers, buybacks, unlocks, and index changes.
- Use relevant market, sector, valuation, technical, and portfolio skills when the event changes fundamentals, flow, or risk.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. What happened
2. Source and timestamp
3. Why it matters
4. Asset-specific impact
5. Second-order effects
6. Next catalysts and uncertainty
