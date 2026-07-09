# Stablecoin Liquidity Risk Workflow

## Checks

- Stablecoin ticker, issuer, chain, contract, and collateral model.
- Peg level and exchange spreads.
- Liquidity depth across main pairs.
- Mint/burn flows and exchange balances.
- Bridge/wrapped version risk.
- Redemption/withdrawal status.
- Concentration in one stablecoin, chain, or exchange.

## Interpretation

- Strong stablecoin liquidity can support crypto spot demand.
- Depegging, thin depth, or redemption stress can force risk-off behavior.
- Stablecoin inflows to exchanges may signal deployable liquidity, but not necessarily immediate buying.
- Bridge-wrapped stablecoins add bridge risk.

## Output format

```text
Exposure:
- Stablecoin:
- Chain/venue:
- Portfolio role:

Peg/liquidity:
- ...

Flows:
- ...

Risks:
- Issuer:
- Venue:
- Bridge:

Action:
- Hold / diversify / reduce / avoid / monitor:

Next checks:
- ...
```
