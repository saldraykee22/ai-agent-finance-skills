# Finance Agent Orchestration Workflow

## Routing map

- BIST/crypto spot command: `bist-crypto-spot-command-center` as the first route for broad workflow, daily prep, portfolio posture, watchlist review, or action planning.
- Daily BIST/crypto prep: `daily-spot-market-briefing` + `market-regime-dashboard` + `market-breadth-internals-analyst` + `economic-calendar-monitor` + `systemic-risk-radar` + optional watchlist alerts.
- Data infrastructure or repeatable workflow: `market-data-pipeline-architect` + `api-source-integration-planner` + `asset-master-data-manager` + `data-quality-reconciliation-engine`.
- Dashboard or monitoring system: `portfolio-dashboard-designer` + `alert-automation-runbook` + `watchlist-alert-monitor` + `portfolio-recordkeeping-ledger`.
- Research production: `research-production-pipeline-manager` + `financial-report-writer` + `finance-research-quality-auditor` + relevant specialist skills.
- Capital deployment: `capital-allocation-cash-manager` + `personal-investment-policy` + `portfolio-risk-manager` + `correlation-exposure-map` + liquidity/execution + cost/slippage.
- BIST equity spot decision: `personal-investment-policy` + `asset-master-data-manager` when needed + `bist-market-analyst` + `market-data-source-verifier` + `position-lifecycle-manager` + optional `data-quality-reconciliation-engine`, `bist-sector-rotation-analyst`, `market-breadth-internals-analyst`, `relative-strength-momentum-ranker`, `alternative-data-sentiment-analyst`, `earnings-estimate-revision-tracker`, `bist-kap-disclosure-analyst`, `market-session-microstructure-analyst`, `spot-trading-playbook`, `pre-trade-checklist-controller`, `sell-discipline-exit-manager`, `signal-scoring-decision-engine`, `investment-committee-simulator`, `market-manipulation-anomaly-detector`, `finance-research-quality-auditor`, `thesis-risk-register`, `scenario-stress-tester`, `watchlist-alert-monitor`, `financial-statement-analyst`, `valuation-modeling-analyst`, `technical-flow-analyst`, `portfolio-risk-manager`, `correlation-exposure-map`, `liquidity-execution-analyst`, `broker-exchange-venue-selector`, `cost-tax-slippage-analyst`, `corporate-actions-analyst`, `insider-ownership-flow-analyst`, `distressed-balance-sheet-risk`, `geopolitical-policy-risk-analyst`, `earnings-call-transcript-analyst`, `decision-quality-behavioral-analyst`.
- US equity: `us-equity-market-analyst` + verifier + optional financials, valuation, options, sector, event, portfolio.
- German equity: `germany-equity-market-analyst` + verifier + optional financials, valuation, sector, event, portfolio.
- Crypto spot decision: `personal-investment-policy` + `asset-master-data-manager` when contract or wrapper identity matters + `crypto-market-analyst` + verifier + `position-lifecycle-manager` + optional `data-quality-reconciliation-engine`, `crypto-narrative-rotation-analyst`, `market-breadth-internals-analyst`, `relative-strength-momentum-ranker`, `alternative-data-sentiment-analyst`, `crypto-tokenomics-supply-analyst`, `stablecoin-liquidity-risk-analyst`, `market-session-microstructure-analyst`, `spot-trading-playbook`, `pre-trade-checklist-controller`, `sell-discipline-exit-manager`, `signal-scoring-decision-engine`, `investment-committee-simulator`, `market-manipulation-anomaly-detector`, `finance-research-quality-auditor`, `thesis-risk-register`, `scenario-stress-tester`, `watchlist-alert-monitor`, `crypto-onchain-flow-analyst`, `custody-counterparty-risk-analyst`, `security-wallet-operations-analyst`, `broker-exchange-venue-selector`, `short-crowding-flow-analyst`, `etf-fund-flow-analyst`, derivatives, technicals, token/corporate-actions unlock logic, portfolio, liquidity/execution, cost/slippage, decision quality.
- Macro/cross-asset: `macro-market-strategist` + fixed income/FX + commodities + verifier.
- Complete company report: market skill + verifier + financial statements + valuation + sector + technicals + report writer.
- Spot trade idea: policy + market skill + verifier + technicals + portfolio risk + correlation map + liquidity/execution + venue selection + cost/slippage + position lifecycle + event calendar + decision quality + signal score + pre-trade checklist + exit discipline.
- Watchlist/screen: screener + verifier + sector or narrative rotation + market breadth + relative strength + alternative data + quant/factor + market skill for final names.
- Event reaction: news/event + verifier + relevant market skill + corporate actions if applicable.
- Derivatives/hedge: options/derivatives + verifier + portfolio risk + technicals.
- Performance review: portfolio accounting + portfolio ledger + benchmark attribution + trade journal + execution-quality TCA + decision quality.
- Trade operations: `trade-blotter-operations-controller` + `pre-trade-checklist-controller` + `portfolio-recordkeeping-ledger` + `execution-quality-tca-analyst` + `trade-journal-reviewer`.
- Custody/venue concern: custody/counterparty + security wallet operations + broker/exchange venue selector + verifier + relevant market skill + portfolio risk.
- Crowded positioning concern: short/crowding + technicals + portfolio risk + relevant market skill.
- Market prep: market-regime dashboard + screener/watchlist + calendar + systemic risk.
- Quality audit: research-quality auditor + verifier + relevant specialist skills.
- Living thesis: thesis-risk register + watchlist-alert monitor + position lifecycle.
- Stress review: scenario-stress tester + portfolio risk + liquidity/execution + systemic risk.
- Drawdown recovery: `drawdown-recovery-manager` + `correlation-exposure-map` + `sell-discipline-exit-manager` + `portfolio-risk-manager` + `trade-journal-reviewer`.
- Model or scoring audit: `model-assumption-validator` + relevant model owner such as valuation, quant/factor, scenario stress, or signal scoring.

## Quality gates

1. Identify the instrument precisely: ticker, exchange, ISIN/CIK/contract address/contract month where relevant.
2. Decide whether data is current-sensitive. If yes, verify source and timestamp before interpretation.
3. Separate facts, calculations, interpretation, scenarios, uncertainties, and next checks.
4. For BIST/crypto spot decisions, include a policy-fit gate, liquidity/execution check, net-cost check, lifecycle stage, and portfolio impact.
5. For actionable ideas, create or update a thesis register, scenario stress, and monitoring triggers when the user needs ongoing management.
6. Use the minimum number of specialist skills needed; add more only when they change the decision.
7. Resolve conflicts by source quality and timestamp, not by confidence of prose.
8. For mixed-market requests, normalize identifiers and currency before ranking.
9. For execution-ready ideas, require a pre-trade checklist and make blocking issues explicit.
10. When several skills disagree, use the signal scoring engine and committee simulator to expose tradeoffs instead of hiding them.
11. For repeatable workflows, define data source, schema, refresh cadence, dashboard view, alert route, and archive location before relying on outputs.
12. For portfolio performance, reconcile ledger, blotter, fills, fees, cash, and holdings before interpreting returns.
13. For exits and drawdowns, separate thesis failure, risk budget breach, liquidity shock, and behavioral error before deciding.
14. For crypto spot, check venue, custody, wallet operations, and stablecoin rails before increasing exposure.

## Synthesis rules

- Put the user's actual decision question first.
- State the route: which skills were used and why.
- Collapse overlapping findings into a single thesis.
- Include scenario triggers and invalidation points.
- Keep unresolved data gaps explicit.

## Output format

```text
Objective:
- ...

Skill route:
- ...

Verified facts:
- ...

Calculations:
- ...

Interpretation:
- ...

Spot decision gate:
- Policy fit:
- Lifecycle stage:
- Liquidity/execution:
- Net cost/slippage:
- Portfolio impact:
- Correlation/exposure:
- Behavioral flags:
- Signal score:
- Pre-trade verdict:

Scenarios:
- Base:
- Upside:
- Downside:

Monitoring and quality:
- Research audit:
- Thesis register:
- Stress test:
- Alerts:
- Spot playbook:
- Exit discipline:
- Execution quality / TCA:
- Ledger / blotter status:
- Dashboard / production handoff:

Uncertainties:
- ...

Next checks:
- ...
```
