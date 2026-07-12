---
name: financial-report-writer
description: Convert financial analysis into research notes, morning briefs, portfolio updates, investment memos, event notes, watchlist summaries, earnings previews, and decision-ready market commentary. Use when the user asks to write, polish, structure, summarize, or turn analysis into a professional financial report.
---

# Financial Report Writer

## Core Workflow

Use this skill to package financial research into clear decision-ready writing. Read `references/analysis-workflow.md` for report formats, section templates, tone rules, and quality checks.

## Operating Rules

- Preserve the analyst's facts, calculations, and uncertainties; do not invent missing data.
- Lead with the decision-relevant view.
- For BIST/crypto spot notes, include policy fit, lifecycle stage, liquidity/execution, net cost/slippage, and portfolio impact when available.
- Use `research-production-pipeline-manager` when the report should become a repeatable daily, weekly, event, or portfolio production workflow.
- Use `portfolio-dashboard-designer` when report sections should map to dashboard widgets or recurring monitoring views.
- Use `model-assumption-validator` when a report depends on valuation, factor, scenario, or signal assumptions that drive the conclusion.
- Use `finance-research-quality-auditor` before finalizing high-stakes or action-oriented research notes.
- Keep source dates and assumptions visible.
- State a data cutoff and evidence confidence. Preserve `Unavailable`, `Estimated`, `Derived`, and `Conflicting` labels instead of smoothing gaps into prose.
- For recommendations, separate thesis attractiveness, execution readiness, and execution authorization.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Title and one-line view
2. Key facts
3. Thesis
4. Scenarios
5. Risks/uncertainties
6. Next checks
