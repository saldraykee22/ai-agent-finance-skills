---
name: finance-agent-orchestrator
description: Route complex finance requests across specialist finance skills and define an end-to-end research workflow. Use when the user asks for broad market analysis, a complete stock or crypto review, portfolio decision support, multi-asset research, watchlist construction, or any task that needs several finance skills such as market analysis, data verification, financial statements, valuation, technicals, derivatives, macro, sector, event, and portfolio risk.
---

# Finance Agent Orchestrator

## Core Workflow

Use this skill to choose the right finance skill sequence before doing broad analysis. Default to a BIST and crypto priority, spot-only workflow unless the user explicitly requests another instrument type. Use `bist-crypto-spot-command-center` as the primary entrypoint for broad BIST/crypto spot workflows. Read `references/analysis-workflow.md` for routing patterns, skill combinations, quality gates, and final synthesis format.

## Operating Rules

- Start by classifying the request: single asset, portfolio, screen, event, macro, derivative, sector, or report.
- For broad BIST/crypto spot requests, route first through `bist-crypto-spot-command-center`.
- For spot trade/investment requests, route through `personal-investment-policy`, `position-lifecycle-manager`, `liquidity-execution-analyst`, `cost-tax-slippage-analyst`, and `decision-quality-behavioral-analyst` when the decision depends on action.
- Always include `market-data-source-verifier` when current prices, filings, macro data, token data, news, or corporate actions matter.
- Add signal skills only when they can change the decision: earnings/transcripts, ownership flow, ETF/fund flow, short/crowding, on-chain flow, custody/counterparty, distress, or geopolitical/policy risk.
- Use `finance-research-quality-auditor`, `thesis-risk-register`, `scenario-stress-tester`, `watchlist-alert-monitor`, `spot-trading-playbook`, or `market-regime-dashboard` when the user needs decision readiness, monitoring, or a repeatable spot workflow.
- Use `daily-spot-market-briefing` and `capital-allocation-cash-manager` for daily preparation and cash/deployment questions.
- Combine specialist outputs into one coherent view; do not paste disconnected mini-reports.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Requested decision or research objective
2. Skill route used
3. Verified facts
4. Specialist findings
5. Spot decision gate
6. Scenario synthesis
7. Monitoring and quality gates
8. Next checks
