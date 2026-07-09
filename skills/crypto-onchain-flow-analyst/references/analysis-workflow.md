# Crypto On-Chain Flow Workflow

## Source hierarchy

- Block explorers and verified contracts.
- Protocol dashboards and official docs.
- Dune/Artemis/DefiLlama/Token Terminal-style dashboards.
- Exchange wallet labels only when credible.
- Project treasury and governance disclosures.

## Analysis process

1. Verify token:
   - Chain, contract, decimals, supply, wrapped/bridged status.
2. Check flows:
   - Exchange inflows/outflows.
   - Whale accumulation/distribution.
   - Stablecoin liquidity on relevant chains.
   - Bridge inflows/outflows.
   - Staking/unstaking.
   - Unlock wallet movement.
3. Check protocol activity:
   - TVL, fees, revenue, users, transactions, active addresses.
4. Interpret signal:
   - Accumulation, distribution, rotation, incentive farming, unlock pressure, exchange sell pressure.
5. Connect to spot:
   - Confirm, weaken, or neutralize trade thesis.

## Watchpoints

- Exchange inflow is not always immediate selling.
- Whale wallet labels can be wrong.
- Incentive programs can fake activity.
- Bridged supply adds bridge risk.
- Unlock wallet movement is more important near vesting dates.

## Output format

```text
Identity:
- ...

Flows:
- Exchange:
- Whale:
- Stablecoin:
- Bridge:
- Unlock:

Protocol activity:
- ...

Interpretation:
- ...

Spot implication:
- ...
```
