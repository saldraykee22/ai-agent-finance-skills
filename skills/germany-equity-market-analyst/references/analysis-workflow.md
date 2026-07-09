# Germany Equity Analysis Workflow

## Source hierarchy

Use current primary sources first when the question is time-sensitive:

- Company investor relations: annual reports, half-year reports, quarterly statements, presentations, guidance, dividend proposal.
- EQS, company ad hoc releases, and voting rights notifications.
- Bundesanzeiger/Unternehmensregister when filings or annual accounts matter.
- Deutsche Boerse/Xetra: venue, market data, index membership, trading calendar.
- BaFin: regulatory notices, short positions, investigations when relevant.
- Official macro sources: ECB, Bundesbank, Destatis, Eurostat, German Federal Ministry sources.
- Reputable market data providers only after primary-source checks.

## Identification checklist

Before analysis, verify:

- Company legal name, ticker, ISIN, WKN, listing venue, currency, and share class.
- Index membership: DAX, MDAX, SDAX, TecDAX, sector indices, Euro Stoxx when relevant.
- Reporting standard, fiscal year, latest reporting period, segment definitions.
- Corporate actions: dividend proposal, ex-dividend date, capital increase, buyback, spin-off, merger.
- ADR/dual listing details if the user asks via a US ticker.
- Liquidity: Xetra volume, Frankfurt volume, free float, spread, short interest/short positions when available.

## Research process

1. Define the request: company/ticker/ISIN, venue, timeframe, and whether the user wants fundamentals, valuation, event analysis, technicals, dividend, or peer comparison.
2. Gather fresh facts:
   - Price, market cap, EV, volume, index membership.
   - Latest report, latest ad hoc/EQS release, guidance, dividend proposal.
   - Recent BaFin/regulatory items if material.
3. Build the business map:
   - Segments, geographies, customer mix, export exposure, supply-chain exposure.
   - Energy sensitivity, wage/labor exposure, China/US exposure, EUR sensitivity.
   - Industrial cycle, auto cycle, chemical cycle, banking/insurance/real-estate context when applicable.
4. Analyze financials:
   - Revenue, order intake/backlog when relevant, margins, EPS, FCF, capex.
   - Net debt, pension obligations, lease liabilities, maturities, interest cost.
   - Working capital and inventory cycle for industrials.
   - IFRS adjustments, restructuring costs, impairments, discontinued operations.
5. Valuation:
   - Use sector-appropriate metrics: P/E, EV/EBITDA, EV/Sales, P/B, dividend yield, FCF yield, NAV, Solvency II metrics, CET1 for banks.
   - Compare to German and European peers first, then global peers where business mix matches.
   - Normalize for cyclicality, balance sheet, pension obligations, and family/state ownership where relevant.
6. Macro and policy:
   - ECB rates, Bund yields, EUR/USD, energy prices, German PMI, industrial production, auto registrations, China demand.
   - EU regulation, German fiscal policy, energy transition, defense spending, banking/real-estate stress when relevant.
7. Technical and flow:
   - Trend, relative strength vs DAX/MDAX/sector, moving averages, support/resistance.
   - Index review dates and passive-flow effects for DAX family changes.
8. Produce scenarios:
   - Base, upside, downside.
   - Catalysts, invalidation points, next data to monitor.

## Germany-specific watchpoints

- Tickers vary by venue; ISIN is the clean identifier.
- Xetra is usually the primary electronic venue for German blue chips.
- Dividends are often annual and tied to AGM approval; verify ex-dividend dates.
- German companies may report quarterly statements with less detail than annual/half-year reports.
- Family, foundation, or state ownership can affect float, governance, and strategic decisions.
- Pension obligations and energy costs can materially affect industrial valuation.
- ADR prices require ratio and FX conversion checks.

## Output format

Prefer this structure:

```text
Executive view:
- ...

Verified data:
- Price/date/source:
- ISIN/venue:
- Latest disclosure/report:

Fundamental drivers:
- ...

Valuation/peers:
- ...

Macro/regulation:
- ...

Technical/flow:
- ...

Scenarios:
- Base:
- Upside:
- Downside:

Uncertainties:
- ...
```

## Quality bar

- Include source names and dates for fresh facts.
- Cite report period and accounting basis.
- Show calculations when deriving ratios.
- Mark stale data clearly.
- Do not include generic boilerplate caveats unless the user explicitly asks.
