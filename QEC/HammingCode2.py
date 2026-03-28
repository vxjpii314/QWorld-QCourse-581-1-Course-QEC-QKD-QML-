import numpy as np

#Parity-check matrix for Hamming code
H = np.array([
    [1, 1, 0, 1, 1, 0,0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]
], dtype=int)

error_syndromes = dict()

#Zero error case
s = np.array([0, 0, 0], dtype=int)
e = np.array([0, 0, 0, 0, 0, 0, 0], dtype=int)
error_syndromes[tuple(s)] = e
print(f"Zero error  -> syndrome: {s}, error: {e}")

#All single-bit error cases
for i in range(7):
    e = np.zeros(7, dtype=int)
    e[i] = 1                    # flip bit i
    s = H @ e % 2               # compute syndrome: s = H * e mod 2
    error_syndromes[tuple(s)] = e
    print(f"Bit {i} error -> syndrome: {s}, error: {e}")

print("\nFull error_syndromes dict:")
for syndrome, error in error_syndromes.items():
    print(f"  syndrome {syndrome} -> error {error}")
