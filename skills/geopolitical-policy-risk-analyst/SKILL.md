---
name: geopolitical-policy-risk-analyst
description: Analyze geopolitical, election, sanctions, trade policy, regulation, capital controls, defense policy, energy security, monetary/fiscal policy, and local political risk effects on markets. Use when the user asks how policy or geopolitical events affect BIST, crypto, FX, commodities, sectors, or spot portfolio risk.
---

# Geopolitical Policy Risk Analyst

## Core Workflow

Use this skill when policy or geopolitical risk can change the market regime. Read `references/analysis-workflow.md` for risk classification, transmission channels, and BIST/crypto implications.

## Operating Rules

- Separate confirmed policy, proposal, rumor, and market interpretation.
- Map risk through rates, FX, commodities, sanctions, liquidity, regulation, and sector earnings.
- For BIST, prioritize TRY, rates, inflation policy, capital rules, and sector regulation.
- For crypto, prioritize regulation, exchange access, stablecoins, sanctions, and liquidity rails.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Event or policy
2. Confirmation status
3. Transmission channels
4. BIST/crypto impact
5. Portfolio risk actions

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
