import numpy as np

#Do parity check on matrix H
H = np.array([
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1]], dtype=int)

#Generator matrix, G
G = np.array([
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]], dtype=int)

#Calculate the product and apply modulo 2
#Note: G.T is the transpose of G
verification_result = (H @ G.T) % 2

print("Product (H @ G.T) mod 2:")
print(verification_result)

#Final check
if np.all(verification_result == 0):
    print("\nVerification successful HG^T = 0")
else:
    print("\nVerification failed: Non-zero product")
