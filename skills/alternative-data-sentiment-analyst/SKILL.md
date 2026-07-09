---
name: alternative-data-sentiment-analyst
description: Analyze alternative data and sentiment signals such as search trends, app rankings, web traffic, social sentiment, developer activity, GitHub activity, protocol users, community growth, job postings, product reviews, exchange social flow, and narrative heat for BIST companies, crypto assets, sectors, and themes. Use when the user asks whether sentiment or alternative data confirms a thesis.
---

# Alternative Data Sentiment Analyst

## Core Rule

Treat alternative data as supporting evidence, not proof. Separate real usage, attention, speculation, and manipulation-prone hype.

## Workflow

1. Define thesis and which alternative signals could genuinely test it.
2. Classify signals as demand, usage, developer, community, sentiment, search, hiring, product, or market hype.
3. Check source reliability, timestamp, sampling bias, survivorship bias, and bot or manipulation risk.
4. Compare signal direction with price, volume, fundamentals, narrative rotation, and catalyst timeline.
5. Route crypto-heavy cases to `crypto-narrative-rotation-analyst`, `crypto-onchain-flow-analyst`, and `market-manipulation-anomaly-detector`.

## Output

Return `Signal Map`, `Evidence Quality`, `Trend Direction`, `Contradictions`, `Manipulation Risk`, `Thesis Impact`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` for alternative data categories.
