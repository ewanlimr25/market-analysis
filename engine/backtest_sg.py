"""Run S-G over the mart and write g3_trades.parquet / g3_suppressed.parquet / g3_dropped.parquet
(DESIGN/91 §2, §6 G3-code).

    python3 -m engine.backtest_sg [--out data/backtest]

Loads `daily_contract` rows once per pre-registered entry offset (DESIGN/91 §1: −3 and −5) plus
once at the exit day (`sa_data.load_pre_rows` reused unmodified — S-G's exit day is S-A's own
entry day, `pre`), builds one `MarkResolver` over the union, and runs `sg.run` for both offsets.
"""
from __future__ import annotations

import argparse
import os
import time

import duckdb
import pandas as pd

from engine import marking as M
from engine.config import DATA, SA_PARAMS, SG_PARAMS, SGParams
from engine.strategies import sa_data
from engine.strategies import sa_filters as F
from engine.strategies import sg, sg_data

OUT_DIR = os.path.join(DATA, "backtest")


def _rows_dict(*frames: pd.DataFrame) -> dict[tuple[str, object], dict]:
    out: dict[tuple[str, object], dict] = {}
    for df in frames:
        if len(df):
            for r in df.to_dict("records"):
                out[(r["option_chain_id"], F.to_date(r["date"]))] = r
    return out


def load_inputs(con, params: SGParams = SG_PARAMS) -> dict:
    t0 = time.time()
    events = sg_data.load_events(con)
    mcap_lo, mcap_hi = SA_PARAMS.mcap_min, SA_PARAMS.mcap_max
    entry_rows_by_offset = {o: sg_data.load_entry_rows(con, events, o, mcap_lo, mcap_hi) for o in params.entry_offsets}
    exit_rows = sg_data.load_exit_rows(con, events, mcap_lo, mcap_hi)

    spreads: dict = {}
    for o in params.entry_offsets:
        spreads.update(sg_data.spread_history(con, events, o))
    spreads.update(sa_data.load_spread_history(con, events))

    tickers = set(events.ticker)
    entry_dates: set = set()
    for o in params.entry_offsets:
        entry_dates.update(sg_data.with_entry_pre(events, o).pre)
    exit_dates = set(events.pre)
    all_dates = entry_dates | exit_dates
    prices = sa_data.load_prices(con, tickers, all_dates)
    iv30d = sa_data.load_iv30d(con, tickers, all_dates)

    rows_dict = _rows_dict(*entry_rows_by_offset.values(), exit_rows)
    print(f"loaded: {len(events)} events, {sum(len(v) for v in entry_rows_by_offset.values())} entry rows, "
          f"{len(exit_rows)} exit rows ({time.time() - t0:.1f}s)")
    return {"events": events, "entry_rows_by_offset": entry_rows_by_offset, "prices": prices,
            "iv30d": iv30d, "spreads": spreads, "rows_dict": rows_dict}


def run_sg(inputs: dict, params: SGParams = SG_PARAMS, cost_mult: float = 1.0) -> sg.RunResult:
    model_inputs_fn = sg_data.build_model_inputs(inputs["prices"], inputs["iv30d"], inputs["spreads"])
    resolver = M.MarkResolver(inputs["rows_dict"], model_inputs_fn)
    return sg.run(inputs["events"], inputs["entry_rows_by_offset"], resolver, inputs["prices"],
                 model_inputs_fn, params.entry_offsets, params, cost_mult, inputs["rows_dict"])


def write_outputs(res: sg.RunResult, out_dir: str = OUT_DIR) -> None:
    os.makedirs(out_dir, exist_ok=True)
    res.trades.to_parquet(os.path.join(out_dir, "g3_trades.parquet"), index=False)
    res.suppressed.to_parquet(os.path.join(out_dir, "g3_suppressed.parquet"), index=False)
    res.dropped.to_parquet(os.path.join(out_dir, "g3_dropped.parquet"), index=False)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT_DIR)
    args = ap.parse_args()
    con = duckdb.connect()
    res = run_sg(load_inputs(con))
    write_outputs(res, args.out)
    t = res.trades
    print(f"trades {len(t)} rows; suppressed {len(res.suppressed)}; dropped {len(res.dropped)}")
    if len(t):
        print(t.groupby(["variant", "structure"]).agg(n=("net_pct", "size"), mean_net_pct=("net_pct", "mean")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
