"""Read a phase document into registers.

A phase document carries its facts in one Machine block, a fenced YAML block under `## Machine`,
and its prose around it. This reader splits the two and parses the YAML. It applies no convention:
no table is read, and no column is matched by prefix here.

This is a reader, not a validator: it reports what the document contains and says nothing about
whether that is admissible. A document with no Machine block, or one that does not parse, yields no
header and no registers, and the rule set reports every register missing. A reader that raised would
report a parse error where the author needs a governance finding.

The shape it returns is the one every consumer receives: header fields, the sections of the prose,
and the registers, each a table as columns and rows or a text-only register as its text. `parse_text`
is the single parser. The compiled transforms call it and return plain data across the capability
boundary.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from transformation.design.evaluate import ParsedDocument

HEADING = re.compile(r"^##\s+(?:(\d+[a-z]?)\.\s+)?(.+?)\s*$")
MACHINE_HEADING = "## Machine"
FENCE_OPEN = re.compile(r"^```ya?ml\s*$")
FENCE_CLOSE = "```"


def _text(value: Any) -> str:
    """A cell as the text the rules judge. A value YAML typed (a number, a boolean) is read back as
    the text that wrote it; an absent value is empty."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _machine_block(lines: list[str]) -> tuple[Any, set[int]]:
    """The parsed Machine block, and the line indexes it occupies, heading included."""
    for i, line in enumerate(lines):
        if line.strip() != MACHINE_HEADING:
            continue
        opened = next((j for j in range(i + 1, len(lines)) if lines[j].strip()), None)
        if opened is None or not FENCE_OPEN.match(lines[opened].strip()):
            return None, {i}
        closed = next((j for j in range(opened + 1, len(lines))
                       if lines[j].strip() == FENCE_CLOSE), None)
        if closed is None:
            return None, set(range(i, len(lines)))
        try:
            data = yaml.safe_load("\n".join(lines[opened + 1:closed]))
        except yaml.YAMLError:
            data = None
        return data, set(range(i, closed + 1))
    return None, set()


def _registers(data: Any) -> list[dict[str, Any]]:
    registers: list[dict[str, Any]] = []
    declared = data.get("registers") if isinstance(data, dict) else None
    if not isinstance(declared, dict):
        return registers
    for register_id, body in declared.items():
        if isinstance(body, dict):
            columns = [_text(c) for c in (body.get("columns") or [])]
            rows = []
            for row in body.get("rows") or []:
                if isinstance(row, dict):
                    rows.append({_text(k): _text(row.get(k)) for k in row})
            registers.append({"id": str(register_id), "columns": columns, "rows": rows, "text": ""})
        else:
            registers.append({"id": str(register_id), "columns": [], "rows": [], "text": _text(body)})
    return registers


def parse_text(text: str) -> tuple[dict[str, str], list[dict[str, Any]], list[dict[str, Any]]]:
    """Parse document text into (header fields, sections, registers) as plain data."""
    lines = text.splitlines()
    data, machine_lines = _machine_block(lines)

    header: dict[str, str] = {}
    if isinstance(data, dict) and isinstance(data.get("header"), dict):
        header = {str(k): _text(v) for k, v in data["header"].items()}

    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    body: list[str] = []
    for i, line in enumerate(lines):
        if i in machine_lines:
            continue
        match = HEADING.match(line)
        if match:
            if current is not None:
                current["text"] = "\n".join(body)
                sections.append(current)
            current = {
                "number": int(match.group(1)) if match.group(1) and match.group(1).isdigit() else None,
                "title": match.group(2).strip(),
                "columns": [],
                "rows": [],
            }
            body = []
        elif current is not None:
            body.append(line)
    if current is not None:
        current["text"] = "\n".join(body)
        sections.append(current)

    return header, sections, _registers(data)


def read_seed(path: Path) -> ParsedDocument:
    """Read a seed document from disk. Absence of the file is fail-hard.

    Reading is the driver's job, never a transform's — this is the boundary that keeps the
    compiled phase pure and its verdict reproducible.
    """
    if not path.is_file():
        raise FileNotFoundError(f"seed not found: {path}")

    raw = path.read_text(encoding="utf-8")
    header, sections, registers = parse_text(raw)
    return ParsedDocument(
        header=header, sections=sections, registers=registers, raw=raw, path=str(path)
    )
