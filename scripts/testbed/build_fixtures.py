"""Regenerate the inadmissible P7/P8 corpus fixtures from CR-1's dossier.

A fixture is an admissible document with a named defect introduced. Hand-authoring one freezes a
copy of the dossier at the moment it was cut, and the copy rots: amending P7 left every P7 fixture
missing four registers, and the P8 order fixture had been written in a `catalog::` namespace the
dossier stopped using long before.

So a fixture is declared as *the defect*, not as a file. The document is the current dossier, and
the transformation states what is wrong with it — which is also the only readable form, because a
reader wants to know what a fixture proves, not to diff two hundred lines to find out.

Run:  python scripts/testbed/build_fixtures.py
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
CR_01 = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"
CORPUS = REPO / "scripts/testbed"

P7 = CR_01 / "p7_design_intent_book_library_mgmt_catalog_v0.md"
P8 = CR_01 / "p8_authoring_mandate_book_library_mgmt_catalog_v0.md"


def drop(text: str, prefix: str, count: int = 1) -> str:
    """Remove the first `count` lines beginning with `prefix`."""
    out, removed = [], 0
    for line in text.splitlines():
        if removed < count and line.startswith(prefix):
            removed += 1
            continue
        out.append(line)
    if removed != count:
        raise SystemExit(f"expected {count} line(s) starting {prefix!r}, removed {removed}")
    return "\n".join(out) + "\n"


def replace(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"expected exactly one {old!r}, found {text.count(old)}")
    return text.replace(old, new)


def after(text: str, prefix: str, addition: str) -> str:
    line = [l for l in text.splitlines() if l.startswith(prefix)]
    if len(line) != 1:
        raise SystemExit(f"expected exactly one line starting {prefix!r}, found {len(line)}")
    return text.replace(line[0], line[0] + "\n" + addition)


NS = "book_library_mgmt::"


def p7_collision(t: str) -> str:
    """A code with no namespace, a node that resolves to nothing, and a store nobody can locate."""
    t = replace(t, f"| Select the current records matching the staff terms | CC | {NS}CC_SEARCH_CATALOG_V0 |",
                "| Select the current records matching the staff terms | CC | CC_SEARCH_UNQUALIFIED_V0 |")
    t = replace(t, f"| {NS}WF_REGISTER_BOOK_V0 | {NS}CC_REGISTER_BIBLIOGRAPHIC_WORK_V0 | CC |",
                f"| {NS}WF_REGISTER_BOOK_V0 | {NS}CC_REGISTER_BIBLIOGRAPHC_WORK_V0 | CC |")
    t = replace(t, "| BIBLIOGRAPHIC_WORKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/bibliographic_works.json |",
                "| BIBLIOGRAPHIC_WORKS | CS_MUTABLE_JSON_V0 |  |")
    return t


def p7_unbound_code(t: str) -> str:
    """A provisional code P5 declared that this design never binds."""
    return drop(t, f"| The authorized staff member performing an operation | AC | {NS}AC_LIBRARY_STAFF_V0 |")


def p7_dropped_reuse(t: str) -> str:
    """A dependency P6 declared satisfied by an existing artifact, never inventoried."""
    return drop(t, "| capability_side_effects::CS_APPENDONLY_JSONL_V0 |")


def p8_broken_order(t: str) -> str:
    """A dropped step, a prerequisite scheduled late, and a critical path through neither."""
    t = drop(t, f"| 2 | 7 | {NS}CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 |")
    t = replace(t, f"| 1 | 1 | {NS}STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | — |",
                f"| 1 | 1 | {NS}STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | {NS}RB_CATALOG_BINDINGS_V0 |")
    return t


def p8_undesigned_artifact(t: str) -> str:
    """A row the mandate invented, which no phase ever designed."""
    t = after(t, f"| 5 | 25 | {NS}VOCAB_CATALOG_STATES_V0 |",
              f"| 5 | 26 | {NS}CC_ARCHIVE_CATALOG_RECORD_V0 | NEW | catalog | — |")
    return after(t, f"| {NS}VOCAB_CATALOG_STATES_V0 | catalog |",
                 f"| {NS}CC_ARCHIVE_CATALOG_RECORD_V0 | catalog |")


def p8_dropped_artifact(t: str) -> str:
    """An artifact P7 declared that the mandate schedules nowhere.

    Removed from the field declarations too: a mandate that dropped a step would not go on
    declaring where the dropped artifact lives, and leaving the declaration would let the placement
    rule fire instead of the reconciliation one.
    """
    t = drop(t, f"| 5 | 25 | {NS}VOCAB_CATALOG_STATES_V0 |")
    return drop(t, f"| {NS}VOCAB_CATALOG_STATES_V0 | catalog |")


FIXTURES = [
    ("corpus_p7/inadmissible_p7_collision.md", P7, p7_collision),
    ("corpus_p7/inadmissible_p7_unbound_code.md", P7, p7_unbound_code),
    ("corpus_p7/inadmissible_p7_dropped_reuse.md", P7, p7_dropped_reuse),
    ("corpus_p8/inadmissible_p8_broken_order.md", P8, p8_broken_order),
    ("corpus_p8/inadmissible_p8_undesigned_artifact.md", P8, p8_undesigned_artifact),
    ("corpus_p8/inadmissible_p8_dropped_artifact.md", P8, p8_dropped_artifact),
]


def main() -> int:
    for name, source, transform in FIXTURES:
        (CORPUS / name).write_text(transform(source.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"  {name:<52} <- {source.name}  [{transform.__name__}]")
    print(f"\n{len(FIXTURES)} fixture(s) derived from the dossier")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
