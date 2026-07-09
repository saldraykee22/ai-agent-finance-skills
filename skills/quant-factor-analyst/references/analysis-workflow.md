# Quant Factor Workflow

## Factor definitions

- Momentum: 3/6/12 month return, relative strength, trend persistence.
- Value: earnings yield, FCF yield, EV/EBITDA, P/B, sales yield, sector-relative valuation.
- Quality: ROE/ROIC, margin stability, accruals, leverage, cash conversion.
- Low volatility: realized volatility, beta, max drawdown.
- Size/liquidity: market cap, ADV, turnover, spread.
- Sentiment/event: earnings revision, volume spike, news/catalyst count.

## Data hygiene

- Use adjusted prices for equities.
- Avoid look-ahead bias: only use data available at the rebalance date.
- Include delisted names when testing if possible; if not, state survivorship risk.
- Normalize within sector/market when factors are structurally different.
- Winsorize or rank extreme values rather than letting outliers dominate.

## Test design

1. Define universe and date range.
2. Define signal and rebalance frequency.
3. Rank into buckets or choose top/bottom lists.
4. Track returns, volatility, drawdown, hit rate, turnover, beta, correlation.
5. Compare to benchmark and equal-weight universe.
6. Interpret whether signal is robust, regime-dependent, or data-mined.

## Output format

```text
Setup:
- Universe:
- Factor:
- Lookback/rebalance:

Data checks:
- ...

Results:
| Bucket/Name | Return | Vol | Drawdown | Notes |

Interpretation:
- ...

Failure modes:
- ...
```
