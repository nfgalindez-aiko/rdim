# Sealed protocol — Exp36c: decomposing the edge-of-chaos inverted-U into richness and coherence

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any confirmatory network
(virgin seeds 7000+) was simulated or measured.

## Context and disclosure
Constraint C3 (constraints paper): debiased reproducible dimensionality (R-dim) is an
inverted-U in the maximal Lyapunov exponent. Two attempts to explain it died: the amplitude-
spectrum account (exp35, sealed, dead) and two counting instruments (exp36a/36b-val:
accurate away from criticality, but counting is structurally leakage-fragile — a component
split across rotated basis vectors is counted multiply; summing is leakage-robust, which is
what R-dim already does). Exploratory data (seeds 5000+, disclosed): top-component coherence
appears high on the ordered side, peaks near the edge, and collapses monotonically into
chaos, while R-dim rises steeply on the ordered side with roughly flat coherence.
**Hypothesis H-dec:** the U decomposes mechanistically — the RISE (order → edge) is carried
by growing richness (more components) at roughly constant coherence; the FALL (edge → chaos)
is carried by coherence collapse.

## Design (frozen)
Networks: standard family (N=64), ρ ∈ {0.6, 0.9, 1.0, 1.1, 1.3, 1.6, 2.0}, 6 nets/ρ,
**virgin seeds 7000+** (never used in any exploration or validation). Per network:
λ_max (project-standard estimator); trial set C1 (n=120, pulse) → per-component split-half
coherences coh_k (SVD basis on half-A average, normalized cross-correlation with half-B
projection), summarizing **coh5 = mean of the top-5 coh_k**; independent trial set C2
(n=120, different seed) → R-dim with the frozen project estimator. The peak group is the
ρ group with maximal median R-dim (determined from these data; predictions below are
relative to it).

## Sealed criteria (single run, single evaluation)
- **G1 (coherence collapse past the edge):** median coh5 per group is non-increasing from
  the peak group toward ρ=2.0; chaos-end median coh5 < 0.3; peak-group median coh5 ≥ 0.6.
- **G2 (order-side dissociation):** from ρ=0.6 to the peak group, median R-dim increases by
  ≥ 1.5 while median coh5 increases by < 0.15 — the rise is not coherence-driven.
- **G3 (chaos-side coupling):** across individual nets with ρ ≥ peak group,
  Spearman(coh5, R-dim) ≥ 0.5, p < 0.01 — the fall is coherence-coupled.

| G1 | G2 | G3 | Reading |
|---|---|---|---|
| ✓ | ✓ | ✓ | H-dec confirmed: the U = richness growth × coherence collapse; C3 mechanistically decomposed with validated instruments only. |
| ✓ | ✗ | ✓ | Coherence carries both sides; richness dissociation not established. Partial. |
| ✗ | — | — | H-dec dead in its sealed form. Reported. |
| ✓ | any | ✗ | Collapse exists but does not couple to the measure net-by-net. Reported. |

## Rules
Zero revisions after sealing. The outcome travels inside the next firm deposit, whichever
cell it lands in. Mechanical verifier required before any number is quoted in a draft.
