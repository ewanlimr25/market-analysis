"""The `signals.json` contract (schemas/signals.schema.json, `d1.0`).

`make daily` stamps every run with `schema_version` and `report_kind`, writes strict JSON (no NaN,
no Infinity), and validates the file it just wrote. Validation never blocks the nightly: a drift is
reported as a WARN line and the file is still the record. Consumers (findings DESIGN/95) mirror the
schema and route by `report_kind`, as they do for the two journal envelopes.
"""
from __future__ import annotations

import json
import math
import os
from datetime import date, datetime
from typing import Any

import jsonschema

from engine.config import REPO

SCHEMA_VERSION = "d1.0"
REPORT_KIND = "engine-daily"
SCHEMA_PATH = os.path.join(REPO, "schemas", "signals.schema.json")


def load_schema(path: str = SCHEMA_PATH) -> dict:
    with open(path) as fh:
        return json.load(fh)


def stamp(signals: dict) -> dict:
    """A new dict with the contract keys first."""
    return {"schema_version": SCHEMA_VERSION, "report_kind": REPORT_KIND, **signals}


def clean(value: Any) -> Any:
    """Strict-JSON copy: NaN/inf -> null, dates -> ISO strings, numpy scalars -> Python."""
    if isinstance(value, dict):
        return {str(k): clean(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, bool):
        return value
    if isinstance(value, float):
        return None if (math.isnan(value) or math.isinf(value)) else value
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if hasattr(value, "item") and not isinstance(value, (str, bytes)):   # numpy scalar
        return clean(value.item())
    return value


def validate(signals: dict, schema: dict | None = None) -> list[str]:
    """Every violation as `path: message`, sorted; an empty list means valid."""
    validator = jsonschema.Draft7Validator(schema or load_schema())
    errors = []
    for err in validator.iter_errors(signals):
        path = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{path}: {err.message}")
    return sorted(errors)


def dumps(signals: dict) -> str:
    """Strict JSON text (`allow_nan=False` guarantees a NaN can never reach the file)."""
    return json.dumps(clean(signals), indent=1, allow_nan=False)
