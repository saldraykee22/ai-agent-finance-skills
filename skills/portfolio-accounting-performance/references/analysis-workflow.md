# Portfolio Accounting and Performance Workflow

## Input fields

- Transaction date/time, asset, venue, side, quantity, price, fee, currency.
- Deposits, withdrawals, transfers, dividends, staking rewards, airdrops, taxes withheld if known.
- Current holdings, current prices, cash balances, FX rates, benchmark.

## Accounting process

1. Normalize transactions by asset and currency.
2. Reconcile holdings:
   - Beginning quantity + buys - sells + transfers/rewards = ending quantity.
3. Calculate cost basis:
   - Use the user's specified method if provided.
   - If not provided, state the chosen method and keep it consistent.
4. Calculate P&L:
   - Realized P&L from closed quantity.
   - Unrealized P&L from remaining quantity.
   - Total P&L = realized + unrealized + income - fees - known taxes.
5. Separate FX:
   - Local asset return versus reporting-currency return.
6. Compare benchmark:
   - BIST: relevant BIST index or sector index.
   - Crypto: BTC, ETH, total crypto market, or selected benchmark.
   - Multi-asset: blended benchmark based on policy weights.

## Attribution

- Allocation: effect of being overweight/underweight an asset or sector.
- Selection: effect of chosen asset versus benchmark.
- Timing: effect of entry/exit if transaction history exists.
- FX: currency translation effect.
- Costs: commissions, spreads, slippage, funding/withdrawal costs.

## Output format

```text
Accounting basis:
- Period:
- Currency:
- Cost method:

P&L:
- Realized:
- Unrealized:
- Income:
- Fees/costs:
- Total:

Contribution:
| Asset | Weight | P&L | Contribution | Notes |

Benchmark:
- ...

Data gaps:
- ...
```
