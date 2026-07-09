---
name: model-assumption-validator
description: Validate assumptions in valuation models, scenario models, signal scores, factor screens, portfolio risk models, liquidity estimates, tokenomics models, macro scenarios, and stress tests. Use when the user asks whether model assumptions are reasonable, which assumptions drive the result, how to audit sensitivity, or how to make a finance model more robust.
---

# Model Assumption Validator

## Core Rule

Find the assumptions that control the decision. Validate ranges, sources, sensitivity, and internal consistency before trusting the model output.

## Workflow

1. Identify model purpose, decision horizon, inputs, outputs, and key formulas.
2. Classify assumptions as observed, estimated, scenario-based, derived, or judgmental.
3. Test source quality, timestamp, unit consistency, currency, adjustment basis, and historical reasonableness.
4. Run sensitivity logic: which assumptions move the decision from proceed to wait or reject.
5. Check for hidden double counting, stale base rates, survivorship bias, hindsight bias, and missing downside cases.
6. Route to `valuation-modeling-analyst`, `quant-factor-analyst`, `scenario-stress-tester`, or `signal-scoring-decision-engine` as needed.

## Output

Return `Model Purpose`, `Critical Assumptions`, `Validation Evidence`, `Sensitivity Drivers`, `Weak Assumptions`, `Required Changes`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for assumption audit templates.
