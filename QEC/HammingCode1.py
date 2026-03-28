#The (7, 4) Hamming Code

import numpy as np
from random import randint

def random_message(k):
    #Returns a 1xk array of random 0s and 1s
    return np.array([randint(0,1) for _ in range(k)], dtype=int)

#Generator matrix, G
G = np.array([
    [ 1 , 0 , 0 , 0 , 1 , 1 , 0 ],
    [ 0 , 1 , 0 , 0 , 1 , 0 , 1 ],
    [ 0 , 0 , 1 , 0 , 0 , 1 , 1 ],
    [ 0 , 0 , 0 , 1 , 1 , 1 , 1 ]], dtype=int)

def hamming_encode(message):
    #Matrix multiplication followed by modulo 2
    codeword = (message @ G) % 2
    return codeword

#Test the encoder
m = random_message(4)
c = hamming_encode(m)

print('Message (m): ', m)
print('Codeword (c):', c)
