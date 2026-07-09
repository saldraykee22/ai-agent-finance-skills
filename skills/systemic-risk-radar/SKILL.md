---
name: systemic-risk-radar
description: Monitor systemic market risk and fragility across valuation pressure, leverage, funding stress, liquidity, credit spreads, FX stress, crypto market structure, BIST local macro risk, geopolitical shocks, and cross-asset contagion. Use when the user asks whether market conditions are risky, whether to reduce exposure, what macro/systemic alarms matter, or how broad risk affects BIST and crypto spot positions.
---

# Systemic Risk Radar

## Core Workflow

Use this skill as the high-level risk alarm panel. Read `references/analysis-workflow.md` for risk categories, signals, and exposure translation.

## Operating Rules

- Separate systemic risk from single-asset thesis risk.
- Translate broad alarms into exposure, sizing, liquidity, and event-calendar implications.
- Prioritize BIST TRY macro sensitivity and crypto liquidity/leverage stress for the default user profile.
- Use `geopolitical-policy-risk-analyst`, `short-crowding-flow-analyst`, and `custody-counterparty-risk-analyst` when policy, positioning, or venue risk is the main transmission channel.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Risk regime
2. Active alarms
3. BIST impact
4. Crypto impact
5. Portfolio actions to consider
6. Watch next
