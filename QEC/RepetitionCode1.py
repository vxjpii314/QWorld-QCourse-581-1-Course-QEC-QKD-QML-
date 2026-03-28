def repetition_encode(data_stream):
    # Triple each bit to create the codeword
    return "".join(bit * 3 for bit in data_stream)

# Test the solution
k = 3
for i in range(2**k):
    message = bin(i)[2:].zfill(k)
    codeword = repetition_encode(message)
    print(f"Message: {message} -> Codeword: {codeword}")
