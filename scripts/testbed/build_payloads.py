"""Regenerate the committed P0 test payloads from their source documents.

A payload embeds a whole seed document as `seed_text`, so a hand-edited payload silently drifts
from the seed it was copied from. Generating them keeps one source of truth: edit the seed or the
corpus entry, run this, commit the result.

Run:  python scripts/testbed/build_payloads.py
"""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
OUT = REPO / "testbed" / "phases" / "test_payloads"

AUTHOR = "bachipeachy"

# A source is resolved against the repo unless it names a workspace root. CR-0 is this repo's own
# change request and its dossier lives here; a business CR's dossier lives with the domain it
# changes, which is a sibling repo. Both are payload sources, so the map carries the root.
ROOTS = {"business_domains": WORKSPACE}

PAYLOADS = {
    "01_admissible_seed.json": (
        "cr_dossiers/cr_00_new_subdomain/p0_seed_transformation_phases_v0.md"
    ),
    "02_admissible_reference.json": "scripts/testbed/corpus/admissible_blockchain_reference.md",
    "03_inadmissible_seven_violations.json": (
        "scripts/testbed/corpus/inadmissible_seven_violations.md"
    ),
    "04_inadmissible_structural.json": "scripts/testbed/corpus/inadmissible_structural.md",
    "05_inadmissible_truncated.json": "scripts/testbed/corpus/inadmissible_truncated.md",
    "06_p1_admissible_register.json": (
        "cr_dossiers/cr_00_new_subdomain/"
        "p1_change_request_transformation_phases_v0.md"
    ),
    "07_p1_inadmissible_register.json": "scripts/testbed/corpus_p1/inadmissible_p1_register.md",
    "08_p2_admissible_register.json": (
        "cr_dossiers/cr_00_new_subdomain/"
        "p2_domain_model_transformation_phases_v0.md"
    ),
    "09_p2_inadmissible_register.json": "scripts/testbed/corpus_p2/inadmissible_p2_register.md",
    # CR-1 — the first business subject. CR-0 is the pipeline authoring its own domain, so it
    # cannot exercise a phase against business content; these three carry the same phases over a
    # library catalog instead.
    "10_p0_admissible_catalog_seed.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p0_seed_book_library_mgmt_catalog_v0.md"
    ),
    "11_p1_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p1_change_request_book_library_mgmt_catalog_v0.md"
    ),
    "12_p2_admissible_catalog_register.json": (
        "business_domains/book_library_mgmt/cr_dossiers/cr_01_catalog/"
        "p2_domain_model_book_library_mgmt_catalog_v0.md"
    ),
    # The catalog register with three defects introduced. Without it the evidence that the rules
    # bite comes only from documents about the pipeline itself — a phase could pass every business
    # document by doing nothing and the suite would still be green.
    "13_p2_inadmissible_catalog_register.json": (
        "scripts/testbed/corpus_p2/inadmissible_p2_catalog_register.md"
    ),
}

# P0 offers a seed, P1 offers a register — the intent field differs, so the payload key does too.
PAYLOAD_KEY = {
    "06_p1_admissible_register.json": "register_text",
    "07_p1_inadmissible_register.json": "register_text",
    "08_p2_admissible_register.json": "register_text",
    "09_p2_inadmissible_register.json": "register_text",
    "11_p1_admissible_catalog_register.json": "register_text",
    "12_p2_admissible_catalog_register.json": "register_text",
    "13_p2_inadmissible_catalog_register.json": "register_text",
}


def root_for(source: str) -> Path:
    return ROOTS.get(source.split("/", 1)[0], REPO)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, source in PAYLOADS.items():
        src = root_for(source) / source
        if not src.is_file():
            raise FileNotFoundError(f"payload source missing: {src}")
        key = PAYLOAD_KEY.get(name, "seed_text")
        payload = {key: src.read_text(encoding="utf-8"), "author_of_record": AUTHOR}
        (OUT / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"  {name:<40} <- {source}")
    print(f"\n{len(PAYLOADS)} payload(s) written to {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
