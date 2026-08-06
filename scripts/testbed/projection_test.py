"""The P1 projection — reproducible, general, and refusing an inadmissible prior.

A projection is only worth trusting if it is the same document every time it runs. The dossier on
disk is therefore an assertion: re-project the seed, and what comes out must be byte-identical to
what is committed. A projection nobody re-runs drifts from its input exactly the way a hand-authored
fixture drifts from its dossier.

Generality is asserted against a seed the projection was not written for. CR-1's seed is a different
CR, of a different type, with registers of different sizes; its projection must be admissible over
P1's full rule set with the seed supplied as its prior, or the projection only works on the document
it was built from.

Run:  python scripts/testbed/projection_test.py
Exit: 0 if every case matched, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORKSPACE = REPO.parent
sys.path.insert(0, str(REPO))

from transformation.design.oracle import evaluate  # noqa: E402
from transformation.design.p0_change_seed import rules as p0_rules  # noqa: E402
from transformation.design.p1_change_request import rules as p1_rules  # noqa: E402
from transformation.design.project import PROJECTIONS  # noqa: E402
from transformation.design.read import parse_text, read_seed  # noqa: E402

DOSSIERS = WORKSPACE / "business_domains/book_library_mgmt/cr_dossiers"
CR_01 = DOSSIERS / "cr_01_catalog"
CR_02 = DOSSIERS / "cr_02_catalog"
CORPUS = REPO / "scripts/testbed/corpus"


def _priors(seed_path: Path) -> dict:
    prior = read_seed(seed_path)
    return {"p0": {"header": prior.header, "sections": prior.sections,
                   "registers": prior.registers}}


def _projected(seed_path: Path):
    """The projected document, read back as the oracle reads one."""
    _, projection = PROJECTIONS["p1"]
    text = projection(read_seed(seed_path))
    header, sections, registers = parse_text(text)
    doc = read_seed(seed_path)
    doc.header, doc.sections, doc.registers, doc.raw = header, sections, registers, text
    doc.__post_init__()
    doc.priors = _priors(seed_path)
    return text, doc


def main() -> int:
    problems: list[str] = []

    # Reproducible: the committed P1 is what the projection emits, byte for byte.
    text, doc = _projected(CR_02 / "p0_seed_book_library_mgmt_catalog_v0.md")
    committed = (CR_02 / "p1_change_request_book_library_mgmt_catalog_v0.md").read_text(
        encoding="utf-8"
    )
    if text == committed:
        print("  PASS  cr_02  projection reproduces the committed P1")
    else:
        problems.append("cr_02 projection differs from the committed P1")
        print("  FAIL  cr_02  projection differs from the committed P1")

    verdict = evaluate(doc, p1_rules.rule_set())
    status = "PASS" if verdict.admissible else "FAIL"
    print(f"  {status}  cr_02  projected P1 {verdict.verdict} "
          f"over {verdict.rules_evaluated} rules")
    if not verdict.admissible:
        problems.append(f"cr_02 projected P1 {verdict.verdict}")
        for finding in verdict.findings:
            print(f"          {finding}")

    # General: a seed the projection was not written for, of a different CR type.
    _, other = _projected(CR_01 / "p0_seed_book_library_mgmt_catalog_v0.md")
    verdict = evaluate(other, p1_rules.rule_set())
    status = "PASS" if verdict.admissible else "FAIL"
    print(f"  {status}  cr_01  projected P1 {verdict.verdict} "
          f"over {verdict.rules_evaluated} rules")
    if not verdict.admissible:
        problems.append(f"cr_01 projected P1 {verdict.verdict}")
        for finding in verdict.findings:
            print(f"          {finding}")

    # Refused: a prior that still carries an open blocking clarification is not projectable, and the
    # CLI is what enforces it — this asserts the verdict the CLI acts on.
    blocked = read_seed(CORPUS / "inadmissible_p0_blocking_clarification.md")
    verdict = evaluate(blocked, p0_rules.rule_set())
    fired = {f.rule for f in verdict.findings}
    if not verdict.admissible and "BLOCKING_CLARIFICATION_OUTSTANDING" in fired:
        print("  PASS  corpus blocking-clarification seed refused before projection")
    else:
        problems.append("a seed with an open blocking clarification was not refused")
        print("  FAIL  corpus blocking-clarification seed was not refused")

    if problems:
        print(f"\nPROJECTION FAILED — {len(problems)} problem(s)")
        return 1
    print("\nPROJECTION PASSED — reproducible, general, and refusing an inadmissible prior")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
