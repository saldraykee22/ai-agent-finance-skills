# Commodities Analysis Workflow

## Source hierarchy

- Energy: EIA, IEA, OPEC, exchange data, pipeline/LNG/shipping data where available.
- Metals: LME, COMEX/CME, SHFE, exchange inventories, producer reports, customs data.
- Agriculture: USDA WASDE, crop progress, weather agencies, exchange data, export inspections.
- Precious metals: real yields, USD, central bank gold data, ETF holdings, futures positioning.
- Market data: futures curves, spreads, volume, open interest, inventories, freight, refining margins.

## Research process

1. Identify commodity:
   - Spot or futures, contract month, exchange, unit, currency, delivery location.
2. Gather current market snapshot:
   - Price, curve shape, key spreads, volume, open interest, volatility.
3. Analyze supply:
   - Production, outages, capex, spare capacity, mining grades, weather, export restrictions.
4. Analyze demand:
   - Industrial cycle, transport, power generation, construction, China demand, substitution.
5. Analyze inventories:
   - Absolute level, seasonal norm, days of demand, location, exchange stocks versus physical stocks.
6. Analyze curve:
   - Backwardation suggests tight nearby supply or strong convenience yield.
   - Contango suggests surplus, storage economics, weak nearby demand, or financing/storage costs.
7. Analyze macro and FX:
   - USD, real yields, global growth, inflation, rates, risk appetite.
8. Review positioning and seasonality:
   - CFTC/COT, managed money, producer hedging, refinery maintenance, heating/cooling season, crop calendar.
9. Map impacted assets:
   - Producers, consumers, margins, currencies, inflation, bonds, equities.

## Commodity-specific notes

- Oil: track crude differentials, refining margins, product inventories, OPEC compliance, shale response.
- Natural gas: weather, storage, LNG flows, pipeline constraints, regional basis.
- Gold: real yields, USD, central bank buying, ETF flows, risk stress.
- Copper: China property/grid demand, inventories, mine supply, treatment charges.
- Grains: acreage, yield, weather, export demand, stocks-to-use.

## Watchpoints

- Front-month charts can mislead around contract rolls.
- Inventory location matters.
- Futures curve signals can reflect financing/storage constraints, not only demand.
- Weather models change quickly.
- Commodity-linked equities depend on cost curve, hedges, leverage, and capital discipline.

## Output format

```text
Snapshot:
- Price/contract/date/source:
- Curve/spreads:

Supply:
- ...

Demand:
- ...

Inventories:
- ...

Macro/positioning:
- ...

Impacted assets:
- Producers:
- Consumers:
- FX/inflation:

Scenarios:
- Base:
- Tightness/upside:
- Surplus/downside:
```
