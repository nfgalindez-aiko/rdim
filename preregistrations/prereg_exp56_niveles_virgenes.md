# Sealed protocol — Exp56: predicting each human's R-dim level, on virgin subjects (double-blind style)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any virgin subject's
data was processed (neither their R-dim nor their spectrum has ever been computed).

## 1. The claim and its full origin (disclosed)
Exp55 (60a39a6) died as sealed: per-subject growth SLOPES are unpredictable — and its
post-hoc diagnostics showed why: the slope's own split-half reliability is +0.317, so
the sealed bar sat above the target's physical ceiling (recorded as method rule #2:
measure the target's reliability before sealing; the bar must sit below it). The same
diagnostics found the real bridge: on the burned 30-subject cohort, predicted LEVELS
track observed R-dim per subject (+0.827/+0.709/+0.658/+0.467 at n = 16/30/60/120,
exploratory, fully disclosed), and the level target is reliable: split-half ceiling of
rd60 = +0.809. This protocol seals the level claim on subjects never touched by any
analysis: ds008037 contains 26 subjects outside the exp31 cohort (which was filled in
ID order); for them, BOTH quantities are computed for the first time inside the single
sealed run.

## 2. Design (frozen)
Subjects: the 26 ds008037 IDs outside the exp31 cohort and the pilot (sub-010, -012,
-014, -018, -024, -030, -031, -033, -038, -040, -043, -044, -045, -046, -047, -048,
-051, -055, -057, -061, -062, -065, -068, -071, -072, -073). Loading/preprocessing:
byte-identical to frozen pipeline21 (artifact interpolation, filters, bad-channel rule
with its >12 exclusion, resample 725 Hz, epoching, |amp| < 300 µV rejection). Inclusion:
≥ 120 valid trials (the exp31 convention); excluded subjects counted and reported.
- **rd60**: pci_xv_trials on the first 60 valid trials (n_splits = 4, seed = 0 — the
  frozen exp31 convention).
- **R_pred(60)**: the bench-certified exp55 pipeline, unchanged (all valid trials,
  halves m₀ = n//2; SVD basis of half A; K = 30; S_k = max(0, cross − median of 20
  circular-shift nulls), shift rng 520000 + subject number; total-vs-max-null gate;
  trajectory floors N_k; R_pred(60) = Σ S_k/(S_k + N_k·(m₀/30))).
One run of everything.

## 3. Sealed test
- **Q1:** Spearman(R_pred(60), rd60) over included, gated subjects ≥ 0.45, one-sided
  p < 0.05, requiring n ≥ 15 (fewer ⇒ verdict marked underpowered).

| Outcome | Reading |
|---|---|
| Q1✓ | First sealed real-data validation of the estimator mechanics: a human's reproducible-dimensionality level is predicted from their own component spectrum, on subjects no analysis had ever touched. |
| Q1✗ | The exploratory bridge did not generalize; reported dead with the full scatter. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome travels with the next firm
deposit.
