# Screener and Watchlist Workflow

## Screen design

1. Define universe: market, asset class, sector, liquidity floor, currency, index membership.
2. Define objective: quality, value, growth, momentum, reversal, income, event, volatility, defensive, crypto narrative.
3. Define hard filters:
   - Liquidity, market cap, volume, spread, reporting availability, listing venue.
4. Define ranking factors:
   - Fundamental: growth, margin, ROIC/ROE, FCF yield, leverage, earnings revision.
   - Valuation: P/E, EV/EBITDA, P/B, EV/Sales, yield, FDV/revenue, sector metrics.
   - Technical: relative strength, trend, breakout, volume expansion, volatility contraction.
   - Event: earnings date, corporate action, macro catalyst, unlock, index change.
   - Risk: leverage, liquidity, drawdown, concentration, regulatory exposure.
5. Create tiers:
   - Tier 1: actionable now.
   - Tier 2: watch for trigger.
   - Tier 3: interesting but data gap or weak confirmation.

## Common templates

- Quality momentum: positive trend + strong margins/ROIC + earnings revision + liquidity.
- Deep value: low multiple + balance sheet survivability + visible catalyst.
- Event watchlist: upcoming catalyst + option/volume activity + clear scenario split.
- Crypto narrative: sector leadership + liquidity + unlock control + protocol traction.
- Defensive income: dividend/cash flow durability + low leverage + low cyclicality.

## Output format

```text
Universe:
- ...

Filters:
- Hard:
- Ranking:

Candidates:
| Name | Ticker | Score/Rank | Why included | Trigger | Main risk |

Watchlist:
- Tier 1:
- Tier 2:
- Tier 3:

Next checks:
- ...
```
