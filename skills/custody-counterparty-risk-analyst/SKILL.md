---
name: custody-counterparty-risk-analyst
description: Analyze custody, exchange, broker, settlement, counterparty, wallet, bridge, stablecoin, withdrawal, deposit, and operational risks for spot portfolios. Use when the user asks where to hold assets, whether exchange or broker risk matters, whether crypto withdrawals/deposits are safe, or how custody/settlement risk affects BIST, crypto, and international spot holdings.
---

# Custody Counterparty Risk Analyst

## Core Workflow

Use this skill to assess risks that are not visible in price charts. Read `references/analysis-workflow.md` for custody, broker, exchange, wallet, stablecoin, bridge, and settlement checks.

## Operating Rules

- Separate asset risk from venue/counterparty risk.
- For crypto, check exchange concentration, withdrawal status, proof/reserve signals where available, stablecoin and bridge exposure.
- Use `security-wallet-operations-analyst` when wallet controls, seed phrase process, withdrawal whitelist, phishing, chain transfer, DeFi approval, or incident response matters.
- Use `broker-exchange-venue-selector` when choosing between venues or setting max exposure by broker or exchange.
- For BIST and equities, check broker/settlement/custody mechanics and corporate action handling.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Asset and venue exposure
2. Custody/counterparty risks
3. Operational constraints
4. Mitigation options
5. Monitoring triggers

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
