"""D13: `make narrate` writes a facts page beside the sheet, fail-soft, and changes no number."""
from __future__ import annotations

import json
import os
from datetime import date

import pytest

from engine.name import narrate as N

pytestmark = pytest.mark.unit

D = date(2026, 9, 18)


def test_finnhub_news_parses_and_sorts_headlines():
    raw = [{"datetime": 1758000000, "headline": "b", "source": "x", "url": "u"},
           {"datetime": 1758100000, "headline": "a", "source": "y", "url": "v"}]
    out = N.finnhub_news("NVDA", D, "k", getter=lambda url: raw)
    assert out["available"] and [r["headline"] for r in out["rows"]] == ["a", "b"]


def test_finnhub_news_is_fail_soft_and_scrubs_the_key():
    def boom(url):
        raise RuntimeError("HTTP 429 token=SECRETKEY")
    out = N.finnhub_news("NVDA", D, "SECRETKEY", getter=boom)
    assert not out["available"] and "SECRETKEY" not in out["reason"] and out["rows"] == []
    assert N.finnhub_news("NVDA", D, None)["reason"] == "no FINNHUB_API_KEY"


def test_checklist_without_a_sheet_says_so():
    lines = N.checklist(None)
    assert len(lines) == len(N.CHECKLIST) and all("no sheet" in l for l in lines)


def test_run_writes_narrate_md_beside_the_sheet(tmp_path):
    out_dir = tmp_path / "NVDA" / D.isoformat()
    out_dir.mkdir(parents=True)
    sheet = {"events": {"earnings": {"date": "2026-11-17", "confirmed": True, "days_to": 60}},
             "premium": {"x1": False, "verdict": "FAIR", "spread_rv5": 6.5},
             "flags": {"borrow": {"decile": 0.1, "fee": 0.25, "available": 1e7}, "si": {"pct_float": 0.013, "dtc": 2.1}, "x2": False, "x5": False},
             "liquidity": {"can_price": True, "failing": None, "contracts": 2051, "hot_chain_days": 21}}
    (out_dir / "ticker.json").write_text(json.dumps(sheet))
    path = N.run("NVDA", D, str(tmp_path), key="k",
                 news_fn=lambda t, d, k: {"available": True, "reason": None, "rows": [{"date": "2026-09-17", "headline": "h", "source": "s", "url": None}]},
                 analyst_fn=lambda t, s, e: {"available": True, "reason": None, "value": [{"date": "2026-09-04", "firm": "F", "from": "Buy", "to": "Buy", "action": "reit"}]},
                 form4_fn=lambda t, d, k: {"available": False, "reason": "offline", "value": None})
    assert path == str(out_dir / "narrate.md") and os.path.exists(path)
    text = open(path).read()
    assert "earnings inside the window: 2026-11-17 (confirmed, 60 days)" in text and "- 2026-09-17 · h (s)" in text
    assert "F: Buy -> Buy" in text and "## Form 4" in text and "- none" in text
    assert json.load(open(out_dir / "ticker.json")) == sheet          # changes no number
