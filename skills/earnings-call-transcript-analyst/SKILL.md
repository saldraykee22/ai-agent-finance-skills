---
name: earnings-call-transcript-analyst
description: Analyze earnings calls, transcripts, investor presentations, management tone, guidance changes, Q&A pressure points, segment commentary, KPI language, and quarter-over-quarter narrative drift. Use when the user asks about earnings calls, management commentary, guidance quality, whether results were good or bad beyond headline numbers, or what changed in a company's narrative after results.
---

# Earnings Call Transcript Analyst

## Core Workflow

Use this skill to extract decision-relevant signal from earnings calls and management commentary. Read `references/analysis-workflow.md` for transcript workflow, tone checks, Q&A analysis, and output format.

## Operating Rules

- Separate reported facts, management claims, analyst questions, tone shifts, and your interpretation.
- Compare current commentary to prior quarter/year when possible.
- For BIST, use KAP earnings notes, investor presentations, and management commentary when transcripts are unavailable.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Call context
2. Management message
3. Guidance and KPI changes
4. Q&A pressure points
5. Narrative shifts
6. Implications for thesis

## Professional Gate

For current-sensitive or action-oriented work, apply the `finance-research-quality-auditor` evidence contract: timestamp perishable inputs, label unavailable or conflicting fields, show decision-changing calculations, and separate analysis, execution readiness, and execution authorization.
