"""The P1 register template — the shape of `p1_change_request_<domain>_<subdomain>_v0.md`.

P1 consumes an accepted seed and produces the Change Request register. Structurally it mirrors the
seed's fifteen registers, with one addition that is the whole point of the phase:

    every row carries a **Source Finding**

That column is what P1 contributes. The seed asserts business content; P1 restates it as governed
rows that each cite where in the seed they came from. A row with no source is content P1 invented,
which is exactly what the phase must not do — and unlike P0's discipline, this one is checkable.

Two registers change shape rather than just gaining a column. `CR Type` and `Requested Outcomes`
are prose in a seed and tables here, because by P1 the classification is a decision with a
rationale rather than a paragraph a human wrote.
"""

from __future__ import annotations

from transformation.phases.p0.template import (
    ARTIFACT_KIND_PREFIXES,
    CERTAINTY,
    CR_TYPES,
    HEADER_FIELDS,
    SCOPE_RELATIONSHIPS,
    Section,
)

# Every row of every table register must cite the seed it came from. The format is checked, not
# just the presence: an unparseable citation is not traceability.
SOURCE_FINDING_PATTERN = r"^(CR seed §\d+|CR seed Subdomain Purpose|human decision)"

SECTIONS: tuple[Section, ...] = (
    Section(
        key="cr_type",
        number=1,
        title="CR Type",
        table_columns=("Classification", "Rationale", "Source Finding"),
    ),
    Section(
        key="business_vocabulary",
        number=2,
        title="Business Vocabulary",
        table_columns=("Term", "Definition", "Source Finding"),
    ),
    Section(
        key="requested_outcomes",
        number=3,
        title="Requested Outcomes",
        table_columns=("Outcome", "Source Finding"),
    ),
    Section(
        key="known_facts",
        number=4,
        title="Known Facts",
        table_columns=("Fact", "Certainty", "Source Finding"),
    ),
    Section(
        key="system_beliefs",
        number=5,
        title="Existing-System Beliefs",
        table_columns=("Belief", "Why It Matters", "Verification Goal", "Source Finding"),
    ),
    Section(
        key="assumptions",
        number=6,
        title="Assumptions",
        table_columns=("Assumption", "Basis", "Source Finding"),
        may_be_empty=True,
    ),
    Section(
        key="constraints",
        number=7,
        title="Constraints",
        table_columns=("Constraint", "Source", "Source Finding"),
        may_be_empty=True,
    ),
    Section(
        key="business_invariants",
        number=8,
        title="Business Invariants",
        table_columns=("Invariant", "Source Finding"),
    ),
    Section(
        key="lifecycle_states",
        number=9,
        title="Lifecycle States",
        table_columns=("Object", "State", "Meaning", "Source Finding"),
    ),
    Section(
        key="business_events",
        number=10,
        title="Business Events",
        table_columns=("Event", "When It Occurs", "Significance", "Source Finding"),
    ),
    Section(
        key="authority_boundaries",
        number=11,
        title="Authority Boundaries",
        table_columns=("Business Object", "Authoritative Owner", "Source Finding"),
    ),
    Section(
        key="out_of_scope",
        number=12,
        title="Out of Scope",
        table_columns=("Item", "Reason", "Source Finding"),
    ),
    Section(
        key="governance_scope",
        number=13,
        title="Governance Scope",
        table_columns=("Scope Item", "Relationship", "Source Finding"),
    ),
    Section(
        key="clarification_requests",
        number=14,
        title="Clarification Requests",
        prose=True,
        may_be_empty=True,
    ),
    Section(
        key="acceptance_criteria",
        number=15,
        title="Acceptance Criteria",
        table_columns=("Criterion", "Source Finding"),
    ),
)

SECTIONS_BY_KEY: dict[str, Section] = {s.key: s for s in SECTIONS}


def section(key: str) -> Section:
    """Look up a declared section, or fail hard. There is no default."""
    if key not in SECTIONS_BY_KEY:
        raise KeyError(f"no such P1 register: {key!r}")
    return SECTIONS_BY_KEY[key]
