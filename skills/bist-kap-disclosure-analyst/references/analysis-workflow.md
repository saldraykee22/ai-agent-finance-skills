# BIST KAP Disclosure Workflow

## Disclosure types

- Financial statements and operating results.
- Material events and business updates.
- Dividend, rights issue, bonus issue, capital reduction.
- Buyback program or execution.
- Major shareholder change and voting rights.
- Related-party transactions.
- Debt, refinancing, pledge, guarantee, collateral.
- Lawsuit, regulatory decision, license, tender, contract.
- Corporate governance and board/management changes.
- M&A, merger, spin-off, asset sale.

## Process

1. Identify company, ticker, disclosure date/time, disclosure type, and source link.
2. Extract facts:
   - Amount, currency, ratio, date, approval status, affected period.
3. Classify materiality:
   - Direct financial impact.
   - Share count/dilution.
   - Liquidity/float/index impact.
   - Governance/related-party risk.
   - Catalyst or thesis change.
4. Map impact:
   - Immediate market reaction.
   - Fundamental change.
   - Valuation input change.
   - Position lifecycle action.
5. Define follow-up:
   - Need financial statement note, investor presentation, AGM result, SPK approval, Borsa notice, or next KAP.

## Output format

```text
Disclosure:
- Company/ticker:
- Date/time:
- Type:

Facts:
- ...

Materiality:
- High / medium / low:

Impact:
- Financial:
- Share count/corporate action:
- Governance:
- Flow/liquidity:

Thesis action:
- Add / hold / trim / exit / review / no action:

Next checks:
- ...
```
