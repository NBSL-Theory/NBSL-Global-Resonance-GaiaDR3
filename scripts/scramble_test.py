import numpy as np
import pandas as pd

# NBSL THEORY - MONTE CARLO VALIDATION V3.0
# Testing 120° Resonance against 1000 random permutations.

def calculate_triplet_angles(coords):
    n = len(coords)
    angles = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a = np.linalg.norm(coords[j]-coords[k])
                b = np.linalg.norm(coords[i]-coords[k])
                c = np.linalg.norm(coords[i]-coords[j])
                cos_a = np.clip((b**2 + c**2 - a**2) / (2 * b * c), -1, 1)
                angles.append(np.degrees(np.arccos(cos_a)))
    return np.array(angles)

# Carregar dados
data = pd.read_csv('data/nbsl_multisector_gaia.csv')
real_coords = data[['x_pc', 'y_pc', 'z_pc']].values

# 1. Análise Real
real_angles = calculate_triplet_angles(real_coords)
obs_resonance = np.sum((real_angles >= 119.9) & (real_angles <= 120.1))

# 2. Monte Carlo (1000 iterações)
hits = 0
for _ in range(1000):
    scrambled = real_coords.copy()
    np.random.shuffle(scrambled)
    s_angles = calculate_triplet_angles(scrambled)
    s_resonance = np.sum((s_angles >= 119.9) & (s_angles <= 120.1))
    if s_resonance >= obs_resonance:
        hits += 1

p_value = hits / 1000
print(f"Resonância Observada: {obs_resonance}")
print(f"P-Value: {p_value}") # Se P < 0.05, o crítico perde o argumento.
 
