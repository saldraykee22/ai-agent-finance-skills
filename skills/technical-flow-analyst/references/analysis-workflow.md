# Technical and Flow Analysis Workflow

## Data checklist

- Current price, timeframe, exchange/venue, session status.
- OHLCV history, adjusted data for equities, continuous contract logic for futures.
- Relative benchmark: sector index, broad index, BTC/ETH, DXY, yield, or commodity peer.
- Volume, turnover, open interest, funding, options OI/IV/skew, breadth when relevant.

## Research process

1. Define instrument, timeframe, and objective: intraday, swing, position, hedge, or monitoring.
2. Determine trend:
   - Higher highs/lows or lower highs/lows.
   - Moving averages and slope.
   - Distance from mean and volatility bands.
3. Mark levels:
   - Prior highs/lows, gaps, VWAP, volume profile zones, consolidation boundaries.
   - Support/resistance as zones, with invalidation beyond the zone.
4. Momentum and volatility:
   - RSI/MACD or similar momentum only as supporting evidence.
   - ATR, realized volatility, implied volatility when available.
   - Divergences require price confirmation.
5. Volume and participation:
   - Breakout with volume expansion.
   - Climax volume, failed breakout, distribution/accumulation signs.
   - Breadth confirmation for indices and sectors.
6. Flow and positioning:
   - Futures open interest, funding, basis, COT where relevant.
   - Options OI, IV, skew, put/call, gamma zones when sourced credibly.
   - ETF flows and passive index events if relevant.
7. Build setup:
   - Directional bias, trigger, entry zone, invalidation, target zones, risk/reward.
   - Alternative path if price fails to confirm.

## Watchpoints

- Adjusted equity charts are necessary around dividends and splits.
- Futures rolls can distort historical levels.
- Low liquidity makes patterns less reliable.
- Indicators lag; price structure and volume lead.
- Funding/OI extremes show crowding, not direction by themselves.
- A breakout without follow-through often matters more than the breakout itself.

## Output format

```text
Trend:
- ...

Levels:
- Support:
- Resistance:
- Invalidation:

Momentum/volume:
- ...

Relative strength/breadth:
- ...

Flow/positioning:
- ...

Setup:
- Trigger:
- Entry zone:
- Targets:
- Failure path:
```
