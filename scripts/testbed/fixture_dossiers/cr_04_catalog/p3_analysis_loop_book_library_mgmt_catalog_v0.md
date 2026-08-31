# Stage 3 — Analysis Loop: book_library_mgmt / catalog
**Stage:** 3 — Analysis Loop
**CR:** cr_04_catalog
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

The question Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | **OVERTURNED. Registering a work does not belong in this change.** This pass first ruled that it did, on the ground that requiring the subject makes no request harder because every request already supplies it. Executing the change against the library's own exercise of the catalog falsified that ground: the caller supplies the subject nested inside the details of the book, and the act reads it at the top level of the request and rebuilds those details itself. No caller has ever sent it where the act reads it. Requiring it therefore makes every present request fail, which is precisely what the seed's ruling against gaining requirements forbids. | Returns the change to the two defects it was raised for. The third is real and is raised separately, where the boundary and the caller move together. | OBSERVED | HIGH | CLOSED | `WF_REGISTER_BOOK_V0` binds `book_fields` from `$.payload.subject`, `$.payload.title` and `$.payload.author`, ignoring the details the caller supplies. The library's exercise sends the subject only inside those supplied details. Emitting the requirement turned that exercise from failing at the second edition to failing at the first registration. |
| Q1a | **The third defect stands, and its correction is not this change's to make.** A boundary that admits a request its act cannot carry out is a defect by the same invariant as the other two, read in the other direction. Correcting it moves a requirement and a caller together, and the seed rules that no operation gains a requirement in this change. | Defers the third defect intact rather than dropping it. It is raised where the caller may move with it. | OBSERVED | HIGH | CLOSED | Requiring the subject is one requirement added; every present caller sends it elsewhere. Both facts are established, and they cannot both be honoured inside a change whose seed forbids the first. |
| Q2 | **One invariant covers all three defects, read in both directions.** Stage 1 stated that an operation requires only what it uses. Its converse — that an operation uses only what it requires — is the same statement of the same relation, and the third defect breaks it. Stating the invariant one-sidedly is what allowed the third defect to survive discovery of the first two. | Fixes what the change asserts: agreement between the two statements, not the removal of surplus requirements. | INFERRED | HIGH | CLOSED | Of the subdomain's ten operations, seven agree exactly, one requires more than it uses, one uses more than it requires, and one requires a detail in the wrong form. |
| Q3 | **The form of a detail is settled by no artifact, so the change must settle it by agreement.** The store declares six paths and no forms. A publication year's form is stated at three boundaries and in a description supplied with each request. Three of those four say number; one says word. There is no authority to defer to, only a majority and the data. | Fixes how the first defect is corrected: the boundary is brought to the form the other three statements share, rather than to a form the catalog declares. | OBSERVED | HIGH | CLOSED | `book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0` declares stores and paths only. `IN_REGISTER_BOOK_V0` and `IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0` say number; `IN_REGISTER_ADDITIONAL_EDITION_V0` says word; every year in the library's exercise of the catalog is a number. |
| Q4 | **Nothing else in the subdomain changes.** Each of the three boundaries is reached by exactly one artifact — the workflow it admits — and by nothing else. No boundary is shared, no boundary is referenced by another domain, and correcting one reaches nothing beyond its own operation. | Establishes that the change is three declarations and no cascade. | OBSERVED | HIGH | CLOSED | Each of the three reports a consumer count of one: its own workflow. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| Registering a further edition asks for the publication year as text while the neighbouring operation asks for a number. | S2 belief_verification #1 | CONFIRMED | Re-read from the composition: one boundary says word, two say number, and the description supplied with each request says number. |
| Correcting bibliographic information asks for three details it does not use. | S2 belief_verification #2 | CONFIRMED | Eight required; five read across four steps. The title, the author and the publication year are read by no step. |
| No other catalog operation asks for something it does not use. | S2 belief_verification #3 | CONFIRMED | Confirmed in the direction stated, and the opposite defect confirmed in registering a work. Both were re-derived from the compiled bindings rather than carried from Stage 2. What was overturned is not the defect but the claim that correcting it reached no caller. |
| Who may perform each operation is stated separately from what the operation needs. | S2 belief_verification #4 | CONFIRMED | The same three things appear in all ten operations of the subdomain and are read by no step of any of them. |
| The details a correction changes are supplied together, as the changed fields. | S2 belief_verification #5 | CONFIRMED | The correction's four steps read the record named and the changed details, and nothing else the request supplied. |
| Both failures break the library's own end-to-end exercise of the catalog. | S2 belief_verification #6 | CONFIRMED | Re-run against the pinned composition: the exercise stops at the second edition, which is absent from the catalog when the exercise looks for it. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The three boundaries being corrected | governance | EXISTING | All three are declared artifacts of this subdomain, each reached by one workflow. |
| The three operations themselves | capability | EXISTING | All three already run and already read what they read. No step changes. |
| The decision about who may perform an operation | governance | EXISTING | Declared uniformly across all ten operations and untouched by this change. |
| The catalog's stores | data | EXISTING | Six stores, unchanged. No held record is migrated, rewritten or revalidated. |
| The comparison of what an operation requires against what it uses | governance | INVESTIGATE | Nothing performs it in the composition. Whether it belongs to this subdomain or to the platform is not this change's to settle. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| book_library_mgmt::IN_REGISTER_ADDITIONAL_EDITION_V0 | The form of one requirement. Nothing else in the subdomain reads it. | 1 | Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0`. |
| book_library_mgmt::IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0 | Three requirements withdrawn. Nothing else in the subdomain reads it. | 1 | Reported by the composition: its only consumer is `book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0`. |
| book_library_mgmt::IN_REGISTER_BOOK_V0 | One requirement added, which the operation already reads. | 1 | Reported by the composition: its only consumer is `book_library_mgmt::WF_REGISTER_BOOK_V0`. |
| The three workflows | None. No step is added, removed or rebound. | — | Each reads exactly what it reads today; the change is to what the boundary above it states. |
| The catalog's six stores | None. | — | No held record changes; the change is to what a new request must supply. |
| The library's end-to-end exercise of the catalog | It completes, where today it stops at the second edition. | — | The exercise is the acceptance evidence, not a consumer of any artifact. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|-----------|----------|-----------|---------------------|----------------|
| Admitting a request to register a further edition | EXTEND | The boundary is right about what it needs and wrong about the form one of them takes. Only the form changes. | Changing the operation to accept a word was considered and rejected: three of the four statements of the form say number, and the data is numbers. | analysis_findings #3 |
| Admitting a request to correct bibliographic information | EXTEND | Three requirements are withdrawn. The other five describe what the operation does. | Making the operation read the three was considered and rejected: a correction that restates the fields it leaves alone is not a correction. | analysis_findings #2 |
| Admitting a request to register a work | REUSE | Unchanged by this change. The requirement it lacks is one every present caller sends elsewhere, so adding it here would break every request the library makes. | Adding the requirement was ruled and then overturned against the library's own exercise of the catalog; amending the callers alongside it was rejected as outside a change whose seed forbids gaining a requirement. | analysis_findings #1 |
| The three operations | REUSE | No step is added, removed or rebound. What each operation does is correct. | Rewriting the operations was considered and rejected: it is the boundaries that are wrong. | analysis_findings #4 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | catalog | All three boundaries are declared by this subdomain, reached only by its own workflows, and reach nothing outside it. | analysis_findings #4 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| The question Stage 2 left open is closed. | SATISFIED | Registering a work does not join the change. The ground for admitting it was overturned by execution: the constraint it appeared to break does reach it, because no present caller supplies the detail where the act reads it. |
| Every belief Stage 2 verified was re-grounded. | SATISFIED | All six confirmed against the pinned composition and against the library's own exercise of the catalog; none overturned. |
| Every operation of the subdomain has been examined. | SATISFIED | All ten compared requirement by requirement against the steps that carry them. Three disagree; seven agree exactly. Two are corrected here and the third is deferred with its ground recorded. |
| The correction for each defect is determined. | SATISFIED | One form brought to the form the other three statements share, and three requirements withdrawn. The third defect is stated, deferred and unchanged. |
| Nothing outside the subdomain is reached. | SATISFIED | Each boundary has exactly one consumer, its own workflow. No store, no other subdomain and no other domain is touched. |
