# Short and Crowding Workflow

## Equity indicators

- Short interest.
- Days to cover.
- Short-sale volume.
- Borrow availability and borrow cost when available.
- Put/call, options OI, skew.
- Margin debt and market leverage context.
- Ownership concentration and free float.

## Crypto indicators

- Perp funding.
- Open interest.
- Basis.
- Liquidation clusters.
- Spot volume versus perp volume.
- Exchange concentration.
- Stablecoin liquidity.

## Analysis process

1. Identify asset, venue, and data timestamp.
2. Determine whether move is:
   - Fundamental.
   - Flow-driven.
   - Short covering.
   - Long liquidation.
   - Liquidity vacuum.
3. Score risk:
   - Squeeze risk: high short/OI, rising price, limited float/liquidity, catalyst.
   - Crowded long risk: high leverage, euphoric funding, thin spot support.
4. Translate to spot:
   - Avoid chasing.
   - Wait for reset.
   - Reduce size.
   - Use staged entry/exit.

## Output format

```text
Positioning snapshot:
- ...

Crowding indicators:
- ...

Risk:
- Squeeze:
- Long unwind:
- Liquidity:

Spot implication:
- ...

Data limits:
- ...
```
