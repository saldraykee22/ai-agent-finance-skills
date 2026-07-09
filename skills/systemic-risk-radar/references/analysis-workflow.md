# Systemic Risk Radar Workflow

## Risk categories

- Valuation pressure: stretched multiples, low risk premium, crowded narratives.
- Leverage: margin debt, derivatives positioning, crypto perps/OI/funding, leveraged products.
- Funding/liquidity: credit spreads, bank stress, stablecoin liquidity, exchange withdrawal risk.
- Macro shock: inflation surprise, rate shock, FX stress, recession signal.
- Local BIST risk: TRY volatility, rates, inflation, policy/regulation, liquidity measures.
- Crypto-specific risk: stablecoin depeg, exchange risk, bridge/protocol exploit, forced deleveraging.
- Geopolitical/commodity risk: energy shock, sanctions, trade restrictions, conflict escalation.

## Process

1. Define relevant portfolio exposures.
2. Gather current high-level indicators.
3. Classify regime:
   - Green: normal risk.
   - Yellow: elevated but manageable.
   - Orange: reduce risk and tighten invalidations.
   - Red: liquidity and capital preservation dominate.
4. Translate into actions:
   - Reduce weakest positions.
   - Avoid illiquid entries.
   - Increase cash.
   - Delay event-risk trades.
   - Tighten review cadence.

## Output format

```text
Risk regime:
- Green / Yellow / Orange / Red:

Active alarms:
- ...

BIST effect:
- ...

Crypto effect:
- ...

Portfolio translation:
- Sizing:
- Liquidity:
- Watchlist:

Watch next:
- ...
```
