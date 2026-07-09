---
name: broker-exchange-venue-selector
description: Compare brokers, crypto exchanges, trading venues, custody venues, order routing, liquidity, fees, spreads, settlement, withdrawal rules, counterparty risk, API access, reporting exports, and operational fit for BIST, crypto spot, US, Germany, ETFs, FX, and commodities. Use when the user asks where to trade, which exchange or broker is better, how to split venue exposure, or how venue choice affects execution.
---

# Broker Exchange Venue Selector

## Core Rule

Venue choice is a risk decision as much as a cost decision. Compare liquidity, custody, reliability, reporting, withdrawal, and counterparty exposure together.

## Workflow

1. Define instruments, order size, holding period, custody preference, and reporting needs.
2. Compare fees, spreads, depth, trading hours, order types, settlement, deposit/withdrawal rails, outages, and export quality.
3. Assess counterparty and custody risk with `custody-counterparty-risk-analyst` and crypto security setup with `security-wallet-operations-analyst`.
4. Check execution quality implications with `liquidity-execution-analyst` and `execution-quality-tca-analyst`.
5. Produce a venue policy: primary venue, backup venue, max exposure, transfer cadence, and review triggers.

## Output

Return `Venue Requirements`, `Comparison Table`, `Execution Impact`, `Custody and Counterparty Risk`, `Reporting Fit`, `Venue Policy`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for venue comparison fields.
