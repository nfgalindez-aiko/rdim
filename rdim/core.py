"""
rdim — debiased perturbational complexity and reproducible dimensionality.

Core implementation. Independent implementation from the published equations of the state-transition
quantification (validated identical to the reference PCIst implementation, r=1.0000;
see Galindez 2026, preprint 1), extended with:
  - fully out-of-sample estimation (XV): basis, component selection and thresholds are
    fit on half the trials and transitions are counted on the held-out half;
  - reproducible dimensionality (R-dim): the number of principal response directions
    that replicate across independent trial halves;
  - built-in null controls: every estimate can be accompanied by a sham/permutation
    floor, because an estimate without its null is not a measurement.
"""
from __future__ import annotations
import numpy as np

__all__ = ["perturbational_complexity", "pcist_standard", "null_floor"]

DEFAULTS = dict(k=1.2, min_snr=1.1, max_var=99.0, n_steps=50, n_splits=4, seed=0)


def _windows(times, baseline, response):
    b = (times >= baseline[0]) & (times < baseline[1])
    r = (times >= response[0]) & (times < response[1])
    if b.sum() < 10 or r.sum() < 10:
        raise ValueError("baseline/response windows too short for these times")
    return b, r


def _project(evoked_fit, evoked_eval, bmask, rmask, min_snr, max_var):
    """SVD basis + variance cut + SNR filter decided on `evoked_fit`; both projected."""
    U, S, Vt = np.linalg.svd(evoked_fit[:, rmask].T, full_matrices=False)
    var = S ** 2
    n_keep = int(np.searchsorted(100 * np.cumsum(var) / var.sum(), max_var) + 1)
    basis = Vt[:n_keep]
    a = basis @ evoked_fit
    b = basis @ evoked_eval
    snr = np.sqrt(np.mean(a[:, rmask] ** 2, axis=1) / np.mean(a[:, bmask] ** 2, axis=1))
    keep = snr > min_snr
    return a[keep], b[keep]


def _nst(x, thr):
    """Average number of state transitions of 1-D series x at threshold thr."""
    D = np.abs(x[:, None] - x[None, :])
    T = np.abs(np.diff((D <= thr).astype(np.int8), axis=1))
    return T.sum() / (len(x) ** 2)


def _stq_fit(comps, bmask, rmask, k, n_steps):
    """Optimal thresholds per component, chosen on the fitting half."""
    thrs = []
    n_r = int(rmask.sum())
    for c in comps:
        cb, cr = c[bmask], c[rmask]
        Db = np.abs(cb[:, None] - cb[None, :])
        Dr = np.abs(cr[:, None] - cr[None, :])
        grid = np.linspace(np.median(Db), Dr.max(), n_steps)
        best_v, best_t = -np.inf, grid[0]
        for t in grid:
            v = (_nst(cr, t) - k * _nst(cb, t)) * n_r
            if v > best_v:
                best_v, best_t = v, t
        thrs.append(best_t)
    return thrs


def _stq_eval(comps, thrs, bmask, rmask, k):
    n_r = int(rmask.sum())
    total = 0.0
    for c, t in zip(comps, thrs):
        v = (_nst(c[rmask], t) - k * _nst(c[bmask], t)) * n_r
        total += max(v, 0.0)
    return total


def perturbational_complexity(trials, times, baseline, response, **kw):
    """Debiased perturbational complexity (XV) and reproducible dimensionality (R-dim).

    Parameters
    ----------
    trials : ndarray (n_trials, n_channels, n_times)
        Single-trial responses, time-locked to the perturbation.
    times : ndarray (n_times,)
        Time stamps (same units as the window arguments; negative = pre-perturbation).
    baseline, response : (t0, t1) tuples.
    k, min_snr, max_var, n_steps, n_splits, seed : see DEFAULTS.

    Returns
    -------
    dict with 'xv' (debiased complexity), 'rdim' (reproducible dimensionality),
    'per_split' lists, and the parameters used.
    """
    p = {**DEFAULTS, **kw}
    trials = np.asarray(trials, dtype=float)
    if trials.ndim != 3:
        raise ValueError("trials must be (n_trials, n_channels, n_times)")
    if trials.shape[0] < 8:
        raise ValueError("need at least 8 trials for split estimation")
    bmask, rmask = _windows(np.asarray(times), baseline, response)
    rng = np.random.default_rng(p["seed"])
    n = trials.shape[0]
    xvs, rdims = [], []
    for _ in range(p["n_splits"]):
        idx = rng.permutation(n)
        evA = trials[idx[: n // 2]].mean(0)
        evB = trials[idx[n // 2:]].mean(0)
        a, b = _project(evA, evB, bmask, rmask, p["min_snr"], p["max_var"])
        if a.shape[0] == 0:
            xvs.append(0.0)
            rdims.append(0.0)
            continue
        rdims.append(sum(max(float(np.corrcoef(a[i, rmask], b[i, rmask])[0, 1]), 0.0)
                         for i in range(a.shape[0])))
        thrs = _stq_fit(a, bmask, rmask, p["k"], p["n_steps"])
        xvs.append(_stq_eval(b, thrs, bmask, rmask, p["k"]))
    return dict(xv=float(np.mean(xvs)), rdim=float(np.mean(rdims)),
                per_split=dict(xv=xvs, rdim=rdims), params=p)


def pcist_standard(evoked, times, baseline, response, **kw):
    """Standard (within-sample) PCIst on a trial-averaged signal — independent implementation (from the published equations), numerically identical to the reference code. Provided for
    comparability; prefer `perturbational_complexity` + `null_floor`."""
    p = {**DEFAULTS, **kw}
    evoked = np.asarray(evoked, dtype=float)
    bmask, rmask = _windows(np.asarray(times), baseline, response)
    a, _ = _project(evoked, evoked, bmask, rmask, p["min_snr"], p["max_var"])
    if a.shape[0] == 0:
        return 0.0
    thrs = _stq_fit(a, bmask, rmask, p["k"], p["n_steps"])
    return float(_stq_eval(a, thrs, bmask, rmask, p["k"]))


def null_floor(trials, times, baseline, response, n_null=20, quantity="both", **kw):
    """Null distribution of the estimator on THESE trials with the perturbation
    erased by design: for each null draw, trials are circularly time-shifted by
    random offsets (destroying time-locking to the perturbation while preserving
    each trial's autocorrelation and spectrum). Report your estimate together
    with, e.g., its percentile in this distribution.

    IMPORTANT — both quantities need their null, for different reasons:

    * ``xv`` is debiased against the baseline inside the estimator, so its null
      sits near zero and the null mainly guards against residual time-locked
      structure.
    * ``rdim`` sums per-component cross-half correlations **clipped at zero**
      (see ``perturbational_complexity``). Clipping keeps only the positive half
      of the noise, so R-dim has a strictly positive floor under the no-response
      null, and that floor grows with the number of retained components — i.e.
      with channel/unit count. Order statistics (rank correlations, growth with
      trial count, contrasts at matched coverage) are unaffected, because the
      floor is an additive offset that is flat in trial count. **Absolute levels,
      and comparisons of level across modalities or systems with different
      component counts, are not**: those must be reported floor-corrected, or at
      least alongside this null.

    Parameters
    ----------
    quantity : {"both", "xv", "rdim"}
        ``"both"`` (default) returns ``{"xv": array, "rdim": array}``.
        ``"xv"`` or ``"rdim"`` return a bare array of that quantity.

    Notes
    -----
    Before v0.2.0 this function returned the ``xv`` array only, which made the
    R-dim floor unmeasurable with the published tool. Pass ``quantity="xv"`` for
    the old return shape.
    """
    if quantity not in ("both", "xv", "rdim"):
        raise ValueError('quantity must be "both", "xv" or "rdim"')
    p = {**DEFAULTS, **kw}
    trials = np.asarray(trials, dtype=float)
    rng = np.random.default_rng(p["seed"] + 1)
    T = trials.shape[2]
    xvs, rdims = [], []
    for j in range(n_null):
        shifted = np.stack([np.roll(t, rng.integers(T // 4, 3 * T // 4), axis=-1)
                            for t in trials])
        r = perturbational_complexity(shifted, times, baseline, response,
                                      **{**kw, "seed": p["seed"] + 100 + j})
        xvs.append(r["xv"])
        rdims.append(r["rdim"])
    if quantity == "xv":
        return np.array(xvs)
    if quantity == "rdim":
        return np.array(rdims)
    return dict(xv=np.array(xvs), rdim=np.array(rdims))

