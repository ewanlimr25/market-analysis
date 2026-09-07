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


# =============================================================================================
# S-B: index vol premium with a VIX gate (DESIGN/80; frozen 2026-09-05). Do not tune before the
# 2026-12-01 read. Nothing above this line changed when S-B was added.
# =============================================================================================
LEDGER_SB_DIR = os.path.join(LEDGER_DIR, "sb")
INDEX_VOL_DIR = os.path.join(MART, "index_vol")
INDEX_VOL_FILE = os.path.join(INDEX_VOL_DIR, "index_vol.parquet")
INDEX_VOL_FALLBACK = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/sb-backtest/index_vol_cboe_2026-09-05.parquet")
PROXY_PRICES_FALLBACK = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/sb-backtest/spy_qqq_yahoo_2026-09-05.parquet")
CBOE_HISTORY_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/{index}_History.csv"
CBOE_INDICES = ("VIX", "VIX3M", "VXN", "VIX9D")


@dataclass(frozen=True)
class SBParams:
    """S-B pre-registered gate, expiry, strike and structure parameters (DESIGN/80 §2-§3)."""
    target_dte_cal: int = 21                     # §3.2 expiry nearest entry + 21 calendar days
    dte_cal_min: int = 7                         # §3.2
    dte_cal_max: int = 30                        # §3.2
    short_sigma: float = 1.0                     # §3.4 short legs at S(1 -/+ m)
    wing_sigma: float = 2.0                      # §3.4 wings at S(1 -/+ 2m)
    strike_band_sigma: float = 0.25              # §3.4 nearest tier-1 strike within +/- 0.25m
    leg_size_min: int = 5                        # §3.4 tier-1 late print on every leg
    short_spread_max: float = 0.10               # §3.6 (the S-A F6 value, reused)
    median_window: int = 20                      # §2 G2: sessions t-21 .. t-2
    take_profit_frac: float = 0.50               # §8 Alt-2 only


@dataclass(frozen=True)
class SBSizing:
    """DESIGN/80 §4."""
    equity: float = 100_000.0
    max_loss_frac: float = 0.03                  # max loss <= 3% of equity per position
    max_open_per_sleeve: int = 3                 # one per week of a three-week hold


SB_PARAMS = SBParams()
SB_SIZING = SBSizing()
SB_FROZEN_ON = date(2026, 9, 5)
SB_LEDGER_OPENS = date(2026, 9, 11)              # §5.3
SB_UNDERLYINGS = ("SPY", "QQQ")
SB_VOL_INDEX = {"SPY": "vix", "QQQ": "vxn"}      # §2 G2 / §3.3 the X series per underlying
SB_STRUCTURES = ("PS", "IC")
# Windows on the entry session (§6.4)
SB_WINDOWS = {
    "P1": (date(2023, 9, 8), date(2024, 8, 30)),
    "P2": (date(2024, 9, 6), date(2025, 8, 29)),
    "P3": (date(2025, 9, 5), date(2026, 11, 6)),
}
SB_MARKED_WINDOW = (date(2026, 3, 13), date(2026, 11, 6))
# Proxy smile: median IV / index per (underlying, leg), measured 2026-09-05 (§1.3, §5.1)
SB_PROXY_IV_MULT = {
    ("SPY", "p1"): 1.07, ("SPY", "p2"): 1.35, ("SPY", "c1"): 0.65, ("SPY", "c2"): 0.74,
    ("QQQ", "p1"): 1.08, ("QQQ", "p2"): 1.34, ("QQQ", "c1"): 0.76, ("QQQ", "c2"): 0.79,
}
# Proxy cost: median late relative NBBO spread per (underlying, leg), measured 2026-09-05 (§1.3)
SB_PROXY_SPREAD = {
    ("SPY", "p1"): 0.0076, ("SPY", "p2"): 0.0132, ("SPY", "c1"): 0.0225, ("SPY", "c2"): 0.222,
    ("QQQ", "p1"): 0.0086, ("QQQ", "p2"): 0.0132, ("QQQ", "c1"): 0.0121, ("QQQ", "c2"): 0.0314,
}
SB_PROXY_STRIKE_STEP = 1.0                       # SPY and QQQ strikes on the $1 grid
# Bar (§6.7)
SB_PRIMARY_TESTS = 4                             # 2 underlyings x 2 structures
SB_DSR_TRIALS = 6                                # 4 primary + Alt-1 + Alt-2 (§8)
SB_NW_LAG = 2                                    # three-deep overlap of weekly entries
SB_GO_T_MIN = 2.0
SB_GO_MONTH_LOSS_MULT = 3.0                      # worst month >= -3 x median month
SB_SCALE_MIN_POSITIONS = 40                      # forward ledger count trigger for scaling up
SB_PBO_BLOCKS = 16


# =============================================================================================
# S-G: pre-earnings ramp, backtest-only research pre-registration (findings/market-analysis
# DESIGN/91; written 2026-09-07). Not a champion: no frozen-params test, no forward ledger, no
# `make daily` step. F1..F4, F7, F8 are reused unchanged from SA_PARAMS via sa_filters.cheap_filters;
# only F5/F6 (contract availability, spread) are re-evaluated at the entry day instead of `pre`.
# =============================================================================================
@dataclass(frozen=True)
class SGParams:
    """S-G pre-registered entry offsets and sizing risk fraction (DESIGN/91 §1-§3)."""
    entry_offsets: tuple[int, ...] = (3, 5)       # G3a (day -3), G3b (day -5); trading sessions before E
    leg_size_min: int = 10                        # F5 reused: size_late >= 10 on both legs at entry_day
    risk_frac: float = 0.010                      # n = floor(risk_frac * equity / premium_paid_per_contract)


SG_PARAMS = SGParams()
SG_EQUITY = 100_000.0
SG_PRIMARY_TESTS = 4                              # 2 entry offsets x 2 structures (LS, LG), DESIGN/91 §4
SG_DSR_TRIALS = DSR_TRIALS + SG_PRIMARY_TESTS     # S-A's 6 + S-G's 4 = 10 (DESIGN/91 §4)
SG_BH_FDR = BH_FDR                                # reuse S-A's 0.10
SG_GO_T_MIN = 2.0                                 # DESIGN/91 §4 bar
SG_PBO_BLOCKS = 16


# =============================================================================================
# Improvement process (findings/market-analysis DESIGN/100, D22; adopted 2026-09-06). The champion
# policy id bumps only when an adjudication promotes a challenger, together with the frozen test.
# =============================================================================================
SA_POLICY_ID = "sa-1.0"
SB_POLICY_ID = "sb-1.0"


# =============================================================================================
# G10: S-B challengers from the CBOE vol-index family (findings/market-analysis
# RESEARCH/47-edge-gaps.md §2; DESIGN/80 §8 idea ledger). Read-only additions: nothing above this
# line moved. `index_vol_ext` never writes into `INDEX_VOL_DIR`; it is its own mart table.
# =============================================================================================
INDEX_VOL_EXT_DIR = os.path.join(MART, "index_vol_ext")
INDEX_VOL_EXT_FILE = os.path.join(INDEX_VOL_EXT_DIR, "index_vol_ext.parquet")
INDEX_VOL_EXT_FALLBACK = os.path.expanduser(
    "~/Development/findings/market-analysis/artifacts/edge-gaps/g10/index_vol_ext_2026-09-07.parquet")
CBOE_EXT_INDICES = ("VVIX", "SKEW")              # single-value CSVs: DATE,<INDEX> (not OHLC/CLOSE)
CBOE_EXT_VALUE_COLUMN = {"VVIX": "VVIX", "SKEW": "SKEW"}
CBOE_EXT_INDEX_COLUMN = {"VVIX": "vvix", "SKEW": "skew"}


# =============================================================================================
# Watch basket (findings/market-analysis DESIGN/110-watch-basket.md; R1 2026-09-07, R2 nightly,
# C-DIV-D added 2026-09-07 evening). Exploration-only, paper rows, `policy_id = "wb-1.0"`: nothing
# above this line moved, and the 18 conditions/thresholds stay in `engine/watch/conditions.py`, not
# here.
# =============================================================================================
LEDGER_WB_DIR = os.path.join(LEDGER_DIR, "wb")
LEDGER_WB_OPEN = date(2026, 9, 8)                # DESIGN/110 §7 R2; before this, nothing is written
                                                  # to ledger/wb/ unless --force-ledger

