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

from transformation.design.evaluate import Block, ParsedDocument

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
EMPTINESS_SENTINEL = "NONE IDENTIFIED"
# Public because the P1 projection must emit the same marker it will later be judged against; a
# second spelling of it in project.py is a second declaration that can drift from this one.


def is_sentinel(row: dict[str, str]) -> bool:
    """True when a row is the declared-empty marker rather than content."""
    values = [str(v).strip() for v in row.values()]
    if not values:
        return False
    return values[0].upper() == EMPTINESS_SENTINEL and not any(values[1:])


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
        if not is_sentinel(row)
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
    minimum = int(rule.params.get("minimum", 1))
    rows = len(block.table.rows)
    if rows < minimum:
        detail = (
            "section requires at least one row"
            if minimum == 1
            else f"section declares {rows} row(s); {minimum} are required"
        )
        return [(_where(rule), detail)]
    return []


@check("TABLE_ROW_COUNT")
def _table_row_count(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """How many rows a register may carry.

    `TABLE_HAS_ROWS` already asserts a floor — a declared register that is empty asserts nothing.
    Nothing asserted a ceiling, so a register meant to carry one answer could carry three
    contradictory ones and no rule anyone could write would notice. That is not a rule nobody
    wrote; it is a rule nobody *could* write, which is why this is a way of judging rather than a
    rule.

    `maximum` is the half that was missing; `minimum` is accepted too so a register owing an exact
    count can declare one thing rather than two rules that could disagree.

    Adding this changes no verdict. A ceiling is a judgement about what a particular register
    means, made per register, and this kind ships applied to none.
    """
    block = _block(doc, rule)
    if block is None or block.table is None:
        return []
    rows = len(block.table.rows)
    minimum = rule.params.get("minimum")
    maximum = rule.params.get("maximum")
    out = []
    if minimum is not None and rows < int(minimum):
        out.append((_where(rule), f"register carries {rows} row(s); at least {minimum} required"))
    if maximum is not None and rows > int(maximum):
        # A rule may say what its own ceiling means; a generic message cannot know why one row.
        detail = rule.params.get("detail")
        out.append((
            _where(rule),
            f"register carries {rows} row(s); at most {maximum} permitted"
            + (f" — {detail}" if detail else ""),
        ))
    return out


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


@check("ROW_ABSENT_WHEN")
def _row_absent_when(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A register may not carry a row in a given state.

    `CELL_IN_VOCABULARY` says which values a column may hold; this says which of them the document
    may still be carrying when it is judged. The difference matters for a register whose whole
    purpose is to hold rows that must eventually be gone — an open question is well-formed and
    still not something a downstream phase may consume.
    """
    out = []
    column = rule.params["column"]
    value = str(rule.params["value"]).strip().upper()
    for i, row in _rows(doc, rule):
        if _cell(row, column).strip().upper() == value:
            out.append((f"{_where(rule)} row {i}", rule.params["detail"]))
    return out


# A cell that declares the question unanswered rather than answering it. Matched at the head of a
# cell, so `UNRESOLVED — whether an edition is a Book` fires and a sentence that merely mentions an
# unresolved question does not. `PENDING` is deliberately absent: in a projection table it means
# scheduled, not unknown.
GOVERNED_HOLE_MARKERS = (
    "UNRESOLVED",
    "UNDECIDED",
    "UNKNOWN",
    "TBD",
    "TBC",
    "TO BE DETERMINED",
    "TO BE DECIDED",
    "TO BE CONFIRMED",
    "NOT YET DECIDED",
    "OPEN QUESTION",
    "???",
)


@check("UNRESOLVED_MARKER_ABSENT")
def _unresolved_marker_absent(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """No register may hedge a cell instead of stating it.

    Document-wide rather than per-register: a hole can open in any cell of any register, and a rule
    that had to name the columns in advance would only ever catch the holes someone had already
    seen. The registers where an open question is the content — a clarification register, a gap
    register — are declared exempt by the phase that owns them.

    An unanswered question is not a value. Left in a register it is *determined* as far as every
    later phase can tell, which is how a design whose central business question was never settled
    reached execution reporting admissible at every gate.
    """
    out = []
    exempt = {r.lower() for r in rule.params.get("exempt", ())}
    markers = tuple(m.upper() for m in rule.params.get("markers", GOVERNED_HOLE_MARKERS))
    for entry in doc.registers:
        register_id = str(entry.get("id") or "")
        if register_id.lower() in exempt or not entry.get("columns"):
            continue
        rows = [dict(r) for r in (entry.get("rows") or [])]
        for i, row in enumerate(rows, start=1):
            if is_sentinel(row):
                continue
            for column, raw in row.items():
                value = str(raw).strip().strip("*_`").upper()
                marker = next((m for m in markers if value.startswith(m)), None)
                if marker:
                    out.append(
                        (
                            f"{register_id} row {i}",
                            rule.params["detail"].format(marker=marker, column=column),
                        )
                    )
    return out


@check("CELL_MATCHES")
def _cell_matches(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every non-empty cell in a column must match a declared pattern.

    Emptiness is CELL_NOT_EMPTY's concern — a rule that checked both would report two findings for
    one defect and make the cause ambiguous.
    """
    out = []
    column = rule.params["column"]
    pattern = re.compile(rule.params["pattern"])
    # A pattern that applies to only some rows says so, the way every other gated check does. A
    # naming rule for one artifact family would otherwise have to be a check kind of its own.
    gate_column = rule.params.get("only_when_column")
    gate_value = rule.params.get("only_when_value")
    for i, row in _rows(doc, rule):
        if gate_column and _cell(row, gate_column).strip().upper() != str(gate_value).upper():
            continue
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
            f"{value!r} contains no citation naming a declared register or recognised source. "
            f"A citation names a register this phase may cite — {_examples(known)} — "
            f"or one of {', '.join(repr(x) for x in literal)}, "
            f"or an artifact already in the baseline, by exact identity "
            f"(e.g. 'blockchain::WF_REGISTER_ACTOR_V0'). "
            f"A register may be named by its id ('known_facts #14') or, prefixed by its phase, "
            f"by its section ('S1 §4 Known Facts #14'). Separate several citations with ';'",
        ))
    return out



def _examples(known: set[str] | list[str], count: int = 3) -> str:
    """A few register ids the author may actually cite, so a diagnostic teaches the grammar.

    A rule that says only what is wrong makes an author read the checker to learn what is right.
    """
    shown = sorted(known)[:count]
    return ", ".join(f"'{r} #1'" for r in shown) + (", …" if len(known) > count else "")


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

    `exempt_prefixes` names values that are terminals by construction rather than identities. A
    workflow's topology legitimately routes to `EXIT_REJECTED`, which is a graph terminal and never
    an artifact — the rule had simply never met one, because CR-1 declared no EXIT rows until its
    topology was completed.
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
            if is_sentinel(row):
                continue
            value = _cell(row, column)
            if value:
                known.add(value.strip())
    target = " or ".join(targets)
    exempt = tuple(rule.params.get("exempt_prefixes") or ())

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
            if exempt and part.startswith(exempt):
                continue
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


@check("NODE_INPUT_BOUND")
def _node_input_bound(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A workflow node must be handed every input its contract requires.

    A contract declares what it accepts; a workflow node declares what it is handed. Nothing checked
    that the second covered the first, so extending a contract to need a new input left its callers
    silently short — the contract was well formed, the workflow was well formed, and the value
    arrived as null at execution. Two contracts were extended that way in one change, and both
    designs were admissible over the full rule set and complete at 100%.

    Only required inputs are checked. An optional one absent is a declaration that the node does not
    supply it, which is what optional means.
    """
    topology = rule.params["topology_register"]
    fields = rule.params["fields_register"]

    declared: dict[str, set[str]] = {}
    for _, row in _content_rows(doc.register(fields)):
        if (_cell(row, "Direction").upper() != "INPUT"
                or _cell(row, "Required").upper() != "YES"):
            continue
        declared.setdefault(_bare_identity(_cell(row, "Artifact")), set()).add(_cell(row, "Field"))

    # A contract this design authors declares its interface above. One it *reuses* declares nothing —
    # the contract already exists, so there is nothing for the design to restate — and that silence
    # was read as "requires nothing". Every instance of this defect has been the same shape: a
    # workflow reusing another subdomain's contract and handing it nothing, admissible over the full
    # rule set, complete at 100%, and discovered only when the act ran and the contract received
    # nulls. Three of them in one change.
    #
    # Unioned rather than overridden. A design extending a contract states the input it adds while
    # the composition still requires the ones it had, and both must be bound; requiring too much is
    # a finding an author can answer, requiring too little is one nobody sees.
    observation = rule.params.get("observation")
    for entry in (doc.observed.get(observation) or []) if observation else []:
        if not isinstance(entry, dict):
            continue
        required = {name for name, spec in (entry.get("inputs") or {}).items()
                    if isinstance(spec, dict) and spec.get("required")}
        if required:
            declared.setdefault(_bare_identity(str(entry.get("contract"))), set()).update(required)

    bound: dict[tuple[str, str], set[str]] = {}
    for _, row in _rows(doc, rule):
        if _cell(row, "Direction").upper() != "INPUT":
            continue
        key = (_bare_identity(_cell(row, "Owner")), _bare_identity(_cell(row, "Step")))
        bound.setdefault(key, set()).add(_cell(row, "Field"))

    out = []
    for i, row in _content_rows(doc.register(topology)):
        if _cell(row, "Node Type").upper() != "CC":
            continue
        workflow = _bare_identity(_cell(row, "Workflow"))
        node = _bare_identity(_cell(row, "Node"))
        missing = sorted(declared.get(node, set()) - bound.get((workflow, node), set()))
        for field in missing:
            out.append((
                f"{topology} row {i}",
                f"{workflow} hands {node} no {field!r}, which that contract requires",
            ))
    return out


@check("BINDING_SOURCE_REACHABLE")
def _binding_source_reachable(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A source rooted at another node must name a node the workflow actually runs.

    `BINDING_SOURCE_UNROOTED` proves a source is a reference rather than a literal. It cannot prove
    the reference resolves: a source naming a contract this workflow never reaches is well-rooted,
    well-formed, and null at execution. One such binding existed in a design that passed every rule.
    """
    topology = rule.params["topology_register"]
    pattern = re.compile(rule.params["pattern"])

    nodes: dict[str, set[str]] = {}
    for _, row in _content_rows(doc.register(topology)):
        nodes.setdefault(_bare_identity(_cell(row, "Workflow")), set()).add(
            _bare_identity(_cell(row, "Node")))

    out = []
    for i, row in _rows(doc, rule):
        owner = _bare_identity(_cell(row, "Owner"))
        if owner not in nodes:
            continue
        for named in sorted(set(pattern.findall(_cell(row, "Bound To")))):
            if _bare_identity(named) not in nodes[owner]:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"source names {named!r}, which {owner} never runs — well-rooted and unreachable",
                ))
    return out


@check("PRIOR_PROSE_CARRIED")
def _prior_prose_carried(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A narrative register carried from an upstream phase, inherited or explicitly superseded.

    Preservation elsewhere is row-keyed, and a paragraph has no key. That is why the one register
    the pipeline could never derive — the subdomain purpose, human-authored once at P0 — was the
    one thing it dropped: P1 through P4 have nowhere to put it, and P5 wrote a fresh paragraph in
    its place. A second author's paragraph is not the business's statement, and nothing recorded
    that the substitution had happened.

    The register itself declares which it is. `INHERITED` means the prose is the prior's, and the
    two must match once whitespace is normalised. `REFINED` means this phase deliberately says more,
    and must state what it added — a disposition that permitted silence would be indistinguishable
    from the loss it exists to prevent.
    """
    phase = rule.params["prior_phase"]
    prior_register = rule.params["prior_register"]
    inherited = str(rule.params.get("inherited_value", "INHERITED")).upper()

    if not doc.has_prior(phase):
        return [(
            _where(rule),
            f"{phase} was not supplied — this handoff is unchecked, and an unchecked handoff "
            f"looks identical to a preserved one",
        )]
    prior = doc.prior_register(phase, prior_register)
    if prior is None:
        return [(_where(rule), f"{phase} carries no {prior_register!r} register to carry forward")]

    rows = _rows(doc, rule)
    if not rows:
        return [(_where(rule), "no disposition declared — say whether the prose is inherited or refined")]

    out = []
    column = rule.params["column"]
    carried = doc.register(rule.params["prose_register"])
    for i, row in rows:
        if _cell(row, column).strip().upper() != inherited:
            continue
        if carried is None:
            out.append((f"{_where(rule)} row {i}", "the register it declares a disposition for is absent"))
            continue
        if _normalise(carried.text()) != _normalise(prior.text()):
            out.append((f"{_where(rule)} row {i}", rule.params["detail"]))
    return out


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


def _key_columns(declared: str | list[str]) -> list[str]:
    """A key column declaration, as a list.

    Some registers are keyed by one column and some by several: an acceptance criterion is unique on
    its own text, while a lifecycle state is unique only as `Object` + `State` — `Registered` appears
    once per object. Declaring a single column for those would compare a book's row against a copy's
    and call a dropped row present.
    """
    return [declared] if isinstance(declared, str) else list(declared)


def _claim(row: dict, columns: list[str]) -> str:
    """What a row asserts, as one comparable string across its key columns."""
    return " · ".join(_normalise(_cell(row, c)) for c in columns)


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

    # A prior row may not oblige anything. A subdomain a change merely reads is named upstream and
    # authors nothing, so the obligation is gated on what the upstream row says about itself rather
    # than on its presence. Absent the gate every prior row obliges, which is the prior behaviour.
    gate_column = rule.params.get("prior_only_when_column")
    gate_values = rule.params.get("prior_only_when_values")
    # A family gate, where the obligation is about what kind of artifact a row names rather than
    # what the row says about it. `existing_inventory` carries no Family column — an artifact
    # carried over from the composition states its family in its own identity, which is the only
    # place it can, because the design assigns it no new code. So the prefix is the family.
    gate_prefixes = rule.params.get("prior_only_when_prefixes")

    def obliges(row) -> bool:
        if gate_prefixes:
            code = _cell(row, rule.params["prior_column"]).split("::")[-1]
            if not any(code.startswith(prefix) for prefix in gate_prefixes):
                return False
        if not gate_column:
            return True
        return _cell(row, gate_column) in gate_values

    there = {
        normalise(identity): ordinal
        for ordinal, row in prior_rows
        if obliges(row) and (identity := _cell(row, rule.params["prior_column"]))
    }
    here = {
        normalise(identity): i
        for i, row in _rows(doc, rule)
        if (identity := _cell(row, rule.params["column"]))
    }

    # `union` widens the local side across more than one register, because a commitment can be
    # honoured in more than one place. A change request that *extends* an existing artifact honours
    # its provisional code in the existing inventory, not by authoring a new identity — and the
    # first CR to extend anything found that no P7 could satisfy both directions of the closure at
    # once. Declared per rule and gated per register, so a widening states which rows count.
    #
    # Only ever declared on `prior_in_here`. The reverse direction asks a different question — was
    # this authored without intent — and an extended artifact may legitimately be substrate the
    # business never named, which is why a union there would refuse correct dossiers.
    for spec in rule.params.get("union", ()):
        block = doc.register(spec["register"])
        gate_column = spec.get("only_when_column")
        gate_value = str(spec.get("only_when_value", "")).strip().upper()
        for i, row in _content_rows(block):
            if gate_column and _cell(row, gate_column).strip().upper() != gate_value:
                continue
            identity = _cell(row, spec["column"])
            if identity:
                here.setdefault(normalise(identity), i)

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
    prior_key = _key_columns(rule.params["prior_key_column"])
    key = _key_columns(rule.params["key_column"])

    # A phase may owe a carry for only some upstream rows: every capability P5 declares IN_SCOPE
    # must be placed at P6, while a DEFERRED one is under no such obligation. The filter reads the
    # upstream row, because that is where the obligation is declared.
    gate_column = rule.params.get("prior_only_when_column")
    gate_value = rule.params.get("prior_only_when_value")

    here = {_claim(row, key) for _, row in _rows(doc, rule)}

    out = []
    total = len(prior_rows)
    for ordinal, row in prior_rows:
        if gate_column and _cell(row, gate_column) != gate_value:
            continue
        claim = _claim(row, prior_key)
        if not claim or claim in here:
            continue
        out.append((
            _where(rule),
            f"{phase} {register} #{ordinal} of {total} is restated nowhere here: {claim!r}",
        ))
    return out


@check("REGISTER_COVERS_REGISTER")
def _register_covers_register(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every row of one register must be accounted for in another register of the same document.

    The cross-phase kinds above check that a handoff between two documents preserved something. This
    is the same question asked *inside* one document, and it is the one the pipeline never asked: P7
    declared six workflows and gave three of them a topology, declared eight capability contracts and
    composed five, and was ADMISSIBLE at fifty-seven rules — because every rule judged the rows that
    were present and nothing required the rows that were not.

    The information already had somewhere to live. What was missing was any obligation that it
    exist, which is a deficiency in the language's **constraints** rather than in its expressiveness.

    Filtered on the source row, because the obligation usually applies to one artifact family: a
    workflow needs a topology, a capability contract needs a composition, and neither needs the
    other's.
    """
    source = rule.params["source_register"]
    block = doc.register(source)
    if block is None or block.table is None:
        return [(
            _where(rule),
            f"{source!r} is absent, so nothing establishes what this register must cover",
        )]

    gate_column = rule.params.get("only_when_column")
    gate_value = rule.params.get("only_when_value")
    source_column = rule.params["source_column"]

    # A gate on the covering side too, because a register may account for several kinds of fact in
    # one table. `artifact_properties` carries every scalar an artifact declares, so a rule asking
    # "is this artifact named as superseded" must read only the rows that say so — otherwise any
    # cell whose value happened to match would answer for it, and the rule would pass on a
    # coincidence.
    covered_gate_column = rule.params.get("covered_only_when_column")
    covered_gate_value = rule.params.get("covered_only_when_value")

    covered = {
        _bare_identity(_cell(row, rule.params["column"]))
        for _, row in _rows(doc, rule)
        if not covered_gate_column or _cell(row, covered_gate_column) == covered_gate_value
    }

    out = []
    for ordinal, row in _content_rows(block):
        if gate_column and _cell(row, gate_column) != gate_value:
            continue
        key = _cell(row, source_column)
        if not key or _bare_identity(key) in covered:
            continue
        out.append((
            f"{_where(rule)}",
            f"{key} is declared at {source} #{ordinal} and this register says nothing about it"
            + (f" ({gate_column} {gate_value})" if gate_column else ""),
        ))
    return out


def _bare_identity(value: str) -> str:
    """An identity without its namespace.

    One register writes `book_library_mgmt::WF_SEARCH_CATALOG_V0` and another writes the same
    workflow as a bare code; both name one artifact, and a coverage check that distinguished them
    would report every row uncovered.
    """
    return _normalise(value).split("::")[-1]


@check("BINDING_SOURCE_PUBLISHED")
def _binding_source_published(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """An output binding must read a field its step's operation actually publishes.

    A step names its outputs in the contract's own vocabulary — `staff_record`, `book_details` — and
    the binding says where each comes from. The *name* is the design's to choose; the *source* is
    not. `capability_result.value` is a claim about what the operation yields, and only the
    composition can settle it.

    **This would not have caught the authorization defect**, and that is worth stating plainly.
    `authorized` was bound to `capability_result.exists`, and `EXISTS` does publish `exists` — the
    binding was structurally perfect and semantically wrong, because the question asked was whether
    a record existed when the question meant was whether a person was entitled. No structural rule
    reaches that. What this catches is a source that does not exist at all: a fabricated field, a
    typo, or a binding left pointing at an operation that has since changed its surface.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _where(rule),
            "no capability surface was observed — a binding source cannot be checked against "
            "operations nobody published",
        )]

    surface: dict[str, dict[str, set[str]]] = {}
    for entry in published:
        if not isinstance(entry, dict):
            continue
        surface[str(entry.get("capability"))] = {
            op: {str(f) for f in (spec.get("output") or [])}
            for op, spec in (entry.get("operations") or {}).items()
        }

    # Which capability and operation each CS step invokes, addressed the way a binding addresses it.
    steps: dict[tuple[str, str], tuple[str, str]] = {}
    composition = doc.register(rule.params["step_register"])
    if composition and composition.table:
        for row in composition.table.rows:
            if _cell(row, "Kind") != "CS":
                continue
            steps[(_bare_identity(_cell(row, "CC Code")), _cell(row, "Step Name"))] = (
                _cell(row, "Capability"), _cell(row, "Operation"))

    out = []
    prefix = "capability_result."
    for i, row in _rows(doc, rule):
        if _cell(row, "Direction") != "OUTPUT":
            continue
        bound = _cell(row, "Bound To")
        if not bound.startswith(prefix):
            continue
        step = steps.get((_bare_identity(_cell(row, "Owner")), _cell(row, "Step")))
        if step is None:
            continue                      # a CT step, or a workflow node — a different surface
        capability, operation = step
        declared = surface.get(capability, {}).get(operation)
        if declared is None:
            continue                      # the operation itself is another rule's business
        field = bound[len(prefix):].split(".")[0]
        if field not in declared:
            out.append((
                f"{_where(rule)} row {i}",
                f"{operation} on {capability.split('::')[-1]} publishes {sorted(declared)}, "
                f"not {field!r} — a binding cannot read a field the operation never yields",
            ))
    return out


@check("BINDING_SOURCE_ROOTED")
def _binding_source_rooted(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A source that names a place must be rooted in a scope execution offers.

    `BINDING_SOURCE_PUBLISHED` asks whether a source reads a field that exists. This asks the prior
    question: whether the source is a reference at all. A binding cell is either a literal the design
    chose — `CATALOG_OPERATIONS`, `false`, `REGISTER_BOOK` — or a reference to somewhere a value comes
    from, and only the roots in `roots` are places. Nothing distinguished the two, so a reference
    written without its root was read as a literal by every layer beneath: the renderer emitted the
    string verbatim, the compiler accepted it, and the runtime handed the step its own binding text.

    CR-1 wrote `results.check_existing.capability_result.exists` and worked. Its re-run wrote
    `assemble_book_record.book_record` — the same intent, the root dropped — and every workflow
    reported SUCCESS while writing the string `"assemble_book_record.book_record"` into the store as
    the book. Construction completeness was 100%: a determined binding to a literal is still
    determined, which is exactly why this has to be a design rule and not a construction one.

    Two shapes are caught. A dotted source whose first segment is not a root names a scope that does
    not exist. A *scope* root written bare is a reference whose field was never written — `payload`
    alone addresses no value. `result_status` is the exception and is not a scope: it is the step's
    status, a scalar with nothing under it, and standing alone is its only correct form. A literal is
    left alone: no dots, or an FQDN, or a number, or an inline object the design states outright.
    """
    roots = rule.params["roots"]
    scopes = [r for r in roots if r not in rule.params["value_roots"]]

    out = []
    for i, row in _rows(doc, rule):
        bound = _cell(row, "Bound To")
        if not bound or bound in ("—", "-"):
            continue                      # BINDING_WITHOUT_SOURCE owns the empty cell
        if bound in scopes:
            out.append((
                f"{_where(rule)} row {i}",
                f"{bound!r} is a scope, not a value — a source rooted in {bound!r} must name the "
                f"field it reads, or construction binds the step to the word itself",
            ))
            continue
        if "." not in bound or "::" in bound or bound.startswith(("{", "[", '"', "'")):
            continue                      # a literal the design chose, not a reference
        if _is_number(bound):
            continue
        root = bound.split(".", 1)[0]
        if root not in roots:
            out.append((
                f"{_where(rule)} row {i}",
                f"{bound!r} is rooted in {root!r}, which execution does not offer — a source names "
                f"one of {sorted(roots)}, or construction reads it as the literal string {bound!r}",
            ))
    return out


def _is_number(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    return True


@check("STORE_PATH_MATCHES_STORAGE")
def _store_path_matches_storage(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A store's path must carry the extension its storage capability writes.

    The capabilities do not all write the same file format: `CS_MUTABLE_JSON_V0` writes one JSON
    object keyed by store key, while `CS_REGISTRY_V0` and `CS_APPENDONLY_JSONL_V0` write JSON Lines.
    A path is free naming and nothing derived it from the binding, so the catalog named two registry
    stores `.json` — files that could never be parsed as the document their extension advertised.

    It cost nothing at compile time and nothing at run time, because the runtime opens the path it is
    given and neither reads nor cares about the suffix. It cost a reader, and the tooling a reader
    writes: the first thing that tried to `json.loads` a store crashed on the second line.

    The mapping is declared in `formats` rather than derived from the capability, because a CS states
    its format in the prose of its configuration schema — `path: Filesystem path to JSONL registry
    file` — and nothing machine-readable says it. Closing *that* gap is a change to the CS
    declaration substrate, and this rule is the cheap half.
    """
    formats: dict[str, str] = rule.params["formats"]

    out = []
    for i, row in _rows(doc, rule):
        storage, path = _cell(row, rule.params["storage_column"]), _cell(row, rule.params["path_column"])
        if not storage or not path:
            continue
        expected = formats.get(_bare_identity(storage))
        if expected is None:
            continue                      # a capability this rule states no format for
        if not path.endswith(expected):
            out.append((
                f"{_where(rule)} row {i}",
                f"{storage.split('::')[-1]} writes {expected} and the path ends {path[path.rfind('.'):]!r} "
                f"— a store's name must not advertise a format its capability does not write",
            ))
    return out


@check("ROWS_CONFINED_TO_PRIOR")
def _rows_confined_to_prior(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """No row here may assert something the upstream register does not.

    `PRIOR_ROWS_PRESENT_BY_KEY` is coverage — it catches the row that went missing. This is the
    other direction, and the hole it closes was demonstrable: a change request carrying
    "books must be shelved by Dewey Decimal number", a business fact no seed states, cited to a
    seed row that does not exist, was ADMISSIBLE over 131 rules. Loss was governed; invention was
    not.

    Only a phase whose contract is *restatement* may carry this rule. P1 interrogates and does not
    author, so its business registers are confined to the seed's; a phase that legitimately adds
    (P2 projects, P3 decides) must not be judged this way.

    It also narrows something the coverage rule deliberately permitted — elaborating one upstream
    row into two. That freedom is what let a business fact enter at P1 wearing the clothes of an
    elaboration. Elaboration now belongs at P0, in the seed, where a person owns the wording.
    """
    prior_rows, unavailable = _prior_rows(doc, rule)
    if unavailable:
        return [(_where(rule), unavailable)]

    phase = rule.params["prior_phase"]
    register = rule.params["prior_register"]
    prior_key = _key_columns(rule.params["prior_key_column"])
    key = _key_columns(rule.params["key_column"])

    upstream = {_claim(row, prior_key) for _, row in prior_rows}

    out = []
    for i, (_, row) in enumerate(_rows(doc, rule), start=1):
        claim = _claim(row, key)
        if not claim or claim in upstream:
            continue
        out.append((
            f"{_where(rule)} row {i}",
            f"states what {phase} {register} does not: {claim!r} — this phase restates business "
            f"content, so a new claim belongs upstream where a person owns it",
        ))
    return out


def _prior_section_registers(phase: str) -> dict[str, str]:
    """Section number → register id, for a prior phase's template.

    The seed is cited by section, not by register id: `CR seed §4 Known Facts #1`. The title in the
    middle is free-form and has already drifted between two change requests, but the number is
    declared by the template, so the number is what resolves.
    """
    from transformation.design.template_reader import load

    return {
        r.section_number: r.id
        for r in load(phase).registers
        if r.section_number is not None
    }


@check("CITATION_ROW_UNRESOLVED")
def _citation_row_unresolved(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """An ordinal citation must name a row that exists.

    `SOURCE_FINDING_UNRESOLVED` checks that a citation names a register some phase declares, which
    catches a fabricated register id and nothing else: `CR seed §4 Known Facts #99` named a real
    register and a row that was never written, and passed.

    Resolution accepts either idiom, because both are in use across the tested dossiers — a prior
    phase's section (`§4 … #1`) or a register id (`S1 system_beliefs #2`) — and looks in the priors
    supplied and in this document's own registers. A citation carrying no ordinal is out of scope:
    every downstream phase from P3 on cites by register name alone, and 162 of P7's citations are
    of that form. Requiring ordinals everywhere is a separate decision from refusing a citation
    that points at nothing.
    """
    column = rule.params["column"]

    resolvable: dict[str, int] = {}
    for entry in doc.registers:
        rid = entry["id"] if isinstance(entry, dict) else entry.id
        block = doc.register(rid)
        if block is not None and block.table is not None:
            resolvable[rid] = len(_content_rows(block))

    sections: dict[str, dict[str, str]] = {}
    for phase in doc.priors:
        sections[phase] = _prior_section_registers(phase)
        for register, count in _prior_register_sizes(doc, phase).items():
            resolvable.setdefault(f"{phase}:{register}", count)

    out = []
    for i, (_, row) in enumerate(_rows(doc, rule), start=1):
        value = _cell(row, column)
        if not value:
            continue
        for register, ordinal in _citations(value, sections):
            # A register id names this document's register *and* the prior's — `acceptance_criteria`
            # exists at both rungs — so the ordinal resolves against whichever candidate can hold
            # it. Checking only the nearest one reported a defect against a P1 row that correctly
            # cited the seed's ninth criterion while this document carried eight.
            candidates = [
                v for k, v in resolvable.items()
                if k == register or k.endswith(f":{register}")
            ]
            size = max(candidates, default=None)
            if size is None or not 1 <= ordinal <= size:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"cites {register} #{ordinal}, which "
                    + ("names no register any phase declares" if size is None
                       else f"does not exist — that register carries {size} row(s)"),
                ))
    return out


def _prior_register_sizes(doc: ParsedDocument, phase: str) -> dict[str, int]:
    """How many content rows each register of a supplied prior carries."""
    from transformation.design.template_reader import load

    sizes: dict[str, int] = {}
    for r in load(phase).registers:
        block = doc.prior_register(phase, r.id)
        if block is not None and block.table is not None:
            sizes[r.id] = len(_content_rows(block))
    return sizes


def _citations(value: str, sections: dict[str, dict[str, str]]) -> list[tuple[str, int]]:
    """Every (register, ordinal) pair a citation cell names, in either idiom.

    The register-id idiom must match a declared id and nothing else. Matching any lowercase run
    before a `#` read `Business Vocabulary #1` as a citation of `ocabulary` — a register no phase
    declares — and reported a defect against a correct citation.
    """
    from transformation.design.derive import _all_declared_registers

    found: list[tuple[str, int]] = []
    for number, ordinal in re.findall(r"§\s*(\d+)[^#|]*#\s*(\d+)", value):
        for mapping in sections.values():
            register = mapping.get(number)
            if register:
                found.append((register, int(ordinal)))
                break
    for register in _all_declared_registers():
        for ordinal in re.findall(rf"(?<![A-Za-z_]){re.escape(register)}\s*#\s*(\d+)", value):
            found.append((register, int(ordinal)))
    return found


@check("STEP_OPERATION_PUBLISHED")
def _step_operation_published(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A step must name an operation its capability actually offers.

    `STEP_CONSUMES_PUBLISHED` skips a step whose operation it cannot resolve, with the note that the
    operation is another rule's business. That rule did not exist, and its absence was not one gap
    but three: an unresolvable operation makes the consumes check, the binding-source check and this
    one all pass in silence, because each of them looks the operation up and finds nothing to
    compare against.

    What it cost: a design declared two clock reads as `READ` where the clock offers only `NOW`, and
    bound their results to a field called `now` where the operation publishes `timestamp`. Admissible
    over a hundred and thirty-four rules, one hundred per cent construction-complete, and refused by
    the compiler at S4 on an invariant the design layer had every fact needed to check.

    A capability absent from the surface is reported rather than skipped. A side effect is substrate
    a business change reuses and never authors, so one the composition does not publish is a name
    that resolves to nothing.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _where(rule),
            "no capability surface was observed — a step's operation cannot be checked against "
            "operations nobody published",
        )]

    offered = {
        str(entry.get("capability")): set(entry.get("operations") or {})
        for entry in published
        if isinstance(entry, dict)
    }

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, "Kind") != "CS":
            continue
        capability, operation = _cell(row, "Capability"), _cell(row, "Operation")
        if capability not in offered:
            out.append((f"{_where(rule)} row {i}",
                        f"{capability!r} publishes no capability surface — a side effect is reused, "
                        f"never authored, so one the composition does not carry names nothing"))
            continue
        if operation and operation not in offered[capability]:
            out.append((f"{_where(rule)} row {i}",
                        f"{capability} offers no operation {operation!r} — it publishes "
                        f"{', '.join(sorted(offered[capability])) or 'none'}"))
    return out


@check("STEP_CONSUMES_PUBLISHED")
def _step_consumes_published(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A step must hand its operation fields the operation accepts.

    The mirror of `BINDING_SOURCE_PUBLISHED`, and the half that was missing. That rule asks whether a
    binding *reads* a field the operation yields; nothing asked whether a step *hands* the operation a
    field it takes.

    The gap was not hypothetical. CR-1's catalog search declared a `LIST` step consuming `filter`,
    and `LIST` declares no inputs at all — it returns every key in the store. The design was
    admissible over 92 rules, constructed, and validated by an acceptance criterion that read "staff
    can search the catalog and locate a registered material", against a search that ignored the
    search terms entirely.

    CS steps only. A CT step declares its binding explicitly in `Interface`, where the transform's
    formals are named on both sides and a different rule governs the mapping.
    """
    observation = rule.params["observation"]
    published = doc.observed.get(observation) or []
    if not published:
        return [(
            _where(rule),
            "no capability surface was observed — a step's inputs cannot be checked against "
            "operations nobody published",
        )]

    accepted: dict[str, dict[str, set[str]]] = {}
    for entry in published:
        if not isinstance(entry, dict):
            continue
        accepted[str(entry.get("capability"))] = {
            op: {str(f) for f in (spec.get("input") or [])}
            for op, spec in (entry.get("operations") or {}).items()
        }

    out = []
    for i, row in _rows(doc, rule):
        if _cell(row, "Kind") != "CS":
            continue
        capability, operation = _cell(row, "Capability"), _cell(row, "Operation")
        declared = accepted.get(capability, {}).get(operation)
        if declared is None:
            continue                      # the operation itself is another rule's business
        for field in (f.strip() for f in _cell(row, "Consumes").split(",")):
            if not field or field == "—":
                continue
            if field not in declared:
                out.append((
                    f"{_where(rule)} row {i}",
                    f"{operation} on {capability.split('::')[-1]} accepts "
                    f"{sorted(declared) or 'no input'}, not {field!r} — a step cannot hand an "
                    f"operation a field it does not take",
                ))
    return out


@check("CITED_ORDINAL_RESOLVES")
def _cited_ordinal_resolves(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A citation naming a row by ordinal must name a row that is there.

    `SOURCE_FINDING_RESOLVES` asks whether a citation names a register this phase may cite. It never
    asks whether the register has the row. So `S1 known_facts #18` against a register holding
    seventeen rows passes, and the finding it claims to rest on does not exist — the failure
    `project.py` names exactly: an ordinal pointing past the end resolves to a claim the row does
    not make, and nothing downstream can tell.

    A projected document cannot have this defect: its ordinals are generated from the rows they
    count. Every hand-authored phase from P2 on can, and P2 did — four citations off by one and one
    past the end of the register, all admitted.

    Resolved against whichever document the citation names: a stage-qualified register is looked up
    in that prior, an unqualified one in this document, which is ordinary intra-phase provenance.

    **Silent when the register cannot be reached.** A prior nobody supplied is the driver's
    omission, and reporting a document defect for a missing command-line argument is the confusion
    `_prior_rows` exists to avoid. This rule reports one thing only: the register was read, and the
    row it was asked for is not in it.
    """
    column = rule.params["column"]
    cited = re.compile(r"^(?:S(\d+)[a-z]?\s+)?([a-z][a-z0-9_]*)\s+#(\d+)\b")

    out: list[tuple[str, str]] = []
    for index, row in _rows(doc, rule):
        for citation in (part.strip() for part in _cell(row, column).split(";")):
            match = cited.match(citation)
            if not match:
                continue
            stage, register, ordinal = match.group(1), match.group(2), int(match.group(3))
            block = doc.prior_register(f"p{stage}", register) if stage else doc.register(register)
            if block is None or block.table is None:
                continue
            held = len(_content_rows(block))
            if ordinal < 1 or ordinal > held:
                where = f"{_where(rule)} row {index}"
                out.append((
                    where,
                    f"cites {register} #{ordinal}, which holds {held} row(s) — the citation "
                    f"resolves to a finding that is not there",
                ))
    return out


def _composition_steps(doc: ParsedDocument, register: str):
    """(owner, step) -> the step's declared row, from a phase's capability composition."""
    block = doc.register(register)
    if block is None or block.table is None:
        return {}
    return {(_bare_identity(_cell(r, "CC Code")), _cell(r, "Step Name")): r
            for _, r in _content_rows(block)}


def _named(cell_value: str) -> set[str]:
    """A comma-separated cell as a set of names, with the empty markers dropped."""
    return {p.strip() for p in cell_value.split(",") if p.strip() and p.strip() not in ("—", "-")}


@check("STEP_INPUTS_BOUND")
def _step_inputs_bound(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """Every input a step consumes must be bound to something.

    A composition says what a step hands its capability; the bindings say where each value comes
    from. Nothing checked that the second covered the first, so a step could declare it consumes
    `key, target_cs, target_ref`, bind only `key`, and be well formed twice over. The capability
    then received two nulls and wrote a row keyed on nothing — `{"key": null}` in a registry whose
    whole purpose is that the key is the identity.

    This is `NODE_INPUT_BOUND` one level down: that rule holds a workflow to the contract it calls,
    this one holds a contract to the capability it calls.
    """
    composition = rule.params["composition_register"]
    bound: dict[tuple[str, str], set[str]] = {}
    for _, row in _rows(doc, rule):
        if _cell(row, "Direction").upper() != "INPUT":
            continue
        key = (_bare_identity(_cell(row, "Owner")), _cell(row, "Step"))
        bound.setdefault(key, set()).add(_cell(row, "Field"))

    # A step input the contract itself declares under the same name needs no binding row: the
    # runtime passes it through by name, and the catalog relies on it throughout. Only a name the
    # contract neither declares nor binds arrives as a null.
    passed_through: dict[str, set[str]] = {}
    fields = doc.register(rule.params["fields_register"])
    if fields is not None and fields.table is not None:
        for _, row in _content_rows(fields):
            if _cell(row, "Direction").upper() == "INPUT":
                passed_through.setdefault(_bare_identity(_cell(row, "Artifact")), set()).add(
                    _cell(row, "Field"))

    # A value an earlier step of the same contract produced under that name is also satisfied: the
    # runtime chains by name within a contract, which is how the catalog feeds `records` from a
    # read into a select without a binding row for it.
    produced: dict[str, set[str]] = {}
    for (owner, _), row in _composition_steps(doc, composition).items():
        produced.setdefault(owner, set()).update(_named(_cell(row, "Produces")))

    # Only side-effect steps are checked. `Consumes` on a CS step names the operation's own inputs
    # — `STEP_CONSUMES_UNDECLARED_INPUT` holds it to the published surface — so an unbound one
    # provably arrives null. On a transform step the column is unenforced, and the tested designs
    # use domain-side names there while the bindings use the transform's, so comparing them would
    # report a defect where a mapping exists. Transform steps become checkable once a transform's
    # contract can be observed; until then this asserts only what it can know.
    out: list[tuple[str, str]] = []
    for (owner, step), row in sorted(_composition_steps(doc, composition).items()):
        if _cell(row, "Kind").upper() != "CS":
            continue
        satisfied = (bound.get((owner, step), set()) | passed_through.get(owner, set())
                     | produced.get(owner, set()))
        for field in sorted(_named(_cell(row, "Consumes")) - satisfied):
            out.append((f"{composition} {owner}/{step}",
                        f"consumes {field!r} and binds it to nothing — the capability receives "
                        f"no value for it"))
    return out


@check("BINDING_SOURCE_WELL_FORMED")
def _binding_source_well_formed(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A binding must name where a value comes from in the form the runtime resolves.

    An output is written to the capability result; an input is read from the artifact's own inputs,
    from a named earlier step, from the admitted payload, or is a literal. `results.record` looks
    like a reference and resolves to nothing, because a step's result is addressed by the step that
    produced it. Well formed, wrong, and silent until execution.
    """
    out: list[tuple[str, str]] = []
    output_form = re.compile(rule.params["output_pattern"])
    input_form = re.compile(rule.params["input_pattern"])
    for i, row in _rows(doc, rule):
        source = _cell(row, "Bound To")
        if not source:
            continue
        direction = _cell(row, "Direction").upper()
        form = output_form if direction == "OUTPUT" else input_form
        if not form.match(source):
            out.append((f"{_where(rule)} row {i}",
                        f"{direction.lower()} binds {source!r}, which is not a form the runtime "
                        f"resolves — {rule.params['detail']}"))
    return out


@check("CONTRACT_OUTPUT_PRODUCED")
def _contract_output_produced(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A contract's declared output must name a value one of its steps surfaces.

    Surfaced, not consumed: a step's OUTPUT binding carries the *domain* name a value takes when it
    leaves the step, while the composition's `Produces` column carries the capability's own name for
    it. `read_work_record` produces `value` and surfaces it as `work_record`, and a contract
    declaring `work_record` is exactly right. Reading the wrong one of those two reports a defect on
    every correct contract that renames anything.

    Declaring an output no step surfaces gives every caller a name that resolves to nothing — the
    contract is well formed, the caller is well formed, and the value arrives absent.
    """
    surfaced: dict[str, set[str]] = {}
    owners: set[str] = set()
    bindings = doc.register(rule.params["bindings_register"])
    if bindings is not None and bindings.table is not None:
        for _, row in _content_rows(bindings):
            owner = _bare_identity(_cell(row, "Owner"))
            owners.add(owner)
            if _cell(row, "Direction").upper() == "OUTPUT":
                surfaced.setdefault(owner, set()).add(_cell(row, "Field"))

    out: list[tuple[str, str]] = []
    for i, row in _rows(doc, rule):
        artifact = _bare_identity(_cell(row, "Artifact"))
        if artifact not in owners or _cell(row, "Direction").upper() != "OUTPUT":
            continue
        field = _cell(row, "Field")
        if field and field not in surfaced.get(artifact, set()):
            out.append((f"{_where(rule)} row {i}",
                        f"{artifact} declares output {field!r}, which no step of it surfaces — "
                        f"its steps surface {', '.join(sorted(surfaced.get(artifact, set()))) or 'nothing'}"))
    return out


def _interface_map(cell_value: str, side: str) -> dict[str, str]:
    """The `in:`/`out:` half of a step's Interface, as capability name -> design name.

    `in: source=matching_books, attribute=group_by; out: grouped=matching_works`. The left of each
    pair is the capability's own name for the value, which is the only half a contract can be held
    to; the right is what the design calls it, which is the design's business.
    """
    out: dict[str, str] = {}
    for part in cell_value.split(";"):
        head, _, body = part.partition(":")
        if head.strip().lower() != side:
            continue
        for pair in body.split(","):
            name, _, mapped = pair.partition("=")
            if name.strip():
                out[name.strip()] = mapped.strip()
    return out


@check("STEP_INTERFACE_CONFORMS")
def _step_interface_conforms(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A transform step must hand its transform the inputs that transform declares.

    The side-effect half of this has been checked since `STEP_CONSUMES_UNDECLARED_INPUT`, because
    the capability surface published side effects. It published no transforms, so a design could
    name `rules` where the transform declares `schema`, or read `validation_status` where it
    answers `violations`, and pass every rule at full Construction Completeness. Four contracts in
    one change request did exactly that, and every one of them failed at execution.

    Read from the **Interface** column rather than `Consumes`, because that column states the
    mapping instead of leaving it to be inferred: `in: source=matching_books` says the transform's
    `source` is fed by the design's `matching_books`, and only the left half is the transform's to
    declare. `Consumes` carries the capability's names on a side-effect step and the design's on a
    transform step, so holding a transform to it would report a defect on every design that renames
    anything.
    """
    observed = {t["transform"]: t for t in
                (doc.observed.get(rule.params["observation"]) or [])
                if isinstance(t, dict) and t.get("transform")}
    if not observed:
        # Reported, not skipped. Returning nothing here made this rule pass in silence through the
        # compiled path for as long as it existed, because the contract that judges a document
        # passed the capability surface and not the transform surface. A rule that cannot see its
        # subject has not checked it, and saying so is the difference between the two.
        return [(
            _where(rule),
            "no transform surface was observed — a step's interface cannot be checked against "
            "transforms nobody published",
        )]

    out: list[tuple[str, str]] = []
    for index, row in _rows(doc, rule):
        if _cell(row, "Kind").upper() != "CT":
            continue
        contract = observed.get(_cell(row, "Capability"))
        if contract is None:
            continue
        where = f"{_where(rule)} row {index}"
        interface = _cell(row, "Interface")
        supplied = _interface_map(interface, "in")
        produced = _interface_map(interface, "out")

        for name in sorted(set(supplied) - set(contract["inputs"])):
            out.append((where, f"hands {_cell(row, 'Capability').split('::')[-1]} an input "
                               f"{name!r} it does not declare — it accepts "
                               f"{', '.join(sorted(contract['inputs'])) or 'nothing'}"))
        for name in sorted(set(produced) - set(contract["outputs"])):
            out.append((where, f"reads {name!r} from "
                               f"{_cell(row, 'Capability').split('::')[-1]}, which answers "
                               f"{', '.join(contract['outputs']) or 'nothing'}"))
        required = {n for n, spec in contract["inputs"].items() if spec.get("required")}
        for name in sorted(required - set(supplied)):
            out.append((where, f"supplies no {name!r}, which "
                               f"{_cell(row, 'Capability').split('::')[-1]} requires"))
    return out


@check("STEP_BINDINGS_MATCH_INTERFACE")
def _step_bindings_match_interface(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A binding may only name a field the step's Interface declares.

    The Interface states what the step hands its capability and reads back; the bindings say where
    each of those comes from. `STEP_INTERFACE_CONFORMS` holds the Interface to the capability's real
    contract, so a binding naming a field the Interface does not carry is bound to a capability
    input that does not exist — checked at one remove, and until now not at all. A first attempt to
    give an occurrence its time bound `occurred_at` on a transform that accepts only `fields`, and
    passed every rule.

    Only steps that declare an Interface are checked. A side-effect step leaves the column empty
    because its `Consumes`/`Produces` already name the operation's own fields, and
    `STEP_CONSUMES_UNDECLARED_INPUT` holds those to the published surface.
    """
    declared: dict[tuple[str, str], tuple[set[str], set[str]]] = {}
    for (owner, step), row in _composition_steps(doc, rule.params["composition_register"]).items():
        interface = _cell(row, "Interface")
        if not interface or interface in ("—", "-"):
            continue
        # An input binds the capability's own name for the value — the left of `in: record=record`.
        # An output binds the *design's* name for it, the right of `out: record=book_record`, because
        # that is the name the value carries once it leaves the step. The two directions read
        # opposite halves of the same column, and a check reading one half for both reports a defect
        # on every step that renames its result.
        declared[(owner, step)] = (set(_interface_map(interface, "in")),
                                   set(_interface_map(interface, "out").values()))

    out: list[tuple[str, str]] = []
    for index, row in _rows(doc, rule):
        key = (_bare_identity(_cell(row, "Owner")), _cell(row, "Step"))
        if key not in declared:
            continue
        direction = _cell(row, "Direction").upper()
        allowed = declared[key][0] if direction == "INPUT" else declared[key][1]
        field = _cell(row, "Field")
        if field and field not in allowed:
            out.append((f"{_where(rule)} row {index}",
                        f"binds {field!r} on {key[1]}, which its interface does not carry — it "
                        f"declares {', '.join(sorted(allowed)) or 'nothing'} in that direction"))
    return out


@check("IMPLEMENTATION_MODULE_CONFORMS")
def _implementation_module_conforms(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A transform's implementation sits where its domain says implementations live.

    A capability transform is the one family whose artifact points outside the composition, and the
    module path is the whole of that pointer. `IMPLEMENTATION_WITHOUT_MODULE` asks only whether the
    cell is filled, so a path that is filled and wrong passed every rule, compiled, verified and
    attested — and failed at execution, where the loader looked in a namespace the domain does not
    use and found nothing.

    The expected path is derived from the artifact's own identity rather than declared, because it
    already is: the domain's build manifest resolves implementations under
    `<domain>.implementation.capability_transforms.atoms`, and the module is named for the artifact it
    implements. Asking a design to restate a path the composition already determines would invite it
    to restate it differently, which is exactly what happened.
    """
    template = rule.params["namespace_template"]
    code_column = rule.params["code_column"]
    module_column = rule.params["module_column"]

    out = []
    for i, row in _rows(doc, rule):
        code, module = _cell(row, code_column), _cell(row, module_column)
        # Presence is another rule's business, and so is the shape of the identity. This one has an
        # opinion only when there is both a well-formed code and a path to compare against it.
        if not code or not module or "::" not in code:
            continue
        domain, _, bare = code.partition("::")
        expected = f"{template.format(domain=domain)}.{bare.lower()}"
        if module != expected:
            out.append((
                f"{_where(rule)} row {i}",
                f"implementation is declared at {module!r}; {domain} resolves transforms at "
                f"{expected!r}. A module the loader does not look for is a transform that does not "
                f"run, and nothing below this notices until it is invoked",
            ))
    return out


@check("CROSS_SUBDOMAIN_REACH_READ_ONLY")
def _cross_subdomain_reach_read_only(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """An act reaching into another subdomain may read what it holds and never change it.

    A subdomain owns what it holds, and ownership that does not include being the only writer is not
    ownership. An act may consult another subdomain's records because a second copy of one truth can
    disagree with the thing it describes; it may not change them, because then two subdomains decide
    what is true and neither is answerable for the result.

    Three published facts and no inference: which subdomain owns a contract, which operations that
    contract's steps perform, and whether each of those operations writes. The last of those did not
    exist until it was declared — the operation *names* read as reads and writes, and a rule resting
    on a name is a convention anybody can break by naming an operation well. `idempotent` does not
    answer it either: a last-write-wins write is idempotent.
    """
    artifacts = doc.observed.get(rule.params["artifact_observation"]) or []
    contracts = doc.observed.get(rule.params["contract_observation"]) or []
    capabilities = doc.observed.get(rule.params["capability_observation"]) or []
    if not artifacts or not contracts or not capabilities:
        return [(
            _where(rule),
            "the composition was not observed — a reach across a subdomain boundary cannot be "
            "checked against subdomains nobody published",
        )]

    # Where each artifact lives. The composition answers for what it already holds; the design
    # answers for what it is authoring, which the composition has never seen.
    subdomain = {_bare_identity(str(a.get("artifact"))): a.get("owner_subdomain")
                 for a in artifacts if isinstance(a, dict)}
    for _, row in _content_rows(doc.register(rule.params["new_register"])):
        code, owner = _bare_identity(_cell(row, "Code")), _cell(row, "Owner Subdomain")
        if code and owner:
            subdomain[code] = owner

    effect = {(str(c.get("capability")), op): spec.get("effect")
              for c in capabilities if isinstance(c, dict)
              for op, spec in (c.get("operations") or {}).items()}

    writes: dict[str, list[tuple[str, str]]] = {}
    for contract in contracts:
        if not isinstance(contract, dict):
            continue
        performed = [
            (str(step.get("op")), str(step.get("store")))
            for step in (contract.get("steps") or [])
            if isinstance(step, dict) and step.get("side_effect")
            and effect.get((str(step.get("side_effect")), str(step.get("op")))) == "write"
        ]
        if performed:
            writes[_bare_identity(str(contract.get("contract")))] = performed

    out = []
    for i, row in _content_rows(doc.register(rule.params["topology_register"])):
        if _cell(row, "Node Type").upper() != "CC":
            continue
        workflow, node = _bare_identity(_cell(row, "Workflow")), _bare_identity(_cell(row, "Node"))
        here, there = subdomain.get(workflow), subdomain.get(node)
        # An unplaced artifact is another rule's finding. Reporting it here too would say the same
        # thing twice and say it less clearly.
        if not here or not there or here == there:
            continue
        for op, store in writes.get(node, []):
            out.append((
                f"{rule.params['topology_register']} row {i}",
                f"{workflow} is in {here} and reaches {node} in {there}, which performs {op} on "
                f"{store}. A subdomain may read what another holds and never change it — the owner "
                f"of a record is the only writer of it",
            ))
    return out


@check("INTERPRETATION_TRANSFORM_REFUSES")
def _interpretation_transform_refuses(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A transform that interprets an observation must be able to refuse it.

    A read reports that the store answered, never what it found, so a step reading state names the
    transform that turns the observation into a decision and the status that decision yields. Both
    have been required since CR-1. Neither asks the one question that decides whether the
    interpretation happens: a `CT` step yields SUCCESS when its transform returns and VIOLATION when
    it raises, so a transform that returns its judgement as a value leaves the step SUCCEEDing
    whatever it found, and the semantic status the row promises is never reached.

    `refuse_self_verification` was exactly this. It named `CT_PURE_COMPARE_EQUAL_V0`, which returns
    `is_equal` and raises only on missing inputs, and routed on whether the transform *ran* rather
    than on what it found — so a person could accept themselves, through a step named for refusing
    it. It passed every rule here, at full Construction Completeness, and the criterion covering it
    passed too because a prior defect had left the subject already decided.

    The fact this rests on could not be inferred: both transforms raise, and only a declaration
    distinguishes the one that raises on its judgement from the one that raises on a missing input.
    Read from the composition for a transform that already exists, and from this design's own
    implementation bindings for one it is authoring — the composition has never seen that one, and a
    rule that skipped it would be silent on exactly the transforms a change introduces.
    """
    column = rule.params["column"]
    observed = doc.observed.get(rule.params["observation"])
    if not observed:
        return [(
            _where(rule),
            "no transform surface was observed — whether an interpreting transform can refuse "
            "cannot be checked against transforms nobody published",
        )]

    refusal = {_bare_identity(str(t.get("transform"))): t.get("refusal")
               for t in observed if isinstance(t, dict) and t.get("transform")}
    for _, row in _content_rows(doc.register(rule.params["design_register"])):
        code = _bare_identity(_cell(row, rule.params["design_code_column"]))
        if code:
            refusal[code] = _cell(row, rule.params["design_refusal_column"]).lower()

    out = []
    for i, row in _rows(doc, rule):
        named = _cell(row, column)
        if not named or named in ("—", "-"):
            continue
        declared = refusal.get(_bare_identity(named))
        where = f"{_where(rule)} row {i}"
        if declared is None:
            out.append((
                where,
                f"interprets with {_bare_identity(named)}, which neither the composition nor this "
                f"design declares a refusal for — an interpretation that cannot be shown to refuse "
                f"has not been checked",
            ))
        elif declared != "raises":
            answers = ("yields its judgement as a value" if declared == "returns"
                       else "makes no judgement at all")
            status = _cell(row, rule.params["status_column"]) or "semantic status"
            out.append((
                where,
                f"interprets with {_bare_identity(named)}, which {answers} — the step succeeds "
                f"whatever it found, so the {status} this row declares is a branch nothing can "
                f"reach",
            ))
    return out


@check("COLUMN_VALUES_UNIQUE")
def _column_values_unique(doc: ParsedDocument, rule) -> list[tuple[str, str]]:
    """A column whose value identifies the row, so two rows may not carry the same one.

    Every other register check asks whether a row says the right thing. This asks whether the
    register says one thing about a subject at all: where a second row restates a subject the first
    already settled, the two may disagree, and nothing downstream can tell which was meant. Reading
    the first, the last, or refusing are three different behaviours and none of them is declared.

    Compared on the bare identity, because a subject written once as `domain::CODE_V0` and once as
    `CODE_V0` is one subject stated twice, and a comparison on the full string would call it two.
    """
    seen: dict[str, int] = {}
    out: list[tuple[str, str]] = []
    column = rule.params["column"]
    for index, row in _rows(doc, rule):
        value = _bare_identity(_cell(row, column))
        if not value:
            continue
        first = seen.setdefault(value, index)
        if first != index:
            out.append((f"{_where(rule)} row {index}", rule.params["detail"].format(value=value, first=first)))
    return out
