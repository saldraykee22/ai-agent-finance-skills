# Portfolio Ledger Workflow

## Tables

- Trades: trade ID, asset ID, venue, side, quantity, price, fees, timestamp, order ID, strategy tag.
- Cash: deposit, withdrawal, transfer, dividend, interest, FX conversion, fee, timestamp.
- Holdings: asset ID, quantity, cost, market value, unrealized P&L, venue, custody.
- Corporate actions: dividend, split, rights, bonus, buyback, merger, redenomination.
- Crypto events: transfer, staking reward, unlock exposure, airdrop, burn, migration, bridge.
- Reconciliation: expected quantity, actual quantity, difference, source, timestamp, resolution.

## Reconciliation Standard

If holdings do not reconcile, do not force performance numbers. Identify missing trades, transfers, fees, corporate actions, or FX rates first.
