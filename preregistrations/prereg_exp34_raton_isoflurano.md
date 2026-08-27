# Preregistration — Exp34: Reproducible dimensionality across wakefulness and isoflurane anesthesia in the same brain (DANDI 000458)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the timestamp of the public commit adding this file, BEFORE any neural
signal from this dataset was read. Dataset knowledge at sealing time: metadata only (session
list, trial tables, electrode tables, sampling rates), archived in the project's scouting map.

## 1. Dataset and question
DANDI 000458 (Allen Institute; Claar, Rembado et al. 2023): 30-channel epidural EEG at 2500 Hz
with biphasic intracortical electrical stimulation in head-fixed mice, with the same animal
awake and under isoflurane anesthesia (subset: post-anesthesia recovery).

**Question:** Within the same brain, is the reproducible dimensionality (R-dim) of the evoked
response lower under isoflurane than awake — and does its growth-with-trials curve flatten?

## 2. Instrument (frozen)
R-dim / PCIst-XV exactly as released in the rdim package v0.1.0 and used in our preprints
(10.5281/zenodo.22101483, .22101631, .22120070): 4 random split-halves (seed = 1000 + subject
index, fixed), SVD basis + SNR>1.1 + 99% variance retention fitted on one half, sum of positive
cross-half correlations of retained response projections. No parameter may be tuned on this
dataset. R-dim values are configuration-specific; only within-configuration comparisons count.

## 3. Preprocessing (frozen; technical amendments allowed only at pilot stage, documented
before any confirmatory computation)
- Signal: acquisition/ElectricalSeriesEEG only. Channels with electrodes.is_data_valid False
  dropped.
- Trials kept: stimulus_type=='electrical', is_valid==True, is_running==False, with defined
  (non-n/a) target region and current, behavioral_epoch in {awake, isoflurane, recovery}.
- Epochs −0.6 to +0.6 s around stimulus onset. Stimulation-artifact blanking: samples in
  [−0.002, +0.010] s excluded from all windows.
- Baseline window (−0.4, −0.05) s; response window (+0.01, +0.5) s.
- Band-pass 1–90 Hz; 60 Hz notch (scipy iirnotch); decimation ×5 (effective 500 Hz).
- Artifact rejection: per-trial 99.9th-percentile robust |z| > 6 (as amended in exp32).

## 3b. AMENDMENT A1 (pilot stage, sealed before any confirmatory computation)
**Change:** the artifact-rejection criterion is computed on the **baseline window only**
(−0.4, −0.05 s), instead of over the whole epoch. Threshold unchanged (per-trial 99.9th
percentile of robust |z| > 6, robust statistics from the baseline).

**Reason (verifiable from the pilot diagnostic, independent of any effect direction):** with
direct intracortical electrical stimulation the evoked response is *larger* than the
stimulation artifact. In pilot sub-521885 the median-across-channels max robust |z| was 2.3
in baseline, 10.9 in the artifact window and **13.7 in the response window**. A whole-epoch
criterion therefore rejects trials *for having strong brain responses* (36% of trials were
being discarded, leaving matched N=75, below the N≥120 tier). Rejecting on baseline targets
what the criterion was meant to target — contaminated trials — and is agnostic to response
amplitude, hence to the tested hypotheses. The threshold value and every other parameter
are unchanged.

**Disclosure:** at the time of writing this amendment the pilot's own R-dim values had been
seen (awake 1.39 vs isoflurane 0.93 at n=60). The amendment is justified solely by the
window-magnitude diagnostic above and applies identically to all states; the pilot remains
excluded from all confirmatory tests.

## 3c. CORRECTION A2 (implementation bug fix + technical validity rule; sealed before any
confirmatory result was computed)
**Bug found:** epoch extraction located each stimulus by linear arithmetic,
sample = round((t_stim − t_first) × 2500). Recordings in this dataset can contain **gaps**
(session sub-521887 is missing ~102 s, i.e. 255,796 samples), so after a gap this indexing
read the EEG several seconds off target. In that session every trial was corrupted (0 valid
trials); other sessions may have lost trials silently.

**Fix:** stimulus samples are now located by search over the recording's actual timestamps,
and each epoch is verified to be time-continuous (its span must equal the nominal epoch
duration within 2 ms). Epochs crossing a recording gap are dropped as technically invalid —
they cannot be epoched, the same category as the fs≤360 Hz exclusion in exp32.

This is a correctness fix plus a validity rule, applied identically to all states, currents
and sessions, and independent of any outcome. All sessions processed before the fix were
discarded and recomputed from scratch. No confirmatory statistic had been computed at the
time of the fix.

## 4. Trial matching (the paper-5 lesson, applied to ourselves)
All state comparisons use matched trials within each session:
- Restrict to current levels present in BOTH compared states.
- Within each current level: n_c = min(count_awake_c, count_state_c); take the FIRST n_c
  valid trials chronologically from each state.
- Matched total N = Σ n_c. Comparisons at equal N per state, always.

## 5. Session/subject selection (fixed from metadata, before signals)
One session per subject: the one with the largest matched awake/isoflurane N (tie → earlier
date). **Pilot subject: sub-521885** (smallest file), excluded from all confirmatory tests.
Inclusion tiers: T-A (H1): matched N ≥ 120. T-B (curves, H2): matched N ≥ 240.
T-C (reversibility, H4): recovery present with matched (iso,recovery) N ≥ 120.
If T-A yields < 8 subjects, all analyses become descriptive (no confirmatory claims).

## 6. Confirmatory hypotheses (Wilcoxon signed-rank, one value per animal, α=0.05 each;
the matrix below fixes joint interpretation)
- **H1 (state):** R-dim(awake, n=120) > R-dim(iso, n=120). One-sided.
- **H2 (curve flattening):** with grid n ∈ {30,60,120,240,(480 if available)} truncated to
  matched N: I_high = R(n_max) − R(n_max/2) computed per state; test
  I_high(awake) > I_high(iso). One-sided. (Within-state ceiling tests T1/T2 as in exp32 are
  reported per state as secondary descriptives.)
- **H4 (reversibility, tier T-C):** R-dim(recovery, n=120) > R-dim(iso, n=120). One-sided.

## 7. Interpretation matrix (sealed)
| H1 | H2 | Reading |
|---|---|---|
| yes | yes | Unconsciousness lowers reproducible dimensionality AND flattens its growth — full confirmation. |
| yes | no  | Level drops but growth persists: fewer visible components, comparably deep well. Partial. |
| no  | yes | States differ in the tail, not at n=120: curves dissociate what points cannot. Partial (methodological headline). |
| no  | no  | R-dim does not separate these states in mouse EEG. Negative result; published as such. |
H4 failing while H1 passes downgrades interpretation to "state-associated with possible
temporal drift". H4 passing upgrades it to "reversible with the state".

## 8. Secondary / controls (descriptive, no confirmatory claims)
- Standard PCIst vs R-dim on identical matched trials: does the standard's separation
  survive debiasing, and how much of it was bias?
- Dose-response: R-dim(awake, n=120) vs current level (non-decreasing expected).
- Region subgroups (MOs-stimulated vs SSp-stimulated sessions).
- Growth law: median R-dim(n) curves per state; comparison with human exp32 curves.

## 9. Sensitivity analyses (sealed)
S1: band 1–200 Hz, decimation ×2. S2: response start +0.02 s (double artifact margin).
S3: is_running trials included. S4: rejection threshold |z| > 5.
Verdicts are claimed only if the H1 verdict is unchanged in S1–S4.

## 10. Honesty rules
All exclusions by criterion, none by outcome. Failed hypotheses are published. One technical
amendment round at pilot maximum, documented before confirmatory runs. Every number in any
resulting manuscript must regenerate from the code archive and pass a mechanical verifier
against the result files, as in our previous work.
