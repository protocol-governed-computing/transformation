"""Derive a phase's rule set from its vendored template.

Most of what governs a phase document is already declared in the template: which registers exist,
what columns they carry, which columns hold a controlled vocabulary, which hold business prose, and
which may legitimately be empty. Restating that in Python produces a second declaration that can
disagree with the tested one — and did, in this repo's first cut.

So the rules that follow mechanically from a template are generated here, and a phase's own
`rules.py` declares only what the template cannot express: belief resolution, citation grounding,
and anything else that is a judgement about meaning rather than shape.

Adding a register to a template therefore adds its rules. Forgetting to add them is not possible,
which is the failure mode that leaves one register quietly ungoverned.
"""

from __future__ import annotations

from transformation.design.template_reader import PhaseTemplate, Register
from transformation.design.rules import Rule

# A compiled artifact identity. Business-language columns must not contain one — a business
# register that names artifacts has had design smuggled into it.
ARTIFACT_TOKEN_PATTERN = r"\b(?:AC|CC|CS|CT|EV|IN|PR|RB|SD|ST|TI|TE|WF)_[A-Z0-9_]+_V\d+\b"

# Sources a citation may name that are not registers: the seed a CR starts from, a ruling only a
# human can make, and a direct observation of the compiled projection.
LITERAL_SOURCES = ("CR seed", "human decision", "projection", "S1 seed")


def _register_rules(register: Register, citable: list[str]) -> list[Rule]:
    """Every rule that follows mechanically from one register's declaration.

    `citable` is what this phase may cite — its own registers plus those its handoff contract
    declares it consumes.
    """
    # A register declared without a table is narrative — the Subdomain Purpose is the only one,
    # and it is narrative by definition: the business context no compiled artifact can derive.
    # It is still governed; it just cannot be governed as rows.
    if not register.columns:
        return [
            Rule(
                id="REGISTER_EMPTY",
                check="SECTION_HAS_TEXT",
                register=register.id,
                params={"detail": "narrative register is empty — it states nothing"},
                intent="a narrative register carries the context nothing downstream can rederive",
            )
        ]

    out: list[Rule] = [
        Rule(
            id="REGISTER_MISSING",
            check="TABLE_PRESENT",
            register=register.id,
            intent="a declared register must be present and readable as rows",
        ),
    ]

    if register.columns:
        out.append(
            Rule(
                id="REGISTER_COLUMN_MISSING",
                check="TABLE_HAS_COLUMNS",
                register=register.id,
                params={"columns": list(register.columns)},
                intent="downstream phases read these columns by name",
            )
        )

    if not register.optional:
        out.append(
            Rule(
                id="REGISTER_EMPTY",
                check="TABLE_HAS_ROWS",
                register=register.id,
                intent="an empty required register asserts nothing",
            )
        )

    # Vocabularies declared inline in the column header, e.g. `Certainty (HIGH, MEDIUM, LOW)`.
    for column, values in register.vocabularies.items():
        out.append(
            Rule(
                id="CELL_NOT_IN_VOCABULARY",
                check="CELL_IN_VOCABULARY",
                register=register.id,
                params={"column": column, "vocabulary": list(values)},
                intent=f"{column} is a controlled vocabulary declared by the template",
            )
        )

    # Business-language columns hold prose about the business, never compiled identities. The flag
    # may scope to specific columns, which is why this is not a whole-document rule.
    business_columns = [c for c in register.business_language_columns if c]
    if business_columns:
        out.append(
            Rule(
                id="DESIGN_LEAKED_INTO_BUSINESS_LANGUAGE",
                check="CELL_TOKEN_ABSENT",
                register=register.id,
                params={
                    "columns": business_columns,
                    "pattern": ARTIFACT_TOKEN_PATTERN,
                    "detail": (
                        "{token!r} appears in business-language column {column!r} — "
                        "this register states business meaning, not design"
                    ),
                },
                intent="business registers name no compiled artifact",
            )
        )

    if register.traceable:
        out.append(
            Rule(
                id="ROW_WITHOUT_SOURCE_FINDING",
                check="CELL_NOT_EMPTY",
                register=register.id,
                params={
                    "column": "Source Finding",
                    "detail": "row cites no earlier finding — a phase restates its input, it does not add to it",
                },
                intent="an uncited row has no provenance in the dossier",
            )
        )
        out.append(
            Rule(
                id="SOURCE_FINDING_UNRESOLVED",
                check="SOURCE_FINDING_RESOLVES",
                register=register.id,
                params={
                    "column": "Source Finding",
                    "known_registers": citable,
                    "literal_sources": list(LITERAL_SOURCES),
                },
                intent="a citation must name something this phase can actually cite",
            )
        )
        out.append(
            Rule(
                id="CITATION_ORDINAL_UNRESOLVED",
                check="CITED_ORDINAL_RESOLVES",
                register=register.id,
                params={"column": "Source Finding"},
                intent="an ordinal past the end of a register cites a finding that is not there",
            )
        )

    return out


def _all_declared_registers() -> set[str]:
    """Every register id declared by any phase template.

    Cached on first use — the templates are vendored and do not change during a run.
    """
    global _DECLARED
    if _DECLARED is None:
        from transformation.design.catalog import PHASES
        from transformation.design.template_reader import load

        ids: set[str] = set()
        for spec in PHASES:
            if spec.template is None:
                continue
            ids |= {r.id for r in load(spec.id).registers}
        _DECLARED = ids
    return _DECLARED


_DECLARED: set[str] | None = None


def derived_rules(template: PhaseTemplate) -> list[Rule]:
    """The rule set that follows from a template, before any phase-specific declaration.

    What a phase may cite is **every register the dossier declares**, not only what its
    `gov_projection` Consumes list forwards. Consumes is the lossless handoff — the working input a
    phase receives — while provenance may reach further back: the tested P7 register cites S1, S3,
    S5 and S6 alike, and none of those are in its Consumes.

    Restricting citation to Consumes rejected six of eight tested dossier documents. The rule that
    holds is that a citation must name a register some phase actually declares, so a typo or a
    fabricated register id is still caught.
    """
    citable = sorted(_all_declared_registers() | {r.id for r in template.registers})
    out: list[Rule] = []
    for register in template.registers:
        out.extend(_register_rules(register, citable))
    return out


def coverage(template: PhaseTemplate) -> dict[str, int]:
    """How much of a phase its template governs — reported so it cannot be assumed.

    A phase whose rules are wholly derived is fully covered by the tested template. One with many
    hand-declared rules is carrying judgement the template does not express, which is legitimate but
    worth seeing.
    """
    return {
        "registers": len(template.registers),
        "derived_rules": len(derived_rules(template)),
        "vocabulary_columns": sum(len(r.vocabularies) for r in template.registers),
        "business_language_registers": sum(1 for r in template.registers if r.business_language_columns),
        "traceable_registers": sum(1 for r in template.registers if r.traceable),
        "optional_registers": sum(1 for r in template.registers if r.optional),
    }
