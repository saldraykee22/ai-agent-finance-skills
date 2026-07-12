---
name: security-wallet-operations-analyst
description: Review crypto wallet operations, exchange account security, withdrawal address controls, hardware wallet process, seed phrase handling, hot and cold wallet split, multisig, phishing risk, bridge risk, DeFi approval hygiene, stablecoin custody, and operational runbooks. Use when the user asks how to hold crypto, reduce wallet risk, split exchange and self-custody, or prepare secure spot crypto operations.
---

# Security Wallet Operations Analyst

## Core Rule

Treat crypto operations as a process system. The main risks are usually key loss, phishing, malicious approvals, wrong chain transfers, exchange lockups, and poor recovery planning.

## Workflow

1. Map assets, chains, venues, wallets, exchange accounts, stablecoins, and transfer habits.
2. Classify custody: exchange, hot wallet, hardware wallet, multisig, DeFi contract, bridge, or cold storage.
3. Review controls: 2FA, withdrawal whitelist, address book, test transfers, seed backup, device hygiene, approval revocation, phishing checks, and emergency contacts.
4. Define operating rules for transfers, storage split, trading balance, cold balance, and incident response.
5. Route venue exposure to `custody-counterparty-risk-analyst` and `broker-exchange-venue-selector`.

## Output

Return `Asset Custody Map`, `Control Checklist`, `Risk Findings`, `Operating Rules`, `Incident Plan`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for wallet operations checklist.

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
