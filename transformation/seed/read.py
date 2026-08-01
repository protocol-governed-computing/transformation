"""Read a phase document into registers.

This is a reader, not a validator: it reports what the document contains and says nothing about
whether that is admissible. Malformed input yields an empty or partial structure and lets the rule
set produce the finding — a reader that raised would report a parse error where the author needs a
governance finding.

`parse_text` is the single parser. The compiled transform calls it and returns plain data across the
capability boundary; the genesis oracle calls it and wraps the result. One parser, so a differential
run compares rule evaluation rather than two different readers.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from transformation.seed.evaluate import ParsedDocument

HEADING = re.compile(r"^##\s+(?:(\d+)\.\s+)?(.+?)\s*$")
BULLET_FIELD = re.compile(r"^-\s+\*\*(?P<name>[^:*]+):\*\*\s*(?P<value>.*?)\s*$")
TABLE_DIVIDER = re.compile(r"^\|[\s:|-]+\|$")


def _split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def _read_table(lines: list[str]) -> tuple[list[str], list[dict[str, str]]]:
    """Extract the first pipe table in a block.

    A table needs a header row and a divider. Zero data rows is a legitimate document state (an
    empty Assumptions table) and is the rule set's business, not the reader's.
    """
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        if i + 1 >= len(lines) or not TABLE_DIVIDER.match(lines[i + 1].strip()):
            continue

        columns = _split_row(line)
        rows: list[dict[str, str]] = []
        for row_line in lines[i + 2:]:
            if not row_line.strip().startswith("|"):
                break
            cells = _split_row(row_line)
            if len(cells) != len(columns):
                # Ragged row: keep what aligns so a rule can name the offending row.
                cells = (cells + [""] * len(columns))[: len(columns)]
            rows.append(dict(zip(columns, cells)))
        return columns, rows
    return [], []


def parse_text(text: str) -> tuple[dict[str, str], list[dict[str, Any]]]:
    """Parse document text into (header fields, ordered sections) as plain data."""
    header: dict[str, str] = {}
    sections: list[dict[str, Any]] = []

    current: dict[str, Any] | None = None
    current_lines: list[str] = []
    preamble: list[str] = []

    def close() -> None:
        if current is None:
            return
        columns, rows = _read_table(current_lines)
        current["text"] = "\n".join(current_lines)
        current["columns"] = columns
        current["rows"] = rows
        sections.append(current)

    for line in text.splitlines():
        match = HEADING.match(line)
        if match:
            close()
            current = {
                "number": int(match.group(1)) if match.group(1) else None,
                "title": match.group(2).strip(),
            }
            current_lines = []
            continue
        if current is None:
            preamble.append(line)
        else:
            current_lines.append(line)

    close()

    for line in preamble:
        field_match = BULLET_FIELD.match(line.strip())
        if field_match:
            header[field_match.group("name").strip()] = field_match.group("value").strip()

    return header, sections


def read_seed(path: Path) -> ParsedDocument:
    """Read a seed document from disk. Absence of the file is fail-hard.

    Reading is the driver's job, never a transform's — this is the boundary that keeps the
    compiled phase pure and its verdict reproducible.
    """
    if not path.is_file():
        raise FileNotFoundError(f"seed not found: {path}")

    raw = path.read_text(encoding="utf-8")
    header, sections = parse_text(raw)
    return ParsedDocument(header=header, sections=sections, raw=raw, path=str(path))
