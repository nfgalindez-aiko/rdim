# Sealed protocol — Exp52: does the saturation tendency generalize? (family-level, properly powered)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. Origin and the rule this protocol obeys (disclosed)
Exp51b (387f305) sealed stratum-level predictions learned from n = 25 cells and tested
them at n = 15: it died 0/3, teaching the recorded rule that the grain of a sealed claim
must be coarser than the training noise. ALL prior data on the three families is burned
and disclosed (training maps n = 25/stratum; the dead confirmatory n = 15/stratum).
Combined, the family-level aggregate — the MEDIAN of the four per-stratum Spearman(ρ,
R-dim) values — was: erf −0.73 (training) / −0.58 (51b); clip −0.51 / −0.47; soft
−0.36 / −0.67. This protocol seals only that coarse aggregate, at proper power.

## 2. Design (frozen)
Families, machinery, λ strata, and ρ sampling ranges exactly as exp51b (comun51.py;
strata {(−0.05,−0.02], (−0.02,−0.005], (−0.005,0.005], (0.005,0.05]}; erf U(0.9,4.0),
clip U(0.9,2.5), soft U(1.1,4.0); ρ from rng(79000+seed)). **30 networks per stratum**
per family = 360 virgin networks. Scan bases (frozen): erf 230000+, clip 240000+, soft
250000+ (caps +30000 each; under-filled strata reported and that family's verdict then
marked underpowered — an uncomfortable cell we accept). R-dim (rdim v0.1.0) on 120
trials (rng(seed+50)); one run.

## 3. Sealed tests (one per family)
- **K1 (erf), K2 (clip), K3 (soft):** the median of the four per-stratum Spearman(ρ,
  R-dim) values ≤ −0.35, with the per-stratum values reported in full.

| Outcome | Reading |
|---|---|
| K1✓ K2✓ K3✓ | The saturation tendency generalizes across ceiling geometries at the family level: saturation hurts reproducible dimensionality whatever the shape of the ceiling. Stratum-level structure remains explicitly unresolved. |
| Partial | Per-family verdicts stand alone; a family that fails marks a real boundary of the law. |
| 0/3 | Even the coarse tendency does not generalize; the tanh law stays family-specific. |

## 4. Rules
One computation of the sealed quantities; no amendments after sealing. Mechanical
verifier before any number enters a draft. The outcome updates §6/§8 of the
C3-mechanics paper before deposit.
