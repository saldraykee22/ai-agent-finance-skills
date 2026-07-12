# Preferred MCP tool routing

## Portability contract

Use these rules with Hermes Agent, Codex, and Antigravity:

1. Discover the connected server and its current tool schema before calling it.
2. Match tools by unqualified capability name; clients may expose different server prefixes.
3. Inspect required parameters and enum values at runtime. Do not infer a schema from this reference.
4. Treat MCP output as source data, not as an investment conclusion.
5. Record provider, tool, symbol, market, parameters, observation timestamp, source timestamp when returned, and freshness status.
6. Never claim a tool was called when it was unavailable or failed. State the gap and use a fallback source.

## `saidsurucu/borsa-mcp`

Prefer this server for BIST and Turkish macro research. It also covers US equities, FX, commodities, funds, indices, and secondary crypto market data.

| Need | Tools | Verification notes |
| --- | --- | --- |
| Identity | `search_symbol`, `get_profile` | Confirm market, ticker, company, share class, and currency first |
| BIST/US snapshot | `get_quick_info`, `get_index_data` | Timestamp price and identify delayed or derived fields |
| Price history | `get_historical_data` | Record interval, range, timezone, and adjustment basis |
| Technical context | `get_technical_analysis`, `get_pivot_points`, `scan_stocks` | Treat indicators as derived evidence, never as standalone decisions |
| Fundamentals | `get_financial_statements`, `get_financial_ratios`, `get_earnings` | Confirm period, consolidation basis, currency, and inflation accounting |
| KAP/events | `get_news`, `get_corporate_actions`, `get_dividends` | Read the original disclosure when material; do not rely only on summaries |
| Screening | `screen_securities`, `get_sector_comparison` | Preserve universe, filters, as-of date, and survivorship limitations |
| Macro/FX/rates | `get_macro_data`, `get_evds_data` when exposed, `get_fx_data`, `get_bond_yields`, `get_economic_calendar` | Prefer official TCMB/EVDS values and release timestamps |
| Funds | `get_fund_data`, `screen_funds` | Record TEFAS date, fees, category, and comparison window |
| Secondary crypto check | `get_crypto_market` | Use Binance directly for Binance execution and order-book decisions |

Server versions may expose different tool counts. Use runtime discovery rather than relying on a fixed count.

## `saldraykee22/binance-trader-mcp`

Prefer this server for Binance spot market microstructure, account state, and explicitly authorized spot execution.

### Public research tier

- Market: `get_ticker`, `get_klines`, `get_orderbook`, `get_recent_trades`, `get_exchange_info`.
- Availability: `ping`, `get_server_time`, `get_symbol_status`.
- Derived analysis: `analyze_indicators`, `multi_indicator_scan`, `multi_timeframe_analysis`, `get_market_overview`, `get_indicator_info`.

Confirm the exact Binance symbol and quote asset. Before sizing, read exchange filters such as tick size, step size, minimum quantity, and minimum notional. Timestamp the order book and do not reuse it after it becomes stale.

### Private read tier

Use `get_account`, `get_open_orders`, `get_order`, and `get_my_trades` only when the user requests account-aware analysis or portfolio/order review. Minimize exposure of balances and trade history in the response.

### Mutation tier

`place_market_order`, `place_limit_order`, `place_oco_order`, `cancel_order`, and any stock-token order tool change external state. Call them only when all conditions hold:

1. The user explicitly asks to place or cancel that specific order in the current conversation.
2. The exact account, symbol, side, order type, quantity or quote amount, price/stop fields, and time-in-force are resolved.
3. Fresh symbol filters, balance, open orders, market data, liquidity, fees, and slippage have been checked.
4. `pre-trade-checklist-controller` returns `Pass`; a `Conditional Pass` is not sufficient.
5. Dry-run/testnet is preferred for testing. Never change environment safety settings or credentials on the user's behalf.
6. Return the exchange response and record order ID/status; never report a fill that the response does not prove.

Do not interpret a general request for analysis, a trade plan, or an execution-ready setup as authorization to place an order.

## Source precedence and fallback

- BIST disclosure/fundamental fact: original KAP or issuer document > `borsa-mcp` structured result > secondary provider.
- Turkish macro fact: TCMB/EVDS/TUIK release > `borsa-mcp` structured result > news summary.
- Binance spot executable price/filter/order state: Binance MCP current response > cached or aggregated market data.
- Crypto identity/supply/on-chain fact: official contract, explorer, protocol docs > exchange metadata > aggregator.
- When preferred MCP data conflicts with a more authoritative primary source, preserve both observations and route to `data-quality-reconciliation-engine`.

## Failure handling

- Retry only safe reads and only when the failure is plausibly transient.
- Do not automatically retry a mutation after a timeout; first query order state to avoid duplicate execution.
- On partial data, label missing fields and reduce conclusion strength.
- On stale data, refresh before an execution decision.
- On symbol ambiguity, stop and resolve identity before any account or order call.
