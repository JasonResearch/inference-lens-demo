"""
run_demo.py

Entry point for the inference lens demonstration.
"""

from inference_lens_sim.config import TRUTH_GALAXY
from inference_lens_sim.truth import build_truth_galaxy


def main():
    truth = build_truth_galaxy(TRUTH_GALAXY)

    print("Truth galaxy built:")
    print(f"  Total baryonic mass = {truth['Mb_total_msun']:.2e} Msun")
    print(f"  Disk scale length   = {truth['Rd_kpc']:.2f} kpc")
    print(f"  Max radius          = {truth['r_kpc'][-1]:.1f} kpc")
    print(f"  Peak V_true         = {truth['Vtrue_kms'].max():.1f} km/s")


if __name__ == "__main__":
    main()
