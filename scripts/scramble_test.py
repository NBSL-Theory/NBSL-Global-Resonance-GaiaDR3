import numpy as np
import pandas as pd
import os

# NBSL THEORY - MONTE CARLO VALIDATION V4.0
# Testing 120° Resonance across independent sectors (Pleiades + Hyades)

def calculate_triplet_resonance(coords, iterations=10000):
    """Calculates 120° resonance using statistical sampling for efficiency."""
    n = len(coords)
    count = 0
    for _ in range(iterations):
        # Randomly select 3 stars from the dataset
        idx = np.random.choice(n, 3, replace=False)
        p1, p2, p3 = coords[idx]
        
        # Triangle sides
        a = np.linalg.norm(p2 - p3)
        b = np.linalg.norm(p1 - p3)
        c = np.linalg.norm(p1 - p2)
        
        # Law of Cosines for angle at p1
        denominator = 2 * b * c
        if denominator == 0: continue
        cos_a = np.clip((b**2 + c**2 - a**2) / denominator, -1, 1)
        angle = np.degrees(np.arccos(cos_a))
        
        # Nodal Resonance Filter (0.1° tolerance)
        if 119.9 <= angle <= 120.1:
            count += 1
    return count

# 1. DATA LOADING - V4.0 Global Analysis
# The script checks for both Pleiades and Hyades datasets
datasets = ['data/gaia_pleiades_full_670.csv', 'data/gaia_hyades_full_v4.csv']
data_frames = []

for f in datasets:
    if os.path.exists(f):
        print(f"--- Loading Dataset: {f} ---")
        data_frames.append(pd.read_csv(f))

if not data_frames:
    # Check archive as fallback
    ARCHIVE_DATA = 'data/archive/nbsl_multisector_gaia.csv'
    if os.path.exists(ARCHIVE_DATA):
        print(f"--- Loading Archive Dataset (V1.0): {ARCHIVE_DATA} ---")
        data_frames.append(pd.read_csv(ARCHIVE_DATA))
    else:
        print("CRITICAL ERROR: No datasets found in /data. Check file names.")
        exit()

# Combine all available star data
combined_data = pd.concat(data_frames)
real_coords = combined_data[['x_pc', 'y_pc', 'z_pc']].values
print(f"Total Nodal Vertices for Analysis: {len(real_coords)}")

# 2. REAL ANALYSIS
print("Analyzing real geometric distribution...")
obs_resonance = calculate_triplet_resonance(real_coords)

# 3. MONTE CARLO (Null Hypothesis Validation)
print("Starting Monte Carlo permutations (1000 iterations)...")
hits = 0
for i in range(1000):
    scrambled = real_coords.copy()
    # Destroy geometric structure by independent axis shuffling
    for col in range(3):
        np.random.shuffle(scrambled[:, col])
    
    s_resonance = calculate_triplet_resonance(scrambled)
    if s_resonance >= obs_resonance:
        hits += 1
    
    if (i+1) % 100 == 0: print(f"Progress: {i+1}/1000")

p_value = hits / 1000

print("-" * 30)
print(f"Observed Resonance (Signal): {obs_resonance}")
print(f"P-Value: {p_value}")

if p_value < 0.05:
    print("VERDICT: HIGH SIGNIFICANCE - Universal Geometric Matrix Confirmed (V4.0).")
else:
    print("VERDICT: Signal within stochastic noise. Further sampling required.")
