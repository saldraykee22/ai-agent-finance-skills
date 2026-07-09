# Financial Statement Analysis Workflow

## Source hierarchy

- Primary filings: annual reports, quarterly reports, SEC filings, exchange filings, KAP/EQS/RNS releases.
- Company investor relations: earnings releases, presentations, transcripts, segment tables.
- Auditor reports and notes to financial statements.
- Regulator filings for restatements, enforcement, related-party transactions, and ownership.

## Research process

1. Identify company, period, currency, accounting standard, consolidation scope, fiscal calendar, and comparison period.
2. Build the reported snapshot:
   - Revenue, gross profit, EBITDA/operating profit, net income, EPS.
   - Cash, debt, net debt, equity, working capital, operating cash flow, capex, free cash flow.
3. Analyze income statement:
   - Volume, price, mix, FX, acquisitions, disposals, one-offs.
   - Gross margin, operating leverage, SG&A, R&D, depreciation, finance expense, tax.
4. Analyze balance sheet:
   - Cash quality, debt maturity, covenants, lease liabilities, pension obligations.
   - Receivables, inventory, payables, provisions, goodwill, intangibles, deferred tax.
5. Analyze cash flow:
   - Operating cash conversion, working capital swings, capex intensity, capitalized costs.
   - FCF after lease payments and recurring capex when relevant.
6. Normalize earnings:
   - Remove one-offs only when truly non-recurring.
   - Track restructuring, impairments, FX gains/losses, revaluation, litigation, tax benefits.
   - Reconcile non-GAAP to GAAP/IFRS.
7. Review earnings quality:
   - Revenue recognition, aggressive capitalization, receivable growth, inventory build, margin expansion without cash.
   - Related-party transactions, auditor changes, internal control issues, restatements.
8. Produce findings with calculations and open data gaps.

## Sector adjustments

- Banks: net interest margin, loan growth, deposits, CET1, NPLs, provisions, duration, liquidity coverage.
- Insurers: combined ratio, solvency, investment portfolio, reserve adequacy.
- REITs: FFO/AFFO, occupancy, lease maturity, cap rates, NAV, debt maturity.
- Software: ARR, NRR, gross retention, CAC, SBC, deferred revenue, RPO.
- Industrials: order intake, backlog, book-to-bill, working capital, capex cycle.
- Retail: same-store sales, inventory turns, shrink, lease liabilities, gross margin.
- Energy/mining: production, reserves, lifting cost, realized price, hedges, sustaining capex.

## Red flags

- Net income rising while operating cash flow deteriorates.
- Receivables or inventory growing faster than revenue without explanation.
- Frequent adjusted earnings exclusions.
- Debt maturity wall or covenant pressure.
- Auditor resignation, material weakness, restatement, delayed filing.
- Large related-party transactions or opaque segment transfers.
- Excessive SBC dilution or buybacks that only offset dilution.

## Output format

```text
Financial snapshot:
- Period/currency/source:
- Key figures:

Profitability:
- ...

Cash flow:
- ...

Balance sheet:
- ...

Earnings quality:
- ...

Red flags:
- ...

Questions/data gaps:
- ...
```
