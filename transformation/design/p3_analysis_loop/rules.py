"""The P3 rule set — what makes an Analysis Loop register admissible.

Seven registers, their columns, their vocabularies and their traceability come from
`templates/p3_analysis_loop_template_v0.md`. Declared here is what the template cannot express.

P3 is the first phase that **decides**. P0 reorganizes, P1 classifies, P2 discovers; P3 resolves
the extend-vs-new question P2 deferred and commits to REUSE / EXTEND / AUTHOR_NEW. Three things
follow that the template has no way to state.

**Reuse eligibility.** A REUSE or EXTEND decision names an existing artifact, and not every
existing artifact may be offered. A domain declares which plane it serves, and a business change
request may draw only on `substrate` and `business`. This is checked, not inferred: the reference
implementation tried inferring relevance from structure and the pre-filter chose against the
author's own later judgement. The declaration bounds the search space; the decision stays with the
author.

**Discovery saturation.** Analysis ends when it has stopped finding things, not when the analyst
tires. Every declared criterion must be SATISFIED, and the register must actually carry them —
a saturation claim resting on three of five criteria is the failure the criteria exist to prevent.

**Overturned answers are marked, never erased.** The verification pass re-checks prior findings
against the composition, and an OVERTURNED item must keep its evidence. Deleting the row instead
would leave a dossier that reads as though the mistake never happened.
"""

from __future__ import annotations

from transformation.design.derive import derived_rules
from transformation.design.rules import (
    Rule,
    dossier_header_rules,
    governed_hole_rules,
)
from transformation.design.template_reader import load

TEMPLATE = load("p3")

# P3 grounds against two observations. The artifact list resolves cited identities exactly as P2
# does; the composition summary carries each domain's declared reuse visibility, which is the one
# fact a reuse search may not infer. Named once so the workflow that gathers them and the rules
# that consume them cannot drift apart.
OBSERVATION_OPERATION = "si.snapshot.summary"
ARTIFACT_OBSERVATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {
    ARTIFACT_OBSERVATION: "artifacts",
    OBSERVATION_OPERATION: "reuse_visibility",
}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# What a business change request may draw on. `platform_service` serves the platform's own
# operation and `internal` exists to prove the platform works; neither is business capability.
BUSINESS_ELIGIBLE = ("substrate", "business")

# The saturation criteria of field manual §4.1. Declared here because the template states them as
# prose beneath the register, and prose beneath a table governs nothing.
SATURATION_CRITERIA = 5


DECISION_RULES: list[Rule] = [
    Rule(
        id="REUSE_CANDIDATE_NOT_ELIGIBLE",
        check="REUSE_CANDIDATE_ELIGIBLE",
        register="authoring_decisions",
        params={
            "column": "Alternatives Checked",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
            "artifact_observation": ARTIFACT_OBSERVATION,
            "eligible": list(BUSINESS_ELIGIBLE),
        },
        intent="a change request may only be offered candidates from a domain that permits reuse",
    ),
    Rule(
        id="DECISION_WITHOUT_ALTERNATIVES",
        check="CELL_NOT_EMPTY",
        register="authoring_decisions",
        params={
            "column": "Alternatives Checked",
            "detail": (
                "decision records no alternatives examined — 'I searched and found nothing' is "
                "credible only with the search shown"
            ),
        },
        intent="a committed decision shows the search that produced it",
    ),
    Rule(
        id="DECISION_WITHOUT_RATIONALE",
        check="CELL_NOT_EMPTY",
        register="authoring_decisions",
        params={
            "column": "Rationale",
            "detail": "decision states no rationale — a classification without a reason is an assertion",
        },
        intent="every decision traces to a grounded reason",
    ),
    Rule(
        id="CITED_ALTERNATIVE_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="authoring_decisions",
        params={
            "column": "Alternatives Checked",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": ARTIFACT_OBSERVATION,
        },
        intent="an alternative examined must be one that really exists",
    ),
    Rule(
        id="IMPACT_WITHOUT_EVIDENCE",
        check="CELL_NOT_EMPTY",
        register="impact_analysis",
        params={
            "column": "Evidence",
            "detail": "impact row carries no evidence — consumer counts are observed, never estimated",
        },
        intent="impact is mechanically captured, never summarised from memory",
    ),
    Rule(
        id="VERIFICATION_WITHOUT_EVIDENCE",
        check="CELL_NOT_EMPTY",
        register="verification_results",
        params={
            "column": "Evidence",
            "detail": (
                "verification records no evidence — grounding is not inherited, so a re-check "
                "that cites nothing did not happen"
            ),
        },
        intent="an overturned answer is marked with what overturned it, never erased",
    ),
]


SATURATION_RULES: list[Rule] = [
    Rule(
        id="SATURATION_CRITERIA_INCOMPLETE",
        check="TABLE_HAS_ROWS",
        register="saturation",
        params={"minimum": SATURATION_CRITERIA},
        intent=(
            "analysis is saturated only against every declared criterion; a claim resting on "
            "fewer is the gap the criteria exist to close"
        ),
    ),
    Rule(
        id="SATURATION_CLAIMED_WITHOUT_EVIDENCE",
        check="CELL_NOT_EMPTY",
        register="saturation",
        params={
            "column": "Evidence",
            "detail": "criterion is asserted satisfied with nothing to show for it",
        },
        intent="saturation is demonstrated, not declared",
    ),
]


# The upstream phase document P3 is judged against — P2's domain model, whose spine is the
# register P3's mandatory verification pass re-checks.
PRIORS = ("p2",)


# P3's verification pass exists to re-ground every prior result against the composition rather than
# inherit it. That is only a pass over P2's beliefs if it actually covers them: an author who
# re-verifies two of three results has re-verified nothing about the third, and the register reads
# as a complete pass either way.
#
# The register legitimately carries rows from elsewhere — a P2 baseline observation is a prior
# finding too — so this checks coverage of the belief spine, not that every row descends from it.
BELIEF_PRESERVATION_RULES: list[Rule] = [
    Rule(
        id="BELIEF_RESULT_NOT_REVERIFIED",
        check="PRIOR_ROWS_CITED",
        register="verification_results",
        params={
            "prior_phase": "p2",
            "prior_register": "belief_verification",
            "prior_key_column": "Belief",
            "citation_column": "Origin",
        },
        intent="a result nobody re-verified was inherited, and grounding is not inherited",
    ),
    Rule(
        id="BELIEF_RESULT_RESTATED_FROM_P2",
        check="PRIOR_ROW_MATCHES_CITED",
        register="verification_results",
        params={
            "prior_phase": "p2",
            "prior_register": "belief_verification",
            "prior_key_column": "Belief",
            "key_column": "Item",
            "citation_column": "Origin",
        },
        intent="a re-verification must address the result it cites, not a substitute for it",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P3 rule set: derived, decisions, saturation, cross-phase, header."""
    return (
        derived_rules(TEMPLATE)
        + DECISION_RULES
        + SATURATION_RULES
        + BELIEF_PRESERVATION_RULES
        + governed_hole_rules()
        + dossier_header_rules()
    )
