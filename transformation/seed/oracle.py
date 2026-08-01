"""The P0 structural oracle — a generic evaluator over the declared rule set.

This module contains **no rules**. It walks `rules.rule_set()`, dispatches each declared rule to
its check kind, and collects findings. What makes a seed admissible is declared in `rules.py`; how
a check is performed is implemented in `checks.py`; this file only composes them.

The oracle is deterministic and reads no snapshot. It judges shape and discipline, never business
correctness: it cannot know whether a Business Truth is true, only whether the seed keeps truths,
beliefs and questions in their proper registers and invents no design.

The verdict is ADMISSIBLE or INADMISSIBLE. There is no warning tier — a seed a human must think
about before P1 consumes it is not admissible.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from transformation.seed.checks import dispatch
from transformation.seed.evaluate import ParsedDocument
from transformation.seed.read import read_seed
from transformation.seed.rules import Rule, rule_set

ADMISSIBLE = "ADMISSIBLE"
INADMISSIBLE = "INADMISSIBLE"


@dataclass(frozen=True)
class Finding:
    rule: str
    where: str
    detail: str
    intent: str = ""

    def __str__(self) -> str:
        return f"[{self.rule}] {self.where}: {self.detail}"


@dataclass
class Verdict:
    verdict: str
    seed: str
    rules_evaluated: int
    findings: list[Finding] = field(default_factory=list)

    @property
    def admissible(self) -> bool:
        return self.verdict == ADMISSIBLE

    def as_dict(self) -> dict:
        return {
            "verdict": self.verdict,
            "seed": self.seed,
            "rules_evaluated": self.rules_evaluated,
            "findings": [
                {
                    "rule": f.rule,
                    "where": f.where,
                    "detail": f.detail,
                    "intent": f.intent,
                }
                for f in self.findings
            ],
        }


def evaluate(doc: ParsedDocument, rules: list[Rule] | None = None) -> Verdict:
    """Apply every declared rule to an already-read seed.

    Every rule is evaluated — there is no short-circuit on first failure. A seed author needs the
    whole finding set, and a rule that never runs is a rule that cannot be trusted.
    """
    declared = rule_set() if rules is None else rules
    findings: list[Finding] = []

    for rule in declared:
        # dispatch() fails hard on an unknown kind: a skipped rule reports green over an
        # unevaluated subject, which is exactly the vacuity failure the oracle exists to catch.
        for where, detail in dispatch(rule.check)(doc, rule):
            findings.append(
                Finding(rule=rule.id, where=where, detail=detail, intent=rule.intent)
            )

    return Verdict(
        verdict=INADMISSIBLE if findings else ADMISSIBLE,
        seed=str(doc.path),
        rules_evaluated=len(declared),
        findings=findings,
    )


def judge_path(path: Path) -> Verdict:
    return evaluate(read_seed(path))
