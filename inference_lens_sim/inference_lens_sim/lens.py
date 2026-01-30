"""
lens.py

Apply observational / inference effects ("inference lens")
to a baryon-only truth galaxy.

First implemented effect:
- surface-brightness truncation (information loss)
"""

import numpy as np


def apply_inference_lens(truth: dict, lens_cfg: dict, seed: int = 1) -> dict:
    """
    Apply inference effects to the truth galaxy.

    Parameters
    ----------
    truth : dict
        Output of build_truth_galaxy()
    lens_cfg : dict
        Loaded JSON lens preset
    seed : int
        Random seed for noise (reserved for future effects)

    Returns
    -------
    dict with inferred observables
    """
    rng = np.random.default_rng(seed)

    r = truth["r_kpc"]
    Sigma = truth["Sigma_b"]
    Vtrue = truth["Vtrue_kms"]

    # Surface-brightness limit (acts like information cutoff)
    sb_limit = lens_cfg["sb_limit_mag_arcsec2"]

    # Convert surface density to a proxy surface brightness
    # (higher Sigma = brighter)
    SB_proxy = -2.5 * np.log10(Sigma / Sigma.max())

    # Observability mask
    observed = SB_proxy <= sb_limit

    # Inferred rotation curve: only where observable
    r_obs = r[observed]
    V_obs = Vtrue[observed]

    return {
        "r_kpc": r_obs,
        "Vobs_kms": V_obs,
        "observed_mask": observed,
        "sb_proxy": SB_proxy,
    }
