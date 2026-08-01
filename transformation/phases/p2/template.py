"""The P2 register template — the Domain Model, confirmed against the snapshot.

P1 restates the seed under traceability. P2 is the first phase that goes and *looks*: every System
Belief the seed recorded is grounded against the assembled composition and given a result.

**Belief Verification is the spine.** Every other register projects from it, and the phase is
complete when every belief has a result. `NOT_FOUND` is a final answer — absence is a finding, not
a reason to keep searching. That distinction is what stops a phase from stalling on something that
genuinely does not exist.

P2 also inverts a rule the earlier phases enforce. P0 and P1 forbid compiled artifact identifiers,
because a business register that names artifacts has had design smuggled into it. P2 *requires*
them: an evidence cell that does not name what was found is not evidence. The same token is
contraband in one register and the whole point in another, which is why rules are declared per
phase rather than shared by default.
"""

from __future__ import annotations

from transformation.phases.p0.template import HEADER_FIELDS, Section

# A verification result. NOT_FOUND is final and admissible — the phase records absence rather than
# treating it as incomplete work.
BELIEF_RESULTS = ("VERIFIED", "NOT_FOUND", "INSUFFICIENT_EVIDENCE")

# What an entity's grounding against the composition turned up.
EVIDENCE_STATUS = ("VERIFIED", "PARTIAL", "NOT_FOUND")

# Evidence must name what was observed. A fully-qualified artifact identity looks like
# `namespace::CODE_V0`; anything else is a claim without a subject.
ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# The inspection operation P2 observes the composition through. Declared here so the register, the
# rule set and the workflow all name the same thing.
OBSERVATION_OPERATION = "si.artifact.list"

SECTIONS: tuple[Section, ...] = (
    Section(
        key="belief_verification",
        number=1,
        title="Belief Verification",
        table_columns=("Belief", "Result", "Evidence", "Source Finding"),
    ),
    Section(
        key="business_entities",
        number=2,
        title="Business Entities",
        table_columns=("Entity", "Description", "Evidence Status", "Source Finding"),
    ),
    Section(
        key="baseline",
        number=3,
        title="Baseline — What Already Exists",
        table_columns=("Artifact", "Kind", "Why It Matters"),
        may_be_empty=True,
    ),
    Section(
        key="gap_analysis",
        number=4,
        title="Gap Analysis — What Is Missing",
        table_columns=("Gap", "Evidence", "Source Finding"),
    ),
    Section(
        key="open_questions",
        number=5,
        title="Open Questions for P3",
        prose=True,
        may_be_empty=True,
    ),
)

SECTIONS_BY_KEY: dict[str, Section] = {s.key: s for s in SECTIONS}


def section(key: str) -> Section:
    """Look up a declared section, or fail hard. There is no default."""
    if key not in SECTIONS_BY_KEY:
        raise KeyError(f"no such P2 register: {key!r}")
    return SECTIONS_BY_KEY[key]
