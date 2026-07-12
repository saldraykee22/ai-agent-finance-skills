---
name: etf-fund-flow-analyst
description: Analyze ETF and fund flows, creations/redemptions, holdings, expense drag, index fund effects, passive flow, sector ETF pressure, crypto ETF flows, fund positioning, and index product impact on underlying assets. Use when the user asks whether ETF/fund flows affect a stock, sector, index, crypto asset, commodity, or portfolio.
---

# ETF Fund Flow Analyst

## Core Workflow

Use this skill to evaluate passive and fund-flow effects. Read `references/analysis-workflow.md` for ETF/fund source checks, flow interpretation, holdings impact, and output format.

## Operating Rules

- Separate fund flow, price return, benchmark change, and underlying asset fundamentals.
- Check whether flow is primary market creation/redemption, secondary trading, or estimated flow.
- For crypto spot, distinguish ETF flows from exchange spot volume and on-chain flows.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Product and exposure
2. Flow data
3. Underlying holdings impact
4. Cost/fee context
5. Thesis implication

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
