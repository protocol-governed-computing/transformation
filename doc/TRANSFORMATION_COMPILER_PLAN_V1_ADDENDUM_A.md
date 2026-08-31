# Plan V1 — Addendum A: the Release 4 Subject

The subject of the release-4 validation: the business problem, its decomposition, and the change
request sequence that drives it. This addendum fixes what `TRANSFORMATION_COMPILER_PLAN_V1.md`
leaves as "a small, real business domain."

---

## 1. The overall business problem

A community library system needs to manage its collection, patrons, circulation, reservations,
acquisitions, and policy enforcement across one or more branches. The system must maintain a
complete audit trail of every business action while enforcing library policies such as borrowing
limits, loan periods, fines, and membership status. It must be designed so that new capabilities
can be introduced incrementally without disrupting existing operations.

That last sentence is the point. The subject was chosen because incremental introduction is its
*business* requirement, not a testing convenience — so every CR in the sequence has a real
rationale, and none of them reads as an artificial exercise of a compiler branch.

## 2. Domain decomposition

Domain: **`book_library_mgmt`**. Its full subdomain space:

| Subdomain | Concern |
|---|---|
| `catalog` | bibliographic works and physical copies |
| `circulation` | loans, returns, due dates |
| `patron` | membership, standing, entitlement class |
| `reservations` | holds and queues |
| `acquisitions` | ordering and receipt |
| `inventory` | shelf state, reconciliation |
| `notifications` | overdue and hold notices |
| `policy` | borrowing limits, loan periods, fines |
| `reporting` | derived views |

Each is independently governable. **Release 4 builds two of them** — `catalog` and `circulation`.
The other seven are the deferred roadmap: they exist to make the deferral in each problem statement
concrete and to give later CRs somewhere to go. They are not release-4 scope and must not be
authored speculatively.

## 3. The change request sequence

Six CRs. Note this supersedes the five-CR sketch in the plan's §4: a second `NEW_SUBDOMAIN`
(CR-3) is added, and it is the most valuable case in the set.

| CR | Type | Subject | What it forces |
|---|---|---|---|
| CR-1 | `NEW_SUBDOMAIN` | `catalog` | placement and ownership against the release-3 composition; P3 **REUSE** of platform capabilities rather than authoring new ones |
| CR-2 | `EXTEND_SUBDOMAIN` | `catalog` | P3 must decide **EXTEND existing Book vs AUTHOR_NEW** — the first decision with a real baseline (CR-1's own output) |
| CR-3 | `NEW_SUBDOMAIN` | `circulation` | **cross-subdomain REUSE of business entities**, not just platform capabilities |
| CR-4 | `MODIFY` | circulation policy | behavioural change under the immutable-version rule (`_V0 → _V1`); existing workflows evolve |
| CR-5 | `DEPRECATE` | Book Category → Subject Classification | retirement with **real consumers to migrate** |
| CR-6 | *refused* | — | the gates bite: rejection recorded as evidence |

### CR-1 — `catalog`

Deliberately read-heavy and policy-light. Entities: Book, Author, Publisher, Category, Physical
Copy. Capabilities: Register Book, Register Physical Copy, Update Bibliographic Information, Search
Catalog, View Book Details, Retire Book Record. No lending, no patrons, no reservations, no fines.

Catalog goes first because it creates the reusable business entities every later CR draws on. A
first CR that solved the whole library would leave CR-2 through CR-5 with nothing legitimate to do.

### CR-2 — extend `catalog`

Multiple editions, ISBN aliases, subject taxonomy, digital resources, book images. This is the
first CR where P3 faces a genuine question rather than a foregone `AUTHOR_NEW`: is a second edition
an extension of Book or a new artifact?

### CR-3 — `circulation`

Reuses Book and Physical Copy from `catalog`; authors Loan, Return, Due Date. CR-1 exercised REUSE
against *platform* capabilities; CR-3 exercises it against *business entities in another
subdomain*, which is a different code path and the stronger claim. It also gives P6 (Governance
Intent) its first real cross-subdomain dependency and P7 a topological sort that spans subdomains.

### CR-4 — modify circulation policy

Single loan period (14 days) becomes entitlement-class-dependent: Faculty 28, Student 14, Guest 7.

**Open issue.** Entitlement class is a `patron` concept, and `patron` is not in release-4 scope.
Two admissible resolutions, to be settled before CR-4 is authored:

- **(a)** `circulation` carries a borrower entitlement class on the Loan as a local governed
  vocabulary, with `patron` later becoming its authority — a legitimate evolution, and arguably a
  better demonstration since it sets up a future `MODIFY` that moves ownership.
- **(b)** CR-4 modifies a policy that needs no patron facts at all — e.g. renewal limits or an
  overdue threshold.

Option (a) is preferred: it keeps the expert's business rationale intact and creates real
downstream work. It must be a stated ruling, not an improvisation during authoring.

### CR-5 — deprecate Book Category

Retire Category; replace with the Subject Classification introduced in CR-2. The sequencing is the
strongest feature of this design: because CR-2 already added subject taxonomy, CR-5 deprecates
something that has **actual consumers built on top of it**, so supersession and consumer migration
are exercised for real rather than declared against an empty consumer set. That is the vacuity trap
the plan's §4 exists to avoid, closed by construction.

### CR-6 — the refusal

One of: a duplicate active catalog authority; an unauthorized vocabulary extension; a second active
placement profile. Pick the one whose rejection is attributable to a single named governance rule —
a refusal that could be explained by three rules at once is weak evidence.

## 4. CR-1 problem statement

The P0 input for CR-1, in the form the plan requires — free-form business prose, human-authored,
making no design decisions:

> A community library maintains thousands of books and other published materials. Library staff
> currently maintain catalog records manually, leading to inconsistent descriptions, duplicate
> entries, and difficulty locating materials.
>
> The library requires a governed catalog management capability that provides a single authoritative
> record for each bibliographic work and each physical copy owned by the library.
>
> The system shall allow authorized staff to: register new books; register physical copies; update
> bibliographic information; retire obsolete records; search the catalog; retrieve complete book
> details.
>
> Each physical copy shall belong to exactly one bibliographic work. Every business operation shall
> be traceable and auditable.
>
> This release intentionally excludes borrowing, reservations, fines, patron management,
> acquisitions, and inventory reconciliation. Those capabilities are expected to be introduced
> through future governed change requests rather than being designed into the initial solution.

The closing paragraph is load-bearing. It is the business author declaring the deferral, which is
what makes the later CRs governed evolution rather than retrofitted scope. In P0 terms it maps
directly to the seed's **Out of Scope** register, and its presence is what lets a Stage-2
verification later distinguish "not yet built" from "was never intended."

## 5. What this addendum changes in the plan

- §4's CR table: five CRs become **six**, with `NEW_SUBDOMAIN` appearing twice (platform-level
  REUSE, then cross-subdomain REUSE).
- The domain is **`book_library_mgmt`**, not `book_library`; the release-4 subdomains are `catalog`
  and `circulation`.
- §8's fixture tree gains `cr_06_refused/` and renumbers: `cr_03_new_subdomain_circulation/`,
  `cr_04_modify/`, `cr_05_deprecate/`.
