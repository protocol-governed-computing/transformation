# Governance Intent — transformation / design, build

## Machine

```yaml
document:
  phase: p6
  domain: transformation
  subdomain:
  - design
  - build
  cr: genesis
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Read a phase document into its registers
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Read the earlier phase documents a phase must agree with
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Apply every rule of a phase and report each failure
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Judge a phase document, with and without the composition and earlier documents
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: The nine phases, each with its rules and its entry point
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Render, measure and attribute the artifacts a mandate schedules
    owner_subdomain: build
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Build an approved mandate
    owner_subdomain: build
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: The author of record and the reviewer
    owner_subdomain: design
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Observe the composition a change is designed against
    owner_subdomain: design
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    source_finding: {phase: p4, register: capability_graph, key: Observe the composition a change is designed against}
  - capability: Write built artifacts where the composition is authored
    owner_subdomain: build
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_TEXT_ARTIFACT_V0
    source_finding: {phase: p4, register: capability_graph, key: Write built artifacts where the composition is authored}
  storage_governance: []
  cross_subdomain_deps:
  - dependency: Read a design and a mandate into their registers
    direction: build → design
    existing_artifact: ''
    status: GAP
    source_finding: {phase: p4, register: design_decisions, row: 1}
  pps_artifacts_requiring_action:
  - fqdn: capability_side_effects::CS_SNAPSHOT_QUERY_V0
    current_status: Declared and in use across six namespaces
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: capability_side_effects::CS_SNAPSHOT_QUERY_V0}
  - fqdn: capability_side_effects::CS_TEXT_ARTIFACT_V0
    current_status: Declared and in use across six namespaces
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: capability_side_effects::CS_TEXT_ARTIFACT_V0}
  - fqdn: execution::STRUCTURE_RUNTIME_EXECUTION_V0
    current_status: Declared and carried by every workflow
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: execution::STRUCTURE_RUNTIME_EXECUTION_V0}
  - fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V1
    current_status: Declared; names the invariants the phases enforce
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: lifecycle::CONSTITUTION_CHANGE_MGMT_V1}
  - fqdn: lifecycle::CONSTITUTION_CONSTRUCTION_V1
    current_status: Declared; names the invariants construction enforces
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: lifecycle::CONSTITUTION_CONSTRUCTION_V1}
  boundary_rules:
  - rule_name: RULES_ARE_DECLARED_NEVER_CODED
    statement: What a phase checks, and why, is declared with the phase; a mechanism knows how to check and nothing about what.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - rule_name: COMPOSITION_READ_ONLY_THROUGH_INSPECTION
    statement: The pipeline reads the composition only through the platform's inspection capability, never from compiled output.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - rule_name: CONSTRUCTION_INVENTS_NOTHING
    statement: Construction writes only what the design states or a governing artifact fixes, and refuses a design that leaves a value undetermined.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - rule_name: BUILD_READS_DESIGN_ONLY_TO_PARSE
    statement: Construction uses the design subdomain's reading capability and nothing else of it.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  governance_outcome:
  - capability: Read a phase document into its registers
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Read a phase document into its registers}
  - capability: Read the earlier phase documents a phase must agree with
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Read the earlier phase documents a phase must agree with}
  - capability: Apply every rule of a phase and report each failure
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: Apply every rule of a phase and report each failure}
  - capability: Judge a phase document, with and without the composition and earlier documents
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: 'Judge a phase document, with and without the composition and earlier documents'}
  - capability: The nine phases, each with its rules and its entry point
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: 'The nine phases, each with its rules and its entry point'}
  - capability: Render, measure and attribute the artifacts a mandate schedules
    owner_subdomain: build
    source_finding: {phase: p6, register: ownership, key: 'Render, measure and attribute the artifacts a mandate schedules'}
  - capability: Build an approved mandate
    owner_subdomain: build
    source_finding: {phase: p6, register: ownership, key: Build an approved mandate}
  - capability: The author of record and the reviewer
    owner_subdomain: design
    source_finding: {phase: p6, register: ownership, key: The author of record and the reviewer}
```

WHERE the change is placed — ownership, dependencies and the rules at each boundary. No new artifact
codes are introduced here.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Boundary Rules

---

## 6. Governance Outcome
