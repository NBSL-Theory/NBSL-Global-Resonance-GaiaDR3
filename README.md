# NBSL-Theory: Non-Baryonic Structural Lattice
**Version:** 2.0 (Universal Validation)  
**Status:** `Active / Open for Peer Review`  
**DOI:** [10.5281/zenodo.19220693](https://doi.org/10.5281/zenodo.19220693)

## 🌌 Overview
This repository contains the mathematical framework and datasets for the **Non-Baryonic Structural Lattice (NBSL)**. We propose that stellar distribution in Gaia DR3 is anchored to a 120° nodal resonance manifold.

## 📁 Repository Structure
* **/scripts**: Contains `scramble_test.py` — O(N³) Angular Resonance Analysis and Positional Scrambling.
* **/data**: Contains `anticenter_sector_gaia.csv` — Observational subset for replication.
* **/docs**: Technical preprints and Nodal Vacuum Tension (NVT) model.

## 🛠️ Usage
To replicate the 120° resonance findings:
1. Clone the repository.
2. Run `python scripts/scramble_test.py` using the provided CSV datasets.
3. Compare the Observational Peak (120° ± 0.1°) against the Scrambled Control.

## ⚖️ Physical Hypothesis (NVT Model)
We propose that the vacuum geometry creates low-energy potential wells (Nodes). Matter is statistically more likely to cluster at these 120° intersections.
**Equation:** V_Lattice(r) = Σ [Λ_geom / |r - r_n|^2]

## ⚖️ Theoretical Physics: Nodal Lagrangian & Vacuum Coupling

To address the mechanism of physical causality, we propose that the NBSL is governed by a Lagrangian density where baryonic matter ($T_{\mu\nu}$) couples directly to the geometric potential of the vacuum ($\Phi_{Lattice}$):

$$\mathcal{L}_{Total} = \mathcal{L}_{GR} + \mathcal{L}_{int}$$

Where the interaction term ($\mathcal{L}_{int}$) is defined as:

$$\mathcal{L}_{int} = -\alpha \int \Phi_{Lattice}(x) T^{\mu}_{\mu}(x) \sqrt{-g} \, d^4x$$

### **Physical Mechanism:**
1. **Geometric Potential ($\Phi_{Lattice}$):** The vacuum is not an empty void but a quantized manifold with local potential minima located at 120° nodal intersections.
2. **Coupling ($\alpha$):** Baryonic mass (stars) "senses" these nodal wells. 
3. **Equilibrium:** Over cosmological timescales, stellar positions drift toward these nodes to achieve a state of **Minimum Potential Energy**.

**Conclusion:** The 120° resonance is not a coincidence; it is a manifestation of matter seeking the path of least resistance within the rigid geometric fabric of the vacuum.


---
Independent Research | Santarém Sector Observation*
