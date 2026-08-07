"""Meta-validation — governance validating governance, before it judges a document.

The design compiler's split is declaration in `rules.py`, mechanism in `checks.py`. That split is
only worth having if the two halves are held in correspondence, and nothing held them: a rule could
name a check kind that no longer exists, pass a parameter no check reads, or omit one every check
path requires, and none of it surfaces until a dossier happens to reach that rule. A mechanism could
lose its last caller and stay in the registry forever, read as governance that is no longer in
force.

This is the same property `INVARIANT_ASSERT_PARITY_V0` asserts for the platform surface — every
declaration enforceable, every enforcement declared — applied to the layer where design rules are
declared. It is meta-governance: it validates the rule sets, never a document, and it must pass
before a verdict over any document means anything. A rule that cannot run reports green over an
unevaluated subject, which is the vacuity failure this codebase exists to refuse.

**A check kind's parameter contract is read from its implementation, not restated.** Restating it
would produce a second declaration that can disagree with the tested one — the same reasoning that
put structural rules in `derive.py` rather than in nine phase modules. A parameter subscripted
unconditionally is required; one read through `.get`, or subscripted inside a branch or an
alternation, is optional. So the contract cannot drift from the code that implements it.
"""

from __future__ import annotations

import ast
import inspect
from dataclasses import dataclass
from types import ModuleType

from transformation.design import catalog
from transformation.design import checks as checks_module
from transformation.design import rules as shared_rules
from transformation.design.checks import kinds as declared_kinds
from transformation.design.p0_change_seed import rules as p0_rules
from transformation.design.p1_change_request import rules as p1_rules
from transformation.design.p2_domain_model import rules as p2_rules
from transformation.design.p3_analysis_loop import rules as p3_rules
from transformation.design.p4_business_model import rules as p4_rules
from transformation.design.p5_business_intent import rules as p5_rules
from transformation.design.p6_governance_intent import rules as p6_rules
from transformation.design.p7_design_intent import rules as p7_rules
from transformation.design.p8_authoring_mandate import rules as p8_rules
from transformation.design.rules import Rule

# Which module declares which phase's rule set. Declared here rather than in the CLI because the
# meta pass and the testbed both need it, and a second mapping is a second thing to forget a phase
# in — the failure this pass exists to catch, one level up.
RULE_MODULES: dict[str, ModuleType] = {
    "p0": p0_rules,
    "p1": p1_rules,
    "p2": p2_rules,
    "p3": p3_rules,
    "p4": p4_rules,
    "p5": p5_rules,
    "p6": p6_rules,
    "p7": p7_rules,
    "p8": p8_rules,
}

# A subscript under one of these is reached only on some paths, so the rule that omits it is not
# thereby broken. `BoolOp` covers the `params.get(a) or params[b]` alternation — b is required only
# when a is absent.
_CONDITIONAL = (ast.If, ast.IfExp, ast.BoolOp, ast.Try, ast.While)


@dataclass(frozen=True)
class MetaFinding:
    """One correspondence defect between what is declared and what is enforced."""

    code: str
    where: str
    detail: str

    def __str__(self) -> str:
        return f"[{self.code}] {self.where}: {self.detail}"


@dataclass(frozen=True)
class ParamContract:
    """What a check kind reads out of a rule's `params`."""

    required: frozenset[str]
    optional: frozenset[str]

    @property
    def known(self) -> frozenset[str]:
        return self.required | self.optional


def _params_read(node: ast.AST, functions: dict[str, ast.FunctionDef]) -> tuple[set[str], set[str], set[str]]:
    """Parameter names one function body reads directly, plus the module functions it calls.

    Returns (unconditionally required, optional, callees). A check kind's full contract is the
    union over its call graph — two helpers in `checks.py` read `params` on their caller's behalf,
    and a contract that stopped at the decorated function would miss them.
    """
    required: set[str] = set()
    optional: set[str] = set()
    callees: set[str] = set()

    def visit(parent: ast.AST, conditional: bool) -> None:
        for child in ast.iter_child_nodes(parent):
            reached_conditionally = conditional or isinstance(parent, _CONDITIONAL)
            name = _subscripted_param(child)
            if name is not None:
                (optional if reached_conditionally else required).add(name)
            if isinstance(child, ast.Call):
                got = _param_get(child)
                if got is not None:
                    optional.add(got)
                if isinstance(child.func, ast.Name) and child.func.id in functions:
                    callees.add(child.func.id)
            visit(child, reached_conditionally)

    visit(node, False)
    return required, optional, callees


def _is_params(node: ast.AST) -> bool:
    """Whether an expression is a rule's `params` mapping.

    Both idioms count: `rule.params` and the defensive `getattr(rule, "params", {})`. A contract
    blind to the second would call a parameter unknown that a check reads every run.
    """
    if isinstance(node, ast.Attribute) and node.attr == "params":
        return True
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "getattr"
        and len(node.args) >= 2
        and isinstance(node.args[1], ast.Constant)
        and node.args[1].value == "params"
    )


def _subscripted_param(node: ast.AST) -> str | None:
    """`params["name"]` — the name, or None."""
    if isinstance(node, ast.Subscript) and _is_params(node.value) and isinstance(node.slice, ast.Constant):
        return node.slice.value
    return None


def _param_get(node: ast.Call) -> str | None:
    """`params.get("name", ...)` — the name, or None."""
    func = node.func
    if isinstance(func, ast.Attribute) and func.attr == "get" and _is_params(func.value):
        if node.args and isinstance(node.args[0], ast.Constant):
            return node.args[0].value
    return None


def _check_kind(node: ast.FunctionDef) -> str | None:
    """The kind a `@check("...")`-decorated function implements."""
    for decorator in node.decorator_list:
        if (
            isinstance(decorator, ast.Call)
            and isinstance(decorator.func, ast.Name)
            and decorator.func.id == "check"
            and decorator.args
            and isinstance(decorator.args[0], ast.Constant)
        ):
            return decorator.args[0].value
    return None


def param_contracts() -> dict[str, ParamContract]:
    """Read every check kind's parameter contract out of `checks.py` itself."""
    tree = ast.parse(inspect.getsource(checks_module))
    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}

    def contract(name: str, seen: tuple[str, ...] = ()) -> tuple[set[str], set[str]]:
        if name in seen:  # a cycle contributes nothing it has not already contributed
            return set(), set()
        required, optional, callees = _params_read(functions[name], functions)
        for callee in callees:
            inherited_required, inherited_optional = contract(callee, seen + (name,))
            required |= inherited_required
            optional |= inherited_optional
        return required, optional

    contracts: dict[str, ParamContract] = {}
    for name, node in functions.items():
        kind = _check_kind(node)
        if kind is None:
            continue
        required, optional = contract(name)
        # A name read both ways is optional: the subscript is the guarded arm of its own `.get`.
        contracts[kind] = ParamContract(frozenset(required - optional), frozenset(optional))
    return contracts


def _shared_factories() -> set[str]:
    """The rule factories `design/rules.py` publishes for phases to compose.

    Functions only — `Rule` itself is the declaration type every phase uses, not a factory that
    contributes rules to a set.
    """
    return {
        name
        for name, obj in vars(shared_rules).items()
        if not name.startswith("_")
        and inspect.isfunction(obj)
        and obj.__module__ == shared_rules.__name__
    }


def verify(rule_modules: dict[str, ModuleType]) -> list[MetaFinding]:
    """Assert the declaration/enforcement correspondence across every phase's rule set.

    `rule_modules` is always supplied — for the same reason `oracle.evaluate` takes its rules. A
    default here would silently verify eight phases and report a confident verdict over nine.
    """
    contracts = param_contracts()
    findings: list[MetaFinding] = []
    referenced_kinds: set[str] = set()

    # A phase the catalogue declares but nothing judges is the vacuity failure one level up: the
    # pipeline reports a phase exists and no rule ever runs against its document.
    for spec in catalog.PHASES:
        if spec.id not in rule_modules:
            findings.append(
                MetaFinding(
                    "PHASE_RULE_SET_MISSING",
                    f"catalog/{spec.id}",
                    f"is declared in the phase catalogue ({spec.purpose}) but no rule set is "
                    f"composed for it — its document would be admitted unjudged",
                )
            )
    for phase_id in sorted(set(rule_modules) - {spec.id for spec in catalog.PHASES}):
        findings.append(
            MetaFinding(
                "PHASE_UNDECLARED",
                f"rules/{phase_id}",
                "composes a rule set for a phase the catalogue does not declare",
            )
        )

    for phase_id, module in sorted(rule_modules.items()):
        rules: list[Rule] = module.rule_set()
        for rule in rules:
            where = f"{phase_id}/{rule.id}"
            referenced_kinds.add(rule.check)

            if rule.check not in contracts:
                findings.append(
                    MetaFinding(
                        "CHECK_KIND_UNDECLARED",
                        where,
                        f"names check kind {rule.check!r}, which no mechanism in checks.py "
                        f"implements — the rule cannot run",
                    )
                )
                continue

            contract = contracts[rule.check]
            for name in sorted(set(rule.params) - contract.known):
                findings.append(
                    MetaFinding(
                        "RULE_PARAM_UNREAD",
                        where,
                        f"passes {name!r} to {rule.check}, which never reads it — the parameter "
                        f"is inert and the rule does not govern what its author declared",
                    )
                )
            for name in sorted(contract.required - set(rule.params)):
                findings.append(
                    MetaFinding(
                        "RULE_PARAM_MISSING",
                        where,
                        f"omits {name!r}, which {rule.check} requires on every path — the rule "
                        f"raises rather than judges as soon as a document reaches it",
                    )
                )

            if not rule.intent:
                findings.append(
                    MetaFinding(
                        "RULE_INTENT_MISSING",
                        where,
                        "declares no intent — a finding nobody can read the reason for is a "
                        "rule nobody can review",
                    )
                )

            if rule.register and rule.section_title:
                findings.append(
                    MetaFinding(
                        "RULE_TARGET_AMBIGUOUS",
                        where,
                        "declares both a register identity and a section title; the register "
                        "wins and the title is never consulted",
                    )
                )

    for kind in sorted(set(declared_kinds()) - referenced_kinds):
        findings.append(
            MetaFinding(
                "CHECK_KIND_ORPHANED",
                f"checks.py/{kind}",
                "is implemented but no declared rule invokes it — enforcement without a "
                "declaration reads as governance that is not in force",
            )
        )

    for name in sorted(_shared_factories()):
        # A phase composes a factory by importing it into its own module namespace, which is the
        # only way `rule_set()` can call it — so importing it is the whole of the evidence.
        if not any(name in vars(module) for module in rule_modules.values()):
            findings.append(
                MetaFinding(
                    "SHARED_FACTORY_ORPHANED",
                    f"rules.py/{name}",
                    "is published for phases to compose but no phase composes it — a shared "
                    "rule factory nobody calls governs nothing",
                )
            )

    return findings