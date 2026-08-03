"""Construction Completeness — does a CR's design uniquely determine the artifacts it built?

**Construction Completeness** is the percentage of construction-required facts that the dossier
uniquely determines. It turns "is the generator ready" from a judgement into a measurement:

    CR-1 as authored          53%
    generator requirement    100%, or the generator is inventing design

That threshold is `UNIQUELY_DETERMINED_OR_STOP` applied to the Construction lifecycle. A fact the
design does not state is a fact the generator would have to invent, and a generator that invents
design is a second, ungoverned design authority.

**This metric is an under-approximation, and the fact list below is why.** The facts are declared by
hand, so completeness measures whether the design states the things this file thought to ask about
— not whether an artifact can actually be rebuilt. CR-1 reached 100% here while
`construction_acceptance.py` reproduced one artifact in twenty-five: this file asked "does this
contract declare a pipeline" and never "does each step state its store, its input bindings and its
result surface". Treat this as the cheap early signal and the acceptance harness as the ground
truth; the fact list should eventually be derived from what the renderer must emit rather than
restated here.


The Construction lifecycle's input contract is `DesignIntent(P7) + AuthoringMandate(P8) + existing
snapshot`. A generator written against a contract that does not determine its output would diff on
every artifact and report only what was already known, so the contract is measured before the
generator is written.

A fact is counted only when the design is the authority for it. `ACK`/`NACK` on an intent is
identical across every intent in the composition because the intent constitution fixes it — the
generator emits it without consulting the design, so requiring the design to restate it would
measure ceremony rather than determinacy.

This is **not** a generator. It emits no artifacts and makes no rendering decisions. For each
artifact a CR actually built, it asks of each determinable fact: is this fact stated anywhere in the
CR's P7 or P8 registers? A fact that is not stated is one the generator would have to invent, and
inventing it is precisely the construction failure the four-lifecycle split exists to name.

It subsumes as-designed vs as-built reconciliation. An artifact whose *identity* traces to nothing
is the built-never-designed drift; a designed identity that was built as something else is the
other face. Both fall out of the same comparison.

Run:  python scripts/testbed/determinism_probe.py [--require <pct>] [dossier] [registry]
Exit: 0, or 1 when completeness is below `--require`.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

from transformation.phases.read import read_seed

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent

DOSSIER = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"
REGISTRY = WORKSPACE / "business_domains/book_library_mgmt/registry/catalog"

MACHINE = re.compile(r"```yaml\n(.*?)\n```", re.S)


def machine(path: Path) -> dict:
    """The Machine block of an authored artifact, as data."""
    found = MACHINE.search(path.read_text(encoding="utf-8"))
    if not found:
        raise SystemExit(f"{path} carries no Machine block")
    return yaml.safe_load(found.group(1))


def registers(doc) -> dict[str, list[dict]]:
    """Every register of a phase document as plain rows."""
    out: dict[str, list[dict]] = {}
    for entry in doc.registers:
        block = doc.register(entry["id"])
        if block and block.table:
            out[entry["id"]] = block.table.rows
    return out


def norm(value: str) -> str:
    return " ".join(str(value).split())


def cell(row: dict, prefix: str) -> str:
    """A cell addressed by column prefix.

    A template declares a column's vocabulary in its header — `Direction (INPUT, OUTPUT,
    ATTRIBUTE)` — so an exact-name lookup misses every column that declares one. `checks.py`
    addresses cells the same way.
    """
    for key, value in row.items():
        if key.startswith(prefix):
            return norm(value)
    return ""


def bare(value: str) -> str:
    return norm(value).split("::")[-1]


class Design:
    """Everything the CR's P7 and P8 registers state, indexed for lookup.

    Indexed on bare codes throughout. A provisional code, a binding FQDN and a workflow node all
    name the same artifact at different rungs, and a probe that distinguished them would report a
    gap wherever the dossier was merely being consistent with the purity ladder.
    """

    def __init__(self, dossier: Path):
        p7 = registers(read_seed(next(dossier.glob("p7_*.md"))))
        p8 = registers(read_seed(next(dossier.glob("p8_*.md"))))
        self.p7, self.p8 = p7, p8

        self.declared = {bare(r["Code"]) for r in p7.get("new_artifacts", [])}
        self.carried = {bare(r["FQDN"]) for r in p7.get("existing_inventory", [])}
        self.scheduled = {bare(r["Code"]) for r in p8.get("build_order", [])}
        self.subdomains = {bare(r["Code"]): norm(r["Subdomain Field"])
                           for r in p8.get("field_declarations", [])}

        # workflow → node → (node type, routing as authored)
        self.topology: dict[str, dict[str, tuple[str, str]]] = {}
        for row in p7.get("execution_topology", []):
            wf = bare(row["Workflow"])
            self.topology.setdefault(wf, {})[bare(row["Node"])] = (
                norm(row["Node Type"]), norm(row["Routing"]))

        # A composition row renders one step, plus a second when it names an interpreting
        # transform: `Interpreted By` is written as a column because the interpretation is always
        # positionally bound to the observation it interprets, but it *is* a step, and construction
        # emits it as one. `—` means the operation's own status is already semantic — READ answers
        # NOT_FOUND for a missing key, while EXISTS answers SUCCESS and carries what it found in a
        # boolean, which is why one needs interpreting and the other does not.
        self.cc_steps: dict[str, list[dict]] = {}
        for row in p7.get("cc_composition", []):
            code = bare(cell(row, "CC Code"))
            self.cc_steps.setdefault(code, []).append(row)
            if cell(row, "Interpreted By") not in ("", "—", "-"):
                self.cc_steps[code].append({**row, "Capability": cell(row, "Interpreted By")})

        self.intents = {bare(r["Code"]): r for r in p8.get("new_intents", [])}

        # The registers that carry the facts the language could not express before.
        self.bindings: dict[str, set[str]] = {}
        for row in p7.get("step_bindings", []):
            if cell(row, "Direction") != "INPUT":
                continue
            self.bindings.setdefault(f"{bare(cell(row, 'Owner'))}/{bare(cell(row, 'Step'))}", set()).add(
                cell(row, "Field"))
        self.fields: dict[tuple[str, str], set[str]] = {}
        for row in p7.get("interface_fields", []):
            key = (bare(row["Artifact"]), cell(row, "Direction"))
            self.fields.setdefault(key, set()).add(cell(row, "Field"))
        self.implementations = {bare(cell(r, "CT Code")) for r in p7.get("implementation_bindings", [])
                                if cell(r, "Module")}
        self.vocabularies = {bare(cell(r, "Vocabulary Code")) for r in p7.get("vocabulary_extensions", [])}
        self.rb = {bare(r["RB Code"]): r for r in p7.get("rb_declarations", [])}
        self.rb_binds = {bare(r["Binds WF"]): bare(r["RB Code"])
                         for r in p7.get("rb_declarations", [])}
        self.stores = p7.get("structure_stores", [])

    def states_identity(self, code: str) -> bool:
        return code in self.declared or code in self.carried


# A determinable fact: what it is called, and a predicate answering whether the design states it.
# Declared per artifact kind rather than discovered, so a fact nobody checks is visible as an
# absence from this table rather than as a silently clean report.
def facts_for(kind: str, art: dict, design: Design) -> list[tuple[str, bool]]:
    code = bare(art["fqdn"])
    # `runtime_binding`, `subdomain` and `structure` are siblings of `core`, not members of it.
    # Reading them from `core` reports every workflow's binding undetermined — a probe bug that
    # looks exactly like a design gap, which is why the first run's list could not be trusted.
    core = art.get("core") or {}
    out: list[tuple[str, bool]] = [
        ("identity", design.states_identity(code)),
        ("scheduled", code in design.scheduled),
        ("subdomain", code in design.subdomains),
    ]

    if kind == "WORKFLOW":
        nodes = core.get("nodes") or {}
        declared_nodes = design.topology.get(code, {})
        routable = {n for n, spec in nodes.items() if spec.get("type") != "EXIT"}
        out += [
            ("node set", bool(declared_nodes) and routable <= set(declared_nodes)),
            ("start node", bool(declared_nodes)),
            ("runtime_binding", bare(str(art.get("runtime_binding", ""))) in design.rb),
            ("actor_context", _actor_declared(core, design)),
        ]
        # Routing must resolve to a node identity, not describe one in prose.
        targets_named = True
        bindings_stated = True
        for name, spec in nodes.items():
            if spec.get("type") == "EXIT":
                continue
            routing = declared_nodes.get(bare(name), ("", ""))[1]
            for outcome, target in (spec.get("next") or {}).items():
                if str(target).startswith("EXIT"):
                    continue
                if bare(target) not in routing:
                    targets_named = False
            declared = design.bindings.get(f"{code}/{bare(name)}", set())
            if not set(spec.get("inputs") or {}) <= declared:
                bindings_stated = False
        out += [("routing targets", targets_named), ("node input bindings", bindings_stated)]

    elif kind == "CAPABILITY_CONTRACT":
        steps = design.cc_steps.get(code, [])
        pipeline = core.get("pipeline") or []
        out += [
            ("pipeline steps", len(steps) == len(pipeline) and bool(steps)),
            ("step capabilities", _steps_match(steps, pipeline)),
            # The contract's typed surface lives in `interface_fields`; `cc_composition` carries the
            # pipeline's own logical vocabulary, which is deliberately a different thing.
            ("inputs", set(core.get("inputs") or {}) <= design.fields.get((code, "INPUT"), set())),
            ("outputs", set(core.get("outputs") or {}) <= design.fields.get((code, "OUTPUT"), set())),
            ("result_status_contract", bool(steps)),
        ]

    elif kind == "INTENT":
        row = design.intents.get(code)
        built_inputs = set(core.get("inputs") or {})
        out += [
            ("workflow", bool(row) and bare(row["Workflow"]) == bare(str(core.get("workflow", "")))),
            ("input field names", built_inputs <= design.fields.get((code, "INPUT"), set())),
        ]

    elif kind == "STRUCTURE":
        stated = {norm(r.get("Store", "")) for r in design.stores}
        built = set(core.get("entity_stores") or {})
        out += [("entity stores", bool(stated) and bool(built))]

    elif kind == "RUNTIME_BINDING":
        out += [("bindings", code in design.rb)]

    elif kind == "CAPABILITY_TRANSFORM":
        out += [
            ("implementation module", code in design.implementations),
            ("inputs", set(core.get("inputs") or {}) <= design.fields.get((code, "INPUT"), set())),
            ("outputs", set(core.get("outputs") or {}) <= design.fields.get((code, "OUTPUT"), set())),
        ]

    elif kind == "VOCABULARY":
        out += [("result_status values", code in design.vocabularies)]

    elif kind == "ACTOR":
        out += [("attributes",
                 set(core.get("attributes") or {}) <= design.fields.get((code, "ATTRIBUTE"), set()))]

    return out


def _actor_declared(core: dict, design: Design) -> bool:
    actor = bare(str(core.get("actor_context", "")))
    return bool(actor) and design.states_identity(actor)


def _steps_match(steps: list[dict], pipeline: list[dict]) -> bool:
    if not steps or len(steps) != len(pipeline):
        return False
    named = {bare(s.get("Capability", "")) for s in steps}
    built = {bare(str(p.get("transform") or p.get("side_effect") or "")) for p in pipeline}
    return built <= named


def _cc_fields_stated(steps: list[dict], fields: dict, column: str) -> bool:
    if not steps or not fields:
        return False
    stated = set()
    for s in steps:
        stated |= {norm(f) for f in norm(s.get(column, "")).split(",") if norm(f)}
    return set(fields) <= stated


KIND_DIR = {
    "WORKFLOW": "workflows", "CAPABILITY_CONTRACT": "capability_contracts",
    "INTENT": "intents", "STRUCTURE": "layers", "RUNTIME_BINDING": "runtime_bindings",
    "CAPABILITY_TRANSFORM": "capability_transforms", "VOCABULARY": "vocabulary",
    "ACTOR": "actors",
}


def main() -> int:
    args = sys.argv[1:]
    require = 0.0
    if "--require" in args:
        i = args.index("--require")
        require = float(args[i + 1])
        del args[i:i + 2]
    dossier = Path(args[0]) if args else DOSSIER
    registry = Path(args[1]) if len(args) > 1 else REGISTRY
    design = Design(dossier)

    built = sorted(registry.rglob("*.md"))
    print(f"determinism probe — {len(built)} built artifact(s) against {dossier.name}\n")

    gaps: Counter[str] = Counter()
    per_artifact: list[tuple[str, str, list[tuple[str, bool]]]] = []
    for path in built:
        art = machine(path)
        kind = str(art.get("artifact_kind", "")).upper()
        facts = facts_for(kind, art, design)
        per_artifact.append((bare(art["fqdn"]), kind, facts))
        for name, ok in facts:
            if not ok:
                gaps[f"{kind}.{name}"] += 1

    for code, kind, facts in per_artifact:
        missing = [n for n, ok in facts if not ok]
        mark = "OK  " if not missing else "GAP "
        print(f"  {mark} {code:<44} {len(facts) - len(missing)}/{len(facts)}"
              + (f"   missing: {', '.join(missing)}" if missing else ""))

    total = sum(len(f) for _, _, f in per_artifact)
    undetermined = sum(gaps.values())
    completeness = 100.0 * (total - undetermined) / total if total else 0.0
    print(f"\n  Construction Completeness  {completeness:.1f}%"
          f"   ({total - undetermined}/{total} facts determined, {undetermined} undetermined)\n")
    print("  undetermined facts, by kind and field:")
    for name, n in gaps.most_common():
        print(f"    {n:>3}  {name}")

    # As-built reconciliation falls out of the same comparison.
    designed = design.declared
    actual = {code for code, _, _ in per_artifact}
    print("\n  as-designed vs as-built")
    print(f"    designed {len(designed)}   built {len(actual)}")
    for label, s in (("designed, not built", designed - actual),
                     ("built, never designed", actual - designed - design.carried)):
        print(f"    {label:<22} {sorted(s) if s else 'none'}")

    if require and completeness + 1e-9 < require:
        print(f"\n  BELOW THRESHOLD — {completeness:.1f}% < {require:.1f}% required")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
