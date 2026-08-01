"""The P0 seed template — the fixed shape of `0_seed_business_problem_statement.md`.

The template is data, not prose. Every rule the oracle enforces is declared here, so adding a
section or a controlled vocabulary is an edit to this file and nowhere else.

Section structure is fixed by RI-0's elicitation document
(`1_input_elicitation_<domain>_<subdomain>_v0.md`), which is the reference instance of this shape.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Controlled vocabularies -----------------------------------------------------------------

# Release 4 reaches the first four. MERGE_SUBDOMAIN / SPLIT_SUBDOMAIN are deliberate future
# extensions: adding one must remain a vocabulary edit, never a redesign.
CR_TYPES = ("NEW_SUBDOMAIN", "EXTEND_SUBDOMAIN", "MODIFY", "DEPRECATE")

CERTAINTY = ("HIGH", "MEDIUM", "LOW")

SCOPE_RELATIONSHIPS = ("CREATED", "EXTENDED", "MODIFIED", "DEPRECATED", "ADJACENT")

# Header fields, in the order they must appear.
HEADER_FIELDS = ("Domain", "Primary subdomain", "Secondary subdomain", "CR version")

# Design leakage ---------------------------------------------------------------------------

# P0 rewrites business prose. It must not invent design, so a compiled-artifact identifier has no
# business appearing in a seed. These prefixes are the artifact kinds the compiler governs; any
# token of the form <PREFIX>_SOMETHING_V<n> is design, not business language.
ARTIFACT_KIND_PREFIXES = (
    "AC", "CC", "CS", "CT", "EV", "IN", "PR", "RB", "SD", "ST", "TI", "TE", "WF",
)


@dataclass(frozen=True)
class Section:
    """One required section of the seed.

    `number` is None for the unnumbered preamble section. `table_columns` declares the exact
    column headers a table section must carry; a section with no table_columns is prose.
    """

    key: str
    number: int | None
    title: str
    table_columns: tuple[str, ...] = ()
    may_be_empty: bool = False
    prose: bool = False


SECTIONS: tuple[Section, ...] = (
    Section(
        key="subdomain_purpose",
        number=None,
        title="Subdomain Purpose",
        prose=True,
    ),
    Section(
        key="cr_type",
        number=1,
        title="CR Type",
        prose=True,
    ),
    Section(
        key="business_vocabulary",
        number=2,
        title="Business Vocabulary",
        table_columns=("Term", "Definition"),
    ),
    Section(
        key="requested_outcomes",
        number=3,
        title="Requested Outcomes",
        prose=True,
    ),
    Section(
        key="known_facts",
        number=4,
        title="Known Facts",
        table_columns=("#", "Fact", "Certainty"),
    ),
    Section(
        key="system_beliefs",
        number=5,
        title="Existing-System Beliefs",
        table_columns=("#", "Belief", "Why it matters", "Verification Goal"),
    ),
    Section(
        key="assumptions",
        number=6,
        title="Assumptions",
        table_columns=("Assumption", "Basis"),
        may_be_empty=True,
    ),
    Section(
        key="constraints",
        number=7,
        title="Constraints",
        table_columns=("Constraint", "Source"),
        may_be_empty=True,
    ),
    Section(
        key="business_invariants",
        number=8,
        title="Business Invariants",
        table_columns=("#", "Invariant"),
    ),
    Section(
        key="lifecycle_states",
        number=9,
        title="Lifecycle States",
        table_columns=("Object", "State", "Meaning"),
    ),
    Section(
        key="business_events",
        number=10,
        title="Business Events",
        table_columns=("Event", "When It Occurs", "Significance"),
    ),
    Section(
        key="authority_boundaries",
        number=11,
        title="Authority Boundaries",
        table_columns=("Business Object", "Authoritative Owner"),
    ),
    Section(
        key="out_of_scope",
        number=12,
        title="Out of Scope",
        table_columns=("Item", "Reason"),
    ),
    Section(
        key="governance_scope",
        number=13,
        title="Governance Scope",
        table_columns=("Scope Item", "Relationship"),
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
        prose=True,
    ),
)

SECTIONS_BY_KEY: dict[str, Section] = {s.key: s for s in SECTIONS}


def section(key: str) -> Section:
    """Look up a declared section, or fail hard. There is no default."""
    if key not in SECTIONS_BY_KEY:
        raise KeyError(f"no such seed section: {key!r}")
    return SECTIONS_BY_KEY[key]
