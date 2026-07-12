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

## Professional evidence contract

For every decision-changing claim, preserve:

| Field | Requirement |
| --- | --- |
| Observation | Exact value or statement; never silently substitute an estimate |
| Identity | Instrument, venue, currency, share class or chain/contract |
| Time | Observation time and source time, including timezone when intraday |
| Provenance | Primary document or provider, MCP/tool when used, and relevant parameters |
| Basis | Raw/adjusted, consolidated/standalone, nominal/real, circulating/fully diluted |
| Status | Verified, derived, estimated, stale, conflicting, or unavailable |

Use `Unavailable` rather than inventing a value. Label derived figures and show the formula. Keep estimates distinct from consensus and management guidance.

## Calculation reproducibility

- State units, currency, period, sign convention, denominator, and rounding rule.
- Show the formula and substituted inputs for decision-changing calculations.
- Reconcile totals to components when possible; explain residuals and rounding differences.
- Do not mix annual, quarterly, trailing, forward, nominal, real, adjusted, or unadjusted values without conversion.
- For returns, disclose price-only versus total return and the corporate-action adjustment basis.
- For crypto, distinguish circulating market cap, FDV, liquid float, emissions, and unlock-adjusted supply.
- For BIST, identify inflation-accounting basis and avoid comparing incompatible pre/post adjustment periods.

## Hard gates

Return `Fail` regardless of narrative strength when any decision-critical condition holds:

- Instrument identity is unresolved.
- Current-sensitive inputs are stale or unverified for the horizon.
- A material source conflict remains unresolved and can change the action.
- Liquidity or executable size cannot be established.
- Invalidation or maximum-loss logic is absent for an action-oriented idea.
- Portfolio impact cannot be estimated because essential holdings or sizing inputs are missing.
- An execution claim lacks explicit user authorization or confirmed exchange response.

## Confidence labels

- `High`: primary/near-primary evidence is current, calculations reproduce, and no material conflict remains.
- `Medium`: conclusion is usable but depends on named estimates, secondary sources, or moderate uncertainty.
- `Low`: missing or conflicting evidence can materially change the conclusion.

Confidence describes evidence strength, not expected return or conviction.

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
