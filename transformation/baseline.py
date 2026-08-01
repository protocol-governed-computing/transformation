"""The pinned baseline.

Validation runs against a named, frozen snapshot — never "the current snapshot". Every register a
snapshot-reading phase emits encodes facts about one specific composition: which artifacts exist,
what the normative closure contains, what a REUSE decision found. Against a moving snapshot those
fixtures fail for reasons that have nothing to do with the transformation compiler, and a
regression becomes indistinguishable from a rebuild.

So: a run that observes a different snapshot_id fails before any phase executes. Rebaselining is a
deliberate, reviewed act — re-pin the id, re-approve the affected registers.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from inspector import api


class BaselineMismatch(RuntimeError):
    """The snapshot on disk is not the one this CR was validated against."""


@dataclass(frozen=True)
class Baseline:
    snapshot_id: str
    artifact_count: int
    domains: tuple[str, ...]

    @staticmethod
    def load(path: Path) -> "Baseline":
        if not path.is_file():
            raise FileNotFoundError(f"baseline pin not found: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        for key in ("snapshot_id", "artifact_count", "domains"):
            if key not in data:
                raise KeyError(f"baseline pin {path} is missing {key!r}")
        return Baseline(
            snapshot_id=data["snapshot_id"],
            artifact_count=int(data["artifact_count"]),
            domains=tuple(data["domains"]),
        )


def observe(snapshot_root: Path) -> Baseline:
    """Read the composition actually present at `snapshot_root`."""
    status, summary = api.query("si.snapshot.summary", {}, str(snapshot_root))
    if status != "SUCCESS":
        raise RuntimeError(f"si.snapshot.summary failed on {snapshot_root}: {status}")
    return Baseline(
        snapshot_id=summary["snapshot_id"],
        artifact_count=int(summary["artifact_count"]),
        domains=tuple(d["domain"] for d in summary.get("domains", [])),
    )


def verify(pin: Baseline, snapshot_root: Path) -> Baseline:
    """Assert the snapshot on disk is the pinned one. Fail hard on any drift."""
    actual = observe(snapshot_root)
    if actual.snapshot_id != pin.snapshot_id:
        raise BaselineMismatch(
            "snapshot does not match the pinned baseline — no phase may run.\n"
            f"  pinned:   {pin.snapshot_id}\n"
            f"  observed: {actual.snapshot_id}\n"
            "Rebaselining is deliberate: re-pin the id and re-approve the affected registers."
        )
    return actual
