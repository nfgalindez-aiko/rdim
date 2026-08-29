# Sealed protocol — Exp48: the shape of the inverted-U's top (peak or plateau?)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The question
Exp45 (b9b4540) left one sharp anomaly: its peak-location criteria failed because the
observed top of R-dim's inverted-U looked like a FLAT PLATEAU across ρ = 1.0–1.3
(medians 6.14 / 5.34 / 5.99 with only 6 networks per point). Training networks had
peaked at 1.3. This protocol settles the top's shape with real power. No prediction is
being defended; this is a sealed ESTIMATION with pre-declared decision rules.

## 2. Design (frozen)
Grid ρ ∈ {0.95, 1.0, 1.05, 1.1, 1.15, 1.2, 1.3, 1.4} × 16 networks = 128 virgin
networks, seeds 8200 + i·16 + j. Per network: R-dim (rdim v0.1.0, frozen) on 120 trials
(rng(seed+50)), pulse nodes rng(seed+2), λ from lyapunov_esn (rng(seed+1), descriptive).
One run.

## 3. Pre-declared decision rules
Bootstrap over networks within each point (10,000 resamples, rng seed 424242):
- **T-pico:** some grid point's median exceeds all others' with bootstrap probability
  P(argmax) ≥ 0.95.
- **T-meseta:** the range of the point medians across the contiguous set
  {1.0, 1.05, 1.1, 1.15, 1.2, 1.3} is < 0.5 dimensions.
Cells: PICO (T-pico ✓); MESETA (T-pico ✗ and T-meseta ✓); INDETERMINADO (both ✗ —
reported with the bootstrap distribution of the argmax, and the additional networks per
point needed for 0.95 estimated descriptively). All three cells publishable.

## 4. Rules
One computation; no amendments after sealing. The outcome travels with the next firm
deposit and resolves (or formally defers) exp45's open anomaly.
