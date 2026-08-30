# rdim — perturbational complexity that cannot flatter itself

Debiased perturbational complexity (PCIst-XV) and **reproducible dimensionality** (R-dim)
for evoked responses — EEG, iEEG, LFP, MEA, simulations. A drop-in, bias-free alternative
to standard PCIst, with null controls built in.

## Why

The standard PCIst pipeline selects its SVD basis, its components and its thresholds on the
same data it then quantifies. On high-dimensional low-SNR data this inflates the index in the
complete absence of any response — up to values typical of wakeful human cortex (details,
boundary conditions and human validation: Galindez 2026, doi:10.5281/zenodo.22101483). `rdim` makes every
selection on half the trials and counts state transitions on the other half; the bias is gone
by construction, at no cost in sensitivity (AUC ≥ standard in every regime tested).

On identical no-response data (32 channels, correlated noise, 40 trials):

| | standard PCIst | rdim XV |
|---|---|---|
| sham (no response at all) | **214.1** | **4.9** |

## Install / use

```
pip install numpy
# copy the rdim/ folder (single dependency: numpy)
```

```python
from rdim import perturbational_complexity, null_floor

r = perturbational_complexity(trials, times, baseline=(-400, -50), response=(0, 300))
null = null_floor(trials, times, baseline=(-400, -50), response=(0, 300))

print(r["xv"])                    # debiased complexity
print(r["rdim"])                  # reproducible dimensionality of the response
print((null >= r["xv"]).mean())   # p-value against the built-in null
```

`trials`: array (n_trials, n_channels, n_times). That's it.

**Report rule we propose to the field:** no perturbational-complexity value without its
paired null. `null_floor` erases the time-locking by circular trial shifts while preserving
every trial's spectrum — if your effect does not clear it, you have measured your pipeline.

## What R-dim means

R-dim counts how many principal directions of the evoked response *replicate across
independent halves of your trials* — the response's reproducible dimensionality. In 366 core
simulated recurrent networks it is the quantity that perturbational complexity actually
tracks (ρ = 0.74), maximal at the edge of chaos and destroyed by both order and chaos
(doi:10.5281/zenodo.22101631). It requires simultaneous sensitivity and stability — which may be why the
brain only exhibits it awake.

## Validation

`tests/test_rdim.py` — sham floor, rich-vs-stereotyped discrimination, null calibration,
determinism. The independently written state-transition core (from the published equations) reproduces the reference PCIst
implementation exactly (r = 1.0000 on 16 cases). Full validation battery: the 27-experiment
suite in the project's reproducibility archive.

## Cite

If you use rdim, cite the companion preprints:

- Galindez, N. (2026). *Selection bias can inflate the Perturbational Complexity Index (PCIst) in high-dimensional low-SNR regimes.* Zenodo. https://doi.org/10.5281/zenodo.22101483
- Galindez, N. (2026). *Debiased perturbational complexity peaks at the edge of chaos.* Zenodo. https://doi.org/10.5281/zenodo.22101631
- Galindez, N. (2026). *A replicated, control-passing association between resting spectral slope and TMS-evoked complexity fails blind preregistered confirmation.* Zenodo. https://doi.org/10.5281/zenodo.22101653
- Galindez, N. (2026). *The reproducible dimensionality of the human intracranial evoked response grows without detectable ceiling up to 480 trials* Zenodo. https://doi.org/10.5281/zenodo.22120070
- Galindez, N. (2026). *Debiased reproducible dimensionality is lower under isoflurane than in wakefulness in the same mouse brain, at matched trial counts and stimulation currents* Zenodo. https://doi.org/10.5281/zenodo.22133404) · [constraints paper](https://doi.org/10.5281/zenodo.22168191) · [field-vs-neurons paper](https://doi.org/10.5281/zenodo.22168243

## Authors

Nicolás Galindez. Developed with substantial AI assistance (Claude, Anthropic). MIT license.


