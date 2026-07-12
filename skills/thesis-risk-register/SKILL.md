---
name: thesis-risk-register
description: Build and maintain an investment thesis risk register with assumptions, evidence, catalysts, risks, invalidation triggers, monitoring indicators, position actions, and review dates. Use when the user asks to track a BIST or crypto thesis, define what would prove a trade wrong, monitor a position, or convert research into a living risk register.
---

# Thesis Risk Register

## Core Workflow

Use this skill to make a thesis monitorable. Read `references/analysis-workflow.md` for register fields, trigger types, and update workflow.

## Operating Rules

- Every thesis must have assumptions, evidence, risks, invalidation, and review triggers.
- Separate thesis risk from execution, liquidity, custody, and behavioral risk.
- For spot positions, map each trigger to hold/add/trim/exit/review actions.
- Do not add generic boilerplate caveats. Keep output analytical, direct, and operational.
- Match the user's language.

## Default Output Shape

1. Thesis summary
2. Assumption register
3. Risk register
4. Invalidation triggers
5. Monitoring cadence
6. Action map

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
