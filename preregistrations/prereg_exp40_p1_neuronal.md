# Sealed protocol — Exp40: The gain prediction (P1) tested at the neuronal level

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE the one quantity the
prediction needs — the evoked-amplitude gain ratio of the SPIKING response — was computed
for any animal.

## 1. The prediction, carried across levels
The minimal visibility account (constraints paper) predicts that a state acting as uniform
gain γ on component amplitudes displaces the R-dim growth curve by D_pred = 2·b̄·ln γ. This
passed its sealed test on EEG (protocol 9be5d99: ordering ρ = +0.41, p = 0.038; median
observed/predicted ratio 1.00). If the account describes mechanism rather than a field-level
coincidence, the SAME prediction must hold one level down, in the spiking populations of the
same brains: D_pred_spk = 2·b̄_spk·ln(RMS_spk_awake / RMS_spk_iso) ≈ D_obs_spk.

## 2. Disclosure and blindness
Known at sealing: the spiking growth curves per state (exp37 archive; D_obs_spk and slopes
are derivable from them) and the EEG P1 result. NEVER computed — the blindness — is
γ_spk: the ratio of trial-averaged evoked spiking-response RMS between states. All analysis
choices are frozen here before γ_spk exists for any animal.

## 3. Operational definitions (frozen; mirror of protocol 9be5d99)
Animals: the 15 exp37 confirmatory animals. Trials: exactly the matched sets of preprints
6–7 (first-120 per state, same seeds). Binned population response: 10 ms bins, epochs,
blanking and windows as preprint 7.
- **Amplitude:** per state, trial-average the binned (trials × units × bins) tensor over
  trials, subtract each unit's baseline-window mean, take RMS over (units × response-window
  bins). γ_spk_inv = RMS_awake / RMS_iso.
- **Slope b̄_spk:** per state, OLS slope of R_spk(n) vs ln n over the exp37 grid points with
  n ≤ N_AI (at least {30, 60, 120}); b̄ = mean of the two states' slopes.
- **Observed displacement:** D_obs = mean over those grid points of [R_awake(n) − R_iso(n)].
- **Technical exclusions (by criterion):** animals with b̄ ≤ 0; for T-b only, animals with
  D_pred < 0.05. Counts reported.

## 4. Sealed tests and matrix (identical to 9be5d99)
- **T-a (ordering):** Spearman(D_obs, D_pred) > 0, one-sided p < 0.05.
- **T-b (calibration):** median D_obs/D_pred within [0.5, 2].

| T-a | T-b | Reading |
|---|---|---|
| pass | pass | The gain account predicts across levels of description: strongest support yet — the visibility mechanics are substrate-general, not a field artifact. |
| pass | fail | Ordering carries across levels but the scale does not: gain is real but level-specific in magnitude. Partial; published. |
| fail | — | The gain account does not carry to spikes: its EEG success is field-specific or coincidental. Uncomfortable and published. |

## 5. Rules
One computation of γ_spk; no re-runs with altered definitions. The outcome travels in the
next firm deposit whichever cell it lands in. Mechanical verifier before any number is
quoted in a draft.
