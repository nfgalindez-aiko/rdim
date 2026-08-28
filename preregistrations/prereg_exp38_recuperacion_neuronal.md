# Sealed protocol — Exp38: Does the neuronal population recover where the field did not?

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any recovery-block spike
time was read. Disclosure: the field-level (EEG) recovery results are published (preprint 6:
recovery did NOT restore field R-dim in an adequately powered test, +0.18 observed vs +0.60
expected) and the awake/iso spiking values are computed (preprint 7 archive). The one thing
never computed — where this test's blindness lives — is spiking R-dim in the RECOVERY blocks.

## 1. The question
Preprint 6's reversibility failure is the program's standing barrier to claiming that R-dim
tracks the state rather than merely associating with it. Two readings could not be separated
there: (a) recovery is genuinely incomplete in the recorded window (biology), or (b) the
field level recovers poorly even though the neurons recover (measurement level). The
simultaneous Neuropixels recordings decide between them.

## 2. Design (frozen; instruments identical to preprints 6–7)
Sessions: the exp37 confirmatory animals whose sessions contain recovery blocks with matched
(recovery, isoflurane) N ≥ 120 under the frozen pipeline-34 matching (state- and
current-matched, first-120, same seeds). From the archived metadata, 8 tier animals carry
recovery blocks (551397, 551399, 569062, 569064, 569068, 569069, 569073, 575102); if fewer
than 6 survive processing, all analyses become descriptive. Pilot: sub-546655 (recovery
present, outside the tier), technical shakeout only. Spiking R-dim: 10 ms bins, identical
epochs/windows/blanking/estimator/seeds as preprint 7.

## 3. Sealed hypotheses (α = 0.05 each)
- **R1 (neuronal recovery exists):** R-dim_spikes(recovery) > R-dim_spikes(iso) at the
  matched 120 trials; one-sided Wilcoxon.
- **R2 (levels compared):** define per level the recovery fraction
  F = (R(recovery) − R(iso)) / (R(awake) − R(iso)), each level using its own rd120 values
  (spiking awake/iso from preprint 7's archive; EEG values recomputed from preprint 6's
  frozen pipeline on the same session). F is computed only for animals with
  (awake − iso) > 0.5 at BOTH levels (fraction otherwise unstable; count reported; if fewer
  than 6 remain, R2 is descriptive). Test: F_spikes > F_EEG, one-sided paired Wilcoxon.

## 4. Interpretation matrix (sealed)
| R1 | R2 | Reading |
|---|---|---|
| ✓ | ✓ | Neurons recover more than the field: preprint 6's reversibility failure is at least partly a field-level limitation; reversibility is rescued at the neuronal level. |
| ✓ | ✗ | Both levels recover partially and comparably: recovery is genuinely incomplete in the recorded window — biology, not measurement; the honest limitation stands but is now characterized. |
| ✗ | — | Neuronal dimensionality does not recover in the window either: the failure is biology; the measure is detecting genuinely slow recovery of reproducible dimensionality after anesthesia. Published as is. |

## 5. Secondary (descriptive)
Recovery-block spontaneous population rate vs awake (arousal check, as in the exp37
depth proxies); recovery growth curves on the preprint-6 grid; per-animal F values tabled.

## 6. Rules
One technical-amendment round at pilot maximum, documented before confirmatory runs. All
exclusions by criterion. Failures published. Mechanical verifier before any number enters
a draft.
