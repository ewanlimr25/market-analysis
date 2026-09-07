"""Per-strategy constants the improvement process reads (DESIGN/100 §2): the metric that is the
reward, the column that defines an independent unit, the entry column the registration date
filters on, the Newey-West lag, the gate value that means ON, and where the ledger lives."""
from __future__ import annotations

import os
from dataclasses import dataclass

from engine import policy as POL
from engine.config import DATA, GO_T_MIN, LEDGER_DIR, LEDGER_SB_DIR, SA_POLICY_ID, SB_GO_T_MIN, SB_NW_LAG, SB_POLICY_ID
from engine.strategies import sb_gate as G

BACKTEST = os.path.join(DATA, "backtest")


@dataclass(frozen=True)
class StrategySpec:
    strategy: str
    champion_id: str
    metric: str            # the reward column: net excess per unit of risk
    unit: str              # one independent outcome = one distinct value of this column
    entry_col: str         # the date a registration filters on (rows entered after `registered`)
    lag: int               # Newey-West lag on the ordered unit series
    gate_on: str           # `gate_verdict` value that means the gate allowed the champion
    go_t: float            # the champion's season bar on t (the rest of the bar lives in the reports)
    units_per_week: float  # for projecting an adjudication date
    ledger_subdir: str     # under --ledger-dir
    backtest_file: str     # fallback series for the realised sd before the ledger has rows

    def ledger_dir(self, root: str = LEDGER_DIR) -> str:
        return os.path.join(root, self.ledger_subdir) if self.ledger_subdir else root


SPECS = {
    "sb": StrategySpec("sb", SB_POLICY_ID, "ror", "post", "entry", SB_NW_LAG, G.GATE_ON, SB_GO_T_MIN, 1.0, "sb",
                       os.path.join(BACKTEST, "sb_marked.parquet")),
    "sa": StrategySpec("sa", SA_POLICY_ID, "net_pct", "pre", "pre", 0, POL.SA_GATE_PASS, GO_T_MIN, 3.0, "",
                       os.path.join(BACKTEST, "trades.parquet")),
}
assert LEDGER_SB_DIR == SPECS["sb"].ledger_dir()


def spec(strategy: str) -> StrategySpec:
    if strategy not in SPECS:
        raise ValueError(f"unknown strategy {strategy!r}; known: {sorted(SPECS)}")
    return SPECS[strategy]
