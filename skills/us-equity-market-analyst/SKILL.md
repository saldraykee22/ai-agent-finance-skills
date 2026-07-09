---
name: us-equity-market-analyst
description: Analyze US-listed equities, ETFs, sectors, earnings, SEC filings, guidance, valuation, options positioning, macro sensitivity, and NYSE/Nasdaq market context. Use when the user asks about US stocks, American companies, ADRs listed in the US, S&P 500/Nasdaq/Dow names, SEC 10-K/10-Q/8-K filings, earnings calls, or US equity trading/investment research.
---

# US Equity Market Analyst

## Core Workflow

Use this skill for US equity research. Start with the exact ticker, listing venue, company, timeframe, and requested depth. If the task depends on price, filings, earnings, guidance, analyst estimates, dividends, buybacks, index membership, options data, or macro releases, verify current sources before analyzing.

Read `references/analysis-workflow.md` for the detailed US equity workflow, source hierarchy, checklist, output format, and common failure modes.

## Operating Rules

- Separate verified facts, accounting data, estimates, interpretation, and unresolved uncertainties.
- Prefer primary sources: SEC EDGAR, company investor relations, exchange pages, official index providers, Federal Reserve, BLS, BEA, Treasury, and official court/regulatory filings.
- Check ticker changes, share classes, ADRs, spin-offs, splits, and adjusted historical data before comparing performance.
- Do not add generic boilerplate caveats. Keep the output analytical, source-grounded, and direct.
- Match the user's language. If the user writes in Turkish, produce Turkish output.

## Companion Skills

- Use `market-data-source-verifier` for price, filings, earnings, guidance, index membership, dividends, buybacks, and news.
- Use `financial-statement-analyst`, `valuation-modeling-analyst`, `sector-industry-analyst`, and `options-derivatives-analyst` for full US equity work.
- Use `corporate-actions-analyst` for splits, dividends, buybacks, spin-offs, mergers, and adjusted-history issues.

## Source Matrix

- Filings: SEC EDGAR and company investor relations.
- Market and indices: NYSE/Nasdaq pages, S&P Dow Jones, Nasdaq, Russell/FTSE where relevant.
- Macro: Federal Reserve, BLS, BEA, Treasury, Census.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

Use concise sections unless the user asks for a full report:

1. Executive view
2. Fresh data and filings check
3. Business and financial drivers
4. Valuation and peer context
5. Earnings, guidance, and estimates
6. Technical/options/flow context
7. Scenario map and key uncertainties
