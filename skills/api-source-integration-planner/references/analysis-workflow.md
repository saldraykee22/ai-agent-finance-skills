# API Source Planning Workflow

## Source Matrix

| Domain | Primary or Near-Primary | Typical Fields | Main Risks |
| --- | --- | --- | --- |
| BIST | Borsa Istanbul, KAP, issuer IR, TCMB | prices, disclosures, indices, macro | access limits, delayed data, adjusted series |
| US | SEC EDGAR, issuer IR, exchanges, Fed | filings, statements, macro, prices | ticker changes, share class mapping |
| Germany | Deutsche Boerse/Xetra, issuer IR, BaFin/EQS style releases | prices, issuer events, filings | venue mismatch, language, delayed access |
| Crypto | exchange APIs, block explorers, protocol docs, governance, DeFi dashboards | price, depth, supply, TVL, wallets | fake volume, contract collisions, bridge supply |
| Portfolio | broker exports, exchange exports, manual ledger | trades, fills, fees, cash | inconsistent CSV schemas, FX conversion |

## Integration Backlog Fields

Priority, data owner, source, endpoint or export type, fields, identifiers, auth, refresh cadence, validation, fallback, downstream consumer.
