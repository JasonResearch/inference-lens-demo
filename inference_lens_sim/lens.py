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
    _rng = np.random.default_rng(seed)  # reserved for future noise effects

    r = truth["r_kpc"]
    Sigma = truth["Sigma_b"]
    Vtrue = truth["Vtrue_kms"]

    # Surface-brightness limit (mag/arcsec^2)
    sb_limit = float(lens_cfg["sb_limit_mag_arcsec2"])

    # Anchor the central (brightest) surface brightness to a realistic value.
    # This makes sb_limit values like 24 vs 28.5 meaningful.
    sb0 = float(lens_cfg.get("sb0_mag_arcsec2", 20.0))  # central SB (mag/arcsec^2)

    # Magnitude-like profile: larger number = fainter
    SB_mag = sb0 - 2.5 * np.log10(Sigma / Sigma.max())

    # Observable where brighter than the limit
    observed = SB_mag <= sb_limit

    # Inferred rotation curve: only where observable
    r_obs = r[observed]
    V_obs = Vtrue[observed]

    return {
        "r_kpc": r_obs,
        "Vobs_kms": V_obs,
        "observed_mask": observed,
        "sb_mag": SB_mag,
    }
