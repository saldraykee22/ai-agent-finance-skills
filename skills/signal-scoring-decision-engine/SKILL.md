---
name: signal-scoring-decision-engine
description: Convert multi-skill finance analysis into a structured decision score across fundamentals, valuation, technicals, momentum, liquidity, catalysts, macro regime, portfolio fit, risk, execution, and data quality. Use when a user wants a ranked decision, spot candidate comparison, watchlist prioritization, trade readiness score, or a concise go wait avoid style decision framework.
---

# Signal Scoring Decision Engine

## Core Rule

Score evidence quality and decision readiness, not just bullish or bearish direction. A strong thesis with weak data should not receive a clean action score.

## Workflow

1. Define the decision: new entry, add, hold, trim, exit, watchlist, or avoid.
2. Pull inputs from relevant specialist skills and separate facts from interpretation.
3. Produce two separate scores: `Thesis Attractiveness` and `Execution Readiness`.
4. Score each defined dimension from -2 to +2 with cited evidence; use `N/A`, not zero, when evidence is missing.
5. Select the BIST/equity or crypto spot weights from `references/analysis-workflow.md`, renormalize only genuinely inapplicable dimensions, and never renormalize missing evidence.
6. Apply hard gates before mapping scores to `Ready`, `Watch`, `Wait for Trigger`, `Reduce`, or `Reject`.
7. Require `pre-trade-checklist-controller` before any execution-ready conclusion.

## Use Together

Use with `finance-agent-orchestrator`, `bist-crypto-spot-command-center`, `relative-strength-momentum-ranker`, `portfolio-risk-manager`, `valuation-modeling-analyst`, and `investment-committee-simulator`.

## Output

Return `Verified Facts`, `Scorecard`, `Weighted Decision`, `Scenario Sensitivity`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` to build a full scoring matrix.
