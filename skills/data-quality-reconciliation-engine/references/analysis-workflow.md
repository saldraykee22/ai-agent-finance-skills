# Data Reconciliation Workflow

## Source Priority

Use primary sources first when available: exchange official data, KAP, SEC EDGAR, issuer IR, Deutsche Boerse or issuer announcements, central bank or statistical agency releases, protocol docs, block explorers, audited proof pages, and exchange notices.

Vendor and aggregator data may be used for speed, but label it as secondary unless it is the only practical source.

## Conflict Taxonomy

- Timestamp mismatch: same field but different update time.
- Adjustment mismatch: split, dividend, rights issue, token migration, burn, emission, or redenomination.
- Instrument mismatch: ADR versus local share, dual listing, wrapped token, synthetic pair, index proxy.
- Unit mismatch: millions versus billions, TRY versus USD or EUR, per share versus total, token count versus percentage.
- Method mismatch: diluted shares versus basic shares, circulating supply versus free float supply, normalized EBITDA versus reported EBITDA.
- Venue mismatch: BIST session price, Xetra price, Frankfurt price, CEX price, DEX pool price, offshore pair.

## Decision Standard

Choose the source that is most primary, freshest, closest to the instrument, and methodologically aligned with the calculation. If two sources remain plausible, run scenarios instead of forcing one answer.
