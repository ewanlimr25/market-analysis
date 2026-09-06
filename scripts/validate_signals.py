#!/usr/bin/env python3
"""Validate one or more `analyses/daily/<date>/signals.json` files against schemas/signals.schema.json.
Exit 0 = every file valid, 1 = any invalid (prints each violation with its path).
Usage: python3 scripts/validate_signals.py --file analyses/daily/2026-09-04/signals.json [more files]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from engine import schema as SCH  # noqa: E402


def check(path: str, schema: dict) -> bool:
    try:
        with open(path) as fh:
            signals = json.load(fh, parse_constant=lambda c: (_ for _ in ()).throw(ValueError(f"non-finite number {c}")))
    except (OSError, ValueError) as exc:
        print(f"INVALID: cannot parse {path}: {exc}")
        return False
    errors = SCH.validate(signals, schema)
    if errors:
        print(f"INVALID: {path}")
        for e in errors:
            print(f"  {e}")
        return False
    print(f"VALID: {path} ({signals.get('report_kind')} {signals.get('schema_version')})")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, nargs="+")
    a = ap.parse_args()
    schema = SCH.load_schema()
    ok = [check(p, schema) for p in a.file]
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main())
