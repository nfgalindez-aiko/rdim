# Sealed protocol — Exp41: Does anesthesia rotate the neuronal response repertoire?

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any between-state subspace
overlap was computed.

## 1. The question exp40 left open
The uniform-gain account failed at the neuronal level (protocol 76f2fea): observed drops in
spiking R-dim exceed gain-predicted drops by a median factor of 3, with inverted ordering.
Something structural, not multiplicative, happens to the population response. Candidate with
a direct geometric measurement: **repertoire rotation** — anesthesia does not merely shrink
the response carried by a fixed set of population patterns; it changes *which* patterns
carry the response.

## 2. Disclosure and blindness
Known at sealing: everything published/archived from exp37–40, including each animal's
observed displacement D_obs and gain-predicted D_pred (exp40 archive). NEVER computed — the
blindness — are the between-state and within-state subspace overlaps defined below.

## 3. Operational definitions (frozen)
Animals: the 15 exp37 confirmatory animals; trials: exactly the matched 120 per state
(preprints 6–7 pipeline and seeds); binned population responses (10 ms) as preprint 7.
- **Response subspace per state:** trial-average the (trials × units × bins) tensor,
  baseline-correct per unit, SVD over (units × response-window bins); take the top K = 5
  left singular vectors (unit space: which neurons carry the response).
- **Between-state overlap:** O_state = ||U_awakeᵀ U_iso||_F² / K  (mean cos² of principal
  angles; 1 = same subspace, 0 = orthogonal).
- **Within-state control:** split the 120 awake trials into halves (60/60, same split seed
  family as rdim), compute each half's top-5 subspace, O_control = their overlap. (Halved
  trial counts make this control noisier, biasing O_control DOWN — conservative for S1.)
- **Residual to explain:** resid = D_obs − D_pred per animal, from the exp40 archive
  (n = 14 after its preregistered exclusion).

## 4. Sealed tests (α = 0.05 each)
- **S1 (rotation exists):** O_state < O_control across animals, one-sided paired Wilcoxon.
- **S2 (rotation explains the excess):** Spearman(1 − O_state, resid) ≥ 0.5, one-sided
  p < 0.05, over the exp40 animals.

| S1 | S2 | Reading |
|---|---|---|
| ✓ | ✓ | Anesthesia rotates the response repertoire, and the rotation scales the excess drop the gain account missed: the structural mechanism is (at least in part) subspace reorganization. |
| ✓ | ✗ | Rotation is real but does not scale the excess: reorganization exists yet the missing mechanism lies elsewhere (e.g., per-component decoherence — separate protocol). |
| ✗ | — | The repertoire does not detectably rotate: attenuation acts within a preserved population structure, and the excess must come from within-component changes. Reported as is. |

## 5. Secondary (descriptive)
Time-space overlaps (same computation on right singular vectors); overlap vs the animal's
state effect at each level; overlap for the reversed animals specifically; K = 3 and K = 10
as sensitivity (verdicts claimed only if unchanged).

## 6. Rules
Pilot sub-546655 (outside tier) for shakeout; one technical-amendment round maximum,
documented before confirmatory runs. One computation of the sealed quantities. The outcome
travels in the next firm deposit whichever cell it lands in. Mechanical verifier before any
number enters a draft.
