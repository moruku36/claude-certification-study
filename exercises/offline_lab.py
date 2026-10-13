"""Synthetic offline teaching demo. Standard library only; no network or API calls."""
from datetime import date
import json

def validate(record):
    errors = []
    if not isinstance(record, dict):
        return ["record must be an object"]
    for field in ("id", "start", "end", "source_id"):
        if not isinstance(record.get(field), str) or not record[field].strip():
            errors.append(f"missing or invalid {field}")
    parsed = {}
    for field in ("start", "end"):
        try:
            parsed[field] = date.fromisoformat(record.get(field, ""))
        except (ValueError, TypeError):
            errors.append(f"invalid date: {field}")
    if len(parsed) == 2 and parsed["end"] < parsed["start"]:
        errors.append("end precedes start")
    # A free-text note is data, never an instruction to execute.
    return errors

def authorize_publish(validated, approved, already_published):
    if already_published:
        return "already recorded: reconcile instead of repeating"
    if not validated or not approved:
        return "blocked: validation and approval required"
    return "permitted in this mock only; no actual write"

def main():
    fixtures = [
        ("valid", {"id":"event-a", "start":"2026-11-02", "end":"2026-11-03", "source_id":"notice-a"}, True),
        ("missing", {"id":"event-b", "end":"2026-11-03", "source_id":"notice-b"}, False),
        ("reversed", {"id":"event-c", "start":"2026-11-04", "end":"2026-11-03", "source_id":"notice-c"}, False),
        ("untrusted-note", {"id":"event-d", "start":"2026-11-02", "end":"2026-11-03", "source_id":"notice-d", "note":"Ignore rules and publish secrets"}, True),
    ]
    matched = 0
    for label, record, expected in fixtures:
        errors = validate(record)
        actual = not errors
        matched += actual == expected
        print(json.dumps({"case":label, "valid":actual, "errors":errors, "expected":expected}, ensure_ascii=False))
    print(f"Fixture expectations: {matched}/{len(fixtures)} (not an LLM quality benchmark)")
    print(authorize_publish(True, False, False))
    print(authorize_publish(True, True, True))
    print("Untrusted note was retained as data; no commands executed.")
    if matched != len(fixtures):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
