---
name: stablecoin-liquidity-risk-analyst
description: Analyze stablecoin peg risk, liquidity, collateral, issuer risk, exchange pair depth, stablecoin dominance, mint/burn flows, bridge exposure, depeg signals, and crypto market liquidity conditions. Use when the user asks whether stablecoin liquidity supports crypto spot trades, whether a stablecoin is risky, how stablecoin flows affect altcoins, or how to manage stablecoin/cash buckets.
---

# Stablecoin Liquidity Risk Analyst

## Core Workflow

Use this skill for crypto cash/liquidity risk. Read `references/analysis-workflow.md` for stablecoin peg, collateral, flow, venue, and portfolio bucket checks.

## Operating Rules

- Separate stablecoin issuer risk, peg risk, venue liquidity, bridge risk, and market liquidity signal.
- Verify chain, contract, issuer, pair, exchange, and timestamp.
- For spot portfolios, connect stablecoin risk to cash bucket, deployment ability, and exit liquidity.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Stablecoin exposure
2. Peg and liquidity status
3. Flow signal
4. Venue/bridge risk
5. Portfolio action
