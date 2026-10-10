# Stage 7 — Design Intent: transformation / design
**Stage:** 7 — Design Intent
**CR:** register_format
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW: two readers replaced, four contracts re-pointed, and the form a phase document carries its
facts in.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| What a document carries | Every consumer of a register receives it as data from one reading step. | One YAML Machine block per phase document: the first fenced yaml block. It holds a header mapping, which replaces the bold header fields, and a registers mapping keyed by register id, in the document's order. A tabular register is a list of rows, each a mapping from column name to string value, columns in declared order. A narrative register is a string. The prose stays Markdown around the block. | S4 design_decisions #1 |
| What the new reader returns | The two forms must be comparable finding for finding. | Exactly what the old reader returns: the header as strings; the sections from the prose headings; each register with its id, columns, rows and text. A register's columns are read from its first row. Values inside cells stay strings, and an empty register keeps its sentinel row, its first column reading NONE IDENTIFIED and the others empty. | S4 design_decisions #2 |
| What changes identity | The readers change meaning; the contracts do not. | The two readers are replaced by V1 readers. The three judging contracts and the construction contract are re-pointed and keep their identities. No phase workflow changes. | S4 design_decisions #3 |
| What happens to the replaced readers | Their implementation is the old reading, and nothing names them after the repoints. | They are deleted at delivery by a recorded human act. The record names the two identities, the business author as the deciding party, and the determination that no retention condition holds: nothing live names them, and the only sealed snapshot containing them is the v5 release, which retains them itself. Their names are never reused. | S4 design_decisions #4 |
| How a document is converted | Conversion must be mechanical to show the forms agree. | A command reads a document with the old reader and writes the new form: the prose without its register tables and header fields, and the block. It runs once over the test documents, the end-to-end payloads' sources and the test copies, and is deleted with the old reader. | S4 design_decisions #5 |
| Where the test copies live | The construction tests read a dossier's design and mandate only. | Beside the catalog's fixtures, one directory per delivered dossier, holding its design and mandate converted. The construction tests read every root from the fixtures. The delivered originals are not edited. | S4 design_decisions #6 |
| How the forms are shown to agree | One evaluator judges both forms. | Every converted document is judged in both forms by the same sealed rule set. The verdicts and the findings, as rule, location and detail, must be identical. The old reader is deleted only when no document differs. | S4 design_decisions #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|--------------------------------------------------|---------|--------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V0 | REPLACE | Parse phase document text into structured registers | It reads a different form, so CT_PURE_PARSE_REGISTERS_V1 supersedes it. It is deleted at delivery. | S6 pps_artifacts_requiring_action #1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | REPLACE | Parse the upstream phase documents a phase is judged against | It reads a different form, so CT_PURE_PARSE_PRIOR_PHASES_V1 supersedes it. It is deleted at delivery. | S6 pps_artifacts_requiring_action #2 |
| transformation::CC_JUDGE_DOCUMENT_V0 | REPOINT | Parse a phase document and judge it against a declared rule set | Binds a replaced reader; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #3 |
| transformation::CC_JUDGE_AGAINST_SNAPSHOT_V1 | REPOINT | Parse a phase document and its priors, observe the composition, and judge them together | Binds a replaced reader; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #4 |
| transformation::CC_JUDGE_AGAINST_COMPOSITION_V1 | REPOINT | Parse a phase document and its priors, observe the composition and its declarations, and judge them together | Binds a replaced reader; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #5 |
| transformation::CC_CONSTRUCT_ARTIFACTS_V0 | REPOINT | Measure a design, refuse it if under-determined, and render the artifacts it schedules | Binds a replaced reader; it names the successor and keeps its identity. | S6 pps_artifacts_requiring_action #6 |
| transformation::CT_PURE_EVALUATE_RULES_V0 | REUSE |  | Judges the same shape from either reader. Unchanged. | S6 pps_artifacts_requiring_action #7 |
| transformation::STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V0 | REVIEW |  | Declares what the domain compiles. Unchanged; named because the authored readers are compiled under it. | S6 pps_artifacts_requiring_action #8 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|
| Reading a phase document's registers from its structured block | CT | transformation::CT_PURE_PARSE_REGISTERS_V1 | Read a phase document's header and registers from its structured block, and its sections from its prose | design | NEW | S6 governance_outcome #1 |
| Reading a prior phase's registers from its structured block | CT | transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | Read the upstream phase documents a phase is judged against, each from its structured block | design | NEW | S6 governance_outcome #1 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | INPUT | document_text | string | YES |  | The full text of the phase document — never a path, never read from disk |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | header | object | YES |  | Header field name to declared value |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | sections | array | YES |  | Ordered sections, each with number, title, text, and any table columns and rows |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | OUTPUT | registers | array | YES |  | Registers addressed by their marker id, each with columns and rows |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | INPUT | prior_texts | object | YES |  | Phase id → full text of that phase's document, supplied by the calling workflow. Empty when |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | OUTPUT | priors | object | YES |  | Phase id → parsed document as header, sections and registers |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | transformation.implementation.capability_transforms.atoms.ct_pure_parse_registers_v1 | execute | PURE_PARSE_REGISTERS | atom | ct_pure | never | S7 new_artifacts CT_PURE_PARSE_REGISTERS_V1 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | transformation.implementation.capability_transforms.atoms.ct_pure_parse_prior_phases_v1 | execute | PURE_PARSE_PRIOR_PHASES | atom | ct_pure | never | S7 new_artifacts CT_PURE_PARSE_PRIOR_PHASES_V1 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| NONE IDENTIFIED |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | supersedes | transformation::CT_PURE_PARSE_REGISTERS_V0 | S7 existing_inventory CT_PURE_PARSE_REGISTERS_V0 |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | supersedes | transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 | S7 existing_inventory CT_PURE_PARSE_PRIOR_PHASES_V0 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| REPLACE | design | 2 | transformation::CT_PURE_PARSE_REGISTERS_V0, transformation::CT_PURE_PARSE_PRIOR_PHASES_V0 |
| EXTEND | design | 0 |  |
| NEW | design | 2 | transformation::CT_PURE_PARSE_REGISTERS_V1, transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| NONE IDENTIFIED |

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| Judging a document | The document is in the old form, after this change | p0 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p1 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p2 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p3 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p4 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p5 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p6 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p7 | REGISTER_MISSING | S0 operation_refusals #1 |
| Judging a document | The document is in the old form, after this change | p8 | REGISTER_MISSING | S0 operation_refusals #1 |

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|
| NONE IDENTIFIED |

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | SUCCESS | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | SUCCESS | human decision |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | INPUT | document_text | "# Stage 1\n\n```yaml\nheader:\n  CR: register_format\nregisters:\n  known_facts:\n  - Fact: A register is data.\n    Certainty: HIGH\n```\n" | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | header | {CR: register_format} | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | sections | [] | human decision |
| transformation::CT_PURE_PARSE_REGISTERS_V1 | reads_header_and_registers_from_the_machine_block | EXPECTED | registers | [{id: known_facts, columns: [Fact, Certainty], rows: [{Fact: A register is data., Certainty: HIGH}], text: ''}] | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | INPUT | prior_texts | {p1: "# Stage 1\n\n```yaml\nheader:\n  CR: register_format\nregisters:\n  known_facts:\n  - Fact: A register is data.\n    Certainty: HIGH\n```\n"} | human decision |
| transformation::CT_PURE_PARSE_PRIOR_PHASES_V1 | reads_each_prior_from_its_machine_block | EXPECTED | priors | {p1: {header: {CR: register_format}, sections: [], registers: [{id: known_facts, columns: [Fact, Certainty], rows: [{Fact: A register is data., Certainty: HIGH}], text: ''}]}} | human decision |

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | Ownership, artifacts requiring action, boundary rules | COMPLETE |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
