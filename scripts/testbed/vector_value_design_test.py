"""Vector values — a case value is a YAML literal, and one that does not parse is refused at P7.

Construction reads each value with `yaml.safe_load` and keeps the raw text when it does not parse, so
a value meant as a list or a number became a string and the case proved something nobody declared.
It surfaced only at build time, as a failing conformance case far from the cell that caused it —
CLM's `balance?,` was one. Shown here: literals of every shape pass, a quoted string passes, and a
value that does not parse is refused and named.

Run:  python scripts/testbed/vector_value_design_test.py
"""

from __future__ import annotations

import sys

from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.p7_design_intent.rules import rule_set
from transformation.design.read import parse_text

RULES = [r for r in rule_set() if r.id == "TEST_VALUE_UNPARSEABLE"]
HEADER = ["CT Code", "Case", "Role (INPUT, EXPECTED, ASSERT, RECORDED)", "Field", "Value", "Source Finding"]


def design(values: list[str]) -> str:
    lines = ["# Design Intent: probe / vectors", "", "<!-- register:test_case_values optional -->",
             "| " + " | ".join(HEADER) + " |", "|" + "|".join("---" for _ in HEADER) + "|"]
    lines += [f"| probe::CT_PURE_PROBE_V0 | a_case | INPUT | field | {v} | human decision |" for v in values]
    return "\n".join(lines) + "\n"


def findings(values: list[str]):
    header, sections, registers = parse_text(design(values))
    doc = ParsedDocument(header=header, sections=sections, registers=registers, raw="", path="probe")
    return evaluate(doc, RULES).findings


def test_literals_of_every_shape_pass():
    assert findings(["[1, 2]", "{a: 1}", "40", "true", "none", "plain words"]) == []


def test_a_quoted_string_passes():
    assert findings(["'balance?,'", '"a: b"']) == []


def test_a_value_that_does_not_parse_is_refused_and_named():
    found = findings(["[1, 2", "{a: 1"])
    assert [f.rule for f in found] == ["TEST_VALUE_UNPARSEABLE"] * 2, found
    assert "[1, 2" in found[0].detail, found[0].detail


if __name__ == "__main__":
    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}"[:1500])
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
