# Sealed protocol — Exp59b: is there a peak in λ at controlled saturation? (the U's top, settled by two axes)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any confirmatory
network was generated (feasibility used only seeds 700000-700399, disclosed: no R-dim
was computed on any of them).

## 1. The question
C3 says complexity peaks at the edge of chaos. The saturation law (01ad3ca, 7ca2e18)
showed that one-knob grids confound criticality with saturation — the observed "peak"
could be a mixture artifact. This protocol scans λ FINELY across the edge at
CONTROLLED saturation: does R-dim show a peak in λ, or is it flat once saturation is
held? If flat, C3's peak re-reads as a property of the one-knob trajectory rather than
of the edge itself — a major conceptual revision. If peaked, the edge keeps its crown
with confounds controlled. Both cells are publishable.

## 2. Design (frozen)
Home family (tanh, N = 64, noise 0.05, sparse W density 0.1). Acceptance by TWO
measured coordinates: saturation slice g_med = ⟨1−x²⟩ ∈ (0.75, 0.85] measured on a
SEPARATE 10-trial stream (rng(seed+60) — never the rdim stream, so acceptance cannot
select on outcome data); λ (twin-trajectory, rng(seed+1)) into six fine strata
{(−0.020,−0.012], (−0.012,−0.006], (−0.006,−0.002], (−0.002,+0.002], (+0.002,+0.008],
(+0.008,+0.020]}. 30 networks per stratum = 180. ρ ~ U(0.9, 1.8) from rng(79000+seed);
pulse 8 nodes rng(seed+2); R-dim (rdim v0.1.0) on 120 trials rng(seed+50). Scan seeds
700400 …, cap 740000; under-filled strata reported → verdict marked underpowered.
One run. Bootstrap 10,000, rng 595959.

## 3. Sealed dual decision rules
- **C-pico:** some stratum's median R-dim exceeds BOTH end strata's medians by ≥ 0.8
  dimensions, with bootstrap P(that stratum is the argmax) ≥ 0.90.
- **C-plano:** the range of the six stratum medians < 0.8 AND no stratum holds
  bootstrap P(argmax) ≥ 0.80.
- Neither: INDETERMINADO, reported with the full bootstrap distribution and a
  descriptive estimate of the added power required.

| Outcome | Reading |
|---|---|
| C-pico | The edge keeps its crown: a genuine λ-peak survives saturation control. |
| C-plano | At fixed saturation the edge confers no R-dim advantage: C3's inverted-U re-reads as the signature of a one-knob trajectory through the (criticality × saturation) plane. |
| Indeterminado | Formally deferred, with the map published. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome travels with the next firm
deposit (paper 8 v2 or its successor).
