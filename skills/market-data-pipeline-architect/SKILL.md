---
name: market-data-pipeline-architect
description: Design market data pipelines, schemas, refresh cadence, storage layers, data lineage, validation checks, adjustment handling, and downstream research feeds for BIST, crypto, US, Germany, FX, commodities, ETFs, macro, filings, and portfolio data. Use when the user wants repeatable data infrastructure, CSV or database schemas, ingestion plans, data marts, or daily finance data workflows.
---

# Market Data Pipeline Architect

## Core Rule

Design the pipeline around decision use, not raw data hoarding. Every field should have owner source, timestamp, adjustment policy, validation rule, and downstream consumer.

## Workflow

1. Define use cases: daily briefing, watchlist ranking, valuation, portfolio dashboard, alerting, trade journal, or research memo.
2. Split sources into primary, secondary, vendor, manual, and derived layers.
3. Define schemas for assets, prices, fundamentals, filings, corporate actions, token supply, on-chain metrics, macro data, trades, holdings, and alerts.
4. Set refresh cadence and timestamp standards for each table.
5. Add validation checks: missing data, stale data, duplicates, corporate action gaps, currency mismatch, token contract mismatch, and outliers.
6. Route uncertain source choices to `api-source-integration-planner`, `asset-master-data-manager`, and `data-quality-reconciliation-engine`.

## Output

Return `Use Cases`, `Source Map`, `Schema Plan`, `Refresh Cadence`, `Validation Rules`, `Downstream Consumers`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` when designing a full pipeline.
