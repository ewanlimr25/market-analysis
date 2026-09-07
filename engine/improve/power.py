"""Power arithmetic for a challenger registration (DESIGN/100 §4): how many independent units are
needed to detect `min_effect` in the reward at one-sided alpha with the required power, given the
champion's realised dispersion, inflated for the autocorrelation the Newey-West lag will absorb."""
from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy import stats as sps

ALPHA, POWER = 0.05, 0.80
MIN_SERIES = 10        # below this the realised sd is not trusted and a fallback series is required


def realised_sd(series) -> float:
    x = np.asarray(pd.Series(series, dtype=float).dropna(), dtype=float)
    if len(x) < 2:
        raise ValueError("need at least two observations for a realised sd")
    return float(x.std(ddof=1))


def autocorr_inflation(series, lag: int) -> float:
    """Bartlett-weighted variance inflation 1 + 2·Σ w_k·ρ_k for k = 1..lag, floored at 1."""
    x = np.asarray(pd.Series(series, dtype=float).dropna(), dtype=float)
    n = len(x)
    if lag <= 0 or n < lag + 3:
        return 1.0
    e = x - x.mean()
    denom = float((e * e).sum())
    if denom <= 0:
        return 1.0
    total = 0.0
    for k in range(1, lag + 1):
        rho = float((e[k:] * e[:-k]).sum()) / denom
        total += (1 - k / (lag + 1)) * rho
    return max(1.0, 1 + 2 * total)


def n_required(min_effect: float, sd: float, alpha: float = ALPHA, power: float = POWER, inflation: float = 1.0) -> int:
    """One-sided test of a paired mean: n = ((z_{1-α} + z_{power}) · sd / min_effect)² · inflation, rounded up."""
    if min_effect <= 0:
        raise ValueError("min_effect must be positive")
    if sd <= 0:
        raise ValueError("sd must be positive")
    if not (0 < alpha < 1 and 0 < power < 1):
        raise ValueError("alpha and power must be in (0, 1)")
    z = sps.norm.ppf(1 - alpha) + sps.norm.ppf(power)
    return int(math.ceil((z * sd / min_effect) ** 2 * max(inflation, 1.0)))


def projected_date(start: date, n: int, units_per_week: float) -> date:
    if units_per_week <= 0:
        raise ValueError("units_per_week must be positive")
    return start + timedelta(days=int(math.ceil(7 * n / units_per_week)))


def plan(min_effect: float, series, lag: int, start: date, units_per_week: float,
         alpha: float = ALPHA, power: float = POWER, sd: float | None = None) -> dict:
    """Everything a registration needs, from the champion's series (or an explicit sd)."""
    x = pd.Series(series, dtype=float).dropna() if series is not None else pd.Series(dtype=float)
    used_sd = sd if sd is not None else realised_sd(x)
    inflation = autocorr_inflation(x, lag) if len(x) else 1.0
    n = n_required(min_effect, used_sd, alpha, power, inflation)
    return {"min_effect": min_effect, "sd": used_sd, "sd_source": "explicit" if sd is not None else f"series (n={len(x)})",
            "lag": lag, "inflation": inflation, "alpha": alpha, "power": power, "n_required": n,
            "units_per_week": units_per_week, "adjudicate_on": projected_date(start, n, units_per_week).isoformat()}
