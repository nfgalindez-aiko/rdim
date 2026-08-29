# Sealed protocol — Exp46: the coherent-response duration law (T_c ~ 1/|λ|, maximal at the edge)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any network with the
confirmatory seeds was generated.

## 1. The claim
The duration of the stimulus-locked (coherent) response is governed by the maximal
Lyapunov exponent on BOTH sides of the edge of chaos: on the stable side relaxation sets
it (T_c ~ 1/|λ|); on the chaotic side trial-to-trial divergence truncates it (T_c falls
as λ grows); therefore **T_c is maximal at the edge**. Corollary for C3: the edge is
where the system has the most coherent time in which to unfold distinguishable response
components (and the falling branch of the inverted-U begins where decoherence shortens
that time). Training on 90 burned networks: stable-side law Spearman +0.917 (p=3.3e-25,
n=61); median T_c across ρ = 1/2/4/10/166.5/96/58/37.5 (edge ~17× its neighbors). The
chaotic-side QUANTITATIVE law (T_c ∝ 1/λ, P ∝ 1/λ) did NOT establish in training
(compressed λ range, n=17) — only the DIRECTION is sealed here, on an extended λ range.

## 2. Operational definitions (frozen)
Per network: coherent instantaneous power e(t) = ⟨evA(·,t), evB(·,t)⟩ clipped at 0, from
truth-scale half-averages (n = 2000, 4 chunks, exactly the exp45 conventions, window-
centered); **T_c** = post-stimulus sample at which cumulative e reaches 80% of its total;
λ from lyapunov_esn(W, rng(seed+1)). Networks: make_W(ρ, rng(seed)), 8 pulse nodes from
rng(seed+2), truth chunks rng(seed+10..13).

## 3. Design (frozen)
Grid ρ ∈ {0.3, 0.5, 0.7, 0.9, 0.95, 1.05, 1.1, 1.2, 1.4, 1.7, 2.0, 2.5, 3.0} × 6
networks = 78 virgin networks, seeds 8100 + i·6 + j. Because ρ maps noisily to λ in the
extended range (pilot on burned seeds 7990-7995: a ρ=2.5 network with λ=−0.12), the
sealed tests are PER NETWORK on measured λ, with strata assigned by pre-declared rule:
stable λ < −0.01, edge |λ| ≤ 0.01, chaotic λ > +0.01 (deep strata at ±0.05 for E2).
One run of the whole grid. Networks with total coherent power 0 (T_c undefined) are
excluded and counted in the report.

## 4. Sealed tests (α = 0.05 where applicable)
- **E1 (stable law):** among stable networks, Spearman(T_c, 1/|λ|) ≥ 0.80, p < 0.05.
- **E2 (edge maximum):** median T_c of edge networks ≥ 3× the median T_c of deep-stable
  networks (λ < −0.05) AND ≥ 3× that of deep-chaotic networks (λ > +0.05). (Requires ≥ 5
  networks per stratum; if any stratum has fewer, E2 is reported as underpowered — an
  uncomfortable cell we accept.)
- **E3 (chaotic direction):** among chaotic networks, Spearman(λ, T_c) ≤ −0.50,
  one-sided p < 0.05.

| Outcome | Reading |
|---|---|
| E1✓ E2✓ E3✓ | The duration law holds across the edge: relaxation governs one side, decoherence the other, and coherent time peaks at criticality — the temporal mechanism beneath C3's inverted-U. |
| E1✓ E2✓ E3✗ | The edge maximum and stable law stand; the chaotic decay remains directionally unproven — reported. |
| E1✓ E2✗ | The law holds where it was trained and fails where it matters most; reported prominently. |
| E1✗ | The training fit did not generalize; the law dies on virgin ground. |

## 5. Secondary (descriptive)
P_coh vs λ per stratum; T_c vs the measured R-dim of exp45-style pipelines is NOT
computed here (no R-dim in this protocol — duration only); the ln-ln slope on the
chaotic side (training gave −0.10) is reported for the future quantitative attempt.

## 6. Rules
One computation of the sealed quantities; no amendments after sealing. Pilot: seeds
7990-7995 (burned, technical shakeout only, disclosed above). Mechanical verifier before
any number enters a draft. The outcome travels with the next firm deposit.
