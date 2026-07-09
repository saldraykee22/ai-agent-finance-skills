---
name: bist-market-analyst
description: Analyze Turkish BIST equities, BIST indices, company disclosures, financial statements, dividends, rights issues, liquidity, technical setups, and market microstructure. Use when the user asks about Borsa Istanbul stocks or indices, KAP disclosures, Turkish listed companies, BIST sector comparisons, TRY macro sensitivity, or a BIST-focused trading/investment research workflow.
---

# BIST Market Analyst

## Core Workflow

Use this skill for Borsa Istanbul research. Start with the user's exact ticker, company, index, timeframe, and desired depth. If the task depends on current prices, disclosures, index membership, dividends, splits, macro data, or regulations, verify with current sources before analyzing.

Read `references/analysis-workflow.md` for the detailed BIST workflow, source hierarchy, checklist, output format, and common failure modes.

## Operating Rules

- Separate verified facts, calculations, interpretation, and open uncertainties.
- Prefer primary sources: KAP, Borsa Istanbul, company investor relations, official financial statements, TCMB, TUIK, and regulator pages.
- Cross-check ticker suffixes, share classes, corporate actions, and adjusted price history before comparing returns.
- Do not add generic boilerplate caveats. Keep the output analytical, source-grounded, and direct.
- Match the user's language. If the user writes in Turkish, produce Turkish output.

## Companion Skills

- Use `market-data-source-verifier` for current price, KAP, financials, corporate actions, index membership, and macro-sensitive facts.
- Use `asset-master-data-manager` when ticker, exchange, ISIN, adjusted price, share class, or index membership ambiguity can affect the analysis.
- Use `data-quality-reconciliation-engine` when BIST price, volume, financial, KAP, or corporate action sources disagree.
- Use `bist-sector-rotation-analyst` and `relative-strength-momentum-ranker` when sector leadership, breadth, or BIST watchlist priority matters.
- Use `bist-kap-disclosure-analyst` when a KAP disclosure, material event, shareholder change, capital action, debt update, or related-party transaction drives the question.
- Use `financial-statement-analyst`, `valuation-modeling-analyst`, `technical-flow-analyst`, and `portfolio-risk-manager` for complete equity work.
- Use `personal-investment-policy`, `position-lifecycle-manager`, `liquidity-execution-analyst`, and `cost-tax-slippage-analyst` when a BIST analysis leads to a spot buy/add/trim/exit decision.
- Use `market-session-microstructure-analyst` when session timing, auction behavior, volatility measures, order restrictions, or settlement affects execution.
- Use `pre-trade-checklist-controller` before a BIST idea is treated as execution-ready.
- Use `signal-scoring-decision-engine` and `investment-committee-simulator` when several BIST signals must be collapsed into one decision.
- Use `market-manipulation-anomaly-detector` when price or volume behavior looks abnormal, catalyst-free, or low-liquidity driven.
- Use `corporate-actions-analyst` for dividends, rights issues, bonus issues, buybacks, mergers, and adjusted-chart issues.
- Use `earnings-call-transcript-analyst`, `insider-ownership-flow-analyst`, `distressed-balance-sheet-risk`, and `geopolitical-policy-risk-analyst` when management commentary, shareholder structure, balance sheet stress, or policy/regulation can change the BIST thesis.
- Use `spot-trading-playbook`, `thesis-risk-register`, `scenario-stress-tester`, `watchlist-alert-monitor`, and `finance-research-quality-auditor` when the output should become an actionable or monitorable spot plan.

## Source Matrix

- Company facts and disclosures: KAP, company investor relations.
- Market data and indices: Borsa Istanbul, official index methodology/pages.
- Macro and rates: TCMB, TUIK, Treasury, BRSA, SPK when relevant.
- Ownership and event signals: KAP major shareholder changes, buybacks, investor presentations, debt maturity notes, sector regulation.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

For spot decisions, also include policy fit, liquidity/execution, position lifecycle stage, portfolio impact, thesis risks, stress scenarios, and monitoring triggers when relevant.

## Default Output Shape

Use concise sections unless the user asks for a full report:

1. Executive view
2. Fresh data and source checks
3. Business and financial drivers
4. Valuation and peer context
5. Technical and flow context
6. Scenario map
7. Key uncertainties to verify next
