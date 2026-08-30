# Sealed protocol — Exp56b: the virgin-subject level prediction, with attrition-corrected inclusion

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit. Blind quantities (rd60 and
R_pred60 of the subjects below) have never been computed.

## 1. Why a second seal (full disclosure)
Exp56 (d2a0647) landed in its pre-declared underpowered cell: only 2 of 26 virgin
subjects passed the frozen ≥120-valid-trials inclusion — because the virgin pool is,
by construction, the pool that FAILED that very bar when the exp31 cohort was filled
in ID order (twelve subjects sit at 112–119 valid trials). Recorded as method rule #3:
when sealing on leftover subjects, first check why they are left over. What was
observed before this seal: ONLY the valid-trial counts and error types of the 26, plus
the two quantities of the 2 subjects that passed (sub-030, sub-040 — hereby BURNED and
excluded from this protocol). No other subject's rd60 or spectrum has been touched.

## 2. Design (frozen)
Subjects: the exp56 list minus the burned two and the structurally absent two
(sub-031, sub-072: no prefrontal acquisition on OpenNeuro): 22 candidates. Pipeline:
byte-identical to exp56/d2a0647 in every step; the ONLY amendment is inclusion,
**≥ 100 valid trials** (rd60 needs 60; spectra use halves m₀ = n//2 ≥ 50 — both
comfortably inside the certified regime). Subjects whose loading fails inside the
frozen pipeline (e.g., non-unique event samples, which the frozen code does not
handle) are excluded and reported, as before. rd60: pci_xv_trials(first 60 valid,
seed = 0). R_pred(60): certified exp55 pipeline unchanged. One run.

## 3. Sealed test (identical bar to d2a0647)
- **Q1:** Spearman(R_pred60, rd60) over included, gated subjects ≥ 0.45, one-sided
  p < 0.05, requiring n ≥ 12 (fewer ⇒ underpowered; the candidate pool caps at ~17
  loadable, disclosed).

| Outcome | Reading |
|---|---|
| Q1✓ | First sealed real-data validation of the estimator mechanics on never-analyzed humans. |
| Q1✗ | The exploratory bridge did not generalize; reported dead with the full scatter. |

## 4. Rules
One computation; no amendments after sealing. Mechanical verifier before any number
enters a draft. The outcome travels with the next firm deposit, together with the
exp55/exp56 chain that produced it.
