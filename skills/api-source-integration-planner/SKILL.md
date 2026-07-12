---
name: api-source-integration-planner
description: Plan and operate finance data-source integrations for prices, filings, fundamentals, macro releases, KAP, Borsa Istanbul, crypto exchanges, block explorers, DeFi data, and portfolio tools. Use when choosing sources, mapping MCP tools, designing connectors, comparing data providers, preparing an integration backlog, or using saidsurucu/borsa-mcp and saldraykee22/binance-trader-mcp across Hermes Agent, Codex, or Antigravity.
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

## MCP Routing

When `borsa-mcp` or `binance-trader-mcp` is available, read `references/mcp-tool-routing.md` before selecting tools. Discover tools by capability rather than assuming a client-specific qualified name. Keep research tools, private account reads, and trade mutations in separate permission tiers.

## Output

Return `Data Needs`, `Source Options`, `Coverage and Limits`, `Integration Backlog`, `Validation Plan`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for the source selection matrix and `references/mcp-tool-routing.md` when either preferred MCP is available.
