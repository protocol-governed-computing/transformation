"""The `IMPLEMENTATION_MODULE_CONFORMS` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import _at, _cell, _rows, _where
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("IMPLEMENTATION_MODULE_CONFORMS")
def _implementation_module_conforms(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
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
                _at(_where(rule), i),
                f"implementation is declared at {module!r}; {domain} resolves transforms at "
                f"{expected!r}. A module the loader does not look for is a transform that does not "
                f"run, and nothing below this notices until it is invoked",
            ))
    return out
