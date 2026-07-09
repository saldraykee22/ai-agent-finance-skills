# Liquidity and Execution Workflow

## Liquidity checks

- Average daily volume and turnover.
- Bid-ask spread.
- Order book depth near intended price.
- Recent volume spikes and whether they are sustainable.
- Session timing and auction effects.
- Exchange/venue reliability and withdrawal/deposit status for crypto.
- BIST regulatory measures, gross settlement, watchlist status, or order restrictions when relevant.

## Execution planning

1. Define target quantity and max acceptable slippage.
2. Compare order size to:
   - Daily volume.
   - Visible depth.
   - Typical candle/session volume.
3. Choose style:
   - Immediate small trade.
   - Staged entry/exit.
   - Limit order near liquidity zone.
   - Wait for volume confirmation.
4. Define abort conditions:
   - Spread widens.
   - Depth vanishes.
   - Price gaps past invalidation.
   - News/event changes thesis.

## Post-trade metrics

- Arrival price.
- Average fill.
- Slippage.
- Fees.
- Fill duration.
- Market impact.

## Output format

```text
Liquidity:
- ADV/depth/spread:
- Venue/session:

Order size:
- Size versus volume:
- Expected slippage:

Execution plan:
- Method:
- Staging:
- Limit/abort rules:

Review:
- Metrics to record:
```
