# Sealed protocol — Exp37: Shadow or substance? Reproducible dimensionality in spiking populations vs the EEG field, same brain, same trials

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any spike time from this
dataset was read. Knowledge at sealing: metadata only (units-table sizes, quality columns,
probe/area labels — scouting map archived in the project), plus everything already published
from the EEG arm (preprint 6: per-animal R-dim values and matched-trial selections; those are
public and reused verbatim as the comparison target).

## 1. The question
When perturbational complexity is measured from field potentials, is it measuring the
reproducible richness of the underlying neuronal population activity, or a field-specific
shadow? DANDI 000458 records both simultaneously: 30-channel epidural EEG (analyzed in
preprint 6) and Neuropixels single units, same animals, same stimulation trials, awake and
under isoflurane. To our knowledge, reproducible dimensionality has never been compared
across these two levels of description within the same brains and trials.

## 2. Instrument (frozen)
R-dim exactly as released (rdim v0.1.0; no parameter tunable here). Spiking input: units'
spike trains binned at 10 ms over the same epochs as preprint 6 (−0.6 to +0.6 s; artifact
blanking [−2, +10] ms zeroed), forming (trials × units × bins); baseline (−0.4, −0.05) s,
response (+0.01, +0.5) s; same per-animal seeds. Unit inclusion: the dataset's own quality
annotation if present (its default-pass category), else all sorted units; sessions with
fewer than 30 included units are excluded (technical tier, set from the scouting map before
any spike was read). Trials: EXACTLY the matched sets of preprint 6 (state- and
current-matched, first-120 per state), regenerated with the same frozen pipeline and seeds.

## 2b. AMENDMENT A1 (sealed immediately after the base protocol, BEFORE any spike was read)
The base commit was sealed with two placeholders left unfilled by an editing error, fixed
here with the archived scouting map (still metadata only; no spike time has been read):
- **Pilot session:** sub-521885 is impossible as pilot (its session carries ZERO sorted
  units — it is EEG-only). Pilot is **sub-546655** (265 units), chosen by criterion: the
  units-bearing session with fewest units among those OUTSIDE the confirmatory tier (its
  matched N was below preprint 6's H1 threshold), so the shakeout cannot touch the
  confirmatory sample.
- **Tier numbers:** 18 sessions carry >= 30 sorted units (265-995); **16 of them (15 unique
  animals)** also belong to preprint 6's H1 tier (matched N >= 120) and form the
  confirmatory sample; for the animal with two sessions, the session already selected by
  preprint 6's one-session-per-animal rule is used. If fewer than 8 animals survive
  processing, all analyses become descriptive.

## 3. Confirmatory hypotheses (α = 0.05 each; matrix fixes joint reading)
- **Q1 (correspondence of levels):** across animals, awake R-dim_spikes correlates with the
  published awake R-dim_EEG: Spearman ≥ 0.5, one-sided p < 0.05.
- **Q2 (state contrast at the neuronal level):** R-dim_spikes(awake) > R-dim_spikes(iso) at
  the matched 120 trials, one-sided Wilcoxon.
- **Q3 (the shadow question — within-animal effect coupling):** per-animal state effect
  Δ_spikes = R-dim_spikes(awake) − R-dim_spikes(iso) correlates with the published Δ_EEG:
  Spearman ≥ 0.5, one-sided p < 0.05.

## 4. Interpretation matrix (sealed)
| Q1 | Q2 | Q3 | Reading |
|---|---|---|---|
| ✓ | ✓ | ✓ | Substance: the field measure tracks neuronal reproducible dimensionality in level, state, and within-animal effect. Strongest possible grounding for field-based complexity. |
| ✓ | ✓ | ✗ | Both levels are rich and state-sensitive, but effects decouple within animal: the field adds/loses information relative to spikes. Important dissociation, reported as such. |
| ✗ | ✓ | — | The state contrast exists at both levels but their magnitudes do not correspond: field complexity is not a proxy for population dimensionality. Uncomfortable and important. |
| — | ✗ | — | The neuronal population does not show the state contrast under the debiased estimator at matched trials: the EEG effect lacks a spiking counterpart here. Most uncomfortable cell; published as is. |

## 5. Secondary (descriptive, no claims)
Growth curves R-dim_spikes(n) per state on the preprint-6 grid; unit-count vs level
(coverage analog); per-area breakdowns where probe labels allow; bin-size sensitivities
(5 ms, 25 ms) — verdicts claimed only if Q-verdicts are unchanged under both.

## 6. Rules
Pilot animal sub-521885 for technical shakeout only (excluded from confirmatory tests);
one round of technical amendments at pilot maximum, publicly documented before confirmatory
runs. All exclusions by criterion, none by outcome. Failures published. Every quoted number
must pass a mechanical verifier against result files before entering any draft.
