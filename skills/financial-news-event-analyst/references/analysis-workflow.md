# Financial News and Event Analysis Workflow

## Source hierarchy

- Primary: company filings, exchange notices, regulator releases, central bank statements, court filings, official macro releases.
- Near-primary: company transcripts, investor presentations, official social accounts, governance forums.
- High-quality secondary: major financial news wires and reputable specialist sources.
- Market data: price, volume, spread, options IV, futures, FX, yields around the event.

## Event classification

- Earnings/guidance: beat/miss, margin, outlook, segment surprise, management tone.
- Corporate action: M&A, buyback, dividend, split, capital raise, spin-off, restructuring.
- Regulatory/legal: approval, ban, fine, lawsuit, investigation, court decision.
- Macro/policy: CPI, jobs, rates, central bank statement, fiscal action.
- Credit/liquidity: downgrade, default, covenant breach, refinancing, bank stress.
- Crypto/protocol: exploit, listing, delisting, unlock, governance vote, chain halt, bridge issue.
- Commodity/geopolitical: supply disruption, sanction, OPEC decision, inventory shock.

## Research process

1. Reconstruct timeline:
   - Event time, source release time, market reaction windows, follow-up statements.
2. Verify facts:
   - What exactly changed versus prior expectation?
   - Is it confirmed, rumored, denied, or preliminary?
3. Map mechanism:
   - Revenue, margin, cash flow, balance sheet, cost of capital, legal liability, liquidity, positioning.
4. Compare expectation:
   - Was the event already priced?
   - Did guidance, consensus, or market-implied probability change?
5. Measure market reaction:
   - Price, volume, relative move, options IV, credit spreads, FX/yields, peer reaction.
6. Identify second-order effects:
   - Suppliers, customers, competitors, sector ETFs, currencies, commodities, rates.
7. Produce scenario tree:
   - Confirmed path, escalation path, reversal/denial path, delayed impact path.

## Watchpoints

- Headlines often omit conditions, effective dates, or accounting treatment.
- Market moves can reflect positioning rather than fundamental impact.
- Rumors need explicit labeling and should not be treated as facts.
- Legal/regulatory processes have timelines and appeal paths.
- Earnings reactions depend on expectations and guidance, not headline EPS alone.

## Output format

```text
Event:
- What happened:
- Source/time:
- Confirmation status:

Market reaction:
- ...

Mechanism:
- Revenue/margin/cash flow:
- Balance sheet/liquidity:
- Valuation/multiple:

Winners/losers:
- Direct:
- Second-order:

Scenarios:
- Base:
- Escalation:
- Reversal:

Watch next:
- ...
```
