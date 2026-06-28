#!/usr/bin/env python3
"""Validate a market-scan (v2) or weekly-review envelope against its JSON Schema.
Routes by report_kind / schema_version. Exit 0 = valid, 1 = invalid (prints the error path).
Usage: python3 scripts/validate_decision.py --file analyses/scan/2026-06-26/decision.json
"""
import argparse, json, os, sys
import jsonschema

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMAS = os.path.join(HERE, "..", "schemas")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    a = ap.parse_args()
    try:
        env = json.load(open(a.file))
    except Exception as e:
        print(f"INVALID: cannot parse {a.file}: {e}"); return 1
    kind = env.get("report_kind")
    if kind == "weekly-review":
        schema_path = os.path.join(SCHEMAS, "weekly_review.schema.json")
    elif kind == "market-scan" or env.get("schema_version") == "2.0":
        schema_path = os.path.join(SCHEMAS, "decision_envelope.v2.schema.json")
    else:
        print(f"INVALID: unknown report_kind/schema_version in {a.file}"); return 1
    schema = json.load(open(schema_path))
    try:
        jsonschema.validate(env, schema)
    except jsonschema.ValidationError as e:
        print(f"INVALID: {a.file}\n  at: {'/'.join(str(p) for p in e.absolute_path)}\n  {e.message}")
        return 1
    print(f"VALID: {a.file} ({kind})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
