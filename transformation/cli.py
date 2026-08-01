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
from transformation.phases.p1 import template as p1_template

# Every phase is a template plus a rule set; the mechanisms are shared. Adding a phase is an entry
# here, not a new command — the CLI generalizes exactly as the artifacts do.
PHASES = {
    "p0": ("the seed phase", p0_rules, p0_template),
    "p1": ("the change request register", p1_rules, p1_template),
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
    type=click.Choice(sorted(PHASES)),
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
    _, rules_mod, _ = PHASES[phase_key]
    verdict = judge_path(doc_path, rules_mod.rule_set())

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
    _, rules_mod, _ = PHASES[phase_key]
    declared = rules_mod.rule_set()

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
    label, _, template_mod = PHASES[phase_key]
    click.echo(f"{phase_key} — {label}\n")
    for spec in template_mod.SECTIONS:
        num = f"{spec.number}. " if spec.number is not None else "   "
        shape = "prose" if spec.prose else f"table[{', '.join(spec.table_columns)}]"
        optional = "  (may be empty)" if spec.may_be_empty else ""
        click.echo(f"  {num}{spec.title} — {shape}{optional}")


@phase.command("list")
def phase_list() -> None:
    """Print the phases this build governs."""
    for key in sorted(PHASES):
        label, rules_mod, template_mod = PHASES[key]
        click.echo(
            f"  {key}  {label:<32} "
            f"{len(template_mod.SECTIONS):>2} registers  "
            f"{len(rules_mod.rule_set()):>3} rules"
        )


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
