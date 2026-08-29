# Sealed protocol — Exp55: each human's growth slope, predicted from their own component spectrum

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any cohort subject's
spectrum was computed.

## 1. The claim
The confirmed estimator mechanics (be89cd3/b9b4540: averaging lowers a per-component
floor as 1/m and reveals components one by one) predict each subject's R-dim growth
curve from their coherent component spectrum {S_k} and trajectory floors {N_k}:
R_pred(n) = Σ_k S_k / (S_k + N_k·(m₀/(n/2))). The 30-subject TMS-EEG cohort of the
program's C6 confirmation (doi 10.5281/zenodo.22101653 companion analyses; published
per-subject R-dim at n ∈ {16, 30, 60, 120}) has its slopes public — **but no subject's
spectrum has ever been computed**. Blindness therefore rests on the predictor, exactly
as in the program's P1 design. Claim: the predicted slope orders the subjects.

## 2. Operational definitions (frozen)
Loading and preprocessing: byte-identical code path to the frozen pipeline21 (same
artifact interpolation −5..+20 ms, filters 1–90 Hz + notch 50, bad-channel rule,
resample 725 Hz, epochs −1.0..+0.999 s, |amp| < 300 µV trial rejection). Per subject,
on ALL valid trials (halves n//2): response window 0–300 ms (218 samples); basis = SVD
of half-A average; K = 30; **S_k = max(0, ⟨p_A, p_B⟩ − median of 20 circular-shift
nulls)** (the bench-certified v2: subtract-the-null, not cut-by-the-null; shift rng
520000 + int(subject number)); gate: total cross-power must exceed the max total null
(a gated-out subject is reported and excluded, counted); **N_k = T_R·var_t(residual
projections)/m₀** (trajectory object, m₀ = n//2); R_pred(n) on the published grid
{16, 30, 60, 120}; b_pred = OLS slope of R_pred vs ln n. b_obs = OLS slope of the
PUBLISHED rd values vs ln n (resultados_exp31.jsonl, untouched). One run.

## 3. Disclosure
Bench history (all archived): geometry-150 bench validated 4/4 first try (order +0.892);
at the real geometry (218 samples, real grid) BA failed by 0.013 (amplitude-dependent
tail detection of the binary cut) and the single documented estimator iteration
(subtract-the-null) re-validated 4/4 (order +0.850, amplitude-leak 0.308, nulls 8/8).
Pilot: sub-001, which is NOT part of the 30-subject cohort (it was the exp21 pilot),
ran the full pipeline (119 trials, gate passed 4× over null, b_pred = +2.09). No cohort
subject has been touched; cohort raw files will be re-downloaded from OpenNeuro
ds008037 (open data) after this seal.

## 4. Sealed test
- **P1:** Spearman(b_pred, b_obs) over the cohort's gated subjects ≥ 0.50, one-sided
  p < 0.05, with n ≥ 25 gated (fewer ⇒ verdict marked underpowered).

| Outcome | Reading |
|---|---|
| P1✓ | First real-data validation of the estimator mechanics: a human's growth slope is predicted from their own component spectrum. C6 stops being only a law and becomes a mechanism observed in people. |
| P1✗ | The mechanics do not transport to human TMS-EEG at per-subject resolution; reported dead, with the full scatter published. |

## 5. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome travels with the next firm
deposit.
