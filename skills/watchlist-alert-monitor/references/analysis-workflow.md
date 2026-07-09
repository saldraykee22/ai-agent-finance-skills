# Watchlist Alert Workflow

## Watchlist states

- Research: data incomplete.
- Waiting for trigger: thesis exists, price/setup not ready.
- Active: position or active plan.
- Review: event or risk changed.
- Remove: thesis failed or opportunity stale.

## Alert types

- Price: level, breakout, breakdown, drawdown.
- Volume/liquidity: unusual volume, spread widening, depth loss.
- Fundamental: earnings, KAP, SEC filing, guidance, debt update.
- Crypto: unlock, exchange inflow, stablecoin liquidity, bridge flow, exploit, listing/delisting.
- Macro: rates, FX, CPI, central bank, policy shock.
- Portfolio: concentration, correlation, max size, drawdown.

## Output format

```text
Watchlist objective:
- ...

Alerts:
| Asset | State | Trigger | Source | Action | Review cadence |

Action map:
- Enter:
- Add:
- Trim:
- Exit:
- Remove:

Next review:
- ...
```
