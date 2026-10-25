
print("Note: \nLeft-to-right: \nP1, P2, D0, P4, D1, D2, D3, P8, D4, D5, D6, D7, D8, D9, D10, P0\n"
      "Right-to-left: \nP0, D10, D9, D8, D7, D6, D5, D4, P8, D3, D2, D1, P4, D0, P2, P1. "
      "This program uses the RIGHT-TO-LEFT convention (P1 is the rightmost bit, P0 the leftmost).")
print("Data is entered as D10 ... D0 (leftmost bit = D10, rightmost bit = D0).")
print("Error position is the Hamming position: 1 = P1 (rightmost) ... 16 = P0 (leftmost).\n")

data = input("Enter 11 data bits (add leading zeros if data is less than 11 bits, eg: for 101, enter 00000000101):")

if len(data) != 11 or any(bit not in "01" for bit in data):
    print("Enter exactly 11 binary bits.")
    exit()

bits = [0] * 17
data_positions = [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]

# Place data bits from right to left
for data_index in range(11):
    bits[data_positions[data_index]] = int(data[10 - data_index])

# Calculate Hamming parity bits
for parity_position in [1, 2, 4, 8]:
    for bit_position in range(1, 16):
        if bit_position & parity_position and bit_position != parity_position:
            bits[parity_position] ^= bits[bit_position]

# Calculate overall parity bit
for bit_position in range(1, 16):
    bits[16] ^= bits[bit_position]

# Display code from left to right
print("SECDED Code:", end=" ")
for bit_position in range(16, 0, -1):
    print(bits[bit_position], end="")
print()

# Receive codeword at the receiver
received_codeword = input("Enter received 16-bit codeword: ")

if len(received_codeword) != 16 or any(bit not in "01" for bit in received_codeword):
    print("Enter exactly 16 binary bits.")
    exit()

# Convert received codeword into Hamming positions
received_bits = [0] * 17
for bit_position in range(1, 17):
    received_bits[bit_position] = int(received_codeword[16 - bit_position])

# Calculate syndrome
syndrome = 0
for parity_position in [1, 2, 4, 8]:
    calculated_parity = 0
    for bit_position in range(1, 16):
        if bit_position & parity_position:
            calculated_parity ^= received_bits[bit_position]
    if calculated_parity:
        syndrome += parity_position

# Check overall parity
overall_parity = 0
for bit_position in range(1, 17):
    overall_parity ^= received_bits[bit_position]

# Detect and correct error
if syndrome == 0 and overall_parity == 0:
    print("No error detected")
elif syndrome != 0 and overall_parity == 1:
    print("Single-bit error at position:", syndrome)
    received_bits[syndrome] ^= 1
elif syndrome == 0 and overall_parity == 1:
    print("Error at overall parity position 16")
    received_bits[16] ^= 1
else:
    print("Double-bit error detected; cannot correct")

# Display final code
print("Final code:", end=" ")
for bit_position in range(16, 0, -1):
    print(received_bits[bit_position], end="")
print()

# Recover original data
print("Data bits:", end=" ")
for data_position in reversed(data_positions):
    print(received_bits[data_position], end="")
print()
