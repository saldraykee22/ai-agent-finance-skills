# Fixed Income and FX Workflow

## Source hierarchy

- Central banks and official rate pages.
- Treasury/finance ministry debt pages and auction results.
- Official inflation and macro data agencies.
- Exchange/market data for yields, bond prices, FX, futures, swaps where available.
- Rating agencies, issuer filings, bond prospectuses, CDS data providers when available.

## Rates process

1. Identify curve and instrument: country, currency, maturity, nominal/real, fixed/floating, benchmark.
2. Gather current levels:
   - Policy rate, 2y, 5y, 10y, 30y, curve slopes, real yields, breakevens.
   - Futures/OIS-implied central bank path when available.
3. Explain move:
   - Growth, inflation, central bank reaction, fiscal supply, term premium, liquidity, risk-off.
4. Assess duration:
   - Price sensitivity to rate moves.
   - Curve risk: steepener/flattener, bull/bear move.
5. Link to assets:
   - Equity multiples, banks, REITs, growth stocks, gold, FX, credit.

## Credit process

1. Identify issuer, seniority, maturity, coupon, currency, covenants, security, call features.
2. Analyze credit:
   - Leverage, interest coverage, FCF, maturity wall, liquidity, refinancing access.
   - Spread versus rating, peers, history, and sovereign curve.
3. Identify risks:
   - Downgrade, covenant breach, default, restructuring, FX mismatch, regulatory risk.

## FX process

1. Identify pair, horizon, and whether spot, forward, carry, hedge, or macro view.
2. Analyze drivers:
   - Rate differentials, real rates, inflation, current account, capital flows, reserves.
   - Terms of trade, commodity exposure, political risk, central bank credibility.
3. Check market structure:
   - Trend, volatility, positioning, option skew, liquidity, intervention risk.
4. Map impact:
   - Importers/exporters, foreign debt, equity translation, inflation pass-through.

## Watchpoints

- Yield and price move inversely; duration determines magnitude.
- Nominal yields can rise from growth optimism or inflation fear.
- Carry can be wiped out by FX depreciation.
- Sovereign local-currency and hard-currency risk are different.
- Credit spreads can lag equity stress until liquidity breaks.
- FX regimes matter: floating, managed, pegged, capital controls.

## Output format

```text
Snapshot:
- Levels/date/source:

Rates/curve:
- ...

Credit/sovereign:
- ...

FX:
- ...

Carry/duration/liquidity:
- ...

Scenarios:
- Base:
- Hawkish/rates up:
- Dovish/rates down:
- Risk-off:

Watch next:
- ...
```
