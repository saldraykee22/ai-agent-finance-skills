---
name: trade-journal-reviewer
description: Review trade journals, trade plans, entries, exits, R-multiples, win rate, expectancy, drawdowns, process adherence, recurring mistakes, emotional patterns, setup quality, and post-trade lessons. Use when the user asks to analyze trades, review performance, diagnose trading mistakes, improve discipline, or summarize a trading journal.
---

# Trade Journal Reviewer

## Core Workflow

Use this skill for post-trade and process analysis. Read `references/analysis-workflow.md` for journal schema, metrics, pattern review, and output format.

## Operating Rules

- Separate outcome quality from decision/process quality.
- Use R-multiple and thesis adherence when entry/stop/exit data exists.
- Identify repeatable patterns, not one-off blame.
- For BIST and crypto spot trades, review liquidity, slippage, position lifecycle stage, and whether the trade followed the personal investment policy.
- Use `execution-quality-tca-analyst` when fill price, spread, slippage, VWAP/TWAP, fees, FX conversion, or venue quality should be measured separately from thesis quality.
- Feed recurring execution mistakes back into `pre-trade-checklist-controller` and `spot-trading-playbook`.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Trade sample summary
2. Metrics
3. Best patterns
4. Mistake patterns
5. Rule changes
6. Next review checklist

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
