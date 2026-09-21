"""Per-strategy constants the improvement process reads (DESIGN/100 §2): the metric that is the
reward, the column that defines an independent unit, the entry column the registration date
filters on, the Newey-West lag, the gate value that means ON, and where the ledger lives.

The two name-sheet entries (findings/stock-deep-dive DESIGN/70 §6) add two things the S-A / S-B
books never needed: a unit column that is an identifier rather than a date (the sheet's unit is a
name and its expiry, so that overlapping same-name rows within 21 sessions count once), and a
pre-registered read trigger — a count, and for the discretionary book a date — below which the read
is NOT_DUE instead of a verdict. Specs that declare neither behave exactly as before.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date

from engine import policy as POL
from engine.config import (DATA, DISC_POLICY_ID, GO_T_MIN, LEDGER_DIR, LEDGER_NAME_DIR, LEDGER_SB_DIR, NAME_PARAMS,
                           NAME_POLICY_ID, SA_POLICY_ID, SB_GO_T_MIN, SB_NW_LAG, SB_POLICY_ID)
from engine.strategies import sb_gate as G

BACKTEST = os.path.join(DATA, "backtest")
GATE_PASS = "PASS"          # the sheet's gate code when no S-C filter and no exclusion fired
NAME_GO_T = 2.0             # DESIGN/70 §6; the same bar S-B carries, on a much slower book


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
    unit_is_date: bool = True             # False: `unit` names an identifier column, not a date
    read_n_required: int | None = None    # pre-registered count trigger; below it the read is NOT_DUE
    read_not_before: date | None = None   # the earliest date the read may run at all

    def ledger_dir(self, root: str = LEDGER_DIR) -> str:
        return os.path.join(root, self.ledger_subdir) if self.ledger_subdir else root


SPECS = {
    "sb": StrategySpec("sb", SB_POLICY_ID, "ror", "post", "entry", SB_NW_LAG, G.GATE_ON, SB_GO_T_MIN, 1.0, "sb",
                       os.path.join(BACKTEST, "sb_marked.parquet")),
    "sa": StrategySpec("sa", SA_POLICY_ID, "net_pct", "pre", "pre", 0, POL.SA_GATE_PASS, GO_T_MIN, 3.0, "",
                       os.path.join(BACKTEST, "trades.parquet")),
    # DESIGN/70 §6: return on risk per sheet row, one unit per name and expiry (`unit_id` is stamped
    # by the R6 writer as "<ticker>:<post>"); the gate read compares strata by `gate_verdict`.
    "sheet": StrategySpec("sheet", NAME_POLICY_ID, "ror", "unit_id", "E", 0, GATE_PASS, NAME_GO_T, 5.0, "name", "",
                          unit_is_date=False, read_n_required=NAME_PARAMS.sheet_read_n),
    # DESIGN/70 §6: R on the owner's share leg, one unit per decision date, no read before 2027-03-01.
    "disc": StrategySpec("disc", DISC_POLICY_ID, "r_share", "E", "E", 0, GATE_PASS, NAME_GO_T, 2.0, "name", "",
                         read_n_required=NAME_PARAMS.disc_read_n, read_not_before=NAME_PARAMS.disc_read_not_before),
}
assert LEDGER_SB_DIR == SPECS["sb"].ledger_dir()
assert LEDGER_NAME_DIR == SPECS["sheet"].ledger_dir() == SPECS["disc"].ledger_dir()


def spec(strategy: str) -> StrategySpec:
    if strategy not in SPECS:
        raise ValueError(f"unknown strategy {strategy!r}; known: {sorted(SPECS)}")
    return SPECS[strategy]
