---
name: spot-trading-playbook
description: Structure BIST and crypto spot trade setups with entry trigger, invalidation, position sizing, liquidity, cost/slippage, execution plan, monitoring, add/trim/exit rules, and post-trade review. Use when the user asks to turn an analysis into a spot trade plan, compare setups, define buy/add/sell rules, or create repeatable BIST/crypto spot playbooks.
---

# Spot Trading Playbook

## Core Workflow

Use this skill as the spot trade action template. Read `references/analysis-workflow.md` for setup types, required fields, and BIST/crypto-specific checks.

## Operating Rules

- Default to spot only; do not introduce leverage unless explicitly requested.
- Every setup must include trigger, invalidation, size, liquidity, cost/slippage, and review plan.
- Use `pre-trade-checklist-controller` as the final gate before treating the setup as execution-ready.
- Use `signal-scoring-decision-engine` when the setup needs a ranked readiness score across multiple inputs.
- Use `market-manipulation-anomaly-detector` before chasing sharp BIST or crypto moves with abnormal volume, thin books, or weak catalyst evidence.
- Prefer waiting for a defined trigger over chasing unconfirmed moves.
- Do not add generic boilerplate caveats. Keep output analytical, direct, and actionable.
- Match the user's language.
- Keep recommendation, execution readiness, and execution authorization as three separate states. A completed trade card never authorizes an MCP order call.

## Default Output Shape

1. Setup type
2. Entry trigger
3. Invalidation
4. Size and execution
5. Monitoring plan
6. Add/trim/exit rules
7. Pre-trade gate verdict

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
