# Sealed protocol — Exp50b: the saturation law (at matched λ, saturation — not criticality — governs complexity)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim and its origin (disclosed)
A labeled exploratory 2D map (156 burned networks, seeds 92000–93398, cells = ρ-band ×
measured-λ stratum, 12 per cell) showed: within EVERY λ stratum, R-dim falls steeply
with ρ (Spearman −0.58 / −0.75 / −0.80 / −0.84, all p < 0.001; medians ~6.5 → ~2 from
ρ ∈ (1.0,1.5] to (2.2,3.0]), while within every ρ band λ shows no detectable effect
(−0.09 / −0.21 / −0.22, all ns). Declared law: **in ρ ∈ (1.0, 3.0], at matched λ,
saturation depth — not criticality — governs reproducible dimensionality**; combined
with the sealed exp49-F3 dissociation (coherent duration peaks at the edge in λ), the
picture is: TIME belongs to criticality, RICHNESS to (freedom from) saturation. This
reframes the falling branch of C3's inverted-U as largely saturation wearing chaos's
clothes (ρ and λ were entangled in every previous grid).

## 2. Design (frozen)
Cells: ρ bands {(1.0,1.5], (1.5,2.2], (2.2,3.0]} × measured-λ strata {(−0.05,−0.02],
(−0.02,−0.005], (−0.005,0.005], (0.005,0.05]} = 12 cells × 12 networks = 144 virgin
networks (the (0.6,1.0] band is omitted: only one feasible stratum, no within-band λ
range). Adaptive scan exactly as the training map (band drawn uniformly among not-full
bands from rng(78000+seed), ρ uniform in band, W = make_W(ρ, rng(seed)), λ from
lyapunov_esn(rng(seed+1)), first-come acceptance), scanning seeds s = 95000, 95001, …
(cap 135000). Per accepted network: R-dim (rdim v0.1.0) on 120 trials (rng(seed+50),
pulse nodes rng(seed+2)). One run.

## 3. Sealed tests
- **G1 (saturation law):** within EACH of the 4 λ strata, Spearman(ρ, R-dim) ≤ −0.50
  with p < 0.05 (n = 36 per stratum).
- **G2 (λ bounded):** within EACH of the 3 ρ bands, |Spearman(λ, R-dim)| < 0.30
  (n = 48 per band). (An equivalence-style bound: λ's effect is at most weak where
  saturation's is strong; we cannot prove zero and do not claim it.)

| Outcome | Reading |
|---|---|
| G1✓ G2✓ | The saturation law stands: in this region complexity is governed by saturation at matched criticality, and criticality adds at most a weak effect. C3's falling branch is to be re-read accordingly. |
| G1✓ G2✗ | Saturation dominates but λ retains a real secondary effect; both reported with sizes. |
| G1✗ | The training map did not generalize; the law dies on virgin ground and is reported dead. |

## 4. Secondary (descriptive, no verdicts)
Median map of the 12 cells; comparison with the training map; Spearman(ρ, R-dim)
pooled; the (0.6,1.0] stable cell re-measured (12 nets) for the rising-branch anchor.

## 5. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome travels with the next firm
deposit (the C3-mechanics paper in preparation).
