# Stage 3 — Analysis Loop: book_library_mgmt / catalog

## Machine

```yaml
header:
  Stage: 3 — Analysis Loop
  CR: cr_04_catalog
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
      Finding: '**OVERTURNED. Registering a work does not belong in this change.** This pass first ruled that it did, on the ground that requiring the subject makes no request harder because every request already supplies it. Executing the change against the library''s own exercise of the catalog falsified that ground: the caller supplies the subject nested inside the details of the book, and the act reads it at the top level of the request and rebuilds those details itself. No caller has ever sent it where the act reads it. Requiring it therefore makes every present request fail, which is precisely what the seed''s ruling against gaining requirements forbids.'
      Impact: Returns the change to the two defects it was raised for. The third is real and is raised separately, where the boundary and the caller move together.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: '`WF_REGISTER_BOOK_V0` binds `book_fields` from `$.payload.subject`, `$.payload.title` and `$.payload.author`, ignoring the details the caller supplies. The library''s exercise sends the subject only inside those supplied details. Emitting the requirement turned that exercise from failing at the second edition to failing at the first registration.'
    - Question Id: Q1a
      Finding: '**The third defect stands, and its correction is not this change''s to make.** A boundary that admits a request its act cannot carry out is a defect by the same invariant as the other two, read in the other direction. Correcting it moves a requirement and a caller together, and the seed rules that no operation gains a requirement in this change.'
      Impact: Defers the third defect intact rather than dropping it. It is raised where the caller may move with it.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: Requiring the subject is one requirement added; every present caller sends it elsewhere. Both facts are established, and they cannot both be honoured inside a change whose seed forbids the first.
    - Question Id: Q2
      Finding: '**One invariant covers all three defects, read in both directions.** Stage 1 stated that an operation requires only what it uses. Its converse — that an operation uses only what it requires — is the same statement of the same relation, and the third defect breaks it. Stating the invariant one-sidedly is what allowed the third defect to survive discovery of the first two.'
      Impact: 'Fixes what the change asserts: agreement between the two statements, not the removal of surplus requirements.'
      Evidence Status (OBSERVED, INFERRED, OPEN): INFERRED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: Of the subdomain's ten operations, seven agree exactly, one requires more than it uses, one uses more than it requires, and one requires a detail in the wrong form.
    - Question Id: Q3
      Finding: '**The form of a detail is settled by no artifact, so the change must settle it by agreement.** The store declares six paths and no forms. A publication year''s form is stated at three boundaries and in a description supplied with each request. Three of those four say number; one says word. There is no authority to defer to, only a majority and the data.'
      Impact: 'Fixes how the first defect is corrected: the boundary is brought to the form the other three statements share, rather than to a form the catalog declares.'
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: '`book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0` declares stores and paths only. `IN_REGISTER_BOOK_V0` and `IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` say number; `IN_REGISTER_ADDITIONAL_EDITION_V0` says word; every year in the library''s exercise of the catalog is a number.'
    - Question Id: Q4
      Finding: '**Nothing else in the subdomain changes.** Each of the three boundaries is reached by exactly one artifact — the workflow it admits — and by nothing else. No boundary is shared, no boundary is referenced by another domain, and correcting one reaches nothing beyond its own operation.'
      Impact: Establishes that the change is three declarations and no cascade.
      Evidence Status (OBSERVED, INFERRED, OPEN): OBSERVED
      Confidence (HIGH, MEDIUM, LOW): HIGH
      Resolution Status (CLOSED, OPEN): CLOSED
      Evidence: 'Each of the three reports a consumer count of one: its own workflow.'
  verification_results:
    columns:
    - Item
    - Origin
    - Result (CONFIRMED, OVERTURNED)
    - Evidence
    rows:
    - Item: Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number.
      Origin: 'S2 belief_verification #1'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-read from the composition: one boundary says word, two say number, and the description supplied with each request says number.'
    - Item: Correcting bibliographic information asks for three details it does not use.
      Origin: 'S2 belief_verification #2'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Eight required; five read across four steps. The title, the author and the publication year are read by no step.
    - Item: No other catalog operation asks for something it does not use.
      Origin: 'S2 belief_verification #3'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: Confirmed in the direction stated, and the opposite defect confirmed in registering a work. Both were re-derived from the compiled bindings rather than carried from Stage 2. What was overturned is not the defect but the claim that correcting it reached no caller.
    - Item: Who may perform each operation is stated separately from what the operation needs.
      Origin: 'S2 belief_verification #4'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: The same three things appear in all ten operations of the subdomain and are read by no step of any of them.
    - Item: The details a correction changes are supplied together, as the changed fields.
      Origin: 'S2 belief_verification #5'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: The correction's four steps read the record named and the changed details, and nothing else the request supplied.
    - Item: Both failures break the library's own end-to-end exercise of the catalog.
      Origin: 'S2 belief_verification #6'
      Result (CONFIRMED, OVERTURNED): CONFIRMED
      Evidence: 'Re-run against the pinned composition: the exercise stops at the second edition, which is absent from the catalog when the exercise looks for it.'
  dependency_discoveries:
    columns:
    - Dependency
    - Type
    - Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE)
    - Evidence
    rows:
    - Dependency: The three boundaries being corrected
      Type: governance
      Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: All three are declared artifacts of this subdomain, each reached by one workflow.
    - Dependency: The three operations themselves
      Type: capability
      Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: All three already run and already read what they read. No step changes.
    - Dependency: The decision about who may perform an operation
      Type: governance
      Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: Declared uniformly across all ten operations and untouched by this change.
    - Dependency: The catalog's stores
      Type: data
      Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE): EXISTING
      Evidence: Six stores, unchanged. No held record is migrated, rewritten or revalidated.
    - Dependency: The comparison of what an operation requires against what it uses
      Type: governance
      Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE): INVESTIGATE
      Evidence: Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle.
  impact_analysis:
    columns:
    - Artifact
    - Impact Scope
    - Consumer Count
    - Evidence
    rows:
    - Artifact: book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0
      Impact Scope: The form of one requirement. Nothing else in the subdomain reads it.
      Consumer Count: '1'
      Evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0`.'
    - Artifact: book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      Impact Scope: Three requirements withdrawn. Nothing else in the subdomain reads it.
      Consumer Count: '1'
      Evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`.'
    - Artifact: book_library_mgmt::IN_REGISTER_BOOK_V0
      Impact Scope: One requirement added, which the operation already reads.
      Consumer Count: '1'
      Evidence: 'Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_BOOK_V0`.'
    - Artifact: The three workflows
      Impact Scope: None. No step is added, removed or rebound.
      Consumer Count: —
      Evidence: Each reads exactly what it reads today; the change is to what the boundary above it states.
    - Artifact: The catalog's six stores
      Impact Scope: None.
      Consumer Count: —
      Evidence: No held record changes; the change is to what a new request must supply.
    - Artifact: The library's end-to-end exercise of the catalog
      Impact Scope: It completes, where today it stops at the second edition.
      Consumer Count: —
      Evidence: The exercise is the acceptance evidence, not a consumer of any artifact.
  authoring_decisions:
    columns:
    - Capability
    - Decision (REUSE, EXTEND, AUTHOR_NEW)
    - Rationale
    - Alternatives Checked
    - Source Finding
    rows:
    - Capability: Admitting a request to register a further edition
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: The boundary is right about what it needs and wrong about the form one of them takes. Only the form changes.
      Alternatives Checked: 'Changing the operation to accept a word was considered and rejected: three of the four statements of the form say number, and the data is numbers.'
      Source Finding: 'analysis_findings #3'
    - Capability: Admitting a request to correct bibliographic information
      Decision (REUSE, EXTEND, AUTHOR_NEW): EXTEND
      Rationale: Three requirements are withdrawn. The other five describe what the operation does.
      Alternatives Checked: 'Making the operation read the three was considered and rejected: a correction that restates the fields it leaves alone is not a correction.'
      Source Finding: 'analysis_findings #2'
    - Capability: Admitting a request to register a work
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: Unchanged by this change. The requirement it lacks is one every present caller sends elsewhere, so adding it here would break every request the library makes.
      Alternatives Checked: Adding the requirement was ruled and then overturned against the library's own exercise of the catalog; amending the callers alongside it was rejected as outside a change whose seed forbids gaining a requirement.
      Source Finding: 'analysis_findings #1'
    - Capability: The three operations
      Decision (REUSE, EXTEND, AUTHOR_NEW): REUSE
      Rationale: No step is added, removed or rebound. What each operation does is correct.
      Alternatives Checked: 'Rewriting the operations was considered and rejected: it is the boundaries that are wrong.'
      Source Finding: 'analysis_findings #4'
  placement_decision:
    columns:
    - Decision (NEW_SUBDOMAIN, EXTEND)
    - Subdomain
    - Rationale
    - Source Finding
    rows:
    - Decision (NEW_SUBDOMAIN, EXTEND): EXTEND
      Subdomain: catalog
      Rationale: All three boundaries are declared by this subdomain, reached only by its own workflows, and reach nothing outside it.
      Source Finding: 'analysis_findings #4'
  saturation:
    columns:
    - Criterion
    - Status (SATISFIED, NOT_SATISFIED)
    - Evidence
    rows:
    - Criterion: The question Stage 2 left open is closed.
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: 'Registering a work does not join the change. The ground for admitting it was overturned by execution: the constraint it appeared to break does reach it, because no present caller supplies the detail where the act reads it.'
    - Criterion: Every belief Stage 2 verified was re-grounded.
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: All six confirmed against the pinned composition and against the library's own exercise of the catalog; none overturned.
    - Criterion: Every operation of the subdomain has been examined.
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: All ten compared requirement by requirement against the steps that carry them. Three disagree; seven agree exactly. Two are corrected here and the third is deferred with its ground recorded.
    - Criterion: The correction for each defect is determined.
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: One form brought to the form the other three statements share, and three requirements withdrawn. The third defect is stated, deferred and unchanged.
    - Criterion: Nothing outside the subdomain is reached.
      Status (SATISFIED, NOT_SATISFIED): SATISFIED
      Evidence: Each boundary has exactly one consumer, its own workflow. No store, no other subdomain and no other domain is touched.
```

The question Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

---

## 5. Authoring Decisions

---

## 6. Placement Decision

---

## 7. Discovery Saturation
