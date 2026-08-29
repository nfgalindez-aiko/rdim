# Sealed protocol — Exp54b: the effective-gain theory (nonlinear networks as their gain-shrunk linear selves)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim and its origin (disclosed)
Linearizing a nonlinear network around its operating point gives δx_{t+1} =
diag(φ′(u))·W·δx_t. The unifying hypothesis: the EXACT linear theory of commit be89cd3,
applied to the effective system — W_eff = diag(g)·W with per-unit gains g_i = ⟨φ′(u_i)⟩
(measured from 10 deterministic trials, response window), effective pulse diag(g)·B·amp,
effective noise σ²·diag(g²) in the Lyapunov equation — predicts R-dim across activation
families with the SAME frozen κ = 0.378. This would unify the rising branch (g ≈ 1),
the saturation law (g shrinks), and the tail law (φ′_p decays faster with p), and
explain why saturation governs at matched λ: the heterogeneous diag(g) reshapes the
response geometry even at matched effective radius. Disclosed training on 996 burned
networks (7 families: tanh, erf, clip, φ_p for p ∈ {1,2,4,8}): pooled Spearman +0.634
(per family +0.44 to +0.74) for the diagonal theory; the SCALAR comparator (ḡ·W) is
crushed (+0.08 to +0.30, with degenerate constant predictions in some families).
Absolute calibration does NOT transfer (the linearization overpredicts levels): this
protocol therefore seals ORDER and COMPARATOR claims only; no value claim is made and
none may be added later.

## 2. Design (frozen)
7 families with their exp51/exp53 conventions and derivatives (tanh: 1−x²; erf:
e^(−πu²/4); clip: 1{|u|<1}; φ_p: (1+|u|^p)^(−(1+1/p))). Per family: 10 networks per λ
stratum ({(−0.05,−0.02], (−0.02,−0.005], (−0.005,0.005], (0.005,0.05]}) = 40, total
280 virgin networks. ρ sampling: tanh U(1.0,3.0); erf U(0.9,4.0); clip U(0.9,2.5);
φ_p U(0.9,3.5) — from rng(79000+seed). Scan bases (frozen): tanh 400000+, erf 410000+,
clip 420000+, p1 430000+, p2 440000+, p4 450000+, p8 460000+ (caps +30000; under-filled
strata reported → verdict marked underpowered). Per network: g from rng(seed+50) 10
trials; R_diag = linear theory on diag(g)W (κ = 0.378, K = 30); R_esc = same with
scalar ḡ; measured R-dim (rdim v0.1.0, 120 trials, rng(seed+50)). One run.

## 3. Sealed tests
- **N1 (order):** pooled Spearman(R_diag, R-dim) over the 280 networks ≥ 0.55, p < 0.05.
- **N2 (heterogeneity is the carrier):** pooled Spearman(R_diag, R-dim) − pooled
  Spearman(R_esc, R-dim) ≥ 0.25, where a degenerate (constant or undefined) scalar
  prediction pool counts as Spearman 0.

| Outcome | Reading |
|---|---|
| N1✓ N2✓ | The effective-gain theory stands as the unifying mechanism at the order level: nonlinear networks are, for reproducible dimensionality, their gain-shrunk linear selves — with per-unit gain heterogeneity as the essential carrier. Level calibration remains an open refinement. |
| N1✓ N2✗ | Order transfers but the scalar shortcut suffices; the heterogeneity story is dropped. |
| N1✗ | The linearization loses what matters; reported dead, per-family profile published. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome updates the C3-mechanics paper
before deposit.
