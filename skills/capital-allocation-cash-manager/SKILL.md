---
name: capital-allocation-cash-manager
description: Manage spot portfolio capital allocation, cash buffers, dry powder, deployment pace, BIST/crypto weighting, currency buckets, concentration limits, staged buying, rebalancing, and opportunity budgeting. Use when the user asks how much cash to keep, how to allocate between BIST and crypto, how much to deploy into a setup, or how to manage capital across spot opportunities.
---

# Capital Allocation Cash Manager

## Core Workflow

Use this skill to decide how much capital should be exposed, reserved, or deployed. Read `references/analysis-workflow.md` for allocation buckets, cash rules, deployment pacing, and output format.

## Operating Rules

- Separate cash policy, opportunity budget, risk budget, and execution budget.
- For BIST/crypto spot portfolios, track TRY/USD/stablecoin exposure, exchange concentration, and exit liquidity.
- Use `stablecoin-liquidity-risk-analyst` when stablecoin buckets are part of cash or dry powder.
- Prefer staged deployment when regime, liquidity, or thesis confirmation is incomplete.
- Do not add generic boilerplate caveats. Keep output analytical, direct, and operational.
- Match the user's language.

## Default Output Shape

1. Capital snapshot
2. Cash and dry powder
3. Allocation buckets
4. Deployment rules
5. Rebalance triggers
6. Constraints
