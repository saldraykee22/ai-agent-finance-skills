---
name: asset-master-data-manager
description: Build and normalize canonical asset identity, instrument metadata, identifiers, exchange mapping, currency, trading venue, corporate action fields, and crypto contract or chain metadata. Use when an analysis spans BIST, US, Germany, crypto, ETFs, indices, FX, commodities, or when tickers, ISINs, token contracts, adjusted prices, listings, currencies, or asset names may be ambiguous.
---

# Asset Master Data Manager

## Core Rule

Create a clean asset master before analysis whenever symbol ambiguity can change the conclusion. Prefer exact identifiers over plain names.

## Workflow

1. Define the asset universe and classify each instrument as equity, ETF, index, crypto token, stablecoin, FX, commodity, derivative, or cash bucket.
2. Normalize identifiers: ticker, exchange, MIC when available, ISIN, FIGI, CIK or LEI for companies, contract address and chain for tokens, issuer, base currency, quote currency, and trading venue.
3. Capture market metadata: lot size, tick size, trading hours, settlement, price limit rules, liquidity venue, benchmark, sector, country, and tax or withholding flags only as factual fields.
4. Record adjustment fields: dividends, splits, bonus issues, rights issues, redenominations, token migrations, burns, emissions, unlocks, and index changes.
5. Mark stale or missing fields explicitly and route uncertain items to `market-data-source-verifier` or `data-quality-reconciliation-engine`.

## Use Together

Use with `market-data-source-verifier` for source proof, `corporate-actions-analyst` for adjustment events, `crypto-tokenomics-supply-analyst` for token supply fields, and `market-screener-watchlist` before ranking a mixed universe.

## Output

Return `Verified Facts`, `Identifier Map`, `Normalization Decisions`, `Ambiguities`, `Uncertainties`, and `Next Checks`.

## Reference

Read `references/analysis-workflow.md` when building or auditing a full cross-market asset master.
