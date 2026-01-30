"""
truth.py

Build a simple baryon-only "truth" disk galaxy.

This is intentionally demonstrative (not a full galaxy formation model):
- Choose an exponential surface density profile Sigma(r) ~ exp(-r/Rd)
- Normalize it so the total baryonic mass integrates to Mb_total
- Compute enclosed mass M(<r) by integrating Sigma(r) over area
- Compute a simple rotation curve proxy: V^2(r) = G * M(<r) / r

Units:
- r is in kpc
- mass is in Msun
- velocity is in km/s
"""

from __future__ import annotations

import numpy as np

# Gravitational constant in convenient astro units:
# G = 4.30091e-6 (kpc * (km/s)^2) / Msun
G_KPC_KMS2_PER_MSUN = 4.30091e-6


def build_truth_galaxy(cfg: dict, seed: int = 1) -> dict:
    """
    Build a baryon-only "truth" galaxy.

    Parameters
    ----------
    cfg : dict
        Expected keys:
          - Mb_total_msun (float)
          - Rd_kpc (float)
          - Rmax_kpc (float)
          - npoints (int)
    seed : int
        Included for interface consistency (not used yet).

    Returns
    -------
    dict with:
      - r_kpc : ndarray
      - Sigma_b : ndarray (Msun/kpc^2)
      - Mb_enclosed_msun : ndarray
      - Vtrue_kms : ndarray
      - Mb_total_msun : float
      - Rd_kpc : float
    """
    # Unpack config with safe defaults
    Mb_total = float(cfg.get("Mb_total_msun", 5e10))
    Rd = float(cfg.get("Rd_kpc", 3.0))
    Rmax = float(cfg.get("Rmax_kpc", 30.0))
    n = int(cfg.get("npoints", 300))

    # Radial grid: start slightly above zero to avoid division by zero in V(r)
    r = np.linspace(0.05, Rmax, n)

    # Exponential surface density shape (unnormalized)
    Sigma_shape = np.exp(-r / Rd)

    # Normalize Sigma so that total mass integrates to Mb_total:
    # Mb_total = ∫ 2π r Sigma(r) dr
    integrand = 2.0 * np.pi * r * Sigma_shape
    norm = np.trapz(integrand, r)
    Sigma = Sigma_shape * (Mb_total / norm)  # Msun/kpc^2

    # Enclosed mass M(<r) = ∫_0^r 2π r' Sigma(r') dr'
    dM_dr = 2.0 * np.pi * r * Sigma
    Mb_enclosed = np.cumsum(dM_dr * np.gradient(r))

    # Simple rotation curve proxy (spherical-equivalent approximation):
    # V^2 = G M(<r) / r
    V = np.sqrt(G_KPC_KMS2_PER_MSUN * Mb_enclosed / r)

    return {
        "r_kpc": r,
        "Sigma_b": Sigma,
        "Mb_enclosed_msun": Mb_enclosed,
        "Vtrue_kms": V,
        "Mb_total_msun": Mb_total,
        "Rd_kpc": Rd,
    }
