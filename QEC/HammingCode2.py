import numpy as np

#Parity-check matrix for Hamming code
H = np.array([
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
], dtype=int)

#Build error_syndromes dict
error_syndromes = dict()

#Zero error case
s = np.array([0, 0, 0], dtype=int)
e = np.array([0, 0, 0, 0, 0, 0, 0], dtype=int)
error_syndromes[tuple(s)] = e

#All single-bit error cases
for i in range(7):
    e = np.zeros(7, dtype=int)
    e[i] = 1                    # flip bit i
    s = H @ e % 2               # compute syndrome: s = H * e mod 2
    error_syndromes[tuple(s)] = e

print("Error syndromes dict:")
for syndrome, error in error_syndromes.items():
    print(f"  syndrome {syndrome} -> error {error}")

#hamming_correct
def hamming_correct(corrupted_c):
    """
    Corrects a corrupted Hamming(7,4) codeword.

    Parameters
    ----------
    corrupted_c : numpy.ndarray, shape (1, 7), dtype=int
        A received (possibly corrupted) codeword containing only 0s and 1s.

    Returns
    -------
    numpy.ndarray, shape (1, 7), dtype=int
        The corrected codeword containing only 0s and 1s.
    """
    
    c_flat = corrupted_c.flatten()

    #Compute syndrome: s = H * c_tilda mod 2
    s = H @ c_flat % 2

    #Look up the error from the syndrome dict
    e = error_syndromes[tuple(s)]

    #Correct the codeword: c = c_tilda + e mod 2
    corrected = (c_flat + e) % 2

    #Reshape back to (1, 7) and return
    return corrected.reshape(1, 7)


#Test the results
print("\n--- Tests ---")

valid_c = np.array([[1, 0, 1, 1, 0, 0, 1]], dtype=int)

#Test 1: No error
print("\nTest 1: No error")
print("  Valid codeword:    ", valid_c)
print("  Corrected codeword:", hamming_correct(valid_c))
print("  Match original:    ", np.array_equal(hamming_correct(valid_c), valid_c))

#Test 2: Single-bit error at position 0
print("\nTest 2: Single-bit error at position 0")
corrupted_c = valid_c.copy()
corrupted_c[0, 0] ^= 1
print("  Corrupted codeword:", corrupted_c)
print("  Corrected codeword:", hamming_correct(corrupted_c))
print("  Match original:    ", np.array_equal(hamming_correct(corrupted_c), valid_c))

#Test 3: Single-bit error at position 3
print("\nTest 3: Single-bit error at position 3")
corrupted_c = valid_c.copy()
corrupted_c[0, 3] ^= 1
print("  Corrupted codeword:", corrupted_c)
print("  Corrected codeword:", hamming_correct(corrupted_c))
print("  Match original:    ", np.array_equal(hamming_correct(corrupted_c), valid_c))

#Test 4: Single-bit error at position 6
print("\nTest 4: Single-bit error at position 6")
corrupted_c = valid_c.copy()
corrupted_c[0, 6] ^= 1
print("  Corrupted codeword:", corrupted_c)
print("  Corrected codeword:", hamming_correct(corrupted_c))
print("  Match original:    ", np.array_equal(hamming_correct(corrupted_c), valid_c))
