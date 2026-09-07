"""Statistics for the validation harness (DESIGN/70 §4.1).

cluster_t         Liang-Zeger cluster-robust mean test; one cluster per shared draw (print date)
bh_reject         Benjamini-Hochberg at a given FDR across the primary tests
deflated_sharpe   Bailey & Lopez de Prado (2014): SR, the expected max SR under the null for the
                  trial count (SR*), their difference, and the PSR at SR* (the DSR probability)
pbo               probability of backtest overfitting by CSCV over user-supplied blocks
binomial_test     two-sided exact binomial test of a rate against a null proportion
mcnemar_test      exact McNemar test on a paired binary comparison's discordant-pair counts
nw_t              Newey-West (Bartlett kernel) mean test for an ordered, autocorrelated series
"""
from __future__ import annotations

import math
from itertools import combinations

import numpy as np
import pandas as pd
from scipy import stats as sps

EULER_GAMMA = 0.5772156649015329


def cluster_t(x, clusters) -> dict:
    """Mean, cluster-robust SE, t and p (Student t on G-1 df) of a sample mean."""
    x = np.asarray(x, dtype=float)
    clusters = np.asarray(clusters)
    ok = np.isfinite(x)
    x, clusters = x[ok], clusters[ok]
    n = len(x)
    if n == 0:
        return {"n": 0, "G": 0, "mean": np.nan, "se": np.nan, "t": np.nan, "p": np.nan,
                "median": np.nan, "hit": np.nan}
    mu = x.mean()
    _, inv = np.unique(clusters, return_inverse=True)
    G = int(inv.max()) + 1
    gsum = np.bincount(inv, weights=x - mu, minlength=G)
    var = (gsum ** 2).sum() / n ** 2
    if G > 1:
        var *= G / (G - 1)
    se = math.sqrt(var) if var > 0 else float("nan")
    t = mu / se if se and se > 0 else float("nan")
    p = float(2 * sps.t.sf(abs(t), df=max(G - 1, 1))) if np.isfinite(t) else float("nan")
    return {"n": int(n), "G": G, "mean": float(mu), "se": float(se), "t": float(t), "p": p,
            "median": float(np.median(x)), "hit": float((x > 0).mean())}


def _cluster_group_var(resid: np.ndarray, clusters) -> tuple[float, int]:
    """Liang-Zeger cluster variance of a residual's mean, and the cluster count G. `clusters` is
    any 1-D array of hashable labels (a combined "a||b" key stands in for a two-way intersection)."""
    _, inv = np.unique(np.asarray(clusters), return_inverse=True)
    G = int(inv.max()) + 1
    gsum = np.bincount(inv, weights=resid, minlength=G)
    var = (gsum ** 2).sum() / len(resid) ** 2
    if G > 1:
        var *= G / (G - 1)
    return float(var), G


def two_way_cluster_t(x, cluster_a, cluster_b) -> dict:
    """Cameron-Gelbach-Miller (2011) two-way cluster-robust t of a sample mean:
    Var = Var_a + Var_b - Var_(a,b), floored at 0 (the intersection cluster removes the
    double-counted covariance). Used for G2's "clustered by (underlying, day)" requirement,
    where neither dimension alone is the right unit: same-day prints across underlyings share a
    market-wide shock, and same-underlying prints across days share a name-specific one.
    """
    x = np.asarray(x, dtype=float)
    a = np.asarray(cluster_a)
    b = np.asarray(cluster_b)
    ok = np.isfinite(x)
    x, a, b = x[ok], a[ok], b[ok]
    n = len(x)
    if n == 0:
        return {"n": 0, "Ga": 0, "Gb": 0, "mean": np.nan, "se": np.nan, "t": np.nan, "p": np.nan,
                "median": np.nan, "hit": np.nan}
    mu = x.mean()
    resid = x - mu
    var_a, Ga = _cluster_group_var(resid, a)
    var_b, Gb = _cluster_group_var(resid, b)
    inter = np.array([f"{ai}||{bi}" for ai, bi in zip(a, b)], dtype=object)
    var_ab, Gab = _cluster_group_var(resid, inter)
    var = max(var_a + var_b - var_ab, 0.0)
    se = math.sqrt(var) if var > 0 else float("nan")
    t = mu / se if se and se > 0 else float("nan")
    df = max(min(Ga, Gb) - 1, 1)
    p = float(2 * sps.t.sf(abs(t), df=df)) if np.isfinite(t) else float("nan")
    return {"n": int(n), "Ga": int(Ga), "Gb": int(Gb), "Gab": int(Gab), "mean": float(mu),
            "se": float(se), "t": float(t), "p": p, "median": float(np.median(x)),
            "hit": float((x > 0).mean())}


def bh_reject(pvals, fdr: float) -> list[bool]:
    """Benjamini-Hochberg step-up: which hypotheses are rejected at the given FDR."""
    p = np.asarray(list(pvals), dtype=float)
    m = len(p)
    if m == 0:
        return []
    order = np.argsort(p)
    ranked = p[order]
    thresholds = fdr * (np.arange(1, m + 1) / m)
    passing = np.nonzero(ranked <= thresholds)[0]
    k = passing.max() + 1 if len(passing) else 0
    out = np.zeros(m, dtype=bool)
    out[order[:k]] = True
    return out.tolist()


def sharpe(x) -> float:
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    if len(x) < 2 or x.std(ddof=1) == 0:
        return float("nan")
    return float(x.mean() / x.std(ddof=1))


def expected_max_sharpe(n_trials: int, var_sharpe: float) -> float:
    """SR*: the expected maximum Sharpe among n_trials null strategies (per-observation units)."""
    if n_trials <= 1 or var_sharpe <= 0:
        return 0.0
    z1 = sps.norm.ppf(1 - 1 / n_trials)
    z2 = sps.norm.ppf(1 - 1 / (n_trials * math.e))
    return float(math.sqrt(var_sharpe) * ((1 - EULER_GAMMA) * z1 + EULER_GAMMA * z2))


def probabilistic_sharpe(x, benchmark: float) -> float:
    """PSR: P(true SR > benchmark) given the sample's skew and (non-excess) kurtosis."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = len(x)
    sr = sharpe(x)
    if not np.isfinite(sr) or n < 3:
        return float("nan")
    skew = float(sps.skew(x, bias=False))
    kurt = float(sps.kurtosis(x, fisher=False, bias=False))
    denom = math.sqrt(max(1 - skew * sr + (kurt - 1) / 4 * sr ** 2, 1e-12))
    return float(sps.norm.cdf((sr - benchmark) * math.sqrt(n - 1) / denom))


def deflated_sharpe(x, n_trials: int, var_sharpe: float) -> dict:
    """SR, SR*, deflated SR (= SR - SR*) and the DSR probability PSR(SR*) for a P&L series."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    sr = sharpe(x)
    sr_star = expected_max_sharpe(n_trials, var_sharpe)
    return {"n": int(len(x)), "sr": sr, "sr_star": sr_star, "deflated_sr": sr - sr_star,
            "dsr_prob": probabilistic_sharpe(x, sr_star),
            "skew": float(sps.skew(x, bias=False)) if len(x) > 2 else float("nan"),
            "kurt": float(sps.kurtosis(x, fisher=False, bias=False)) if len(x) > 3 else float("nan"),
            "n_trials": int(n_trials), "var_sharpe": float(var_sharpe)}


def _block_moments(pnl: pd.DataFrame, block_ids: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Per (block, config) sums, sums of squares and counts; blocks x configs arrays."""
    labels, inv = np.unique(block_ids, return_inverse=True)
    n_blocks, n_cfg = len(labels), pnl.shape[1]
    vals = pnl.to_numpy(dtype=float)
    sums = np.zeros((n_blocks, n_cfg))
    sq = np.zeros((n_blocks, n_cfg))
    cnt = np.zeros((n_blocks, 1))
    for j in range(n_cfg):
        sums[:, j] = np.bincount(inv, weights=vals[:, j], minlength=n_blocks)
        sq[:, j] = np.bincount(inv, weights=vals[:, j] ** 2, minlength=n_blocks)
    cnt[:, 0] = np.bincount(inv, minlength=n_blocks)
    return sums, sq, cnt


def _sharpe_from_moments(s: np.ndarray, q: np.ndarray, n: np.ndarray) -> np.ndarray:
    mean = s / n
    var = np.maximum((q - n * mean ** 2) / np.maximum(n - 1, 1), 1e-18)
    return mean / np.sqrt(var)


def pbo(pnl: pd.DataFrame, block_ids) -> dict:
    """Probability of backtest overfitting (Bailey et al. 2017, CSCV) over the given blocks.

    `pnl` is (n_obs x n_configs); `block_ids` labels each observation's block (e.g. a date
    bucket). Every combination of half the blocks is in-sample: the best IS config by Sharpe is
    ranked OOS; PBO is the share of combinations where that rank falls below the median.
    """
    block_ids = np.asarray(block_ids)
    n_cfg = pnl.shape[1]
    n_blocks = len(np.unique(block_ids))
    if n_cfg < 2:
        raise ValueError("pbo needs at least two configurations")
    if n_blocks < 2 or n_blocks % 2:
        raise ValueError(f"pbo needs an even number of blocks >= 2, got {n_blocks}")
    sums, sq, cnt = _block_moments(pnl, block_ids)
    logits = []
    for is_blocks in combinations(range(n_blocks), n_blocks // 2):
        is_mask = np.zeros(n_blocks, dtype=bool)
        is_mask[list(is_blocks)] = True
        sr_is = _sharpe_from_moments(sums[is_mask].sum(0), sq[is_mask].sum(0), cnt[is_mask].sum())
        sr_oos = _sharpe_from_moments(sums[~is_mask].sum(0), sq[~is_mask].sum(0), cnt[~is_mask].sum())
        best = int(np.argmax(sr_is))
        rank = (sr_oos < sr_oos[best]).sum() + 1          # 1 = worst OOS
        omega = rank / (n_cfg + 1)
        logits.append(math.log(omega / (1 - omega)))
    logits = np.asarray(logits)
    return {"pbo": float((logits < 0).mean()), "mean_logit": float(logits.mean()),
            "n_combinations": int(len(logits)), "n_configs": int(n_cfg), "n_blocks": int(n_blocks)}


def binomial_test(successes: int, n: int, p0: float) -> dict:
    """Two-sided exact binomial test of an observed rate against a null rate `p0` (e.g. a
    pooled pin rate against a baseline rate treated as the null). NaN fields when n == 0."""
    if n == 0:
        return {"n": 0, "successes": 0, "rate": float("nan"), "p0": float(p0), "p": float("nan")}
    res = sps.binomtest(int(successes), int(n), float(p0), alternative="two-sided")
    return {"n": int(n), "successes": int(successes), "rate": successes / n, "p0": float(p0),
            "p": float(res.pvalue)}


def mcnemar_test(b: int, c: int) -> dict:
    """Exact McNemar test on the discordant-pair counts of a paired binary comparison: `b` is
    the count where the first condition was true and the second false, `c` the reverse. NaN
    when there are no discordant pairs."""
    b, c = int(b), int(c)
    n = b + c
    if n == 0:
        return {"b": 0, "c": 0, "n": 0, "p": float("nan")}
    p = float(min(2 * sps.binom.cdf(min(b, c), n, 0.5), 1.0))
    return {"b": b, "c": c, "n": n, "p": p}


def nw_t(x, lag: int) -> dict:
    """Mean and Newey-West (Bartlett kernel) t of an ordered series with `lag` autocorrelation
    lags; p from Student t on n - 1 df. NaN for fewer than three observations."""
    x = np.asarray(x, dtype=float)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 3:
        return {"n": int(n), "mean": np.nan, "se": np.nan, "t": np.nan, "p": np.nan, "median": np.nan, "hit": np.nan}
    mu = x.mean()
    e = x - mu
    s = float((e * e).sum())
    for k in range(1, min(lag, n - 1) + 1):
        w = 1 - k / (lag + 1)
        s += 2 * w * float((e[k:] * e[:-k]).sum())
    var = s / n ** 2
    se = math.sqrt(var) if var > 0 else float("nan")
    t = mu / se if se and se > 0 else float("nan")
    p = float(2 * sps.t.sf(abs(t), df=n - 1)) if np.isfinite(t) else float("nan")
    return {"n": int(n), "mean": float(mu), "se": float(se), "t": float(t), "p": p,
            "median": float(np.median(x)), "hit": float((x > 0).mean())}
