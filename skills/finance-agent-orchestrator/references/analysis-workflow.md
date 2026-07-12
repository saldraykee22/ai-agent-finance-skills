# Finance orchestration routes

## Route selection

Choose one primary route from the table. Add conditional skills only when the condition is present.

| Request | Primary skill | Conditional additions |
| --- | --- | --- |
| Broad BIST/crypto spot workflow | `bist-crypto-spot-command-center` | Use its routing reference |
| BIST equity | `bist-market-analyst` | KAP, statements, valuation, sector, technical, ownership, distress |
| Crypto asset | `crypto-market-analyst` | Tokenomics, on-chain, stablecoin, custody, narrative, derivatives |
| US equity | `us-equity-market-analyst` | Statements, valuation, sector, event, options |
| German equity | `germany-equity-market-analyst` | Statements, valuation, sector, event |
| Macro/cross-asset | `macro-market-strategist` | Rates/FX, commodities, geopolitical risk |
| Screen/watchlist | `market-screener-watchlist` | Relative strength, factor, breadth, sector/narrative |
| Portfolio construction/risk | `portfolio-risk-manager` | Correlation, capital allocation, stress, liquidity |
| Performance review | `portfolio-accounting-performance` | Ledger, attribution, journal, execution TCA |
| Event reaction | `financial-news-event-analyst` | Corporate actions and relevant market skill |
| Data/research system | `market-data-pipeline-architect` | API integration, asset master, reconciliation, production |

## Cross-cutting gates

- Add `asset-master-data-manager` only when identity, venue, contract, wrapper, currency, or identifier ambiguity matters.
- Add `market-data-source-verifier` whenever current prices, filings, macro releases, supply, flows, news, or corporate actions affect the answer.
- Add `data-quality-reconciliation-engine` only when material sources disagree.
- Add `scenario-stress-tester` for nonlinear downside or portfolio-impact questions.
- Add `signal-scoring-decision-engine` or `investment-committee-simulator` only when several credible signals conflict or readiness must be challenged.
- Add `finance-research-quality-auditor` for publication, high-stakes decisions, or an explicit auditâ€”not every analysis.

## Lifecycle gates

Move through only the stages the user requests:

1. Research: market/domain primary skill plus verification.
2. Decision: `personal-investment-policy`, `portfolio-risk-manager`, and relevant scenario checks.
3. Execution: `liquidity-execution-analyst`, `cost-tax-slippage-analyst`, then `pre-trade-checklist-controller`.
4. Position management: `position-lifecycle-manager`, `sell-discipline-exit-manager`, and `thesis-risk-register`.
5. Monitoring: `watchlist-alert-monitor` or `alert-automation-runbook`.
6. Record/review: ledger, blotter, accounting, TCA, and journal skills as applicable.

## Synthesis contract

Separate verified facts, calculations, interpretation, scenarios, uncertainties, and next checks. State why each selected specialist was necessary. If a specialist did not change the conclusion, omit its detail. Resolve conflicts by authority, methodology, coverage, and timestamp.
