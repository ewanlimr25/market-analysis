"""engine.mart.earnings_events: E1's event construction, promoted and partitioned by `pre`.

Unit tests run on a synthetic screener + price panel built in tmp_path; the integration tests
rebuild the real table and compare it against the recorded E1 artifact.
"""
from __future__ import annotations

import glob
import os
from datetime import date, timedelta

import duckdb
import pandas as pd
import pytest

from engine import calendar as cal
from engine import config
from engine.mart import earnings_events as ee
from engine.mart import store
from engine.mart import vix as vixmod

PANEL_START, PANEL_END = date(2026, 3, 2), date(2026, 10, 30)
CAL = cal.trading_days(PANEL_START, PANEL_END)
E_APR = date(2026, 4, 15)                      # Wednesday
E_APR_PREV, E_APR_NEXT = date(2026, 4, 14), date(2026, 4, 16)
SEASON_EVENTS = {"S1": E_APR, "off": date(2026, 6, 24), "S2": date(2026, 7, 22), "S3": date(2026, 10, 14)}
FAR_NED_DAYS = 91
BASE_VOLUME, VOLUME_STEP = 1_000_000, 10_000
STUB_VIX = {E_APR: 17.5}

E1_ARTIFACT = os.path.expanduser("~/Development/findings/market-analysis/artifacts/vol/out/e1_events.parquet")
REAL_SCREENER = os.path.join(config.STOCKS, config.SCREENER_GLOB)
MEGA_CAPS = [("MSFT", date(2026, 4, 29)), ("META", date(2026, 4, 29)), ("GOOGL", date(2026, 4, 29)),
             ("AAPL", date(2026, 4, 30)), ("AMZN", date(2026, 4, 29)),   # AMZN printed 04-29 in the artifact
             ("NVDA", date(2026, 5, 20)), ("NVDA", date(2026, 8, 26))]


# ---- synthetic panel ----------------------------------------------------------------------------
def _screener_rows(ticker: str, E: date, er_time: str | None | list, iv_prev: float = 0.60,
                   iv_E: float | None = None, iv_next: float | None = None, implied: float = 0.05,
                   ned_at_E: date | None = None, issue_type: str = "Common Stock",
                   avg30_volume: float = 2e6) -> list[dict]:
    """Screener rows on every session in [E - 14d, E] carrying ned = E, plus the session after E."""
    e_prev, e_next = cal.prev_session(E), cal.next_session(E)
    iv = {e_prev: iv_prev, E: iv_prev if iv_E is None else iv_E, e_next: iv_prev if iv_next is None else iv_next}
    window = [d for d in CAL if E - timedelta(days=ee.CANDIDATE_LOOKBACK_DAYS) <= d <= E] + [e_next]
    rows = []
    for k, d in enumerate(window):
        ned = E if d <= E else E + timedelta(days=FAR_NED_DAYS)
        if d == E and ned_at_E is not None:
            ned = ned_at_E
        label = er_time[k % len(er_time)] if isinstance(er_time, list) else er_time
        rows.append({"date": d, "ticker": ticker, "next_earnings_date": ned, "er_time": label,
                     "implied_move_perc": implied, "iv30d": iv.get(d, iv_prev), "iv_rank": 42.0,
                     "marketcap": 5e9, "sector": "Industrials", "close": 99.0, "issue_type": issue_type,
                     "avg30_volume": avg30_volume})
    return rows


def _price_rows(ticker: str, close: float, overrides: dict[date, float] | None = None,
                start: date = PANEL_START, varying_volume: bool = False) -> list[dict]:
    rows = []
    for k, d in enumerate(CAL):
        if d < start:
            continue
        c = (overrides or {}).get(d, close)
        v = BASE_VOLUME + VOLUME_STEP * k if varying_volume else BASE_VOLUME
        rows.append({"ticker": ticker, "date": d, "open": c, "high": c, "low": c, "close": c,
                     "adjclose": c, "volume": v})
    return rows


def _write_screener(stocks_dir: str, rows: list[dict]) -> str:
    folder = os.path.join(stocks_dir, "Stock Screener")
    os.makedirs(folder, exist_ok=True)
    frame = pd.DataFrame(rows).astype({"er_time": "string", "sector": "string", "issue_type": "string"})
    for d, part in frame.groupby("date"):
        part.to_parquet(os.path.join(folder, f"stock-screener-{d.isoformat()}.parquet"), index=False)
    return os.path.join(stocks_dir, config.SCREENER_GLOB)


def _sessions_ending(d: date, n: int) -> list[date]:
    i = CAL.index(d)
    return CAL[i - n + 1: i + 1]


@pytest.fixture(scope="module")
def panel(tmp_path_factory) -> dict:
    root = str(tmp_path_factory.mktemp("panel"))
    scr = (_screener_rows("PM", E_APR, "postmarket")
           + _screener_rows("AM", E_APR, "premarket", implied=0.04)
           + _screener_rows("INFP", E_APR, None, iv_prev=0.60, iv_E=0.40, iv_next=0.38)
           + _screener_rows("INFQ", E_APR, None, iv_prev=0.60, iv_E=0.62, iv_next=0.40)
           + _screener_rows("UNR", E_APR, None, iv_prev=0.60, iv_E=0.59, iv_next=0.58)
           + _screener_rows("TIE", E_APR, ["postmarket", "unknown"], iv_prev=0.60, iv_E=0.40, iv_next=0.38)
           + _screener_rows("MAJ", E_APR, ["postmarket", "postmarket", "unknown"], iv_prev=0.60, iv_E=0.40)
           + _screener_rows("NED", E_APR, "postmarket", ned_at_E=date(2026, 4, 22))
           + _screener_rows("CHEAP", E_APR, "postmarket")
           + _screener_rows("ETFX", E_APR, "postmarket", issue_type="ETF")
           + _screener_rows("NEWT", E_APR, "postmarket", avg30_volume=3e6)
           + _screener_rows("PART", E_APR, "postmarket")
           + sum((_screener_rows("SEAS", E, "postmarket") for E in SEASON_EVENTS.values()), []))
    prices = {
        "SPY": _price_rows("SPY", 500.0),
        "PM": _price_rows("PM", 100.0, {E_APR_NEXT: 108.0}, varying_volume=True),
        "AM": _price_rows("AM", 50.0, {E_APR: 47.0}),
        "INFP": _price_rows("INFP", 20.0), "INFQ": _price_rows("INFQ", 20.0), "UNR": _price_rows("UNR", 20.0),
        "NED": _price_rows("NED", 20.0), "CHEAP": _price_rows("CHEAP", 4.0), "ETFX": _price_rows("ETFX", 20.0),
        "TIE": _price_rows("TIE", 20.0), "MAJ": _price_rows("MAJ", 20.0),
        "NEWT": _price_rows("NEWT", 30.0, start=_sessions_ending(E_APR, 5)[0]),
        "PART": _price_rows("PART", 40.0, start=_sessions_ending(E_APR, 12)[0], varying_volume=True),
        "SEAS": _price_rows("SEAS", 100.0, {cal.next_session(E): 105.0 for E in SEASON_EVENTS.values()}),
    }
    prices_path = os.path.join(root, "prices.parquet")
    pd.DataFrame(sum(prices.values(), [])).to_parquet(prices_path, index=False)
    return {"stocks_dir": root, "screener_glob": _write_screener(root, scr), "prices_path": prices_path,
            "prices": prices, "e_min": cal.next_session(PANEL_START), "e_max": cal.prev_session(PANEL_END)}


def _stub_regime(d: date) -> str:
    return "CHOP"


def _stub_vix(d: date) -> float | None:
    return STUB_VIX.get(d)


def _build(panel: dict, **kw) -> pd.DataFrame:
    return ee.build_events(duckdb.connect(), panel["screener_glob"], panel["prices_path"],
                           panel["e_min"], panel["e_max"], regime_fn=_stub_regime, vix_fn=_stub_vix, **kw)


@pytest.fixture(scope="module")
def events(panel) -> pd.DataFrame:
    return _build(panel)


def _row(events: pd.DataFrame, ticker: str, E: date = E_APR) -> pd.Series:
    sub = events[(events.ticker == ticker) & (events.E == E)]
    assert len(sub) == 1, f"{ticker} {E}: {len(sub)} rows"
    return sub.iloc[0]


# ---- unit: timing rule --------------------------------------------------------------------------
@pytest.mark.unit
def test_labelled_postmarket_uses_E_and_next_session(events):
    r = _row(events, "PM")
    assert (r.timing, r.how, r.er_time) == ("postmarket", "labelled", "postmarket")
    assert (r.pre, r.post, r.date) == (E_APR, E_APR_NEXT, E_APR)


@pytest.mark.unit
def test_labelled_premarket_uses_prev_session_and_E(events):
    r = _row(events, "AM")
    assert (r.timing, r.how) == ("premarket", "labelled")
    assert (r.pre, r.post, r.date) == (E_APR_PREV, E_APR, E_APR_PREV)


@pytest.mark.unit
def test_unlabelled_crush_on_E_is_inferred_premarket(events):
    r = _row(events, "INFP")
    assert (r.timing, r.how, r.er_time) == ("premarket", "inferred", "unknown")
    assert (r.pre, r.post) == (E_APR_PREV, E_APR)
    assert r.iv30d_pre == pytest.approx(0.60) and r.iv30d_post == pytest.approx(0.40)


@pytest.mark.unit
def test_unlabelled_crush_on_next_session_is_inferred_postmarket(events):
    r = _row(events, "INFQ")
    assert (r.timing, r.how) == ("postmarket", "inferred")
    assert (r.pre, r.post) == (E_APR, E_APR_NEXT)


@pytest.mark.unit
def test_unlabelled_without_crush_is_unresolved_two_session_window(events):
    r = _row(events, "UNR")
    assert (r.timing, r.how) == ("unresolved", "2-session")
    assert (r.pre, r.post) == (E_APR_PREV, E_APR_NEXT)


@pytest.mark.unit
def test_label_tie_in_window_is_unlabelled_and_goes_to_inference(events):
    tie, maj = _row(events, "TIE"), _row(events, "MAJ")
    assert (tie.er_time, tie.timing, tie.how) == ("unknown", "premarket", "inferred")
    assert (maj.er_time, maj.timing, maj.how) == ("postmarket", "postmarket", "labelled")


# ---- unit: filters ----------------------------------------------------------------------------
@pytest.mark.unit
def test_filters_drop_rescheduled_cheap_and_etf_names(events):
    assert not set(events.ticker) & {"NED", "CHEAP", "ETFX"}
    assert set(events.ticker) == {"PM", "AM", "INFP", "INFQ", "UNR", "TIE", "MAJ", "NEWT", "PART", "SEAS"}


# ---- unit: arithmetic -------------------------------------------------------------------------
@pytest.mark.unit
def test_move_arithmetic_on_known_closes(events):
    pm, am = _row(events, "PM"), _row(events, "AM")
    assert (pm.spot_pre, pm.close_post) == (100.0, 108.0)
    assert pm.gap_signed == pytest.approx(0.08) and pm.realized_move == pytest.approx(0.08)
    assert pm.implied_move_perc == pytest.approx(0.05) and pm.proxy_pnl == pytest.approx(-0.03)
    assert (am.spot_pre, am.close_post) == (50.0, 47.0)
    assert am.gap_signed == pytest.approx(-0.06) and am.realized_move == pytest.approx(0.06)
    assert am.proxy_pnl == pytest.approx(0.04 - 0.06)


@pytest.mark.unit
def test_runup_columns_look_five_sessions_back(events):
    r = _row(events, "PM")
    assert r.imp_5d_ago == pytest.approx(0.05) and r.iv30d_5d_ago == pytest.approx(0.60)
    assert r.iv_rank_pre == 42.0 and r.marketcap == 5e9 and r.sector == "Industrials"
    assert r.issue_type == "Common Stock"


# ---- unit: dollar ADV -------------------------------------------------------------------------
@pytest.mark.unit
def test_adv_usd_20d_is_mean_dollar_volume_over_twenty_sessions(events, panel):
    r = _row(events, "PM")
    window = set(_sessions_ending(E_APR, ee.ADV_WINDOW_SESSIONS))
    dv = [p["close"] * p["volume"] for p in panel["prices"]["PM"] if p["date"] in window]
    assert len(dv) == 20
    assert r.adv_usd_20d == pytest.approx(sum(dv) / 20)
    assert r.adv_usd_30d == pytest.approx(2e6 * 100.0)


@pytest.mark.unit
def test_adv_usd_20d_uses_partial_window_when_at_least_ten_sessions(events, panel):
    r = _row(events, "PART")
    dv = [p["close"] * p["volume"] for p in panel["prices"]["PART"] if p["date"] <= E_APR]
    assert len(dv) == 12
    assert r.adv_usd_20d == pytest.approx(sum(dv) / 12)


@pytest.mark.unit
def test_adv_usd_20d_falls_back_to_screener_adv_when_under_ten_sessions(events):
    r = _row(events, "NEWT")
    assert r.adv_usd_30d == pytest.approx(3e6 * 30.0)
    assert r.adv_usd_20d == pytest.approx(r.adv_usd_30d)


# ---- unit: enrichment -------------------------------------------------------------------------
@pytest.mark.unit
def test_season_and_month_labels_on_pre(events):
    for label, E in SEASON_EVENTS.items():
        r = _row(events, "SEAS", E)
        assert r.season == label, (E, r.season)
        assert r.month == E.strftime("%Y-%m")


@pytest.mark.unit
def test_regime_and_vix_come_from_injected_callables(events):
    pm, am = _row(events, "PM"), _row(events, "AM")
    assert pm.regime_pre == "CHOP" and pm.vix_pre == 17.5
    assert pd.isna(am.vix_pre)


@pytest.mark.unit
def test_output_columns_are_exactly_the_spec(events):
    assert list(events.columns) == ee.COLUMNS


# ---- unit: partitioning -------------------------------------------------------------------------
@pytest.mark.unit
def test_pre_only_returns_that_dates_rows(panel):
    sub = _build(panel, pre_only=E_APR)
    assert set(sub.pre) == {E_APR}
    assert set(sub.ticker) == {"PM", "INFQ", "MAJ", "NEWT", "PART", "SEAS"}


@pytest.mark.unit
def test_build_day_writes_a_readable_partition(panel, tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(config, "STOCKS", panel["stocks_dir"])
    monkeypatch.setattr(config, "PRICES", panel["prices_path"])
    out = ee.build_day(E_APR, duckdb.connect(), regime_fn=_stub_regime, vix_fn=_stub_vix)
    assert store.has_partition(ee.TABLE, E_APR)
    back = store.read_partition(ee.TABLE, E_APR)
    assert set(back.ticker) == set(out.ticker) == {"PM", "INFQ", "MAJ", "NEWT", "PART", "SEAS"}
    assert set(back.date) == {E_APR} and list(back.columns) == ee.COLUMNS


@pytest.mark.unit
def test_build_day_rejects_non_trading_day():
    with pytest.raises(ValueError):
        ee.build_day(date(2026, 4, 18), duckdb.connect())


@pytest.mark.unit
def test_season_of_uses_config_windows():
    assert ee.season_of(date(2026, 4, 1)) == "S1" and ee.season_of(date(2026, 6, 15)) == "S1"
    assert ee.season_of(date(2026, 6, 16)) == "off" and ee.season_of(date(2026, 9, 4)) == "S2"
    assert ee.season_of(date(2026, 10, 1)) == "S3" and ee.season_of(date(2026, 12, 1)) == "off"


# ---- unit: vix loader -------------------------------------------------------------------------
@pytest.mark.unit
def test_load_vix_reads_mart_file_when_present(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path))
    os.makedirs(os.path.dirname(vixmod.vix_path()), exist_ok=True)
    pd.DataFrame({"date": [date(2026, 4, 15)], "vix": [17.5]}).to_parquet(vixmod.vix_path(), index=False)
    monkeypatch.setattr(vixmod, "fetch_vix", lambda rng=None: pytest.fail("must not fetch"))
    out = vixmod.load_vix()
    assert list(out.columns) == ["date", "vix"] and out.date.tolist() == [date(2026, 4, 15)]


@pytest.mark.unit
def test_load_vix_falls_back_to_e4_artifact_without_raising(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    fallback = tmp_path / "e4.parquet"
    pd.DataFrame({"date": ["2026-04-14", "2026-04-15"], "vix": [18.0, 17.5], "spy": [1.0, 2.0]}).to_parquet(fallback)
    monkeypatch.setattr(vixmod, "E4_VRP_FALLBACK", str(fallback))

    def boom(rng=None):
        raise OSError("no network")
    monkeypatch.setattr(vixmod, "fetch_vix", boom)
    out = vixmod.load_vix()
    assert out.date.tolist() == [date(2026, 4, 14), date(2026, 4, 15)] and out.vix.tolist() == [18.0, 17.5]
    assert "no network" in capsys.readouterr().out


@pytest.mark.unit
def test_load_vix_returns_empty_frame_when_nothing_available(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MART", str(tmp_path / "mart"))
    monkeypatch.setattr(vixmod, "E4_VRP_FALLBACK", str(tmp_path / "missing.parquet"))
    monkeypatch.setattr(vixmod, "fetch_vix", lambda rng=None: (_ for _ in ()).throw(OSError("offline")))
    out = vixmod.load_vix()
    assert out.empty and list(out.columns) == ["date", "vix"]


# ---- integration: rebuild == E1 artifact --------------------------------------------------------
needs_real_data = pytest.mark.skipif(
    not (glob.glob(REAL_SCREENER) and os.path.exists(config.PRICES) and os.path.exists(E1_ARTIFACT)),
    reason="screener panel, price panel or E1 artifact not on disk")


@pytest.fixture(scope="module")
def rebuilt_and_artifact() -> tuple[pd.DataFrame, pd.DataFrame]:
    con = duckdb.connect()
    e_min, panel_max = ee.default_event_range(con, REAL_SCREENER)
    e_max = date(2026, 9, 3)                  # the E1 artifact's last event; the panel keeps growing past it
    assert e_min == date(2026, 3, 16) and panel_max >= e_max
    ours = ee.build_events(con, REAL_SCREENER, config.PRICES, e_min, e_max,
                           regime_fn=_stub_regime, vix_fn=_stub_vix)
    return ours, pd.read_parquet(E1_ARTIFACT)


@pytest.mark.integration
@needs_real_data
def test_rebuild_matches_e1_event_set(rebuilt_and_artifact):
    ours, e1 = rebuilt_and_artifact
    assert len(ours) == 3260 and len(e1) == 3260
    assert set(zip(ours.ticker, ours.E)) == set(zip(e1.ticker, e1.E))
    assert ours.pre.nunique() == 97


@pytest.mark.integration
@needs_real_data
def test_rebuild_matches_e1_windows_and_timing(rebuilt_and_artifact):
    ours, e1 = rebuilt_and_artifact
    m = ours.merge(e1, on=["ticker", "E"], suffixes=("", "_e1"))
    assert len(m) == 3260
    for col in ("pre", "post", "timing"):
        assert (m[col] == m[f"{col}_e1"]).all(), col
    # One documented `how` difference: JEF 2026-06-24 carried a 5-5 tie between 'postmarket' and
    # 'unknown' over its 14-day window; E1's DuckDB mode() happened to return the label, the
    # deterministic plurality rule here calls it unlabelled and the crush inference then gives the
    # SAME postmarket timing. pre/post/timing/P&L are identical; only the provenance label moves.
    diff = m[m.how != m.how_e1]
    assert list(zip(diff.ticker, diff.E.astype(str))) == [("JEF", "2026-06-24")]
    assert ours.timing.value_counts().to_dict() == {"postmarket": 1593, "premarket": 1478, "unresolved": 189}
    assert ours.how.value_counts().to_dict() == {"labelled": 2988, "2-session": 189, "inferred": 83}


@pytest.mark.integration
@needs_real_data
def test_rebuild_matches_e1_pnl(rebuilt_and_artifact):
    ours, e1 = rebuilt_and_artifact
    assert abs(ours.proxy_pnl.mean() - e1.pnl.mean()) < 1e-9
    m = ours.merge(e1, on=["ticker", "E"], suffixes=("", "_e1"))
    assert (m.spot_pre == m.c_pre).all() and (m.close_post == m.c_post).all()
    assert (m.adv_usd_30d.fillna(-1) == m.adv_usd.fillna(-1)).all()


@pytest.mark.integration
@needs_real_data
def test_rebuild_matches_e1_on_hand_checked_mega_caps(rebuilt_and_artifact):
    ours, e1 = rebuilt_and_artifact
    for ticker, E in MEGA_CAPS:
        a = e1[(e1.ticker == ticker) & (e1.E == E)].iloc[0]
        b = ours[(ours.ticker == ticker) & (ours.E == E)].iloc[0]
        assert (b.pre, b.post) == (a.pre, a.post), (ticker, E)
