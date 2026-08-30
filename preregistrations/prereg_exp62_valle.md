# Sealed protocol — Exp62: the valley law (does exact criticality tax richness, and through what?)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any confirmatory
network was generated.

## 1. Origin (disclosed)
At controlled saturation, the exact edge appeared twice as a local R-dim minimum —
never as a sealed claim: 4c50450's fine map (edge stratum 5.82 vs flanks 7.07/6.88)
and 81600bd's three cells (edge 6.41, lowest). If real, the finding is positive and
mechanistically pointed: the same critical slowing that crowns coherent TIME should
inflate the trajectory-noise floor of averaged responses (the program's long-known
critical-fluctuation intrusion), taxing richness exactly at λ = 0. The mechanism is
pre-declared and tested jointly. Two sightings + one seal: whatever falls here, the
valley question closes.

## 2. Design (frozen)
Home family; saturation slice g_med ∈ (0.75, 0.85] on the separate rng(seed+60) stream
(as 4c50450). Three fine λ cells: **stable-flank** (−0.012, −0.004], **exact-edge**
(−0.004, +0.004], **chaotic-flank** (+0.004, +0.012]; 60 virgin networks each = 180.
ρ ~ U(0.9, 1.8) rng(79000+seed); pulse rng(seed+2). Per network: R-dim (120 trials,
rng(seed+50)); and the trajectory floor **N_med** = median over the top-10 components
of T·var_t(evoked-residual projections)/60, measured on the independent rng(seed+40)
set with the exp45-certified trajectory object (basis = SVD of that set's half-A
average). Feasibility: reuses 4c50450's registered scan of the same region (disclosed;
no new quantities were observed). Scan seeds 870000…, cap 910000; under-filled cells
reported → underpowered. One run. Bootstrap 10,000, rng 626262.

## 3. Sealed tests
- **V1 (the valley):** the edge cell's median R-dim ≤ each flank's median − 0.4, with
  bootstrap P(edge is the minimum) ≥ 0.85.
- **V2 (the mechanism):** the edge cell's median N_med exceeds each flank's, with
  bootstrap P(edge is the maximum of N_med) ≥ 0.85.

| Outcome | Reading |
|---|---|
| V1✓ V2✓ | The critical tax is law with its mechanism: exact criticality inflates the trajectory-noise floor and charges it against richness — the throne of time is paid for in the coin of richness. |
| V1✓ V2✗ | The valley is real, its mediator open; reported. |
| V1✗ | The two sightings were sampling noise; the valley question closes, reported. |

## 4. Rules
One computation; no amendments after sealing. Mechanical verifier before any number
enters a draft. The outcome travels with the next firm deposit.
