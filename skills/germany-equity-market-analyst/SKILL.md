---
name: germany-equity-market-analyst
description: Analyze German-listed equities, Xetra/Frankfurt trading, DAX/MDAX/SDAX/TecDAX names, issuer disclosures, annual reports, BaFin/regulatory context, eurozone macro sensitivity, valuation, dividends, and peer comparisons. Use when the user asks about German stocks, German indices, Xetra tickers, Frankfurt listings, German company filings, ADR/dual listings tied to Germany, or Germany-focused equity research.
---

# Germany Equity Market Analyst

## Core Workflow

Use this skill for German equity research. Start with the exact company, ticker, ISIN, exchange venue, timeframe, and requested depth. If the task depends on price, filings, earnings, dividend dates, index membership, German regulation, ECB/macro data, or corporate actions, verify current sources before analyzing.

Read `references/analysis-workflow.md` for the detailed Germany equity workflow, source hierarchy, checklist, output format, and common failure modes.

## Operating Rules

- Separate verified facts, accounting data, interpretation, and unresolved uncertainties.
- Prefer primary sources: company investor relations, Bundesanzeiger, EQS/news releases, BaFin, Deutsche Boerse/Xetra, official index pages, ECB, Destatis, Bundesbank, and regulator filings.
- Check ISIN, WKN, ticker venue, ADR ratio, share class, currency, and reporting standard before analysis.
- Do not add generic boilerplate caveats. Keep the output analytical, source-grounded, and direct.
- Match the user's language. If the user writes in Turkish, produce Turkish output.

## Companion Skills

- Use `market-data-source-verifier` for ISIN/WKN, Xetra/Frankfurt data, filings, EQS releases, dividends, and index membership.
- Use `financial-statement-analyst`, `valuation-modeling-analyst`, `sector-industry-analyst`, and `fixed-income-fx-analyst` for complete German equity work.
- Use `corporate-actions-analyst` for annual dividends, buybacks, capital actions, spin-offs, ADR ratios, and adjusted-history issues.

## Source Matrix

- Company disclosures: investor relations, EQS, Bundesanzeiger/Unternehmensregister.
- Market and indices: Deutsche Boerse, Xetra, DAX family index pages.
- Regulation and macro: BaFin, ECB, Bundesbank, Destatis, Eurostat.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

Use concise sections unless the user asks for a full report:

1. Executive view
2. Fresh data and disclosure check
3. Business and financial drivers
4. Valuation and European peer context
5. Macro, FX, and regulation exposure
6. Technical and flow context
7. Scenario map and key uncertainties
