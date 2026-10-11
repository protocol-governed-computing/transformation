"""Give the structured columns their types, once (charter §8, M3.3a).

Every column is text, or null when it says nothing. The columns measured to carry structure get
their JSON Schema type: a list of names, a routing (outcome to target), an interface (`in` and
`out`), a binding (a path, a literal or a generated value), a test value (any YAML value), or a
citation (M3.3b).

    python scripts/rebuild/type_columns.py

Deleted at the swap.
"""
from __future__ import annotations

import json
from pathlib import Path

SCHEMAS = Path(__file__).resolve().parents[2] / "registry/schema"

TEXT = {"type": ["string", "null"]}
LIST = {"type": ["array", "null"], "items": {"type": "string"}}
ROUTING = {"type": ["object", "null"], "additionalProperties": {"type": "string"}}
INTERFACE = {"type": ["object", "null"], "additionalProperties": False,
             "properties": {"in": {"type": "object", "additionalProperties": {"type": "string"}},
                            "out": {"type": "object", "additionalProperties": {"type": "string"}}}}
BINDING = {"oneOf": [
    {"type": "null"},
    {"type": "string"},
    {"type": "object", "required": ["literal"], "additionalProperties": False, "properties": {"literal": {}}},
    {"type": "object", "required": ["generated"], "additionalProperties": False,
     "properties": {"generated": {"const": True}}},
]}
ANY = {}
# A citation names a row of a register (by ordinal or by what it says), a whole register, an
# artifact already in the composition, or a human ruling. A cell citing several holds a list.
_REFERENCE = {"type": "object", "required": ["register"], "additionalProperties": False,
              "properties": {"phase": {"type": "string", "pattern": "^p[0-8]$"},
                             "register": {"type": "string", "pattern": "^[a-z][a-z0-9_]*$"},
                             "row": {"type": "integer"},
                             "key": {"type": "string", "minLength": 1}},
              "not": {"required": ["row", "key"]}}
_ARTIFACT = {"type": "object", "required": ["artifact"], "additionalProperties": False,
             "properties": {"artifact": {"type": "string",
                                         "pattern": "^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V[0-9]+$"}}}
_HUMAN = {"type": "object", "required": ["source"], "additionalProperties": False,
          "properties": {"source": {"const": "human"}}}
CITATION = {"oneOf": [
    {"type": "null"}, _REFERENCE, _ARTIFACT, _HUMAN,
    {"type": "array", "minItems": 2, "items": {"oneOf": [_REFERENCE, _ARTIFACT, _HUMAN]}},
]}
# A property value names several things for these properties, and one thing for every other.
PROPERTY_VALUE = {"type": ["string", "array", "null"], "items": {"type": "string"}}

TYPED = {
    ("execution_topology", "routing"): ROUTING,
    ("cc_composition", "routing"): ROUTING,
    ("cc_composition", "interface"): INTERFACE,
    ("cc_composition", "consumes"): LIST,
    ("cc_composition", "produces"): LIST,
    ("rb_declarations", "cs_bindings"): LIST,
    ("generation_provenance", "generator_sources"): LIST,
    ("declared_reach", "consults"): LIST,
    ("build_order", "depends_on"): LIST,
    ("step_bindings", "bound_to"): BINDING,
    ("transport_bindings", "bound_to"): BINDING,
    ("molecule_step_bindings", "bound_to"): BINDING,
    ("test_case_values", "value"): ANY,
    ("artifact_properties", "value"): PROPERTY_VALUE,
}


def main() -> int:
    for path in sorted(SCHEMAS.glob("REGISTER_SCHEMA_P*.json")):
        declared = json.loads(path.read_text(encoding="utf-8"))
        for register_id, body in declared["properties"]["registers"]["properties"].items():
            for key, column in (body.get("items") or {}).get("properties", {}).items():
                cites = key == "source_finding" or (register_id, key) == ("verification_results", "origin")
                if cites:
                    column.pop("type", None)
                    column["$ref"] = "#/$defs/citation"
                    declared.setdefault("$defs", {})["citation"] = CITATION
                else:
                    column.update(TYPED.get((register_id, key), TEXT))
        path.write_text(json.dumps(declared, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
