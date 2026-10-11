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

# Rules the rebuild changes on purpose, each a divergence in REBUILD_CHARTER §8: (phase, id,
# register, param) whose value may differ. Everything else about the rule must still be identical.
DIVERGENCES = {
    ("p7", "CELL_NOT_IN_VOCABULARY", "new_artifacts", "vocabulary"): "M3.1-1",
}


def _declared(phase: str, a: dict | None, b: dict | None) -> str | None:
    """The divergence that explains a difference between two rules, or None."""
    if not a or not b:
        return None
    for (p, rid, register, param), name in DIVERGENCES.items():
        if (phase, a["id"], a["register"]) == (p, rid, register) and \
                {**a, "params": {k: v for k, v in a["params"].items() if k != param}} == \
                {**b, "params": {k: v for k, v in b["params"].items() if k != param}} and \
                sorted(a["params"].get(param) or []) == sorted(b["params"].get(param) or []):
            return name
    return None


def dump() -> dict:
    from transformation.design.meta import RULE_MODULES

    out = {}
    for phase, module in RULE_MODULES.items():
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
        for name in explained:
            print(f"{phase}: declared divergence {name}")
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
