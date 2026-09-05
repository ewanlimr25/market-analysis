"""Paths and the pre-registered parameters (DESIGN/70 §2, §3; frozen 2026-09-05).

Everything a strategy or the marking engine reads as a threshold lives here so that a
change is a diff to one file. The S-A filters F1..F8 are pre-registered and MUST NOT be
edited before the Season 3 (2026-10-01 .. 2026-11-30) read; see `SA_FROZEN_ON`.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(REPO, "scripts")
DATA = os.path.join(REPO, "data")
MART = os.path.join(DATA, "mart")
ANALYSES_DAILY = os.path.join(REPO, "analyses", "daily")
LEDGER_DIR = os.path.join(REPO, "ledger")            # forward ledger: committed, never re-derived
PRICES = os.path.join(DATA, "prices.parquet")
STOCKS = os.path.expanduser(os.environ.get("UW_STOCKS_DIR", "~/Documents/Stocks"))

ALL_OPTIONS_FILE = "All Options/bot-eod-report-{d}.parquet"
HOT_CHAINS_FILE = "Hot Option Chains/hot-chains-{d}.parquet"
SCREENER_FILE = "Stock Screener/stock-screener-{d}.parquet"
SCREENER_GLOB = "Stock Screener/stock-screener-*.parquet"

ET_TZ = "America/New_York"
# Session window applied to every All Options print (RESEARCH/20 §1.6: the post-close tail is
# captured inconsistently across days, so a hard cut is required; the 16:00 minute is kept
# for the closing rotation).
SESSION_START = "09:30:00"
SESSION_END_EXCL = "16:01:00"
LATE_START = "15:00:00"      # `late` window: executed_at >= 15:00 ET
EARLY_END = "10:30:00"       # `early` window: executed_at <= 10:30 ET

# Integer scaling for deterministic size-weighted sums (bit-for-bit across thread counts).
PRICE_SCALE = 10_000         # option prices to 1e-4
IV_SCALE = 1_000_000         # implied vol to 1e-6

# Marking engine (DESIGN/70 §2)
TIER1_MIN_SIZE = 5           # size_<when> >= 5 -> tier 1 VWAP mark
MODEL_SPREAD_FLOOR = 0.05    # tier 3 relative spread floor
MODEL_IV_LOOKBACK = 5        # sessions to look back for a contract iv_vwap
MODEL_SPREAD_LOOKBACK = 20   # sessions of the name's late_rel_spread for the tier-3 spread
RISK_FREE_RATE = 0.04
COMMISSION_PER_CONTRACT = 0.65
CONTRACT_MULTIPLIER = 100

ISSUE_TYPES = ("Common Stock", "ADR")


@dataclass(frozen=True)
class SAParams:
    """S-A pre-registered filters and structures (DESIGN/70 §3). Do not tune."""
    price_min: float = 10.0                      # F2
    mcap_min: float = 2e9                        # F3
    mcap_max: float = 50e9                       # F3
    adv_min: float = 50e6                        # F4 (20-day dollar ADV)
    atm_band: float = 0.025                      # F5 |K/S - 1| <= 2.5%
    leg_size_min: int = 10                       # F5 size_late >= 10 on both legs
    spread_max: float = 0.10                     # F6 late_rel_spread <= 10% on both legs
    implied_min: float = 0.04                    # F7
    implied_max: float = 0.15                    # F7
    wing_mult: float = 2.0                       # IC wings at S * (1 +/- 2 * implied)
    a2_excluded_sectors: tuple[str, ...] = ("Technology", "Communication Services")


@dataclass(frozen=True)
class SizingParams:
    """DESIGN/70 §3.3 with the owner's 2026-09-05 decisions: placeholders kept, E = $100,000."""
    equity: float = 100_000.0
    ic_max_loss_frac: float = 0.005              # IC max loss <= 0.5% of equity
    ss_stress_frac: float = 0.010                # SS stress loss <= 1.0% of equity
    ss_stress_move_mult: float = 3.0             # stress = P&L at a 3x implied move
    max_open_events: int = 8
    max_per_sector: int = 3
    night_budget_frac: float = 0.40              # <= 40% of the book's risk budget on one night


SA_PARAMS = SAParams()
SIZING = SizingParams()
SA_FROZEN_ON = date(2026, 9, 5)

# Season windows on `pre` (DESIGN/70 §4.1)
SEASONS = {
    "S1": (date(2026, 4, 1), date(2026, 6, 15)),
    "S2": (date(2026, 7, 1), date(2026, 9, 4)),
    "S3": (date(2026, 10, 1), date(2026, 11, 30)),
}
PRIMARY_TESTS = 4            # 2 variants x 2 structures
DSR_TRIALS = 6               # 4 primary + 2 pre-registered exit rules (DESIGN/70 §4.1)
BH_FDR = 0.10
GO_T_MIN = 2.5
GO_MIN_EVENTS = 60
GO_WORST_TO_MEAN_WIN_MAX = 4.0
