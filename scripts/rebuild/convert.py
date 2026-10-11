"""Convert a phase document from tables to a Machine block, with the oracle's own reader.

The oracle reads the Markdown, and what it returns is written out as data. The conversion is
mechanical: no value is edited, so a difference in findings between the two forms is a difference in
reading, never in content. It runs against the oracle, not the rebuild, because the rebuild no longer
reads tables:

    PYTHONPATH=~/pgc-oracle/transformation python scripts/rebuild/convert.py SRC DST [SRC DST ...]

What moves into the Machine block:
- the header fields the oracle reads from the preamble;
- every register: a text-only register as its text, and a table as a list of rows, each a mapping
  from column key to value. A register whose only row is the emptiness sentinel is `[]`, declared
  empty; a table with no rows at all is `null`, present and stating nothing.

Each value takes the type its column declares in the rebuild's register schema. A none marker is
`null`. A list, a routing, an interface, a binding and a test value are structured as the oracle's
own reading reads them. A blank test value leaves its column out of the row. A citation becomes a
mapping naming what it cites (M3.3b). A cell that does not structure cleanly is kept as the text it was, and the
rebuild refuses its type.

What stays prose: headings, narrative, and any table no register marker opens. Each register's
marker and table, and each header line, leave the prose.

Deleted at the swap, with the table reader it runs.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

import header as header_form  # this directory; the oracle runs the script from here
import typed_values
import transformation
from transformation.design import read as oracle_read
from transformation.design.checks import is_sentinel
from transformation.design.p7_design_intent.rules import LITERAL_FORMS
from transformation.build.render import _binding as render_step, _bound_value as render_entrance
from transformation.build.render import _molecule_source as render_molecule

if "pgc-oracle" not in str(Path(transformation.__file__).resolve()):
    raise SystemExit(f"convert.py must run against the oracle; imported {transformation.__file__}")


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper: yaml.SafeDumper, value: str) -> yaml.Node:
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _str)

# A citation is written on one line, `{phase: p2, register: gaps, row: 1}`, as an author writes it.
_CITATION_KEYS = {"phase", "register", "row", "key", "artifact", "source"}


def _mapping(dumper: yaml.SafeDumper, value: dict) -> yaml.Node:
    flow = bool(value) and set(value) <= _CITATION_KEYS and bool({"register", "artifact", "source"} & set(value))
    return dumper.represent_mapping("tag:yaml.org,2002:map", value, flow_style=flow or None)


_Dumper.add_representer(dict, _mapping)


REBUILD_SCHEMAS = Path(__file__).resolve().parents[2] / "registry" / "schema"
NONE_MARKERS = ("—", "-", "NONE", "N/A")
VOCAB_IN_COLUMN = re.compile(r"^(?P<name>[^(]+?)\s*\((?P<values>[A-Z][A-Z0-9_]*(?:\s*,\s*[A-Z][A-Z0-9_]*)+)\)\s*$")
LITERAL = re.compile(rf"^(?:{LITERAL_FORMS})$")
LIST_PROPERTIES = re.compile(r"^(?:emit\..+|supersedes|parameters)$")


def _key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_") or "number"


def _columns() -> dict[str, dict[str, dict]]:
    """register id → column key → its column declaration, across every phase's schema."""
    out: dict[str, dict[str, dict]] = {}
    for path in sorted(REBUILD_SCHEMAS.glob("REGISTER_SCHEMA_P*.json")):
        for rid, body in json.loads(path.read_text(encoding="utf-8"))["properties"]["registers"]["properties"].items():
            out.setdefault(rid, {}).update((body.get("items") or {}).get("properties") or {})
    return out


COLUMNS = _columns()


def _seed_sections() -> dict[str, str]:
    """The seed's section number → its register id. A seed is cited by section number."""
    declared = json.loads((REBUILD_SCHEMAS / "REGISTER_SCHEMA_P0_V0.json").read_text(encoding="utf-8"))
    return {body["x-section"]["number"]: rid
            for rid, body in declared["properties"]["registers"]["properties"].items()
            if (body.get("x-section") or {}).get("number") is not None}


SEED_SECTIONS = _seed_sections()
IDENTITY = re.compile(r"^[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+$")
SEED = re.compile(r"^CR seed\s*§\s*(\d+)\b[^#]*?(?:#\s*(\d+))?\s*$")
STAGED = re.compile(r"^S(\d+)[a-z]?\s+([a-z][a-z0-9_]*)\b\s*(.*)$")
LOCAL = re.compile(r"^([a-z][a-z0-9_]*)\s+#\s*(\d+)$")
ORDINAL = re.compile(r"^#\s*(\d+)\b\s*(?:[—–-]\s*.*)?$")
# Several citations are separated by `;` or ` · `, each followed by the start of another citation. A
# `;` inside a trailing remark separates nothing.
SEVERAL = re.compile(r"\s*;\s*(?=S\d|CR seed|human decision|[a-z][a-z0-9_.]*(?:::|\s+#))|\s+·\s+(?=S\d|CR seed)")


def _one_citation(part: str):
    """One citation as a mapping, or None when it does not structure."""
    if part == "human decision":
        return {"source": "human"}
    if IDENTITY.match(part):
        return {"artifact": part}
    seed = SEED.match(part)
    if seed:
        register = SEED_SECTIONS.get(seed.group(1))
        if register is None:
            return None
        return {"phase": "p0", "register": register, **({"row": int(seed.group(2))} if seed.group(2) else {})}
    staged = STAGED.match(part)
    if staged:
        cited = {"phase": f"p{staged.group(1)}", "register": staged.group(2)}
        rest = staged.group(3).strip()
        if not rest:
            return cited
        ordinal = ORDINAL.match(rest)
        if ordinal:
            return {**cited, "row": int(ordinal.group(1))}
        key = re.sub(r"^[—–-]\s*", "", rest).strip()
        return {**cited, "key": key} if key else cited
    local = LOCAL.match(part)
    if local:
        return {"register": local.group(1), "row": int(local.group(2))}
    return None


def _citation(cell: str):
    """A citation cell as a mapping, or a list for several. A blank cites nothing, `null`. One that
    does not structure stays the text it was, and the rebuild refuses its type."""
    if cell == "" or cell in NONE_MARKERS:
        return None
    parts = [p for p in SEVERAL.split(cell) if p.strip()]
    cited = [_one_citation(p.strip()) for p in parts]
    if any(c is None for c in cited):
        return cell
    return cited[0] if len(cited) == 1 else cited


def _column_key(register_id: str, header: str) -> str:
    """The key a document's column header reads as. The oracle addresses a column by the start of
    its header, so a header is the declared column whose title it starts with, the longest first."""
    declared = COLUMNS.get(register_id, {})
    match = VOCAB_IN_COLUMN.match(header)
    name = match.group("name").strip() if match else header.strip()
    if _key(name) in declared:
        return _key(name)
    titled = sorted(((c["title"], k) for k, c in declared.items() if header.startswith(c["title"])),
                    key=lambda tk: -len(tk[0]))
    return titled[0][1] if titled else _key(name)


def _names(cell: str, separators: str = ",") -> list[str]:
    parts = re.split(f"[{re.escape(separators)}]", cell)
    return [p.strip() for p in parts if p.strip() and p.strip() not in NONE_MARKERS]


def _routing(cell: str):
    # An ending written `emit <moment>` names what it announces, which the design declares as an
    # `emit.<ending>` property. The oracle reads it as no routes, and so does this (charter M3.3-8).
    if cell.startswith("emit ") and "->" not in cell:
        return None
    out = {}
    for segment in (s.strip() for s in cell.split(";")):
        if not segment:
            continue
        outcome, sep, target = segment.partition("->")
        if not sep or not outcome.strip() or not target.strip():
            return cell
        out[outcome.strip()] = target.strip()
    return out


def _interface(cell: str):
    out: dict[str, dict[str, str]] = {}
    for part in (p.strip() for p in cell.split(";")):
        if not part:
            continue
        head, sep, body = part.partition(":")
        side = head.strip().lower()
        if not sep or side not in ("in", "out") or side in out:
            return cell
        out[side] = {}
        for pair in (x.strip() for x in body.split(",")):
            if not pair:
                continue
            name, _, mapped = pair.partition("=")
            if not name.strip():
                return cell
            out[side][name.strip()] = mapped.strip()
    return out


# How the oracle's construction renders a binding's value, per register. A literal is stored as the
# value construction would have handed the runtime, so the rebuild renders it unchanged.
RENDER = {"step_bindings": render_step, "transport_bindings": render_entrance,
          "molecule_step_bindings": render_molecule}


def _binding(register_id: str, cell: str):
    if cell.lower() == "generated":
        return {"generated": True}
    if register_id == "molecule_step_bindings" and cell == "iterator":
        return cell
    if not LITERAL.match(cell):
        return cell
    try:
        return {"literal": RENDER[register_id](cell)}
    except ValueError:
        return cell


# A column whose value may be anything has no text that means "nothing stated": `""` and `null` are
# values. A blank cell leaves the column out of its row.
OMIT = object()


# Columns that take any value but that the oracle wrote as text. They convert as text, and
# `typed_values` types what the oracle read as a number or a flag (M5-1).
WRITTEN_AS_TEXT = {("interface_fields", "default"), ("artifact_properties", "value")}


def _test_value(cell: str):
    if cell == "":
        return OMIT
    try:
        return yaml.safe_load(cell)
    except yaml.YAMLError:
        return cell


def _value(register_id: str, key: str, cell: str, row: dict[str, str]):
    cell = cell.strip()
    declared = COLUMNS.get(register_id, {}).get(key, {})
    kind = declared.get("type")
    if register_id == "artifact_properties" and key == "value":
        prop = next((v for h, v in row.items() if _column_key(register_id, h) == "property"), "")
        kind = ["array", "null"] if LIST_PROPERTIES.match(prop.strip()) else ["string", "null"]
    if declared.get("$ref") == "#/$defs/citation":
        return _citation(cell)
    if "oneOf" in declared:
        return None if cell in NONE_MARKERS else ("" if cell == "" else _binding(register_id, cell))
    if key in COLUMNS.get(register_id, {}) and "type" not in declared \
            and (register_id, key) not in WRITTEN_AS_TEXT:
        return _test_value(cell)
    if cell in NONE_MARKERS:
        return None
    if kind == ["array", "null"]:
        return _names(cell, ",;" if key == "depends_on" else ",")
    if kind == ["object", "null"]:
        if cell == "":
            return {}
        return _interface(cell) if key == "interface" else _routing(cell)
    return cell


def _register(entry: dict):
    if not entry["columns"]:
        return entry["text"]
    content = [row for row in entry["rows"] if not is_sentinel(row)]
    if not entry["rows"]:
        return None
    if not content:
        return []
    out = []
    for row in content:
        mapped: dict = {}
        for header, cell in row.items():
            key = _column_key(entry["id"], header)
            if key not in mapped:
                value = _value(entry["id"], key, cell, row)
                if value is not OMIT:
                    mapped[key] = value
        out.append(mapped)
    return out


def _owned_lines(lines: list[str]) -> set[int]:
    """Indexes of the lines the Machine block takes over: header fields, markers, register tables
    and text-only register bodies. Located exactly the way the oracle's reader locates them."""
    owned: set[int] = set()
    first_heading = next((i for i, l in enumerate(lines) if oracle_read.HEADING.match(l)), len(lines))
    for i in range(first_heading):
        if oracle_read.BULLET_FIELD.match(lines[i].strip()):
            owned.add(i)
    for i, line in enumerate(lines):
        if not oracle_read.REGISTER_MARKER.match(line):
            continue
        owned.add(i)
        header_at = next((j for j in range(i + 1, min(i + 4, len(lines)))
                          if lines[j].lstrip().startswith("|")), None)
        if header_at is not None:
            j = header_at
            while j < len(lines) and lines[j].strip().startswith("|"):
                owned.add(j)
                j += 1
        else:
            for j in range(i + 1, len(lines)):
                if oracle_read.HEADING.match(lines[j]) or oracle_read.REGISTER_MARKER.match(lines[j]):
                    break
                owned.add(j)
    return owned


def convert(text: str) -> str:
    header, _, registers = oracle_read.parse_text(text)
    block: dict = {"document": header_form.document(header, text.splitlines()[0] if text else ""),
                   "registers": {}}
    for entry in registers:
        if entry["id"] not in block["registers"]:
            block["registers"][entry["id"]] = _register(entry)

    lines = text.splitlines()
    owned = _owned_lines(lines)
    prose = [line for i, line in enumerate(lines) if i not in owned]
    machine = yaml.dump(block, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100000)

    title_end = 1 if prose and prose[0].startswith("# ") else 0
    out = prose[:title_end] + ["", "## Machine", "", "```yaml", machine.rstrip("\n"), "```", ""]
    out += prose[title_end:]
    collapsed: list[str] = []
    for line in out:
        if line.strip() == "" and collapsed and collapsed[-1].strip() == "":
            continue
        collapsed.append(line)
    return typed_values.migrate("\n".join(collapsed).rstrip("\n") + "\n")


def main(argv: list[str]) -> int:
    if not argv or len(argv) % 2:
        print(__doc__)
        return 2
    for src, dst in zip(argv[::2], argv[1::2]):
        out = Path(dst)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(convert(Path(src).read_text(encoding="utf-8")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
