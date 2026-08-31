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
    null = null_floor(trials, TIMES, BW, RW, n_null=8)["xv"]
    p = (null >= r["xv"]).mean()
    assert p == 0.0, f"la respuesta real deberia superar todo el nulo (p={p})"
    print(f"  ok  nulo: XV={r['xv']:.1f} vs null max={null.max():.1f} (p={p:.3f})")

def test_reproducible():
    trials = make_trials()
    a = perturbational_complexity(trials, TIMES, BW, RW, seed=7)
    b = perturbational_complexity(trials, TIMES, BW, RW, seed=7)
    assert a["xv"] == b["xv"]
    print("  ok  determinismo con semilla fija")


# ---------------------------------------------------------------------------
# Banco de verdad conocida para R-dim.
# Hasta v0.2.0 la suite solo verificaba un ORDEN (rica > simple), nunca un
# NUMERO: R-dim no tenia banco de verdad conocida. Aca se inyectan k
# direcciones espaciales ortogonales coherentes y se exige que R-dim lea k.
# ---------------------------------------------------------------------------

def inyectar(k, n=60, ch=48, snr=1.5, rng=None):
    """Cama de ruido con k direcciones coherentes ortogonales. Verdad = k."""
    rng = rng or np.random.default_rng(1234 + k)
    trials = rng.standard_normal((n, ch, len(TIMES)))
    if k == 0:
        return trials
    base = np.linalg.qr(rng.standard_normal((ch, k)))[0][:, :k]   # ortonormal
    t = np.clip(TIMES, 0, None)
    amp = snr * trials.std()
    for j in range(k):
        tau = 80.0 + 40.0 * j
        curso = np.where(TIMES > 0, np.exp(-t / tau) * np.cos(2 * np.pi * (5 + 4 * j)
                                                              * t / 1000), 0.0)
        trials += amp * base[:, j][None, :, None] * curso[None, None, :]
    return trials


def test_rdim_lee_la_verdad_inyectada():
    """A SNR alto, R-dim debe leer k, no solo ordenar. Tolerancia +-0.5 dim."""
    print("  banco de verdad conocida (SNR alto: R-dim debe LEER k):")
    ok = True
    for k in (0, 3, 5, 10):
        vals = [perturbational_complexity(
            inyectar(k, snr=6.0, rng=np.random.default_rng(700 + k * 10 + s)),
            TIMES, BW, RW, seed=s)["rdim"] for s in range(3)]
        m = float(np.mean(vals))
        if k == 0:
            bien = 0 < m < 1.5      # el piso de rectificacion, no cero
            print(f"    k=0  -> R-dim {m:5.2f}   (piso de rectificacion: "
                  f"positivo y <1.5)")
        else:
            bien = abs(m - k) <= 0.5
            print(f"    k={k:<2d} -> R-dim {m:5.2f}   (verdad {k}, "
                  f"error {m - k:+.2f})")
        ok = ok and bien
    assert ok, "R-dim no lee la dimensionalidad inyectada a SNR alto"
    print("  ok  a SNR alto R-dim lee la verdad inyectada")


def test_rdim_sublee_cuando_baja_el_snr():
    """CALIBRACION: R-dim converge a la verdad con senal fuerte y SUB-LEE
    monotonicamente cuando el SNR por componente baja. Es la propiedad que
    convierte cualquier caida de ganancia en una caida aparente de
    dimensionalidad, y por eso hay que medirla y publicarla.

    Medido (media de 3 semillas, k = 3 / 5 / 10):
        SNR 6.0 -> 3.13 / 5.11 / 10.10   (exacto)
        SNR 3.0 -> 2.98 / 4.90 /  9.81
        SNR 1.5 -> 2.49 / 4.25 /  8.87
        SNR 1.0 -> 1.96 / 3.50 /  7.72
        SNR 0.5 -> 0.86 / 1.76 /  4.50   (-60%)
    """
    k = 5
    lect = {}
    for snr in (0.5, 1.5, 6.0):
        vals = [perturbational_complexity(
            inyectar(k, snr=snr, rng=np.random.default_rng(700 + k * 10 + s)),
            TIMES, BW, RW, seed=s)["rdim"] for s in range(3)]
        lect[snr] = float(np.mean(vals))
    print("  calibracion por SNR (verdad k=5): " +
          ", ".join(f"SNR {s}: {v:.2f}" for s, v in lect.items()))
    assert lect[0.5] < lect[1.5] < lect[6.0], "la lectura debe crecer con el SNR"
    assert abs(lect[6.0] - k) <= 0.5, "a SNR alto tiene que dar la verdad"
    assert lect[0.5] < 0.6 * k, "a SNR bajo tiene que sub-leer marcadamente"
    print("  ok  R-dim es exacto con senal fuerte y sub-lee con senal debil "
          "(un cambio de ganancia se lee como cambio de dimension)")


def test_rdim_tiene_piso_positivo_y_plano_en_n():
    """El piso de R-dim bajo el nulo es POSITIVO (clip en cero) y NO crece con
    la cantidad de ensayos. Ambas cosas hay que saberlas: la primera invalida
    comparaciones de nivel sin corregir; la segunda salva los claims de
    crecimiento."""
    pisos = {}
    for n in (30, 60, 120):
        vals = [perturbational_complexity(inyectar(0, n=n, rng=np.random.default_rng(900 + n + s)),
                                          TIMES, BW, RW, seed=s)["rdim"]
                for s in range(4)]
        pisos[n] = float(np.mean(vals))
    print(f"  piso de R-dim bajo el nulo: " +
          ", ".join(f"n={n}: {v:.2f}" for n, v in pisos.items()))
    assert all(v > 0 for v in pisos.values()), "el piso deberia ser estrictamente positivo"
    creci = pisos[120] - pisos[30]
    assert abs(creci) < 0.6, f"el piso NO deberia crecer con n (creció {creci:+.2f})"
    print(f"  ok  piso positivo y plano en n (variacion {creci:+.2f})")


def test_null_floor_devuelve_rdim():
    """Regresion de v0.2.0: null_floor debe poder dar el nulo de R-dim.
    Antes devolvia solo xv, y el piso de R-dim era inmedible con la herramienta
    publicada."""
    trials = make_trials(rich=True)
    nulo = null_floor(trials, TIMES, BW, RW, n_null=6)
    assert isinstance(nulo, dict) and "rdim" in nulo and "xv" in nulo
    assert len(nulo["rdim"]) == 6
    solo_xv = null_floor(trials, TIMES, BW, RW, n_null=6, quantity="xv")
    assert solo_xv.shape == (6,)
    r = perturbational_complexity(trials, TIMES, BW, RW)
    p_rdim = float((nulo["rdim"] >= r["rdim"]).mean())
    print(f"  ok  null_floor da ambos: R-dim={r['rdim']:.2f} vs nulo "
          f"mediana {np.median(nulo['rdim']):.2f} (p={p_rdim:.3f})")


if __name__ == "__main__":
    for fn in [test_sham_near_zero, test_rich_beats_simple,
               test_null_floor_calibrated, test_reproducible,
               test_rdim_lee_la_verdad_inyectada,
               test_rdim_sublee_cuando_baja_el_snr,
               test_rdim_tiene_piso_positivo_y_plano_en_n,
               test_null_floor_devuelve_rdim]:
        fn()
    print("TODOS LOS TESTS PASARON")
