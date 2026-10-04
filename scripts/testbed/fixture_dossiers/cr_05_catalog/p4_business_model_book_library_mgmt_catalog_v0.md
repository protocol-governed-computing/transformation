# Stage 4 — Business Model: book_library_mgmt / catalog

**Stage:** 4 — Business Model

**CR:** cr_05_catalog

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one the catalog already has: each step keeps doing what it does, and holds the
rule it applies instead of being handed it.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized staff | Performs catalog operations. | Internal staff | S1 known_facts #1 |
| The staff function | Decides which staff are authorized. | Adjacent subdomain | S1 known_facts #2 |
| The catalog | Holds the library's records, and now every rule it applies to them. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Book | Title, author, publication year, subject and state. | One keyed store, one record per book, unchanged. | S2 entities #1 |
| The Physical Copy | One copy of a book, and its state. | One keyed store, one record per barcode, unchanged. | S2 entities #2 |
| The Catalog's Rules | Who may perform a catalog operation, and what a book, a work and a further edition must contain. | Held by the catalog steps that apply them. Held by nothing today. | S3 analysis_findings Q1 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments the catalog announces are unchanged. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| The catalog | refuses | anyone the library has not authorized | Refuse anyone the library has not authorized | S3 authoring_decisions Refuse anyone the library has not authorized |
| The catalog | refuses | a registration missing what it must contain | Refuse a registration the catalog finds incomplete | S3 authoring_decisions Refuse a registration the catalog finds incomplete |
| The catalog | records | a copy as registered | Register a copy as registered | S3 authoring_decisions Register a copy as registered |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Refuse anyone the library has not authorized | S3 authoring_decisions Refuse anyone the library has not authorized | CRITICAL | GAP-01 | The confirming step holds the library's rules. |
| Refuse a registration the catalog finds incomplete | S3 authoring_decisions Refuse a registration the catalog finds incomplete | CRITICAL | GAP-02 | A rule following each check refuses on what it found. |
| Hold what a book, a work and a further edition must contain | S3 authoring_decisions Hold what a book, a work and a further edition must contain | CRITICAL | GAP-03 | The checking contracts hold their descriptions. |
| Check what the catalog records | S3 authoring_decisions Check what the catalog records | CRITICAL | GAP-04 | Each registration act checks the record it writes. |
| Record the subject callers supply | S3 authoring_decisions Record the subject callers supply | CRITICAL | GAP-05 | The register act reads the subject where callers send it. |
| Register a copy as registered | S3 authoring_decisions Register a copy as registered | CRITICAL | GAP-06 | The copy contract writes the state itself. |
| Keep a corrected record's state, and check it against the book description | S3 authoring_decisions Keep a corrected record's state, and check it against the book description | CRITICAL | GAP-07 | The correction keeps the state and refuses a record that fails the description. |
| Admit a request without the rules the catalog holds | S3 authoring_decisions Admit a request without the rules the catalog holds | CRITICAL | GAP-08 | The gates stop requiring what the catalog holds and what no act reads. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| catalog | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | platform transform | SATISFIED | S3 dependency_discoveries Refusing on a list of rules |
| catalog | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | platform transform | SATISFIED | S3 dependency_discoveries Checking a record's structure |
| catalog | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | platform transform | SATISFIED | S3 dependency_discoveries Assembling a record from fields |
| catalog | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | amended contract | SATISFIED | S3 dependency_discoveries Confirming staff |
| catalog | book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 | amended contract | SATISFIED | S3 dependency_discoveries Checking a submission |
| catalog | book_library_mgmt::CC_REGISTER_BOOK_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording a book |
| catalog | book_library_mgmt::CC_REGISTER_ADDITIONAL_EDITION_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording an edition |
| catalog | book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording a copy |
| catalog | book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | amended contract | SATISFIED | S3 dependency_discoveries Correcting a record |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every correct request from authorized staff is admitted, with the same outcome as today. | S1 constraints #1 | The business author |
| 2 | Records made under a request's own rules stay as they were made. | S1 constraints #2 | The business author |
| 3 | What a request says about the catalog's rules is ignored, not refused. | S1 known_facts #9 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Refuse anyone the library has not authorized | Refuse anyone the library has not authorized | catalog | EXTEND |
| GAP-02 | S3 authoring_decisions Refuse a registration the catalog finds incomplete | Refuse a registration the catalog finds incomplete | catalog | EXTEND |
| GAP-03 | S3 authoring_decisions Hold what a book, a work and a further edition must contain | Hold what a book, a work and a further edition must contain | catalog | EXTEND |
| GAP-04 | S3 authoring_decisions Check what the catalog records | Check what the catalog records | catalog | EXTEND |
| GAP-05 | S3 authoring_decisions Record the subject callers supply | Record the subject callers supply | catalog | EXTEND |
| GAP-06 | S3 authoring_decisions Register a copy as registered | Register a copy as registered | catalog | EXTEND |
| GAP-07 | S3 authoring_decisions Keep a corrected record's state, and check it against the book description | Keep a corrected record's state, and check it against the book description | catalog | EXTEND |
| GAP-08 | S3 authoring_decisions Admit a request without the rules the catalog holds | Admit a request without the rules the catalog holds | catalog | EXTEND |
| GAP-09 | S3 analysis_findings Q9 | Establish who a caller is | outside the catalog | DEFERRED |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Each rule is held by the step that applies it, as a fixed value. | S3 analysis_findings Q1 | A rule written where it is applied holds for every act that composes the step, and no request can widen it. | Nothing may hand the catalog a rule the catalog holds. |
| 2 | Each check is followed by a rule refusing when it found anything. | S3 analysis_findings Q2 | The platform check stays a reporter, as ruled; the catalog's contract decides. | A check's report is consumed, never left unread. |
| 3 | What each registration checks is the record it writes. | S3 analysis_findings Q4 | A check of a supplied copy judges something other than what is recorded. | No registration checks a copy supplied beside the record. |
| 4 | The register act records the subject where callers send it. | S3 analysis_findings Q5 | Every present caller sends it there, and every book recorded today lacks one. | No present caller changes what it sends. |
| 5 | A copy's registered state and a correction's state are the catalog's own. | S3 analysis_findings Q6 | There is one state a copy is registered in, and a correction does not change state. | No request sets a registered copy's or a corrected book's state. |
| 6 | The gates stop requiring what the catalog holds and what no act reads. | S3 analysis_findings Q8 | A gate requiring an unread field refuses a correct request for its absence. | Every field an act reads stays required where it was. |
| 7 | Records made before this change are left as they are. | S3 analysis_findings Q10 | The record is added to and never rewritten. | No migration, backfill or repair step may be authored. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Refuse anyone the library has not authorized | GAP-01 |
| Refuse a registration the catalog finds incomplete | GAP-02 |
| Hold what a book, a work and a further edition must contain | GAP-03 |
| Check what the catalog records | GAP-04 |
| Record the subject callers supply | GAP-05 |
| Register a copy as registered | GAP-06 |
| Keep a corrected record's state, and check it against the book description | GAP-07 |
| Admit a request without the rules the catalog holds | GAP-08 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Establish who a caller is | GAP-09. The credentials a request presents are its own; the catalog holds the rules they are judged by and does not authenticate them. |
| Records made under a request's own rules | Declined by the business: the record is added to and never rewritten. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
