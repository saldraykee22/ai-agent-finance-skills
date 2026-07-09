# Trade Blotter Workflow

## State Machine

Idea -> Planned -> Pre-trade checked -> Approved -> Working -> Partial fill or Filled -> Ledger recorded -> TCA reviewed -> Journal reviewed -> Archived.

## Required Fields

Trade ID, thesis ID, asset ID, side, intended quantity, approved quantity, venue, order type, limit, timestamp, status, fill quantity, fill price, fees, slippage note, ledger status, journal status.

## Control Breaks

Missing pre-trade check, missing thesis, stale order, fill quantity mismatch, fee mismatch, portfolio ledger mismatch, or no post-trade review.
