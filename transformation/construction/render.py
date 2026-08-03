"""Construction — render protocol artifacts from a design and a mandate.

The Construction lifecycle sits between Transformation and Compilation. P0–P8 judge documents and
emit verdicts; construction consumes `DesignIntent(P7) + AuthoringMandate(P8)` and emits artifacts.
It is the first governed step that *creates* rather than judges, which is why it is a lifecycle
stage and not a tenth phase — numbering it would blur a construction failure ("the mandate was valid
but did not uniquely determine an artifact") back into a P8 failure ("the mandate is incomplete").

**What is rendered is the Machine block.** An artifact's prose is human narrative — intent,
rationale, the reasoning a reviewer needs — and no register determines it or should. The Machine
block is what the compiler reads, what the snapshot seals and what the runtime executes, so it is
what a design has to determine. Acceptance is semantic equality of that block, never text equality
of the file.

Nothing here decides anything. Every value is read from a register or from a constitution-fixed
default, and a fact the design does not state is a fact this module must not invent — an inventing
generator is a second, ungoverned design authority. Where a value cannot be derived, the renderer
omits it and the acceptance harness reports it as undetermined.
"""

from __future__ import annotations

import ast
from typing import Any

# Constitution per family. Fixed by the platform, not by any change request — a design that restated
# them would be declaring something it does not own.
GOVERNED_BY = {
    "AC": "fb.governance::CONSTITUTION_GOVERNANCE_V0",
    "IN": "fb.intent::CONSTITUTION_INTENT_V0",
    "WF": "fb.workflow::CONSTITUTION_WORKFLOW_V0",
    "CC": "fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0",
    "CT": "fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0",
    "RB": "fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0",
    "VOCAB": "fb.vocabulary::CONSTITUTION_VOCABULARY_V0",
    "STRUCTURE": "fb.structure::CONSTITUTION_STRUCTURE_V0",
}

KIND = {
    "AC": "ACTOR", "IN": "INTENT", "WF": "WORKFLOW", "CC": "CAPABILITY_CONTRACT",
    "CT": "CAPABILITY_TRANSFORM", "RB": "RUNTIME_BINDING", "VOCAB": "VOCABULARY",
    "STRUCTURE": "STRUCTURE",
}

# Where each family's artifact is written, relative to the domain's registry root.
DIRECTORY = {
    "AC": "actors", "IN": "intents", "WF": "workflows", "CC": "capability_contracts",
    "CT": "capability_transforms", "RB": "runtime_bindings", "VOCAB": "vocabulary",
    "STRUCTURE": "layers",
}

# An intent's outcome surface is fixed by the intent constitution — every intent in the composition
# carries the same two. Requiring a design to restate them would be ceremony, not determinacy.
INTENT_OUTCOMES = {
    "ACK": {"description": "Request accepted for processing"},
    "NACK": {"description": "Request rejected"},
}

WORKFLOW_STRUCTURE = "fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0"


def norm(value: Any) -> str:
    return " ".join(str(value or "").split())


def cell(row: dict, prefix: str) -> str:
    """A cell addressed by column prefix — a header may carry its vocabulary in parentheses."""
    for key, value in row.items():
        if key.startswith(prefix):
            return norm(value)
    return ""


def bare(value: str) -> str:
    return norm(value).split("::")[-1]


def rows(registers: dict, name: str) -> list[dict]:
    return [r for r in registers.get(name, []) if norm(next(iter(r.values()), "")).upper() != "NONE IDENTIFIED"]


def typed_fields(design: dict, code: str, direction: str) -> dict:
    """The typed fields an artifact declares in one direction, from `interface_fields`."""
    out: dict[str, Any] = {}
    for row in rows(design, "interface_fields"):
        if bare(cell(row, "Artifact")) != bare(code) or cell(row, "Direction") != direction:
            continue
        spec: dict[str, Any] = {"type": cell(row, "Type") or "string"}
        if cell(row, "Required") == "YES":
            spec["required"] = True
        default = cell(row, "Default")
        if default and default not in ("—", "-"):
            spec["default"] = _literal(default)
        # `Meaning` is documentation. The built corpus carries a description on some fields and not
        # others, which is a sign it is prose rather than governed content — rendering it would make
        # the generator author documentation the design never committed to.
        out[cell(row, "Field")] = spec
    return out


def _literal(value: str) -> Any:
    low = value.lower()
    if low in ("true", "false"):
        return low == "true"
    try:
        return int(value)
    except ValueError:
        return value


def render_all(p7: dict, p8: dict) -> list[dict]:
    """Every artifact the mandate schedules, in build order, as `{path, machine}`.

    One call over the whole mandate rather than one call per artifact: a capability contract is a
    fixed pipeline with no iteration, so a construction step that rendered one artifact could never
    render twenty-five. The iteration lives inside a pure transform, where it observes nothing.
    """
    family = {bare(cell(r, "Code")): cell(r, "Family") for r in rows(p7, "new_artifacts")}
    summary = {bare(cell(r, "Code")): cell(r, "Summary") for r in rows(p7, "new_artifacts")}
    subdomain = {bare(cell(r, "Code")): cell(r, "Subdomain Field")
                 for r in rows(p8, "field_declarations")}

    out = []
    for row in rows(p8, "build_order"):
        code = cell(row, "Code")
        short = bare(code)
        fam = family.get(short)
        if fam not in KIND:
            continue
        machine = _render(fam, code, short, summary.get(short, ""), subdomain.get(short, ""), p7, p8)
        domain = norm(code).split("::")[0]
        out.append({
            "path": f"registry/{subdomain.get(short, '')}/{DIRECTORY[fam]}/{short}.md",
            "domain": domain,
            "machine": machine,
        })
    return out


def _render(fam, code, short, summary, sub, p7, p8) -> dict:
    machine: dict[str, Any] = {
        "fqdn": code,
        "artifact_kind": KIND[fam],
        "version": "v0",
        "governed_by": GOVERNED_BY[fam],
    }
    builder = _BUILDERS[fam]
    builder(machine, code, short, summary, sub, p7, p8)
    return machine


def _intent(m, code, short, summary, sub, p7, p8):
    row = next((r for r in rows(p8, "new_intents") if bare(cell(r, "Code")) == short), {})
    m["core"] = {
        "summary": summary or cell(row, "Purpose"),
        "workflow": bare(cell(row, "Workflow")),
        "inputs": typed_fields(p7, code, "INPUT"),
        "outcomes": INTENT_OUTCOMES,
    }


def _workflow(m, code, short, summary, sub, p7, p8):
    binding = next((cell(r, "RB Code") for r in rows(p7, "rb_declarations")
                    if bare(cell(r, "Binds WF")) == short), "")
    topo = [r for r in rows(p7, "execution_topology") if bare(cell(r, "Workflow")) == short]
    actor = next((cell(r, "Code") for r in rows(p7, "new_artifacts")
                  if cell(r, "Family") == "AC"), "")

    nodes: dict[str, Any] = {}
    start = ""
    for r in topo:
        node = bare(cell(r, "Node"))
        node_type = cell(r, "Node Type")
        if node_type == "IN" and not start:
            start = node
        if node_type in ("EXIT", "EXIT_SUCCESS"):
            nodes[node] = {"type": "EXIT",
                           "outcome": "SUCCESS" if node.endswith("COMPLETED") else "VIOLATION"}
            continue
        spec: dict[str, Any] = {"type": node_type, "code": node}
        bindings = _bindings(p7, short, node, "INPUT")
        if bindings:
            spec["inputs"] = bindings
        spec["next"] = _edges(cell(r, "Routing"))
        nodes[node] = spec

    m["runtime_binding"] = binding
    m["subdomain"] = sub
    m["structure"] = WORKFLOW_STRUCTURE
    m["core"] = {"summary": summary, "actor_context": actor, "start_node": start, "nodes": nodes}


def _bindings(p7: dict, owner: str, step: str, direction: str) -> dict:
    """What one node or step is handed, or where its results go."""
    return {cell(b, "Field"): _binding(cell(b, "Bound To"))
            for b in rows(p7, "step_bindings")
            if bare(cell(b, "Owner")) == owner and bare(cell(b, "Step")) == step
            and cell(b, "Direction") == direction}


def _binding(bound_to: str) -> str:
    """A declared source rendered as the runtime's binding expression.

    The design states where a value comes from; the `$.`-prefixed form is a rendering convention of
    the execution surface, which is construction's business and not the designer's.
    """
    if bound_to.startswith(("{", "[")):
        try:
            return ast.literal_eval(bound_to)
        except (ValueError, SyntaxError):
            return bound_to
    if bound_to.startswith(("payload.", "results.", "inputs.", "capability_result.", "result_status")):
        return f"$.{bound_to}"
    return _literal(bound_to)


def _edges(routing: str) -> dict:
    """`SUCCESS -> TARGET; VIOLATION -> EXIT_REJECTED` as an outcome→target mapping."""
    out = {}
    for part in routing.split(";"):
        if "->" not in part:
            continue
        outcome, target = part.split("->", 1)
        out[norm(outcome)] = bare(target)
    return out


def _contract(m, code, short, summary, sub, p7, p8):
    steps = [r for r in rows(p7, "cc_composition") if bare(cell(r, "CC Code")) == short]
    statuses, pipeline = ["SUCCESS"], []
    for r in steps:
        pipeline.append(_step(p7, short, r))
        semantic = cell(r, "Semantic Status")
        if semantic and semantic not in statuses and semantic != "—":
            statuses.append(semantic)
        interpreter = cell(r, "Interpreted By")
        if interpreter not in ("", "—", "-"):
            # The interpretation is a step of its own; the register folds it into the row it
            # interprets because it is always positionally bound to that observation.
            name = _interpret_step(p7, short, r)
            pipeline.append(_step(p7, short, r, interpreter=interpreter, name=name,
                                  last=r is steps[-1]))
    m["core"] = {
        "summary": summary,
        "inputs": typed_fields(p7, code, "INPUT"),
        "outputs": typed_fields(p7, code, "OUTPUT"),
        "result_status_contract": {"allowed": statuses + ["VIOLATION", "BACKEND_ERROR"],
                                   "on_input_failure": "VIOLATION"},
        "pipeline": pipeline,
    }


def _step(p7: dict, owner: str, r: dict, interpreter: str = "", name: str = "",
          last: bool = False) -> dict:
    """One pipeline step: what it binds, what it addresses, and how it routes on its own result."""
    step_name = name or cell(r, "Step Name")
    out: dict[str, Any] = {"step": step_name}
    if interpreter:
        out["transform"] = interpreter
    else:
        kind = cell(r, "Kind")
        out["side_effect" if kind == "CS" else "transform"] = cell(r, "Capability")
        if kind == "CS":
            out["op"] = cell(r, "Operation")
        store = cell(r, "Store")
        if store and store not in ("—", "-"):
            out["store"] = store
    inputs = _bindings(p7, owner, step_name, "INPUT")
    outputs = _bindings(p7, owner, step_name, "OUTPUT")
    if inputs:
        out["inputs"] = inputs
    if outputs:
        out["outputs"] = outputs
    if interpreter:
        semantic = cell(r, "Semantic Status")
        routing = {"SUCCESS": "exit" if last else "continue"}
        if semantic and semantic not in ("—", "-", "SUCCESS"):
            routing[semantic] = "exit"
        routing["VIOLATION"] = "exit"
    else:
        routing = _edges(cell(r, "Routing"))
    if routing:
        out["result_surface"] = list(routing)
        out["on_result"] = routing
    return out


def _interpret_step(p7: dict, owner: str, r: dict) -> str:
    """The interpreting step's declared name — the one step_bindings addresses it by."""
    observed = cell(r, "Step Name")
    for b in rows(p7, "step_bindings"):
        if bare(cell(b, "Owner")) != owner:
            continue
        if cell(b, "Bound To").startswith(f"results.{observed}."):
            return cell(b, "Step")
    return f"interpret_{observed}"


def _transform(m, code, short, summary, sub, p7, p8):
    row = next((r for r in rows(p7, "implementation_bindings") if bare(cell(r, "CT Code")) == short), {})
    m["core"] = {
        "summary": summary,
        "inputs": typed_fields(p7, code, "INPUT"),
        "outputs": typed_fields(p7, code, "OUTPUT"),
    }
    m["machine"] = {
        "ct_kind": cell(row, "Kind") or "atom",
        "ct_purity": cell(row, "Purity") or "ct_pure",
        "operation": cell(row, "Operation"),
        "implementation": {"module": cell(row, "Module"), "callable": cell(row, "Callable")},
    }


def _properties(p7: dict, code: str) -> dict:
    return {cell(r, "Property"): _literal(cell(r, "Value"))
            for r in rows(p7, "artifact_properties") if bare(cell(r, "Artifact")) == bare(code)}


def _actor(m, code, short, summary, sub, p7, p8):
    m["core"] = {"summary": summary, **_properties(p7, code),
                 "attributes": typed_fields(p7, code, "ATTRIBUTE")}


def _vocabulary(m, code, short, summary, sub, p7, p8):
    entries = [cell(r, "Value") for r in rows(p7, "vocabulary_extensions")
               if bare(cell(r, "Vocabulary Code")) == short]
    extends = next((cell(r, "Extends") for r in rows(p7, "vocabulary_extensions")
                    if bare(cell(r, "Vocabulary Code")) == short), "")
    m.pop("core", None)
    m["extends"] = extends
    m["result_status"] = {"casing": "UPPER_SNAKE", "entries": entries}


def _structure(m, code, short, summary, sub, p7, p8):
    stores = {cell(r, "Store Name"): {"path": cell(r, "Proposed Path")}
              for r in rows(p7, "structure_stores")}
    props = _properties(p7, code)
    m["core"] = {"summary": summary, "layer": props.pop("layer", "DOMAINS"),
                 "domain": norm(code).split("::")[0], "subdomain": sub,
                 "storage_roots": {"base_path": props.pop("base_path", "")},
                 "entity_stores": stores, **props}


def _binding_artifact(m, code, short, summary, sub, p7, p8):
    decls = [r for r in rows(p7, "rb_declarations") if bare(cell(r, "RB Code")) == short]
    structure = next((cell(r, "Storage Structure") for r in decls), "")
    bindings = {}
    for r in decls:
        wf = bare(cell(r, "Binds WF"))
        bindings[wf] = [s.strip() for s in cell(r, "CS Bindings").split(",") if s.strip()]
    m["core"] = {"summary": summary, "storage_structure": structure, "bindings": bindings}


_BUILDERS = {
    "IN": _intent, "WF": _workflow, "CC": _contract, "CT": _transform,
    "AC": _actor, "VOCAB": _vocabulary, "STRUCTURE": _structure, "RB": _binding_artifact,
}
