---
name: portfolio-recordkeeping-ledger
description: Define and audit portfolio recordkeeping, transaction ledgers, holdings tables, cash movements, cost basis fields, dividends, corporate actions, crypto transfers, exchange fees, FX conversions, realized and unrealized P&L, and reconciliation rules for spot portfolios. Use when the user wants clean portfolio records, spreadsheet schemas, broker or exchange import mapping, or performance-ready ledgers.
---

# Portfolio Recordkeeping Ledger

## Core Rule

Make the ledger reconstructable. Every position, P&L number, cash balance, fee, dividend, transfer, and FX conversion should trace back to a transaction or adjustment event.

## Workflow

1. Define ledger scope: BIST, crypto spot, US, Germany, cash, FX, fees, dividends, and transfers.
2. Create tables for trades, cash movements, holdings, corporate actions, token events, fees, FX rates, and reconciliation.
3. Map broker, exchange, wallet, and manual exports into canonical fields.
4. Reconcile holdings against portfolio accounting and execution records.
5. Route performance calculations to `portfolio-accounting-performance` and execution details to `execution-quality-tca-analyst`.

## Output

Return `Ledger Scope`, `Tables`, `Required Fields`, `Import Mapping`, `Reconciliation Rules`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for ledger schemas.
