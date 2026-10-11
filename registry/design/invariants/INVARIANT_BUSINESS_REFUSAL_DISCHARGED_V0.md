# INVARIANT_BUSINESS_REFUSAL_DISCHARGED_V0

## Machine

```yaml
fqdn: transformation::INVARIANT_BUSINESS_REFUSAL_DISCHARGED_V0
artifact_kind: INVARIANT
version: V0
governed_by: transformation::CONSTITUTION_DESIGN_V0
authority: pgc.platform
concern: design
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the design compiler, evaluating each phase's sealed rule set over a phase document
assert_projection:
  applies_to_kinds:
  - WF
```

---

## 1. Claim

Every refusal the business declared is refused by a real step and outcome, deferred to a named owner, or carried by a rule in force.

## 2. Why

A refusal stated in prose and carried by nothing refuses nothing. The business believes the system says no, and it does not.

## 3. How it is checked

Each declared refusal is accounted for: a discharge names a step and an outcome the topology really has and that routes to a refusing ending, a deferral names its owner, or a governing rule is in force in the pinned composition.
