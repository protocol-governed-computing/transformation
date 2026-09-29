"""Withdrawn facts — an amendment says what it takes away.

An artifact a design extends is rendered whole and replaces the one the composition holds, so every
fact the design omits is a fact the artifact loses, and construction refuses the loss. Shown here: a
withdrawal covers the facts at and beneath the place it names and nothing else; a fact omitted
without a withdrawal is still refused; a withdrawal naming a place where nothing is lost is itself
refused; a value refined into a list or an object is not lost; and at P7 a fact is withdrawn only
from an artifact the design extends.

Run:  python scripts/testbed/withdrawal_design_test.py
"""

from __future__ import annotations

import sys

from transformation.build.completeness import narrowing, withdraw
from transformation.design.evaluate import ParsedDocument
from transformation.design.oracle import evaluate
from transformation.design.p7_design_intent.rules import rule_set
from transformation.design.read import parse_text

LOST = {"CC_DECIDE_V0": [".core.inputs.allowed_set.required", ".core.inputs.allowed_set.type",
                         ".core.inputs.rules[0].field", ".core.inputs.rules[0].op",
                         ".core.inputs.subject.type"]}


def test_a_withdrawal_covers_the_facts_at_and_beneath_the_place_it_names():
    remaining, unfounded = withdraw(LOST, {"CC_DECIDE_V0": [".core.inputs.allowed_set",
                                                            ".core.inputs.rules"]})
    assert remaining == {"CC_DECIDE_V0": [".core.inputs.subject.type"]}, remaining
    assert unfounded == {}, unfounded


def test_a_place_that_merely_shares_a_prefix_is_not_withdrawn():
    remaining, _ = withdraw({"CC_DECIDE_V0": [".core.inputs.rules_version"]},
                            {"CC_DECIDE_V0": [".core.inputs.rules"]})
    assert remaining == {"CC_DECIDE_V0": [".core.inputs.rules_version"]}, remaining


def test_a_withdrawal_where_nothing_is_lost_is_unfounded():
    remaining, unfounded = withdraw(LOST, {"CC_DECIDE_V0": [".core.inputs.allowed_set",
                                                            ".core.inputs.decision"],
                                           "CC_OTHER_V0": [".core.inputs.x"]})
    assert unfounded == {"CC_DECIDE_V0": [".core.inputs.decision"],
                         "CC_OTHER_V0": [".core.inputs.x"]}, unfounded
    assert ".core.inputs.subject.type" in remaining["CC_DECIDE_V0"], remaining


def test_a_value_refined_into_a_list_or_an_object_is_not_lost():
    prior = {"core": {"pipeline": [{"step": "judge", "inputs": {"rules": "$.inputs.rules",
                                                                "parameters": "$.inputs.parameters",
                                                                "gone": "$.inputs.gone"}}]}}
    now = {"core": {"pipeline": [{"step": "judge", "inputs": {"rules": [{"field": "x", "op": "not_null"}],
                                                              "parameters": {"x": "$.inputs.x"}}}]}}
    lost = narrowing([{"path": "probe/CC_JUDGE_V0.md", "machine": now}], {"CC_JUDGE_V0": prior})
    assert lost == {"CC_JUDGE_V0": [".core.pipeline[judge].inputs.gone"]}, lost


def _doc(action: str) -> ParsedDocument:
    text = (
        "# Design Intent: probe / withdrawal\n\n"
        "<!-- register:existing_inventory -->\n"
        "| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |\n"
        "|---|---|---|---|---|\n"
        f"| probe::CC_DECIDE_V0 | {action} | Decides | Amended | human decision |\n\n"
        "<!-- register:withdrawn_facts optional -->\n"
        "| Artifact | Fact | Reason | Source Finding |\n"
        "|---|---|---|---|\n"
        "| probe::CC_DECIDE_V0 | .core.inputs.allowed_set | The contract holds its set | human decision |\n\n"
    )
    header, sections, registers = parse_text(text)
    return ParsedDocument(header=header, sections=sections, registers=registers, raw=text, path="probe",
                          observed={})


def test_a_fact_is_withdrawn_only_from_an_artifact_the_design_extends():
    rule = [r for r in rule_set() if r.id == "WITHDRAWAL_NOT_AN_AMENDMENT"]
    assert [f.rule for f in evaluate(_doc("EXTEND"), rule).findings] == []
    assert [f.rule for f in evaluate(_doc("REUSE"), rule).findings] == ["WITHDRAWAL_NOT_AN_AMENDMENT"]


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
