# Insider and Ownership Flow Workflow

## Source hierarchy

- US: SEC Forms 3, 4, 5, 13D/13G, 13F, proxy statements.
- BIST: KAP disclosures, company IR, MKK/free-float information when available, buyback programs.
- Germany/EU: voting rights notifications, company disclosures, BaFin/EQS where relevant.
- Funds/ETFs: issuer holdings, fund reports, index provider data.

## Analysis process

1. Identify ownership instrument:
   - Common shares, preferred, ADR, options, RSUs, warrants, fund holdings.
2. Classify flow:
   - Insider buy/sell.
   - Planned sale or compensation-related transaction.
   - Major shareholder increase/decrease.
   - Fund/institutional reporting change.
   - Buyback/cancellation.
3. Assess signal quality:
   - Open-market buy is usually stronger than grant/option exercise.
   - Sale can be liquidity, tax, diversification, or negative signal.
   - 13F data is delayed and incomplete for shorts/non-US assets.
4. Connect to thesis:
   - Alignment, overhang, free-float pressure, passive flow, governance risk.

## Watchpoints

- Do not treat delayed filings as current flow.
- Large holders may use derivatives or off-market transactions.
- BIST free-float and ownership changes can affect liquidity and index eligibility.
- Crypto founder/team wallets belong with `crypto-onchain-flow-analyst` unless ownership is off-chain/legal.

## Output format

```text
Ownership snapshot:
- ...

Recent changes:
| Holder/insider | Action | Amount | Date | Source | Signal |

Interpretation:
- ...

Limitations:
- ...

Thesis impact:
- ...
```
