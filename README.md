# NBSL-Theory: Non-Baryonic Structural Lattice
**Version:** 3.0 (Multi-Sector & Monte Carlo Validation)  
**Status:** `Active / Open for Peer Review`  
**DOI:** [10.5281/zenodo.19221396](https://doi.org/10.5281/zenodo.19221396)

## 🌌 Overview
This repository contains the mathematical framework, multi-sector datasets, and Monte Carlo validation for the **Non-Baryonic Structural Lattice (NBSL)**. We demonstrate that stellar distribution in Gaia DR3 is anchored to a 120° nodal resonance manifold with a **P-Value < 0.001**.

## 📊 Statistical Validation (V3.0)
To neutralize the Look-Elsewhere Effect (LEE) and confirm the structural nature of the lattice, we implemented:
* **Multi-Sector Replication:** Verification across 3 independent galactic sectors (Anticenter, Sirius, Polaris).
* **Monte Carlo Permutation (N=1000):** Randomized control tests to break spatial phase.
* **Result:** The 120.0° ± 0.1° resonance persists with a statistical significance of P < 0.001.

## 📁 Repository Structure
* **/scripts**: `scramble_test.py` — O(N³) Angular Resonance & Monte Carlo Analysis.
* **/data**: `anticenter_sector_gaia.csv` — Multi-sector coordinate subsets (Active).
* **/docs**: Technical preprints and Nodal Lagrangian Dynamics.

## 🛠️ Usage
1. Clone the repository.
2. Run `python scripts/scramble_test.py`.
3. The script will execute 1,000 permutations and output the real vs. random resonance frequency.

## ⚖️ Theoretical Physics: Nodal Lagrangian & Vacuum Coupling
We propose a Lagrangian density where baryonic matter ($T_{\mu\nu}$) couples to the geometric potential of the vacuum ($\Phi_{Lattice}$):

$$\mathcal{L}_{Total} = \mathcal{L}_{GR} - \alpha \int \Phi_{Lattice}(x) T^{\mu}_{\mu}(x) \sqrt{-g} \, d^4x$$

**Physical Mechanism:**
* **Nodal Wells:** The vacuum is a quantized manifold with potential minima at 120° intersections.
* **Energy Minimization:** Matter is statistically anchored to these nodes to achieve the lowest energy state within the vacuum fabric.

---
Independent Research | Santarém Sector Observation | Open Science
