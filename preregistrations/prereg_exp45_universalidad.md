# Sealed protocol — Exp45: estimator-mechanics universality across the full inverted-U

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim
The exp44b linear theory (commit be89cd3, confirmed) established that R-dim follows from
[coherent signal spectrum + noise] through a universal averaging formula. This protocol
tests the strong extension to NONLINEAR networks across the full inverted-U (both
branches and the peak): with the coherent spectrum and the noise measured — not derived —
the same formula predicts R-dim:

    R_pred = κ · Σ_{k=1}^{30} S_k / (S_k + N_k),        κ = 0.68 (FROZEN from training)

- S_k: truth-scale coherent power of component k (n = 2000 cross-half amplitudes on the
  half-A SVD basis, total window power), with a per-component circular-shift null
  threshold (max of 20 shifts) — this measurement pipeline was validated on a known-truth
  bench (nulls 0.01–0.02; injected-spectrum recovery within 0.4; bench criteria and all
  three iterations documented in the code archive: CRITERIOS-45-BANCO.md, banco45*.py).
- N_k = T·σ̄²_k/60: trajectory noise power of the 60-trial average — per-time variance of
  evoked residuals (independent n = 120 set) projected on u_k, times the window length.
If this holds, the inverted-U is fully factorized: dynamics enter only through the
INPUTS (what chaos does to the coherent spectrum and the noise), never through the
formula — and the falling branch is the collapse of the coherent spectrum, quantified.

## 2. Disclosure and blindness
Fully disclosed (all in 03-experimentos/exp45_rama_descendente/ and the working document
02-apuestas/teoria-rama-descendente.md): the complete training history on the burned
exp36c networks (seeds 7000–7041), including two failed operationalizations (matched-
filter floor; a scale bug, both documented), the refuted stimulus-quenching hypothesis
(ν_sham/ν_evoked ≈ 1.0), the clean estimator nulls across the grid (rdim on sham
0.06–0.38 — the U is real), and the final training fit (Spearman +0.912, predicted peak
at ρ = 1.1 adjacent to the observed 1.3, κ fitted once = 0.68). Blindness: seeds 8000+ —
never touched by any experiment (reserved once for a protocol that died in training
without running). Smoke pilot: seed 7999, one network, outside the confirmatory set.

## 3. Design (frozen)
Grid ρ ∈ {0.3, 0.6, 0.9, 1.0, 1.1, 1.3, 1.6, 2.0} × 6 networks = 48 virgin tanh
networks, seeds 8000 + i·6 + j (make_W(ρ, rng(seed)); 8 pulse nodes from rng(seed+2)).
Per network, with the exp36c conventions: truth chunks from rng(seed+10..13) (4 × 500
trials), evoked residual set rng(seed+40) (120 trials), measured R-dim (rdim v0.1.0,
frozen) from rng(seed+50) (120 trials). One run of the whole grid.

## 4. Sealed tests (α = 0.05 where applicable)
- **A1 (order):** Spearman(R_pred, R-dim) over the 48 networks ≥ 0.80.
- **A2 (peak):** argmax over ρ of median R_pred within ±1 grid step of argmax of median
  R-dim.
- **A3 (values):** median |R_pred − R-dim| ≤ 1.5 dimensions (κ frozen; no refitting).
- **A4 (both branches):** median R_pred is unimodal with an interior maximum (not at
  ρ = 0.3 nor 2.0), rising before it and falling after it — and so is measured R-dim.

| Outcome | Reading |
|---|---|
| A1–A4 pass | The estimator mechanics are universal across the U: the inverted-U is [dynamics → coherent spectrum & noise] × [averaging formula]; the falling branch is the measured collapse of the coherent spectrum. Together with be89cd3 this closes the C3 mechanism at the phenomenological level. |
| A1✓ A2✗ | Order without peak: something at the peak still escapes the measured spectrum; reported as the sharpest open anomaly. |
| A1✓ A3✗ | κ is not transportable; the formula ranks but does not calibrate. |
| A1✗ | The training fit did not generalize; the universality claim dies on virgin ground and is reported dead. |
| A4✗ (predicted side) | The predictor fails to reproduce the U's shape on virgin networks; reported. |

## 5. Secondary (descriptive, no verdicts)
Capa B: ln(total coherent power) vs λ on the chaotic side (training showed −0.48,
p = 0.11, n = 12 — underpowered); the per-ρ curves of Σ S_k and median N_k (which input
drives each branch). These inform a future sealed protocol; nothing here claims them.

## 6. Rules
One computation of the sealed quantities; no amendments after sealing (training absorbed
all revision freedom, documented). Mechanical verifier before any number enters a draft.
The outcome travels with the next firm deposit, whichever cell it lands in.
