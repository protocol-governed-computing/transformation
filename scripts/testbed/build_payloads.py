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
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, source in PAYLOADS.items():
        src = REPO / source
        if not src.is_file():
            raise FileNotFoundError(f"payload source missing: {src}")
        payload = {"seed_text": src.read_text(encoding="utf-8"), "author_of_record": AUTHOR}
        (OUT / name).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"  {name:<40} <- {source}")
    print(f"\n{len(PAYLOADS)} payload(s) written to {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
