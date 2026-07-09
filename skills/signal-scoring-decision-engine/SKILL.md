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
3. Score each dimension from -2 to +2: fundamentals, valuation, trend, relative strength, catalysts, liquidity, macro regime, sector or narrative rotation, portfolio fit, execution, and data quality.
4. Weight dimensions by asset type and time horizon. For spot trading, give liquidity, trend, invalidation, and position impact meaningful weight.
5. Convert scores into `Ready`, `Watch`, `Wait for Trigger`, `Reduce`, or `Reject`.
6. Require `pre-trade-checklist-controller` before any execution-ready conclusion.

## Use Together

Use with `finance-agent-orchestrator`, `bist-crypto-spot-command-center`, `relative-strength-momentum-ranker`, `portfolio-risk-manager`, `valuation-modeling-analyst`, and `investment-committee-simulator`.

## Output

Return `Verified Facts`, `Scorecard`, `Weighted Decision`, `Scenario Sensitivity`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` to build a full scoring matrix.
