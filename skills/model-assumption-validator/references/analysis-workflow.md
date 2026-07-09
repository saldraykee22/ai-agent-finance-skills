# Model Assumption Validation Workflow

## Assumption Audit Table

| Assumption | Value | Source | Type | Sensitivity | Confidence | Issue | Fix |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Common Failure Modes

- Growth and margin assumptions inconsistent with industry cycle.
- Discount rate, FX, inflation, or terminal value drives most of valuation.
- Token supply model ignores unlocks, emissions, staking dilution, or bridge supply.
- Liquidity model assumes normal volume during stress.
- Signal score double counts momentum through technical and relative strength fields.
- Portfolio risk model ignores correlation rising during drawdowns.

## Decision Standard

If changing one weak assumption flips the decision, mark the model as decision-sensitive and require scenario presentation.
