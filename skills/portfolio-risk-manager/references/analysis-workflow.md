# Portfolio Risk Management Workflow

## Input checklist

- Holdings, quantities, cost basis, current price, currency, asset class, sector, country, liquidity.
- Cash, leverage, margin, derivatives, futures, options, borrow, funding cost.
- Time horizon, maximum acceptable drawdown, turnover tolerance, tax constraints if provided.
- Existing stop levels, invalidation points, thesis status, catalyst dates.

## Research process

1. Build portfolio snapshot:
   - Gross exposure, net exposure, cash, leverage, currency exposure.
   - Position weights by asset, sector, country, factor, theme, and liquidity bucket.
2. Identify concentration:
   - Single-name weight, top 5 weight, correlated themes, hidden macro bets.
   - Revenue/geography overlap across companies.
3. Estimate risk:
   - Volatility, beta, drawdown history, correlation clusters, VaR-style approximation when useful.
   - Liquidity risk using average daily volume and estimated exit days.
4. Position sizing:
   - Define invalidation level and loss per unit.
   - Size = capital at risk / distance to invalidation.
   - Adjust for liquidity, volatility, event risk, correlation, and conviction.
5. Stress test:
   - Equity drawdown, rate shock, FX shock, commodity shock, credit spread widening, liquidity gap.
   - Asset-specific event such as earnings miss, token unlock, regulatory hit, devaluation.
6. Risk controls:
   - Stop or invalidation, hedge, trim, diversify, rebalance, stagger entry, reduce leverage.
   - Define what data would increase, reduce, or close exposure.

## Sizing patterns

- Volatility-based: lower weight for higher realized/implied volatility.
- Thesis-risk based: size by max loss to invalidation.
- Liquidity-based: cap position by exit capacity.
- Correlation-aware: reduce size when multiple names share the same driver.
- Event-aware: reduce or hedge before binary catalysts if gap risk dominates.

## Watchpoints

- Diversification by ticker can still be concentration by factor.
- Correlations rise in stress.
- Liquidity vanishes when it matters most.
- Stop levels can fail through gaps; use scenario loss, not just stop loss.
- FX can dominate local equity returns for international portfolios.
- Leverage changes the portfolio before the thesis has time to work.

## Output format

```text
Portfolio snapshot:
- ...

Exposure map:
- Asset/sector/country/currency:
- Concentrations:

Risk estimates:
- Volatility/drawdown:
- Liquidity:
- Correlation:

Position sizing:
- ...

Stress tests:
- Scenario 1:
- Scenario 2:
- Scenario 3:

Actions/controls:
- ...

Missing data:
- ...
```
