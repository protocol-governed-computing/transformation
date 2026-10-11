"""Convert a phase document from tables to a Machine block, with the oracle's own reader.

The oracle reads the Markdown, and what it returns is written out as data. The conversion is
mechanical: no value is edited, so a difference in findings between the two forms is a difference in
reading, never in content. It runs against the oracle, not the rebuild, because the rebuild no longer
reads tables:

    PYTHONPATH=~/pgc-oracle/transformation python scripts/rebuild/convert.py SRC DST [SRC DST ...]

What moves into the Machine block:
- the header fields the oracle reads from the preamble;
- every register, a table as its columns and rows, a text-only register as its text.

What stays prose: headings, narrative, and any table no register marker opens. Each register's
marker and table, and each header line, leave the prose.

Deleted at the swap, with the table reader it runs.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

import transformation
from transformation.design import read as oracle_read

if "pgc-oracle" not in str(Path(transformation.__file__).resolve()):
    raise SystemExit(f"convert.py must run against the oracle; imported {transformation.__file__}")


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper: yaml.SafeDumper, value: str) -> yaml.Node:
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _str)


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
    block: dict = {"header": dict(header), "registers": {}}
    for entry in registers:
        if entry["columns"]:
            block["registers"][entry["id"]] = {
                "columns": list(entry["columns"]),
                "rows": [dict(row) for row in entry["rows"]],
            }
        else:
            block["registers"][entry["id"]] = entry["text"]

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
    return "\n".join(collapsed).rstrip("\n") + "\n"


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
