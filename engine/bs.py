"""Black-Scholes price for the tier-3 fallback mark (DESIGN/70 §2; RESEARCH/50 §2.1).

Vectorized over numpy arrays. European, no dividends; the fallback is only used for legs that
did not print, so model risk here is deliberately confined to the small leg.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

OPTION_TYPES = ("call", "put")
_MIN_T = 1e-12


def _validate(sigma, option_type: str) -> None:
    if option_type not in OPTION_TYPES:
        raise ValueError(f"option_type must be one of {OPTION_TYPES}, got {option_type!r}")
    if np.any(np.asarray(sigma, dtype=float) < 0):
        raise ValueError("sigma must be non-negative")


def price(S, K, t, r: float, sigma, option_type: str):
    """BS price. S, K, t (years), sigma may be scalars or arrays; t <= 0 returns intrinsic."""
    _validate(sigma, option_type)
    S = np.asarray(S, dtype=float)
    K = np.asarray(K, dtype=float)
    t = np.asarray(t, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    sign = 1.0 if option_type == "call" else -1.0
    intrinsic = np.maximum(sign * (S - K), 0.0)
    live = (t > _MIN_T) & (sigma > 0)
    t_safe = np.where(live, t, 1.0)
    sig_safe = np.where(live, sigma, 1.0)
    vol_t = sig_safe * np.sqrt(t_safe)
    d1 = (np.log(S / K) + (r + 0.5 * sig_safe ** 2) * t_safe) / vol_t
    d2 = d1 - vol_t
    disc = np.exp(-r * t_safe)
    model = sign * (S * norm.cdf(sign * d1) - K * disc * norm.cdf(sign * d2))
    out = np.where(live, model, intrinsic)
    return float(out) if out.ndim == 0 else out
