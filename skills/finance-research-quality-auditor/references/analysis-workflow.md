# Finance Research Quality Audit Workflow

## Evidence tiers

- Tier 1: primary sources such as filings, KAP, SEC, exchange pages, official macro releases, block explorers, company IR.
- Tier 2: reputable aggregators, transcript providers, fund-flow providers, analytics dashboards.
- Tier 3: media summaries, social posts, unsourced screenshots, stale tables.

## Audit checklist

1. Identity:
   - Correct ticker, exchange, chain, contract, ISIN, CIK, currency, reporting period.
2. Source freshness:
   - Timestamp current price, volume, filing, funding, OI, macro, news, and on-chain data.
3. Calculations:
   - Ratios, valuation, P&L, breakeven, sizing, and scenario math.
4. Assumptions:
   - Explicit, sourced, and consistent with horizon.
5. Alternatives:
   - Base/upside/downside and invalidation.
6. Spot decision readiness:
   - Policy fit, liquidity, cost/slippage, position lifecycle stage, portfolio exposure, behavioral flags.
7. Missing risks:
   - Corporate action, custody, policy, distress, ownership, crowding, event calendar.

## Verdict scale

- Pass: decision-ready with minor monitoring items.
- Conditional pass: usable after named fixes.
- Fail: conclusion rests on missing, stale, or contradictory evidence.

## Output format

```text
Audit verdict:
- Pass / Conditional pass / Fail:

Evidence gaps:
- ...

Calculation/logic issues:
- ...

Missing decision gates:
- ...

Required fixes:
- ...

Clean decision frame:
- ...
```
