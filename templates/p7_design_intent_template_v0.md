# Design Intent: [domain] / [subdomain]
**Domain:** [domain]  
**Subdomain:** [subdomain]  
**Version:** V0  
**Status:** DRAFT  
**Pipeline Stage:** Stage 7 — Design Intent (HOW)  
**Produced by:** v0.5.0 SDLC authoring pipeline  
**Purity:** HOW only — business facts (Business Model) and placement decisions (Governance Intent) not repeated  

---

## Document Contract

**This artifact is a structured register document — not a narrative.** P7 assigns the **binding
FQDNs** the rest of the build depends on. The worker emits register ROWS; a deterministic renderer
owns the document and a structural oracle validates the codes BEFORE a human reviews.

VALID OUTPUT:
- Populated register tables (every required register below)
- Binding FQDNs in `code` / `rb_code` / `binds_wf` / `storage_structure` columns, each
  well-formed (`domain::PREFIX_NAME_V<n>`) and assigned EXACTLY ONCE
- Business-language capability descriptions in the `capability` column

INVALID OUTPUT:
- Narrative summaries / reasoning essays replacing registers
- A binding FQDN referenced anywhere (topology, RB) but absent from `new_artifacts`
- Two spellings of the same capability (a typo is a SECOND immutable artifact, not a synonym)

A required register with no rows MUST render as a single `| NONE IDENTIFIED |` row. The renderer
rejects a malformed FQDN, an empty required register, an undeclared reference, or a near-duplicate
code mechanically.

---

### Binding-FQDN discipline (the oracle enforces these)

- **Well-formed:** every assigned code is `domain::PREFIX_NAME_V<n>` (PREFIX ∈ WF/IN/RB/CC/CT/EV/
  STRUCTURE; explicit `_V0`).
- **One canonical FQDN per capability — assign it ONCE, reuse the EXACT string everywhere**
  (topology, pipelines, RB, summary). A binding FQDN is immutable: a spelling/term variant of the
  same concept (e.g. `GENESIS` vs `GENEISIS`) silently creates a SECOND, permanently-misnamed
  artifact. Spell domain terms exactly.
- **Referenced ⇒ declared:** every NEW code that appears in `execution_topology` or
  `rb_declarations` MUST appear as a row in `new_artifacts`. CTs and EVs are first-class new
  artifacts — never implicit.
- **Genuinely new:** an assigned `new_artifacts` code MUST NOT already exist in the snapshot
  (the oracle collision-checks via grounding). Existing artifacts go in `existing_inventory`.
- **Reconciled:** the NEW counts in `artifact_summary` MUST equal the rows of `new_artifacts`.

### Data-to-decision closure (the oracle enforces these)

P7 does not merely assign artifacts. It assigns the **behavioural interpretation path** from a
capability's output, through a decision, to a workflow transition. A design that names every
artifact correctly and leaves that path unstated is admissible and still cannot work.

- **No implicit truthiness.** `exists`, `matched`, `authorized` and every other boolean a capability
  returns is an **observation**, never a decision. A step that reads external state cannot drive
  business routing directly.
- **A step branches on what its operation answers, or says what produced the rest.** Every
  operation publishes its `result_status_values`. A `CS` step routing on one of those — a registry
  claim exiting on `ALREADY_EXISTS`, a read exiting on `NOT_FOUND` — is routing on the store's own
  answer, and interprets nothing. A step routing on anything else MUST name the transform that
  produces that outcome (`Interpreted By`) and the outcome itself (`Semantic Status`).
- **`—` in either column is a declaration, not a blank.** It says the step's output is data and the
  branches are the operation's own. It is the right answer for most steps and refused wherever the
  routing names an outcome the operation cannot produce.
- **`Store` and `Consumes` take the same dash and it says something different in each.** In `Store`
  it declares that the step addresses no store, which is true exactly when its capability keeps no
  records — a clock and every transform. In `Consumes` it declares that the step hands the operation
  nothing, which is true exactly when the operation takes no input. Both are checked against what the
  composition publishes, so a storage step addressing nothing and a read consuming nothing are each
  refused where they read as a design that works.
- **Routing closure.** Every workflow branch is backed by the whole chain:

```
CS result  →  CT interpretation  →  semantic outcome  →  WF transition
```

> **Raw capability observations never determine workflow behaviour directly.**

An interpretation transform expresses its decision the only way the execution contract allows: a
`CT` step yields `SUCCESS` when it returns and `VIOLATION` when it raises. A transform that returns
a boolean for both answers has interpreted nothing, however it is named — which is why a transform
named here must declare `refusal: raises` in §9.

### Capability Composition discipline (the oracle enforces these)

`cc_composition` declares the second half of Design Intent: WHAT each new CC is composed of. Workflow
topology (§5) says how CCs route to one another; composition says what is *inside* each CC. It is
**declarative, not procedural** — you declare the governed capabilities the CC is built from and how
data flows between them; you never write code, JSON, JSONPath, or an implementation.

- **CT/CS only.** Each composition step is a Capability Transform (`CT`, pure compute, zero side
  effects) or a Capability Side Effect (`CS`, the only place external state changes) — never a CC, WF,
  or IN. A CC composes *capabilities*, not other CCs.
- **Codes verbatim.** Every `Capability` cell is a CT/CS binding FQDN copied verbatim from
  `new_artifacts` (NEW) or a grounded `existing_inventory` artifact (REUSE) — same immutability rule
  as every binding FQDN. A composition code absent from both registers is a defect.
- **Data flow is logical, not wired.** `Consumes` / `Produces` name business/data fields (e.g.
  `proposed_block`, `content_hash`), connecting a CC's inputs to its steps and step-to-step. Concrete
  JSONPath wiring is construction (S8), not design.
- **Outcome coverage.** The outcomes the composition can yield MUST cover the CC's routing surface in
  `execution_topology` (§5): if topology routes the CC on `SUCCESS` and `ALREADY_EXISTS`, the
  composition must be able to produce both. The oracle cross-checks composition ⊇ topology surface.
- **CT purity.** A `CT` step may not appear where a side effect is required, and may never be a CS.

### Business-Language Rule

Only the `capability` column of `new_artifacts` is business language (name the need, not the
artifact). Every other column legitimately carries FQDNs / controlled tokens — that is where the
binding codes belong. Existing artifacts are cited by their real FQDN in `fqdn` / source columns.

---

## Stage Inputs — Questions for the Human

*Answer crisply before drafting. The right column states how the agent uses each answer.*

| # | Question for the Human | How the Agent Uses the Answer (Intent) |
|---|------------------------|----------------------------------------|
| 1 | For each open design decision carried from Stages 1–4: which concrete resolution (store shape, schema fields, algorithm, reuse-vs-new)? | Becomes `design_resolution`. Every row traces to a Business Model design decision; new decisions invented here are flagged. |
| 2 | Where an existing artifact partially fits: REUSE as-is, EXTEND it, or REPLACE it? | Fixes `existing_inventory` actions. REPLACE/EXTEND of shared artifacts affects other subdomains. |
| 3 | Do you approve the proposed store names, paths, and key fields? | Locks `structure_stores`. Storage topology is a governance concern — paths declared here, never hardcoded later. |
| 4 | Gate 1: do you approve the full dossier as the design basis? | Gate 1 approval authorizes Stage 7. Without it, no mandate may be drafted. |

**Agent execution rules for this stage (binding FQDNs are assigned here):**
- Every new artifact maps 1:1 to a Governance Intent outcome; every FQDN carries `_V<n>`.
- **Workflow nodes are IN, CC, EXIT/EXIT_SUCCESS only.** Sub-workflow invocation = gateway CC bound to `CS_WORKFLOW_GATEWAY_V0` (precedent: `CC_INVOKE_BLOCK_PROPOSAL_V0`). EV_ artifacts are emitted facts, never triggers.
- A store is written only by CCs of its owning subdomain. Writing CCs for peer stores are declared in the dependency-gap section with peer ownership.
- Before declaring a new CT or EV: check the existing inventory (the transform vocabulary and event set usually already contain the atom) — if reused, it belongs in `existing_inventory`, not `new_artifacts`.
- **Compose every new CC.** Each `family = CC` row in `new_artifacts` gets a `cc_composition` (§6): the ordered CT/CS steps it is built from + their data flow. Leaving a CC's composition unstated leaves construction a design decision — exactly the black box this stage exists to close.
- **Module path assignment (reference):** IN→`[repo].registry.[subdomain].intents`, WF→`.workflows`, CC→`.capability_contracts`, CT→`.capability_transforms`, RB→`.runtime_bindings`, STRUCTURE→`.structures`. A missing assignment is a build failure.

---

### Citing a prior row

Every row carries a `Source Finding` naming where its content came from. A citation resolves when it
names one of:

- **a register this phase may cite**, by id and ordinal — `known_facts #14`;
- **the same, by section**, prefixed with the phase that declared it — `S1 §4 Known Facts #14`;
- **a literal source** — `CR seed`, `human decision`, `projection`, `S1 seed`;
- **an artifact already in the baseline**, by exact identity — `blockchain::WF_REGISTER_ACTOR_V0`.

Separate several citations with `;`. One resolvable citation grounds the row.

**A carried claim is carried verbatim.** Where a register restates a row an earlier phase declared —
a belief, an authoring decision, a capability — the text must match that row exactly. Tightening a
sentence while citing the row it came from is how a claim drifts from what was decided, so the rules
treat a tidier synonym as a new claim and refuse it. Cite it as it stands, or change it in the phase
that owns it.

---

## 1. Design Decisions Resolution

*The Design Decisions Register populated throughout Stages 1–4 — resolved here. Each row traces to a Business Model design decision (`source_finding`).*

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|

---

## 2. Artifact Inventory — Existing Artifacts

*All existing PPS artifacts touched by this CR. Action ∈ REPLACE | REUSE | EXTEND | REVIEW. `fqdn` is the existing artifact, cited by exact FQDN.*

**An `EXTEND` is a whole redeclaration, not a delta.** Construction renders an amended artifact from
this design alone and the result replaces its predecessor, so every register that describes it must
describe it *as it will be* — every store the declaration carries, every field the contract accepts
and returns, every node the workflow runs — not only the parts this change adds. A design that
states the delta renders an artifact with the rest deleted, and reports 100% completeness while
doing it, because completeness asks whether the design's own claims are determined and never what
the composition already holds.

*The word invites the wrong reading and the reading is expensive: it produced a storage declaration
carrying two stores where five existed. `tc construction check --snapshot` compares each amendment
with the artifact it replaces and refuses one that narrows it.*

*`Summary` states what the artifact **is**, where `Reason` states why this change touches it. It is
required for an `EXTEND`, because a rendered artifact without its summary is one this change
silently emptied. A `REUSE` or `REVIEW` row is not rendered and may leave it blank.*

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|

---

## 3. Artifact Family Mapping — New Artifacts

*Each Governance Outcome capability mapped to an artifact family with a binding FQDN assigned.
`capability` is business language; `code` is the binding FQDN; `family` is the execution concern;
`owner_subdomain` is the owning subdomain; `source_finding` traces to the S6 ownership / S4 gap.*

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

*One RB per WF. The RB declares which CS substrates the WF requires and which storage structure resolves store paths. An undeclared CS binding is a runtime failure. `cs_bindings` may list several CS FQDNs (comma-separated).*

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|

---

## 5. Execution Topology

*The DAG flattened to one row per node, in execution order, per workflow. `node` is an IN/CC binding
FQDN or a terminal (EXIT / EXIT_SUCCESS).*

*`routing` states the outcome→target edges as **edges, not prose**: `STATUS -> target` entries
separated by `;`, where STATUS is a business status name (ACK, NACK, SUCCESS, NOT_FOUND,
ALREADY_EXISTS, DENIED, VIOLATION, BACKEND_ERROR) and target is a node of this same workflow or a
terminal. `SUCCESS -> CC_APPEND_CATALOG_OPERATION_V0; VIOLATION -> EXIT_REJECTED`. A description of
where control goes is not a routing declaration — it names no node, and construction cannot resolve
it.*

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|

---

## 6. Capability Composition

*The inside of each new CC: the ordered CT/CS steps it is composed of and how data flows between
them. Declarative, not procedural — governed capabilities + data flow, never code or JSONPath. One
row per (CC, step), in execution order. `capability` is a CT/CS binding FQDN (verbatim from
`new_artifacts` or `existing_inventory`); `consumes`/`produces` name logical data fields. The
outcomes the composition can yield must cover the CC's routing surface in `execution_topology` (§5).
`Interface` (CT steps) is the **explicit invocation binding** — how this step's CC-local fields bind
to the invoked capability's declared FORMAL parameters, so a reusable CT keeps its own vocabulary and
the CC keeps its business vocabulary. Syntax: `in: <ct_formal>=<cc_local>, …; out: <ct_output>=<cc_local>, …`
(e.g. `in: left=predecessor_hash, right=current_head; out: is_equal=is_match`). CS steps leave it blank.*

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|

---

## 7. Step Bindings

*What each workflow node and each contract step is handed, and where its results go. A step whose
bindings are undeclared is one construction must invent bindings for, and an invented binding is a
design decision taken outside the gate.*

*`owner` is the workflow or capability contract; `step` is its node or step name. A workflow node
takes INPUT bindings only; a contract step takes both, because its outputs are named for later steps
and for the contract's own surface.*

*`bound_to` is declarative, never an expression: `payload.<field>` names a field of the starting
intent, `<node>.<field>` names an earlier node's output in this same workflow, and a bare literal is
a constant the design fixes (an operation name, a status). Rendering that into `$.payload.x` is
construction's business — the design states the source, not the syntax.*

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|

---

## 8. Interface Fields

*Every typed field an artifact declares, whichever family it belongs to. An intent's inputs, a
capability contract's inputs and outputs, a transform's inputs and outputs, and an actor's
attributes are one shape — (artifact, direction, field, type) — and they were all unexpressible for
the same reason: the language could describe a capability but never a field of one.*

*`direction` ∈ INPUT | OUTPUT | ATTRIBUTE. `required` ∈ YES | NO. `default` is stated only when the
field has one; a field with no default and `required: NO` is simply absent when not supplied.*

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|

---

## 9. Implementation Bindings

*Where a transform's code lives. A CT is the one family whose artifact points outside the
composition, and the module path is a governance concern for the same reason a store path is: it is
declared once, at design time, never discovered later.*

*`operation` is the CT's declared operation name; `purity` ∈ ct_pure | ct_impure; `kind` ∈ atom |
molecule.*

*`refusal` says how the transform expresses a judgement about its subject: `raises` refuses, which
the execution contract reads as VIOLATION; `returns` yields the judgement as an output, so the step
succeeds whatever it found; `never` judges nothing. It is about the subject, never the inputs —
every transform raises on a missing input, so that would make the fact uniform and therefore empty.
A transform named as an interpretation must declare `raises`, because a judgement the step cannot
fail on is a branch nothing reaches.*

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|

---

## 10. Vocabulary Extensions

*Business status names this change adds, and the vocabulary they extend. A workflow that routes on
`DENIED` needs `DENIED` to exist; the routing surface and the vocabulary that admits it are declared
together or the composition compiles with a status nothing recognizes.*

*`Extends` is required and the none marker is an answer. A vocabulary that builds on nothing is a
base vocabulary, which is a decision; left blank it is indistinguishable from a design that never
settled the question, and both render the same empty field.*

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|

---

## 11. Runtime Policies

*The per-capability configuration a runtime binding carries. `dispatcher.py` resolves
`rb_policy[rb][capability]["policy"]` at execution, so this is what an RB *is* — the workflow that
binds it is a separate fact, declared on the workflow in §4.*

*A capability listed in `rb_declarations` with no row here binds with an empty policy, which is a
declaration that it needs no configuration rather than an omission.*

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|

---

## 12. Artifact Properties

*Scalar facts a family declares that no other register carries — an actor's `type` today. A property
that recurs across families has stopped being family-specific and earns its own register; this one
exists so that a single scalar does not.*

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|

---

## 13. STRUCTURE Stores

*New entity stores. `storage_type` selects the CS substrate — a store a capability claims keys in is a registry store, which the composition already carries examples of; `proposed_path` is the declared store path (governance concern — never hardcoded later); `used_by` names the writing CC (its owning subdomain only).*

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|-----------------------------------------------------------|---------------|---------|----------------|

---

## 14. Transport Bindings

*What a boundary contract publishes and how it maps across the boundary. An ingress declares the
operation identity a caller names, what dispatches it, and how the canonical input becomes the
workflow payload; an egress declares how a result surface becomes the fields a caller reads. One row
per mapped field, so a mapping is checkable rather than a blob.*

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|

## 15. Artifact Summary

*Artifact count by action type, for Stage 7 input. The oracle reconciles: the NEW counts here MUST equal the rows of `new_artifacts`. `artifacts` lists the codes for that action.*

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|

---

## 16. Generation Provenance

*How an artifact is **reached**. Every other register says what an artifact must become; this one
says what determines it, and it is the only register that can describe an artifact nobody types.*

*An artifact listed here is produced by invoking its generator, and construction never writes it —
two producers of one truth drift, and the drift is silent until something reads the stale one. The
generator is authoritative: where the artifact and the generator disagree, the artifact is stale, and
the build refuses rather than reporting on a copy.*

*`Generator` is what construction invokes, as `module:callable`, and it must be importable from the
composition rather than reached as a script. `Generator Sources` names everything the emission reads
— a template and the declaration read with it are **one** generator, and naming either alone permits
regenerating from a stale pairing.*

*The artifact is still scheduled as an artifact. A design does not schedule a generator: the artifact
is what enters the composition and what conformance judges, and a mandate scheduling a generator
schedules something that never appears in a snapshot.*

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|

---

## 17. Declared Reach

*The bindings an act **consults** — the records another subdomain of its own domain owns, which this
act reads and never writes. Ownership is §4 and is exactly one; reach is here and may be several,
and the two are separate registers rather than one with a column telling them apart, because a
column would put them a typo apart with nothing between them but the rule that reads it.*

*`Act` is the workflow's binding FQDN; `Consults` names the binding, comma-separated for several,
and **never the records behind it**. Which records a binding covers is the owning subdomain's own
declaration, and restating it here is a second copy kept by someone other than whoever answers for
it. The rules read the composition for that half.*

*Every declared reach is used by a read the act performs, and every read the act's own binding does
not cover is declared here. Neither half is a rule alone: the first permits a reserve, the second
permits a silent reach.*

*An act that reads only what it owns declares none, which is most acts.*

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 18. Refusal Discharge

*What carries out an operation the business said it refuses. The seed states the refusal and the
condition; this register states the act, the step and the outcome that stop it — and it is the only
place a design says so, because a refusal nothing discharges is a refusal in prose.*

*`Operation` and `Refused When` are the seed's own wording, taken from its `operation_refusals`
register: the pair identifies which declared refusal this row answers, and a row naming a pair the
seed does not state is answering for a refusal nobody approved.*

*`Act` is the workflow's binding FQDN and `Step` is a step of that workflow, both resolved against
§5. `Outcome` is one the step reports, and it must route to a node typed `EXIT` — an ending that
refuses. An outcome routing anywhere else does not stop the operation, however plainly this register
says it does.*

*A refusal this change does not carry out belongs in §19, not here and not nowhere.*

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

---

## 19. Refusal Deferrals

*A refusal the business declared and this design does not discharge, with the owner who will. The
two registers are read together for coverage and apart for everything else: a discharge names a
place in the topology, a deferral names a person and a condition, and one table holding both would
leave half its cells empty on every row — where a blank meaning "not applicable" is indistinguishable
from one meaning "unanswered".*

*`Deferred To` is who owns it and must not be blank; a deferral with no owner is a refusal dropped
in language that sounds like a plan. `Until` is the condition that ends the deferral.*

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|

---

---

## Gate 1 — Design Approval

**Gate 1 closes here.** The full dossier (Stages 0–7) is presented for review as a body. Any
prior-stage artifact amended during the Stage 6–7 session is included. This is a unified review of
the complete design, not a per-stage approval. Gate 1 approval authorizes Stage 7 — Authoring
Mandate. Gate 2 (after Stage 7) locks the full dossier before artifact authoring begins.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | change_request_[subdomain]_v0.md | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | business_model_[subdomain]_v0.md | COMPLETE |
| Stage 5 — Business Intent | business_intent_[subdomain]_v0.md | COMPLETE |
| Stage 6 — Governance Intent | governance_intent_[subdomain]_v0.md | COMPLETE — APPROVED |
| Stage 7 — Design Intent | This document | PENDING GATE 1 APPROVAL |
| Stage 8 — Authoring Mandate | Pending | — |
| Stage 8 — Authoring Manifest | Pending | — |

---

## gov_projection — Governed Handoff to Stage 7

*The bounded inputs and emit keys mirror the engine's gov_projection schema exactly
(`contracts/gov_projection.py`). P7 is the binding stage — it consumes the full design context
(S2 attribute/step data, S4 gaps/decisions, S5 intent + provisional codes, S6 placement) and emits
the five registers S7 builds from, plus `cc_composition` which the S8 Build Sheet assembles. Emit
keys match the register ids above exactly.*

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entity_attributes · process_steps |
| **Consumes** ← Stage 4 | gap_register · design_decisions · authoring_scope |
| **Consumes** ← Stage 5 | scope_boundary · invariants · actions · provisional_codes |
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action |
| **Emits** → Stage 7 | new_artifacts · existing_inventory · rb_declarations · execution_topology · artifact_summary |
| **Emits** → Stage 8 (Build Sheet) | cc_composition · generation_provenance |
