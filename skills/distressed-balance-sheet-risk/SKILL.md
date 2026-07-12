---
name: distressed-balance-sheet-risk
description: Analyze financial distress, refinancing risk, covenant pressure, liquidity runway, debt maturity walls, going concern risk, credit downgrades, default risk, restructuring, dilution risk, and balance sheet fragility. Use when the user asks whether a company is financially stressed, whether debt can be refinanced, whether equity is at dilution/default risk, or whether a cheap stock is a value trap.
---

# Distressed Balance Sheet Risk

## Core Workflow

Use this skill when balance sheet survival may dominate upside. Read `references/analysis-workflow.md` for debt, liquidity, covenant, and value-trap checks.

## Operating Rules

- Separate solvency, liquidity, refinancing, covenant, and dilution risk.
- Use latest financial statements, debt notes, maturity tables, cash flow, and market yields where available.
- For BIST, pay attention to FX debt, short-term debt, working capital, rates, and inflation accounting distortions.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Balance sheet stress snapshot
2. Liquidity runway
3. Debt maturity and covenant risk
4. Dilution/default scenarios
5. Equity thesis implication

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
