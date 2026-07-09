---
name: benchmark-attribution-analyst
description: Explain portfolio performance versus benchmarks using allocation, selection, timing, sector, factor, currency, cash drag, and cost attribution. Use when the user asks why a portfolio underperformed or outperformed, whether BIST or crypto choices added value, how benchmark choice changes interpretation, or which holdings drove results.
---

# Benchmark Attribution Analyst

## Core Workflow

Use this skill to explain performance, not just calculate it. Read `references/analysis-workflow.md` for benchmark selection, attribution categories, and output format.

## Operating Rules

- Choose benchmark based on the user's actual universe and policy.
- Separate allocation, selection, timing, FX, costs, and cash drag.
- If data is incomplete, provide a qualitative attribution and list missing fields.
- Do not add generic boilerplate caveats. Keep the output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Benchmark choice
2. Portfolio return vs benchmark
3. Attribution drivers
4. Winners/laggards
5. Lessons for allocation
