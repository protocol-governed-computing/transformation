"""CT_PURE_ATTRIBUTE_PROVENANCE_V0 — where each rendered value came from.

The measure that admits a design to construction used to test whether a leaf was non-empty, and a
value the renderer wrote from its own text is non-empty. So a renderer that never asked the design
for a fact could supply it and the design still measured complete — which is a second design
authority nobody approved.

Presence cannot distinguish the two. Provenance can, and only the renderer knows it: it is the thing
that put the value there. This reports one origin per leaf from what the renderer recorded.

  stated_by_design           a register of the design carries it
  governed_elsewhere         a constitution fixes it, and the artifact fixing it is named
  carried_from_predecessor   the artifact already carried it and no register can express it
  supplied_by_renderer       the renderer wrote it on its own authority, and nothing governs it

Only the last is unaccounted for. Silence means the design stated it: a builder reaches for a
register and writes what it finds, so the ordinary case needs no record and only a departure does.

CONSTITUTIONAL: Pure — no I/O, no clock, no filesystem.
"""
from __future__ import annotations

from typing import Any

STATED_BY_DESIGN = "stated_by_design"


def _leaves(value: Any, path: str = ""):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _leaves(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            key = next((item[k] for k in ("step", "code", "name")
                        if isinstance(item, dict) and item.get(k)), index)
            yield from _leaves(item, f"{path}[{key}]")
    else:
        yield path


def _origin(sources: dict, path: str) -> tuple[str, str]:
    """The origin recorded for a leaf, and what governs it where anything does.

    A record on an ancestor covers what hangs beneath it: a builder supplying a whole field supplies
    every leaf of it, and making it enumerate them would be asking it to walk a shape it has not
    finished building.
    """
    if path in sources:
        entry = sources[path]
        return tuple(entry) if isinstance(entry, (list, tuple)) else (entry, "")
    for ancestor, entry in sources.items():
        if path.startswith(ancestor + "."):
            return tuple(entry) if isinstance(entry, (list, tuple)) else (entry, "")
    return (STATED_BY_DESIGN, "")


def execute(inputs: dict, **_: Any) -> dict:
    rendered = inputs["rendered"]
    sources = inputs["sources"] or {}

    provenance: dict[str, str] = {}
    governing: dict[str, str] = {}
    for artifact in rendered:
        machine = artifact.get("machine") or {}
        code = str(machine.get("fqdn", "")).split("::")[-1]
        recorded = sources.get(code) or sources
        for path in _leaves(machine):
            origin, governed_by = _origin(recorded, path)
            provenance[f"{code}{path}"] = origin
            if governed_by:
                governing[f"{code}{path}"] = governed_by

    return {"provenance": provenance, "governing_artifacts": governing}
