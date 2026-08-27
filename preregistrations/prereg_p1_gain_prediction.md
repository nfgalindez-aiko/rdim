# Sealed protocol — P1: quantitative test of the uniform-gain visibility account

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of the commit adding this file, BEFORE the new
quantity it requires (evoked-amplitude gain γ) was computed for any animal.

## 1. The prediction
The minimal visibility account (companion constraints paper) posits response components with
amplitudes a_k = A·e^(−k/τ) against an effective noise floor θσ/√n, giving
R(n) ≈ τ·ln(A/θσ) + (τ/2)·ln n. If a state change acts as a **uniform gain** γ on all
component amplitudes, then for each animal:

  **D_pred = 2·b̄·ln(RMS_awake / RMS_iso)**,  and the account predicts **D_obs ≈ D_pred**,

where b̄ is the within-state growth slope per ln n (τ/2 in model terms) and the RMS ratio
estimates 1/γ from the evoked response amplitude itself.

## 2. Disclosure of what is already known at sealing
The R-dim growth curves of both states (hence D_obs and the slopes) are already published
(preprint 6, per-animal archive) and were seen before this protocol was written. **The test's
blindness rests entirely on γ**: the evoked-amplitude ratio has never been computed for any
animal, and D_pred cannot be anticipated from the published quantities. The protocol commits
all analysis choices before γ exists.

## 3. Operational definitions (frozen)
Data and pipeline: identical to preprint 6's sealed pipeline (dandiset 000458; same
preprocessing, artifact rules A1/A2, matching by state and current; same seeds; pilot animal
sub-521885 excluded). Tier: confirmatory animals with matched N_AI ≥ 120 (the H1 tier, n = 20).
- **Amplitude:** per state, on exactly the first 120 matched trials (the same trials as the
  published rd120): trial-average the epochs, subtract the mean of the baseline window, and
  take the RMS over (channels × response-window samples). γ_inv = RMS_awake / RMS_iso.
- **Slope b̄:** per state, OLS slope of R(n) against ln n over the published grid points with
  n ≤ N_AI (at least {30, 60, 120}); b̄ = mean of the two states' slopes (the model holds them
  equal; averaging reduces noise).
- **Observed displacement:** D_obs = mean over the same grid points of [R_awake(n) − R_iso(n)].
- **Technical exclusions (by criterion):** animals with b̄ ≤ 0 (no growth: the model's
  premise is absent, no prediction defined); for T-P1b only, animals with D_pred < 0.05
  (ratio unstable). Counts reported.

## 4. Tests and interpretation matrix (sealed)
- **T-P1a (ordering):** Spearman correlation between D_obs and D_pred across animals > 0,
  one-sided p < 0.05.
- **T-P1b (calibration):** median of D_obs/D_pred within [0.5, 2].

| T-P1a | T-P1b | Reading |
|---|---|---|
| pass | pass | The uniform-gain visibility account is quantitatively supported: anesthesia's effect on R-dim is predicted, animal by animal, from evoked amplitude alone. |
| pass | fail | Ordering right, scale wrong: gain is real but not uniform across components, or the spectrum is not exponential. The account survives qualitatively only; the calibration failure is published. |
| fail | —   | The uniform-gain reading of constraint C9 is dead. The visibility mechanics remain supported only by C5–C7; the account's §4 is amended accordingly and the failure is published. |

## 5. Honesty rules
One computation of γ; no re-runs with altered definitions. The outcome enters the
constraints paper (currently unreleased) whichever cell it lands in, before that paper is
deposited. All numbers must pass a mechanical verifier against result files.
