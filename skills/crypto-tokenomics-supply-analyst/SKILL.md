---
name: crypto-tokenomics-supply-analyst
description: Analyze crypto tokenomics, circulating supply, FDV, unlocks, vesting, emissions, burns, staking rewards, treasury allocations, team/investor cliffs, float, dilution, and supply-side sell pressure. Use when the user asks whether tokenomics are good, whether an unlock matters, why FDV is high, how emissions affect spot holders, or whether supply risk weakens a crypto trade.
---

# Crypto Tokenomics Supply Analyst

## Core Workflow

Use this skill to evaluate crypto supply risk before spot decisions. Read `references/analysis-workflow.md` for tokenomics checks, unlock severity, FDV interpretation, and output format.

## Operating Rules

- Verify chain, contract, supply figures, unlock schedule, and source timestamp.
- Separate circulating supply, liquid float, total supply, max supply, and FDV.
- Treat unlocks as risk only after considering recipient, liquidity, market depth, and vesting history.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Token identity
2. Supply and FDV
3. Unlock/emission schedule
4. Sell-pressure risk
5. Spot thesis impact

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
