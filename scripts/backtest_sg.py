#!/usr/bin/env python3
"""Thin CLI entry point for the S-G backtest (DESIGN/91 §6 G3-code). Delegates entirely to
`engine.backtest_sg`; `make backtest-sg` calls the module form directly (`python3 -m
engine.backtest_sg`), matching S-A/S-B convention. This wrapper exists so the backtest can also be
run as `python3 scripts/backtest_sg.py` per DESIGN/91 §6.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.backtest_sg import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
