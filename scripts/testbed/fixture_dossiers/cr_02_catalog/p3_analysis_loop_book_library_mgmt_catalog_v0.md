# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 3 — Analysis Loop
  CR: cr_02_catalog
  Status: DRAFT
  Feeds: Stage 4 — Business Model
registers:
  analysis_findings:
    columns:
    - Question Id
    - Finding
    - Impact
    - Evidence Status (OBSERVED, INFERRED, OPEN)
    - Confidence (HIGH, MEDIUM, LOW)
    - Resolution Status (CLOSED, OPEN)
    - Evidence
    rows:
    - Question Id: Q1
      Finding: The existing record is identified by title, author and publication year, and two records differing only in publication year are already two records. The catalog therefore already distinguishes editions, and no identity has to change.
      Impact: The change adds the work above the existing record instead of redefining it; no existing identity, record or operation is redefined.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key from title, author and publication_year; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 claims it
    - Question Id: Q2
      Finding: Uniqueness in this composition is claimed through a registry keyed on one value, and a key is formed by a pure transform before it is claimed. A work's key of title and author can be formed and claimed the same way.
      Impact: The work's identity needs no new mechanism, only a new key and a new claim step.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE and EXISTS; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 is the worked precedent
    - Question Id: Q3
      Finding: The transform that forms the edition key is depended on by 23 artifacts and forms a three-attribute key. Making it also form a two-attribute key would change a transform every catalog operation reaches.
      Impact: The work key is formed by a new transform rather than by widening the existing one.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: si.topology.impact impacted_count 23 for book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    - Question Id: Q4
      Finding: Selecting records by stated criteria exists as a pure transform; grouping the selected records by an attribute they share does not.
      Impact: Work-level search needs a grouping transform that the composition does not carry.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects and returns records; no transform in the composition groups them
    - Question Id: Q5
      Finding: The search and retrieval steps are each reached by one workflow and one entry point, and their own consumer closure is the subdomain rather than the composition.
      Impact: Changing what they return disturbs nothing outside the catalog.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: si.topology.impact impacted_namespaces book_library_mgmt only for book_library_mgmt::CC_SEARCH_CATALOG_V0 and book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
    - Question Id: Q6
      Finding: A physical copy is recorded against one record and claims its own barcode, so a copy already belongs to exactly one edition.
      Impact: Copies are untouched by this change — no decision, no extension, no new artifact.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0
    - Question Id: Q7
      Finding: The subdomain declares its own stores and binds its own workflows to them, and the binding declaration is referenced by nine artifacts within the subdomain and none outside it.
      Impact: A store for works is declared and bound in the subdomain's own declarations, and the blast radius stays inside the catalog.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: si.artifact.refs ref_count 9 for book_library_mgmt::RB_CATALOG_BINDINGS_V0, all within book_library_mgmt
    - Question Id: Q8
      Finding: book_library_mgmt declares its reuse visibility as business, so the previous change's own artifacts are legitimate candidates for this one.
      Impact: Reuse and extension of the catalog's artifacts are permitted rather than assumed.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: si.snapshot.summary reuse_visibility book_library_mgmt business
    - Question Id: Q9
      Finding: Whether any record was written under the previous change cannot be established from the composition; a snapshot declares stores and paths and does not carry their contents.
      Impact: The existing-records promise is carried forward as a criterion execution must settle, not as a design question.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares five paths and no contents; no inspection operation reads a store
    - Question Id: Q10
      Finding: Registration already claims two identities and writes two records, in an order established so that every claim precedes every write.
      Impact: A work claim is placed among the claims, before any write, rather than appended to the operation.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: book_library_mgmt::CC_REGISTER_BOOK_V0 and book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
  verification_results:
    columns:
    - Item
    - Origin
    - Result (CONFIRMED, OVERTURNED)
    - Evidence
    rows:
    - Item: The book_library_mgmt catalog is believed to be part of the current composition, established by a previous governed change.
      Origin: 'S2 belief_verification #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read against the pinned composition: book_library_mgmt carries 43 artifacts and declares compiler version 4, alongside five other domains'
    - Item: The catalog is believed to hold bibliographic records and physical copies of library materials.
      Origin: 'S2 belief_verification #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0: five stores, of which BOOKS and PHYSICAL_COPIES hold the records, one append-only trail and two registries'
    - Item: A book is believed to be identified by title, author and publication year.
      Origin: 'S2 belief_verification #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: inputs title, author, publication_year; output one identity_key claimed by book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0'
    - Item: A physical copy is believed to belong to exactly one book.
      Origin: 'S2 belief_verification #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Re-read book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0; no path records a copy against more than one record
    - Item: The catalog is believed to provide registering books, registering physical copies, updating bibliographic information, retiring records, searching the catalog and retrieving complete book details.
      Origin: 'S2 belief_verification #5'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-counted against the composition: nine workflows and nine entry points in book_library_mgmt, each reaching book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 first'
    - Item: A retired record is believed to be reinstatable.
      Origin: 'S2 belief_verification #6'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Re-read book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_PHYSICAL_COPY_V0, reached through their own entry points
    - Item: Records written under the previous change are believed to exist and to be readable.
      Origin: 'S2 belief_verification #7'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'The result stands and is re-grounded: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares paths and no contents, and no inspection operation in the composition reads a store. The belief remains unresolvable from a snapshot, which is a fact about where it can be settled, not a defect in the belief'
    - Item: Durable records are written, read, selected and updated in place through a declared side effect.
      Origin: S2 pps_baseline_fqdns — durable record store
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Re-read capability_side_effects::CS_MUTABLE_JSON_V0; impacted_count 46 across ai_governance, book_library_mgmt and workload
    - Item: Uniqueness is claimed through a registry keyed on a single value.
      Origin: S2 pps_baseline_fqdns — uniqueness registry
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Re-read capability_side_effects::CS_REGISTRY_V0; impacted_count 43 across ai_governance and book_library_mgmt
    - Item: Selecting records by stated criteria exists as a pure transform, and grouping them does not.
      Origin: 'S2 architectural_observations #5'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Re-read capability_transforms::CT_PURE_FILTER_RECORDS_V0; impacted_count 33, and the composition carries no grouping transform
  dependency_discoveries:
    columns:
    - Dependency
    - Type
    - Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE)
    - Evidence
    rows:
    - Dependency: Durable record storage for works
      Type: side effect
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: capability_side_effects::CS_MUTABLE_JSON_V0
    - Dependency: Uniqueness claim for a work's identity
      Type: side effect
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: capability_side_effects::CS_REGISTRY_V0
    - Dependency: The work identity key, formed from title and author
      Type: transform
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: No transform in the composition forms a two-attribute key; book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms the three-attribute edition key
    - Dependency: Grouping selected records by an attribute they share
      Type: transform
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): AUTHOR_NEW
      Evidence: capability_transforms::CT_PURE_FILTER_RECORDS_V0 selects and does not group
    - Dependency: The store declaration that must carry the work stores
      Type: structure
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0, impacted_count 10
    - Dependency: The binding declaration that must bind the work stores
      Type: runtime binding
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::RB_CATALOG_BINDINGS_V0, ref_count 9
    - Dependency: The registration step that must claim the work
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::CC_REGISTER_BOOK_V0, impacted_count 22
    - Dependency: The search step whose answer must be grouped by work
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::CC_SEARCH_CATALOG_V0, impacted_count 31
    - Dependency: The retrieval step that must carry a work summary
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0, impacted_count 31
    - Dependency: The authorization check every catalog operation reaches first
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    - Dependency: The audit step every catalog operation reaches last
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    - Dependency: Copy registration and barcode uniqueness
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0, unchanged by this change
    - Dependency: Retirement and reinstatement of an edition
      Type: contract
      Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE): REUSE
      Evidence: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
  impact_analysis:
    columns:
    - Artifact
    - Impact Scope
    - Consumer Count
    - Evidence
    rows:
    - Artifact: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '10'
      Evidence: si.topology.impact impacted_count 10, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
    - Artifact: book_library_mgmt::RB_CATALOG_BINDINGS_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '9'
      Evidence: si.topology.impact impacted_count 9, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 9
    - Artifact: book_library_mgmt::CC_REGISTER_BOOK_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '22'
      Evidence: si.topology.impact impacted_count 22, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
    - Artifact: book_library_mgmt::CC_SEARCH_CATALOG_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '31'
      Evidence: si.topology.impact impacted_count 31, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
    - Artifact: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '31'
      Evidence: si.topology.impact impacted_count 31, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
    - Artifact: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '22'
      Evidence: si.topology.impact impacted_count 22, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
    - Artifact: book_library_mgmt::IN_SEARCH_CATALOG_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
    - Artifact: book_library_mgmt::IN_RETRIEVE_BOOK_DETAILS_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '1'
      Evidence: si.topology.impact impacted_count 1, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 1
    - Artifact: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '23'
      Evidence: si.topology.impact impacted_count 23, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — examined and not widened
    - Artifact: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '20'
      Evidence: si.topology.impact impacted_count 20, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — read as precedent, not changed
    - Artifact: capability_side_effects::CS_MUTABLE_JSON_V0
      Impact Scope: ai_governance, book_library_mgmt, workload
      Consumer Count: '46'
      Evidence: si.topology.impact impacted_count 46, impacted_namespaces ai_governance, book_library_mgmt and workload; si.artifact.refs ref_count 14 — reused as-is
    - Artifact: capability_side_effects::CS_REGISTRY_V0
      Impact Scope: ai_governance, book_library_mgmt
      Consumer Count: '43'
      Evidence: si.topology.impact impacted_count 43, impacted_namespaces ai_governance and book_library_mgmt; si.artifact.refs ref_count 10 — reused as-is
    - Artifact: capability_transforms::CT_PURE_FILTER_RECORDS_V0
      Impact Scope: book_library_mgmt
      Consumer Count: '33'
      Evidence: si.topology.impact impacted_count 33, impacted_namespaces book_library_mgmt; si.artifact.refs ref_count 2 — examined and not extended
    - Artifact: book_library_mgmt::WF_SEARCH_CATALOG_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
    - Artifact: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
    - Artifact: book_library_mgmt::WF_REGISTER_BOOK_V0
      Impact Scope: none
      Consumer Count: '0'
      Evidence: si.topology.impact impacted_count 0, impacted_namespaces empty; si.artifact.refs ref_count 0
  authoring_decisions:
    columns:
    - Capability
    - Decision (REUSE, EXTEND, AUTHOR_NEW)
    - Rationale
    - Alternatives Checked
    - Source Finding
    rows:
    - Capability: Hold a work record durably and update it in place
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: A work record is written, read and updated in place exactly as an edition record is, and the declared mechanism is read rather than modified.
      Alternatives Checked: capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is; capability_side_effects::CS_APPENDONLY_JSONL_V0 was examined and rejected because a work record must be updated, not only appended.
      Source Finding: 'S3 analysis_findings #2'
    - Capability: Enforce that one work exists per title and author
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Register-if-absent gives the atomic uniqueness a work identity needs, and the key formed from two attributes is a catalog business rule rather than a change to the mechanism.
      Alternatives Checked: capability_side_effects::CS_REGISTRY_V0 reused with a two-attribute key, exactly as the edition key uses it with three; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 was examined as the worked precedent and claims a different key against a different store.
      Source Finding: 'S3 analysis_findings #2'
    - Capability: Form the identifying key of a work from its title and author
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: The work's key is a different business key from the edition's, and the transform that forms the edition key is reached by every catalog operation. Widening it would change the identity of the existing record to serve a new one.
      Alternatives Checked: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 was examined and rejected — it forms a three-attribute key and 23 artifacts depend on it; capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 was examined and rejected because assembling a record applies no identity rule.
      Source Finding: 'S3 analysis_findings #3'
    - Capability: Claim a work's identity so that two registrations of one work do not produce two works
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Nothing in the composition claims a work. The claim is a governed step of its own, composed the way the edition claim is composed, against the work's own registry store.
      Alternatives Checked: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 was examined and rejected — it claims the edition key against the edition registry; capability_side_effects::CS_REGISTRY_V0 is reused beneath the new step rather than replaced.
      Source Finding: 'S3 analysis_findings #2'
    - Capability: Resolve the work an edition belongs to
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Registering an additional edition must name an existing work and receive its record; no step in the composition answers which work a title and author denote.
      Alternatives Checked: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 was examined and rejected — it resolves an edition by its own three-attribute key and cannot answer for a work.
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Group selected records by an attribute they share
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: Work-level search returns one result per work, which requires grouping the matching editions. Selection and grouping are different operations on the same records.
      Alternatives Checked: capability_transforms::CT_PURE_FILTER_RECORDS_V0 was examined and rejected — it selects records by criteria and returns them ungrouped; capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 was examined and rejected because it assembles one record rather than relating several.
      Source Finding: 'S3 analysis_findings #4'
    - Capability: Declare the stores the catalog owns
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The catalog owns its stores and must now own two more — one holding work records and one claiming work identities. The declaration is the subdomain's own and its consumers are all within it.
      Alternatives Checked: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 extended with the work stores; authoring a second storage declaration for the same subdomain was examined and rejected because a subdomain declares its stores once.
      Source Finding: 'S3 analysis_findings #7'
    - Capability: Bind the catalog's workflows to the stores they use
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The new stores must be reachable by the workflows that read and write them, and binding is declared once per subdomain.
      Alternatives Checked: book_library_mgmt::RB_CATALOG_BINDINGS_V0 extended with the work stores; a second binding declaration was examined and rejected for the same reason as the storage declaration.
      Source Finding: 'S3 analysis_findings #7'
    - Capability: Register an edition of a work the catalog does not yet hold
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The existing registration already confirms authorization, validates, claims two identities, writes two records and audits. It gains a work claim among the claims, before any write, and changes in no other way.
      Alternatives Checked: book_library_mgmt::CC_REGISTER_BOOK_V0 extended; authoring a separate registration was examined and rejected because two registrations for one act would duplicate every refusal the existing one enforces.
      Source Finding: 'S3 analysis_findings #10'
    - Capability: Validate that a registration carries what a work and an edition require
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: Validation already runs before any claim and knows the edition's attributes; it must also confirm what a work requires.
      Alternatives Checked: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0 extended; capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 was examined and is reused beneath it rather than replacing it.
      Source Finding: 'S3 analysis_findings #10'
    - Capability: Register an additional edition of an existing work
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: This is the operation the change exists to add. It resolves an existing work rather than creating one, and claims only the edition, so it is a different business operation from registering a work.
      Alternatives Checked: book_library_mgmt::CC_REGISTER_BOOK_V0 was examined and rejected — it creates the work and requires a first copy, neither of which an additional edition does; book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 was examined and rejected because a further edition is not a further copy.
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Search the catalog and answer at the level of the work
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: 'The existing search already selects registered records by subject or title and excludes retired ones. What changes is the shape of the answer: the matching editions are grouped under their work. Its consumers are one workflow and one entry point, both within the subdomain.'
      Alternatives Checked: book_library_mgmt::CC_SEARCH_CATALOG_V0 extended; authoring a second search was examined and rejected because two searches would leave staff choosing which one answers their question.
      Source Finding: 'S3 analysis_findings #5'
    - Capability: Retrieve an edition's complete details with a summary of its work
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: Retrieval already assembles an edition and the physical copies of it; it gains the work summary so the work's title need not be looked up separately.
      Alternatives Checked: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 extended; authoring a separate work retrieval was examined and rejected because the business asked for one retrieval carrying a summary, not a second operation.
      Source Finding: 'S3 analysis_findings #5'
    - Capability: Admit a request to register an additional edition of an existing work
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: A new business operation is reached through its own entry point, which declares what a caller must supply — the work it belongs to and the edition's own attributes.
      Alternatives Checked: book_library_mgmt::IN_REGISTER_BOOK_V0 was examined and rejected — it admits a registration that creates a work and requires a first copy.
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Recognise the moment a work enters the catalog
      Decision (REUSE, EXTEND, AUTHOR_NEW): AUTHOR_NEW
      Rationale: The catalog declares a business moment for each thing that enters it, and a work entering is a moment nothing currently declares.
      Alternatives Checked: book_library_mgmt::EV_BOOK_REGISTERED_V0 was examined and rejected — it names an edition entering the catalog, which continues to be its own moment.
      Source Finding: 'S3 analysis_findings #1'
    - Capability: Confirm the staff member performing an operation is authorized
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Every catalog operation reaches the same check first, and the operations this change adds do the same.
      Alternatives Checked: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #10'
    - Capability: Record every performed operation in the catalog's audit trail
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: The trail records whatever operation it is handed, including the ones this change adds.
      Alternatives Checked: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #10'
    - Capability: Register a physical copy against exactly one edition
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: A copy already belongs to exactly one record, and that record is an edition. Nothing about copies changes.
      Alternatives Checked: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0 and book_library_mgmt::CC_CLAIM_COPY_BARCODE_V0 satisfy it as-is.
      Source Finding: 'S3 analysis_findings #6'
    - Capability: Retire and reinstate an edition independently of the work's other editions
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Retirement is declared on the existing record and cascades to nothing, which is exactly what retiring one edition requires.
      Alternatives Checked: book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 satisfy it as-is.
      Source Finding: 'S3 analysis_findings #6'
    - Capability: Update an edition's bibliographic information
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: The update already refuses a change that would duplicate another record, and duplication remains an edition-level rule.
      Alternatives Checked: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 satisfies it as-is.
      Source Finding: 'S3 analysis_findings #6'
  placement_decision:
    columns:
    - Decision (NEW_SUBDOMAIN, EXTEND)
    - Subdomain
    - Rationale
    - Source Finding
    rows:
    - Decision (NEW_SUBDOMAIN, EXTEND): EXTEND
      Subdomain: catalog
      Rationale: The work is the abstraction above the record the catalog already holds, it is identified by attributes the catalog already stores, and every operation it touches is one the catalog already owns. Placing it in a subdomain of its own would split one authoritative description of the library's holdings across two owners.
      Source Finding: 'S3 analysis_findings #7'
  saturation:
    columns:
    - Criterion
    - Status (SATISFIED, NOT_SATISFIED)
    - Evidence
    rows:
    - Criterion: No unresolved CRITICAL gaps
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: 'The six CRITICAL gaps carried from Stage 2 each resolve to a committed decision: the work entity and its store to REUSE of capability_side_effects::CS_MUTABLE_JSON_V0, its identity to a new key transform and a new claim step, grouping to a new transform, and search, retrieval and registration to extensions of book_library_mgmt::CC_SEARCH_CATALOG_V0, book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 and book_library_mgmt::CC_REGISTER_BOOK_V0'
    - Criterion: No open analyst questions
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Stage 2 carried none, and all ten findings in this stage are CLOSED
    - Criterion: No dependency expansion in the last pass
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: The thirteen dependencies were established in one pass against book_library_mgmt::RB_CATALOG_BINDINGS_V0 and the substrate side effects; re-reading them surfaced no further dependency
    - Criterion: Verification pass complete, no OVERTURNED item unresolved
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: All ten items re-grounded and CONFIRMED, including the seventh belief whose unresolvability from a snapshot is itself confirmed against book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    - Criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Every finding in this stage is OBSERVED. The Stage 2 rows that were INFERRED concern the work, which no artifact yet expresses; each is carried forward as a committed AUTHOR_NEW decision rather than left as a suspicion
```

Every decision here is taken against a subdomain the pipeline itself authored, so the reuse question
is asked of the previous change's own output rather than of the substrate alone. Impact counts are
read from the composition, never estimated.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

Every impacted namespace is book_library_mgmt's own except for the two substrate side effects, which
are reused unchanged and gain a consumer rather than losing one.

---

## 5. Authoring Decisions

---

## 6. Subdomain Placement Decision

---

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · assumptions · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · constraints |
| **Consumes** ← Stage 2 | belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
