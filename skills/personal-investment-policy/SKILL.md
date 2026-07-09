---
name: personal-investment-policy
description: Define and apply a personal investment policy for spot trading and investing, especially BIST and crypto first, with clear universe, risk limits, position sizing rules, time horizons, decision criteria, review cadence, and prohibited behaviors. Use when the user asks to standardize their investing style, create personal rules, evaluate whether a trade fits their process, or make finance agents behave consistently with a spot-only BIST/crypto-priority workflow.
---

# Personal Investment Policy

## Core Workflow

Use this skill as the user's finance operating policy. Treat the default profile as BIST and crypto priority, spot transactions only, no leverage unless the user explicitly overrides it. Read `references/analysis-workflow.md` for policy structure, decision gates, and rule templates.

## Operating Rules

- Convert broad market ideas into policy-fit checks before detailed analysis.
- Prefer spot risk, cash allocation, liquidity, invalidation, and review cadence over leverage mechanics.
- Use `bist-crypto-spot-command-center` for broad workflows and `capital-allocation-cash-manager` for cash/deployment rules.
- If a user asks for a trade, identify whether it is allowed, conditionally allowed, or outside policy.
- Do not add generic boilerplate caveats. Keep the output analytical, direct, and process-focused.
- Match the user's language.

## Default Output Shape

1. Policy fit
2. Allowed universe and horizon
3. Risk and sizing rules
4. Required checks
5. Decision gate
6. Review trigger
