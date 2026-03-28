# (3, 1) Repetition Code

def repetition_decode(codeword):
    """
    Decodes a string by taking a majority vote for every 3-bit block.
    """
    estimated_message = ""
    
    # Step through the codeword in chunks of 3
    for i in range(0, len(codeword), 3):
        chunk = codeword[i : i + 3]
        
        # Majority vote: if there are more '1's than '0's, pick '1'
        if chunk.count('1') > chunk.count('0'):
            estimated_message += '1'
        else:
            estimated_message += '0'
            
    return estimated_message

#Test Script
from random import randint, random

def repetition_encode(data_stream):
    return "".join(bit * 3 for bit in data_stream)

message_length = 5
p = 0.1  # Probability of a bit flip

# 1.Create random message
message = ''.join([str(randint(0,1)) for i in range(message_length)])
print(f"Original Message:  {message}")

# 2.Encoding
codeword = repetition_encode(message)
print(f"Encoded Codeword:  {codeword}")

# 3.Simulate Noisy Channel(Corrupted bits)
corrupted_codeword = ''
for c in codeword:
    if random() < p:
        corrupted_codeword += '1' if c == '0' else '0'
    else:
        corrupted_codeword += c
print(f"Corrupted:         {corrupted_codeword}")

# 4.Decoding
estimated_message = repetition_decode(corrupted_codeword)
print(f"Estimated Message: {estimated_message}")
print(f"Success?           {message == estimated_message}")
