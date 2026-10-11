# Stage 2 — Domain Model Discovery: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 2 — Domain Model Discovery
  CR: cr_03_catalog
  Status: DRAFT
  Feeds: Stage 3 — Analysis Loop
registers:
  entities:
    columns:
    - Entity
    - Description
    - Store Model
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Work
      Description: Something the library carries, independent of any edition.
      Store Model: Held by the catalog.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #1'
    - Entity: Book
      Description: An edition of a work.
      Store Model: Held by the catalog.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #2'
    - Entity: Physical copy
      Description: One copy of a book, on a shelf.
      Store Model: Held by the catalog.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #3'
    - Entity: Moment
      Description: Something the catalog announces because the business declared it matters.
      Store Model: Declared, and referred to by nothing.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_vocabulary #7'
  entity_attributes:
    columns:
    - Entity
    - Attribute
    - Meaning
    - Evidence Status
    - Source Finding
    rows:
    - Entity: Moment
      Attribute: What it names
      Meaning: The act whose completion it announces.
      Evidence Status: VERIFIED
      Source Finding: 'S1 business_events #1'
    - Entity: Moment
      Attribute: Whether it is announced
      Meaning: Whether anything in the composition refers to it.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #1'
    - Entity: Book
      Attribute: State
      Meaning: Whether it is in service or retired.
      Evidence Status: VERIFIED
      Source Finding: 'S1 lifecycle_states #1'
    - Entity: Physical copy
      Attribute: State
      Meaning: Whether it is in service or retired.
      Evidence Status: VERIFIED
      Source Finding: 'S1 lifecycle_states #3'
  business_processes:
    columns:
    - Process
    - Initiator
    - Outcome
    - Evidence Status
    - Source Finding
    rows:
    - Process: Registering a work, a book or a physical copy
      Initiator: The library
      Outcome: The thing is held by the catalog.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #2'
    - Process: Correcting bibliographic information
      Initiator: The library
      Outcome: What the library publishes is changed.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #2'
    - Process: Retiring a book or a physical copy
      Initiator: The library
      Outcome: The thing is out of service; what is known about it is kept.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #2'
    - Process: Reinstating a book or a physical copy
      Initiator: The library
      Outcome: The thing is back in service.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #4'
    - Process: Announcing a moment
      Initiator: The completion of the act it names
      Outcome: Nothing. No act announces anything today.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 system_beliefs #1'
  process_steps:
    columns:
    - Process
    - 'Step #'
    - Action
    - Record Produced
    - Evidence Status
    - Source Finding
    rows:
    - Process: Announcing a moment
      'Step #': '1'
      Action: Complete the act the moment names.
      Record Produced: The act's own record.
      Evidence Status: VERIFIED
      Source Finding: 'S1 known_facts #3'
    - Process: Announcing a moment
      'Step #': '2'
      Action: Announce the moment, carrying which thing it concerns and when.
      Record Produced: The announcement.
      Evidence Status: NOT_FOUND
      Source Finding: 'S1 known_facts #7'
  belief_verification:
    columns:
    - Belief
    - Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE)
    - Evidence
    - Source Finding
    rows:
    - Belief: The catalog declares six moments and announces none of them.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: Six are declared — `book_library_mgmt::EV_WORK_REGISTERED_V0`, `EV_BOOK_REGISTERED_V0`, `EV_PHYSICAL_COPY_REGISTERED_V0`, `EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0`, `EV_BOOK_RETIRED_V0`, `EV_PHYSICAL_COPY_RETIRED_V0`. Each reports a reference count of zero, and no workflow in the domain announces anything at all.
      Source Finding: 'S1 system_beliefs #1'
    - Belief: The catalog performs registration, correction, retirement and reinstatement, each as its own act.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: Ten workflows are held for this subdomain, including registration of a book, an additional edition and a physical copy; correction of bibliographic information; retirement and reinstatement of both a book record and a physical copy.
      Source Finding: 'S1 system_beliefs #2'
    - Belief: Nothing checks whether a declared moment is ever announced.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: No rule relates a declared moment to a reference to it. The six have been declared and silent since the subdomain was built, and nothing has reported a fault.
      Source Finding: 'S1 system_beliefs #3'
    - Belief: Reinstatement has no declared moment of its own.
      Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE): VERIFIED
      Evidence: Two workflows reinstate, and neither a book reinstated nor a copy reinstated appears among the six declared moments. The business's ruling that reinstatement is silent and the composition agree.
      Source Finding: 'S1 system_beliefs #4'
  pps_baseline_fqdns:
    columns:
    - Capability
    - FQDN
    - What It Does
    - Fit (EXACT, PARTIAL, MISMATCH)
    - Cannot Do
    rows:
    - Capability: Registers a book
      FQDN: book_library_mgmt::WF_REGISTER_BOOK_V0
      What It Does: Registers an edition of a work.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Registers an additional edition
      FQDN: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
      What It Does: Registers a further edition of a work already carried.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Registers a physical copy
      FQDN: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
      What It Does: Puts a copy on a shelf.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Corrects bibliographic information
      FQDN: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      What It Does: Changes what the library publishes about a book.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Retires a book
      FQDN: book_library_mgmt::WF_RETIRE_BOOK_RECORD_V0
      What It Does: Takes an edition out of service.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Retires a physical copy
      FQDN: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
      What It Does: Takes a copy out of service.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Announces nothing.
    - Capability: Reinstates a book
      FQDN: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
      What It Does: Returns an edition to service.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing; the business has ruled reinstatement silent.
    - Capability: Reinstates a physical copy
      FQDN: book_library_mgmt::WF_REINSTATE_PHYSICAL_COPY_V0
      What It Does: Returns a copy to service.
      Fit (EXACT, PARTIAL, MISMATCH): EXACT
      Cannot Do: Nothing; the business has ruled reinstatement silent.
    - Capability: Declares that a work was registered
      FQDN: book_library_mgmt::EV_WORK_REGISTERED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: Is referred to by nothing and is therefore never announced.
    - Capability: Declares that a book was registered
      FQDN: book_library_mgmt::EV_BOOK_REGISTERED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: The same.
    - Capability: Declares that a physical copy was registered
      FQDN: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: The same.
    - Capability: Declares that bibliographic information was updated
      FQDN: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: The same.
    - Capability: Declares that a book was retired
      FQDN: book_library_mgmt::EV_BOOK_RETIRED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: The same.
    - Capability: Declares that a physical copy was retired
      FQDN: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
      What It Does: Names the moment.
      Fit (EXACT, PARTIAL, MISMATCH): PARTIAL
      Cannot Do: The same.
  gaps:
    columns:
    - Gap
    - Severity
    - Impact
    - Evidence Status
    - Source Finding
    rows:
    - Gap: No act announces any moment.
      Severity: CRITICAL
      Impact: The whole of this change. Six declared moments are silent.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #1'
    - Gap: Nothing checks that a declared moment is announced.
      Severity: CRITICAL
      Impact: The silence returned unnoticed once and would again.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #3'
    - Gap: The moment naming a registered work has no single act that plainly produces it.
      Severity: OPEN QUESTION
      Impact: Registration of a book and of an additional edition both concern works; which announces a work registered is not evident from the composition.
      Evidence Status: VERIFIED
      Source Finding: 'S1 assumptions #1'
  architectural_observations:
    columns:
    - Observation
    - Evidence
    - Evidence Status
    - Source Finding
    rows:
    - Observation: A declared moment that nothing refers to is indistinguishable, from the outside, from a moment the business never declared.
      Evidence: Reference count of zero on all six.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #1'
    - Observation: This is the same defect a different domain was found to have, in the same shape and for the same reason.
      Evidence: Six moments here; three in the identity function of another domain, all silent, none checked.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #3'
    - Observation: Every act this change touches already exists and needs no new capability. Only where each act ends is changed.
      Evidence: Ten workflows held for this subdomain, all performing their acts today.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #2'
    - Observation: The business's ruling and the composition agree that reinstatement is silent, so this change removes a question rather than answering one.
      Evidence: Two reinstatement workflows, no declared moment for either.
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #4'
  discovery_concerns:
    columns:
    - Concern
    - Evidence
    - Severity
    - Evidence Status
    - Source Finding
    rows:
    - Concern: The business believed the catalog announced six moments and it announced none. Nothing reported a fault, because nothing checks.
      Evidence: Reference count of zero on all six, and no announcement anywhere in the domain.
      Severity: CRITICAL
      Evidence Status: VERIFIED
      Source Finding: 'S1 system_beliefs #1'
    - Concern: Two acts register something that concerns a work, and only one moment names a work registered. Attaching it to the wrong act would announce something untrue.
      Evidence: Registration of a book and of an additional edition both exist.
      Severity: MAJOR
      Evidence Status: VERIFIED
      Source Finding: 'S1 assumptions #1'
  open_questions:
    columns:
    - Question
    - Category
    - Why It Matters
    - Source Finding
    rows:
    - Question: Which act announces that a work was registered — registering a book, or registering an additional edition?
      Category: business
      Why It Matters: A moment attached to the wrong act announces something untrue.
      Source Finding: 'S1 assumptions #1'
```

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface. What was searched is recorded, not only what was found.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3
