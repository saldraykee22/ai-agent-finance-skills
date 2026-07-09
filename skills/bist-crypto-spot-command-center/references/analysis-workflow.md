# BIST and Crypto Spot Command Workflow

## Default user profile

- Primary markets: BIST equities and crypto spot.
- Instrument: spot only unless user explicitly asks otherwise.
- Objective: decision-ready, source-grounded, repeatable market workflow.
- Secondary markets: US, Germany, FX, rates, commodities, and ETFs only when they affect BIST/crypto or portfolio regime.

## Command routes

- Daily prep: `daily-spot-market-briefing` + `market-regime-dashboard` + `market-breadth-internals-analyst` + `economic-calendar-monitor` + `systemic-risk-radar` + rotation and relative strength checks when watchlists need priority.
- Daily production: `research-production-pipeline-manager` + `financial-report-writer` when the daily prep should become a repeatable morning note.
- Single BIST asset: `asset-master-data-manager` if identity is ambiguous + `bist-market-analyst` + `market-data-source-verifier` + optional `data-quality-reconciliation-engine`, `bist-sector-rotation-analyst`, `market-breadth-internals-analyst`, `relative-strength-momentum-ranker`, `alternative-data-sentiment-analyst`, `earnings-estimate-revision-tracker`, `bist-kap-disclosure-analyst`, financials, valuation, technicals, liquidity, policy, thesis register.
- Single crypto asset: `asset-master-data-manager` if contract, chain, or wrapper can matter + `crypto-market-analyst` + `market-data-source-verifier` + optional `data-quality-reconciliation-engine`, `crypto-narrative-rotation-analyst`, `market-breadth-internals-analyst`, `relative-strength-momentum-ranker`, `alternative-data-sentiment-analyst`, `crypto-tokenomics-supply-analyst`, `stablecoin-liquidity-risk-analyst`, on-chain, custody, wallet/security operations, crowding, technicals, liquidity, policy, thesis register.
- Decision synthesis: `signal-scoring-decision-engine` + `investment-committee-simulator` when multiple specialist outputs must become a single decision.
- Trade setup: `spot-trading-playbook` + `position-lifecycle-manager` + `sell-discipline-exit-manager` + `liquidity-execution-analyst` + `broker-exchange-venue-selector` + `market-session-microstructure-analyst` + `cost-tax-slippage-analyst` + `pre-trade-checklist-controller`.
- Portfolio posture: `portfolio-risk-manager` + `correlation-exposure-map` + `capital-allocation-cash-manager` + `portfolio-accounting-performance` + `benchmark-attribution-analyst`.
- Portfolio dashboard: `portfolio-dashboard-designer` + `portfolio-recordkeeping-ledger` + `alert-automation-runbook` when the user wants ongoing monitoring.
- Watchlist: `market-screener-watchlist` + `relative-strength-momentum-ranker` + `watchlist-alert-monitor` + `alert-automation-runbook` + `thesis-risk-register`.
- Abnormal move: `market-manipulation-anomaly-detector` + source verifier before chasing a sharp BIST or crypto move.
- Quality review: `finance-research-quality-auditor` + `decision-quality-behavioral-analyst` + `investment-committee-simulator`.
- Post-trade review: `trade-blotter-operations-controller` + `portfolio-recordkeeping-ledger` + `trade-journal-reviewer` + `execution-quality-tca-analyst`.
- Data system: `market-data-pipeline-architect` + `api-source-integration-planner` + `data-quality-reconciliation-engine` when the workflow must be automated or repeated.
- Drawdown recovery: `drawdown-recovery-manager` + `sell-discipline-exit-manager` + `correlation-exposure-map` when portfolio damage or repeated losses require a reset.
- Crypto operations: `security-wallet-operations-analyst` + `broker-exchange-venue-selector` + `custody-counterparty-risk-analyst` when venue, wallet, transfer, or custody risk can affect the spot plan.

## Decision gate

```text
Proceed:
- Data verified.
- Policy fit clear.
- Liquidity and costs acceptable.
- Thesis and invalidation defined.
- Portfolio impact acceptable.
- Correlation and hidden exposure acceptable.
- Monitoring triggers defined.
- Pre-trade checklist passed when action is execution-ready.
- Ledger and blotter route defined after execution.

Wait:
- Good idea but trigger missing, regime poor, event ahead, liquidity weak, or cost too high.

Reject:
- Data conflict, no invalidation, poor liquidity, outside policy, excessive concentration, or thesis broken.
```

## Output format

```text
Objective:
- ...

Market posture:
- BIST:
- Crypto:
- Global:

Skill route:
- ...

Spot decision gate:
- Policy:
- Data:
- Liquidity:
- Cost:
- Thesis:
- Portfolio:
- Correlation:
- Behavior:
- Signal score:
- Pre-trade verdict:
- Ledger/blotter:
- Dashboard/alerts:

Action plan:
- Proceed / Wait / Reject:
- Entry/monitor/review:

Next checks:
- ...
```
