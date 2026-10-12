# Delivery — transformation genesis

This dossier describes the transformation module as it stands: 46 artifacts across the design and
build subdomains. It is judged on admission only, against a composition that holds everything except
transformation.

## How it was written

- P0–P6 were written by hand. P1 is the seed's projection (`tc phase project`).
- P5's `provisional_codes` and P7 were generated from the live registry, and P8 from P7, by the
  scripts in `scripts/genesis/`, kept as they ran. The design decisions and the
  refusal deferrals in P7 are stated by hand.
- The problem statement was drafted for its author to confirm at Gate 0.

## What the dossier exposed

Each was entered in the rebuild charter's §8 (Genesis) before any code changed. The charter is
held by git.

| Finding | What it is | Disposition |
|---|---|---|
| G-1 | The phase check crashed reading its merit policy from a composition without transformation | Fixed: the rating is not computed |
| G-2 | The design language gives every workflow the same actor | Open; reconstruction only |
| G-3 | The design language cannot state a field's structure | Open; reconstruction only |
| G-4 | Three seed refusals are enforced outside any governed workflow | Stated as deferrals |
| G-5 | None of the six transforms carries a test vector, which P7 refuses | Fixed: all six proven by vectors |
| G-6 | The store rule refuses a root-addressed persistence step | Fixed: the rule reads the store-keeping vocabulary |
| G-7 | Construction's provenance step reported every leaf as stated by the design | Fixed |
| G-8 | The completeness measure ignores the provenance it is handed | Open |
| G-9 | A stood-down transform was required to be reached | Fixed in the compiler |
| G-10 | The module's vocabularies and vectors were never compiled | Fixed: the build manifest names them |
| G-11 | The compiler reads artifact names in test data as references | Fixed: `artifact::VOCAB_DECLARATION_REPRESENTATION_V1` declares a vector's cases data (dossier `data_parts`, held on `archive/rebuild-transformation`) |
| G-12 | P5's entry point did not declare `prior_texts`, which its workflow reads, so the gate admitted a payload the workflow could not resolve | Fixed: `IN_BUSINESS_INTENT_SUBMITTED_V1` requires it, as every other phase's entry point does; V0 is retired by record |

## Where it stands

- Pinned to `72ff39c8…` (497 artifacts), the composition without transformation, side-assembled
  after blockchain's cr_07_own_values. Each earlier pin was retaken deliberately: `01fd3cfe…` predates
  the vocabulary's new version, `b6e2a39c…` still held the three platform artifacts the swap deleted,
  and `37968c3e…` still held the fourteen blockchain identities cr_07 retired.
- P0–P8 are each admissible under the rebuilt module's declared rules, with no findings.
- No gate is closed. Gate 0 (the seed), Gate 1 (P7) and Gate 2 (P8) are the business author's.
- G-2, G-3, G-4 and G-8 stay open. Each goes through the lifecycle, judged by the rebuilt module.
