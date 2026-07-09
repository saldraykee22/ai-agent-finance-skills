---
name: api-source-integration-planner
description: Plan finance API and data source integrations for prices, filings, fundamentals, macro releases, KAP disclosures, Borsa Istanbul data, SEC EDGAR, Deutsche Boerse or Xetra data, crypto exchange APIs, block explorers, DeFi dashboards, token unlock data, and portfolio tools. Use when choosing sources, designing connectors, comparing free and paid data, or preparing an API integration backlog.
---

# API Source Integration Planner

## Core Rule

Prefer source reliability and identifier precision over convenience. Do not propose an API as trusted until coverage, freshness, licensing, rate limits, and identifier mapping are clear.

## Workflow

1. Define required data fields and decision horizon.
2. Classify each source as primary, near-primary, aggregator, vendor, exchange, protocol, manual, or derived.
3. Check coverage, frequency, latency, historical depth, rate limits, authentication, cost, licensing, and failure modes.
4. Map identifiers through `asset-master-data-manager`.
5. Define fallback sources and reconciliation rules through `data-quality-reconciliation-engine`.
6. Produce an integration backlog with priority, source, fields, refresh cadence, and validation checks.

## Output

Return `Data Needs`, `Source Options`, `Coverage and Limits`, `Integration Backlog`, `Validation Plan`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for source selection matrix.
