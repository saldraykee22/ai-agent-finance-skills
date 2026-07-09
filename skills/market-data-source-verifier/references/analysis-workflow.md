# Market Data Verification Workflow

## Source hierarchy

- Prices/volume: exchange, issuer/exchange pages, reputable market data providers.
- Filings: SEC EDGAR, KAP, EQS/company releases, Bundesanzeiger, regulator portals.
- Macro: central banks, official statistical agencies, treasury/finance ministries.
- Crypto: block explorers, protocol docs, exchange pages/APIs, governance forums, reputable aggregators.
- Corporate actions: company IR, exchange notices, KAP/SEC/EQS, official index providers.
- News/events: original announcement, filing, regulator notice, central bank statement, court filing, then high-quality news wires.

## Verification checklist

1. Confirm identity:
   - Ticker, exchange, ISIN, CIK, WKN, contract address, chain, futures contract, option expiry/strike.
2. Confirm timestamp:
   - Date, time zone, market session, release time, data delay.
3. Confirm adjustment basis:
   - Split/dividend adjusted or raw price, consolidated or standalone financials, nominal or real macro data.
4. Cross-check:
   - Use at least two sources for high-impact or surprising data when possible.
5. Resolve conflicts:
   - Prefer primary source.
   - Prefer newest timestamp when source quality is comparable.
   - Preserve conflict note if unresolved.

## Perishable fields

- Price, volume, market cap, funding, open interest, option IV, yield, FX, commodity futures, macro surprise, news status.
- Treat these as stale unless timestamped.

## Output format

```text
Identifier:
- ...

Sources:
| Field | Value | Source | Timestamp | Notes |

Verified facts:
- ...

Conflicts/stale data:
- ...

Use/avoid:
- Use:
- Avoid:
```
