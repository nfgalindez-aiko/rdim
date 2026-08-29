# Sealed protocol — Exp53b: the tail of the nonlinearity decides where saturation takes over

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim and its origin (disclosed)
Exp52 (754ed78) confirmed the family-level saturation tendency and left open WHERE
saturation takes over in slow saturators (softsign shows no effect in its stable
strata). Hypothesis: the speed of the activation's tail decides. Parametric family
φ_p(u) = u/(1+|u|^p)^(1/p) (slope 1 at the origin for all p; p = 1 IS softsign; p → ∞
tends to hard clip). Metric: A_est(p) = median of the two stable-strata Spearman(ρ,
R-dim) values. Disclosed training (25 networks/stratum for p ∈ {2,4,8}, plus the burned
exp52 soft and clip data as anchors): A_est = −0.14 (p=1) → −0.36 (p=2) → −0.72 (p=4)
→ −0.74 (p=8), clip anchor −0.60 — the saturation-governed regime advances with tail
speed and saturates by p ≈ 4. Per the program's post-exp51 rule, only ONE coarse claim
is sealed; the full 4 × 4 profile is reported.

## 2. Design (frozen)
p ∈ {1, 2, 4, 8}; λ strata {(−0.05,−0.02], (−0.02,−0.005], (−0.005,0.005],
(0.005,0.05]}; ρ ~ U(0.9, 3.5) from rng(79000+seed) for all p (feasibility disclosed;
for p = 1 this range covers exp52's soft range); **30 networks per stratum** per p =
480 virgin networks, run fresh for all four p (the exp52 soft data is NOT recycled into
the verdict). Scan bases (frozen): p=1 → 300000+, p=2 → 310000+, p=4 → 320000+,
p=8 → 330000+ (caps +30000; under-filled strata reported, verdict then marked
underpowered). R-dim (rdim v0.1.0) on 120 trials (rng(seed+50)); pulse nodes
rng(seed+2); Lyapunov by twin trajectories (rng(seed+1)). One run.

## 3. Sealed test
- **M1 (the tail law):** A_est(p=8) − A_est(p=1) ≤ −0.30.

| Outcome | Reading |
|---|---|
| M1✓ | The tail decides: fast tails hand the stable regime to saturation; slow tails keep it criticality-free. Together with 01ad3ca/754ed78, the saturation account gains its WHERE. |
| M1✗ | The training profile did not generalize; reported dead, profile published. |

## 4. Rules
One computation of the sealed quantity; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome updates §8 of the C3-mechanics
paper before deposit.
