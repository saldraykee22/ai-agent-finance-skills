# Benchmark Attribution Workflow

## Benchmark selection

- BIST-only: XU100, relevant sector index, or custom equal-weight BIST watchlist.
- Crypto-only: BTC, ETH, BTC/ETH blend, total crypto market, or chosen narrative basket.
- BIST + crypto: custom blended benchmark based on policy weights.
- Multi-market: blended benchmark by asset class, currency, and target allocation.

## Attribution categories

- Allocation: being overweight/underweight asset class, sector, theme, or cash.
- Selection: choosing better/worse assets within a bucket.
- Timing: entry/exit and rebalance timing.
- FX: currency movement versus reporting currency.
- Costs: commission, spread, slippage, fees, tax drag if supplied.
- Cash drag: uninvested cash effect.

## Process

1. Define period and reporting currency.
2. Choose benchmark and explain why.
3. Calculate or estimate portfolio return and benchmark return.
4. Attribute difference by category.
5. Identify repeatable edge versus one-off effect.

## Output format

```text
Benchmark:
- ...

Return comparison:
- Portfolio:
- Benchmark:
- Difference:

Attribution:
| Driver | Effect | Explanation |

Top contributors:
- ...

Top detractors:
- ...

Lessons:
- ...
```
