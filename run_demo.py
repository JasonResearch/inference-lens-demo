"""
run_demo.py

Entry point for the inference lens demonstration.
Compare two inference lenses applied to the same baryon-only truth galaxy.
"""

import json
from pathlib import Path

from inference_lens_sim.config import TRUTH_GALAXY
from inference_lens_sim.truth import build_truth_galaxy
from inference_lens_sim.lens import apply_inference_lens


def load_lens(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def summarize(label: str, inferred: dict):
    r = inferred["r_kpc"]
    V = inferred["Vobs_kms"]

    if len(r) == 0:
        print(f"{label}: no observable data")
        return

    print(f"{label}:")
    print(f"  Observable extent  = {r.max():.2f} kpc")
    print(f"  Points observed    = {len(r)}")
    print(f"  Peak inferred V    = {V.max():.1f} km/s")


def main():
    truth = build_truth_galaxy(TRUTH_GALAXY)

    lens_A = load_lens("presets/lens_A_deep_sharp.json")
    lens_B = load_lens("presets/lens_B_shallow_blurry.json")

    inferred_A = apply_inference_lens(truth, lens_A, seed=1)
    inferred_B = apply_inference_lens(truth, lens_B, seed=1)

    print("=== Inference Lens Comparison (same truth) ===")
    summarize("Lens A (deep / sharp)", inferred_A)
    summarize("Lens B (shallow / blurry)", inferred_B)


if __name__ == "__main__":
    main()
