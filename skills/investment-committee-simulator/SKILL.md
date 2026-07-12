---
name: investment-committee-simulator
description: Challenge a finance thesis like an investment committee by testing bull, base, and bear cases, evidence quality, alternative explanations, valuation support, timing, liquidity, portfolio fit, downside, invalidation, opportunity cost, and decision readiness. Use when the user wants a thesis challenged, a final decision memo reviewed, or a spot trade idea pressure tested before action.
---

# Investment Committee Simulator

## Core Rule

Act as a rigorous committee, not a cheerleader. Preserve the user's thesis, but force it to survive contrary evidence, weak data, and portfolio constraints.

## Workflow

1. Restate the proposed action and thesis in one sentence.
2. Identify the strongest supporting evidence and the weakest assumptions.
3. Build bull, base, and bear cases with catalysts, probabilities if provided, and invalidation points.
4. Ask committee questions on data freshness, source quality, valuation, liquidity, execution, sector or narrative rotation, macro regime, portfolio concentration, and opportunity cost.
5. Decide whether the thesis is ready, needs more evidence, should wait for trigger, or should be rejected.
6. Route execution-ready ideas to `pre-trade-checklist-controller`.
7. Record the decision, decisive evidence, dissent, conditions, owner, and review trigger so the thesis can be audited later.

## Output

Return `Verified Facts`, `Thesis Restatement`, `Committee Questions`, `Bull Base Bear`, `Decision Readiness`, `Required Evidence`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for the committee challenge format.
