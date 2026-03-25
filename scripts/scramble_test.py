import numpy as np
import pandas as pd
import os

# NBSL THEORY - MONTE CARLO VALIDATION V3.1 (High-Performance Edition)
# Optimized for N=670 dataset and backward compatibility.

def calculate_triplet_resonance(coords, iterations=10000):
    """Calcula a ressonância de 120° usando amostragem estatística para eficiência."""
    n = len(coords)
    count = 0
    for _ in range(iterations):
        # Seleciona 3 estrelas aleatórias do dataset
        idx = np.random.choice(n, 3, replace=False)
        p1, p2, p3 = coords[idx]
        
        # Lados do triângulo
        a = np.linalg.norm(p2 - p3)
        b = np.linalg.norm(p1 - p3)
        c = np.linalg.norm(p1 - p2)
        
        # Lei dos Cossenos para o ângulo em p1
        denominator = 2 * b * c
        if denominator == 0: continue
        cos_a = np.clip((b**2 + c**2 - a**2) / denominator, -1, 1)
        angle = np.degrees(np.arccos(cos_a))
        
        # Filtro de Ressonância Nodal (Tolerância de 0.1°)
        if 119.9 <= angle <= 120.1:
            count += 1
    return count

# 1. LOCALIZAÇÃO ROBUSTA DOS DADOS
PRIMARY_DATA = 'data/gaia_pleiades_full_670.csv'
ARCHIVE_DATA = 'data/archive/nbsl_multisector_gaia.csv'

if os.path.exists(PRIMARY_DATA):
    print(f"--- Loading V3.1 Dataset: {PRIMARY_DATA} ---")
    data = pd.read_csv(PRIMARY_DATA)
elif os.path.exists(ARCHIVE_DATA):
    print(f"--- Loading Archive Dataset (V1.0): {ARCHIVE_DATA} ---")
    data = pd.read_csv(ARCHIVE_DATA)
else:
    print("CRITICAL ERROR: No dataset found. Please check /data folder.")
    exit()

# Extração de coordenadas (x, y, z em parsecs)
real_coords = data[['x_pc', 'y_pc', 'z_pc']].values

# 2. ANÁLISE REAL
print("Analyzing real geometric distribution...")
obs_resonance = calculate_triplet_resonance(real_coords)

# 3. MONTE CARLO (Validação de Hipótese Nula)
print("Starting Monte Carlo permutations (1000 iterations)...")
hits = 0
for i in range(1000):
    scrambled = real_coords.copy()
    # Scramble: baralhar coordenadas para destruir a estrutura geométrica
    for col in range(3):
        np.random.shuffle(scrambled[:, col])
    
    s_resonance = calculate_triplet_resonance(scrambled)
    if s_resonance >= obs_resonance:
        hits += 1
    
    if (i+1) % 100 == 0: print(f"Progress: {i+1}/1000")

p_value = hits / 1000

print("-" * 30)
print(f"Resonância Observada (Sinal): {obs_resonance}")
print(f"P-Value: {p_value}")
if p_value < 0.01:
    print("VERDICT: HIGH SIGNIFICANCE - Geometric Matrix Hypothesis Confirmed.")
else:
    print("VERDICT: Null Hypothesis cannot be rejected.")
