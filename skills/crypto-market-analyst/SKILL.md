---
name: crypto-market-analyst
description: Analyze crypto assets, spot and derivatives markets, tokenomics, on-chain data, DeFi protocols, exchange liquidity, funding, open interest, unlocks, catalysts, and market structure. Use when the user asks about Bitcoin, Ethereum, altcoins, crypto narratives, futures positioning, token research, exchange data, on-chain flows, or crypto trading/investment research.
---

# Crypto Market Analyst

## Core Workflow

Use this skill for crypto market research across spot, derivatives, on-chain, protocol, and narrative layers. If the task depends on price, funding, open interest, protocol TVL, token supply, exchange listings, unlock schedules, governance, exploits, or regulatory news, verify with current sources before analyzing.

Read `references/analysis-workflow.md` for the detailed crypto workflow, source hierarchy, checklist, output format, and common failure modes.

## Operating Rules

- Separate market facts, chain facts, tokenomics, interpretation, and unresolved uncertainties.
- Prefer primary or near-primary sources: project docs, block explorers, governance forums, exchange APIs/pages, protocol dashboards, official announcements, and reputable data aggregators.
- Check chain, contract address, ticker collisions, wrapped assets, bridged supply, and exchange-specific symbols before analysis.
- Do not add generic boilerplate caveats. Keep the output analytical, source-grounded, and direct.
- Match the user's language. If the user writes in Turkish, produce Turkish output.

## Companion Skills

- Use `market-data-source-verifier` for price, liquidity, contract address, token supply, unlocks, exchange data, and protocol metrics.
- Use `asset-master-data-manager` when ticker collision, contract address, chain, bridge, wrapped token, or venue identity can change the analysis.
- Use `data-quality-reconciliation-engine` when price, supply, TVL, exchange volume, unlock, or on-chain sources disagree.
- Use `crypto-narrative-rotation-analyst` and `relative-strength-momentum-ranker` when narrative leadership, alt rotation, BTC/ETH relative strength, or watchlist priority matters.
- Use `crypto-tokenomics-supply-analyst` when supply, FDV, unlocks, vesting, emissions, burns, or staking dilution drive the thesis.
- Use `options-derivatives-analyst` for perps, funding, basis, OI, liquidation zones, and derivatives-led moves.
- Use `technical-flow-analyst`, `portfolio-risk-manager`, and `corporate-actions-analyst` for setups, sizing, and unlock/emission/burn analysis.
- Use `personal-investment-policy`, `position-lifecycle-manager`, `liquidity-execution-analyst`, and `cost-tax-slippage-analyst` when crypto analysis leads to a spot buy/add/trim/exit decision.
- Use `crypto-onchain-flow-analyst`, `custody-counterparty-risk-analyst`, `short-crowding-flow-analyst`, and `etf-fund-flow-analyst` when on-chain flows, exchange/custody risk, positioning, or ETF/fund flows can change the spot thesis.
- Use `stablecoin-liquidity-risk-analyst` when stablecoin peg, pair depth, liquidity rails, or cash bucket risk matters.
- Use `market-session-microstructure-analyst` when exchange session behavior, weekend liquidity, maintenance, order book depth, or pair microstructure affects execution.
- Use `pre-trade-checklist-controller` before a crypto idea is treated as execution-ready.
- Use `signal-scoring-decision-engine` and `investment-committee-simulator` when several crypto signals must be collapsed into one decision.
- Use `market-manipulation-anomaly-detector` when a token move may reflect fake liquidity, social pump, wash trading, venue divergence, or abnormal pre-news activity.
- Use `spot-trading-playbook`, `thesis-risk-register`, `scenario-stress-tester`, `watchlist-alert-monitor`, and `finance-research-quality-auditor` when the output should become an actionable or monitorable crypto spot plan.

## Source Matrix

- Identity and supply: block explorers, protocol docs, official token contracts.
- Market data: exchange pages/APIs, CoinGecko/CoinMarketCap only after identity checks.
- Protocol traction: DefiLlama, Token Terminal, Dune/Artemis-style dashboards, governance forums.
- Flow and custody: exchange wallets, stablecoin liquidity, bridge activity, ETF issuer holdings, exchange status pages, proof/reserve signals where available.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

For spot decisions, also include policy fit, exchange/venue liquidity, transfer/fee/slippage cost, lifecycle stage, portfolio impact, thesis risks, stress scenarios, and monitoring triggers when relevant.

## Default Output Shape

Use concise sections unless the user asks for a full report:

1. Executive view
2. Fresh market data
3. Derivatives and liquidity
4. On-chain/protocol context
5. Tokenomics and unlocks
6. Narrative and catalyst map
7. Scenarios and invalidation points
