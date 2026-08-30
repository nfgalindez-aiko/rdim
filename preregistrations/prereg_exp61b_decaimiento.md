# Sealed protocol — Exp61b: the quantitative law of chaotic decay of coherent time

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any confirmatory
network was generated.

## 1. Origin (disclosed)
The duration law (83ae4da) left its chaotic clause failed: direction significant
(Spearman −0.41, p = 0.039) but under the −0.50 bar, on a compressed λ range. Training
on 69 burned chaotic networks (exp46/exp49 archives; λ 0.011–0.217) gives Spearman
−0.529 (p = 3 × 10⁻⁶) and an ln–ln slope of **−0.588** — challenging the naive
derivation T_c ≈ ln(A/σ)/λ, whose exponent is −1. The empirical law to seal is
T_c ∝ λ^(−0.6); the derived −1 is carried as a contrast prediction. Target reliability
(rule #2): T_c split-half across independent truth sets = +0.976 on 10 burned nets.
Extended-range feasibility: ρ ~ U(2.5, 4.0) yields λ up to 0.26 (73% above 0.15).

## 2. Design (frozen)
Home family (tanh, N = 64, noise 0.05). Four λ strata {(0.01, 0.03], (0.03, 0.08],
(0.08, 0.15], (0.15, 0.30]} × 15 = 60 virgin networks; ρ ~ U(1.0, 4.0) rng(79000+seed);
λ by twin trajectories rng(seed+1); pulse rng(seed+2). T_c per network by the frozen
exp46 operationalization (truth n = 2000 in 4 chunks rng(seed+10..13); cross-half
instantaneous coherent power, 80% cumulative time). Scan seeds 820000…, cap 860000;
under-filled strata reported → underpowered. One run.

## 3. Sealed tests
- **D1 (magnitude):** Spearman(λ, T_c) ≤ −0.50 over the 60 networks, p < 0.05.
- **D2 (form):** OLS slope of ln T_c on ln λ within [−0.94, −0.24] (trained −0.588
  ± 0.35). The derived exponent −1 lies OUTSIDE this interval's center; whether the
  confirmatory slope's 95% CI excludes −1 is reported (not a sealed criterion).

| Outcome | Reading |
|---|---|
| D1✓ D2✓ | The chaotic decay of coherent time is law: T_c falls as a sublinear power of λ (≈ λ^−0.6). The duration law (83ae4da) gains its missing clause; the naive divergence derivation is quantitatively wrong and says so. |
| D1✓ D2✗ | Decay confirmed, form unstable; reported. |
| D1✗ | The training pool overfit; reported dead. |

## 4. Rules
One computation; no amendments after sealing. Mechanical verifier before any number
enters a draft. The outcome travels with the next firm deposit.
