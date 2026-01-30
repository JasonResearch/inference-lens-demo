"""
lens.py

Apply observational / inference effects ("inference lens")
to a baryon-only truth galaxy.
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
        Random seed for noise

    Returns
    -------
    dict with inferred observables (placeholder for now)
    """
    rng = np.random.default_rng(seed)

    r = truth["r_kpc"]
    Vtrue = truth["Vtrue_kms"]

    # Placeholder: start with truth, distort later
    Vobs = Vtrue.copy()

    return {
        "r_kpc": r,
        "Vobs_kms": Vobs,
    }
