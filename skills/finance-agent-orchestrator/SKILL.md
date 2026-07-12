---
name: finance-agent-orchestrator
description: Route complex finance requests through the smallest sufficient set of specialist finance skills and synthesize one decision-ready result. Use for broad market analysis, complete stock or crypto reviews, portfolio decisions, multi-asset research, watchlists, recurring research systems, or any request spanning several finance domains.
---

# Finance Agent Orchestrator

## Workflow

1. Restate the decision, deliverable, horizon, instruments, and constraints.
2. Classify the request and select one primary skill. For broad BIST or crypto spot work, select `bist-crypto-spot-command-center`.
3. Add only specialists whose outputs can change the conclusion. Read `references/analysis-workflow.md` for route selection.
4. Verify current-sensitive facts before interpreting them. Reconcile material conflicts instead of averaging them.
5. Apply the relevant decision or quality gates.
6. Synthesize one answer; do not concatenate specialist reports.

## Routing Rules

- Use one primary route and normally no more than three conditional specialists at first pass.
- Expand the route only for a stated evidence gap, conflict, risk, or requested deliverable.
- Treat data verification as a gate, not a decorative step.
- Do not invoke execution, monitoring, reporting, or audit skills unless the user needs that lifecycle stage.
- Preserve the user's requested market and instrument scope. Default to BIST/crypto spot only when the request leaves scope unspecified.
- Match the user's language and avoid generic boilerplate caveats.

## Output Contract

Present the objective and bottom line first, followed by verified facts, analysis, scenarios, uncertainties, and next checks. For an actionable decision, also state policy fit, invalidation, portfolio impact, liquidity/cost constraints, and a `Proceed`, `Wait`, or `Reject` verdict.
