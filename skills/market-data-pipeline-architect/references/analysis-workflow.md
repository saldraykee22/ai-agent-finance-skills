# Market Data Pipeline Workflow

## Canonical Tables

- `assets`: canonical identifiers, venue, currency, sector, chain, contract, issuer.
- `prices`: OHLCV, source, timestamp, venue, adjustment flag, currency.
- `fundamentals`: statements, ratios, period, restatement flag, source filing.
- `events`: KAP, SEC, issuer, macro, corporate actions, token unlocks, exchange notices.
- `token_supply`: circulating, total, max, FDV, unlock schedule, source.
- `onchain`: TVL, fees, users, flows, wallets, exchange balances, bridge data.
- `macro`: rates, FX, inflation, central bank events, liquidity indicators.
- `positions`: holdings, cost basis, cash, FX buckets, exposure.
- `trades`: orders, fills, fees, slippage, journal tags.
- `alerts`: trigger, state, severity, owner, last checked, next check.

## Pipeline Layers

1. Raw source capture.
2. Canonical normalization.
3. Reconciled analytical tables.
4. Derived signals and rankings.
5. Research, dashboard, alert, and trade-decision outputs.

## Validation Rules

Every current-sensitive field needs timestamp, source, freshness threshold, and fallback route. Every adjusted return calculation needs corporate action policy.
