# Sealed protocol — Exp57b: attacking our own laws (size, biological wiring, noise)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The question
The saturation law (01ad3ca, 754ed78) and the effective-gain theory (8bf6f60) are
confirmed in their home family: N = 64, sparse random wiring (density 0.1), noise 0.05,
tanh. If they are laws of systems rather than of the toy, they must survive the axes
never varied. Five variants (tanh throughout — the nonlinearity axis was already
attacked in exp51/52): **N128** and **N256** (size ×2, ×4); **dale** (80/20 E/I wiring,
inhibitory balance ×−4, the frozen exp13 constructor); **ruido02** and **ruido10**
(noise 0.02 and 0.10). Disclosed feasibility (registered in DISENO-57.md before this
seal): λ-strata yields per variant; ρ sampling U(0.85, 2.2) for N128/N256, U(1.0, 3.0)
otherwise; a by-product worth recording — Dale-wired networks sit naturally at the edge
(median λ = −0.014).

## 2. Design (frozen)
Per variant: λ strata {(−0.05,−0.02], (−0.02,−0.005], (−0.005,0.005], (0.005,0.05]}
by measured λ (twin-trajectory, rng(seed+1)); 30 networks per stratum = 120; scan bases
650000 (N128), 660000 (N256), 670000 (dale), 680000 (ruido02), 690000 (ruido10), caps
+30000, ρ from rng(79000+seed); pulse = 8 nodes rng(seed+2), amp 2.0. Per network:
R-dim (rdim v0.1.0, 120 trials, rng(seed+50)); effective gains g_i = ⟨1−x²⟩ (10 trials,
rng(seed+50), response window); R_diag and R_esc by the frozen 8bf6f60 machinery
(κ = 0.378, K = 30) on diag(g)·W and ḡ·W. One run of all five variants. Under-filled
strata reported → that variant's verdicts marked underpowered.

## 3. Sealed tests (per variant; bars identical to the confirmed laws)
- **S1 (saturation):** median of the 4 per-stratum Spearman(ρ, R-dim) ≤ −0.35.
- **S2 (effective theory, order):** pooled Spearman(R_diag, R-dim) ≥ 0.55, p < 0.05.
- **S3 (heterogeneity carrier):** pooled order(diag) − order(scalar) ≥ 0.25
  (degenerate scalar counts as 0).

| Outcome | Reading |
|---|---|
| A variant passes S1–S3 | The laws hold in that world; each survival retroactively strengthens the whole edifice (consilience). |
| A variant fails some | The failing claim's scope boundary is drawn there and reported — the laws are of-the-family on that axis. |
| Broad failure | The home-family results stand as written (their scope was always declared) and the generality program is reported honestly. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing (feasibility
absorbed the design freedom, registered). Mechanical verifier before any number enters
a draft. The outcome travels with the next firm deposit (C3-mechanics paper).
