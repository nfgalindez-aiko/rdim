# Sealed protocol — Exp44b: an exact linear theory of R-dim, confirmed on virgin networks

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim
For linear networks x_t = W·x_{t−1} + noise + pulse, R-dim is predicted in closed form
from the connectivity matrix alone. Signal and noise separate exactly: the evoked
response is the deterministic impulse trajectory D = [W·Bp, W²·Bp, …] (window-centered),
its SVD gives component amplitudes s_k and patterns (u_k, v_k); the noise floor per
component is ν_k² = v_cᵀ·Toeplitz(g)·v_c / m with g(τ) = u_kᵀWᵗΣu_k and Σ the stationary
Lyapunov covariance (Σ = WΣWᵀ + σ²I); each component's split-half correlation is
r_k = s_k²/(s_k² + ν_k²), and

    R_theory(n) = κ · Σ_{k=1}^{64} r_k(m = n/2),    κ = 0.378 (FROZEN)

κ is a single global constant absorbing the estimator's selection/clipping machinery,
fitted once on the exploration set and frozen here.

## 2. Disclosure and blindness
Fully disclosed: the exploration set (seeds 9000–9023, 24 networks, ρ ∈ {0.3…0.99}),
where the functional form was derived, κ was fitted at n = 120, and the n-axis was
checked (per-n Spearman 0.945–0.985; increment Spearman +0.686). Blindness: seeds
9100+ — no network, trial or quantity has ever been generated from them. Exploration
files: 03-experimentos/exp44_teoria_lineal/ (exp44.py, variantes44.py, explor44_n.py,
results). Smoke pilot: seed 9095 (one network, outside the confirmatory set).

## 3. Design (frozen)
Grid ρ ∈ {0.3, 0.6, 0.8, 0.9, 0.95, 0.99} × 6 networks = 36 virgin networks, seeds
9100 + i·6 + j (W and pulse nodes exactly as the exploration pipeline: make_W(ρ, rng(seed)),
8 pulse nodes from rng(seed+2)). Per network: R_theory(n) from W alone; measured R-dim
(rdim v0.1.0, frozen) on 240 linear trials (rng(seed+50)), evaluated on the first
n ∈ {30, 60, 120, 240}. One run of the whole grid.

## 4. Sealed tests (α = 0.05 where applicable)
- **L1 (order):** Spearman(R_theory, R-dim) at n = 120 over the 36 networks ≥ 0.90.
- **L2 (values):** median |R_theory − R-dim| at n = 120 ≤ 1.0 dimensions (κ frozen; no
  refitting).
- **L3 (mechanism):** Spearman over networks of predicted vs observed growth increments
  Δ = R(240) − R(60) ≥ 0.50, one-sided p < 0.05.
- **L4 (shape):** the median measured R-dim at n = 120 is maximal at ρ = 0.99 (no
  interior peak in the stable linear family) — and so is the theory's.

| Outcome | Reading |
|---|---|
| L1–L4 all pass | First exact theory slice of the program: in the linear world R-dim is computable from connectivity, the trial-scaling mechanism is averaging-against-a-floor, and the U's falling branch is NOT a linear phenomenon — it belongs to nonlinearity/chaos. |
| L1✓ L2✗ | The theory ranks but does not calibrate: κ is not a constant across families; reported as such. |
| L1✓ L3✗ | Levels predicted, growth mechanism not established at per-network resolution. |
| L1✗ | The exploration fit was overfitted to its 24 networks; the theory dies on virgin ground and is reported dead. |
| L4✗ | An interior peak exists in the linear family — the U would NOT need nonlinearity; this would refute our partition claim and be reported prominently. |

## 5. Rules
One computation of the sealed quantities; no amendments after sealing (exploration
absorbed all revision freedom). Mechanical verifier before any number enters a draft.
The outcome travels with the next firm deposit, whichever cell it lands in.
