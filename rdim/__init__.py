"""rdim — debiased perturbational complexity and reproducible dimensionality.

Quickstart:
    from rdim import perturbational_complexity, null_floor
    r = perturbational_complexity(trials, times, baseline=(-400, -50), response=(0, 300))
    null = null_floor(trials, times, baseline=(-400, -50), response=(0, 300))
    print(r['xv'], r['rdim'], (null >= r['xv']).mean())  # value, dimension, null p-value
"""
from .core import perturbational_complexity, pcist_standard, null_floor

__version__ = "0.2.0"
__all__ = ["perturbational_complexity", "pcist_standard", "null_floor"]
