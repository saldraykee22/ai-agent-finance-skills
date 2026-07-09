---
name: earnings-estimate-revision-tracker
description: Track earnings estimate revisions, consensus changes, guidance updates, analyst expectation drift, revenue and margin revisions, EPS or EBITDA estimate changes, pre-earnings setup, post-earnings reset, and surprise risk for BIST, US, German equities, sectors, and peers. Use when the user asks what the market expects, whether expectations are rising or falling, or how revisions affect valuation and catalysts.
---

# Earnings Estimate Revision Tracker

## Core Rule

Price often reacts to expectation change, not just reported results. Track whether the bar is rising, falling, crowded, or stale.

## Workflow

1. Define company, peer group, reporting date, and key metrics.
2. Gather current expectations, recent revisions, company guidance, management tone, and sector read-throughs.
3. Compare estimates to history, peer trends, margins, FX, commodity inputs, and macro drivers.
4. Classify setup: low bar, high bar, mixed revisions, stale consensus, crowded optimism, or negative reset.
5. Route to `valuation-modeling-analyst`, `earnings-call-transcript-analyst`, `financial-statement-analyst`, and `financial-news-event-analyst`.

## Output

Return `Verified Facts`, `Consensus Map`, `Revision Direction`, `Expectation Risk`, `Valuation Impact`, `Catalyst Setup`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for revision analysis fields.
