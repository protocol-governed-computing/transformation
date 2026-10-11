# Stage 5 — Business Intent: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 5 — Business Intent
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 6 — Governance Intent
registers:
  subdomain_purpose: |2

    The Catalog subdomain governs the library's authoritative description of what it holds: one record
    for each work the library has catalogued, one for each edition in which that work is published, and
    one for each physical copy it owns. It establishes the authority to say what the library has and how
    its holdings relate — a work exists in the collection because the catalog says so, an edition belongs
    to that work because the catalog records it that way, and a copy is a copy of one edition for the
    same reason. It manages the lifecycle of editions and copies from registration through retirement
    and back, and it records every operation performed against it so that any change to the library's
    description of itself can be traced afterwards. It exists because a work published more than once
    cannot be described accurately by a catalog that knows only editions, which is what the library had.
    It does not govern who borrows the collection, what is ordered, who the library's patrons are, or
    which staff are authorized.
  purpose_provenance:
    columns:
    - Source
    - Disposition (INHERITED, REFINED)
    - Refinement
    rows:
    - Source: CR seed §0 Subdomain Purpose
      Disposition (INHERITED, REFINED): REFINED
      Refinement: 'The seed states the change — that the record the previous change calls a book is an edition and that the work is added above it. This states the subdomain that results: the three records it holds, the authority it establishes over how they relate, the lifecycle it manages, and the four functions it does not govern. Nothing here contradicts the seed; what it adds is the standing description rather than the narrative of the change.'
  scope_boundary:
    columns:
    - Capability
    - Status (IN_SCOPE, DEFERRED)
    - Notes
    - Source Finding
    rows:
    - Capability: Form the identifying key of a work from its title and author
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: A different business key from the edition's; the edition key is not widened
      Source Finding: S4 authoring_scope GAP-01
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Claimed atomically, as the edition's identity is
      Source Finding: S4 authoring_scope GAP-02
    - Capability: Resolve the work an edition belongs to
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Answers which work a title and author denote
      Source Finding: S4 authoring_scope GAP-03
    - Capability: Group selected records by an attribute they share
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Selection already exists; grouping does not
      Source Finding: S4 authoring_scope GAP-04
    - Capability: Declare the stores the catalog owns
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Extended with the work store and the work identity registry
      Source Finding: S4 authoring_scope GAP-05
    - Capability: Bind the catalog's workflows to the stores they use
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Extended so the new stores are reachable
      Source Finding: S4 authoring_scope GAP-06
    - Capability: Register an edition of a work the catalog does not yet hold
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Gains a work claim among the claims, before any write
      Source Finding: S4 authoring_scope GAP-07
    - Capability: Validate that a registration carries what a work and an edition require
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Runs before any claim, as it does today
      Source Finding: S4 authoring_scope GAP-08
    - Capability: Register an additional edition of an existing work
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The operation this change exists to add
      Source Finding: S4 authoring_scope GAP-09
    - Capability: Search the catalog and answer at the level of the work
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Search terms unchanged; one result per matching work
      Source Finding: S4 authoring_scope GAP-10
    - Capability: Retrieve an edition's complete details with a summary of its work
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: Retrieval stays edition retrieval
      Source Finding: S4 authoring_scope GAP-11
    - Capability: Admit a request to register an additional edition of an existing work
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: A new operation is reached through its own entry point
      Source Finding: S4 authoring_scope GAP-12
    - Capability: Recognise the moment a work enters the catalog
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Notes: The catalog declares a moment for each thing that enters it
      Source Finding: S4 authoring_scope GAP-13
    - Capability: Multiple identifiers for one publication
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: What an identifier identifies could not be answered until an edition was defined
      Source Finding: S4 authoring_scope Deferred
    - Capability: A governed subject taxonomy
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: A further catalog need, deferred to a change of its own
      Source Finding: S4 authoring_scope Deferred
    - Capability: Digital resources associated with catalog records
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: A further catalog need, deferred to a change of its own
      Source Finding: S4 authoring_scope Deferred
    - Capability: Images associated with catalog records
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: A further catalog need, deferred to a change of its own
      Source Finding: S4 authoring_scope Deferred
    - Capability: Deciding which staff are authorized
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Notes: Belongs to the staff function, which a future change introduces
      Source Finding: S4 authoring_scope Deferred
  business_objects:
    columns:
    - Store Name
    - Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID)
    - Business Rationale
    - Source Finding
    rows:
    - Store Name: Work record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: The library needs one place that says which works it holds; a work's description is corrected in place rather than re-registered
      Source Finding: S4 bm_entities Work
    - Store Name: Work identity registry
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): IDENTITY_REGISTRY
      Business Rationale: Two registrations describing the same work must not produce two works, and only an atomic claim can guarantee that
      Source Finding: S4 resources The work identity registry
    - Store Name: Edition record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: 'Unchanged from the previous change: an edition''s description is corrected in place and its state moves both ways'
      Source Finding: S4 bm_entities Edition
    - Store Name: Physical copy record
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): MUTABLE_STATE
      Business Rationale: 'Unchanged from the previous change: a copy''s state moves both ways on the same record'
      Source Finding: S4 bm_entities Physical Copy
    - Store Name: Catalog audit trail
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): APPEND_ONLY_JOURNAL
      Business Rationale: 'Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended'
      Source Finding: S4 bm_entities Business Operation
    - Store Name: Edition identity registry
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): IDENTITY_REGISTRY
      Business Rationale: 'Unchanged from the previous change: no two editions share a title, author and publication year'
      Source Finding: 'S4 constraint_register #9'
    - Store Name: Copy barcode registry
      Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID): IDENTITY_REGISTRY
      Business Rationale: 'Unchanged from the previous change: no two copies share a barcode'
      Source Finding: 'S4 constraint_register #7'
  identity_semantics:
    columns:
    - Store Name
    - Identity Field
    - Source
    - Uniqueness Rule
    - Cross-Subdomain Relationship
    - Source Finding
    rows:
    - Store Name: Work record
      Identity Field: Title and author together
      Source: Supplied by the staff member registering the first edition of the work
      Uniqueness Rule: Two registrations carrying the same title and author describe the same work, and the second names the work that exists rather than creating another
      Cross-Subdomain Relationship: None
      Source Finding: 'S1 identity_and_sameness #1'
    - Store Name: Work identity registry
      Identity Field: The key formed from title and author
      Source: Formed by the catalog from the two identifying attributes
      Uniqueness Rule: The key is claimed once; a second claim on it resolves to the work already registered rather than refusing
      Cross-Subdomain Relationship: None
      Source Finding: 'S4 design_decisions #3'
    - Store Name: Edition record
      Identity Field: Title, author and publication year together
      Source: Supplied by the staff member registering the edition
      Uniqueness Rule: Two registrations carrying the same title, author and publication year describe the same edition, and the second is refused
      Cross-Subdomain Relationship: Names exactly one work record
      Source Finding: 'S1 identity_and_sameness #2'
    - Store Name: Physical copy record
      Identity Field: Barcode
      Source: Assigned by the library and supplied when the copy is registered
      Uniqueness Rule: Two records carrying the same barcode describe the same copy, and the second is refused
      Cross-Subdomain Relationship: Names exactly one edition record
      Source Finding: 'S1 identity_and_sameness #3'
    - Store Name: Catalog audit trail
      Identity Field: Append position
      Source: Assigned when the entry is appended
      Uniqueness Rule: Each performed operation appends exactly one entry, and no entry is amended or removed
      Cross-Subdomain Relationship: Names the staff member who performed the operation
      Source Finding: S4 bm_entities Business Operation
    - Store Name: Edition identity registry
      Identity Field: The key formed from title, author and publication year
      Source: Formed by the catalog, unchanged from the previous change
      Uniqueness Rule: The key is claimed once; a second claim on it fails and the registration is refused
      Cross-Subdomain Relationship: None
      Source Finding: 'S4 constraint_register #9'
    - Store Name: Copy barcode registry
      Identity Field: Barcode
      Source: Assigned by the library
      Uniqueness Rule: The barcode is claimed once; a second claim on it fails and the copy registration is refused
      Cross-Subdomain Relationship: None
      Source Finding: 'S4 constraint_register #7'
  invariants:
    columns:
    - Invariant
    - Business Reason
    - Source Finding
    rows:
    - Invariant: Each edition belongs to exactly one work
      Business Reason: An edition is a publication of one published work; an edition recorded against two works would make the collection's description untrue
      Source Finding: 'S4 constraint_register #6'
    - Invariant: Each physical copy belongs to exactly one edition
      Business Reason: A copy the library owns is a copy of one publication, which is what a staff member holds when they hold it
      Source Finding: 'S4 constraint_register #7'
    - Invariant: No two works share the same title and author
      Business Reason: The library needs one place that says which works it holds, and two records for one work would defeat the grouping this change exists to provide
      Source Finding: 'S4 constraint_register #8'
    - Invariant: No two editions of a work share the same publication year
      Business Reason: Editions are told apart by when they were published, so two carrying the same year cannot be told apart at all
      Source Finding: 'S4 constraint_register #9'
    - Invariant: Every work has at least one edition
      Business Reason: A work enters the catalog because the library holds a publication of it; a work with no edition describes nothing the library has
      Source Finding: 'S4 constraint_register #10'
    - Invariant: A work is never retired
      Business Reason: A work whose editions are all retired is simply that, and retiring the work would hide editions whose details must remain retrievable
      Source Finding: 'S4 constraint_register #11'
    - Invariant: Every claim precedes every write in a registration
      Business Reason: A registration that is refused must leave nothing behind, including a work nobody asked for
      Source Finding: 'S4 constraint_register #12'
    - Invariant: A record written under the previous change remains valid and usable without recreation
      Business Reason: The library's existing catalogue is the collection; a change that required it to be rebuilt would be a new catalogue, not an extension
      Source Finding: 'S4 constraint_register #2'
    - Invariant: Every business operation performed against the catalog is traceable and auditable
      Business Reason: The library must be able to say afterwards who changed its description of itself, and how
      Source Finding: 'S4 constraint_register #5'
    - Invariant: Only authorized staff perform catalog operations
      Business Reason: The catalog is the library's authoritative description of its holdings and is not open to alteration by anyone who asks
      Source Finding: 'S4 constraint_register #1'
  actions:
    columns:
    - Action
    - Object
    - Trigger
    - Status (IN_SCOPE, DEFERRED)
    - Source Finding
    rows:
    - Action: Register
      Object: A work and its first edition, with that edition's first copy
      Trigger: Authorized staff register an edition of a work the catalog does not yet hold
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register an edition of a work the catalog does not yet hold
    - Action: Register
      Object: An additional edition of an existing work
      Trigger: Authorized staff register a further edition of a work the catalog already holds
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register an additional edition of an existing work
    - Action: Register
      Object: A physical copy of an edition
      Trigger: Authorized staff register a further copy against a registered edition
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Register a physical copy against exactly one edition
    - Action: Update
      Object: An edition's bibliographic information
      Trigger: Authorized staff change a registered edition's description
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Update an edition's bibliographic information
    - Action: Retire
      Object: An edition record or a physical copy
      Trigger: Authorized staff judge the record obsolete, or the copy lost or damaged
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retire and reinstate an edition independently of the work's other editions
    - Action: Reinstate
      Object: A retired edition record or physical copy
      Trigger: Authorized staff return the record to the registered state
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retire and reinstate an edition independently of the work's other editions
    - Action: Search
      Object: The catalog, answering at the level of the work
      Trigger: Authorized staff search by subject or title
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Search the catalog and answer at the level of the work
    - Action: Retrieve
      Object: An edition's complete details, with a summary of its work
      Trigger: Authorized staff select an edition and ask for everything about it
      Status (IN_SCOPE, DEFERRED): IN_SCOPE
      Source Finding: S4 capability_graph Retrieve an edition's complete details with a summary of its work
    - Action: Associate
      Object: An identifier, a taxonomy term, a digital resource or an image with a record
      Trigger: A future governed change takes the need up
      Status (IN_SCOPE, DEFERRED): DEFERRED
      Source Finding: S4 authoring_scope Deferred
  provisional_codes:
    columns:
    - Provisional Code
    - Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE)
    - Summary
    - Source Finding
    rows:
    - Provisional Code: IN_REGISTER_ADDITIONAL_EDITION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): IN
      Summary: A request to register a further edition of a work the catalog already holds
      Source Finding: S5 actions Register
    - Provisional Code: WF_REGISTER_ADDITIONAL_EDITION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): WF
      Summary: The governed sequence that registers a further edition of an existing work
      Source Finding: S5 actions Register
    - Provisional Code: CC_REGISTER_ADDITIONAL_EDITION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: Resolves the named work, claims the edition's identity, writes the edition record and records the operation
      Source Finding: S4 gap_register GAP-09
    - Provisional Code: CC_CLAIM_WORK_IDENTITY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: Claims a work's identity so that two registrations of one work do not produce two works
      Source Finding: S4 gap_register GAP-02
    - Provisional Code: CC_RESOLVE_WORK_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: Answers which work a title and author denote, and returns the work already registered
      Source Finding: S4 gap_register GAP-03
    - Provisional Code: CC_REGISTER_BOOK_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: 'Extended: claims the work alongside the edition and the barcode, before any record is written'
      Source Finding: S4 gap_register GAP-07
    - Provisional Code: CC_VALIDATE_BOOK_SUBMISSION_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: 'Extended: confirms a registration carries what a work requires as well as what an edition requires'
      Source Finding: S4 gap_register GAP-08
    - Provisional Code: CC_SEARCH_CATALOG_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: 'Extended: groups the matching editions under the work they belong to and answers one result per work'
      Source Finding: S4 gap_register GAP-10
    - Provisional Code: CC_ASSEMBLE_BOOK_DETAILS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CC
      Summary: 'Extended: carries a summary of the work the edition belongs to alongside the edition and its copies'
      Source Finding: S4 gap_register GAP-11
    - Provisional Code: CT_PURE_FORM_WORK_IDENTITY_KEY_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CT
      Summary: Forms the single key claimed for a work from its title and author
      Source Finding: S4 gap_register GAP-01
    - Provisional Code: CT_PURE_SELECT_RECORDS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CT
      Summary: Selects the records matching stated criteria and returns none when none match, so an edition the library holds no copies of can still be described
      Source Finding: S4 gap_register GAP-11
    - Provisional Code: CT_PURE_GROUP_RECORDS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): CT
      Summary: Groups selected records by an attribute they share, so a search can answer once per work
      Source Finding: S4 gap_register GAP-04
    - Provisional Code: EV_WORK_REGISTERED_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): EV
      Summary: The moment a work enters the catalog
      Source Finding: S4 gap_register GAP-13
    - Provisional Code: STRUCTURE_CATALOG_STORAGE_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): STRUCTURE
      Summary: 'Extended: declares the work record store and the work identity registry alongside the stores the catalog already owns'
      Source Finding: S4 gap_register GAP-05
    - Provisional Code: RB_CATALOG_BINDINGS_V0
      Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE): RB
      Summary: 'Extended: binds the work store and the work identity registry to the workflows that read and write them'
      Source Finding: S4 gap_register GAP-06
  cross_subdomain_refs:
    columns:
    - CC Code
    - Defined In
    - Role
    - Source Finding
    rows: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | p4_business_model_book_library_mgmt_catalog_v0.md | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | capability_graph · gap_register · constraint_register · design_decisions · authoring_scope · bm_entities · actors · events |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
