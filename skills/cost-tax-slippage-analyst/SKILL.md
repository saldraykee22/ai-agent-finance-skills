---
name: cost-tax-slippage-analyst
description: Estimate the net impact of trading costs, spreads, slippage, exchange fees, broker commissions, FX conversion, withdrawal/deposit costs, funding costs, ETF/fund expenses, and tax drag without giving jurisdiction-specific tax advice. Use when the user asks about net return, spot trade cost, BIST or crypto execution drag, breakeven price, after-cost performance, or comparing venues and instruments.
---

# Cost Tax Slippage Analyst

## Core Workflow

Use this skill to convert gross ideas into net outcomes. Read `references/analysis-workflow.md` for cost stack, breakeven, venue comparison, and output format.

## Operating Rules

- Separate explicit costs, implicit costs, FX costs, tax assumptions, and unknowns.
- Do not invent tax rates; use user-provided rates or state placeholders.
- For spot trading, focus on commission, spread, slippage, transfer/withdrawal, FX conversion, and breakeven.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Trade or portfolio cost basis
2. Cost stack
3. Breakeven move
4. Net return impact
5. Data needed to refine
