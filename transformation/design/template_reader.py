"""Read a vendored phase template into the register declaration a rule set derives from.

The templates under `templates/` are the battle-tested originals from RI-0's change pipeline. They
already declare, in a machine-readable form, most of what a phase's rules need:

    <!-- register:known_facts business_language -->
    | Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |

That one marker plus the header row gives the register's identity, its flags, its columns, and any
controlled vocabulary a column constrains. Re-deriving those by hand — which is what the first cut
of this repo did — produces a second, less precise copy that drifts from the tested one.

Two things the templates express that hand-written declarations got wrong:

- **`business_language` is per register — and sometimes per column.** A register carrying the bare
  flag holds business prose throughout and must name no compiled artifact. The scoped form,
  `business_language=capability,notes`, says only those columns are business prose while the rest of
  the register may legitimately carry identities. A register without the flag may cite freely, which
  is why a baseline register names FQDNs while its neighbours cannot.
- **A section may hold several registers.** The register, not the section, is the unit rules attach
  to.

The `gov_projection` block is read too: it declares what a phase consumes from its predecessor and
emits to its successor, by register id. That is the contract making the phases a pipeline rather
than a series of independent validators.

P0 has no template here, and correctly so — the seed phase is new in this rehost and has no RI-0
original to salvage.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parents[2] / "templates"

_HEADING = re.compile(r"^##\s+(?:(\d+[a-z]?)\.\s+)?(.+?)\s*$")
_MARKER = re.compile(r"^<!--\s*register:([a-z_]+)((?:\s+[a-z_]+(?:=[a-z_,]+)?)*)\s*-->\s*$")
_VOCAB_IN_COLUMN = re.compile(r"^(?P<name>[^(]+?)\s*\((?P<values>[A-Z][A-Z0-9_]*(?:\s*,\s*[A-Z][A-Z0-9_]*)+)\)\s*$")
_PROJECTION_ROW = re.compile(r"^\|\s*\*\*(?P<direction>Consumes|Emits)\*\*[^|]*\|(?P<fields>[^|]*)\|")


# Columns that cite rather than state. A citation names its subject — including, in a grounding
# phase, a compiled artifact — so these are never business-language columns.
_PROVENANCE_COLUMNS = ("Source Finding", "Evidence")


def _is_provenance_column(column: str) -> bool:
    return any(column.startswith(p) for p in _PROVENANCE_COLUMNS)


@dataclass(frozen=True)
class Register:
    """One declared register of a phase document."""

    id: str
    section_number: str | None
    section_title: str
    columns: tuple[str, ...]
    vocabularies: dict[str, tuple[str, ...]] = field(default_factory=dict)
    flags: frozenset[str] = frozenset()
    scoped_flags: dict[str, tuple[str, ...]] = field(default_factory=dict)

    @property
    def business_language(self) -> bool:
        """The register holds business prose and must name no compiled artifact."""
        return "business_language" in self.flags

    @property
    def business_language_columns(self) -> tuple[str, ...]:
        """Columns that must hold business prose and name no compiled artifact.

        The bare flag constrains the register's *content*; the scoped form names exactly which
        columns it constrains.

        Provenance columns are exempt from the bare flag. `Source Finding` records where a row came
        from and `Evidence` records what grounding turned up — both are citations by construction,
        and in a phase that verifies against the composition they must name artifacts. Treating
        them as business prose reports a finding against every correctly-grounded row, which is what
        the battle-tested P2 instance exposed.
        """
        if self.business_language:
            return tuple(c for c in self.columns if not _is_provenance_column(c))
        return self.scoped_flags.get("business_language", ())

    @property
    def optional(self) -> bool:
        """The register may legitimately carry no rows."""
        return "optional" in self.flags

    @property
    def traceable(self) -> bool:
        """Rows cite where they came from."""
        return any(c.startswith("Source Finding") for c in self.columns)


@dataclass(frozen=True)
class PhaseTemplate:
    """A phase's registers and its declared handoff contract."""

    phase: str
    path: Path
    registers: tuple[Register, ...]
    consumes: tuple[str, ...] = ()
    emits: tuple[str, ...] = ()

    def register(self, register_id: str) -> Register:
        for r in self.registers:
            if r.id == register_id:
                return r
        raise KeyError(f"{self.phase} declares no register {register_id!r}")


def _split_row(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [cell.strip() for cell in stripped.split("|")]


def _parse_columns(header_line: str) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    """Split a table header into column names, lifting any inline controlled vocabulary.

    `Certainty (HIGH, MEDIUM, LOW)` declares both the column and the values it admits. Reading the
    vocabulary from the template rather than restating it in Python is the difference between one
    declaration and two that can disagree.
    """
    columns: list[str] = []
    vocabularies: dict[str, tuple[str, ...]] = {}
    for raw in _split_row(header_line):
        match = _VOCAB_IN_COLUMN.match(raw)
        if match:
            name = match.group("name").strip()
            values = tuple(v.strip() for v in match.group("values").split(","))
            columns.append(name)
            vocabularies[name] = values
        else:
            columns.append(raw)
    return tuple(columns), vocabularies


def _parse_projection(lines: list[str]) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Read the gov_projection handoff table: what the phase consumes and what it emits."""
    consumes: tuple[str, ...] = ()
    emits: tuple[str, ...] = ()
    for line in lines:
        match = _PROJECTION_ROW.match(line)
        if not match:
            continue
        fields = tuple(
            f.strip().strip("`")
            for f in match.group("fields").replace("·", "\n").split("\n")
            if f.strip().strip("`")
        )
        if match.group("direction") == "Consumes":
            consumes = fields
        else:
            emits = fields
    return consumes, emits


def read_template(path: Path, phase: str) -> PhaseTemplate:
    """Parse a vendored phase template. A template with no registers is fail-hard."""
    if not path.is_file():
        raise FileNotFoundError(f"phase template not found: {path}")

    lines = path.read_text(encoding="utf-8").splitlines()
    registers: list[Register] = []
    section_number: str | None = None
    section_title = ""
    projection_lines: list[str] = []
    in_projection = False

    for i, line in enumerate(lines):
        heading = _HEADING.match(line)
        if heading:
            section_number = heading.group(1)
            section_title = heading.group(2).strip()
            in_projection = section_title.lower().startswith("gov_projection")
            continue

        if in_projection:
            projection_lines.append(line)
            continue

        marker = _MARKER.match(line)
        if not marker:
            continue

        # The header row is the next line that opens a table. A marker with no table is a
        # declaration of a register that cannot be read as rows — the rule set must see that.
        header_line = next(
            (lines[j] for j in range(i + 1, min(i + 4, len(lines))) if lines[j].lstrip().startswith("|")),
            None,
        )
        columns, vocabularies = _parse_columns(header_line) if header_line else ((), {})

        bare: set[str] = set()
        scoped: dict[str, tuple[str, ...]] = {}
        for token in marker.group(2).split():
            if "=" in token:
                name, _, values = token.partition("=")
                scoped[name] = tuple(v for v in values.split(",") if v)
            else:
                bare.add(token)

        registers.append(
            Register(
                id=marker.group(1),
                section_number=section_number,
                section_title=section_title,
                columns=columns,
                vocabularies=vocabularies,
                flags=frozenset(bare),
                scoped_flags=scoped,
            )
        )

    if not registers:
        raise ValueError(f"{path} declares no registers — it is not a phase template")

    consumes, emits = _parse_projection(projection_lines)
    return PhaseTemplate(
        phase=phase, path=path, registers=tuple(registers), consumes=consumes, emits=emits
    )


def load(phase: str, filename: str | None = None) -> PhaseTemplate:
    """Load a phase's vendored template.

    The filename comes from the catalogue unless overridden, so the phase identity and its template
    cannot drift apart. A phase with no template — p0, which is new in this rehost — is fail-hard
    rather than silently empty.
    """
    if filename is None:
        from transformation.design.catalog import phase as phase_spec

        spec = phase_spec(phase)
        if spec.template is None:
            raise KeyError(
                f"{phase} has no vendored template — it is new in this rehost, and its shape is "
                f"declared in transformation/phases/{phase}/template.py"
            )
        filename = spec.template
    return read_template(TEMPLATES / filename, phase)
