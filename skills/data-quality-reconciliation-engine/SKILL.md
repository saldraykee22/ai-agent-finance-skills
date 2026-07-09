---
name: data-quality-reconciliation-engine
description: Reconcile conflicting or stale financial data across prices, volumes, adjusted series, filings, statements, macro releases, corporate actions, token supply, exchange data, on-chain data, analyst estimates, and news timestamps. Use when sources disagree, a number looks suspicious, current data is required, or an analysis depends on exact market data.
---

# Data Quality Reconciliation Engine

## Core Rule

Do not average away a data conflict. Identify the conflict type, rank source authority, explain the likely cause, and choose the field that should drive the analysis.

## Workflow

1. Define the disputed field and why it matters.
2. List sources with timestamp, data vendor or primary source, update frequency, units, currency, adjustment basis, and coverage.
3. Classify the conflict: stale timestamp, adjusted versus unadjusted, different exchange, currency conversion, corporate action, filing restatement, token supply definition, wrapper or chain mismatch, intraday delay, or vendor calculation method.
4. Select the analysis field and mark any fields unsuitable for decision use.
5. Route unresolved facts to `market-data-source-verifier`, `asset-master-data-manager`, `corporate-actions-analyst`, or `crypto-tokenomics-supply-analyst`.

## Output

Return `Verified Facts`, `Conflict Table`, `Chosen Data`, `Rejected Data`, `Calculations`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` when resolving a multi-source or high impact data conflict.
