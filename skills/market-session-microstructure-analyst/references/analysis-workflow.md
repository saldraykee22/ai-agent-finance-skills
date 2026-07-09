# Market Session and Microstructure Workflow

## Checks

- Venue and trading calendar.
- Session state: pre-open, continuous trading, auction, close, after-hours, weekend crypto.
- Order book depth and spread.
- Order types available.
- Circuit breakers, volatility interruption, price limits, market-wide halt.
- Settlement cycle and corporate action dates.
- BIST-specific measures: gross settlement, short-sale restriction, order package measures, watchlist status.
- Crypto-specific measures: exchange maintenance, withdrawal status, funding timestamp, weekend liquidity, stablecoin pair depth.

## Process

1. Define intended action: enter, add, trim, exit, transfer, rebalance.
2. Identify best liquidity window.
3. Check microstructure constraints.
4. Choose execution style:
   - Wait for auction/continuous session.
   - Stage orders.
   - Limit order only.
   - Avoid low-liquidity window.
5. Define abort conditions.

## Output format

```text
Venue/session:
- ...

Liquidity window:
- ...

Microstructure risks:
- ...

Execution timing:
- ...

Abort conditions:
- ...
```
