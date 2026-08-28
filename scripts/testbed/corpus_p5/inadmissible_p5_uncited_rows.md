# Business Intent — book_library_mgmt / catalog (deliberately inadmissible fixture))

> Every row below is authored; what is wrong with each is where it says it came from.

**Stage:** 5 — Business Intent
**CR:** cr_01_catalog
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The catalog governs the library's authoritative description of what it holds: one record for each book
it catalogs, and one for each physical copy it owns. It establishes the authority to state what the
library has — a book exists in the collection because the catalog says so, and a copy belongs to
exactly one book because the catalog records it that way. It manages the lifecycle of both records
from registration through retirement and back, and it records every operation performed against it so
that any change to the library's description of itself can be traced afterwards. It exists because
those records are maintained by hand today, which produces inconsistent descriptions, duplicate
entries and difficulty locating materials. It does not govern who borrows the collection, what is
ordered, who the library's patrons are, or which staff are authorized.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | States the authority the subdomain establishes — a book exists in the collection because the catalog says so — the lifecycle it manages from registration through retirement and back, and the four functions it explicitly does not govern. The seed states what the catalog is for and why it exists; none of these four additions contradicts it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| catalog | Governs the library's authoritative description of what it holds — one record per book it catalogs and one per physical copy it owns — and the lifecycle of both from registration through retirement and back. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Register a book together with its first physical copy | IN_SCOPE | A book is never registered without a copy | S4 authoring_scope GAP-05 |
| Register a further physical copy against a registered book | IN_SCOPE | Refused if the barcode is already owned or the book is not registered | S4 authoring_scope GAP-06 |
| Update a book's bibliographic information | IN_SCOPE | Refused if the change would make the book a duplicate of another | S4 authoring_scope GAP-07 |
| Retire a book record | IN_SCOPE | Leaves the book's copies untouched | S4 authoring_scope GAP-08 |
| Retire a physical copy | IN_SCOPE | Leaves the book record untouched, including when it was the last copy | S4 authoring_scope GAP-09 |
| Return a retired book record to the registered state | IN_SCOPE | Reinstatement is explicit, never derived | S4 authoring_scope GAP-10 |
| Return a retired physical copy to the registered state | IN_SCOPE | Reinstatement is explicit, never derived | S4 authoring_scope GAP-11 |
| Search the catalog by subject or title | IN_SCOPE | Retired books are excluded from results | S4 authoring_scope GAP-12 |
| Retrieve a book's complete details with the copies held | IN_SCOPE | Serves retired books as well as registered ones | S4 authoring_scope GAP-13 |
| Confirm the staff member performing an operation is authorized | IN_SCOPE | The catalog reads authorization; it never grants it | S4 authoring_scope GAP-04 |
| Record every performed catalog operation in the catalog's own audit trail | IN_SCOPE | The catalog owns the trail it appends to | S4 authoring_scope GAP-01 |
| Read every book record so that a search can select among them by content | IN_SCOPE | An existing mechanism amended to publish records; owned by platform, not by the catalog | S4 authoring_scope GAP-17 |
| Deciding which staff are authorized | DEFERRED | Belongs to the staff function, which a future change request introduces | S1 authority_deferrals #1 |
| Deleting a catalog record | DEFERRED | Not deferred but excluded: a record is never deleted, so no capability is authored for it | S1 business_invariants #9 |
| Importing the records staff maintain manually today | DEFERRED | The catalog starts empty | S1 out_of_scope Import of the records staff maintain manually today |
| Circulation, patron, staff, reservations, acquisitions, inventory, notifications, policy and reporting | DEFERRED | The nine remaining project functions, adjacent and untouched | S1 governance_scope #2 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Book record | MUTABLE_STATE | The library requires one authoritative record per book, its bibliographic information is correctable, and its state moves from registered to retired and back on the same record | S0 business_invariants #99 |
| Physical copy record | MUTABLE_STATE | The library requires one authoritative record per copy it owns, and a copy's state moves both ways on the same record | S4 bm_entities Physical Copy |
| Catalog audit trail | APPEND_ONLY_JOURNAL | Every operation must be traceable afterwards, and a trail that could be amended would not be evidence | S4 resources Catalog audit trail |
| Book identity registry | IDENTITY_REGISTRY | Duplicate prevention needs an atomic claim on a book's identity at the moment of registration | S4 design_decisions #3 |
| Copy barcode registry | IDENTITY_REGISTRY | No two copies the library owns may share a barcode, and the claim must hold at the moment of registration | S1 business_invariants #6 |

No record is ever deleted. Retirement is the only way a record leaves use, and it is reversible, which
is why both record stores hold state as data rather than by which store a record occupies.

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Book record | Title, author and publication year together | Supplied by the staff member registering the book | Two registrations carrying the same publication year, and the same title and author without regard to letter case or repeated spacing, describe the same book, and the second is refused | None | S1 identity_and_sameness #1 |
| Physical copy record | Barcode | Assigned by the library and supplied when the copy is registered | Two records carrying the same barcode describe the same copy, and the second is refused | Names exactly one book record | S1 identity_and_sameness #2 |
| Catalog audit trail | Append position | Assigned when the entry is appended | Each performed operation appends exactly one entry, and no entry is amended or removed | Names the staff member who performed the operation | S4 resources Catalog audit trail |
| Book identity registry | The key formed from title, author and publication year | Formed by the catalog, comparing title and author without regard to letter case or repeated spacing | The key is claimed once; a second claim on it fails and the registration is refused | None | S4 design_decisions #3 |
| Copy barcode registry | Barcode | Assigned by the library | The barcode is claimed once; a second claim on it fails and the copy registration is refused | None | S1 business_invariants #6 |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Each physical copy belongs to exactly one book | A copy the library owns is a copy of one published thing; a copy recorded against two books would make the collection's description untrue |  |
| Each book the library holds has exactly one authoritative record | The library needs one place that says what it holds, which is what CC_REGISTER_BOOK_V0 is for | S1 business_invariants #2 |
| Each physical copy the library owns has exactly one authoritative record | Two records for one copy would make the library's count of what it owns unreliable | S1 business_invariants #3 |
| No two registered books share the same title, author and publication year | Duplicate entries are the pain this change exists to remove | S1 business_invariants #4 |
| A book carries at least one subject | Subject is what staff search on when looking for material rather than a known title, so a book with none could not be found that way | S1 business_invariants #5 |
| No two physical copies the library owns share the same barcode | A barcode is how staff name one copy among several of the same book, including when retiring one | S1 business_invariants #6 |
| Every business operation performed against the catalog is traceable and auditable | The library must be able to account afterwards for every change to its description of itself | S1 business_invariants #7 |
| Only authorized staff perform catalog operations | The catalog is the library's authoritative record, and an unauthorized change to it would not be authoritative | S1 business_invariants #8 |
| No catalog record is ever deleted | Retirement is the only way a record leaves use; a deleted record would leave its audit trail pointing at nothing | S1 business_invariants #9 |
| A registered book always has at the moment of registration at least one physical copy | The library catalogs what it holds, and a book it holds no copy of is not a holding | S1 operation_refusals #2 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Register | Book, with its first physical copy | An authorized staff member registers a book the library has acquired | IN_SCOPE | S4 registration_register Register a book |
| Register | Physical copy | An authorized staff member records a further copy of a registered book | IN_SCOPE | S4 capability_graph Register a further physical copy against a registered book |
| Update | Book's bibliographic information | An authorized staff member corrects or changes a book's description | IN_SCOPE | S4 capability_graph Update a book's bibliographic information |
| Retire | Book record | An authorized staff member judges the record obsolete | IN_SCOPE | S4 capability_graph Retire a book record |
| Retire | Physical copy | A copy is lost or damaged | IN_SCOPE | S4 capability_graph Retire a physical copy |
| Reinstate | Book record | An authorized staff member returns a retired book to use | IN_SCOPE | S4 capability_graph Return a retired book record to the registered state |
| Reinstate | Physical copy | An authorized staff member returns a retired copy to use | IN_SCOPE | S4 capability_graph Return a retired physical copy to the registered state |
| Search | Catalog | An authorized staff member looks for material by subject or by title | IN_SCOPE | S4 capability_graph Search the catalog by subject or title, excluding retired books |
| Retrieve | Book's complete details | An authorized staff member asks what the library holds of one book | IN_SCOPE | S4 capability_graph Retrieve a book's complete details with the copies the library holds |
| Delete | Book record or physical copy | Never — no trigger exists, because a record is never deleted | DEFERRED | S1 business_invariants #9 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| catalog | AC_LIBRARY_STAFF_V0 | AC | The authorized staff member who performs a catalog operation | S4 actors Authorized staff member |
| catalog | IN_REGISTER_BOOK_V0 | IN | A request to register a book together with its first physical copy | S5 actions Register |
| catalog | IN_REGISTER_PHYSICAL_COPY_V0 | IN | A request to register a further copy against a registered book | S5 actions Register |
| catalog | IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | IN | A request to change a registered book's description | S5 actions Update |
| catalog | IN_RETIRE_BOOK_RECORD_V0 | IN | A request to retire a book record judged obsolete | S5 actions Retire |
| catalog | IN_RETIRE_PHYSICAL_COPY_V0 | IN | A request to retire a lost or damaged copy | S5 actions Retire |
| catalog | IN_REINSTATE_BOOK_RECORD_V0 | IN | A request to return a retired book record to the registered state | S5 actions Reinstate |
| catalog | IN_REINSTATE_PHYSICAL_COPY_V0 | IN | A request to return a retired copy to the registered state | S5 actions Reinstate |
| catalog | IN_SEARCH_CATALOG_V0 | IN | A request to locate material by subject or by title | S5 actions Search |
| catalog | IN_RETRIEVE_BOOK_DETAILS_V0 | IN | A request for a book's complete details with the copies held | S5 actions Retrieve |
| catalog | WF_REGISTER_BOOK_V0 | WF | Registering a book and its first copy, end to end | S4 capability_graph Register a book together with its first physical copy |
| catalog | WF_REGISTER_PHYSICAL_COPY_V0 | WF | Registering a further copy against a registered book | S4 capability_graph Register a further physical copy against a registered book |
| catalog | WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | WF | Changing a book's description without making it a duplicate | S4 capability_graph Update a book's bibliographic information |
| catalog | WF_RETIRE_BOOK_RECORD_V0 | WF | Retiring a book record, leaving its copies untouched | S4 capability_graph Retire a book record |
| catalog | WF_RETIRE_PHYSICAL_COPY_V0 | WF | Retiring a copy, leaving the book record untouched | S4 capability_graph Retire a physical copy |
| catalog | WF_REINSTATE_BOOK_RECORD_V0 | WF | Returning a retired book record to the registered state | S4 capability_graph Return a retired book record to the registered state |
| catalog | WF_REINSTATE_PHYSICAL_COPY_V0 | WF | Returning a retired copy to the registered state | S4 capability_graph Return a retired physical copy to the registered state |
| catalog | WF_SEARCH_CATALOG_V0 | WF | Searching by subject or title, excluding retired books, and recording that it happened | S4 capability_graph Search the catalog by subject or title, excluding retired books |
| catalog | WF_RETRIEVE_BOOK_DETAILS_V0 | WF | Assembling a book with the copies the library holds of it | S4 capability_graph Retrieve a book's complete details with the copies the library holds |
| catalog | CC_CONFIRM_STAFF_AUTHORIZED_V0 | CC | Confirm the staff member may perform catalog operations | S4 capability_graph Confirm the staff member performing an operation is authorized |
| catalog | CC_CLAIM_BOOK_IDENTITY_V0 | CC | Claim a book's identity so a second registration of the same book is refused | S4 capability_graph Enforce that one book exists per title, author and publication year |
| catalog | CC_CLAIM_COPY_BARCODE_V0 | CC | Claim a copy's barcode so a second copy carrying it is refused | S4 capability_graph Enforce that one physical copy exists per barcode |
| catalog | CC_REGISTER_BOOK_V0 | CC | Record a book's bibliographic information as the catalog's authoritative description of it | S4 capability_graph Register a book together with its first physical copy |
| catalog | CC_REGISTER_PHYSICAL_COPY_V0 | CC | Record a copy against exactly one book | S4 capability_graph Register a further physical copy against a registered book |
| catalog | CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | CC | Replace a book's descriptive content, refusing a change that duplicates another book | S4 capability_graph Update a book's bibliographic information |
| catalog | CC_RETIRE_BOOK_RECORD_V0 | CC | Mark a book record retired so it is no longer offered as current | S4 capability_graph Retire a book record |
| catalog | CC_RETIRE_PHYSICAL_COPY_V0 | CC | Mark a copy retired so the library no longer holds it | S4 capability_graph Retire a physical copy |
| catalog | CC_REINSTATE_BOOK_RECORD_V0 | CC | Mark a retired book record registered again | S4 capability_graph Return a retired book record to the registered state |
| catalog | CC_REINSTATE_PHYSICAL_COPY_V0 | CC | Mark a retired copy registered again | S4 capability_graph Return a retired physical copy to the registered state |
| catalog | CC_SEARCH_CATALOG_V0 | CC | Select the registered books matching a subject or title, excluding retired ones | S4 capability_graph Search the catalog by subject or title, excluding retired books |
| catalog | CC_ASSEMBLE_BOOK_DETAILS_V0 | CC | Assemble a book's record with the copies recorded against it | S4 capability_graph Retrieve a book's complete details with the copies the library holds |
| catalog | CC_APPEND_CATALOG_OPERATION_V0 | CC | Append a durable account of a performed operation to the catalog's own audit trail | S4 capability_graph Record a performed catalog operation in the catalog's audit trail |
| catalog | CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | CT | Forms the single key claimed for a book from its title, author and publication year | S4 gap_register GAP-06 |
| catalog | CC_VALIDATE_BOOK_SUBMISSION_V0 | CC | Confirms a registration carries what a book record requires, before any identity is claimed | S4 gap_register GAP-06 |
| catalog | CC_RESOLVE_BOOK_IDENTITY_V0 | CC | Resolves a registered book by its identifying key, so an update names the book independently of the attributes it changes | S4 gap_register GAP-08 |
| catalog | EV_BOOK_REGISTERED_V0 | EV | The moment a book enters the catalog | S4 gap_register GAP-16 |
| catalog | EV_PHYSICAL_COPY_REGISTERED_V0 | EV | The moment the library records another copy it owns | S4 gap_register GAP-16 |
| catalog | EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0 | EV | The moment a book's authoritative description changes | S4 gap_register GAP-16 |
| catalog | EV_BOOK_RETIRED_V0 | EV | The moment a book record is judged obsolete | S4 gap_register GAP-16 |
| catalog | EV_PHYSICAL_COPY_RETIRED_V0 | EV | The moment the library no longer holds a copy | S4 gap_register GAP-16 |
| catalog | RB_CATALOG_BINDINGS_V0 | RB | Binds the catalog's operations to the stores and mechanisms they use | S4 gap_register GAP-03 |
| catalog | STRUCTURE_CATALOG_STORAGE_V0 | STRUCTURE | Declares the stores the catalog owns and the paths they occupy | S4 gap_register GAP-02 |
---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|

No capability contract from another subdomain is referenced. The catalog reuses declared mechanisms —
durable records, uniqueness, an append-only trail and four pure transforms — and composes them itself,
so that no catalog operation depends on another subdomain's semantics or writes into its stores.

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
