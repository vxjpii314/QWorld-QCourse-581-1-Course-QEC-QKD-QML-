import numpy as np

def noise_channel(c, p):
    """
    Simulates a noisy channel by flipping bits with probability p.
    """
    #Create a 'flip mask' where 1 means flip and 0 means stay the same
    #np.random.random generates floats in [0.0, 1.0)
    flip_mask = (np.random.random(c.shape) < p).astype(int)
    
    #Use modulo 2 addition to flip the bits
    return (c + flip_mask) % 2

def random_message(k):
    return np.array([np.random.randint(0, 2) for _ in range(k)], dtype=int).reshape(1, k)

#Test the channel
c = random_message(7)
corrupted_c = noise_channel(c, 0.5)

print('Original c: ', c)
print('Corrupted c:', corrupted_c)
