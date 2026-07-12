---
name: financial-statement-analyst
description: Perform deep financial statement analysis, earnings quality review, accounting normalization, ratio analysis, cash flow analysis, segment analysis, balance sheet risk review, and red-flag detection. Use when the user asks to analyze 10-K/10-Q reports, annual reports, quarterly results, income statements, balance sheets, cash flows, margins, debt, working capital, accounting quality, or company financial health.
---

# Financial Statement Analyst

## Core Workflow

Use this skill for bottom-up accounting and financial quality analysis. If the user references current filings, latest earnings, restatements, or company-specific figures, verify the latest report and period before analyzing.

Read `references/analysis-workflow.md` for the full statement analysis checklist, normalization rules, red flags, sector adjustments, and output format.

## Operating Rules

- Separate reported figures, adjusted figures, calculations, interpretation, and unresolved data gaps.
- Always state period, currency, accounting basis, and whether figures are consolidated.
- Reconcile profitability with cash generation before concluding quality.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.
- Make every decision-changing ratio reproducible from named statement lines, units, currency, period, and formula. For BIST, identify inflation-accounting and consolidation basis before time-series comparison.

## Companion Skills

- Use `market-data-source-verifier` for latest filing, reporting period, currency, restatement, and company disclosure checks.
- Use `sector-industry-analyst` for sector-specific KPIs and `valuation-modeling-analyst` when normalized figures feed valuation.
- Use `financial-report-writer` when converting findings into a research note.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Financial snapshot
2. Revenue and margin bridge
3. Cash flow and working capital
4. Balance sheet and leverage
5. Earnings quality
6. Red flags and follow-up questions
