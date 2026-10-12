# Delivery — transformation genesis

This dossier describes the transformation module as it stands: 46 artifacts across the design and
build subdomains. It is judged on admission only, against a composition that holds everything except
transformation.

## How it was written

- P0–P6 were written by hand. P1 is the seed's projection (`tc phase project`).
- P5's `provisional_codes` and P7 were generated from the live registry, and P8 from P7, by the
  scripts in `.github/process/notes/genesis-generators/`, kept as they ran. The design decisions and the
  refusal deferrals in P7 are stated by hand.
- The problem statement was drafted for its author to confirm at Gate 0.

## What the dossier exposed

Each is entered in `transformation/doc/REBUILD_CHARTER.md` §8 (Genesis) before any code changes.

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
| G-11 | The compiler reads artifact names in test data as references | Fixed: `software_governance/dossiers/data_parts` declares a vector's cases data |

## Where it stands

- Pinned to `b6e2a39c…`, the composition without transformation, side-assembled after G-11. The first
  pin, `01fd3cfe…`, predates the vocabulary's new version and was retaken once, deliberately.
- P0–P8 are each admissible under the rebuilt module's declared rules, with no findings.
- No gate is closed. Gate 0 (the seed), Gate 1 (P7) and Gate 2 (P8) are the business author's.
- G-2, G-3, G-4 and G-8 stay open. Each goes through the lifecycle after the swap.
