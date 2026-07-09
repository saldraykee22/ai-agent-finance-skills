---
name: insider-ownership-flow-analyst
description: Analyze insider transactions, management ownership, major shareholder changes, institutional ownership, 13F filings, Form 3/4/5, beneficial ownership, free float, lockups, pledges, fund holder changes, and BIST ownership disclosures. Use when the user asks who is buying or selling, whether insiders or institutions are accumulating, ownership quality, free-float pressure, or holder structure risk.
---

# Insider Ownership Flow Analyst

## Core Workflow

Use this skill to interpret ownership and holder-flow data. Read `references/analysis-workflow.md` for source hierarchy, transaction classification, 13F limitations, BIST ownership checks, and output format.

## Operating Rules

- Separate insider transactions, institutional filings, major shareholder disclosures, and inferred flow.
- Timestamp ownership data; many holder reports are delayed.
- For BIST, prioritize KAP shareholder disclosures, buyback disclosures, free float, and major holder changes.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Ownership snapshot
2. Recent holder changes
3. Insider/management alignment
4. Flow interpretation
5. Data limitations
