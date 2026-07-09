---
name: portfolio-accounting-performance
description: Analyze portfolio accounting and performance for spot portfolios, including realized and unrealized P&L, cash flows, dividends, fees, FX impact, deposits/withdrawals, benchmark comparison, contribution, and performance attribution. Use when the user asks how a portfolio performed, why returns changed, how much was made or lost, or how BIST/crypto spot holdings contributed to total performance.
---

# Portfolio Accounting Performance

## Core Workflow

Use this skill for portfolio return truth. Read `references/analysis-workflow.md` for P&L, cash flow, attribution, benchmark, and reporting methods.

## Operating Rules

- Separate market return, deposits/withdrawals, fees, taxes, FX, and realized trading decisions.
- For spot portfolios, track quantity, average cost, cash, realized P&L, unrealized P&L, and total equity.
- Mark missing transaction data clearly; do not infer fills or costs without saying so.
- Use `portfolio-recordkeeping-ledger` when transactions, cash movements, dividends, crypto transfers, fees, FX conversion, or holdings need to be structured before performance analysis.
- Use `trade-blotter-operations-controller` when planned orders, working orders, partial fills, or post-trade routing need operational reconciliation.
- Use `portfolio-dashboard-designer` when performance outputs should feed a recurring monitoring dashboard.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Portfolio accounting basis
2. P&L summary
3. Contribution by holding
4. Cash flow and FX effects
5. Benchmark comparison
6. Data gaps
