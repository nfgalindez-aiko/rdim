# Sealed protocol — Exp51b: the graded saturation law (saturation geometry decides where saturation governs)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim and its origin (disclosed)
Exp50b (01ad3ca, confirmed 7/7) established the saturation law in tanh networks. A
labeled training campaign (300 burned networks, three new activation families with
slope 1 at the origin; full history in DISENO-51.md) found the law is GRADED by
saturation geometry, and a universal-coordinate upgrade (mean |activity| as pooled
axis; a pooled crossover) did NOT materialize (also disclosed). Frozen per-family
predictions, from training numbers:
- **erf** (fast, smooth saturator): full tanh-like law (training −0.60/−0.77/−0.76/−0.70).
- **clip** (abrupt saturator): law present but WEAKER (training −0.57/−0.64/−0.46/−0.42).
- **soft** (slow, heavy-tailed saturator): saturation does NOT govern while unsaturated —
  no ρ effect in stable strata (training −0.14/−0.14 ns), λ has a real POSITIVE effect
  in the less-saturated half (training +0.515), and saturation captures the system only
  at edge/chaos strata (training −0.58/−0.72).
Reading if confirmed: fast saturators are saturation-governed everywhere; slow
saturators remain criticality-governed until saturation catches up — the geometry of
the ceiling decides which force rules.

## 2. Design (frozen)
Families and machinery exactly as exp51 training (comun51.py: φ_erf = erf(u·√π/2),
φ_clip = clip(u,−1,1), φ_soft = u/(1+|u|); generic twin-trajectory Lyapunov; rdim
v0.1.0 on 120 trials, rng(seed+50); pulse nodes rng(seed+2)). λ strata {(−0.05,−0.02],
(−0.02,−0.005], (−0.005,0.005], (0.005,0.05]}; ρ sampled per family from the frozen
ranges (erf U(0.9,4.0), clip U(0.9,2.5), soft U(1.1,4.0); ρ from rng(79000+seed)).
15 networks per stratum per family = 180 virgin networks. Scan bases (frozen):
erf 200000+, clip 210000+, soft 220000+ (caps +15000 each; under-filled strata
reported). One run.

## 3. Sealed tests (α = 0.05 where applicable; Spearman(ρ, R-dim) within stratum)
- **J1 (erf, full law):** all 4 strata ≤ −0.50 with p < 0.05.
- **J2 (clip, weak law):** all 4 strata negative with p < 0.05 (magnitude bar ≤ −0.30,
  pre-declared as the weaker-law family).
- **J3 (soft, the dissociation):** (a) both stable strata |Spearman| < 0.40; (b) both
  edge/chaos strata ≤ −0.45 with p < 0.05; (c) Spearman(λ, R-dim) among networks with
  ρ ≤ the family's accepted-median ≥ +0.30, one-sided p < 0.05.

| Outcome | Reading |
|---|---|
| J1✓ J2✓ J3✓ | The graded law stands: saturation geometry decides where saturation governs; the edge-of-chaos story is family-dependent in exactly the predicted pattern. |
| Partial | Each family's verdict reported on its own; the failures mark where training overfit. |
| All ✗ | The training maps did not generalize; reported dead. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome travels with the next firm
deposit (the C3-mechanics paper in preparation).
