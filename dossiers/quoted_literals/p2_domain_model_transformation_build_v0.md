# Stage 2 — Domain Model Discovery: transformation / build
**Stage:** 2 — Domain Model Discovery
**CR:** quoted_literals
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against how construction renders a binding today and
against the designs already delivered. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Binding | A design's statement of where a step's input comes from. | A row of the Design Intent's step-bindings register, rendered into the input of a node or step. | VERIFIED | S1 business_vocabulary #1 |
| Literal | A binding to a value the design fixes. | Rendered by the same reading of a value that renders a field's default and an artifact's property. | VERIFIED | S1 business_vocabulary #2 |
| Quoted literal | A literal written inside quote marks, as a value with a dot in it must be. | Rendered as its text, quote marks included. | VERIFIED | S1 business_vocabulary #3 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Literal | Rendered value | The value the artifact carries for it. | VERIFIED | S1 requested_outcomes #1 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Rendering a binding | Construction, from an approved design | The artifact carries a value for the input. | VERIFIED | S1 business_events #1 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Rendering a binding | 1 | A list or mapping is read as one; a reference is rendered as the runtime's path to it. | The input's value. | VERIFIED | S1 system_beliefs #1 |
| Rendering a binding | 2 | Anything else is read as a literal: true or false, a whole number, or else the text as written. | The input's value. | VERIFIED | S1 system_beliefs #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Construction hands the runtime a quoted literal with its quote marks. | VERIFIED | Rendered today: a binding written "si.artifact.list" yields the text with both quote marks, and one written in single quotes keeps them too. | S1 system_beliefs #1 |
| Construction reads a whole number as a number and any other number as text. | VERIFIED | Rendered today: 3 yields the number 3, and -1.5 yields the text -1.5. | S1 system_beliefs #2 |
| No delivered artifact carries a quoted or decimal literal. | VERIFIED | No step binding of any delivered design is quoted or decimal. The quoted and decimal values delivered designs carry are test-case values, which are read as YAML and rendered by another path. | S1 system_beliefs #3 |
| The design is admissible and construction reports the artifact determined, while the runtime receives the wrong value. | VERIFIED | The measure marks a value determined when the design states one, and a quoted binding states one. | S1 system_beliefs #4 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Renders artifacts from a design | transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Renders every artifact a mandate schedules from the design that determines it. | PARTIAL | Render a quoted or decimal literal as the value it states. |
| Constructs artifacts from a design | transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Measures, renders and writes the artifacts a mandate schedules. | EXACT | Nothing here; it runs the rendering unchanged. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A quoted literal renders with its quote marks. | CRITICAL | The runtime receives a value the design never stated, and nothing reports it. | VERIFIED | S1 system_beliefs #1 |
| A decimal number renders as text. | MAJOR | The runtime receives text where the design stated a number. | VERIFIED | S1 system_beliefs #2 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| One reading of a value renders a binding, a field's default and an artifact's property. Correcting it for bindings alone leaves the other two rendered as today. | The same reading is called from the three places. | VERIFIED | S1 constraints #1 |
| The rendering of a binding is the transform's implementation; its declaration states nothing about how a literal is rendered. | The render transform's declaration names its inputs and outputs and no rendering of a value. | VERIFIED | S1 requested_outcomes #3 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| One probe asserts that a quoted literal keeps its quotes, recording today's rendering as intended. | The keyed-node design test expects each recorded reason with its quote marks. | MINOR | VERIFIED | S1 system_beliefs #1 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
