---
name: crypto-onchain-flow-analyst
description: Analyze crypto on-chain flows, exchange inflows/outflows, whale wallets, stablecoin liquidity, bridge flows, treasury wallets, staking flows, unlock wallets, holder concentration, protocol revenue, TVL, and chain activity. Use when the user asks whether on-chain data supports a crypto spot trade, whether whales are accumulating or distributing, or whether exchange/stablecoin/protocol flows are changing.
---

# Crypto Onchain Flow Analyst

## Core Workflow

Use this skill for crypto-native flow evidence. Read `references/analysis-workflow.md` for wallet labeling, exchange flow, stablecoin, bridge, unlock, and protocol activity checks.

## Operating Rules

- Verify chain, contract address, wallet labels, and timestamps.
- Treat wallet labels as probabilistic unless from primary/proven sources.
- Separate exchange flow, treasury/team wallets, stablecoin liquidity, and protocol usage.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Asset and chain identity
2. On-chain flow snapshot
3. Holder and exchange behavior
4. Protocol/activity context
5. Spot trade implication

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
