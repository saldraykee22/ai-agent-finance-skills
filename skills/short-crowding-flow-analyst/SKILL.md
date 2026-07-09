---
name: short-crowding-flow-analyst
description: Analyze short interest, days to cover, borrow availability, borrow cost, securities lending, short-sale volume, crowded longs, crowded shorts, squeeze risk, forced covering, margin leverage, and positioning fragility. Use when the user asks whether a stock or crypto asset is crowded, vulnerable to squeeze, at risk of forced selling, or driven by positioning rather than fundamentals.
---

# Short Crowding Flow Analyst

## Core Workflow

Use this skill to separate thesis from positioning pressure. Read `references/analysis-workflow.md` for short/crowding indicators, equity and crypto differences, and output format.

## Operating Rules

- Timestamp short, borrow, margin, funding, and OI data.
- Separate short squeeze risk, crowded long risk, and ordinary negative sentiment.
- For crypto, use funding, open interest, liquidation clusters, exchange concentration, and spot/perp divergence.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Positioning snapshot
2. Short/crowding indicators
3. Squeeze or unwind risk
4. Spot decision implication
5. Data limitations
