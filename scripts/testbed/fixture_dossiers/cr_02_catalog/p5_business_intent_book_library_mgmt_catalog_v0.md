# Stage 5 — Business Intent: book_library_mgmt / catalog

**Stage:** 5 — Business Intent
**CR:** cr_02_catalog
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

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

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | The seed states the change — that the record the previous change calls a book is an edition and that the work is added above it. This states the subdomain that results: the three records it holds, the authority it establishes over how they relate, the lifecycle it manages, and the four functions it does not govern. Nothing here contradicts the seed; what it adds is the standing description rather than the narrative of the change. |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Form the identifying key of a work from its title and author | IN_SCOPE | A different business key from the edition's; the edition key is not widened | S4 authoring_scope GAP-01 |
| Claim a work's identity so that two registrations of one work do not produce two works | IN_SCOPE | Claimed atomically, as the edition's identity is | S4 authoring_scope GAP-02 |
| Resolve the work an edition belongs to | IN_SCOPE | Answers which work a title and author denote | S4 authoring_scope GAP-03 |
| Group selected records by an attribute they share | IN_SCOPE | Selection already exists; grouping does not | S4 authoring_scope GAP-04 |
| Declare the stores the catalog owns | IN_SCOPE | Extended with the work store and the work identity registry | S4 authoring_scope GAP-05 |
| Bind the catalog's workflows to the stores they use | IN_SCOPE | Extended so the new stores are reachable | S4 authoring_scope GAP-06 |
| Register an edition of a work the catalog does not yet hold | IN_SCOPE | Gains a work claim among the claims, before any write | S4 authoring_scope GAP-07 |
| Validate that a registration carries what a work and an edition require | IN_SCOPE | Runs before any claim, as it does today | S4 authoring_scope GAP-08 |
| Register an additional edition of an existing work | IN_SCOPE | The operation this change exists to add | S4 authoring_scope GAP-09 |
| Search the catalog and answer at the level of the work | IN_SCOPE | Search terms unchanged; one result per matching work | S4 authoring_scope GAP-10 |
| Retrieve an edition's complete details with a summary of its work | IN_SCOPE | Retrieval stays edition retrieval | S4 authoring_scope GAP-11 |
| Admit a request to register an additional edition of an existing work | IN_SCOPE | A new operation is reached through its own entry point | S4 authoring_scope GAP-12 |
| Recognise the moment a work enters the catalog | IN_SCOPE | The catalog declares a moment for each thing that enters it | S4 authoring_scope GAP-13 |
| Multiple identifiers for one publication | DEFERRED | What an identifier identifies could not be answered until an edition was defined | S4 authoring_scope Deferred |
| A governed subject taxonomy | DEFERRED | A further catalog need, deferred to a change of its own | S4 authoring_scope Deferred |
| Digital resources associated with catalog records | DEFERRED | A further catalog need, deferred to a change of its own | S4 authoring_scope Deferred |
| Images associated with catalog records | DEFERRED | A further catalog need, deferred to a change of its own | S4 authoring_scope Deferred |
| Deciding which staff are authorized | DEFERRED | Belongs to the staff function, which a future change introduces | S4 authoring_scope Deferred |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Work record | MUTABLE_STATE | The library needs one place that says which works it holds; a work's description is corrected in place rather than re-registered | S4 bm_entities Work |
| Work identity registry | IDENTITY_REGISTRY | Two registrations describing the same work must not produce two works, and only an atomic claim can guarantee that | S4 resources The work identity registry |
| Edition record | MUTABLE_STATE | Unchanged from the previous change: an edition's description is corrected in place and its state moves both ways | S4 bm_entities Edition |
| Physical copy record | MUTABLE_STATE | Unchanged from the previous change: a copy's state moves both ways on the same record | S4 bm_entities Physical Copy |
| Catalog audit trail | APPEND_ONLY_JOURNAL | Unchanged from the previous change: an operation that has been performed cannot be un-performed, so its record is never amended | S4 bm_entities Business Operation |
| Edition identity registry | IDENTITY_REGISTRY | Unchanged from the previous change: no two editions share a title, author and publication year | S4 constraint_register #9 |
| Copy barcode registry | IDENTITY_REGISTRY | Unchanged from the previous change: no two copies share a barcode | S4 constraint_register #7 |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Work record | Title and author together | Supplied by the staff member registering the first edition of the work | Two registrations carrying the same title and author describe the same work, and the second names the work that exists rather than creating another | None | S1 identity_and_sameness #1 |
| Work identity registry | The key formed from title and author | Formed by the catalog from the two identifying attributes | The key is claimed once; a second claim on it resolves to the work already registered rather than refusing | None | S4 design_decisions #3 |
| Edition record | Title, author and publication year together | Supplied by the staff member registering the edition | Two registrations carrying the same title, author and publication year describe the same edition, and the second is refused | Names exactly one work record | S1 identity_and_sameness #2 |
| Physical copy record | Barcode | Assigned by the library and supplied when the copy is registered | Two records carrying the same barcode describe the same copy, and the second is refused | Names exactly one edition record | S1 identity_and_sameness #3 |
| Catalog audit trail | Append position | Assigned when the entry is appended | Each performed operation appends exactly one entry, and no entry is amended or removed | Names the staff member who performed the operation | S4 bm_entities Business Operation |
| Edition identity registry | The key formed from title, author and publication year | Formed by the catalog, unchanged from the previous change | The key is claimed once; a second claim on it fails and the registration is refused | None | S4 constraint_register #9 |
| Copy barcode registry | Barcode | Assigned by the library | The barcode is claimed once; a second claim on it fails and the copy registration is refused | None | S4 constraint_register #7 |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Each edition belongs to exactly one work | An edition is a publication of one published work; an edition recorded against two works would make the collection's description untrue | S4 constraint_register #6 |
| Each physical copy belongs to exactly one edition | A copy the library owns is a copy of one publication, which is what a staff member holds when they hold it | S4 constraint_register #7 |
| No two works share the same title and author | The library needs one place that says which works it holds, and two records for one work would defeat the grouping this change exists to provide | S4 constraint_register #8 |
| No two editions of a work share the same publication year | Editions are told apart by when they were published, so two carrying the same year cannot be told apart at all | S4 constraint_register #9 |
| Every work has at least one edition | A work enters the catalog because the library holds a publication of it; a work with no edition describes nothing the library has | S4 constraint_register #10 |
| A work is never retired | A work whose editions are all retired is simply that, and retiring the work would hide editions whose details must remain retrievable | S4 constraint_register #11 |
| Every claim precedes every write in a registration | A registration that is refused must leave nothing behind, including a work nobody asked for | S4 constraint_register #12 |
| A record written under the previous change remains valid and usable without recreation | The library's existing catalogue is the collection; a change that required it to be rebuilt would be a new catalogue, not an extension | S4 constraint_register #2 |
| Every business operation performed against the catalog is traceable and auditable | The library must be able to say afterwards who changed its description of itself, and how | S4 constraint_register #5 |
| Only authorized staff perform catalog operations | The catalog is the library's authoritative description of its holdings and is not open to alteration by anyone who asks | S4 constraint_register #1 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Register | A work and its first edition, with that edition's first copy | Authorized staff register an edition of a work the catalog does not yet hold | IN_SCOPE | S4 capability_graph Register an edition of a work the catalog does not yet hold |
| Register | An additional edition of an existing work | Authorized staff register a further edition of a work the catalog already holds | IN_SCOPE | S4 capability_graph Register an additional edition of an existing work |
| Register | A physical copy of an edition | Authorized staff register a further copy against a registered edition | IN_SCOPE | S4 capability_graph Register a physical copy against exactly one edition |
| Update | An edition's bibliographic information | Authorized staff change a registered edition's description | IN_SCOPE | S4 capability_graph Update an edition's bibliographic information |
| Retire | An edition record or a physical copy | Authorized staff judge the record obsolete, or the copy lost or damaged | IN_SCOPE | S4 capability_graph Retire and reinstate an edition independently of the work's other editions |
| Reinstate | A retired edition record or physical copy | Authorized staff return the record to the registered state | IN_SCOPE | S4 capability_graph Retire and reinstate an edition independently of the work's other editions |
| Search | The catalog, answering at the level of the work | Authorized staff search by subject or title | IN_SCOPE | S4 capability_graph Search the catalog and answer at the level of the work |
| Retrieve | An edition's complete details, with a summary of its work | Authorized staff select an edition and ask for everything about it | IN_SCOPE | S4 capability_graph Retrieve an edition's complete details with a summary of its work |
| Associate | An identifier, a taxonomy term, a digital resource or an image with a record | A future governed change takes the need up | DEFERRED | S4 authoring_scope Deferred |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, STRUCTURE) | Summary | Source Finding |
|------------------|-------------------------|---------|----------------|
| IN_REGISTER_ADDITIONAL_EDITION_V0 | IN | A request to register a further edition of a work the catalog already holds | S5 actions Register |
| WF_REGISTER_ADDITIONAL_EDITION_V0 | WF | The governed sequence that registers a further edition of an existing work | S5 actions Register |
| CC_REGISTER_ADDITIONAL_EDITION_V0 | CC | Resolves the named work, claims the edition's identity, writes the edition record and records the operation | S4 gap_register GAP-09 |
| CC_CLAIM_WORK_IDENTITY_V0 | CC | Claims a work's identity so that two registrations of one work do not produce two works | S4 gap_register GAP-02 |
| CC_RESOLVE_WORK_V0 | CC | Answers which work a title and author denote, and returns the work already registered | S4 gap_register GAP-03 |
| CC_REGISTER_BOOK_V0 | CC | Extended: claims the work alongside the edition and the barcode, before any record is written | S4 gap_register GAP-07 |
| CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | Extended: confirms a registration carries what a work requires as well as what an edition requires | S4 gap_register GAP-08 |
| CC_SEARCH_CATALOG_V0 | CC | Extended: groups the matching editions under the work they belong to and answers one result per work | S4 gap_register GAP-10 |
| CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | Extended: carries a summary of the work the edition belongs to alongside the edition and its copies | S4 gap_register GAP-11 |
| CT_PURE_FORM_WORK_IDENTITY_KEY_V0 | CT | Forms the single key claimed for a work from its title and author | S4 gap_register GAP-01 |
| CT_PURE_SELECT_RECORDS_V0 | CT | Selects the records matching stated criteria and returns none when none match, so an edition the library holds no copies of can still be described | S4 gap_register GAP-11 |
| CT_PURE_GROUP_RECORDS_V0 | CT | Groups selected records by an attribute they share, so a search can answer once per work | S4 gap_register GAP-04 |
| EV_WORK_REGISTERED_V0 | EV | The moment a work enters the catalog | S4 gap_register GAP-13 |
| STRUCTURE_CATALOG_STORAGE_V0 | STRUCTURE | Extended: declares the work record store and the work identity registry alongside the stores the catalog already owns | S4 gap_register GAP-05 |
| RB_CATALOG_BINDINGS_V0 | RB | Extended: binds the work store and the work identity registry to the workflows that read and write them | S4 gap_register GAP-06 |
---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|

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
