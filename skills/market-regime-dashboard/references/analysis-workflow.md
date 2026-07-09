# Market Regime Dashboard Workflow

## Regime labels

- Risk-on trend.
- Selective risk-on.
- Choppy/mean-reverting.
- Defensive.
- Liquidity stress.
- Event-driven.

## Dashboard components

- BIST: XU100 trend, sector breadth, volume, TRY rates/FX, KAP/event flow, liquidity measures.
- Crypto: BTC/ETH trend, alt breadth, stablecoin liquidity, funding/OI, on-chain flow, exchange risk.
- Global: SPX/Nasdaq/DAX, rates, DXY/EURUSD/USDTRY, commodities, credit spreads, volatility.
- Portfolio: cash weight, concentration, drawdown, open risk, event calendar.

## Action translation

- Risk-on trend: allow quality setups, normal size if liquidity confirms.
- Selective risk-on: prefer leaders, avoid weak liquidity.
- Choppy: reduce chase, use tighter triggers, smaller size.
- Defensive: prioritize cash, trim weak positions, avoid new illiquid entries.
- Liquidity stress: capital preservation and exit liquidity dominate.
- Event-driven: wait for event or size smaller.

## Output format

```text
Regime:
- ...

BIST:
- ...

Crypto:
- ...

Global:
- ...

Spot posture:
- Size:
- Watchlist:
- Liquidity:
- Review cadence:

Watch next:
- ...
```
