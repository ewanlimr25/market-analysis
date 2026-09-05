"""Deterministic options-premium engine (DESIGN/70 in ~/Development/findings/market-analysis).

Layers: `mart` (materialized daily tables), `marking` (tiered option marks), `strategies`
(pure functions from tables to trade lists), `validation` (clustered t, BH, DSR, seasons),
`daily` (make daily) and `ledger` (the forward ledger). No model call anywhere in this package.
"""
