"""Suite de validacion de rdim, destilada de los experimentos 02-16 del proyecto.
Correr: python tests/test_rdim.py
"""
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rdim import perturbational_complexity, pcist_standard, null_floor

RNG = np.random.default_rng(0)
TIMES = np.arange(-400, 600).astype(float)
BW, RW = (-400, -20), (0, 500)

def make_trials(n=40, ch=32, response=True, rich=True, rng=RNG):
    trials = rng.standard_normal((n, ch, len(TIMES))) * 0.5
    if response:
        t = np.clip(TIMES, 0, None)
        if rich:
            for f0, tau in [(31, 90.0), (17, 140.0), (7, 220.0)]:
                topo = rng.standard_normal(ch)[:, None]
                trials += (topo * np.where(TIMES > 0, np.sin(2 * np.pi * f0 * t / 1000)
                                           * np.exp(-t / tau), 0))[None]
        else:
            topo = np.ones((ch, 1))
            trials += (topo * np.where(TIMES > 0, 3 * np.exp(-t / 150), 0))[None]
    return trials

def test_sham_near_zero():
    sham = make_trials(response=False)
    r = perturbational_complexity(sham, TIMES, BW, RW)
    assert r["xv"] < 8, f"sham XV demasiado alto: {r['xv']}"
    print(f"  ok  sham: XV={r['xv']:.2f} (esperado ~0)  [el estandar da "
          f"{pcist_standard(sham.mean(0), TIMES, BW, RW):.1f} en el mismo dato]")

def test_rich_beats_simple():
    rich = perturbational_complexity(make_trials(rich=True), TIMES, BW, RW)
    simple = perturbational_complexity(make_trials(rich=False), TIMES, BW, RW)
    assert rich["xv"] > 2 * max(simple["xv"], 1), (rich["xv"], simple["xv"])
    assert rich["rdim"] > simple["rdim"]
    print(f"  ok  rica vs simple: XV {rich['xv']:.1f} > {simple['xv']:.1f}; "
          f"R-dim {rich['rdim']:.2f} > {simple['rdim']:.2f}")

def test_null_floor_calibrated():
    trials = make_trials(rich=True)
    r = perturbational_complexity(trials, TIMES, BW, RW)
    null = null_floor(trials, TIMES, BW, RW, n_null=8)
    p = (null >= r["xv"]).mean()
    assert p == 0.0, f"la respuesta real deberia superar todo el nulo (p={p})"
    print(f"  ok  nulo: XV={r['xv']:.1f} vs null max={null.max():.1f} (p={p:.3f})")

def test_reproducible():
    trials = make_trials()
    a = perturbational_complexity(trials, TIMES, BW, RW, seed=7)
    b = perturbational_complexity(trials, TIMES, BW, RW, seed=7)
    assert a["xv"] == b["xv"]
    print("  ok  determinismo con semilla fija")

if __name__ == "__main__":
    for fn in [test_sham_near_zero, test_rich_beats_simple,
               test_null_floor_calibrated, test_reproducible]:
        fn()
    print("TODOS LOS TESTS PASARON")
