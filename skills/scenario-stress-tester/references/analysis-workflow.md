# Scenario Stress Testing Workflow

## Scenario templates

- BIST market shock: XU100 down, TRY rate shock, liquidity thinning, sector regulation.
- Crypto shock: BTC/ETH drawdown, altcoin beta, stablecoin stress, exchange withdrawal issue, perp deleveraging.
- FX shock: TRY depreciation/appreciation, USD liquidity stress.
- Rate shock: local or global yields rise, growth multiples compress.
- Single-name shock: earnings miss, KAP negative disclosure, exploit, unlock sell pressure.
- Liquidity shock: spread widens, order book depth disappears, volume dries.

## Process

1. Define current exposure and reporting currency.
2. Choose scenarios and shock sizes.
3. Map direct and second-order impact.
4. Estimate loss or range.
5. Identify action thresholds:
   - No action.
   - Review.
   - Trim.
   - Exit.
   - Pause new entries.

## Output format

```text
Scenario set:
- ...

Impact table:
| Scenario | Direct impact | Second-order impact | Estimated loss | Action |

Liquidity constraints:
- ...

Thresholds:
- Review:
- Trim:
- Exit:
```
