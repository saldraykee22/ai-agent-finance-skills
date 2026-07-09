# Custody and Counterparty Risk Workflow

## Risk categories

- Exchange/broker solvency and operational reliability.
- Withdrawal/deposit status.
- Settlement cycle and failed settlement.
- Corporate action processing.
- Wallet key management.
- Stablecoin issuer/collateral risk.
- Bridge and wrapped asset risk.
- Concentration of assets at one venue.
- Jurisdiction/regulatory access risk.

## Process

1. Identify venue, asset, chain, account type, and custody model.
2. Determine exposure:
   - Amount held.
   - Percent of portfolio.
   - Withdrawal/settlement dependency.
3. Check operational status:
   - Deposits/withdrawals.
   - Network congestion.
   - Corporate action deadlines.
   - Broker/exchange notices.
4. Define mitigations:
   - Split custody.
   - Reduce venue concentration.
   - Prefer native assets over bridged assets when risk matters.
   - Keep transaction records and proof of balances.
   - Test small withdrawals before large transfers.

## Output format

```text
Exposure:
- Asset:
- Venue:
- Size:

Risks:
- Custody:
- Settlement:
- Operational:
- Jurisdiction:

Mitigation:
- ...

Monitor:
- ...
```
