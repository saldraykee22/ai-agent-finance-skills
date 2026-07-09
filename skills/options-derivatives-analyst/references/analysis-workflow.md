# Options and Derivatives Workflow

## Data checklist

- Underlying price, venue, contract multiplier, expiry, strike, settlement type, margin/collateral.
- IV, realized volatility, IV rank/percentile, skew, term structure, open interest, volume.
- Futures/perps: funding, basis, open interest, liquidation zones, curve shape, roll yield.
- Event calendar: earnings, CPI/FOMC, product launch, unlock, court/regulator decision.

## Analysis process

1. Define objective: directional trade, volatility trade, hedge, income, risk reduction, synthetic exposure.
2. Compare implied move to expected catalyst range.
3. Read positioning:
   - OI concentration, volume spike, skew change, put/call, funding/OI divergence.
4. Choose structure:
   - Bullish: call spread, risk reversal, futures/perp, stock replacement.
   - Bearish: put spread, collar, short future, protective put.
   - Volatility: straddle/strangle, calendar, iron condor only when range thesis exists.
   - Hedge: protective put, collar, beta hedge, futures overlay.
5. Assess Greeks:
   - Delta, gamma, theta, vega, assignment/exercise, liquidity.
6. Scenario test:
   - Underlying up/down/flat, IV crush/expansion, time decay, gap risk, liquidity.

## Watchpoints

- Options flow is not automatically bullish or bearish; it may be hedging.
- IV can be expensive for good reason before events.
- Gamma zones are model-dependent; treat as approximate.
- Perp funding can stay extreme longer than expected.
- Futures roll and basis matter for holding period return.

## Output format

```text
Instrument:
- ...

Volatility/positioning:
- ...

Structure map:
- Directional:
- Volatility:
- Hedge:

Risk:
- Greeks:
- Liquidity:
- Failure modes:

Scenarios:
- ...
```
