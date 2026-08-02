"""The P2 rule set — what makes a Domain Model register admissible.

Ten registers, their columns, their vocabularies and their traceability come from
`templates/p2_domain_model_template_v0.md`. What is declared here is what the template cannot
express, and for P2 that is one thing above all: **grounding**.

P1 could be judged from the document alone — traceability is a property of what the register says
about itself. P2 cannot. A row claiming an artifact already exists is a claim about the assembled
composition, and the only way to check it is to look. That is why P2 is the first phase to bind a
capability rather than compose pure transforms.

Grounding is checked through the identity-preserving taxonomy of field manual §4.7, not by counting
what was not found. A CR that designs anything is full of identities absent from the baseline; a
rule that flagged them would reject every correct dossier for doing its job.
"""

from __future__ import annotations

from transformation.phases.derive import derived_rules
from transformation.phases.rules import Rule, dossier_header_rules
from transformation.phases.template_reader import load

TEMPLATE = load("p2")

# The inspection operation P2 grounds against. Named once, so the workflow that gathers the
# observation and the rules that consume it cannot drift apart.
OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

# A fully-qualified artifact identity, e.g. `blockchain::WF_PROPOSE_BLOCK_V0`.
ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"


GROUNDING_RULES: list[Rule] = [
    Rule(
        id="BASELINE_IDENTITY_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="pps_baseline_fqdns",
        params={
            "column": "FQDN",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
            "detail_missing": "baseline row names no artifact identity",
        },
        intent="the baseline register records what already exists, so every row must be observable",
    ),
    Rule(
        id="VERIFIED_BELIEF_IDENTITY_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="belief_verification",
        params={
            "column": "Evidence",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
            "only_when_column": "Result",
            "only_when_value": "VERIFIED",
        },
        intent="a belief grounded on an identity must be grounded on one that is really there",
    ),
    Rule(
        id="BELIEF_WITHOUT_EVIDENCE",
        check="CELL_NOT_EMPTY",
        register="belief_verification",
        params={
            "column": "Evidence",
            "detail": "belief has a result but records nothing about how it was reached",
        },
        intent="a result without evidence is an assertion, not a verification",
    ),
]



# The upstream phase documents P2 is judged against. P2 consumes P1's change request through the
# `gov_projection` handoff, and until now nothing checked that it arrived intact.
PRIORS = ("p1",)


# P1 declares what the author believes the system already provides; P2's spine is the register that
# resolves each of those beliefs. That makes the handoff checkable in the only way that matters —
# every belief committed to at P1 must have a result at P2, and the result must be about the belief
# that was actually declared.
#
# This is the first pair of rules in the pipeline that read two documents. A dropped belief is
# invisible to P1 (which never sees P2) and invisible to P2 (whose register is well formed with two
# rows or with three); it exists only in the gap between them.
BELIEF_PRESERVATION_RULES: list[Rule] = [
    Rule(
        id="BELIEF_NOT_CARRIED_FROM_P1",
        check="PRIOR_ROWS_CITED",
        register="belief_verification",
        params={
            "prior_phase": "p1",
            "prior_register": "system_beliefs",
            "prior_key_column": "Belief",
            "citation_column": "Source Finding",
        },
        intent="a belief nobody carried forward is forgotten, not resolved",
    ),
    Rule(
        id="BELIEF_RESTATED_FROM_P1",
        check="PRIOR_ROW_MATCHES_CITED",
        register="belief_verification",
        params={
            "prior_phase": "p1",
            "prior_register": "system_beliefs",
            "prior_key_column": "Belief",
            "key_column": "Belief",
            "citation_column": "Source Finding",
        },
        intent="a verification must resolve the belief it cites, not a substitute for it",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P2 rule set: derived, grounding, cross-phase, then the header."""
    return (
        derived_rules(TEMPLATE)
        + GROUNDING_RULES
        + BELIEF_PRESERVATION_RULES
        + dossier_header_rules()
    )
