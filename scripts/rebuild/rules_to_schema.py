"""Move each phase's hand-declared rules out of `rules.py` into its register schema, once.

A rule `expand.py` already derives from the schema's shape stays derived. Every other rule the
phase's `rule_set()` returns is written as one entry of the schema's top-level `allOf`, in the order
the phase declared it, naming its register with `x-register`. Order is kept because a sealed rule
set is an ordered list, and its order is part of what a workflow declares. `declared.encode`
refuses a rule that does not come back unchanged when decoded.
The phase's declared priors are written as `x-priors`, and the composition facts it grounds
against as `x-observations`.

    python scripts/rebuild/rules_to_schema.py

Deleted at the swap: from then on the schemas are edited, never regenerated.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

from transformation.design.declared import Columns, encode
from transformation.design.expand import derived_rules
from transformation.design.rules import Rule
from transformation.design.schema import SCHEMAS, load

ORACLE = Path.home() / "pgc-oracle" / "transformation"
HERE = Path(__file__).resolve().parent


def oracle_rule_sets() -> dict[str, list[Rule]]:
    """Every phase's rule set as the oracle declares it, read through `declarations.py --dump`."""
    env = dict(os.environ, PYTHONPATH=str(ORACLE))
    done = subprocess.run([sys.executable, str(HERE / "declarations.py"), "--dump"], cwd=ORACLE,
                          env=env, capture_output=True, text=True, check=True)
    return {phase: [Rule(**r) for r in rules] for phase, rules in json.loads(done.stdout).items()}


def oracle_attribute(name: str) -> dict:
    env = dict(os.environ, PYTHONPATH=str(ORACLE))
    code = ("import json; from transformation.design.meta import RULE_MODULES as M; "
            f"print(json.dumps({{p: getattr(m, {name!r}, None) for p, m in M.items()}}, default=list))")
    done = subprocess.run([sys.executable, "-c", code], cwd=ORACLE, env=env, capture_output=True,
                          text=True, check=True)
    return json.loads(done.stdout)


def signature(rule) -> tuple:
    """A rule as a comparable value. A vocabulary is compared as a set: the one derived rule whose
    order changes on purpose (charter §8, M3.1-1) still matches the oracle's."""
    params = dict(rule.params)
    if rule.check == "CELL_IN_VOCABULARY":
        params["vocabulary"] = sorted(params.get("vocabulary") or [])
    return (rule.id, rule.check, rule.register, rule.section_title, json.dumps(params, sort_keys=True),
            rule.intent)


def main() -> int:
    moved = 0
    priors, observations = oracle_attribute("PRIORS"), oracle_attribute("OBSERVATIONS")
    for phase, rules in oracle_rule_sets().items():
        shape = load(phase)
        path = SCHEMAS / shape.path.name
        declared = json.loads(path.read_text(encoding="utf-8"))
        derived = Counter(signature(r) for r in derived_rules(shape))
        top: list[dict] = []
        for rule in rules:
            sig = signature(rule)
            if derived[sig]:
                derived[sig] -= 1
                continue
            if rule.section_title not in (None, rule.register):
                raise SystemExit(f"{phase} {rule.id}: a section title the schema cannot state")
            if rule.register is None:
                top.append(encode(rule, None))
            else:
                r = shape.register(rule.register)
                top.append({"x-register": rule.register,
                            **encode(rule, Columns(dict(zip(r.columns, r.keys))))})
            moved += 1
        if top:
            declared["allOf"] = top
        declared["x-priors"] = list(priors[phase] or ())
        if observations[phase]:
            declared["x-observations"] = observations[phase]
        path.write_text(json.dumps(declared, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{moved} rules written into the register schemas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
