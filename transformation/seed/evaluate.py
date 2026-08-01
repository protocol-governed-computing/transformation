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
    """A phase document as registers, however it arrived."""

    header: dict[str, str]
    sections: list[Any]
    raw: str
    path: str = ""

    def __post_init__(self) -> None:
        self.blocks = [
            s if isinstance(s, Block) else Block.from_mapping(s) for s in self.sections
        ]

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
    """One rule as it arrives from a declaration — workflow input or Python rule set."""

    id: str
    check: str
    section_title: str | None = None
    params: dict[str, Any] = field(default_factory=dict)
    intent: str = ""

    @staticmethod
    def from_mapping(data: Mapping[str, Any]) -> "DeclaredRule":
        for required in ("id", "check"):
            if required not in data:
                raise KeyError(f"declared rule is missing {required!r}: {dict(data)}")
        return DeclaredRule(
            id=data["id"],
            check=data["check"],
            section_title=data.get("register"),
            params=dict(data.get("params") or {}),
            intent=data.get("intent", ""),
        )
