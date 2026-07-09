---
name: corporate-actions-analyst
description: Analyze corporate actions and token supply events including dividends, splits, bonus issues, rights issues, buybacks, mergers, spin-offs, tender offers, delistings, index changes, token unlocks, emissions, burns, airdrops, redenominations, and exchange listing events. Use when the user asks how a corporate action affects price, share count, valuation, charts, liquidity, tax/cash flow, or historical comparability.
---

# Corporate Actions Analyst

## Core Workflow

Use this skill for equity corporate actions and crypto supply events. Read `references/analysis-workflow.md` for action-specific mechanics, adjusted data checks, and impact analysis.

## Operating Rules

- Verify official date, record date, ex-date, payment/effective date, ratio, and eligibility.
- Recalculate share count, per-share metrics, chart adjustments, and cash impact when relevant.
- Separate mechanical adjustment from economic impact.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Action summary
2. Key dates and ratios
3. Mechanical impact
4. Economic/flow impact
5. Data adjustment notes
