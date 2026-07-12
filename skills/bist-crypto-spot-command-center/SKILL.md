---
name: bist-crypto-spot-command-center
description: Coordinate decision-ready BIST equity and crypto spot workflows with minimal specialist routing. Use for complete spot decisions, daily preparation, watchlist review, portfolio posture, trade setup, risk checks, position management, or recurring BIST and crypto workflows.
---

# BIST Crypto Spot Command Center

## Workflow

1. Identify the objective, asset or portfolio, horizon, lifecycle stage, and constraints.
2. Select one command route from `references/analysis-workflow.md`.
3. Establish market posture only when it affects the requested decision.
4. Verify current-sensitive inputs and resolve material conflicts.
5. Apply the spot decision gate; stop at `Wait` or `Reject` when a blocking condition exists.
6. Add execution, monitoring, or review skills only if the request reaches those stages.

## Operating Rules

- Prioritize BIST equities and crypto spot; do not introduce derivatives unless explicitly requested or needed as market context.
- Start with one market skill and add specialists only for decision-changing questions.
- Separate verified facts, calculations, interpretation, scenarios, uncertainties, and next checks.
- For actionable ideas, require thesis, invalidation, portfolio fit, liquidity, net costs, catalyst risk, and monitoring logic.
- Match the user's language and avoid generic boilerplate caveats.
- Prefer `borsa-mcp` for BIST/Turkish macro research and `binance-trader-mcp` for Binance spot data when connected. Use `api-source-integration-planner` for portable tool discovery and permission-tier rules.
- Never promote research into account access or order execution without the corresponding user request and gate.

## Output Contract

Lead with the objective, bottom line, and `Proceed`, `Wait`, or `Reject` verdict. Then give the minimal skill route, evidence, decision gate, action plan, risks, and next checks.
