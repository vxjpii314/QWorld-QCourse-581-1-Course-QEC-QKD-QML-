import numpy as np

#Quick test of modulo arithmetic
print(f"Basic mod check: (1 + 1) % 2 = {(1 + 1) % 2}\n")

#Initialize matrix and vector using integers to avoid float defaults
mat_a = np.array([[1, 0], [1, 1]], dtype=int)
vec_b = np.array([1, 1], dtype=int)

print("Matrix A:\n", mat_a, "\n")

#Standard addition results in values outside GF(2)
print("Standard addition (M+M):\n", mat_a + mat_a)
print("Note: '2' is invalid in a binary system.\n")

# Use modulo 2 to keep values within the {0, 1} range
print("Corrected addition ((M+M) % 2):\n", (mat_a + mat_a) % 2)

print("-" * 10)
print("Vector b:", vec_b)

#Matrix-vector multiplication followed by a modulo operation
#Using @ for dot product; % 2 ensures the result is binary
raw_prod = mat_a @ vec_b
print("Raw product (M@v):", raw_prod)
print("Binary product (M@v % 2):", raw_prod % 2)
