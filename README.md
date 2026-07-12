# AI Agent Finance Skills

A collection of **77 finance-focused AI agent skills** designed for use with AI coding agents (OpenAI Codex, Claude Code, etc.). These skills cover the full spectrum of financial analysis, trading, risk management, and portfolio operations.

## Skill Categories

### 📊 Market Analysis
| Skill | Description |
|-------|-------------|
| `us-equity-market-analyst` | US equities analysis and research |
| `germany-equity-market-analyst` | German equity market analysis |
| `bist-market-analyst` | Borsa Istanbul equities and indices |
| `commodities-market-analyst` | Commodities market research |
| `crypto-market-analyst` | Cryptocurrency market analysis |
| `fixed-income-fx-analyst` | Fixed income and FX markets |
| `bist-sector-rotation-analyst` | Turkish sector rotation tracking |
| `crypto-narrative-rotation-analyst` | Crypto narrative rotation analysis |
| `sector-industry-analyst` | Sector and industry analysis |
| `macro-market-strategist` | Macroeconomic strategy |
| `relative-strength-momentum-ranker` | RS and momentum ranking |
| `market-breadth-internals-analyst` | Market breadth and internals |
| `economic-calendar-monitor` | Economic events calendar |

### 📄 Financial Statements & Valuation
| Skill | Description |
|-------|-------------|
| `financial-statement-analyst` | Financial statement analysis |
| `valuation-modeling-analyst` | Valuation and modeling |
| `financial-report-writer` | Financial report generation |
| `bist-kap-disclosure-analyst` | KAP disclosure analysis (Turkey) |
| `earnings-call-transcript-analyst` | Earnings call analysis |
| `earnings-estimate-revision-tracker` | Estimate revision tracking |
| `quant-factor-analyst` | Quantitative factor analysis |

### 📈 Technical & Flow Analysis
| Skill | Description |
|-------|-------------|
| `technical-flow-analyst` | Technical analysis and flows |
| `market-session-microstructure-analyst` | Market microstructure |
| `execution-quality-tca-analyst` | Transaction cost analysis |
| `liquidity-execution-analyst` | Liquidity and execution |
| `market-manipulation-anomaly-detector` | Anomaly detection |
| `options-derivatives-analyst` | Options and derivatives |

### 🛡️ Risk & Portfolio Management
| Skill | Description |
|-------|-------------|
| `portfolio-risk-manager` | Portfolio risk management |
| `portfolio-accounting-performance` | Portfolio accounting and performance |
| `portfolio-dashboard-designer` | Portfolio dashboard design |
| `portfolio-recordkeeping-ledger` | Portfolio recordkeeping |
| `scenario-stress-tester` | Scenario and stress testing |
| `systemic-risk-radar` | Systemic risk monitoring |
| `drawdown-recovery-manager` | Drawdown and recovery |
| `correlation-exposure-map` | Correlation and exposure mapping |
| `distressed-balance-sheet-risk` | Distressed balance sheet analysis |
| `geopolitical-policy-risk-analyst` | Geopolitical and policy risk |
| `custody-counterparty-risk-analyst` | Custody and counterparty risk |
| `thesis-risk-register` | Investment thesis risk tracking |
| `decision-quality-behavioral-analyst` | Behavioral decision quality |

### 💰 Capital Allocation & Trading
| Skill | Description |
|-------|-------------|
| `capital-allocation-cash-manager` | Capital allocation and cash management |
| `position-lifecycle-manager` | Position lifecycle management |
| `pre-trade-checklist-controller` | Pre-trade checklist |
| `spot-trading-playbook` | Spot trading playbook |
| `sell-discipline-exit-manager` | Sell discipline and exits |
| `trade-blotter-operations-controller` | Trade blotter operations |
| `trade-journal-reviewer` | Trade journal review |
| `signal-scoring-decision-engine` | Signal scoring and decisions |
| `investment-committee-simulator` | Investment committee simulation |
| `cost-tax-slippage-analyst` | Cost, tax and slippage analysis |
| `broker-exchange-venue-selector` | Broker/venue selection |

### 🔍 Research & Data
| Skill | Description |
|-------|-------------|
| `financial-news-event-analyst` | Financial news and events |
| `alternative-data-sentiment-analyst` | Alternative data and sentiment |
| `market-data-source-verifier` | Market data source verification |
| `data-quality-reconciliation-engine` | Data quality and reconciliation |
| `market-data-pipeline-architect` | Data pipeline architecture |
| `research-production-pipeline-manager` | Research pipeline management |
| `finance-research-quality-auditor` | Research quality auditing |
| `model-assumption-validator` | Model assumption validation |
| `benchmark-attribution-analyst` | Benchmark attribution |

### 🤖 Specialized Domains
| Skill | Description |
|-------|-------------|
| `asset-master-data-manager` | Asset master data management |
| `corporate-actions-analyst` | Corporate actions analysis |
| `insider-ownership-flow-analyst` | Insider ownership and flows |
| `short-crowding-flow-analyst` | Short interest and crowding |
| `etf-fund-flow-analyst` | ETF and fund flow analysis |
| `market-screener-watchlist` | Market screening and watchlists |
| `watchlist-alert-monitor` | Alert monitoring |
| `daily-spot-market-briefing` | Daily market briefing |
| `market-regime-dashboard` | Market regime dashboard |
| `personal-investment-policy` | Personal investment policy |

### 🌐 Crypto & Digital Assets
| Skill | Description |
|-------|-------------|
| `crypto-onchain-flow-analyst` | On-chain flow analysis |
| `crypto-tokenomics-supply-analyst` | Tokenomics and supply analysis |
| `stablecoin-liquidity-risk-analyst` | Stablecoin liquidity risk |
| `security-wallet-operations-analyst` | Security and wallet operations |
| `bist-crypto-spot-command-center` | BIST/crypto spot command center |

### 🔧 Orchestration & Automation
| Skill | Description |
|-------|-------------|
| `finance-agent-orchestrator` | Multi-agent finance orchestration |
| `alert-automation-runbook` | Alert automation runbook |
| `api-source-integration-planner` | API source integration planning |

## Skill Structure

Each skill follows the standard agent skill format:

```
skills/
├── <skill-name>/
│   ├── SKILL.md              # Main skill instructions
│   ├── agents/
│   │   └── openai.yaml       # OpenAI Codex metadata
│   └── references/           # Reference documents, workflows, examples
│       └── *.md
```

## Usage

These skills work with any AI agent that supports the Agent Skills standard (OpenAI Codex, Claude Code, etc.).

### Installation

```bash
# Clone the repository
git clone https://github.com/saldraykee22/ai-agent-finance-skills.git

# Install all skills into a platform's global directory
python scripts/install_skills.py --platform codex
python scripts/install_skills.py --platform hermes
python scripts/install_skills.py --platform antigravity
```

Use `--dry-run` before replacing an installation. See [Platform setup](docs/platform-setup.md) for workspace installs and MCP configuration.

### Invoking a Skill

In your AI agent, use the `$` prefix:

```
$us-equity-market-analyst Analyze NVDA with focus on data center revenue trends
```

Or let the agent auto-detect the relevant skill.

## Preferred MCP Data Sources

- [`saidsurucu/borsa-mcp`](https://github.com/saidsurucu/borsa-mcp): preferred structured source for BIST, KAP, Turkish macro/EVDS, financial statements, indices, TEFAS, FX, commodities, and supporting US-market research.
- [`saldraykee22/binance-trader-mcp`](https://github.com/saldraykee22/binance-trader-mcp): preferred source for Binance spot market data, exchange filters, order books, account/order review, and explicitly authorized spot execution.

Use `$api-source-integration-planner` to discover tools by capability across Hermes Agent, Codex, and Antigravity. The skills separate public research, private account reads, and order-changing tools into distinct permission tiers. A trade analysis or execution-ready plan does not by itself authorize an order.

## Professional Decision Standard

Action-oriented research separates thesis attractiveness from execution readiness, applies hard data/liquidity/risk gates, and preserves a reproducible evidence ledger. BIST analysis identifies inflation-accounting and consolidation basis; crypto analysis distinguishes circulating value, FDV, liquid float, emissions, and token-holder value accrual. Position sizes must survive both the planned invalidation and a realistic adverse-gap scenario.

Validate these cross-skill contracts with:

```bash
python scripts/validate_professional_contract.py
python scripts/evaluate_skill_routing.py
python scripts/audit_collection_coverage.py
```

The routing evaluation uses realistic boundary prompts across BIST, crypto, portfolio risk, execution, data quality, macro, and global markets. It requires at least 90% top-choice accuracy and 95% top-three coverage while rejecting highly overlapping descriptions.

## License

MIT
