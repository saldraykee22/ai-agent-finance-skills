---
name: trade-blotter-operations-controller
description: Control trade blotter workflow for planned, staged, working, filled, cancelled, partial, and reviewed spot trades across BIST, crypto, US, Germany, ETFs, FX, and commodities. Use when the user wants an operations view of orders, fill status, execution readiness, trade lifecycle, blotter schema, or post-trade routing.
---

# Trade Blotter Operations Controller

## Core Rule

Keep idea, order, fill, position, and journal states separate. A trade is not complete until it is recorded, reconciled, reviewed, and linked back to the thesis.

## Workflow

1. Classify each item: idea, planned order, approved order, working order, partial fill, full fill, cancelled, amended, reviewed, or archived.
2. Check whether pre-trade gate passed before approval.
3. Record order and fill fields with timestamp, venue, order type, quantity, price, fees, and execution notes.
4. Route fills to `portfolio-recordkeeping-ledger`, `execution-quality-tca-analyst`, `portfolio-accounting-performance`, and `trade-journal-reviewer`.
5. Flag unresolved operations issues: missing fill, fee mismatch, partial fill, wrong venue, stale order, or missing thesis link.

## Output

Return `Blotter State`, `Pending Actions`, `Control Breaks`, `Post-Trade Routing`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for blotter schema and state machine.
