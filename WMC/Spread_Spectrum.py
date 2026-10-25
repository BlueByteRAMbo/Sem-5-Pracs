print("-"*40,"\nDSSS using Barker code\n","-"*40)

barker = "11100010010"

def encrypt(data):
    encrypted = ""
    for bit in data:
        for chip in barker:
            encrypted += str(int(bit)^int(chip))
    return encrypted

def decrypt(encrypted_data):
    decrypted = ""
    n = len(barker)
    for i in range(0,len(encrypted_data),n):
        block = encrypted_data[i : i + n]

        original = ""
        for j in range(n):
            original += str(int(block[j])^int(barker[j]))

        if original.count('1')>original.count('0'):
            decrypted += '1'
        else:
            decrypted += '0'
    return decrypted

data = input("Enter data: ")

encrypted = encrypt(data)
print("Encrypted data: ",encrypted)
decrypted = decrypt(encrypted)
print("Decrypted data: ",decrypted)
