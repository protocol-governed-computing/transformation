"""The P2 rule set — what makes a Domain Model register admissible.

P2 is the first phase whose rules cannot be satisfied by writing carefully. Structural discipline
and traceability are checkable against the document alone; **grounding is not**. A belief marked
`VERIFIED` is a claim about the assembled composition, and the only way to check it is to look.

So P2's distinctive rules split in two:

- *Completeness* — every belief has a result, every result is in the vocabulary, every `VERIFIED`
  row cites what was found. Checkable from the document.
- *Grounding* — every artifact identity cited actually exists in the observed composition.
  Checkable only against an observation, supplied through the governed inspection capability.

The second is what makes the phase's evidence non-forgeable, and it is the reason P2 needs a
capability at all rather than another pure transform.
"""

from __future__ import annotations

from transformation.phases.p0.template import HEADER_FIELDS
from transformation.phases.p1.template import SOURCE_FINDING_PATTERN
from transformation.phases.p2.template import (
    ARTIFACT_REFERENCE_PATTERN,
    BELIEF_RESULTS,
    EVIDENCE_STATUS,
    OBSERVATION_OPERATION,
    SECTIONS,
    section,
)
from transformation.phases.rules import Rule, structural_rules


def _traceability_rules() -> list[Rule]:
    """Registers that restate earlier findings must still cite them.

    The Baseline register is exempt: its rows are what P2 *observed*, not what an earlier phase
    said, so citing a seed finding for them would be a fabricated provenance.
    """
    out: list[Rule] = []
    for spec in SECTIONS:
        if "Source Finding" not in spec.table_columns:
            continue
        out.append(
            Rule(
                id="ROW_WITHOUT_SOURCE_FINDING",
                check="CELL_NOT_EMPTY",
                section_title=spec.title,
                params={
                    "column": "Source Finding",
                    "detail": "row cites no earlier finding — P2 grounds the change request, it does not restart it",
                },
                intent="an uncited row has no provenance in the dossier",
            )
        )
        out.append(
            Rule(
                id="SOURCE_FINDING_MALFORMED",
                check="CELL_MATCHES",
                section_title=spec.title,
                params={
                    "column": "Source Finding",
                    "pattern": SOURCE_FINDING_PATTERN,
                    "detail": (
                        "{value!r} does not name a seed register — cite 'CR seed §N …', "
                        "'CR seed Subdomain Purpose', or 'human decision'"
                    ),
                },
                intent="an unparseable citation is not traceability",
            )
        )
    return out


SEMANTIC_RULES: list[Rule] = [
    Rule(
        id="HEADER_FIELD_MISSING",
        check="HEADER_FIELD_PRESENT",
        params={"fields": list(HEADER_FIELDS)},
        intent="the register must say which domain and subdomain it changes",
    ),
    Rule(
        id="HEADER_MALFORMED",
        check="HEADER_FIELD_MATCHES",
        params={
            "fields": ["Domain", "Primary subdomain"],
            "pattern": r"^[a-z][a-z0-9_]*",
        },
        intent="domain and subdomain are identifiers, not prose",
    ),
    Rule(
        id="BELIEF_WITHOUT_RESULT",
        check="CELL_NOT_EMPTY",
        section_title=section("belief_verification").title,
        params={
            "column": "Result",
            "detail": "belief has no result — P2 is complete only when every belief is answered",
        },
        intent="an unanswered belief is the phase's stop condition, not an omission",
    ),
    Rule(
        id="BELIEF_RESULT_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("belief_verification").title,
        params={"column": "Result", "vocabulary": list(BELIEF_RESULTS)},
        intent="NOT_FOUND is a final answer; an invented result hides what was actually found",
    ),
    Rule(
        id="BELIEF_WITHOUT_EVIDENCE",
        check="CELL_NOT_EMPTY",
        section_title=section("belief_verification").title,
        params={
            "column": "Evidence",
            "detail": "belief has a result but records nothing about how it was reached",
        },
        intent="a result without evidence is an assertion, not a verification",
    ),
    Rule(
        id="VERIFIED_BELIEF_WITHOUT_ARTIFACT",
        check="CITED_ARTIFACTS_EXIST",
        section_title=section("belief_verification").title,
        params={
            "column": "Evidence",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
            "only_when_column": "Result",
            "only_when_value": "VERIFIED",
            "detail_missing": (
                "belief is VERIFIED but names no artifact — evidence must say what was found"
            ),
            "detail_absent": (
                "cited artifact {fqdn!r} does not exist in the observed composition"
            ),
        },
        intent="grounding a belief means naming something that is actually there",
    ),
    Rule(
        id="ENTITY_EVIDENCE_STATUS_NOT_IN_VOCABULARY",
        check="CELL_IN_VOCABULARY",
        section_title=section("business_entities").title,
        params={"column": "Evidence Status", "vocabulary": list(EVIDENCE_STATUS)},
        intent="an entity is grounded, partly grounded, or absent — nothing else",
    ),
    Rule(
        id="BASELINE_ARTIFACT_NOT_OBSERVED",
        check="CITED_ARTIFACTS_EXIST",
        section_title=section("baseline").title,
        params={
            "column": "Artifact",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
            "detail_missing": "baseline row names no artifact identity",
            "detail_absent": (
                "baseline claims {fqdn!r} already exists, but it is not in the observed composition"
            ),
        },
        intent="the baseline is what was observed, so every row must be observable",
    ),
    Rule(
        id="OPEN_QUESTIONS_UNSTATED",
        check="SECTION_HAS_TEXT",
        section_title=section("open_questions").title,
        params={
            "detail": "state the questions P3 must resolve, or '(none)' — an empty section asserts nothing"
        },
        intent="silence is not the same as 'nothing left for P3'",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P2 rule set: structural, then traceability, then semantic."""
    return structural_rules(SECTIONS) + _traceability_rules() + SEMANTIC_RULES
