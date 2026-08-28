# Stage 2 — Domain Model Discovery: transformation / build
**Stage:** 2 — Domain Model Discovery
**CR:** construction_determinacy
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned composition and against the
renderer that construction is. What was searched is recorded, not only what was found. Where a
belief came back narrower or wider than Stage 1 stated it, the correction is recorded against the
belief.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Design | The approved statement of what is to be built. | The seventh phase document of a dossier, with its registers. | VERIFIED | S1 business_vocabulary #1 |
| Mandate | The approved statement of what is to be built in what order. | The eighth phase document, scheduling only what does not yet exist. | VERIFIED | S1 business_vocabulary #2 |
| Rendering | Producing an artifact from what the design states. | One builder per family; eleven families are renderable. | VERIFIED | S1 business_vocabulary #3 |
| Determined fact | Something about an artifact that the design states. | Not held. Judged by whether the rendered value came out empty. | VERIFIED | S1 business_vocabulary #4 |
| Invented fact | Something the renderer supplies from anywhere but the design. | Not held, not counted, and indistinguishable from a determined one. | VERIFIED | S1 business_vocabulary #5 |
| The measure | The count of how much of an artifact the design determines. | Computed per build attempt; refuses below complete. | VERIFIED | S1 business_vocabulary #6 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The measure | Its population | Every leaf of what the renderer emits, walked one by one. Derived from the renderer, never declared. | VERIFIED | S1 system_beliefs #1 |
| The measure | Its test | Whether the rendered leaf came out empty, unless the design declared the emptiness deliberate. | VERIFIED | S1 system_beliefs #1 |
| Determined fact | How it is recognised | By being non-empty. Nothing distinguishes a value the design supplied from one the renderer did. | VERIFIED | S1 known_facts #12 |
| Invented fact | Where it comes from | A literal in the renderer, a default beside a design lookup, or the namespace of a scheduled artifact. | VERIFIED | S1 system_beliefs #5 |
| Rendering | What it may write | Every artifact the mandate schedules, plus a build manifest when it judges the domain to have none. | VERIFIED | S1 system_beliefs #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Measuring a design | An attempt to construct | The design determines its artifacts, or nothing is written. | VERIFIED | S1 business_events #1 |
| Rendering an artifact | A design that measured complete | The artifact, as the design determines it. | VERIFIED | S1 business_events #2 |
| Writing a construction | A rendering that measured complete | The artifacts on disk, under the root their binding declares. | VERIFIED | S1 known_facts #13 |
| Founding a domain's manifest | The renderer, when it judges the domain to have none | A manifest nobody designed. | VERIFIED | S1 known_facts #8 |
| Distinguishing a determined fact from an invented one | Nobody | Nothing performs this. | NOT_FOUND | S1 system_beliefs #1 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Measuring a design | 1 | Render every artifact the design and mandate name. | The rendered shape. | VERIFIED | S1 system_beliefs #1 |
| Measuring a design | 2 | Walk that shape leaf by leaf and count each leaf as a fact needed. | The population. | VERIFIED | S1 system_beliefs #1 |
| Measuring a design | 3 | Mark a leaf determined when it is not empty. | The measurement. | VERIFIED | S1 known_facts #12 |
| Measuring a design | 4 | Ask where each non-empty leaf came from. | Nothing. No step performs this. | NOT_FOUND | S1 system_beliefs #1 |
| Founding a domain's manifest | 5 | Read the domain from the namespace of the first artifact the mandate schedules. | The domain's name. | VERIFIED | S1 system_beliefs #3 |
| Founding a domain's manifest | 6 | Write the manifest when no file of that name exists beneath the root. | The manifest. | VERIFIED | S1 system_beliefs #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The population the measure counts is derived from the renderer rather than from the artifact. | VERIFIED | The requirement list is the shape the renderer emits, walked leaf by leaf, and its own account says so: the list *is* construction. That is deliberate and it is why the list cannot drift from the renderer — an earlier hand-written list held a hundred and seventy facts where the derived one holds seven hundred and ten. **The strength and the blind spot are the same property.** A leaf is counted determined when it is not empty, and a leaf the renderer fills from its own text is not empty. The measure cannot ask where a value came from, only whether there is one. | S1 system_beliefs #1 |
| A vocabulary's group name and spelling rule are literals in the renderer. | VERIFIED | One line writes both, as two constants, for every vocabulary the renderer will ever produce. No register of any phase carries either. The seven designed values are lower case and the rule written beside them says upper case, so the platform refused the artifact when the composition was next built. | S1 system_beliefs #2 |
| A build manifest is written when the renderer judges the domain to have none. | VERIFIED | The manifest is written when the mandate schedules anything, no file of its name exists beneath the root, and no generator was named for it. **Stage 1 said the domain was inferred from where the change sat; it is inferred from the namespace of the first artifact the mandate schedules.** For a business domain the namespace and the domain coincide, so the inference has been invisible. For the platform they do not: one domain carries a namespace per concern, so a vocabulary in the conformance namespace produced a manifest declaring conformance a business domain importing the platform. | S1 system_beliefs #3 |
| No design register carries a group name, a spelling rule or a domain name. | VERIFIED | The seventh phase declares twenty registers. The one that carries a vocabulary states a value and its meaning, and has no column for the group the values belong to or the spelling they must take. No register anywhere names the domain an artifact belongs to; the renderer reads it off the identity. | S1 system_beliefs #4 |
| Every family the renderer writes may carry invented facts, not only these two. | NOT_FOUND | Every builder was read and its literal values listed. **The belief is wider than what was found.** Of eleven families, one invents a fact no design can state: the vocabulary's group name and spelling rule. One invents a fact deliberately and says why in its own text: an event's moment-of-occurrence field, added because the event constitution fixes it and no design should restate it. Two carry a default beside a design lookup — a structure's layer, and a transform's kind and purity — which a design may state and which fall back when it does not. The rest write only the names of registers and keys. **One defect, one declared exception, three defaults.** | S1 system_beliefs #5 |
| Nothing else was written that the mandate did not schedule. | VERIFIED | Two changes have been emitted. One scheduled a single vocabulary and produced it plus a manifest. The other scheduled two artifacts, amended two, marked two superseded, and produced nothing further. The manifest is the only artifact ever written outside a mandate. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Measures a design and refuses an under-determined one | transformation::CT_PURE_MEASURE_COMPLETENESS_V0 | Measures Construction Completeness and refuses a design that does not determine its artifacts. | MISMATCH | Counts a leaf as determined when it is not empty, so a fact the renderer supplies passes as one the design stated. |
| Renders every artifact a mandate schedules | transformation::CT_PURE_RENDER_ARTIFACTS_V0 | Renders each artifact from the design that determines it. | MISMATCH | Supplies a vocabulary's group name and spelling rule from its own text, which no design may override. |
| Writes a rendered construction to disk | transformation::CC_PERSIST_ARTIFACTS_V0 | Writes a rendered construction beneath the root its runtime binding declares. | PARTIAL | Also writes a build manifest the mandate did not schedule, when it judges the domain to have none. |
| Carries out a construction | transformation::WF_CONSTRUCT_ARTIFACTS_V0 | Measures a design, refuses it if under-determined, and renders the artifacts it schedules. | PARTIAL | The act is right; two of its three steps carry the defect. |
| Constructs protocol artifacts from an approved design | transformation::CC_CONSTRUCT_ARTIFACTS_V0 | Constructs protocol artifacts from an approved design and mandate. | PARTIAL | Names the steps that measure, render and write; unchanged in shape by this. |
| Admits a design for construction | transformation::IN_CONSTRUCTION_REQUESTED_V0 | Offers an approved design and mandate for construction. | EXACT | Nothing. What is offered is correct; what is done with it is not. |
| Binds the construction lifecycle | transformation::RB_CONSTRUCTION_BINDINGS_V0 | Runtime bindings for the construction lifecycle. | EXACT | Nothing; unchanged by this. |

---

## 5. Gaps

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The measure cannot see a fact the renderer supplies. | HIGH | A design may measure complete while the renderer authors part of the artifact. This is the gap that makes the change a mechanism rather than a correction to two builders. | VERIFIED | S1 business_invariants #2 |
| A vocabulary's group name and spelling rule cannot be designed. | HIGH | Every vocabulary the renderer writes carries the same two, and the one written so far was refused by the platform for it. | VERIFIED | S1 requested_outcomes #2 |
| A domain is read from an artifact's namespace. | HIGH | For the platform, one domain carries many namespaces, so the inference produces a domain that does not exist. It has been invisible because every domain emitted so far was a business domain, where the two coincide. | VERIFIED | S1 requested_outcomes #4 |
| An artifact is written that no mandate scheduled. | MEDIUM | A mandate freezes scope at a gate; something written outside it was approved by nobody. | VERIFIED | S1 business_invariants #3 |
| A default and a determined fact are indistinguishable in the measurement. | MEDIUM | Three defaults are in use. Each is overridable by a design and none is wrong today, but the measure counts a fallback exactly as it counts a stated fact. | VERIFIED | S1 system_beliefs #5 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The measure's strength and its blind spot are one property. | Deriving the population from the renderer is what stops the list drifting, and is exactly what makes a fact the renderer never asks for uncountable. Replacing the derivation would reintroduce the drift it was built to end. | VERIFIED | S1 system_beliefs #1 |
| The renderer already knows how to declare an invented fact honestly. | An event's moment-of-occurrence field is added by the renderer and its own text states why: the event constitution fixes it, and a design that states its own keeps it. The distinction between a fact worth supplying and one worth refusing is already drawn once, in prose. | VERIFIED | S1 system_beliefs #5 |
| A default already has a place to be overridden. | A structure's layer and a transform's kind and purity are read from the design and fall back only when absent. The pattern for a designable fact with a default exists; the vocabulary's two facts simply have no lookup at all. | VERIFIED | S1 system_beliefs #5 |
| The domain inference was invisible because every emit so far was a business domain. | In a business domain the artifact's namespace and its domain are the same word. The first platform emit was the first time they differed, and it produced a manifest for a domain that does not exist. | VERIFIED | S1 known_facts #9 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A leaf-walking measure cannot see a fact that is a path. | The group a vocabulary's values belong to is a key in the rendered shape, not a value in it, so no leaf is it. Recording it as one marks every leaf beneath it supplied, which slanders each entry the design did state. The spelling rule beside it is a value and is visible, so a vocabulary whose group is undesigned is caught anyway — but by its neighbour rather than by itself, and a group undesigned where the spelling is stated would pass. | MEDIUM | VERIFIED | S1 system_beliefs #1 |
| A literal census finds what is written as text and not what is computed. | Every builder's literal values were listed. A fact the renderer derives from a path, a length, or the order of a list would not appear in that census, and the domain inference is precisely such a fact — it was found by reading, not by listing. | HIGH | VERIFIED | S1 system_beliefs #5 |
| Two emits are a thin basis for the claim that nothing else is written outside a mandate. | Both were run in one session, on two changes, against two domains. Nine families have never been emitted at all. | MEDIUM | INSUFFICIENT_EVIDENCE | S1 system_beliefs #6 |
| Whether a default should count as determined is undecided. | Three defaults are in use, each overridable, none wrong today. A design that omits one gets a working artifact and a complete measurement, which is either a convenience or the same defect in a milder form. | MEDIUM | VERIFIED | S1 system_beliefs #5 |

---

## 8. Open Questions

<!-- register:open_questions business_language -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Is a build manifest something a design ever schedules, or something outside construction entirely? | GOVERNANCE | Discovery sharpened rather than answered it. The manifest's own account calls every field of it compiler configuration and says no phase designs it — which argues for removing it from construction rather than giving it a design. Both are available and they are not the same act. | S1 clarification_requests #1 |
| Does a default count as a fact the design determined? | GOVERNANCE | Three are in use and none is wrong. Counting a fallback as determined is the same move that let the vocabulary's two literals pass, in a milder form, and the answer decides whether this change reaches three more facts. | S1 system_beliefs #5 |
