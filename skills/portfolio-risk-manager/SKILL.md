---
name: portfolio-risk-manager
description: Analyze portfolio construction, position sizing, exposure, concentration, correlation, drawdown, volatility, liquidity, hedging, rebalancing, factor risk, scenario stress tests, and trade risk controls. Use when the user asks about portfolio allocation, how much to size a position, risk/reward, stop levels, hedges, diversification, exposure by asset/sector/currency, or portfolio stress under market scenarios.
---

# Portfolio Risk Manager

## Core Workflow

Use this skill for portfolio-level risk and sizing. If current prices, volatility, correlations, FX, margin rules, liquidity, or portfolio holdings matter, verify current inputs or ask for the missing holdings.

Read `references/analysis-workflow.md` for the full risk framework, sizing rules, stress tests, exposure checklist, and output format.

## Operating Rules

- Separate portfolio facts, assumptions, risk calculations, and judgment.
- Think in downside, liquidity, correlation, and concentration, not only expected return.
- Use ranges when inputs are uncertain.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.
- For spot portfolios, default leverage to zero unless the user explicitly states otherwise. Size to scenario loss and executable exit capacity, not conviction alone.

## Companion Skills

- Use `market-data-source-verifier` for current prices, volatility, FX, liquidity, margin, and event dates.
- Use `technical-flow-analyst` for invalidation zones and `economic-calendar-monitor` for event risk.
- Use relevant market and asset-class skills to understand the drivers behind each position.
- Use `personal-investment-policy`, `position-lifecycle-manager`, `portfolio-accounting-performance`, and `benchmark-attribution-analyst` when the task involves ongoing portfolio management or performance review.
- Use `custody-counterparty-risk-analyst`, `systemic-risk-radar`, `short-crowding-flow-analyst`, and `geopolitical-policy-risk-analyst` when risk comes from venues, broad fragility, crowded positioning, or policy shock.
- Use `scenario-stress-tester`, `market-regime-dashboard`, and `thesis-risk-register` when portfolio risk needs forward-looking monitoring and stress thresholds.
- Use `capital-allocation-cash-manager` when the question is about cash, dry powder, deployment pace, or BIST/crypto bucket weights.
- Use `correlation-exposure-map` when hidden concentration, shared drivers, FX exposure, custody exposure, or liquidity clusters may dominate apparent diversification.
- Use `drawdown-recovery-manager` when current losses require a recovery plan, risk reset, or temporary reduction in new entries.
- Use `sell-discipline-exit-manager` when risk control requires trims, exits, invalidation enforcement, or profit protection.

## Single-Idea To Portfolio Rule

For any individual trade or investment idea, translate the idea into portfolio impact: position size, correlation, liquidity, invalidation, gap risk, event risk, and what would force a reduction or exit.

For BIST and crypto spot portfolios, explicitly check cash weight, single-name/coin concentration, TRY/USD exposure, exchange/venue concentration, custody/wallet concentration, correlation clusters, and exit liquidity.

## Output Discipline

Structure decision-oriented outputs as `Verified Facts`, `Calculations`, `Interpretation`, `Scenarios`, `Uncertainties`, and `Next Checks`.

## Default Output Shape

1. Portfolio snapshot
2. Exposure map
3. Position sizing logic
4. Stress scenarios
5. Risk controls
6. Rebalance or hedge candidates
