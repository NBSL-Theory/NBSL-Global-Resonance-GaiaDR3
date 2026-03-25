# NBSL-Theory: Non-Baryonic Structural Lattice (Global Analysis)
**Version:** 3.0 (Multi-Sector & Monte Carlo Validation)  
**Status:** `Active / Peer-Review` | **DOI:** [10.5281/zenodo.19221396](https://doi.org/10.5281/zenodo.19221396)

## Project Overview
This repository hosts the evidence for a 120° nodal resonance in the galactic vacuum fabric. In Version 3.0, we transition from local observations to a Global Manifold Validation.

## V3.0 Key Findings
* Multi-Sector Evidence: Resonance confirmed in Galactic Anticenter, Sirius Local Sector, and Polaris North.
* Statistical Rigor: 1,000-iteration Monte Carlo permutation test.
* Significance: P-Value < 0.001 (Zero flukes detected in random controls).

## Repository Map
* /data: anticenter_sector_gaia.csv (Contains all 3 sectors for replication).
* /scripts: scramble_test.py (Full Monte Carlo engine).
* requirements.txt: Environment setup.

## Execution
pip install -r requirements.txt
python scripts/scramble_test.py

## Physical Causal Model (Lagrangian)
L = L_GR - alpha * integral[ Phi_Lattice(x) * T(x) * sqrt(-g) d4x ]

**Physical Mechanism:**
Matter is anchored to vacuum nodes via geometric potential minimization. The 120° resonance is a manifestation of matter seeking the path of least resistance within the rigid geometric fabric of the vacuum.

---
Independent Research | Global Gaia DR3 Analysis | Open Science
