"""The document header (M4-1): the oracle's bold header lines, restated as `document`.

    header:                              document:
      Stage: 3 — Analysis Loop             phase: p3
      CR: cr_01_catalog          ──►       domain: book_library_mgmt
      Status: DRAFT                        subdomain: catalog
      Feeds: Stage 4 — Business Model      cr: cr_01_catalog
                                           rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0

`Status` goes: a document's standing is its verdict. `Feeds` goes: the dispatch states the order.
Domain and subdomain are read from the title, `…: <domain> / <subdomain>` or `… — <domain> /
<subdomain>`. A title naming two subdomains, `identity and wallet`, gives a list. A field the oracle
document lacks stays absent, so a document refused for a missing field is still refused.

Shared by `convert.py`, which writes the mirror the comparison judges, and this script,
which migrates the testbed in place.

    python scripts/rebuild/header.py FILE...     migrate documents in place
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

TITLE = re.compile(r"(?:: |— )(?P<domain>[a-z_]+) / (?P<subdomain>[a-z_]+(?: and [a-z_ ]+?)?)\s*(?:\(|$)")
STAGE = re.compile(r"^\s*(?P<n>[0-8])\b")
RULE_SET = "transformation.schemas.REGISTER_SCHEMA_P{n}_V0"


def document(header: dict, title: str) -> dict:
    """The `document` mapping for an oracle header and the document's title line."""
    out: dict = {}
    stage = STAGE.match(str(header.get("Stage") or ""))
    if stage:
        out["phase"] = f"p{stage.group('n')}"
    found = TITLE.search(title)
    if found:
        out["domain"] = found.group("domain")
        subdomains = [s.strip() for s in found.group("subdomain").split(" and ")]
        out["subdomain"] = subdomains[0] if len(subdomains) == 1 else subdomains
    if str(header.get("CR") or "").strip():
        out["cr"] = str(header["CR"]).strip()
    if stage:
        out["rule_set"] = RULE_SET.format(n=stage.group("n"))
    return out


def dump(doc: dict) -> str:
    return yaml.safe_dump({"document": doc}, sort_keys=False, allow_unicode=True, width=100)


def migrate(text: str) -> str:
    """A Machine-block document with its `header:` restated as `document:`."""
    lines = text.splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if line == "header:\n")
    end = next(i for i in range(start + 1, len(lines)) if not lines[i].startswith((" ", "\t")))
    header = yaml.safe_load("".join(lines[start:end]))["header"] or {}
    return "".join(lines[:start]) + dump(document(header, lines[0])) + "".join(lines[end:])


if __name__ == "__main__":
    for name in sys.argv[1:]:
        path = Path(name)
        path.write_text(migrate(path.read_text(encoding="utf-8")), encoding="utf-8")
