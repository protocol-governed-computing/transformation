# Genesis Triage and the G-11 Design

The genesis dossier was meant to check the rebuilt module at the end. Instead it ran early and found
eleven defects (charter §8, Genesis). Five were fixed as they were found. This document stops that
pattern. It sorts every finding once, designs the one fix the swap needs, and moves the dossier back
to the end.

---

## 1. The rule from here

- The genesis dossier is frozen. Nothing more is fixed because the dossier found it.
- Before the swap, one change lands: G-11, designed below and approved before it is built.
- The dossier is then regenerated once, against the finished module, as acceptance item 7.
- Every other open finding goes through the lifecycle after the swap, judged by the rebuilt module.

---

## 2. Triage

### 2.1 Fixed, and kept

Each was declared in charter §8 before its code, is covered by a test, and leaves the regression and
the oracle comparison green. Rolling them back would undo correct work.

| Finding | What was fixed |
|---|---|
| G-1 | A phase check against a composition without its policy reports the rating as not computed |
| G-5 (part) | Vectors for four transforms; transform conformance proves all four |
| G-6 | The store rule reads the design language's `storage_type` group, not a capability's category |
| G-7 | Render returns the `sources` it declares; `CT_PURE_ATTRIBUTE_PROVENANCE_V1` reads them |
| G-9 | The compiler does not require a superseded transform to be reached |
| G-10 | `STRUCTURE_BUILD_TRANSFORMATION_CONFIG_V1` compiles the module's vocabularies and vectors |

### 2.2 Before the swap

| Finding | Why it cannot wait |
|---|---|
| G-11 | It blocks the genesis dossier's admission. Render and attribution cannot carry vectors until a vector's data stops being read as references. |
| G-5 (rest) | Two vectors, render and attribution. They follow G-11 directly. |

### 2.3 After the swap, through the lifecycle

None of these blocks admission. Each is a change to the rebuilt module, judged by it.

| Finding | What it is | Why it can wait |
|---|---|---|
| G-2 | Construction gives every workflow the same actor | Affects reconstruction only; admission is the acceptance bar |
| G-3 | The design language cannot state a field's `structure` | Affects reconstruction only |
| G-4 | Three seed refusals are enforced outside any governed workflow | True of the module today; the dossier states them as deferrals |
| G-8 | The completeness measure ignores the provenance it is handed | The gate works; this is a second derivation of one fact |

---

## 3. The G-11 design

### 3.1 The defect

S1 finds the references in a declaration by walking it. A full name under a reference part is a
reference. A full name anywhere else is refused as undeclared (E105). The one exception is the
supersession parts, which name an artifact without reaching it.

A vector is data. Its cases hold the inputs a transform is handed and the outputs it must return. A
design compiler's inputs and outputs name artifacts: a rendered actor carries
`governed_by: governance::CONSTITUTION_GOVERNANCE_V0`. S1 reads that value as a reference, finds it
in no reference part, and refuses the vector.

### 3.2 The change

The platform declares a third kind of part beside references and supersession: **data**. A data
part holds values. Nothing beneath it is read for references.

- **`artifact::VOCAB_DECLARATION_REPRESENTATION_V1`** supersedes V0. It adds one group:

  ```yaml
  data:
    casing: lower_snake
    entries:
    - cases
  ```

  `cases` is the part of a TEST_DATA artifact that holds its vectors, and no other kind uses it.
  `target`, the transform a vector tests, stays outside it and stays a reference.
- **The compiler** reads V1. `representation.py` names V1, adds `data` to its groups, and its walk
  skips a data part exactly as it skips a supersession part. Every reference finder goes through
  that walk, so none needs changing.
- **`sameness`** names V1. A data part is compared as values, which it already does; a value under
  it is never re-pointed to a successor, which also holds already.
- **`test_reference_semantics`** gains two cases: a full name under `cases` is not a reference, and
  `target` still is.

### 3.3 What it does not change

- No artifact other than the vocabulary changes meaning. Its V0 stands down and is deleted at the
  swap with the rest.
- Nothing else reads the vocabulary by identity. The handlers that mention it read it through
  `representation.py`.
- A key name means the same thing in every kind. `bindings` was not chosen, because a runtime
  binding's `bindings` is a reference-keyed part.

### 3.4 How it is governed

The vocabulary is a platform artifact, so this is a `software_governance` change. It runs as one
dossier, judged by the frozen oracle, so the rebuilt module does not judge a change it depends on.
The compiler and `sameness` changes follow from the vocabulary and land with it.

### 3.5 How it is proven

1. `test_reference_semantics` passes with its two new cases.
2. The two remaining vectors are authored, and transform conformance proves all six transforms.
3. `regression.sh --all` passes, and the oracle comparison stays identical.
4. The genesis dossier is regenerated and admitted, P0 to P8, as acceptance item 7.

---

## 4. After G-11

1. Regenerate the genesis dossier once: re-check P0–P6, regenerate P5 and P7, generate P8, judge
   every phase.
2. Run the single-instance check and the rehearsed swap again.
3. Swap (charter §10).
