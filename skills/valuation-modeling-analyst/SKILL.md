---
name: valuation-modeling-analyst
description: Build valuation analyses using DCF, comparable multiples, precedent transactions, sum-of-the-parts, NAV, dividend discount, residual income, scenario analysis, sensitivity tables, and reverse DCF. Use when the user asks what a company or asset is worth, valuation range, fair value, target price mechanics, assumptions, multiples, WACC, terminal value, peer comparison, or upside/downside scenarios.
---

# Valuation Modeling Analyst

## Core Workflow

Use this skill for valuation and scenario modeling. If the task depends on current price, market cap, debt, cash, shares, rates, estimates, or latest financials, verify current inputs before modeling.

Read `references/analysis-workflow.md` for model selection, input checklist, WACC logic, scenario rules, sector-specific valuation methods, and output format.

## Operating Rules

- Separate input facts, assumptions, formulas, valuation output, and sensitivity.
- Prefer valuation ranges over false precision.
- Tie every major assumption to history, peers, guidance, or explicit scenario logic.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.
- Do not apply equity DCF mechanically to crypto tokens. First prove that cash flows or economic value accrue to token holders; otherwise use supply, adoption, protocol economics, comparable networks, and scenario analysis.

## Companion Skills

- Use `market-data-source-verifier` for price, shares, net debt, rates, estimates, and latest financial base.
- Use `financial-statement-analyst` for normalized inputs and `sector-industry-analyst` for sector-native metrics.
- Use `model-assumption-validator` when growth, margin, WACC, terminal value, multiple, SOTP discount, token supply, or scenario assumptions drive the conclusion.
- Use the relevant market skill for listing/market context and `portfolio-risk-manager` when valuation informs sizing.

## Valuation Depth Rules

- Include reverse DCF when the user asks what the current price implies or when market price appears stretched.
- Use SOTP when segments have materially different economics, peer groups, or capital intensity.
- Include sensitivity tables or concise sensitivity ranges for WACC, terminal value, growth, margin, and key sector drivers.
- Choose sector-specific methods before generic multiples when the sector requires them.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Valuation method choice
2. Input base and assumptions
3. Valuation range
4. Sensitivities
5. Reverse-implied expectations
6. What would change the valuation
