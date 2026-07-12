---
name: market-data-source-verifier
description: Verify financial market data, source quality, timestamps, identifiers, corporate actions, filings, macro releases, token supply, exchange data, prices, volumes, and news claims. Use when analysis depends on current or exact data, when sources conflict, when a ticker/contract/ISIN/CIK/address may be ambiguous, or before producing market-sensitive conclusions.
---

# Market Data Source Verifier

## Core Workflow

Use this skill as the data quality gate for finance work. Read `references/analysis-workflow.md` for source hierarchy, timestamp rules, identifier checks, and conflict resolution.

## Operating Rules

- Verify current-sensitive claims before analysis.
- Prefer primary sources and timestamp every perishable market fact.
- Flag stale, missing, conflicting, adjusted, or derived data.
- When `borsa-mcp` or `binance-trader-mcp` is available, use `api-source-integration-planner` to apply its MCP capability map, provenance fields, source precedence, and failure rules.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Data requested
2. Identifier check
3. Source table
4. Conflicts or stale fields
5. Verified facts to use
