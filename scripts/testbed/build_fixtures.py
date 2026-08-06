"""Regenerate the inadmissible corpus fixtures from CR-1's dossier.

A fixture is an admissible document with a named defect introduced. Hand-authoring one freezes a
copy of the dossier at the moment it was cut, and the copy rots: amending P7 left every P7 fixture
missing four registers, and the P8 order fixture had been written in a `catalog::` namespace the
dossier stopped using long before.

So a fixture is declared as *the defect*, not as a file. The document is the current dossier, and
the transformation states what is wrong with it — which is also the only readable form, because a
reader wants to know what a fixture proves, not to diff two hundred lines to find out.

Every negative catalog fixture is derived this way. The five that were still hand-authored went stale
the moment the dossier was replaced: a P4 fixture judged against a new P3 reported twenty-six
unconsolidated decisions, and a P1 fixture judged against a new seed reported a hundred and forty-two
findings. A derived fixture cannot drift from the dossier it is cut from.

Run:  python scripts/testbed/build_fixtures.py
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
CR_01 = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog"
CORPUS = REPO / "scripts/testbed"

P1 = CR_01 / "p1_change_request_book_library_mgmt_catalog_v0.md"
P2 = CR_01 / "p2_domain_model_book_library_mgmt_catalog_v0.md"
P3 = CR_01 / "p3_analysis_loop_book_library_mgmt_catalog_v0.md"
P4 = CR_01 / "p4_business_model_book_library_mgmt_catalog_v0.md"
P6 = CR_01 / "p6_governance_intent_book_library_mgmt_catalog_v0.md"
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


def p1_dropped_criterion(t: str) -> str:
    """An acceptance criterion the seed declared and the change request drops."""
    return drop(t, "| Every catalog operation performed can be traced and audited afterwards. |")


def p2_grounding(t: str) -> str:
    """A misspelled identity, a right-code/wrong-namespace one, and design in a business cell."""
    t = replace(t, "capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Assembles a durable record",
                "capability_transforms::CT_PURE_ASEMBLE_RECORD_V0 | Assembles a durable record")
    t = replace(t, "| Record shape validation | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |",
                "| Record shape validation | ai_governance::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |")
    return replace(t, "| Nothing in the composition holds a book record or a copy record. |",
                   "| Nothing in the composition holds a book record, so CC_REGISTER_BOOK_V0 must be authored. |")


def p2_dropped_belief(t: str) -> str:
    """A Stage-1 belief the domain model never verifies."""
    return drop(t, "| No capability in the current composition manages a library catalog. | NOT_FOUND |")


def p3_ineligible_reuse(t: str) -> str:
    """Candidates offered to a business change request from domains that permit no reuse."""
    return replace(t, "| capability_side_effects::CS_REGISTRY_V0 satisfies it as-is. | S3 analysis_findings #2 |",
                   "| transformation::CT_PURE_PARSE_REGISTERS_V0 and workload::EV_CONJECTURE_EVALUATED_V0 "
                   "were offered as candidates. | S3 analysis_findings #2 |")


def p3_restated_result(t: str) -> str:
    """A re-verification that cites one belief and addresses another."""
    return replace(t, "| book_library_mgmt does not appear to be part of the current software baseline. | S2 belief_verification #1 |",
                   "| The catalog has no records of its own to verify. | S2 belief_verification #1 |")


def p4_consolidation(t: str) -> str:
    """A dangling gap reference, an unowned gap, a scope row pointing nowhere, a bad dependency."""
    t = replace(t, "| catalog | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call |",
                "| catalog | capability_side_effects::CS_MUTABLE_JSN_V0 | capability call |")
    t = replace(t, "| Retire a book record | S3 authoring_decisions Retire a book record | CRITICAL | GAP-09 |",
                "| Retire a book record | S3 authoring_decisions Retire a book record | CRITICAL | GAP-99 |")
    t = replace(t, "| GAP-01 | S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail | Record a performed catalog operation in the catalog's audit trail | catalog | NEW |",
                "| GAP-01 | S3 authoring_decisions Record a performed catalog operation in the catalog's audit trail | Record a performed catalog operation in the catalog's audit trail |  | NEW |")
    return replace(t, "| Search the catalog by subject or title, excluding retired books | GAP-13 |",
                   "| Search the catalog by subject or title, excluding retired books | GAP-98 |")


def p4_dropped_decision(t: str) -> str:
    """A capability P3 committed that the consolidation never carries."""
    return drop(t, "| Retrieve a book's complete details with the copies the library holds | S3 authoring_decisions")


def p6_placement(t: str) -> str:
    """A malformed dependency direction, and an in-scope capability placed under a code."""
    t = replace(t, "| Read whether a staff member is authorized to perform catalog operations | catalog → staff |",
                "| Read whether a staff member is authorized to perform catalog operations | staff and catalog both |")
    return replace(t, "| Search the catalog by subject or title | catalog | OWNED |",
                   "| CC_SEARCH_CATALOG_V0 | catalog | OWNED |")


def p6_unplaced_scope(t: str) -> str:
    """A capability P5 declared in scope that the placement phase never mentions."""
    return drop(t, "| Retire a physical copy | catalog | OWNED |")


def p7_collision(t: str) -> str:
    """A code with no namespace, a node that resolves to nothing, and a store nobody can locate."""
    t = replace(t, f"| Select the registered books matching a subject or title, excluding retired ones | CC | {NS}CC_SEARCH_CATALOG_V0 |",
                "| Select the registered books matching a subject or title, excluding retired ones | CC | CC_SEARCH_UNQUALIFIED_V0 |")
    t = replace(t, f"| {NS}WF_REGISTER_BOOK_V0 | {NS}CC_REGISTER_BOOK_V0 | CC |",
                f"| {NS}WF_REGISTER_BOOK_V0 | {NS}CC_REGISTR_BOOK_V0 | CC |")
    t = replace(t, "| BOOKS | CS_MUTABLE_JSON_V0 | book_library_mgmt/catalog/books.json |",
                "| BOOKS | CS_MUTABLE_JSON_V0 |  |")
    return t


def p7_unbound_code(t: str) -> str:
    """A provisional code P5 declared that this design never binds."""
    return drop(t, f"| The authorized staff member who performs a catalog operation | AC | {NS}AC_LIBRARY_STAFF_V0 |")


def p7_dropped_reuse(t: str) -> str:
    """A reused artifact dropped from the inventory, leaving a step bound to nothing.

    `SATISFIED_DEPENDENCY_NOT_INVENTORIED` cannot be proven against this dossier: it reads P6's
    `cross_subdomain_deps` Existing Artifact column, and this CR's only cross-subdomain dependency is
    the staff authorization GAP, which names no artifact by design. The rule is therefore uncovered —
    recorded rather than papered over with a fixture that does not exercise it.
    """
    return drop(t, "| capability_side_effects::CS_APPENDONLY_JSONL_V0 | REUSE |")


def p7_unrooted_source(t: str) -> str:
    """A cross-step source with its root dropped — the defect that reached execution.

    `results.assemble_book_record.book_record` names a prior step's output; `assemble_book_record.
    book_record` names nothing, and every layer below reads it as a literal string. The renderer
    emitted it verbatim, the compiler accepted it, and the runtime handed the store its own binding
    text as the book. Nothing refused it: construction completeness was 100%, because a binding
    determined to be a literal is still determined.
    """
    return replace(t, "results.assemble_book_record.book_record",
                   "assemble_book_record.book_record")


def p7_store_path_mismatch(t: str) -> str:
    """A registry store named for a format its capability does not write.

    `CS_REGISTRY_V0` writes JSON Lines; `.json` advertises a document that could never be parsed as
    one. It compiled, ran, and cost nothing until the first tool that tried to read the store.
    """
    return replace(t, "book_library_mgmt/catalog/book_identity_registry.jsonl",
                   "book_library_mgmt/catalog/book_identity_registry.json")


def build_step(text: str, code: str) -> str:
    """The build_order row scheduling `code`, found by what it schedules rather than by its number.

    Anchoring on a literal step number bound these fixtures to the mandate's current ordering, and
    every artifact inserted into an earlier wave renumbered everything after it — three separate
    breakages, each of them the anchor going stale rather than the fixture being wrong.
    """
    rows = [l for l in text.splitlines()
            if l.startswith("| ") and f"| {code} | " in l and l.split(" | ")[1].isdigit()]
    if len(rows) != 1:
        raise SystemExit(f"expected exactly one build_order row for {code}, found {len(rows)}")
    return rows[0]


def p8_broken_order(t: str) -> str:
    """A dropped step, a prerequisite scheduled late, and a critical path through neither."""
    t = drop(t, build_step(t, f"{NS}CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0"))
    t = replace(t, f"| 1 | 1 | {NS}STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | — |",
                f"| 1 | 1 | {NS}STRUCTURE_CATALOG_STORAGE_V0 | NEW | catalog | {NS}RB_CATALOG_BINDINGS_V0 |")
    return t


def p8_undesigned_artifact(t: str) -> str:
    """A row the mandate invented, which no phase ever designed."""
    anchor = build_step(t, f"{NS}RB_CATALOG_BINDINGS_V0")
    wave, step = anchor.split(" | ")[0].lstrip("| "), int(anchor.split(" | ")[1])
    t = after(t, anchor,
              f"| {wave} | {step + 1} | {NS}CC_ARCHIVE_CATALOG_RECORD_V0 | NEW | catalog | — |")
    return after(t, f"| {NS}RB_CATALOG_BINDINGS_V0 | catalog |",
                 f"| {NS}CC_ARCHIVE_CATALOG_RECORD_V0 | catalog |")


def p8_dropped_artifact(t: str) -> str:
    """An artifact P7 declared that the mandate schedules nowhere.

    The last step is the one to drop: removing any earlier one would break step contiguity as well,
    and two findings for one edit would make the reconciliation rule hard to see. Removed from the
    field declarations too, so the placement rule does not fire in the reconciliation rule's place.
    """
    t = drop(t, build_step(t, f"{NS}RB_CATALOG_BINDINGS_V0"))
    t = drop(t, f"| {NS}RB_CATALOG_BINDINGS_V0 | catalog |")
    # A mandate that dropped an artifact would not go on routing its critical path through it —
    # leaving the path row fires CRITICAL_PATH_NOT_IN_BUILD_ORDER instead of the reconciliation rule.
    return drop(t, f"| 4 | {NS}RB_CATALOG_BINDINGS_V0 |")


FIXTURES = [
    ("corpus_p1/inadmissible_p1_dropped_criterion.md", P1, p1_dropped_criterion),
    ("corpus_p2/inadmissible_p2_catalog_register.md", P2, p2_grounding),
    ("corpus_p2/inadmissible_p2_dropped_belief.md", P2, p2_dropped_belief),
    ("corpus_p3/inadmissible_p3_ineligible_reuse.md", P3, p3_ineligible_reuse),
    ("corpus_p3/inadmissible_p3_restated_result.md", P3, p3_restated_result),
    ("corpus_p4/inadmissible_p4_broken_consolidation.md", P4, p4_consolidation),
    ("corpus_p4/inadmissible_p4_dropped_decision.md", P4, p4_dropped_decision),
    ("corpus_p6/inadmissible_p6_unplaced.md", P6, p6_placement),
    ("corpus_p6/inadmissible_p6_unplaced_scope.md", P6, p6_unplaced_scope),
    ("corpus_p7/inadmissible_p7_collision.md", P7, p7_collision),
    ("corpus_p7/inadmissible_p7_unbound_code.md", P7, p7_unbound_code),
    ("corpus_p7/inadmissible_p7_dropped_reuse.md", P7, p7_dropped_reuse),
    ("corpus_p7/inadmissible_p7_unrooted_source.md", P7, p7_unrooted_source),
    ("corpus_p7/inadmissible_p7_store_path.md", P7, p7_store_path_mismatch),
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
