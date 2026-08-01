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
OUT = REPO / "testbed" / "phases" / "test_payloads"

AUTHOR = "bachipeachy"

PAYLOADS = {
    "01_admissible_seed.json": (
        "examples/transformation/phases/cr_00_new_subdomain/p0_seed_transformation_phases_v0.md"
    ),
    "02_admissible_reference.json": "scripts/testbed/corpus/admissible_blockchain_reference.md",
    "03_inadmissible_seven_violations.json": (
        "scripts/testbed/corpus/inadmissible_seven_violations.md"
    ),
    "04_inadmissible_structural.json": "scripts/testbed/corpus/inadmissible_structural.md",
    "05_inadmissible_truncated.json": "scripts/testbed/corpus/inadmissible_truncated.md",
    "06_p1_admissible_register.json": (
        "examples/transformation/phases/cr_00_new_subdomain/"
        "p1_change_request_transformation_phases_v0.md"
    ),
    "07_p1_inadmissible_register.json": "scripts/testbed/corpus_p1/inadmissible_p1_register.md",
    "08_p2_admissible_register.json": (
        "examples/transformation/phases/cr_00_new_subdomain/"
        "p2_domain_model_transformation_phases_v0.md"
    ),
    "09_p2_inadmissible_register.json": "scripts/testbed/corpus_p2/inadmissible_p2_register.md",
}

# P0 offers a seed, P1 offers a register — the intent field differs, so the payload key does too.
PAYLOAD_KEY = {
    "06_p1_admissible_register.json": "register_text",
    "07_p1_inadmissible_register.json": "register_text",
    "08_p2_admissible_register.json": "register_text",
    "09_p2_inadmissible_register.json": "register_text",
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, source in PAYLOADS.items():
        src = REPO / source
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
