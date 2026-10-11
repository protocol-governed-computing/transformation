"""Typed construction values (M5-1, M5-2), applied to Machine-block documents in place.

- `interface_fields.default` is a typed value. A text the oracle read as a number or a flag becomes
  that value: `'30'` is `30`, `'false'` is `false`. Other text stays text, `'[]'` among it, as the
  oracle rendered it; and `''` still declares no default.
- `interface_fields.type` names a type only. A format written after it, `string (date-time)`, moves
  to `format`.
- `implementation_bindings.module` goes. Construction derives it from the transform's identity.

Used by `convert.py`, which writes the mirror the comparison judges, and run on the testbed:

    python scripts/rebuild/typed_values.py FILE...
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REGISTER = re.compile(r"^  ([a-z][a-z0-9_]*):")
DEFAULT = re.compile(r"^(?P<lead>\s+(?:- )?)default: (?P<value>'[^']*')\s*$")
TYPE = re.compile(r"^(?P<lead>\s+(?:- )?)type: (?P<type>\w+) \((?P<format>[\w-]+)\)\s*$")
MODULE = re.compile(r"^\s+(?:- )?module: .*$")


def _typed(text: str):
    value = yaml.safe_load(text)
    held = yaml.safe_load(value) if isinstance(value, str) and value else value
    return held if isinstance(held, (bool, int)) else None


def migrate(text: str) -> str:
    out, register = [], None
    for line in text.splitlines(keepends=True):
        found = REGISTER.match(line)
        if found:
            register = found.group(1)
        if register == "interface_fields":
            default = DEFAULT.match(line)
            if default and _typed(default.group("value")) is not None:
                typed = yaml.safe_dump(_typed(default.group("value")), default_flow_style=True).strip()
                typed = typed.removesuffix("\n...").removesuffix("...").strip()
                line = f"{default.group('lead')}default: {typed}\n"
            typed_type = TYPE.match(line)
            if typed_type:
                indent = " " * len(typed_type.group("lead"))
                line = (f"{typed_type.group('lead')}type: {typed_type.group('type')}\n"
                        f"{indent}format: {typed_type.group('format')}\n")
        if register == "implementation_bindings" and MODULE.match(line):
            if line.lstrip().startswith("- "):
                raise ValueError("a row that opens with its module cannot lose it line by line")
            continue
        out.append(line)
    return "".join(out)


if __name__ == "__main__":
    for name in sys.argv[1:]:
        path = Path(name)
        path.write_text(migrate(path.read_text(encoding="utf-8")), encoding="utf-8")
