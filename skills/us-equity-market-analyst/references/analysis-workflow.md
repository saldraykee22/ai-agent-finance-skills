# US Equity Analysis Workflow

## Source hierarchy

Use current primary sources first when the question is time-sensitive:

- SEC EDGAR: 10-K, 10-Q, 8-K, S-1, DEF 14A, Form 4, 13D/13G, 13F where relevant.
- Company investor relations: earnings releases, decks, transcripts, guidance, segment details.
- Exchange and issuer pages: listing venue, share class, market data basics.
- Index providers: S&P Dow Jones, Nasdaq, Russell/FTSE for membership and rebalance events.
- Official macro sources: Federal Reserve, BLS, BEA, Treasury, Census, EIA.
- Options/market data providers: OCC/Cboe/exchange sources where possible; reputable aggregators for IV, skew, OI, gamma context.

## Identification checklist

Before analysis, verify:

- Ticker, company legal name, exchange, CIK, share class, ADR status, currency.
- Fiscal year-end, latest reported quarter, reporting segments, accounting standard.
- Corporate actions: split, dividend, buyback authorization, spin-off, merger, secondary offering.
- Market cap, enterprise value, float, average daily volume, short interest if relevant.
- Upcoming events: earnings date, investor day, product launch, regulatory decision, ex-dividend date.

## Research process

1. Define the request: ticker/company, timeframe, trade/investment horizon, and whether the user wants fundamentals, valuation, event analysis, technicals, options, or peer comparison.
2. Gather fresh facts:
   - Price, market cap, EV, volume, 52-week range, index membership.
   - Latest SEC filing and latest earnings release.
   - Recent 8-Ks, guidance updates, major news, insider transactions when material.
3. Build the business map:
   - Revenue segments, geographies, customer concentration, unit economics, moat, pricing power.
   - Cyclicality, rate sensitivity, FX exposure, commodity exposure, regulatory exposure.
4. Analyze financials:
   - Revenue growth, gross margin, operating margin, EBITDA where appropriate, EPS.
   - Cash, debt, net debt, interest expense, maturities, FCF, capex, working capital.
   - SBC, dilution, buybacks, restructuring, impairment, tax effects, one-offs.
5. Earnings and guidance:
   - Compare actuals vs prior guidance and consensus.
   - Identify drivers of beat/miss: volume, price, mix, margin, FX, tax, buybacks.
   - Track management language changes across calls.
6. Valuation:
   - Use sector-appropriate multiples: P/E, EV/EBITDA, EV/Sales, P/B, FCF yield, PEG, ARR multiples, NAV.
   - Compare to direct peers, own history, growth/margin profile, balance sheet, and quality.
   - For banks, insurers, REITs, biotech, energy, and software, use sector-specific metrics.
7. Technical/options/flow:
   - Trend, relative strength vs SPY/QQQ/sector ETF, moving averages, support/resistance.
   - Options: IV rank, skew, put/call, OI concentration, earnings-implied move, gamma only when sourced credibly.
8. Produce scenarios:
   - Base, upside, downside.
   - Catalysts, invalidation points, next data to monitor.

## US-specific watchpoints

- Non-GAAP metrics vary widely. Reconcile to GAAP when conclusions depend on adjustments.
- SBC can materially affect dilution and FCF interpretation.
- Buybacks can drive EPS even when net income is flat.
- Mega-cap index weight can cause ETF/passive flow effects.
- ADRs can carry currency, local-market, and depositary-ratio issues.
- Guidance may be annual, quarterly, or metric-specific; do not compare unlike metrics.
- Options data is perishable. Timestamp it.

## Output format

Prefer this structure:

```text
Executive view:
- ...

Verified data:
- Price/date/source:
- Latest filing:
- Latest earnings:

Fundamental drivers:
- ...

Valuation/peers:
- ...

Earnings/guidance:
- ...

Technical/options/flow:
- ...

Scenarios:
- Base:
- Upside:
- Downside:

Uncertainties:
- ...
```

## Quality bar

- Cite filing names, dates, and periods.
- Show calculations when deriving ratios.
- Distinguish trailing, forward, consensus, and company-guided numbers.
- Mark stale data clearly.
- Do not include generic boilerplate caveats unless the user explicitly asks.
