# Crypto Analysis Workflow

## Source hierarchy

Use current sources when the question is time-sensitive:

- Exchange pages/APIs: spot price, volume, order book, funding, open interest, futures basis, borrow rates when available.
- Project primary sources: docs, whitepaper, GitHub, blog, official X/account, Discord/forum announcements, governance proposals.
- Block explorers: token contract, supply, holders, transfers, treasury wallets, bridge contracts.
- Data aggregators: CoinGecko, CoinMarketCap, DefiLlama, Token Terminal, Dune, Artemis, Glassnode, CryptoQuant, Coinglass, Laevitas, TradingView.
- Security sources: audit reports, exploit postmortems, bug bounty pages, chain monitoring accounts.
- Regulatory/legal sources when relevant: official agency releases, court filings, exchange notices.

## Identification checklist

Before analysis, verify:

- Asset name, ticker, chain, contract address, decimals, wrapped/bridged status.
- Exchange venue and quote currency.
- Circulating supply, total supply, max supply if any, fully diluted valuation, market cap.
- Unlock schedule, emissions, staking rewards, burns, vesting cliffs, treasury allocation.
- Spot liquidity, exchange distribution, market-maker concentration signals, major pair depth.
- Derivatives availability, funding rate, open interest, long/short skew, liquidation clusters.

## Research process

1. Define the request: asset, chain, timeframe, trade/investment horizon, and whether the user wants spot, derivatives, on-chain, protocol, or narrative analysis.
2. Gather fresh market facts:
   - Price, market cap, FDV, 24h volume, major venues, spread/depth if available.
   - BTC/ETH correlation and relative strength.
   - Recent news, listings, delistings, governance votes, exploit/security events.
3. Analyze liquidity and derivatives:
   - Funding rate, open interest, futures basis, liquidation levels, volume/OI divergence.
   - Spot vs perp behavior; identify whether price move is spot-led or leverage-led.
   - Exchange concentration and shallow liquidity risks.
4. Analyze tokenomics:
   - Supply schedule, unlock dates, emissions, staking/validator rewards, burn mechanics.
   - Insider/team/investor allocations and likely sell pressure windows.
   - Utility, fee capture, governance rights, revenue link, and value accrual path.
5. Analyze protocol/on-chain data:
   - Active addresses, transactions, fees, revenue, TVL, stablecoin liquidity, bridge flows.
   - Developer activity and ecosystem growth when relevant.
   - Whale and treasury flows only when address labels are credible.
6. Analyze narrative and catalysts:
   - Sector narrative such as L1, L2, AI, DePIN, RWA, gaming, memecoins, restaking, privacy.
   - Upcoming launches, airdrops, mainnet upgrades, ETF/regulatory events, exchange listings.
   - Distinguish real adoption from social momentum.
7. Produce scenarios:
   - Base, upside, downside.
   - Trigger, invalidation, and the data that would change the view.

## Crypto-specific watchpoints

- Ticker collisions are common. Always confirm contract address and chain.
- FDV can dominate near-term risk when circulating supply is small.
- Thin liquidity can make market cap misleading.
- On-chain labels can be wrong. Treat unlabeled wallet interpretations cautiously.
- Funding and OI extremes can signal crowded positioning, not direction by themselves.
- Bridge and wrapped-asset risks are separate from the underlying asset.
- Governance and multisig control can matter as much as published tokenomics.
- Airdrop farming and incentive programs can inflate activity metrics.

## Output format

Prefer this structure:

```text
Executive view:
- ...

Fresh market data:
- Price/date/source:
- Volume/liquidity:
- Funding/OI:

Token/protocol facts:
- Contract/chain:
- Supply/FDV:
- Unlocks/emissions:

Drivers:
- ...

Scenarios:
- Base:
- Upside:
- Downside:

Uncertainties:
- ...
```

## Quality bar

- Include source names and timestamps/dates for fresh facts.
- Use multiple sources for market-moving claims.
- Show ratio and valuation calculations.
- Mark stale or unverified data clearly.
- Do not include generic boilerplate caveats unless the user explicitly asks.
