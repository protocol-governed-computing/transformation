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
from typing import Any, Callable

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


def _content_rows(block: Block | None):
    """Numbered content rows of a register block, sentinel excluded.

    The emptiness sentinel is not content: it is a statement that the register has no entries.
    Checking its blank cells for vocabularies and citations would report findings against a
    register whose author correctly said there was nothing to report.
    """
    if block is None or block.table is None:
        return []
    return [
        (i, row)
        for i, row in enumerate(block.table.rows, start=1)
        if not _is_sentinel(row)
    ]


def _rows(doc: ParsedDocument, rule):
    """Content rows of the register a rule governs."""
    return _content_rows(_block(doc, rule))


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
    # `minimum` defaults to 1 — "declared but empty asserts nothing". A register whose rows are a
    # fixed checklist rather than free content declares the count it owes, so a claim resting on
    # fewer rows than the criteria it cites is reported rather than read as complete.
    minimum = int(getattr(rule, "params", {}).get("minimum", 1))
    rows = len(block.table.rows)
    if rows < minimum:
        detail = (
            "section requires at least one row"
            if minimum == 1
            else f"section declares {rows} row(s); {minimum} are required"
        )
        return [(_where(rule), detail)]
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
    """A column that must carry a value — optionally only for rows in a given state.

    `only_when_column` / `only_when_value` narrow the rule to the rows it is really about, the same
    gating `CITED_ARTIFACTS_RESOLVE` uses. Without it a requirement that applies to one status
    would report against every row, and a register would have to be split to say something true
    about part of itself.
    """
    out = []
    column = rule.params["column"]
    only_when_column = rule.params.get("only_when_column")
    only_when_value = rule.params.get("only_when_value")
    for i, row in _rows(doc, rule):
        if only_when_column:
            gate = _cell(row, only_when_column)
            if gate.strip().upper() != str(only_when_value).upper():
                continue
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
    new artifacts, which arrive at P7. Until then both are left unflagged rather than guessed,
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



@check("REUSE_CANDIDATE_ELIGIBLE")
def _reuse_candidate_eligible(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every artifact offered as a reuse candidate must come from a domain that permits it.

    A domain declares which plane it serves; the declaration bounds the *search space* and never
    makes the *decision*. So this check answers one question only — may this domain's artifacts be
    offered at all — and says nothing about whether reusing any particular one is wise. That call
    stays with the author, per artifact, against evidence.

    Two ways to fail, and the second matters more than it looks:

    - the cited domain declares a visibility this CR may not draw on
    - the cited domain declares **no** visibility at all

    The second is a hard failure rather than a permissive default. Nothing yet stops a domain from
    compiling without the declaration, so absence would otherwise mean "search everything" — the
    inference the declaration exists to prevent, arriving silently through the back door.
    """
    observation = rule.params["observation"]
    eligible = set(rule.params["eligible"])
    pattern = re.compile(rule.params["pattern"])

    # The observation is scope → visibility. Scope, not domain: substrate layers declare a
    # visibility but are not composed domains, so a domain-keyed answer would omit exactly the
    # artifacts a business change request most legitimately reuses.
    declared: dict[str, Any] = dict(doc.observed.get(observation, {}) or {})

    # A cited identity names a *namespace*; the domain that owns it is what declares visibility.
    # They coincide for a business domain and diverge for the platform, whose namespaces are
    # federation boundaries — so an unknown namespace is resolved through the observation, never
    # by splitting the string and hoping.
    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, rule.params["column"])
        for identity in pattern.findall(value):
            namespace = identity.split("::")[0]
            domain = namespace if namespace in declared else _owning_domain(doc, rule, identity)
            if domain is None:
                continue                          # not in the baseline: proposed-new, not a reuse
            visibility = declared.get(domain)
            if visibility is None:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{identity!r} belongs to domain {domain!r}, which declares no reuse "
                    f"visibility — eligibility would have to be inferred, and inferring "
                    f"relevance is reserved to the author",
                ))
            elif visibility not in eligible:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{identity!r} belongs to domain {domain!r}, declared {visibility!r} — "
                    f"not offerable to this change request "
                    f"(eligible: {', '.join(sorted(eligible))})",
                ))
    return out


def _owning_domain(doc: ParsedDocument, rule, identity: str) -> str | None:
    """The domain that owns a cited identity, from the artifact observation."""
    for entry in doc.observed.get(rule.params["artifact_observation"], []) or []:
        if isinstance(entry, dict) and entry.get("artifact") == identity:
            return entry.get("domain")
    return None


@check("CELL_RESOLVES_IN_REGISTER")
def _cell_resolves_in_register(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A value in one register must name a row that really exists in another.

    The first check that reads two registers at once. Earlier phases judge each register on its own
    terms, because discovery has nothing to be consistent *with* yet. A consolidation phase is
    different: its whole job is that the registers agree, so an entry pointing at a gap nobody
    declared is exactly the defect it exists to catch — and one no single-register rule can see.

    Absence of the cell is not this rule's business; a blank is `CELL_NOT_EMPTY`'s finding, and
    reporting it twice would make one defect look like two.
    """
    # One target register, or several: a code may legitimately be declared new here OR carried over
    # from the existing inventory, and a rule naming only one of those would reject the other.
    targets = rule.params.get("target_registers") or [rule.params["target_register"]]
    target_column = rule.params["target_column"]
    target_columns = rule.params.get("target_columns") or [target_column] * len(targets)

    known: set[str] = set()
    for register, column in zip(targets, target_columns):
        block = doc.register(register)
        if block is None or block.table is None:
            continue
        for row in block.table.rows:
            if _is_sentinel(row):
                continue
            value = _cell(row, column)
            if value:
                known.add(value.strip())
    target = " or ".join(targets)

    only_when_column = rule.params.get("only_when_column")
    only_when_value = rule.params.get("only_when_value")
    # A declared "nothing here" is an answer, not a dangling reference — the same distinction
    # `DEPENDENCY_PRECEDES` draws for a step that depends on nothing.
    none_markers = {str(m).strip() for m in rule.params.get("none_markers", ["—", "-", "NONE", "N/A"])}

    out = []
    for i, row in _rows(doc, rule):
        if only_when_column:
            gate = _cell(row, only_when_column)
            if gate.strip().upper() != str(only_when_value).upper():
                continue
        value = _cell(row, rule.params["column"])
        if not value or value.strip() in none_markers:
            continue
        for part in (p.strip() for p in value.split(";")):
            if part and part not in none_markers and part not in known:
                detail = rule.params.get(
                    "detail", "a document may only point at what it declared"
                )
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{part!r} names no row in {target}.{target_column} — {detail}",
                ))
    return out


@check("CELL_PREFIXED_BY_COLUMN")
def _cell_prefixed_by_column(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """One column must agree with another in the same row.

    A register that classifies its own rows can disagree with itself: a code named `CC_…` filed
    under family `WF` is well-formed in both cells and wrong as a pair. Checking each column against
    a fixed vocabulary cannot see it, because both values are individually legal.
    """
    column = rule.params["column"]
    prefix_column = rule.params["prefix_column"]
    separator = rule.params.get("separator", "_")

    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        prefix = _cell(row, prefix_column)
        if not value or not prefix:
            continue                             # emptiness is CELL_NOT_EMPTY's finding
        if not value.startswith(f"{prefix}{separator}"):
            out.append((
                f"{_where(rule)} row {i}",
                f"{value!r} does not agree with {prefix_column} {prefix!r} — "
                f"the row classifies itself two ways",
            ))
    return out


@check("CITED_ARTIFACTS_ABSENT")
def _cited_artifacts_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """An identity claimed as NEW must not already be in the composition.

    The inverse of `CITED_ARTIFACTS_RESOLVE`, and the only rule in the pipeline that reads a
    successful resolution as the defect. Every phase before this one cites what exists; the design
    phase assigns identities that will exist, and an assignment that collides with something
    already there is not a new artifact — it is a silent redefinition of an old one.

    Reported per identity, because a designer needs to know which name to change, not that one of
    them was taken.
    """
    observation = rule.params["observation"]
    pattern = re.compile(rule.params["pattern"])
    observed = _observed_identities(doc, observation)

    if not observed:
        return [(
            _where(rule),
            "no composition was observed — a collision check that cannot see the baseline would "
            "admit every colliding name",
        )]

    out = []
    for i, row in _rows(doc, rule):
        value = _cell(row, rule.params["column"])
        for identity in pattern.findall(value):
            if identity in observed:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{identity!r} already exists in the composition — assigning it here would "
                    f"redefine an artifact rather than create one",
                ))
    return out


@check("COLUMN_SEQUENCE_CONTIGUOUS")
def _column_sequence_contiguous(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """An integer column must run contiguously from a declared start.

    The first rule about a register's rows *as a sequence* rather than each row on its own. Every
    row can be individually perfect and the register still wrong: a gap in a build sequence means an
    artifact was dropped between two steps that both look fine, and nothing reading rows one at a
    time would notice the absence.
    """
    column = rule.params["column"]
    start = int(rule.params.get("start", 1))

    seen: list[tuple[int, int]] = []
    for i, row in _rows(doc, rule):
        value = _cell(row, column)
        if not value:
            continue
        try:
            seen.append((int(value), i))
        except ValueError:
            return [(f"{_where(rule)} row {i}", f"{value!r} is not a step number")]

    if not seen:
        return []

    out = []
    expected = start
    for number, i in sorted(seen):
        if number != expected:
            out.append((
                f"{_where(rule)} row {i}",
                f"step {number} follows {expected - 1} — the sequence skips {expected}, "
                f"and a gap is an artifact silently dropped",
            ))
            expected = number
        expected += 1
    duplicates = len(seen) - len({n for n, _ in seen})
    if duplicates:
        out.append((_where(rule), f"{duplicates} duplicate step number(s) — order must be total"))
    return out


@check("DEPENDENCY_PRECEDES")
def _dependency_precedes(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Everything a row depends on must be built before it.

    This is what makes a build order a *topological* sort rather than a list. A mandate whose steps
    are individually well formed but whose dependency is scheduled later is not a sequence anyone
    can execute — and the defect is invisible in either row alone.

    A dependency that is not itself a step is a prerequisite from outside this build (an artifact
    that already exists), which is legitimate and deliberately not reported here.
    """
    column = rule.params["column"]
    depends_column = rule.params["depends_column"]
    order_column = rule.params["order_column"]
    none_markers = {str(m).strip() for m in rule.params.get("none_markers", ["—", "-", "NONE", ""])}

    position: dict[str, int] = {}
    rows = []
    for i, row in _rows(doc, rule):
        code = _cell(row, column)
        step = _cell(row, order_column)
        try:
            step_number = int(step)
        except ValueError:
            continue
        if code:
            position[code] = step_number
        rows.append((i, code, step_number, _cell(row, depends_column)))

    out = []
    for i, code, step_number, depends in rows:
        for part in (p.strip() for p in depends.replace(",", ";").split(";")):
            if not part or part in none_markers:
                continue
            prerequisite = position.get(part)
            if prerequisite is None:
                continue          # built outside this mandate — legitimate
            if prerequisite >= step_number:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{code!r} is step {step_number} but depends on {part!r} at step "
                    f"{prerequisite} — a prerequisite scheduled later is not a build order",
                ))
    return out


# Cross-phase checks -------------------------------------------------------------------------
#
# These read `doc.priors` — the upstream phase documents this one was handed. Every check above
# judges one document, which is sufficient while a defect lives inside it. It stops being
# sufficient at a handoff: nine phases pass work forward through `gov_projection`, and a phase that
# quietly drops an upstream commitment is well formed in isolation and wrong as a pipeline.
#
# The defect is only visible with both documents open, which is what makes these a different rule
# form rather than another register rule. They carry no phase names — which phase reads which is
# declared in that phase's rule set, exactly as an observation is.


def _prior_rows(doc: ParsedDocument, rule):
    """Content rows of the upstream register a cross-phase rule reads.

    Returns `(rows, unavailable)`. `unavailable` distinguishes the two ways a prior register can be
    absent, because they blame different people: a prior nobody supplied is the driver's omission,
    a register missing from a supplied prior is the upstream author's. Collapsing them would report
    a document defect for a missing command-line argument.
    """
    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]

    if not doc.has_prior(phase):
        return [], (
            f"{phase} was not supplied — this handoff is unchecked, and an unchecked handoff "
            f"looks identical to a preserved one"
        )
    block = doc.prior_register(phase, register)
    if block is None or block.table is None:
        return [], f"{phase} carries no readable {register!r} register to preserve"
    return _content_rows(block), None


def _cited_ordinals(value: str, register: str) -> set[int]:
    """Every `<register> #n` ordinal a citation cell names.

    A register id is unique across the pipeline, so the id alone identifies the upstream register
    and the stage qualifier a dossier writes in front of it (`S1 system_beliefs #2`) is redundant
    for matching. Requiring the qualifier would reject a correct citation over its prefix.

    A citation naming a section title rather than a register id is out of scope here — the seed is
    cited that way and the title is free-form, which `PRIOR_ROWS_PRESENT_BY_KEY` exists to handle.
    """
    return {
        int(n)
        for n in re.findall(rf"{re.escape(register)}\s*#\s*(\d+)", value)
    }


def _normalise(text: str) -> str:
    return " ".join(text.split())


@check("PRIOR_ROWS_CITED")
def _prior_rows_cited(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every row of an upstream register must be carried forward and cited here.

    Belief Preservation, stated as k of N: N rows were committed to upstream, k of them are cited
    downstream, and the rule is that k equals N. A belief nobody carried is not resolved — it is
    forgotten, and the dossier reports ADMISSIBLE over a question the change never answered.

    Reported per dropped row rather than as a count, because an author needs to know which
    commitment went missing, not how many did.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_where(rule), unavailable)]

    register = rule.params["prior_register"]
    phase = rule.params["prior_phase"]
    column = rule.params["citation_column"]
    key_column = rule.params.get("prior_key_column")

    cited: set[int] = set()
    for _, row in _rows(doc, rule):
        cited |= _cited_ordinals(_cell(row, column), register)

    out = []
    total = len(prior_rows)
    for ordinal, row in prior_rows:
        if ordinal in cited:
            continue
        subject = _normalise(_cell(row, key_column)) if key_column else ""
        out.append((
            f"{_where(rule)}",
            f"{phase} {register} #{ordinal} of {total} is carried nowhere in this register"
            + (f": {subject!r}" if subject else ""),
        ))
    return out


@check("PRIOR_ROW_MATCHES_CITED")
def _prior_row_matches_cited(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A row that cites an upstream row must still say what that row said.

    Projection Fidelity. `PRIOR_ROWS_CITED` proves nothing was dropped; it does not prove anything
    was preserved — a row can carry the citation forward and restate the claim as something the
    upstream phase never committed to, which is worse than dropping it, because the citation now
    lends the substitution a provenance it does not have.

    An ordinal naming no upstream row is reported here too: it is a citation that resolves to
    nothing, and the coverage check cannot see it — a phantom `#7` leaves all of #1..#3 uncited
    just the same.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_where(rule), unavailable)]

    register = rule.params["prior_register"]
    phase = rule.params["prior_phase"]
    column = rule.params["citation_column"]
    key_column = rule.params["key_column"]
    prior_key_column = rule.params["prior_key_column"]

    upstream = {ordinal: row for ordinal, row in prior_rows}

    out = []
    for i, row in _rows(doc, rule):
        for ordinal in sorted(_cited_ordinals(_cell(row, column), register)):
            if ordinal not in upstream:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"cites {register} #{ordinal}, and {phase} declares only "
                    f"{len(upstream)} row(s) there",
                ))
                continue
            here = _normalise(_cell(row, key_column))
            there = _normalise(_cell(upstream[ordinal], prior_key_column))
            if here != there:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"restates {register} #{ordinal} as {here!r}, which {phase} declared as "
                    f"{there!r} — a citation is not a licence to change the claim",
                ))
    return out


@check("PRIOR_IDENTITIES_COVERED")
def _prior_identities_covered(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Two registers naming artifact identities must name the same ones.

    The handoffs above are checked row by row, because a belief is a claim and claims are matched by
    what they say. From P4 on, a dossier stops citing upstream rows ordinally and starts naming
    artifacts, so there is nothing to match a row against — but there is something better. An
    identity is exact. Two registers that both name identities are reconciled as sets, and the
    citation idiom stops mattering entirely.

    `require` says which way the containment runs, and the two directions are different defects:

        prior_in_here   something the upstream phase committed to went unscheduled
        here_in_prior   something is scheduled that no upstream phase ever designed

    Both are silent in either document alone. A build order made entirely of well-formed rows can
    omit an artifact the design declared, and a design listing every artifact can be missing one the
    mandate invented — and each document is internally consistent throughout.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_where(rule), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    require = rule.params["require"]
    if require not in ("prior_in_here", "here_in_prior"):
        raise KeyError(f"{rule.id}: 'require' must be prior_in_here or here_in_prior, not {require!r}")

    # A provisional code and the FQDN it is later bound to are the same identity stated at two rungs
    # of the purity ladder — P5 must not namespace one, P7 must. Comparing the raw cells would
    # report every code unbound, so the rule declares which representation it is matching on.
    match_on = rule.params.get("match_on", "exact")
    if match_on not in ("exact", "bare_code"):
        raise KeyError(f"{rule.id}: 'match_on' must be exact or bare_code, not {match_on!r}")
    normalise = (lambda v: v.split("::")[-1]) if match_on == "bare_code" else (lambda v: v)

    there = {
        normalise(identity): ordinal
        for ordinal, row in prior_rows
        if (identity := _cell(row, rule.params["prior_column"]))
    }
    here = {
        normalise(identity): i
        for i, row in _rows(doc, rule)
        if (identity := _cell(row, rule.params["column"]))
    }

    if require == "prior_in_here":
        return [
            (f"{_where(rule)}",
             f"{identity} is declared at {phase} {register} #{ordinal} and appears nowhere here")
            for identity, ordinal in sorted(there.items(), key=lambda kv: kv[1])
            if identity not in here
        ]
    return [
        (f"{_where(rule)} row {i}",
         f"{identity} appears in no {phase} {register} row — it was never designed")
        for identity, i in sorted(here.items(), key=lambda kv: kv[1])
        if identity not in there
    ]


@check("PRIOR_ROWS_PRESENT_BY_KEY")
def _prior_rows_present_by_key(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every row of an upstream register must reappear here, matched on what it says.

    The third way two documents are compared, and the one that needs no idiom at all.

    `PRIOR_ROWS_CITED` matches on an ordinal citation, which works from P1 to P3 because those
    dossiers cite `S1 system_beliefs #2`. It cannot work against the seed: the seed is cited by
    section title, and the title is free-form — CR-0 writes `CR seed §5 Beliefs #1` where CR-1
    writes `System Beliefs #1`, both abbreviating "Existing-System Beliefs — Requiring
    Verification". A label that has already drifted between two change requests is not something to
    match on, and blessing both spellings would only invite a third.

    `PRIOR_IDENTITIES_COVERED` matches on an identity, which is exact but only exists once a phase
    is naming artifacts.

    Between them sits a register that is restated in business language: the row is the same claim,
    written the same way, in a register of the same name. So match on the claim.

    Coverage only, deliberately. A row here that is in no upstream register is an *addition*, and
    the phases that restate legitimately elaborate — splitting one outcome into two is not a defect.
    Loss is the silent half: a change request missing an acceptance criterion is a perfectly
    well-formed change request, and that criterion is what the finished composition is later
    validated against.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_where(rule), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    prior_key = rule.params["prior_key_column"]
    key = rule.params["key_column"]

    # A phase may owe a carry for only some upstream rows: every capability P5 declares IN_SCOPE
    # must be placed at P6, while a DEFERRED one is under no such obligation. The filter reads the
    # upstream row, because that is where the obligation is declared.
    gate_column = rule.params.get("prior_only_when_column")
    gate_value = rule.params.get("prior_only_when_value")

    here = {_normalise(_cell(row, key)) for _, row in _rows(doc, rule)}

    out = []
    total = len(prior_rows)
    for ordinal, row in prior_rows:
        if gate_column and _cell(row, gate_column) != gate_value:
            continue
        claim = _normalise(_cell(row, prior_key))
        if not claim or claim in here:
            continue
        out.append((
            _where(rule),
            f"{phase} {register} #{ordinal} of {total} is restated nowhere here: {claim!r}",
        ))
    return out
