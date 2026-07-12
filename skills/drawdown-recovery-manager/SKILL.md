---
name: drawdown-recovery-manager
description: Build drawdown recovery plans for spot portfolios by diagnosing losses, exposure clusters, cash use, risk breaches, behavioral errors, liquidity issues, market regime shifts, and recovery pacing. Use when the user asks how to recover after losses, reduce drawdown, stop bleeding, reset process, rebuild confidence, or decide what to cut after a BIST or crypto portfolio decline.
---

# Drawdown Recovery Manager

## Core Rule

Recovery starts with exposure and process diagnosis, not with making the loss back quickly. Reduce fragility before increasing risk.

## Workflow

1. Quantify drawdown by position, market, sector, narrative, FX bucket, and time period.
2. Separate market beta loss, bad thesis, poor execution, overconcentration, liquidity shock, and behavioral mistakes.
3. Identify forced actions: cut broken theses, reduce correlated exposure, rebuild cash, stop new entries, or tighten pre-trade gates.
4. Define recovery pace: pause, stabilize, selective redeploy, or normal risk.
5. Route to `correlation-exposure-map`, `portfolio-risk-manager`, `sell-discipline-exit-manager`, `trade-journal-reviewer`, and `capital-allocation-cash-manager`.

## Output

Return `Drawdown Map`, `Loss Attribution`, `Control Breaches`, `Immediate Actions`, `Recovery Plan`, `Behavioral Fixes`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for recovery framework.

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
