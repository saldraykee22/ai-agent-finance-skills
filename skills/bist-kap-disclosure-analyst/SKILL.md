---
name: bist-kap-disclosure-analyst
description: Analyze KAP disclosures, BIST material events, financial statement notices, dividends, capital increases, buybacks, shareholder changes, related-party transactions, debt updates, lawsuits, regulatory decisions, and corporate governance filings. Use when the user asks what a KAP disclosure means, whether a BIST announcement is material, how it affects a stock thesis, or what follow-up checks are needed after a disclosure.
---

# BIST KAP Disclosure Analyst

## Core Workflow

Use this skill to read KAP disclosures like a BIST analyst. Read `references/analysis-workflow.md` for disclosure classification, materiality checks, and output format.

## Operating Rules

- Prefer the KAP disclosure text over media summaries.
- Separate mechanical facts, financial impact, governance impact, and market-flow impact.
- Check dates, ratios, amounts, currency, board/AGM approvals, and effective conditions.
- Do not add generic boilerplate caveats. Keep output analytical, sourced, and direct.
- Match the user's language.

## Default Output Shape

1. Disclosure summary
2. Materiality
3. Financial and share-count impact
4. Thesis impact
5. Follow-up checks
