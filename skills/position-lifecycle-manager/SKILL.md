---
name: position-lifecycle-manager
description: Manage a spot position from idea to watchlist, entry, add, trim, hold, exit, and post-mortem. Use when the user asks how to manage a BIST or crypto spot position, whether to enter/add/reduce/exit, how to define invalidation, how to monitor catalysts, or how to turn an analysis into a position plan.
---

# Position Lifecycle Manager

## Core Workflow

Use this skill to turn research into a controlled position lifecycle. Read `references/analysis-workflow.md` for stage gates, action rules, and monitoring templates.

## Operating Rules

- Every position must have thesis, trigger, invalidation, size logic, liquidity check, catalyst map, and review date.
- For spot trades, do not rely on liquidation/funding mechanics as the core risk control.
- Separate watchlist, entry, add, trim, hold, exit, and post-mortem decisions.
- Use `thesis-risk-register`, `watchlist-alert-monitor`, `scenario-stress-tester`, and `spot-trading-playbook` for complete ongoing management.
- Use `sell-discipline-exit-manager` when the position is extended, thesis is impaired, trim rules are needed, or the user asks whether to sell or hold.
- Use `drawdown-recovery-manager` when a position or group of positions has caused portfolio-level damage.
- Use `broker-exchange-venue-selector` and `security-wallet-operations-analyst` when venue, wallet, custody, or transfer operations affect crypto spot management.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Lifecycle stage
2. Thesis and trigger
3. Invalidation
4. Size and liquidity
5. Monitor list
6. Next action

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
