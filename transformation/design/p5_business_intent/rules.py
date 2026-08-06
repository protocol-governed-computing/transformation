"""The P5 rule set — what makes a Business Intent register admissible.

Seven registers, their columns, their vocabularies and their traceability come from
`templates/p5_business_intent_template_v0.md`. Declared here is what the template cannot express.

P5 is the first step **up the purity ladder**. Every phase before it is business language only;
P5 admits *provisional* artifact codes — `CC_REGISTER_BOOK_V0` — because naming the thing you
intend to build is how intent becomes specific. What it still may not admit is a *binding*: a
domain-qualified FQDN, a JSONPath, a module path. Those are P7's, and a phase that reached for
them would be deciding placement before governance intent had been established.

That produces the rule pair that is P5's signature, and they pull in opposite directions:

- `provisional_codes` **must not** be namespaced. A code carrying a domain has already been placed.
- `cross_subdomain_refs` **must** cite exact, resolvable FQDNs, because those artifacts already
  exist and citing what exists is observation, not design (field manual §4.2's standing exception
  at every rung).

The same document therefore forbids a namespace in one register and requires one in another, and
the reason is not stylistic: one register names what this change will create, the other names what
it will lean on.

A cell with no basis in the seed or the snapshot is declared `UNRESOLVED` — a governed hole. It is
admissible, scored on the figure of merit, and strictly better than a guess.
"""

from __future__ import annotations

from transformation.design.derive import derived_rules
from transformation.design.rules import (
    Rule,
    dossier_header_rules,
    governed_hole_rules,
)
from transformation.design.template_reader import load

TEMPLATE = load("p5")

# P5 is the phase where the subdomain purpose reappears, and until now it reappeared as a fresh
# paragraph by a second author. It reads the seed so the substitution has to be declared.
PRIORS = ("p0",)

OBSERVATION_OPERATION = "si.artifact.list"

# operation → the key its result carries rows under.
OBSERVATIONS = {OBSERVATION_OPERATION: "artifacts"}

ARTIFACT_REFERENCE_PATTERN = r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+"

# A provisional code: family, name, version — and no namespace. The families are the template's,
# read from it rather than restated, because the two declarations drifted once already: the pattern
# admitted four families while a business change routinely authors transforms, events, bindings and
# a storage declaration, and every one of those fell outside the P5→P7 closure as a result.
PROVISIONAL_CODE_FAMILIES = TEMPLATE.register("provisional_codes").vocabularies["Family"]
PROVISIONAL_CODE_PATTERN = (
    r"^(?:" + "|".join(PROVISIONAL_CODE_FAMILIES) + r")_[A-Z0-9_]+_V\d+$"
)


PURPOSE_RULES: list[Rule] = [
    Rule(
        id="PURPOSE_NOT_CARRIED_FROM_SEED",
        check="PRIOR_PROSE_CARRIED",
        register="purpose_provenance",
        params={
            "prior_phase": "p0",
            "prior_register": "subdomain_purpose",
            "prose_register": "subdomain_purpose",
            "column": "Disposition",
            "inherited_value": "INHERITED",
            "detail": (
                "the purpose is declared INHERITED and does not match the seed's — inherit it "
                "word for word, or declare REFINED and say what this phase adds"
            ),
        },
        intent="the one narrative no artifact can derive is authored once and never quietly replaced",
    ),
    Rule(
        id="REFINEMENT_NOT_STATED",
        check="CELL_NOT_EMPTY",
        register="purpose_provenance",
        params={
            "column": "Refinement",
            "only_when_column": "Disposition",
            "only_when_value": "REFINED",
            "detail": (
                "a refined purpose must state what it adds that the seed did not say; silence "
                "here is the silent replacement this register exists to prevent"
            ),
        },
        intent="superseding upstream content is allowed, doing it without saying so is not",
    ),
]


PURITY_RULES: list[Rule] = [
    Rule(
        id="PROVISIONAL_CODE_ALREADY_BOUND",
        check="CELL_TOKEN_ABSENT",
        register="provisional_codes",
        params={
            "columns": ["Provisional Code"],
            "pattern": r"::",
            "detail": (
                "{token!r} in {column!r} — a provisional code carrying a namespace has already "
                "been placed, and placement is Stage 7's decision"
            ),
        },
        intent="a provisional code names what to build, never where it will live",
    ),
    Rule(
        id="PROVISIONAL_CODE_MALFORMED",
        check="CELL_MATCHES",
        register="provisional_codes",
        params={
            "column": "Provisional Code",
            "pattern": PROVISIONAL_CODE_PATTERN,
            "detail": "provisional code must be FAMILY_NAME_V<n> with no namespace",
        },
        intent="a provisional code is readable as a family, a name and a version",
    ),
    Rule(
        id="PROVISIONAL_FAMILY_MISMATCH",
        check="CELL_PREFIXED_BY_COLUMN",
        register="provisional_codes",
        params={"column": "Provisional Code", "prefix_column": "Family"},
        intent="a code and the family it is filed under agree",
    ),
    Rule(
        id="CROSS_SUBDOMAIN_REF_UNRESOLVED",
        check="CITED_ARTIFACTS_RESOLVE",
        register="cross_subdomain_refs",
        params={
            "column": "CC Code",
            "pattern": ARTIFACT_REFERENCE_PATTERN,
            "observation": OBSERVATION_OPERATION,
        },
        intent="a capability borrowed from elsewhere must be one that really exists",
    ),
    Rule(
        id="BINDING_LEAKED_INTO_INTENT",
        check="CELL_TOKEN_ABSENT",
        register="business_objects",
        params={
            "columns": ["Store Name", "Record Model", "Business Rationale"],
            "pattern": r"\$\.[A-Za-z_]|/[a-z_]+/|\b[0-9a-f]{16,}\b",
            "detail": (
                "{token!r} in {column!r} — a path, a binding expression or a hash is an "
                "implementation decision, and Stage 7 owns those"
            ),
        },
        intent="intent says what must be true, never how it is wired",
    ),
    Rule(
        id="INVARIANT_WITHOUT_BUSINESS_REASON",
        check="CELL_NOT_EMPTY",
        register="invariants",
        params={
            "column": "Business Reason",
            "detail": (
                "invariant states no business reason — a rule without one is a technical "
                "constraint and belongs elsewhere"
            ),
        },
        intent="every invariant is answerable to the business, not to the design",
    ),
    Rule(
        id="IDENTITY_WITHOUT_UNIQUENESS_RULE",
        check="CELL_NOT_EMPTY",
        register="identity_semantics",
        params={
            "column": "Uniqueness Rule",
            "detail": (
                "identity declares no uniqueness rule — what a duplicate means is irreducible "
                "business knowledge the compiler cannot infer"
            ),
        },
        intent="identity semantics are stated, never inferred from field names",
    ),
]


def rule_set() -> list[Rule]:
    """The complete declared P5 rule set: derived, then purity, then the dossier header."""
    return (
        derived_rules(TEMPLATE)
        + PURPOSE_RULES
        + PURITY_RULES
        + governed_hole_rules()
        + dossier_header_rules()
    )
