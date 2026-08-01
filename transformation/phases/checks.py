"""Check kinds — the implementation half of the P0 oracle.

A check kind is a *mechanism*: "is this cell's value in a vocabulary", "is this column absent",
"does this token appear anywhere". It knows how to inspect a seed document and nothing about which
register it is inspecting or why that matters. Those are declared in `rules.py`.

This mirrors the platform's own split: a workflow graph declares nodes and bindings and names a
capability by FQDN; the capability implements a mechanism and holds no policy. Adding a governance
rule must not require a new mechanism, and a new mechanism must not carry a rule's intent.

The registry is closed. An unknown check kind is fail-hard, never a skipped rule — a silently
skipped rule is the vacuity failure this codebase has hit repeatedly.
"""

from __future__ import annotations

import re
from typing import Callable

from transformation.phases.evaluate import Block, ParsedDocument

CheckFn = Callable[[ParsedDocument, "object"], list[tuple[str, str]]]

_REGISTRY: dict[str, CheckFn] = {}


def check(kind: str) -> Callable[[CheckFn], CheckFn]:
    def register(fn: CheckFn) -> CheckFn:
        if kind in _REGISTRY:
            raise KeyError(f"duplicate check kind: {kind}")
        _REGISTRY[kind] = fn
        return fn

    return register


def dispatch(kind: str) -> CheckFn:
    """Resolve a check kind, or fail hard."""
    if kind not in _REGISTRY:
        raise KeyError(
            f"unknown check kind {kind!r}; declared kinds are {sorted(_REGISTRY)}"
        )
    return _REGISTRY[kind]


def kinds() -> list[str]:
    return sorted(_REGISTRY)


# Helpers ----------------------------------------------------------------------------------


def _block(doc: ParsedDocument, rule) -> Block | None:
    return doc.find(rule.section_title) if rule.section_title else None


def _cell(row: dict[str, str], prefix: str) -> str:
    for key, value in row.items():
        if key.startswith(prefix):
            return value.strip()
    return ""


def _rows(doc: ParsedDocument, rule):
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    return list(enumerate(block.table.rows, start=1))


# Check kinds ------------------------------------------------------------------------------


@check("HEADER_FIELD_PRESENT")
def _header_field_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    for name in rule.params["fields"]:
        if not doc.header.get(name, "").strip():
            out.append(("header", f"required field {name!r} absent"))
    return out


@check("HEADER_FIELD_MATCHES")
def _header_field_matches(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    pattern = re.compile(rule.params["pattern"])
    for name in rule.params["fields"]:
        value = doc.header.get(name, "").strip()
        if value and not pattern.match(value):
            out.append(("header", f"{name} {value!r} does not match {rule.params['pattern']}"))
    return out


@check("SECTION_PRESENT")
def _section_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    if _block(doc, rule) is None:
        return [(rule.section_title, "required section absent from the seed")]
    return []


@check("SECTION_NUMBERED")
def _section_numbered(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    expected = rule.params["number"]
    if block.number != expected:
        return [(rule.section_title, f"expected section {expected}, found {block.number}")]
    return []


@check("SECTIONS_ASCENDING")
def _sections_ascending(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    numbers = [b.number for b in doc.blocks if b.number is not None]
    if numbers != sorted(numbers):
        return [("document", "numbered sections are not in ascending order")]
    return []


@check("SECTION_HAS_TEXT")
def _section_has_text(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    if not block.text():
        return [(rule.section_title, rule.params["detail"])]
    return []


@check("SECTION_DECLARES_ONE_OF")
def _section_declares_one_of(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    vocabulary = rule.params["vocabulary"]
    found = [t for t in vocabulary if re.search(rf"\b{re.escape(t)}\b", block.text())]
    if not found:
        return [(rule.section_title, f"nothing declared; expected one of {list(vocabulary)}")]
    if len(found) > 1:
        return [(rule.section_title, f"multiple values named: {found}")]
    return []


@check("TABLE_PRESENT")
def _table_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    if block.table is None:
        return [(rule.section_title, "section requires a table, none found")]
    return []


@check("TABLE_HAS_COLUMNS")
def _table_has_columns(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    out = []
    for expected in rule.params["columns"]:
        if not any(col.startswith(expected) for col in block.table.columns):
            out.append(
                (
                    rule.section_title,
                    f"required column {expected!r} absent; found {block.table.columns}",
                )
            )
    return out


@check("TABLE_HAS_ROWS")
def _table_has_rows(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    if not block.table.rows:
        return [(rule.section_title, "section requires at least one row")]
    return []


@check("COLUMN_ABSENT")
def _column_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    forbidden = rule.params["column"]
    if any(col.startswith(forbidden) for col in block.table.columns):
        return [(rule.section_title, rule.params["detail"])]
    return []


@check("CELL_IN_VOCABULARY")
def _cell_in_vocabulary(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    vocabulary = rule.params["vocabulary"]
    for i, row in _rows(doc, rule):
        value = _cell(row, column).upper()
        if value not in vocabulary:
            out.append(
                (
                    f"{rule.section_title} row {i}",
                    f"{value!r} is not one of {list(vocabulary)}",
                )
            )
    return out


@check("CELL_NOT_EMPTY")
def _cell_not_empty(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    for i, row in _rows(doc, rule):
        if not _cell(row, column):
            out.append((f"{rule.section_title} row {i}", rule.params["detail"]))
    return out


@check("CELL_NOT_PREFIXED")
def _cell_not_prefixed(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    for i, row in _rows(doc, rule):
        value = _cell(row, column).lower()
        for prefix in rule.params["prefixes"]:
            if value.startswith(prefix):
                out.append(
                    (
                        f"{rule.section_title} row {i}",
                        rule.params["detail"].format(prefix=prefix.strip()),
                    )
                )
                break
    return out


@check("TOKEN_ABSENT")
def _token_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    pattern = re.compile(rule.params["pattern"])
    return [
        ("document", rule.params["detail"].format(token=token))
        for token in sorted(set(pattern.findall(doc.raw)))
    ]


@check("CELL_MATCHES")
def _cell_matches(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every non-empty cell in a column must match a declared pattern.

    Emptiness is CELL_NOT_EMPTY's concern — a rule that checked both would report two findings for
    one defect and make the cause ambiguous.
    """
    out = []
    column = rule.params["column"]
    pattern = re.compile(rule.params["pattern"])
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        if value and not pattern.match(value):
            out.append((f"{rule.section_title} row {i}", rule.params["detail"].format(value=value)))
    return out
