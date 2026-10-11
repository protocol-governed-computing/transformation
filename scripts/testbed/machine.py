"""Write a phase document for a probe: a title, and its registers in a Machine block.

The design tests build small documents to trip one rule and leave the rest silent. They state
registers as columns and rows, and this writes them in the form the reader reads. An empty register
carries the emptiness sentinel as its one row, as an authored document does.
"""
from __future__ import annotations

from typing import Iterable

import yaml

SENTINEL = "NONE IDENTIFIED"


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(
    str, lambda d, v: d.represent_scalar("tag:yaml.org,2002:str", v, style="|" if "\n" in v else None))


def register(register_id: str, columns: list[str], rows: Iterable[tuple],
             sentinel: bool = True) -> tuple[str, dict]:
    """One register: its columns, and each row as a mapping from column to text. An empty register
    carries the sentinel row unless `sentinel` is false, which leaves a register with columns and no
    rows."""
    body = []
    for row in rows:
        cells = [str(c) for c in row] + [""] * (len(columns) - len(row))
        body.append(dict(zip(columns, cells[: len(columns)])))
    if not body and sentinel:
        body = [dict(zip(columns, [SENTINEL] + [""] * (len(columns) - 1)))]
    return register_id, {"columns": list(columns), "rows": body}


def document(title: str, *registers: tuple[str, dict], header: dict[str, str] | None = None,
             prose: str = "") -> str:
    """The document text: title, Machine block, then any prose."""
    block: dict = {}
    if header:
        block["header"] = dict(header)
    block["registers"] = dict(registers)
    machine = yaml.dump(block, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100000)
    return f"# {title}\n\n## Machine\n\n```yaml\n{machine}```\n" + (f"\n{prose}\n" if prose else "")
