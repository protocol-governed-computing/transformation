"""Declaration identity: the rebuild's rules equal the oracle's, rule for rule (REBUILD_DESIGN §8.2).

Each side prints every phase's declared rule set as JSON: id, check, register, section title, params
and intent, in declaration order. The two are compared phase by phase. A rule the rebuild changes on
purpose is a divergence declared in the charter, and is listed here by phase and position.

    python scripts/rebuild/declarations.py            compare
    python scripts/rebuild/declarations.py --dump     print this side's rules (used by compare)

Exit 0 when every phase agrees, 1 otherwise.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
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


def main(argv: list[str]) -> int:
    if "--dump" in argv:
        json.dump(dump(), sys.stdout, default=list)
        return 0
    was, now = side(str(ORACLE), ORACLE), side(None, REBUILD)
    differ = 0
    for phase in was:
        a, b = was[phase], now.get(phase, [])
        if a == b:
            continue
        if len(a) != len(b):
            differ += 1
        print(f"\n{phase}: oracle {len(a)} rules, rebuild {len(b)}")
        for i in range(max(len(a), len(b))):
            ra = a[i] if i < len(a) else None
            rb = b[i] if i < len(b) else None
            if ra != rb and _declared(phase, ra, rb):
                print(f"   #{i + 1} declared divergence {_declared(phase, ra, rb)}")
                continue
            if ra != rb:
                differ += 1
                print(f"   #{i + 1}")
                print(f"     oracle:  {json.dumps(ra)[:400]}")
                print(f"     rebuild: {json.dumps(rb)[:400]}")
    total = sum(len(v) for v in was.values())
    if differ:
        print(f"\nDECLARATIONS DIFFER — {differ} phase(s)")
        return 1
    print(f"DECLARATIONS IDENTICAL — {total} rules over {len(was)} phases")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
