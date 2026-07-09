# Thesis Risk Register Workflow

## Register fields

- Asset, venue, currency, position status.
- Thesis statement.
- Key assumptions.
- Evidence supporting each assumption.
- Risks that would weaken the thesis.
- Invalidation triggers.
- Catalysts and dates.
- Monitoring indicators.
- Required action if triggered.
- Review cadence.

## Trigger types

- Price/technical: level break, failed breakout, trend loss.
- Fundamental: margin, revenue, debt, cash flow, guidance, KAP/filing change.
- Crypto-native: unlock, exchange inflow, stablecoin liquidity, protocol usage, exploit.
- Macro/policy: rates, FX, regulation, inflation, sanctions.
- Portfolio: concentration, liquidity, correlation, drawdown.
- Behavioral: FOMO, thesis drift, refusal to exit.

## Output format

```text
Thesis:
- ...

Assumptions:
| Assumption | Evidence | Monitor | Break condition |

Risks:
| Risk | Probability | Impact | Trigger | Action |

Action map:
- Add:
- Hold:
- Trim:
- Exit:
- Review:

Next review:
- ...
```
