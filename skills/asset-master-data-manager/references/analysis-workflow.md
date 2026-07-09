# Asset Master Data Workflow

## Identity Fields

- Equity: local ticker, exchange, MIC, ISIN, FIGI if available, issuer name, country, reporting currency, sector, industry, index memberships, listing status.
- US equity: ticker, exchange, CIK, SEC filer name, share class, ADR relationship if relevant.
- Germany equity: Xetra or Frankfurt ticker, ISIN, WKN when available, issuer, segment, reporting currency.
- BIST equity: BIST ticker, KAP issuer name, ISIN, market segment, index membership, trading method, price limit relevance.
- Crypto: token symbol, full name, contract address, chain, decimals, native or wrapped status, canonical bridge, CEX tickers, DEX pair addresses, circulating supply source, FDV source.
- ETF or fund: ticker, ISIN, issuer, benchmark, domicile, expense ratio, distribution policy, holdings date.

## Normalization Checks

1. Check whether the symbol maps to multiple securities, share classes, exchanges, wrappers, ADRs, or chains.
2. Separate local currency returns from base currency returns.
3. Record whether price series are adjusted for dividends, splits, rights issues, token migrations, or redenominations.
4. Use timestamps for every market data field that can change intraday.
5. Treat company name matches as weak evidence until an exchange specific identifier confirms the instrument.

## Output Template

| Field | Value | Source | Timestamp | Confidence |
| --- | --- | --- | --- | --- |

End with:

- `Ambiguities`: unresolved mappings.
- `Required Adjustments`: corporate action or token event handling.
- `Routing`: next specialist skill to call.
