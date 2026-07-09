# ETF and Fund Flow Workflow

## Source hierarchy

- Fund issuer holdings and flow pages.
- ETF prospectus, fact sheet, index methodology.
- Exchange/issuer creation-redemption data when available.
- Reputable fund-flow aggregators.
- For crypto ETFs: issuer holdings, custody disclosures, authorized participant mechanics where available.

## Analysis process

1. Identify product:
   - Ticker, issuer, index, asset class, holdings, expense ratio, currency.
2. Distinguish:
   - AUM change from price return.
   - Net flow from market performance.
   - Estimated flow from official holdings.
3. Map underlying impact:
   - Holding weight.
   - Liquidity of underlying.
   - Rebalance schedule.
   - Creation/redemption pressure.
4. Assess flow persistence:
   - One-day spike, trend, event-driven, passive rebalance.
5. Connect to spot decision:
   - Supportive flow, overhang, crowded exposure, or irrelevant noise.

## Watchpoints

- ETF volume is not the same as fund inflow.
- AUM can rise because asset price rose.
- Passive flow can affect small/liquid names more than mega caps.
- Fund fee and tracking difference matter for long holding periods.

## Output format

```text
Product:
- ...

Flow:
- ...

Underlying impact:
- ...

Cost/fee:
- ...

Implication:
- ...

Data limits:
- ...
```
