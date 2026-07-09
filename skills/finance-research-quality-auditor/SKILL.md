---
name: finance-research-quality-auditor
description: Audit finance research for evidence quality, source freshness, calculation correctness, unsupported claims, missing scenario analysis, stale market data, weak assumptions, and decision readiness. Use when the user asks to review an analysis, check whether a finance conclusion is reliable, improve research quality, or validate a BIST/crypto spot decision before action.
---

# Finance Research Quality Auditor

## Core Workflow

Use this skill as a final research quality gate. Read `references/analysis-workflow.md` for audit checklist, scoring, evidence tiers, and output format.

## Operating Rules

- Audit facts, sources, calculations, assumptions, scenarios, and actionability separately.
- Treat current-sensitive data as invalid unless timestamped or clearly marked stale.
- For BIST and crypto spot decisions, require policy fit, liquidity, cost/slippage, invalidation, and portfolio impact.
- Do not add generic boilerplate caveats. Keep output analytical, direct, and corrective.
- Match the user's language.

## Default Output Shape

1. Audit verdict
2. Evidence gaps
3. Calculation/logic issues
4. Missing decision gates
5. Required fixes
6. Clean version if requested
