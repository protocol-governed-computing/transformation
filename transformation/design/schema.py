"""Load a phase's register schema: the declaration of what its document must carry.

Each phase's shape is a JSON Schema in `registry/schema/`, with an `$id`. It declares the registers,
their columns, which may be empty, which hold business prose, and which controlled vocabulary a
column draws on. Rules that follow from shape are expanded from it (`expand.py`), so it is the one
declaration of a document's shape. The phase templates are guides for an author, checked against it.

A column's vocabulary is a reference, `x-vocab: {artifact, group}`, to a group of a VOCABULARY
artifact. It is resolved from the artifact's declaration and never copied into the schema.

Every schema is validated against `SCHEMA_REGISTER_SCHEMA_V0` when it is loaded, so a schema using a
keyword the evaluator does not implement is refused rather than silently ignored.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import jsonschema
import yaml

REPO = Path(__file__).resolve().parents[2]
SCHEMAS = REPO / "registry" / "schema"
META = SCHEMAS / "SCHEMA_REGISTER_SCHEMA_V0.json"
REGISTRY = REPO / "registry"
MACHINE_BLOCK = re.compile(r"## Machine\s*\n+```yaml\n(.*?)\n```", re.S)

# Columns that cite rather than state. A citation names its subject — including, in a grounding
# phase, a compiled artifact — so these are never business-language columns.
_PROVENANCE_COLUMNS = ("Source Finding", "Evidence")


def _is_provenance_column(column: str) -> bool:
    return any(column.startswith(p) for p in _PROVENANCE_COLUMNS)


@dataclass(frozen=True)
class Register:
    """One declared register of a phase document."""

    id: str
    section_number: str | None
    section_title: str
    columns: tuple[str, ...]
    keys: tuple[str, ...] = ()
    vocabularies: dict[str, tuple[str, ...]] = field(default_factory=dict)
    required_columns: tuple[str, ...] = ()
    optional: bool = False
    business_language_scope: tuple[str, ...] | bool = ()

    @property
    def business_language(self) -> bool:
        """The register holds business prose throughout and must name no compiled artifact."""
        return self.business_language_scope is True

    @property
    def business_language_columns(self) -> tuple[str, ...]:
        """Columns that must hold business prose and name no compiled artifact.

        The register-wide flag exempts provenance columns: `Source Finding` and `Evidence` are
        citations by construction, and in a phase that grounds against the composition they must
        name artifacts. A scoped flag names exactly the columns it constrains.
        """
        if self.business_language_scope is True:
            return tuple(c for c in self.columns if not _is_provenance_column(c))
        by_key = dict(zip(self.keys, self.columns))
        return tuple(by_key[k] for k in self.business_language_scope or ())

    @property
    def optional_columns(self) -> tuple[str, ...]:
        required = set(self.required_columns)
        return tuple(c for c in self.columns if c not in required)

    @property
    def traceable(self) -> bool:
        """Rows cite where they came from."""
        return any(c.startswith("Source Finding") for c in self.columns)

    @property
    def headings(self) -> tuple[str, ...]:
        """Each column as a document heads it: its name, then any vocabulary it admits."""
        return tuple(
            f"{c} ({', '.join(self.vocabularies[c])})" if c in self.vocabularies else c
            for c in self.columns
        )


@dataclass(frozen=True)
class PhaseShape:
    """A phase's registers and its declared handoff, as its register schema states them."""

    phase: str
    schema_id: str
    path: Path
    registers: tuple[Register, ...]
    consumes: tuple[str, ...] = ()
    emits: tuple[str, ...] = ()

    def register(self, register_id: str) -> Register:
        for r in self.registers:
            if r.id == register_id:
                return r
        raise KeyError(f"{self.phase} declares no register {register_id!r}")


@lru_cache(maxsize=None)
def vocabulary_group(artifact: str, group: str) -> tuple[str, ...]:
    """The entries of one group of a VOCABULARY artifact, read from its declaration."""
    code = artifact.split("::")[-1]
    found = sorted(REGISTRY.rglob(f"{code}.md"))
    if not found:
        raise KeyError(f"vocabulary {artifact} is declared nowhere in {REGISTRY}")
    machine = yaml.safe_load(MACHINE_BLOCK.search(found[0].read_text(encoding="utf-8")).group(1))
    if machine.get("fqdn") != artifact:
        raise KeyError(f"{found[0]} declares {machine.get('fqdn')}, not {artifact}")
    if group not in machine:
        raise KeyError(f"vocabulary {artifact} has no group {group!r}")
    return tuple(machine[group]["entries"])


@lru_cache(maxsize=None)
def _meta() -> dict:
    return json.loads(META.read_text(encoding="utf-8"))


def read_schema(path: Path, phase: str) -> PhaseShape:
    """Parse a register schema. One that the meta-schema refuses is fail-hard."""
    declared = json.loads(path.read_text(encoding="utf-8"))
    jsonschema.validate(declared, _meta())
    registers: list[Register] = []
    for register_id, body in declared["properties"]["registers"]["properties"].items():
        section = body.get("x-section") or {}
        if body["type"] == "string":
            registers.append(Register(id=register_id, section_number=section.get("number"),
                                      section_title=section.get("title", ""), columns=(),
                                      optional=False))
            continue
        items = body["items"]
        keys = tuple(items["properties"])
        columns = tuple(items["properties"][k]["title"] for k in keys)
        vocabularies = {
            items["properties"][k]["title"]: vocabulary_group(**items["properties"][k]["x-vocab"])
            for k in keys if "x-vocab" in items["properties"][k]
        }
        required = set(items.get("required") or ())
        scope = body.get("x-business-language", ())
        registers.append(Register(
            id=register_id,
            section_number=section.get("number"),
            section_title=section.get("title", ""),
            columns=columns,
            keys=keys,
            vocabularies=vocabularies,
            required_columns=tuple(c for k, c in zip(keys, columns) if k in required),
            optional=body.get("minItems", 0) == 0,
            business_language_scope=scope if scope is True else tuple(scope),
        ))
    return PhaseShape(
        phase=phase,
        schema_id=declared["$id"],
        path=path,
        registers=tuple(registers),
        consumes=tuple(declared.get("x-consumes") or ()),
        emits=tuple(declared.get("x-emits") or ()),
    )


@lru_cache(maxsize=None)
def load(phase: str) -> PhaseShape:
    """Load a phase's register schema, named by the phase catalogue."""
    from transformation.design.catalog import phase as phase_spec

    return read_schema(SCHEMAS / phase_spec(phase).schema, phase)
