"""`tc` — the transformation compiler CLI.

The only interface this tool has. It is build-time: no transport surface, no Operation Identity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from transformation.baseline import Baseline, BaselineMismatch, observe, verify
from transformation.phases.checks import kinds as check_kinds
from transformation.phases.oracle import judge_path
from transformation.phases.p0 import rules as p0_rules
from transformation.phases.p0 import template as p0_template
from transformation.phases.p1 import rules as p1_rules
from transformation.phases.p2 import rules as p2_rules
from transformation.phases import catalog
from transformation.phases.template_reader import load as load_template

# Rule sets still declared per phase; purpose, question, key rule and purity rung come from the
# catalogue, which mirrors field manual §4.1 and §4.2.
RULE_SETS = {
    "p0": p0_rules,
    "p1": p1_rules,
    "p2": p2_rules,
}


@click.group()
@click.version_option(package_name="transformation_compiler")
def main() -> None:
    """PGC transformation compiler — governed change request to authoring mandate."""


@main.group()
def phase() -> None:
    """The dossier phases — judge a document against a phase's declared rule set."""


_PHASE_OPTION = click.option(
    "--phase",
    "phase_key",
    type=click.Choice(sorted(RULE_SETS)),
    required=True,
    help="Which phase's template and rule set to apply.",
)


@phase.command("check")
@click.argument("doc_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@_PHASE_OPTION
@click.option("--json", "as_json", is_flag=True, help="Emit the verdict as JSON.")
def phase_check(doc_path: Path, phase_key: str, as_json: bool) -> None:
    """Judge a phase document against that phase's structural oracle.

    Exit 0 if ADMISSIBLE, 1 if INADMISSIBLE.
    """
    verdict = judge_path(doc_path, RULE_SETS[phase_key].rule_set())

    if as_json:
        click.echo(json.dumps(verdict.as_dict(), indent=2))
    else:
        click.echo(f"{verdict.verdict}  [{phase_key}]  {doc_path}")
        for finding in verdict.findings:
            click.echo(f"  {finding}")
        click.echo(
            f"  {len(verdict.findings)} finding(s) over {verdict.rules_evaluated} declared rules"
        )

    sys.exit(0 if verdict.admissible else 1)


@phase.command("rules")
@_PHASE_OPTION
@click.option("--json", "as_json", is_flag=True, help="Emit the rule set as JSON.")
def phase_rules(phase_key: str, as_json: bool) -> None:
    """Print a phase's declared admissibility rule set.

    The rules are data, not code: this is the whole of what governs that phase's document.
    """
    declared = RULE_SETS[phase_key].rule_set()

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


@phase.command("template")
@_PHASE_OPTION
def phase_template(phase_key: str) -> None:
    """Print a phase's required section structure."""
    spec = catalog.phase(phase_key)
    click.echo(f"{phase_key} — {spec.purpose}\n  {spec.question}\n  admits: {spec.rung}\n")

    if spec.template is None:
        # P0 is new in this rehost and declares its own shape.
        from transformation.phases.p0.template import SECTIONS

        for s in SECTIONS:
            num = f"{s.number}. " if s.number is not None else "   "
            shape = "prose" if s.prose else f"table[{', '.join(s.table_columns)}]"
            click.echo(f"  {num}{s.title} — {shape}{'  (may be empty)' if s.may_be_empty else ''}")
        return

    for reg in load_template(phase_key).registers:
        cols = f"table[{', '.join(reg.columns)}]" if reg.columns else "no table"
        click.echo(f"  §{reg.section_number or '-':<3} {reg.id:<24} {cols}{'  (may be empty)' if reg.optional else ''}")
        for column, values in reg.vocabularies.items():
            click.echo(f"       {column}: {', '.join(values)}")


@phase.command("list")
def phase_list() -> None:
    """Print the pipeline: what each phase is for, and what vocabulary it admits.

    A phase name says which step; it does not say what the step is for. The commonest authoring
    failure is answering the next phase's question early, so the question and the purity rung are
    stated alongside the name.
    """
    for spec in catalog.PHASES:
        built = "built" if spec.id in RULE_SETS else "   — "
        rules = len(RULE_SETS[spec.id].rule_set()) if spec.id in RULE_SETS else 0
        click.echo(f"  {spec.id:<4} {spec.purpose:<20} [{built}] {rules or '':>4} rules   admits: {spec.rung}")
        click.echo(f"       {spec.question}")
        click.echo(f"       rule: {spec.key_rule}")
        if spec.gate:
            click.echo(f"       {spec.gate}")
        click.echo()


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
