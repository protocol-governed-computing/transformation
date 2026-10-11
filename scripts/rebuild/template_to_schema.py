"""Write each phase template's register declaration out as a JSON Schema, once.

The templates declared shape as Markdown tables, read by `template_reader`. From M3.1 the register
schemas are the declaration, and the templates are guides checked against them. This writes what
`template_reader` reads, nothing more and nothing less:

- every register, required; a register that may not be empty has `minItems: 1`;
- a table register is an array of objects whose properties are its columns, keyed `snake_case`,
  each with its display name as `title` and its vocabulary as `x-vocab`;
- a text-only register is a non-empty string;
- the section a register sits in, its business-language scope, and the phase's handoff.

Controlled vocabularies go to one VOCABULARY artifact, one named group per closed set, referenced by
the schema and never copied into it.

    python scripts/rebuild/template_to_schema.py

Deleted at the swap: once written, the schemas are edited, never regenerated.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from transformation.design.template_reader import load

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "registry/schema"
VOCAB_PATH = REPO / "registry/design/vocabulary/VOCAB_DESIGN_REGISTER_TERMS_V0.md"
VOCAB_FQDN = "transformation::VOCAB_DESIGN_REGISTER_TERMS_V0"
PHASES = ("p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8")

# One name per closed set. A set declared in two orders is one set, in the order given here.
GROUPS = {
    ("HIGH", "MEDIUM", "LOW"): "certainty",
    ("YES", "NO"): "yes_no",
    ("NEW_SUBDOMAIN", "EXTEND_SUBDOMAIN", "MODIFY", "DEPRECATE"): "classification",
    ("REUSE", "EXTEND", "AUTHOR_NEW"): "reuse_decision",
    ("NEW_SUBDOMAIN", "EXTEND"): "placement_decision",
    ("INPUT", "OUTPUT"): "field_direction",
    ("INPUT", "OUTPUT", "ATTRIBUTE"): "interface_direction",
    ("INGRESS", "EGRESS"): "transport_direction",
    ("EXISTING", "EXTEND", "REUSE", "AUTHOR_NEW", "INVESTIGATE"): "dependency_disposition",
    ("INHERITED", "REFINED"): "purpose_disposition",
    ("OWNED", "SATISFIED", "DEFERRED"): "ownership_disposition",
    ("OBSERVED", "INFERRED", "OPEN"): "evidence_status",
    ("SUCCESS", "VIOLATION"): "expected_outcome",
    ("AC", "IN", "WF", "CC", "CT", "EV", "RB", "VOCAB", "STRUCTURE", "TI", "TE"): "artifact_family",
    ("EXACT", "PARTIAL", "MISMATCH"): "fit",
    ("WF_INVOCATION", "SNAPSHOT_READ"): "handler_kind",
    ("CT", "CS"): "composition_kind",
    ("IN", "CC", "EXIT", "EXIT_SUCCESS"): "node_type",
    ("HUMAN", "SNAPSHOT", "GOVERNANCE"): "clarification_owner",
    ("MUTABLE_STATE", "APPEND_ONLY_JOURNAL", "IDENTITY_REGISTRY", "HYBRID"): "record_model",
    ("CREATED", "EXTENDED", "MODIFIED", "DEPRECATED", "ADJACENT"): "scope_relationship",
    ("CLOSED", "OPEN"): "resolution_status",
    ("VERIFIED", "NOT_FOUND", "INSUFFICIENT_EVIDENCE"): "belief_result",
    ("CONFIRMED", "OVERTURNED"): "verification_result",
    ("INPUT", "CARRY", "UPDATE"): "molecule_binding_role",
    ("INPUT", "EXPECTED", "ASSERT", "RECORDED"): "test_value_role",
    ("SATISFIED", "NOT_SATISFIED"): "saturation_status",
    ("IN_SCOPE", "DEFERRED"): "scope_status",
    ("SATISFIED", "GAP"): "dependency_status",
    ("CS_APPENDONLY_JSONL_V0", "CS_MUTABLE_JSON_V0", "CS_REGISTRY_V0"): "storage_type",
    ("REPLACE", "REVIEW", "REUSE", "EXTEND"): "pps_action",
    ("REPLACE", "REUSE", "EXTEND", "REPOINT", "REVIEW"): "inventory_action",
    ("REPLACE", "EXTEND", "NEW"): "gap_resolution",
}


def key(column: str) -> str:
    """A column's key. `#`, an ordinal with no name, is keyed `number`."""
    return re.sub(r"[^a-z0-9]+", "_", column.strip().lower()).strip("_") or "number"


def group_of(values: tuple[str, ...]) -> str:
    for declared, name in GROUPS.items():
        if set(declared) == set(values):
            return name
    raise SystemExit(f"no group named for {values}")


def schema(phase: str) -> dict:
    template = load(phase)
    registers: dict[str, dict] = {}
    for r in template.registers:
        section = {"number": r.section_number, "title": r.section_title}
        if not r.columns:
            registers[r.id] = {"type": "string", "minLength": 1, "x-section": section}
            continue
        properties: dict[str, dict] = {}
        for column in r.columns:
            prop: dict = {"title": column}
            if column in r.vocabularies:
                prop["x-vocab"] = {"artifact": VOCAB_FQDN, "group": group_of(r.vocabularies[column])}
            properties[key(column)] = prop
        body: dict = {
            "type": "array",
            "x-section": section,
            "items": {
                "type": "object",
                "properties": properties,
                "required": [key(c) for c in r.required_columns],
            },
        }
        if not r.optional:
            body["minItems"] = 1
        if r.business_language:
            body["x-business-language"] = True
        elif r.scoped_flags.get("business_language"):
            body["x-business-language"] = [key(c) for c in r.business_language_columns]
        registers[r.id] = body
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"transformation.schemas.REGISTER_SCHEMA_{phase.upper()}_V0",
        "$comment": "The registers a phase document's Machine block carries, and their shape.",
        "type": "object",
        "required": ["registers"],
        "x-consumes": list(template.consumes),
        "x-emits": list(template.emits),
        "properties": {
            "registers": {
                "type": "object",
                "required": [r.id for r in template.registers],
                "properties": registers,
            },
        },
    }


def vocabulary() -> str:
    groups = {name: {"casing": "UPPER_SNAKE", "entries": list(values)} for values, name in GROUPS.items()}
    machine = {
        "fqdn": VOCAB_FQDN,
        "artifact_kind": "VOCABULARY",
        "version": "v0",
        "governed_by": "vocabulary::CONSTITUTION_VOCABULARY_V0",
        "authority": "pgc.platform",
        "concern": "design",
        "extends": "",
        **{name: groups[name] for name in sorted(groups)},
    }
    block = yaml.safe_dump(machine, sort_keys=False, allow_unicode=True, width=100)
    return (
        "# VOCAB_DESIGN_REGISTER_TERMS_V0\n\n## Machine\n\n```yaml\n" + block + "```\n\n---\n\n"
        "## Intent\n\n"
        "The closed sets a phase document's registers draw on. Each register schema names the group a\n"
        "column takes its values from, and nothing restates a group's entries.\n"
    )


def main() -> int:
    SCHEMAS.mkdir(parents=True, exist_ok=True)
    for phase in PHASES:
        out = SCHEMAS / f"REGISTER_SCHEMA_{phase.upper()}_V0.json"
        out.write_text(json.dumps(schema(phase), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    VOCAB_PATH.parent.mkdir(parents=True, exist_ok=True)
    VOCAB_PATH.write_text(vocabulary(), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
