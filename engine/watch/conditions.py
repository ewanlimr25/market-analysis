"""The 18 watch-basket conditions (`DESIGN/110-watch-basket.md` §2, fixed; do not add, drop,
re-sign or re-threshold a condition outside a read, per §6). C-DIV-D (daily RSI bullish
divergence) was added 2026-09-07 evening, before any forward row, per §2/§8.

Every function here is a small pure predicate over an ALREADY-COMPUTED metric (a decile flag, an
indicator value, a structure flag) -- the data plumbing that produces those metrics from the
marts and the Yahoo bars cache lives in `retro.py` (R1, backtest) and, in R2, `nightly.py`. This
split keeps every threshold a one-line, hand-testable function and matches DESIGN/110's own
per-row phrasing ("Rule" column).

Null safety (DESIGN/110 §1): a condition whose input is missing returns `None`, never `False`.
Three-valued (Kleene) logic is used wherever a condition ANDs/ORs sub-checks, so an unknown
sub-check can still leave the overall result `True` or `False` when the other sub-checks already
decide it, and only forces `None` when it is the deciding one.
"""
from __future__ import annotations

import math

# =============================================================================================
# Thresholds (DESIGN/110 §2) -- the only place a number in this module may be changed, and only
# by a read (§6), never by editing a row's meaning.
# =============================================================================================

C_HIGH_MIN_PCT_52W_RANGE = 0.85           # C-HIGH
C_LOW_MAX_PCT_52W_RANGE = 0.15            # C-LOW
C_SHORT_MIN_DAYS_TO_COVER = 5.0           # C-SHORT (FINRA, point-in-time)
C_SHORT_MIN_BORROW_FEE_PCT = 5.0          # C-SHORT (IBKR fee, percent)
C_IVUP_MIN_IVRANK_CHG_5D = 10.0           # C-IVUP, IV-rank points
C_VOL_IV30D_LO = 0.30                     # C-VOL
C_VOL_IV30D_HI = 0.80                     # C-VOL
C_VOL_MCAP_LO = 1e9                       # C-VOL
C_VOL_MCAP_HI = 20e9                      # C-VOL
C_VOL_MIN_DAYS_TO_EARNINGS = 35           # C-VOL, "no earnings within 35 days"
C_RSI_MAX_WEEKLY_RSI = 30.0               # C-RSI
C_AVWAP_LOOKBACK_SESSIONS = 5             # C-AVWAP / C-AVWAP-LOSS
C_POC_MAX_RANGE_FRACTION = 0.25           # C-POC / C-POC-LOSS, (high60-low60)/close
C_POC_ACCEPTANCE_SESSIONS = 2             # C-POC / C-POC-LOSS
C_LEAP_MIN_PREMIUM = 1_000_000.0          # C-LEAP, single-leg premium at the ask
C_LEAP_MIN_DTE = 180                      # C-LEAP
C_DP_MIN_PREMIUM = 5_000_000.0            # C-DP, dark-pool premium that day

# The 18 condition ids, grouped by sign (DESIGN/110 §2 "Sign" column). C-DIV-D sits immediately
# after C-DIV everywhere ids are listed (DESIGN/110 §2 row order).
SIGN_PLUS = ("C-HIGH", "C-IVUP", "C-DIV", "C-DIV-D", "C-AVWAP", "C-POC", "C-SWING")
SIGN_MINUS = ("C-LOW", "C-SHORT", "C-OIBUILD", "C-CROWD", "C-AVWAP-LOSS", "C-POC-LOSS", "C-SWING-LOSS")
SIGN_VOL = ("C-VOL",)
SIGN_LOGGED = ("C-RSI", "C-LEAP", "C-DP")
ALL_CONDITIONS = SIGN_PLUS + SIGN_MINUS + SIGN_VOL + SIGN_LOGGED
assert len(ALL_CONDITIONS) == 18


def _isnan(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x))


def kleene_and(values) -> bool | None:
    """`False` if any value is `False`; else `None` if any is `None`/unknown; else `True`."""
    vals = list(values)
    if any(v is False for v in vals):
        return False
    if any(v is None for v in vals):
        return None
    return True


def kleene_or(values) -> bool | None:
    """`True` if any value is `True`; else `None` if any is `None`/unknown; else `False`."""
    vals = list(values)
    if any(v is True for v in vals):
        return True
    if any(v is None for v in vals):
        return None
    return False


def _threshold(value, op) -> bool | None:
    return None if _isnan(value) else bool(op(value))


# =============================================================================================
# The 18 conditions
# =============================================================================================


def c_high(pct_52w_range: float | None) -> bool | None:
    """C-HIGH: near 52-week high, `pct_52w_range >= 0.85`."""
    return _threshold(pct_52w_range, lambda v: v >= C_HIGH_MIN_PCT_52W_RANGE)


def c_low(pct_52w_range: float | None) -> bool | None:
    """C-LOW: near 52-week low, `pct_52w_range <= 0.15`."""
    return _threshold(pct_52w_range, lambda v: v <= C_LOW_MAX_PCT_52W_RANGE)


def c_short(days_to_cover: float | None, borrow_fee_pct: float | None) -> bool | None:
    """C-SHORT: crowded short side. FINRA `days_to_cover >= 5` (point-in-time) OR IBKR
    `borrow_fee_pct >= 5`. Either side alone can decide `True`; both missing is `None`."""
    dtc = _threshold(days_to_cover, lambda v: v >= C_SHORT_MIN_DAYS_TO_COVER)
    fee = _threshold(borrow_fee_pct, lambda v: v >= C_SHORT_MIN_BORROW_FEE_PCT)
    return kleene_or([dtc, fee])


def c_oibuild(is_top_decile_oi_net_5d: bool | None) -> bool | None:
    """C-OIBUILD: 5-day net call-OI build in the cross-sectional top decile that night. The
    decile flag itself is computed once per night across the universe (`retro.py`/`nightly.py`);
    this function only carries the sign forward."""
    return is_top_decile_oi_net_5d


def c_crowd(is_top_decile_premium_to_cap: bool | None) -> bool | None:
    """C-CROWD: `tot_prem / marketcap` in the cross-sectional top decile that night."""
    return is_top_decile_premium_to_cap


def c_ivup(ivrank_chg_5d: float | None) -> bool | None:
    """C-IVUP: IV rank waking, `ivrank_chg_5d >= +10` points."""
    return _threshold(ivrank_chg_5d, lambda v: v >= C_IVUP_MIN_IVRANK_CHG_5D)


def c_vol(iv30d: float | None, marketcap: float | None, has_tier1_atm_pair: bool | None,
           days_to_next_earnings: float | None) -> bool | None:
    """C-VOL: premium-sellable. `iv30d` in [0.30, 0.80], marketcap in [$1B, $20B], a tier-1 ATM
    pair exists that day, and no earnings within 35 days (a missing `next_earnings_date` is
    "unknown", not "clear" -- pass `days_to_next_earnings=None` and it drives the overall result
    to `None` unless another sub-check is already `False`)."""
    iv_ok = _threshold(iv30d, lambda v: C_VOL_IV30D_LO <= v <= C_VOL_IV30D_HI)
    mcap_ok = _threshold(marketcap, lambda v: C_VOL_MCAP_LO <= v <= C_VOL_MCAP_HI)
    earnings_ok = _threshold(days_to_next_earnings, lambda v: v > C_VOL_MIN_DAYS_TO_EARNINGS)
    return kleene_and([iv_ok, mcap_ok, has_tier1_atm_pair, earnings_ok])


def c_rsi(weekly_rsi_last: float | None) -> bool | None:
    """C-RSI: weekly RSI(14) oversold, `<= 30`. Logged only (no sign)."""
    return _threshold(weekly_rsi_last, lambda v: v <= C_RSI_MAX_WEEKLY_RSI)


def c_div(bullish_divergence_flag: bool | None) -> bool | None:
    """C-DIV: RSI bullish divergence over the last 8 weekly bars (`indicators.bullish_divergence`)."""
    return bullish_divergence_flag


def c_div_d(bullish_divergence_daily_flag: bool | None) -> bool | None:
    """C-DIV-D: RSI bullish divergence over the last 20 daily bars, same halves rule as C-DIV but
    on daily closes and daily RSI(14) (`indicators.bullish_divergence`, `series._daily_divergence`).
    Added 2026-09-07 evening, before any forward row (DESIGN/110 §2, §8)."""
    return bullish_divergence_daily_flag


def c_avwap(reclaim_flag: bool | None) -> bool | None:
    """C-AVWAP: close above the AVWAP anchored at the 52-week-low date, crossed within 5 sessions
    (`indicators.crossed_within` on the anchored series)."""
    return reclaim_flag


def c_avwap_loss(loss_flag: bool | None) -> bool | None:
    """C-AVWAP-LOSS: mirror of C-AVWAP, anchored at the 52-week-high date."""
    return loss_flag


def c_poc(accept_above_flag: bool | None) -> bool | None:
    """C-POC: value acceptance above a tight range -- the range condition
    `(high60-low60)/close <= 0.25` AND close above the value-area high for the last 2 sessions,
    both folded into `accept_above_flag` upstream (`retro.py`'s per-ticker POC computation)."""
    return accept_above_flag


def c_poc_loss(accept_below_flag: bool | None) -> bool | None:
    """C-POC-LOSS: mirror of C-POC, acceptance below the value-area low."""
    return accept_below_flag


def c_swing(structure_flag: bool | None) -> bool | None:
    """C-SWING: ATR(14)-zigzag (2x ATR reversal), last three pivots HL-HH-HL
    (`indicators.swing_structure`)."""
    return structure_flag


def c_swing_loss(structure_flag: bool | None) -> bool | None:
    """C-SWING-LOSS: mirror of C-SWING, LH-LL-LH (`indicators.swing_structure_loss`)."""
    return structure_flag


def c_leap(has_leap_print: bool | None) -> bool | None:
    """C-LEAP: >= $1M single-leg call premium at the ask, DTE >= 180, that day. Logged only (no
    sign until a read assigns one, DESIGN/110 §2 evidence column: "09-07 run: sign undetermined")."""
    return has_leap_print


def c_dp(has_dark_pool_print: bool | None) -> bool | None:
    """C-DP: dark-pool premium >= $5M that day. Logged only, control (`RESEARCH/30 §5`)."""
    return has_dark_pool_print


CONDITION_FUNCS = {
    "C-HIGH": c_high, "C-LOW": c_low, "C-SHORT": c_short, "C-OIBUILD": c_oibuild,
    "C-CROWD": c_crowd, "C-IVUP": c_ivup, "C-VOL": c_vol, "C-RSI": c_rsi, "C-DIV": c_div,
    "C-DIV-D": c_div_d,
    "C-AVWAP": c_avwap, "C-AVWAP-LOSS": c_avwap_loss, "C-POC": c_poc, "C-POC-LOSS": c_poc_loss,
    "C-SWING": c_swing, "C-SWING-LOSS": c_swing_loss, "C-LEAP": c_leap, "C-DP": c_dp,
}
assert set(CONDITION_FUNCS) == set(ALL_CONDITIONS)
