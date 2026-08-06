"""Gamma-sign regression tests for scripts/zerodte_setup.py.

Anchored on the live failure of 2026-08-05: the script emitted SPY as
GO_PREMIUM_SELL_INTRADAY labelled "long-gamma: quieter, mean-reverting" while
`uw options-structure gex` read NEGATIVE / dealers short gamma.

The measured cause, from that session's panel and CLI output:

    CLI   dte_max=45  total_gex=+636,479,709  zero_gamma_level=775.97
          underlying_price=771.34             regime=NEGATIVE
    script (same 0-45DTE window)  sum(+-gamma*OI)=+8,260  ->  called it LONG gamma

Both compute the same positive aggregate. The CLI does not use its sign: the
regime is spot-vs-flip, and spot sat 4.63 BELOW the flip. Aggregate sign and
dealer-gamma regime are different quantities and the script conflated them.
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import zerodte_setup as Z  # noqa: E402

pytestmark = pytest.mark.unit


class TestGammaRegime:
    """spot-vs-flip is the convention; the aggregate's sign is not."""

    def test_spot_below_flip_is_short_gamma(self):
        assert Z.gamma_regime(771.34, 775.97) == -1

    def test_spot_above_flip_is_long_gamma(self):
        assert Z.gamma_regime(780.0, 775.97) == +1

    def test_unknown_flip_is_unknown_not_a_guess(self):
        # Fail closed. Returning +1/-1 here is what let the bug ship.
        assert Z.gamma_regime(771.34, None) is None

    def test_spot_exactly_at_flip_is_not_long(self):
        # At the flip the book is pinned; it must not read as the benign branch.
        assert Z.gamma_regime(775.97, 775.97) != +1

    def test_the_2026_08_05_spy_configuration(self):
        """The exact live numbers that broke: positive aggregate, short regime."""
        assert Z.gamma_regime(771.34, 775.97) == -1, (
            "SPY 2026-08-05: spot 771.34 below flip 775.97 is SHORT gamma, "
            "notwithstanding total_gex of +636,479,709"
        )


class TestAggregateSignIsNotTheRegime:
    """The 0-45DTE aggregate keeps its validated job (wing width) and loses the
    job it was never validated for (naming the dealer regime)."""

    def test_positive_aggregate_does_not_imply_long_gamma(self):
        latest = _latest(spot=771.34, zero_gamma_level=775.97, net_gex=+636_479_709)
        out = Z.recommend(latest, _ctx())
        assert out["dealer_gamma_regime"] == "SHORT"
        assert "long-gamma" not in out["suggested_structure"]

    def test_short_gamma_never_labelled_quieter_mean_reverting(self):
        out = Z.recommend(_latest(spot=771.34, zero_gamma_level=775.97), _ctx())
        assert "quieter" not in out["suggested_structure"]
        assert "mean-reverting" not in out["suggested_structure"]


class TestFailClosed:
    def test_unknown_regime_stands_aside(self):
        out = Z.recommend(_latest(spot=771.34, zero_gamma_level=None), _ctx())
        assert out["sell_premium"] is False
        assert out["size_scalar"] == 0.0
        assert "regime" in (out["stand_aside_reason"] or "").lower()

    def test_unknown_regime_does_not_raise(self):
        # `None > 0` used to be a live TypeError path.
        Z.recommend(_latest(spot=771.34, zero_gamma_level=None), _ctx())

    def test_short_gamma_stands_aside(self):
        out = Z.recommend(_latest(spot=771.34, zero_gamma_level=775.97), _ctx())
        assert out["sell_premium"] is False
        assert out["size_scalar"] == 0.0

    def test_long_gamma_may_sell(self):
        out = Z.recommend(_latest(spot=780.0, zero_gamma_level=775.97), _ctx())
        assert out["sell_premium"] is True
        assert out["size_scalar"] > 0


class TestCliIsTheArbiter:
    def test_cli_regime_overrides_a_disagreeing_local_read(self):
        # Local flip says long (spot above); CLI says NEGATIVE. CLI wins.
        latest = _latest(spot=780.0, zero_gamma_level=775.97, cli_regime="NEGATIVE")
        out = Z.recommend(latest, _ctx())
        assert out["dealer_gamma_regime"] == "SHORT"
        assert out["gamma_source"] == "cli"
        assert out["sell_premium"] is False

    def test_disagreement_is_surfaced_not_swallowed(self):
        latest = _latest(spot=780.0, zero_gamma_level=775.97, cli_regime="NEGATIVE")
        out = Z.recommend(latest, _ctx())
        assert out["gamma_disagreement"] is True

    def test_agreement_is_flagged_false(self):
        latest = _latest(spot=771.34, zero_gamma_level=775.97, cli_regime="NEGATIVE")
        assert Z.recommend(latest, _ctx())["gamma_disagreement"] is False

    def test_disagreement_stands_aside_even_when_cli_says_long(self):
        """QQQ, 2026-08-05: CLI POSITIVE, local flip 734.61 vs spot 717.19 = SHORT.

        The CLI wins the *label*, but two sources disagreeing means the regime is
        not reliably known. For a sleeve whose left tail is unsampled, that is a
        stand-aside, not a half-size sell.
        """
        latest = _latest(spot=717.19, zero_gamma_level=734.61, cli_regime="POSITIVE")
        out = Z.recommend(latest, _ctx())
        assert out["dealer_gamma_regime"] == "LONG"
        assert out["gamma_disagreement"] is True
        assert out["sell_premium"] is False
        assert out["size_scalar"] == 0.0


class TestExistingGatesStillHold:
    def test_vix_spike_still_stands_aside(self):
        latest = _latest(spot=780.0, zero_gamma_level=775.97, vix=20.0, vix_prev=17.0)
        out = Z.recommend(latest, _ctx())
        assert out["sell_premium"] is False
        assert "VIX" in (out["stand_aside_reason"] or "")

    def test_backwardation_still_halves_size(self):
        base = Z.recommend(_latest(spot=780.0, zero_gamma_level=775.97), _ctx())
        hot = Z.recommend(
            _latest(spot=780.0, zero_gamma_level=775.97, front_iv=0.30), _ctx()
        )
        assert hot["caution"] is not None
        assert hot["size_scalar"] == pytest.approx(base["size_scalar"] * 0.5)

    def test_pure_math_core_untouched(self):
        assert Z.straddle_pnl_pct(1.0, 0.5) == pytest.approx(0.3)
        assert Z.vol_state(12.0, (15.0, 20.0)) == "LOW"
        assert Z.vol_state(25.0, (15.0, 20.0)) == "HIGH"


# ---------- fixtures ----------------------------------------------------------


def _latest(*, spot, zero_gamma_level, net_gex=+1000.0, cli_regime=None,
            vix=16.0, vix_prev=16.0, front_iv=0.16):
    return {
        "symbol": "SPY",
        "spot": spot,
        "implied_move": 0.9,
        "vix": vix,
        "vix_prev": vix_prev,
        "front_iv": front_iv,
        "net_gex_0_45d": net_gex,
        "zero_gamma_level": zero_gamma_level,
        "cli_gamma_regime": cli_regime,
    }


def _ctx():
    return {
        "vix_tercile_bounds": [15.0, 20.0],
        "long_gamma_mean_range_pct": 0.8,
        "short_gamma_mean_range_pct": 1.4,
    }


class TestRegimeFromBook:
    """No flip level does not mean no regime -- a one-signed book is still known."""

    def test_flip_present_uses_spot_vs_flip(self):
        # cumulative: -5 at K=100, +5 at K=110 -> crossing between; spot below it.
        book = [(100.0, -5.0), (110.0, 10.0)]
        assert Z.zero_gamma_level(book) is not None
        assert Z.gamma_regime_from_book(101.0, book) == -1

    def test_all_positive_book_is_long_without_a_flip(self):
        book = [(100.0, 5.0), (110.0, 7.0)]
        assert Z.zero_gamma_level(book) is None
        assert Z.gamma_regime_from_book(105.0, book) == +1

    def test_all_negative_book_is_short_without_a_flip(self):
        book = [(100.0, -5.0), (110.0, -7.0)]
        assert Z.zero_gamma_level(book) is None
        assert Z.gamma_regime_from_book(105.0, book) == -1

    def test_empty_book_is_unknown(self):
        assert Z.gamma_regime_from_book(105.0, []) is None


class TestRangeBasisIsSeparateFromRegimeBasis:
    """Wing width comes from the AGGREGATE bucket it was measured on; the
    sell/stand-aside decision comes from the spot-vs-flip dealer regime. Measured
    2026-08-05: the aggregate is the better range predictor (corr -0.36 SPY) while
    spot-vs-flip is the correct regime (matches the CLI). Do not re-merge them."""

    def test_range_follows_aggregate_not_regime(self):
        # Regime SHORT (spot below flip) but aggregate POSITIVE -> the 2026-08-05 SPY
        # shape. Wing width must still be quoted off the long-gamma bucket.
        out = Z.recommend(
            _latest(spot=771.34, zero_gamma_level=775.97, net_gex=+636_479_709), _ctx())
        assert out["dealer_gamma_regime"] == "SHORT"
        assert out["expected_range_pct"] == _ctx()["long_gamma_mean_range_pct"]

    def test_negative_aggregate_quotes_the_wider_bucket(self):
        out = Z.recommend(
            _latest(spot=780.0, zero_gamma_level=775.97, net_gex=-1000.0), _ctx())
        assert out["dealer_gamma_regime"] == "LONG"
        assert out["expected_range_pct"] == _ctx()["short_gamma_mean_range_pct"]
