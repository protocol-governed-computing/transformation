"""Declaration identity: the rebuild's rules equal the oracle's, rule for rule (REBUILD_DESIGN §8.2).

Each side prints every phase's declared rule set as JSON: id, check, register, section title, params
and intent. The two are compared phase by phase, as sets. Order is checked elsewhere: a sealed rule
set is an ordered list, and `tc phase emit --check` refuses a workflow whose rules moved. A rule the
rebuild changes on purpose is a divergence declared in the charter, and is reported by name.

    python scripts/rebuild/declarations.py            compare
    python scripts/rebuild/declarations.py --dump     print this side's rules (used by compare)

Exit 0 when every phase agrees, 1 otherwise.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

ORACLE = Path.home() / "pgc-oracle" / "transformation"
REBUILD = Path(__file__).resolve().parents[2]

# Rules the rebuild changes on purpose, each a divergence in REBUILD_CHARTER §8.
# A list param declared in another order: (phase, id, register, param), the same entries.
REORDERED = {
    ("p7", "CELL_NOT_IN_VOCABULARY", "new_artifacts", "vocabulary"): "M3.1-1",
}
# A rule restated: (phase, id, register) → the divergence, and the fields that may differ. The rest
# of the rule must still be identical.
RESTATED = {
    ("p7", "REGISTER_COLUMN_MISSING", "implementation_bindings"): ("M3.3-7", {"params"}),
    ("p7", "REGISTER_COLUMN_MISSING", "molecule_steps"): ("M3.3-7", {"params"}),
    ("p7", "STORE_PATH_FORMAT_MISMATCH", "structure_stores"): ("M3.4a-1", {"check", "params"}),
    ("p0", "BELIEF_STATED_AS_FACT", "system_beliefs"): ("M3.4a-1", {"check", "params"}),
    ("p7", "TOPOLOGY_NODE_REPEATED", "execution_topology"): ("M3.4a-1", {"check", "params"}),
    ("p7", "BINDING_SOURCE_UNROOTED", "step_bindings"): ("M3.4a-1", {"check", "params"}),
    ("p7", "BINDING_SOURCE_MALFORMED", "step_bindings"): ("M3.4a-1", {"check", "params"}),
    ("p7", "GENERATED_SOURCE_WITHOUT_GENERATOR", "step_bindings"): ("M2-9", {"params"}),
    ("p7", "TEST_VALUE_EMPTY", "test_case_values"): ("M3.3-9", {"check", "params"}),
    ("p7", "GOVERNING_RULE_NOT_IN_FORCE", "refusal_governance_discharge"): ("M3.3b-4", {"params"}),
}
# A rule restated in every phase that derives it: id → the divergence, and the fields that may differ.
RESTATED_EVERYWHERE = {
    "SOURCE_FINDING_UNRESOLVED": ("M3.3b-1", {"params"}),
    "ROW_WITHOUT_SOURCE_FINDING": ("M3.3b-2", {"check"}),
    "HEADER_FIELD_MISSING": ("M4-1", {"params", "intent"}),
}
# A rule only the oracle has: (phase, id) → the divergence that retired it.
RETIRED = {("p7", "TEST_VALUE_UNPARSEABLE"): "M2-10", ("p1", "CITATION_ROW_UNRESOLVED"): "M3.4a-2",
           ("p7", "IMPLEMENTATION_WITHOUT_MODULE"): "M5-2", ("p7", "IMPLEMENTATION_MODULE_MISPLACED"): "M5-2",
           ("p7", "MOLECULE_DECLARES_IMPLEMENTATION"): "M5-2"}
# A rule only the oracle has, in every phase: id → the divergence that retired it.
RETIRED_EVERYWHERE = {"LIFECYCLE_STATE_NOT_IN_VOCABULARY": "M4-2"}
# A rule only the rebuild has: its check, or its id, → the divergence that added it.
ADDED = {"CELL_OF_TYPE": "M3.3-4", "HEADER_FIELD_OF_TYPE": "M4-1", "HEADER_FIELD_MISMATCH": "M4-1"}
# A procedure restated as several constraints: (phase, id) → the divergence. The first is matched
# as restated; the rest are added.
SPLIT = {("p7", "STORE_PATH_FORMAT_MISMATCH"): "M3.4a-1", ("p7", "BINDING_SOURCE_MALFORMED"): "M3.4a-1"}


def _declared(phase: str, a: dict, b: dict) -> str | None:
    """The divergence that explains a difference between two rules, or None."""
    for (p, rid, register, param), name in REORDERED.items():
        if (phase, a["id"], a["register"]) == (p, rid, register) and \
                {**a, "params": {k: v for k, v in a["params"].items() if k != param}} == \
                {**b, "params": {k: v for k, v in b["params"].items() if k != param}} and \
                sorted(a["params"].get(param) or []) == sorted(b["params"].get(param) or []):
            return name
    restated = RESTATED.get((phase, a["id"], a["register"])) or RESTATED_EVERYWHERE.get(a["id"])
    if restated and (b["id"], b["register"]) == (a["id"], a["register"]):
        name, fields = restated
        if {k: v for k, v in a.items() if k not in fields | {"intent"}} == \
                {k: v for k, v in b.items() if k not in fields | {"intent"}} and \
                (a["intent"] == b["intent"] or "intent" in fields):
            return name
    return None


def dump() -> dict:
    try:
        from transformation.design.rule_sets import RULE_SETS
    except ImportError:  # the oracle declares its rule sets in one module per phase
        from transformation.design.meta import RULE_MODULES as RULE_SETS

    out = {}
    for phase, module in RULE_SETS.items():
        out[phase] = [
            {"id": r.id, "check": r.check, "register": r.register, "section_title": r.section_title,
             "params": r.params, "intent": r.intent}
            for r in module.rule_set()
        ]
    return out


def side(pythonpath: str | None, cwd: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    if pythonpath:
        env["PYTHONPATH"] = pythonpath
    done = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--dump"], cwd=cwd, env=env,
                          capture_output=True, text=True)
    if done.returncode:
        raise SystemExit(done.stderr[-3000:])
    return json.loads(done.stdout)


def _signature(rule: dict) -> str:
    return json.dumps(rule, sort_keys=True)


def main(argv: list[str]) -> int:
    if "--dump" in argv:
        json.dump(dump(), sys.stdout, default=list)
        return 0
    was, now = side(str(ORACLE), ORACLE), side(None, REBUILD)
    differ = 0
    for phase in was:
        a = Counter(_signature(r) for r in was[phase])
        b = Counter(_signature(r) for r in now.get(phase, []))
        only_a = [json.loads(x) for x in (a - b).elements()]
        only_b = [json.loads(x) for x in (b - a).elements()]
        explained = []
        for ra in list(only_a):
            match = next((rb for rb in only_b if _declared(phase, ra, rb)), None)
            if match is not None:
                explained.append(_declared(phase, ra, match))
                only_a.remove(ra)
                only_b.remove(match)
        for ra in list(only_a):
            retired = RETIRED.get((phase, ra["id"])) or RETIRED_EVERYWHERE.get(ra["id"])
            if retired:
                explained.append(retired)
                only_a.remove(ra)
        for rb in list(only_b):
            added = ADDED.get(rb["check"]) or ADDED.get(rb["id"])
            if added:
                explained.append(added)
                only_b.remove(rb)
            elif (phase, rb["id"]) in SPLIT:
                explained.append(SPLIT[(phase, rb["id"])])
                only_b.remove(rb)
        for name in sorted(set(explained)):
            count = explained.count(name)
            print(f"{phase}: declared divergence {name}" + (f" ({count} rules)" if count > 1 else ""))
        if only_a or only_b:
            differ += 1
            print(f"\n{phase}: {len(only_a)} rule(s) only in the oracle, {len(only_b)} only in the rebuild")
            for r in only_a:
                print(f"   oracle:  {json.dumps(r)[:400]}")
            for r in only_b:
                print(f"   rebuild: {json.dumps(r)[:400]}")
    total = sum(len(v) for v in was.values())
    if differ:
        print(f"\nDECLARATIONS DIFFER — {differ} phase(s)")
        return 1
    print(f"DECLARATIONS IDENTICAL — {total} rules over {len(was)} phases, compared as sets")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
