# Pre-Trade Gate

## Required Checks

| Gate | Pass Standard |
| --- | --- |
| Instrument identity | Exact ticker, venue, currency, and token contract if crypto |
| Data freshness | Price, volume, event, and source timestamps are current enough for the requested horizon |
| Catalyst risk | Earnings, KAP, filing, macro, unlock, dividend, split, index change, and regulatory events checked |
| Liquidity | Expected order size is reasonable versus volume, spread, and market depth |
| Position size | Fits cash, concentration, loss tolerance, and scenario risk |
| Invalidation | Clear level, event, or thesis condition that proves the setup wrong |
| Execution | Order type, session timing, staged plan, slippage range, and partial fill plan defined |
| Monitoring | Review cadence, alerts, and post-trade journal fields defined |

## Verdicts

- `Pass`: no blocking issue, execution plan is explicit.
- `Conditional Pass`: one or more conditions must be satisfied first.
- `Do Not Execute Yet`: missing core data, unacceptable risk, weak liquidity, or no invalidation.
