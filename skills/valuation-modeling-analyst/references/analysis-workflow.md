# Valuation Modeling Workflow

## Method selection

- DCF: use when cash flows are forecastable and capital structure can be modeled.
- Multiples: use for market-relative valuation and quick peer context.
- SOTP: use when segments have different economics or peer sets.
- NAV: use for real estate, holding companies, natural resources, banks in some contexts.
- Dividend discount/residual income: use for banks, insurers, mature dividend assets.
- Reverse DCF: use to infer what current price already assumes.

## Input checklist

- Current price, diluted shares, market cap, cash, debt, leases, minority interest, pension deficit, associates.
- Historical revenue, margins, tax, capex, depreciation, working capital, FCF.
- Guidance and consensus estimates when available.
- Peer multiples, growth, margin, leverage, return profile.
- Risk-free rate, equity risk premium, beta, country risk, cost of debt, tax rate.

## DCF process

1. Define forecast horizon and business drivers.
2. Forecast revenue by volume, price, mix, segment, or users when possible.
3. Forecast margins with operating leverage and reinvestment needs.
4. Model taxes, working capital, capex, D&A, SBC if relevant, and FCF.
5. Estimate WACC:
   - Cost of equity = risk-free rate + beta * equity risk premium + country/company adjustments.
   - Cost of debt = current or normalized pre-tax borrowing cost.
   - Use target capital structure when current leverage is distorted.
6. Estimate terminal value:
   - Perpetuity growth must be consistent with long-term nominal growth.
   - Exit multiple must be consistent with terminal margins, growth, and returns.
7. Bridge enterprise value to equity value and per-share value.
8. Run sensitivity on WACC, terminal growth/multiple, margin, growth, and reinvestment.

## Multiples process

1. Select peers with matching business model, geography, growth, margin, and balance sheet.
2. Normalize metrics:
   - Use forward or trailing consistently.
   - Adjust for one-offs, leases, cash, debt, minorities, pension, SBC where material.
3. Choose metrics:
   - EV/EBITDA, EV/EBIT, EV/Sales, P/E, P/B, FCF yield, dividend yield.
   - Sector metrics such as ARR, NAV, reserves, AUM, CET1, FFO.
4. Explain premium/discount versus peers.

## Scenario rules

- Base: most likely operating path.
- Upside: specific drivers, not just higher multiple.
- Downside: explicit margin, demand, balance sheet, or valuation compression path.
- Include trigger and invalidation for each scenario.

## Crypto/token valuation

1. Verify chain, contract, circulating supply, liquid float, FDV, treasury, vesting, emissions, burns, and unlock schedule.
2. Map protocol usage, fees, revenue, incentives, and treasury flows.
3. Prove the token-holder value-accrual mechanism before using fee or cash-flow multiples.
4. Compare networks only after normalizing business model, security budget, dilution, liquidity, and adoption stage.
5. Use scenario ranges for adoption, take rate, token velocity, dilution, and terminal multiple; avoid false-precision target prices.
6. Show both circulating-value and fully diluted outcomes and identify the supply date assumed.

## Watchpoints

- Terminal value often dominates DCF; expose that sensitivity.
- Do not mix nominal and real assumptions.
- Multiples embed market mood; do not treat them as intrinsic truth.
- Share count, dilution, and SBC can materially change per-share value.
- Net debt must match the enterprise value definition.

## Output format

```text
Method:
- ...

Inputs:
- Price/date/source:
- Shares/net debt:
- Financial base:

Assumptions:
- Revenue:
- Margin:
- Reinvestment:
- WACC/terminal:

Valuation:
- DCF:
- Multiples:
- SOTP/NAV if relevant:

Sensitivity:
- ...

Reverse-implied view:
- ...

Key breaks:
- ...
```
