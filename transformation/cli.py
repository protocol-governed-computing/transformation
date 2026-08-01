"""`tc` — the transformation compiler CLI.

The only interface this tool has. It is build-time: no transport surface, no Operation Identity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from transformation.baseline import Baseline, BaselineMismatch, observe, verify
from transformation.seed.checks import kinds as check_kinds
from transformation.seed.oracle import judge_path
from transformation.seed.rules import rule_set
from transformation.seed.template import CR_TYPES, SECTIONS


@click.group()
@click.version_option(package_name="transformation_compiler")
def main() -> None:
    """PGC transformation compiler — governed change request to authoring mandate."""


@main.group()
def seed() -> None:
    """P0 — the seed phase."""


@seed.command("check")
@click.argument("seed_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--json", "as_json", is_flag=True, help="Emit the verdict as JSON.")
def seed_check(seed_path: Path, as_json: bool) -> None:
    """Judge a seed against the P0 structural oracle.

    Exit 0 if ADMISSIBLE, 1 if INADMISSIBLE.
    """
    verdict = judge_path(seed_path)

    if as_json:
        click.echo(json.dumps(verdict.as_dict(), indent=2))
    else:
        click.echo(f"{verdict.verdict}  {seed_path}")
        for finding in verdict.findings:
            click.echo(f"  {finding}")
        click.echo(
            f"  {len(verdict.findings)} finding(s) over {verdict.rules_evaluated} declared rules"
        )

    sys.exit(0 if verdict.admissible else 1)


@seed.command("rules")
@click.option("--json", "as_json", is_flag=True, help="Emit the rule set as JSON.")
def seed_rules(as_json: bool) -> None:
    """Print the declared admissibility rule set.

    The rules are data, not code: this is the whole of what governs a seed.
    """
    declared = rule_set()

    if as_json:
        click.echo(
            json.dumps(
                [
                    {
                        "id": r.id,
                        "check": r.check,
                        "register": r.section_title,
                        "params": r.params,
                        "intent": r.intent,
                    }
                    for r in declared
                ],
                indent=2,
            )
        )
        return

    for rule in declared:
        register = rule.section_title or "(document)"
        click.echo(f"  {rule.id:<38} {rule.check:<24} {register}")
        if rule.intent:
            click.echo(f"  {'':<38} └─ {rule.intent}")
    click.echo(f"\n  {len(declared)} rules over {len(check_kinds())} check kinds")


@seed.command("template")
def seed_template() -> None:
    """Print the required seed section structure."""
    click.echo(f"CR types: {', '.join(CR_TYPES)}\n")
    for spec in SECTIONS:
        label = f"{spec.number}. " if spec.number is not None else "   "
        shape = "prose" if spec.prose else f"table[{', '.join(spec.table_columns)}]"
        optional = "  (may be empty)" if spec.may_be_empty else ""
        click.echo(f"  {label}{spec.title} — {shape}{optional}")


@main.group()
def baseline() -> None:
    """The pinned validation baseline."""


@baseline.command("verify")
@click.argument("pin_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--snapshot",
    "snapshot_root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    required=True,
    help="Snapshot root to check against the pin.",
)
def baseline_verify(pin_path: Path, snapshot_root: Path) -> None:
    """Assert the snapshot on disk is the pinned baseline."""
    pin = Baseline.load(pin_path)
    try:
        actual = verify(pin, snapshot_root)
    except BaselineMismatch as exc:
        click.echo(str(exc), err=True)
        sys.exit(1)
    click.echo(f"BASELINE OK  {actual.snapshot_id}")
    click.echo(f"  artifacts {actual.artifact_count}  domains {', '.join(actual.domains)}")


@baseline.command("show")
@click.option(
    "--snapshot",
    "snapshot_root",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    required=True,
    help="Snapshot root to read.",
)
def baseline_show(snapshot_root: Path) -> None:
    """Print the composition present at a snapshot root, as a pin."""
    actual = observe(snapshot_root)
    click.echo(
        json.dumps(
            {
                "snapshot_id": actual.snapshot_id,
                "artifact_count": actual.artifact_count,
                "domains": list(actual.domains),
            },
            indent=2,
        )
    )
