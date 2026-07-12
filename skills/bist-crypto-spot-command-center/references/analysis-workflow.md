# BIST and crypto spot routes

## Primary routes

| Objective | Start with | Add only when needed |
| --- | --- | --- |
| Daily preparation | `daily-spot-market-briefing` | Regime, breadth, calendar, systemic risk, sector/narrative rotation |
| Single BIST asset | `bist-market-analyst` | KAP, statements, valuation, sector, ownership, technicals |
| Single crypto asset | `crypto-market-analyst` | Tokenomics, on-chain, narrative, stablecoin, custody, technicals |
| Watchlist | `market-screener-watchlist` | Relative strength, breadth, sector/narrative rotation, alerts |
| Portfolio posture | `portfolio-risk-manager` | Correlation, capital allocation, performance, stress |
| Trade setup | `spot-trading-playbook` | Lifecycle, exit discipline, liquidity, venue, costs, session microstructure |
| Post-trade review | `trade-journal-reviewer` | Blotter, ledger, accounting, execution TCA |
| Drawdown recovery | `drawdown-recovery-manager` | Correlation, sell discipline, portfolio risk, behavioral review |
| Data or dashboard system | `market-data-pipeline-architect` | API integration, asset master, reconciliation, dashboard, alerts |

## Conditional gates

- Identity ambiguity: `asset-master-data-manager`.
- Any current-sensitive claim: `market-data-source-verifier`.
- Material source conflict: `data-quality-reconciliation-engine`.
- Abnormal price/volume or suspicious liquidity: `market-manipulation-anomaly-detector`.
- Multiple conflicting signals: `signal-scoring-decision-engine`; use `investment-committee-simulator` when the thesis needs an adversarial challenge.
- Execution-ready action: `liquidity-execution-analyst`, `cost-tax-slippage-analyst`, and `pre-trade-checklist-controller`.
- Ongoing position: `position-lifecycle-manager`, `thesis-risk-register`, and `watchlist-alert-monitor`.
- Venue, transfer, or custody risk: `broker-exchange-venue-selector`, `custody-counterparty-risk-analyst`, or `security-wallet-operations-analyst` according to the actual issue.

## Spot decision gate

- `Proceed`: verified data, policy fit, acceptable liquidity/cost, defined thesis and invalidation, acceptable portfolio impact, and a monitoring plan.
- `Wait`: thesis may be valid but a trigger, source, event outcome, liquidity condition, or price condition is missing.
- `Reject`: identity/data conflict, no falsifiable thesis, unacceptable liquidity/cost, policy breach, excessive concentration, or broken thesis.

Never convert a research-only request into a trade recommendation. Never advance to execution while a gate is unresolved.
