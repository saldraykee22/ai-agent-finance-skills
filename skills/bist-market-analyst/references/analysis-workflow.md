# BIST Analysis Workflow

## Source hierarchy

Use current primary sources first when the question is time-sensitive:

- KAP: material disclosures, financial statements, corporate actions, shareholder structure, buybacks, capital increases.
- Borsa Istanbul: market data, indices, trading calendar, market rules, short selling lists, volatility-based measures, index constituent changes.
- Company investor relations: presentations, annual reports, earnings decks, guidance, operational KPIs.
- MKK and Takasbank when relevant: custody, settlement, investor statistics, securities lending and settlement context.
- TCMB, TUIK, Treasury, BRSA, EMRA, CMB/SPK: macro, rates, inflation, FX, sector-specific regulation.
- Reputable market data providers only after primary-source checks.

## Identification checklist

Before analysis, verify:

- Ticker, company legal name, market segment, share class, and index memberships.
- Reporting currency, consolidation scope, fiscal period, and whether the latest financials are standalone or consolidated.
- Corporate actions: dividend, bonus issue, rights issue, split, capital reduction, merger, tender offer, buyback.
- Liquidity: average daily volume, free float, free-float market cap, spread, recent unusual volume.
- Trading constraints: short-sale status, circuit breakers, gross settlement, order package measures, watchlist status.

## Research process

1. Define the question: ticker/index, horizon, catalyst type, and whether the user wants technical, fundamental, event-driven, or relative-value analysis.
2. Gather fresh facts: latest price, market cap, free float, volume, index status, last KAP items, latest financial period, and upcoming calendar items.
3. Build the company map: revenue segments, export/import exposure, FX sensitivity, working capital cycle, debt profile, ownership, related parties.
4. Analyze financials:
   - Revenue growth, gross margin, EBITDA/operating margin, net margin.
   - Net debt, cash, FX position, short-term debt, interest coverage.
   - Working capital, inventory, receivables, payables, operating cash flow, capex.
   - One-offs, revaluation gains, tax effects, inflation accounting effects when applicable.
5. Compare peers:
   - Use BIST sector peers first, then regional/global peers when business models match.
   - Normalize for leverage, liquidity, free float, growth, margin, and accounting differences.
   - Use EV/EBITDA, P/E, P/B, dividend yield, FCF yield, and sector-specific metrics where appropriate.
6. Evaluate macro and policy exposure:
   - TRY rates, inflation, FX, CDS, commodity prices, minimum wage, credit conditions.
   - Sector-specific regulation such as banking, energy tariffs, construction, aviation, telecom, retail, defense.
7. Review technical and flow:
   - Trend, support/resistance, volume confirmation, moving averages, relative strength vs XU100 and sector index.
   - Avoid treating technical levels as precise predictions; frame them as invalidation or confirmation zones.
8. Produce scenarios:
   - Base, upside, downside.
   - Triggers, invalidation points, data needed, and expected market reaction path.

## BIST-specific watchpoints

- Inflation accounting can distort historical comparability. State whether figures are inflation-adjusted.
- High nominal earnings may be driven by FX, inventory gains, revaluation, deferred tax, or monetary gains/losses.
- BIST small/mid caps can be dominated by liquidity, order-book depth, and regulatory measures.
- KAP disclosures often matter more than media summaries. Read the disclosure itself.
- Dividend yield must use the correct ex-dividend date and adjusted price context.
- Rights issues and bonus issues change share count and chart interpretation.
- Index changes can create passive-flow effects near effective dates.

## Output format

Prefer this structure:

```text
Executive view:
- ...

Verified data:
- Price/date/source:
- Latest KAP items:
- Latest financial period:

Fundamental drivers:
- ...

Valuation/peers:
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
- Show calculations when deriving ratios.
- Mark stale data clearly.
- Do not produce confident conclusions from a single source.
- Do not include generic boilerplate caveats unless the user explicitly asks.
