
# Inference Lens Demo (Dark-Matter-Like Discrepancy Without Adding Mass)

This repository provides a controlled, reproducible demonstration that a **dark-matter-like dynamical discrepancy**
can be produced by **measurement + inference differences** (an "inference lens"), even when the underlying
("truth") system contains **no dark matter**.

The goal is demonstrative:
- Hold the *true* baryonic mass distribution fixed.
- Simulate two observational/inference pipelines (Lens A vs Lens B).
- Show that the inferred dynamical mismatch changes **without changing the true mass**.

This does **not** claim dark matter is "just optics."
It demonstrates an **existence proof**: inference and normalization choices can manufacture a discrepancy signal.

## What this produces

A single run generates:
- A 3-panel figure:
  1) Truth rotation curve vs inferred curves (Lens A and Lens B)
  2) Observed surface-brightness profiles / truncation behavior (how information is lost)
  3) Discrepancy proxy comparison (e.g., log10(J3) or Mdyn/Mb proxy)
- A CSV summary of inferred parameters and mismatch metrics for A and B

## Quickstart

### 1) Install
```bash
pip install -r requirements.txt
```
### 2) Run default A/B demonstration
```bash
python run_demo.py --out outputs/demo --seed 1 --save-plots
```
### 3) Run a single preset
```bash
python run_demo.py --preset presets/lens_A_deep_sharp.json --out outputs/runA --seed 1 --save-plots
python run_demo.py --preset presets/lens_B_shallow_blurry.json --out outputs/runB --seed 1 --save-plots
```
## Presets
- `lens_A_deep_sharp.json`: deep SB limit, low blur, minimal smearing (good recovery)
- `lens_B_shallow_blurry.json`: shallow SB limit, higher blur, beam smearing (information loss)

## Output
- summary.csv (truth and inferred values)
- figure_demo.png (the 3-panel figure)
- config_used.json (exact config snapshot for reproducibility)

## Reproducibility
- All runs can be made deterministic with --seed.
- The output directory includes a saved copy of the configuration used.

## License
MIT (see LICENSE)
---

## requirements.txt (simple and standard)
```txt
numpy
scipy
pandas
matplotlib
```
