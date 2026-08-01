"""Check kinds — the implementation half of the P0 oracle.

A check kind is a *mechanism*: "is this cell's value in a vocabulary", "is this column absent",
"does this token appear anywhere". It knows how to inspect a seed document and nothing about which
register it is inspecting or why that matters. Those are declared in `rules.py`.

This mirrors the platform's own split: a workflow graph declares nodes and bindings and names a
capability by FQDN; the capability implements a mechanism and holds no policy. Adding a governance
rule must not require a new mechanism, and a new mechanism must not carry a rule's intent.

The registry is closed. An unknown check kind is fail-hard, never a skipped rule — a silently
skipped rule is the vacuity failure this codebase has hit repeatedly.
"""

from __future__ import annotations

import re
from typing import Callable

from transformation.phases.evaluate import Block, ParsedDocument

CheckFn = Callable[[ParsedDocument, "object"], list[tuple[str, str]]]

_REGISTRY: dict[str, CheckFn] = {}


def check(kind: str) -> Callable[[CheckFn], CheckFn]:
    def register(fn: CheckFn) -> CheckFn:
        if kind in _REGISTRY:
            raise KeyError(f"duplicate check kind: {kind}")
        _REGISTRY[kind] = fn
        return fn

    return register


def dispatch(kind: str) -> CheckFn:
    """Resolve a check kind, or fail hard."""
    if kind not in _REGISTRY:
        raise KeyError(
            f"unknown check kind {kind!r}; declared kinds are {sorted(_REGISTRY)}"
        )
    return _REGISTRY[kind]


def kinds() -> list[str]:
    return sorted(_REGISTRY)


# Helpers ----------------------------------------------------------------------------------


def _block(doc: ParsedDocument, rule) -> Block | None:
    """Locate what a rule governs.

    A register identity wins when the rule declares one — it is stable across retitling and
    unambiguous when a section holds several registers. Section-title matching remains for P0,
    which has no RI-0 template and therefore no register markers.
    """
    register = getattr(rule, "register", None)
    if register:
        found = doc.register(register)
        if found is not None:
            return found
        # Fall through: a document with no register markers (P0, and any hand-authored register
        # predating the template salvage) is still addressable by section title. Returning None
        # here would report every register missing rather than checking it.
    return doc.find(rule.section_title) if rule.section_title else None


def _where(rule) -> str:
    return getattr(rule, "register", None) or rule.section_title or "document"


def _cell(row: dict[str, str], prefix: str) -> str:
    for key, value in row.items():
        if key.startswith(prefix):
            return value.strip()
    return ""


# A register with nothing in it renders one `| NONE IDENTIFIED |` row rather than no rows at all.
# Emptiness is declared, never inferred from absence — an empty table and a register nobody filled
# in look identical, and only one of them is a considered answer.
_EMPTINESS_SENTINEL = "NONE IDENTIFIED"


def _is_sentinel(row: dict[str, str]) -> bool:
    """True when a row is the declared-empty marker rather than content."""
    values = [str(v).strip() for v in row.values()]
    if not values:
        return False
    return values[0].upper() == _EMPTINESS_SENTINEL and not any(values[1:])


def _rows(doc: ParsedDocument, rule):
    """Content rows of the register a rule governs.

    The emptiness sentinel is excluded: it is a statement that the register has no entries, not an
    entry. Checking its blank cells for vocabularies and citations would report findings against a
    register whose author correctly said there was nothing to report.
    """
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    return [
        (i, row)
        for i, row in enumerate(block.table.rows, start=1)
        if not _is_sentinel(row)
    ]


# Check kinds ------------------------------------------------------------------------------


@check("HEADER_FIELD_PRESENT")
def _header_field_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    for name in rule.params["fields"]:
        if not doc.header.get(name, "").strip():
            out.append(("header", f"required field {name!r} absent"))
    return out


@check("HEADER_FIELD_MATCHES")
def _header_field_matches(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    pattern = re.compile(rule.params["pattern"])
    for name in rule.params["fields"]:
        value = doc.header.get(name, "").strip()
        if value and not pattern.match(value):
            out.append(("header", f"{name} {value!r} does not match {rule.params['pattern']}"))
    return out


@check("SECTION_PRESENT")
def _section_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    if _block(doc, rule) is None:
        return [(_where(rule), "required section absent from the seed")]
    return []


@check("SECTION_NUMBERED")
def _section_numbered(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    expected = rule.params["number"]
    if block.number != expected:
        return [(_where(rule), f"expected section {expected}, found {block.number}")]
    return []


@check("SECTIONS_ASCENDING")
def _sections_ascending(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    numbers = [b.number for b in doc.blocks if b.number is not None]
    if numbers != sorted(numbers):
        return [("document", "numbered sections are not in ascending order")]
    return []


@check("SECTION_HAS_TEXT")
def _section_has_text(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        # Same reasoning as TABLE_PRESENT: an absent narrative register is a finding, not a skip.
        if getattr(rule, "register", None):
            return [(_where(rule), "declared register is absent from the document")]
        return []
    if not block.text():
        return [(_where(rule), rule.params["detail"])]
    return []


@check("SECTION_DECLARES_ONE_OF")
def _section_declares_one_of(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None:
        return []
    vocabulary = rule.params["vocabulary"]
    found = [t for t in vocabulary if re.search(rf"\b{re.escape(t)}\b", block.text())]
    if not found:
        return [(_where(rule), f"nothing declared; expected one of {list(vocabulary)}")]
    if len(found) > 1:
        return [(_where(rule), f"multiple values named: {found}")]
    return []


@check("TABLE_PRESENT")
def _table_present(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """The register must be there, and must be readable as rows.

    Absence is the finding this check exists for. Returning nothing when the register is missing —
    which is what an earlier version did — meant a document could drop a register entirely and be
    judged admissible: every cell-level rule skips a register it cannot find, so nothing else would
    have spoken up either.
    """
    block = _block(doc, rule)
    if block is None:
        return [(_where(rule), "declared register is absent from the document")]
    if block.table is None:
        return [(_where(rule), "register is present but carries no table, so it cannot be read as rows")]
    return []


@check("TABLE_HAS_COLUMNS")
def _table_has_columns(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    out = []
    for expected in rule.params["columns"]:
        if not any(col.startswith(expected) for col in block.table.columns):
            out.append(
                (
                    _where(rule),
                    f"required column {expected!r} absent; found {block.table.columns}",
                )
            )
    return out


@check("TABLE_HAS_ROWS")
def _table_has_rows(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    if not block.table.rows:
        return [(_where(rule), "section requires at least one row")]
    return []


@check("COLUMN_ABSENT")
def _column_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    forbidden = rule.params["column"]
    if any(col.startswith(forbidden) for col in block.table.columns):
        return [(_where(rule), rule.params["detail"])]
    return []


@check("CELL_IN_VOCABULARY")
def _cell_in_vocabulary(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    vocabulary = rule.params["vocabulary"]
    for i, row in _rows(doc, rule):
        value = _cell(row, column).upper()
        if value not in vocabulary:
            out.append(
                (
                    f"{_where(rule)} row {i}",
                    f"{value!r} is not one of {list(vocabulary)}",
                )
            )
    return out


@check("CELL_NOT_EMPTY")
def _cell_not_empty(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    for i, row in _rows(doc, rule):
        if not _cell(row, column):
            out.append((f"{_where(rule)} row {i}", rule.params["detail"]))
    return out


@check("CELL_NOT_PREFIXED")
def _cell_not_prefixed(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    out = []
    column = rule.params["column"]
    for i, row in _rows(doc, rule):
        value = _cell(row, column).lower()
        for prefix in rule.params["prefixes"]:
            if value.startswith(prefix):
                out.append(
                    (
                        f"{_where(rule)} row {i}",
                        rule.params["detail"].format(prefix=prefix.strip()),
                    )
                )
                break
    return out


@check("TOKEN_ABSENT")
def _token_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    pattern = re.compile(rule.params["pattern"])
    return [
        ("document", rule.params["detail"].format(token=token))
        for token in sorted(set(pattern.findall(doc.raw)))
    ]


@check("CELL_MATCHES")
def _cell_matches(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every non-empty cell in a column must match a declared pattern.

    Emptiness is CELL_NOT_EMPTY's concern — a rule that checked both would report two findings for
    one defect and make the cause ambiguous.
    """
    out = []
    column = rule.params["column"]
    pattern = re.compile(rule.params["pattern"])
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        if value and not pattern.match(value):
            out.append((f"{_where(rule)} row {i}", rule.params["detail"].format(value=value)))
    return out


# Observation-aware checks ------------------------------------------------------------------
#
# These read `doc.observed` — facts gathered from the assembled composition through the governed
# inspection capability and handed to the evaluator as declared input. They are the only checks
# that can be wrong for a reason outside the document: a citation is a claim about the world, and
# checking it needs the world.


def _observed_identities(doc: ParsedDocument, operation: str) -> set[str]:
    """Artifact identities from an observation, however the inspection surface shaped them.

    `si.artifact.list` answers with rows, not bare identities; other operations may answer with
    plain strings. Normalising here keeps the shape of an inspection result out of the rule
    declaration, which should say *what* is checked rather than how the surface happens to reply.
    """
    out: set[str] = set()
    for entry in doc.observed.get(operation, []) or []:
        if isinstance(entry, str):
            out.add(entry)
        elif isinstance(entry, dict):
            value = entry.get("artifact") or entry.get("fqdn") or entry.get("fqdn_id")
            if value:
                out.add(str(value))
    return out


@check("CITED_ARTIFACTS_RESOLVE")
def _cited_artifacts_resolve(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Classify every cited artifact identity against the observed baseline, and report only defects.

    Field manual §4.7, Identity-Preserving Taxonomy — every reference resolves to one of:

        A  exact          the identity is in the baseline
        B  typo-alias     a near-match exists; the citation is misspelled
        C  wrong-domain   the code exists, under a different namespace
        D  proposed-new   well-formed, absent from the baseline — legitimate new design
        E  fabrication    no identity anywhere

    Only B, C and E are defects. **A count of not-found citations is inadmissible evidence**: it
    over-flags D, and D is what every CR that designs anything is full of. An earlier version of
    this check did exactly that — it would have rejected a correct dossier for proposing new work.

    D and E are not separable from the document alone; telling them apart needs the CR's declared
    new artifacts, which arrive at P6b. Until then both are left unflagged rather than guessed,
    because guessing here reintroduces the over-flagging the taxonomy exists to prevent.
    """
    known = _observed_identities(doc, rule.params["observation"])
    if not known:
        return [(
            _where(rule),
            "no composition was observed — citations cannot be resolved, so this register's "
            "grounding is unchecked",
        )]

    # Index the baseline by bare code, so a right-code/wrong-namespace citation is recognisable.
    by_code: dict[str, list[str]] = {}
    for fqdn in known:
        by_code.setdefault(fqdn.split("::")[-1], []).append(fqdn)

    out = []
    column = rule.params["column"]
    gate_column = rule.params.get("only_when_column")
    gate_value = rule.params.get("only_when_value")
    pattern = re.compile(rule.params["pattern"])

    for i, row in _rows(doc, rule):
        if gate_column and _cell(row, gate_column).upper() != gate_value:
            continue
        cited = pattern.findall(_cell(row, column))
        if not cited and rule.params.get("detail_missing"):
            out.append((f"{_where(rule)} row {i}", rule.params["detail_missing"]))
            continue

        for fqdn in cited:
            if fqdn in known:
                continue                                        # A — exact
            code = fqdn.split("::")[-1]
            if code in by_code:                                 # C — wrong domain
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{fqdn!r} names a code that exists elsewhere: {sorted(by_code[code])} — "
                    f"wrong namespace, not a new artifact",
                ))
                continue
            near = [k for k in by_code if _is_near(code, k)]
            if near:                                            # B — typo alias
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{fqdn!r} closely resembles {sorted(near)[:3]} — likely a misspelled citation",
                ))
            # D / E — indistinguishable without the CR's proposed set; not flagged.
    return out


def _is_near(a: str, b: str) -> bool:
    """Cheap single-edit proximity — enough to catch a misspelling, not enough to over-match."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    short, long = (a, b) if len(a) < len(b) else (b, a)
    for i in range(len(long)):
        if long[:i] + long[i + 1:] == short:
            return True
    return False


@check("CELL_TOKEN_ABSENT")
def _cell_token_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A pattern must not appear in specific columns.

    Scoped to columns rather than the whole document, because a register can legitimately hold both
    business prose and the identity it was grounded against. Applying the rule document-wide would
    forbid the citation that makes the grounding checkable.
    """
    out = []
    pattern = re.compile(rule.params["pattern"])
    for column in rule.params["columns"]:
        for i, row in _rows(doc, rule):
            for token in sorted(set(pattern.findall(_cell(row, column)))):
                out.append((
                    f"{_where(rule)} row {i}",
                    rule.params["detail"].format(token=token, column=column),
                ))
    return out


@check("SOURCE_FINDING_RESOLVES")
def _source_finding_resolves(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A citation must name something this phase can legitimately cite.

    The valid set is declared, not guessed at with a regex:

    - a register this phase **consumes**, from its `gov_projection` handoff contract
    - a register this phase **owns** — a later register citing an earlier one of the same phase is
      ordinary intra-phase provenance
    - a **non-register source**: the seed, a human ruling, or a direct observation of the projection

    A stage qualifier may precede the register id (`S1 business_vocabulary Block`), which is how the
    tested dossiers disambiguate a register name that several phases carry.

    Anything else is a citation to nowhere. An earlier version of this rule matched a hand-tuned
    regex and rejected `analysis_findings Q2` — a correct citation of the phase's own register —
    because the pattern had never been derived from what a phase may actually cite.
    """
    known = set(rule.params["known_registers"])
    literal = tuple(rule.params.get("literal_sources", ()))
    stage = re.compile(r"^S\d+[a-z]?\s+")

    # Field manual §4.2: at every rung, an artifact already in the baseline may be cited by exact
    # FQDN as evidence — citing the baseline is observation, not design. So an identity grounds a
    # row just as a register reference does.
    identity = re.compile(r"[a-z][a-z0-9_.]*::[A-Z][A-Z0-9_]*_V\d+")

    def resolves(citation: str) -> bool:
        citation = citation.strip()
        if not citation or citation.startswith(literal):
            return True
        if identity.search(citation):
            return True
        head = stage.sub("", citation).split()
        return bool(head) and head[0].strip(":,.;()") in known

    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, rule.params["column"])
        if not value:
            continue                             # emptiness is ROW_WITHOUT_SOURCE_FINDING's job
        # A cell may carry several citations, separated by `;` — the tested dossiers routinely
        # ground one row in two places. One resolvable citation makes the row traceable; requiring
        # all of them would reject a row whose second reference is an aside rather than a register.
        if any(resolves(part) for part in value.split(";")):
            continue
        out.append((
            f"{_where(rule)} row {i}",
            f"{value!r} contains no citation naming a declared register or recognised source",
        ))
    return out

