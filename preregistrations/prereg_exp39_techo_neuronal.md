# Sealed protocol — Exp39: The ceiling hunt in spiking populations (trial-scaling to ~960)

**Author:** Nicolás Galindez (ORCID 0009-0000-8207-0536), with AI assistance (Claude, Anthropic).
**Status:** SEALED at the public timestamp of this commit, BEFORE any spiking R-dim beyond
the previously published trial selections was computed. Disclosure: spiking R-dim on
*state-and-current-matched* selections up to rd480 exists (preprint 7 archive). This
protocol uses a DIFFERENT, never-computed selection (all valid awake trials, currents
pooled, chronological) and extends the grid to n = 960 — where the blindness lives.

## 1. The question
Constraint C5: simulated networks reach finite, system-specific R-dim ceilings (~9–11 for
1024-unit nets at feasible trial counts). Constraint C7: humans show no detectable ceiling
to 480 trials at the field level. Spiking populations here sit at ≈ 8.9 (median) at 480
matched trials and rising. With up to ~960 valid awake trials per session and hundreds of
units, this dataset probes double the human range at the neuronal level: does the
biological well show its bottom where the in-silico wells do?

## 2. Design (frozen)
- Trials: all electrical-stimulation trials with defined current, is_valid, not running,
  state = awake (primary; isoflurane as the same analysis run secondarily), chronological
  first-n. Currents pooled within state (as the human study pooled stimulus categories);
  no state comparison is made here, so no matching applies. Note: pooled currents make this
  a "session repertoire" scaling, stated as such.
- Grid: n ∈ {30, 60, 120, 240, 480, 960} truncated to each session's valid count.
- Instrument: rdim v0.1.0 frozen; 10 ms bins; epochs/windows/blanking/seeds as preprint 7.
- Tier (from archived metadata, before any spike read): sessions with ≥ 30 sorted units AND
  ≥ 480 valid awake trials. One session per animal (the preprint-6/7 selection where it
  exists; otherwise the session with more valid awake trials). Pilot: sub-546655 (units
  present, 459 awake valid — below tier), technical shakeout only. If < 8 tier animals
  survive, analyses become descriptive.

## 3. Sealed tests (exp32's sealed pair, unchanged)
Per session: I_high = R(n_max) − R(n_max/2) (n_max = largest grid point ≤ valid count;
n_max/2 must be a grid point), I_low = R(60) − R(30).
- **T1 (deceleration):** I_high < I_low across sessions, one-sided Wilcoxon, α = 0.05.
- **T2 (growth at the top):** I_high > 0, one-sided Wilcoxon, α = 0.05.

| T1 | T2 | Reading |
|---|---|---|
| no | yes | No detectable ceiling to ~960 trials at the neuronal level: the human C7 pattern replicates one level down and twice as far; the in-silico ceilings do not describe cortex at these scales. |
| yes | yes | Deceleration with continued growth: the ceiling's approach is visible — first empirical contact between C5 and biology; descriptive saturating fits (D) become meaningful and are compared with the in-silico 9–11. |
| yes | no | Ceiling reached within the sampled range: the biological well has a bottom; D per session reported and compared with C5. |
| no | no | No growth at top and no deceleration signal: measurement regime problem; reported as such. |

## 4. Secondary (descriptive)
The same analysis under isoflurane (valid counts to ~720): does the anesthetized state
show its ceiling earlier, as the parallel-curves picture would allow? Growth-law slope per
ln n compared with the human 0.94 and with preprint 7's matched-trial curves. Saturating
fits D per session (as in preprint 5, with the same caveats). Unit-count vs level.

## 5. Rules
One technical-amendment round at pilot maximum, documented before confirmatory runs. All
exclusions by criterion. Failures published, attached to the next firm step. Mechanical
verifier before any number enters a draft.
