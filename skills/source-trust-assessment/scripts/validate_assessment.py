#!/usr/bin/env python3
"""Validate a source trust assessment JSON against the methodology rules.

Usage:
    python validate_assessment.py assessment.json [more.json ...]
    python validate_assessment.py -          # read one assessment from stdin

Checks the structure defined in assets/assessment.schema.json (a subset of JSON Schema
implemented with the standard library, so no installation is needed) and the methodology
rules that a schema cannot express:

- trust.code equals sourceReliability + informationCredibility
- AI-only assessments are not "verified"
- certified-expert assessments name the assessor and authorization
- a legal act with legalStatus "n/a" or non-legal content with a legal status is flagged
- criteria evidence indexes point to existing evidence items

Exit codes: 0 valid, 1 invalid, 2 usage or read error.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "assets" / "assessment.schema.json"
AI_ONLY = {"ai"}
EXPERTS = {"expert", "certified-expert", "ai+expert", "ai+certified-expert"}


def check_schema(value, schema: dict, path: str, errors: list[str]) -> None:
    """Minimal JSON Schema subset: type, enum, const, required, properties, additionalProperties,
    items, minLength, minimum, pattern."""
    import re

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must be {schema['const']!r}")
        return
    if "enum" in schema:
        if value not in schema["enum"]:
            errors.append(f"{path}: {value!r} is not one of {schema['enum']}")
        return
    types = schema.get("type")
    if types:
        types = [types] if isinstance(types, str) else types
        checks = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
        ok = any((t == "integer" and isinstance(value, int) and not isinstance(value, bool))
                 or (t in checks and isinstance(value, checks[t])) for t in types)
        if not ok:
            errors.append(f"{path}: expected {'/'.join(types)}, got {type(value).__name__}")
            return
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: must not be empty")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, int) and "minimum" in schema and value < schema["minimum"]:
        errors.append(f"{path}: must be >= {schema['minimum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: required")
        props = schema.get("properties", {})
        for key, item in value.items():
            if key in props:
                check_schema(item, props[key], f"{path}.{key}", errors)
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key}: unknown field")
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            check_schema(item, schema["items"], f"{path}[{i}]", errors)


def check_rules(doc: dict, errors: list[str], warnings: list[str]) -> None:
    trust = doc.get("trust") or {}
    rel, cred = trust.get("sourceReliability"), trust.get("informationCredibility")
    if rel and cred and trust.get("code") != f"{rel}{cred}":
        errors.append(f"trust.code: must be {rel}{cred}")
    by = trust.get("assessedBy")
    if by in AI_ONLY and trust.get("verificationStatus") == "verified":
        errors.append("trust.verificationStatus: AI-only assessment cannot be 'verified'")
    if trust.get("verificationStatus") == "verified" and by not in EXPERTS:
        warnings.append("trust.verificationStatus: 'verified' should involve an expert assessor")
    if by in ("certified-expert", "ai+certified-expert"):
        assessor = trust.get("assessor") or {}
        if not assessor.get("name") or not assessor.get("authorization"):
            errors.append("trust.assessor: certified-expert requires name and authorization")
    authority, status = trust.get("legalAuthority"), trust.get("legalStatus")
    if authority and authority != "none" and status == "n/a":
        errors.append("trust.legalStatus: a legal act needs in-force, draft or repealed")
    if authority == "none" and status in ("in-force", "draft", "repealed"):
        warnings.append("trust.legalStatus: content without legal authority usually has 'n/a'")
    evidence = doc.get("evidence") or []
    for i, crit in enumerate(doc.get("criteria") or []):
        for idx in crit.get("evidence", []):
            if isinstance(idx, int) and idx >= len(evidence):
                errors.append(f"criteria[{i}].evidence: index {idx} out of range")
    if cred == 1 and not any(e.get("relation") == "confirms" for e in evidence):
        warnings.append("trust.informationCredibility: 1 (confirmed) without confirming evidence")
    methodology = doc.get("methodology") or {}
    if methodology.get("modified") and not methodology.get("modifications"):
        errors.append("methodology.modifications: describe what was modified")


def validate(doc, schema: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    check_schema(doc, schema, "$", errors)
    if isinstance(doc, dict):
        check_rules(doc, errors, warnings)
    return errors, warnings


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__, file=sys.stderr)
        return 2
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    status = 0
    for name in argv:
        try:
            text = sys.stdin.read() if name == "-" else Path(name).read_text(encoding="utf-8")
            doc = json.loads(text)
        except (OSError, json.JSONDecodeError) as e:
            print(f"{name}: cannot read: {e}", file=sys.stderr)
            return 2
        errors, warnings = validate(doc, schema)
        for w in warnings:
            print(f"{name}: warning: {w}")
        for e in errors:
            print(f"{name}: error: {e}")
        if errors:
            status = 1
        else:
            print(f"{name}: valid")
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
