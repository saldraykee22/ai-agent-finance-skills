# Cost, Tax, and Slippage Workflow

## Cost stack

- Broker/exchange commission.
- Bid-ask spread.
- Market impact/slippage.
- FX conversion spread and transfer cost.
- Crypto network withdrawal/deposit fee.
- Fund/ETF expense ratio and tracking difference.
- Known tax/withholding fields supplied by the user.
- Opportunity cost from delayed fill or fragmented execution.

## Breakeven process

1. Identify instrument, venue, quote currency, order size, expected price, and holding period.
2. Estimate round-trip explicit cost:
   - Buy fee + sell fee + transfer/withdrawal + FX cost.
3. Estimate implicit cost:
   - Half-spread or full spread depending on fill assumption.
   - Slippage based on order size versus liquidity.
4. Add tax placeholder only if user provides rate or known withholding.
5. Compute breakeven:
   - Required gross move = total round-trip cost / capital deployed.
6. Compare alternatives:
   - Venue A vs venue B.
   - Spot asset vs ETF/fund.
   - BIST local trade vs foreign listing/ADR if relevant.

## Output format

```text
Trade:
- Asset/venue:
- Size:
- Currency:

Cost stack:
| Cost | Estimate | Basis | Confidence |

Breakeven:
- One-way:
- Round-trip:

Net impact:
- ...

Missing inputs:
- ...
```
