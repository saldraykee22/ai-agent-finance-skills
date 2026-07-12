# Decision Scoring Workflow

## Score architecture

Keep two scores separate:

- `Thesis Attractiveness`: expected quality of the opportunity if the thesis is correct.
- `Execution Readiness`: whether evidence, timing, liquidity, sizing, and controls permit action now.

Score each dimension from `-2` to `+2`. Compute a 0-100 result with:

`normalized score = 50 + 25 * sum(score_i * weight_i) / sum(weight_i)`

Use integer weights totaling 100. Show every component and the arithmetic. Use `N/A` only when a dimension is structurally irrelevant; renormalize those weights. Treat missing evidence as a readiness defect and never hide it through renormalization.

## BIST/equity spot thesis weights

| Dimension | Weight |
| --- | ---: |
| Fundamental quality/earnings trend | 20 |
| Valuation and implied expectations | 15 |
| Price trend and relative strength | 15 |
| Catalyst quality/timing | 10 |
| Sector and macro regime | 10 |
| Balance-sheet/downside resilience | 10 |
| Liquidity/free float/market structure | 10 |
| Evidence quality | 10 |

## Crypto spot thesis weights

| Dimension | Weight |
| --- | ---: |
| Token utility/value accrual/adoption | 15 |
| Supply, float, emissions, and unlocks | 15 |
| Price trend and relative strength | 15 |
| Narrative and catalyst quality | 10 |
| On-chain/protocol traction | 10 |
| Spot liquidity and venue quality | 15 |
| Security, governance, and custody risk | 10 |
| Evidence quality | 10 |

## Execution-readiness weights

| Dimension | Weight |
| --- | ---: |
| Identity and data freshness | 15 |
| Trigger and timing | 15 |
| Invalidation and scenario loss | 15 |
| Liquidity, spread, depth, and slippage | 15 |
| Position size and portfolio fit | 15 |
| Catalyst/event risk | 10 |
| Order plan and venue constraints | 10 |
| Monitoring and exit plan | 5 |

## Hard gates

Cap `Execution Readiness` below 60 and prohibit `Ready` when any of these is unresolved:

- identity, venue, currency, or crypto contract;
- stale decision-critical market data;
- no trigger or no falsifiable invalidation;
- unknown executable liquidity, spread, or size constraints;
- unacceptable portfolio concentration or scenario loss;
- unresolved material event, corporate action, unlock, or source conflict;
- missing explicit user authorization for an external order mutation.

The authorization gate does not prevent an execution-ready plan; it prevents an actual order call.

## Decision mapping

- `Ready`: readiness >= 75, thesis >= 60, every hard gate passed, and pre-trade verdict is `Pass`.
- `Watch`: thesis >= 60 but readiness < 60 or evidence is incomplete.
- `Wait for Trigger`: thesis >= 60 and readiness 60-74 with a named missing trigger/condition.
- `Reduce`: existing position has thesis < 50, a risk-budget breach, or a broken monitoring condition.
- `Reject`: thesis < 40, a fatal hard gate, no identifiable edge, or unacceptable downside/liquidity.

Scores do not create precision. Always state the top three contributors, top three detractors, sensitivity to one score-step changes, and evidence confidence.

## Output contract

Return the evidence cutoff time, both scorecards, formulas, hard-gate status, confidence, decision, conditions that change it, and the next required checks.
