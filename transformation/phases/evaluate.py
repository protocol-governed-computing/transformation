"""Plain-data shapes shared by the genesis oracle and the compiled evaluator.

The compiled transform receives registers and rules as ordinary mappings — that is what crosses a
capability boundary. The genesis oracle works on the same shapes, so both apply identical logic to
identical inputs and a differential run compares like with like.

Nothing here judges anything. These are the structures a check kind is handed.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass
class Table:
    columns: list[str] = field(default_factory=list)
    rows: list[dict[str, str]] = field(default_factory=list)


@dataclass
class Block:
    """One `##` section of a phase document."""

    number: int | None
    title: str
    body: str = ""
    table: Table | None = None

    def text(self) -> str:
        return self.body.strip()

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "Block":
        table = None
        if data.get("columns"):
            table = Table(
                columns=list(data.get("columns") or []),
                rows=[dict(r) for r in (data.get("rows") or [])],
            )
        return Block(
            number=data.get("number"),
            title=data.get("title", ""),
            body=data.get("text", ""),
            table=table,
        )


@dataclass
class ParsedDocument:
    """A phase document as registers, plus whatever was observed about the composition.

    `observed` is empty for phases that judge a document alone. A phase that grounds claims against
    the assembled system fills it from a governed inspection capability, keyed by the operation that
    produced each fact — so a check can say which observation it relied on, and a missing
    observation is visible rather than silently absent.
    """

    header: dict[str, str]
    sections: list[Any]
    raw: str
    path: str = ""
    registers: list[Any] = field(default_factory=list)
    observed: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.blocks = [
            s if isinstance(s, Block) else Block.from_mapping(s) for s in self.sections
        ]

    def register(self, register_id: str) -> Block | None:
        """The register with this identity, or None if the document does not carry it.

        Registers are addressed by the `<!-- register:id -->` marker an authored document repeats
        from its template. Identity is stable across retitling and unambiguous when one section
        holds several registers.
        """
        for entry in self.registers:
            if entry.get("id") == register_id:
                table = None
                if entry.get("columns"):
                    table = Table(
                        columns=list(entry["columns"]),
                        rows=[dict(r) for r in (entry.get("rows") or [])],
                    )
                return Block(
                    number=None,
                    title=register_id,
                    body=entry.get("text", ""),
                    table=table,
                )
        return None

    def find(self, title_prefix: str) -> Block | None:
        """First block whose title starts with `title_prefix`.

        Real titles carry trailing annotations ("Known Facts — Business Truths (…)"), so match on
        the prefix and keep the annotation as authored.
        """
        low = title_prefix.lower()
        for block in self.blocks:
            if block.title.lower().startswith(low):
                return block
        return None


@dataclass(frozen=True)
class DeclaredRule:
    """One rule as it arrives from a declaration — workflow input or Python rule set.

    Carries both locators. `register` addresses a register by the identity an authored document
    repeats from its template; `section_title` is the fallback for P0, which has no RI-0 template
    and therefore no markers. A rule that declared a register but arrived without the field would
    resolve to nothing and pass silently — the whole register ungoverned, with no finding to say so.
    """

    id: str
    check: str
    section_title: str | None = None
    register: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "DeclaredRule":
        for required in ("id", "check"):
            if required not in data:
                raise KeyError(f"declared rule is missing {required!r}: {dict(data)}")
        register = data.get("register")
        return DeclaredRule(
            id=data["id"],
            check=data["check"],
            section_title=data.get("section_title") or register,
            register=register,
            params=dict(data.get("params") or {}),
            intent=data.get("intent", ""),
        )
