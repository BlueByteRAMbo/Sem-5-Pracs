import hashlib

def hash_value(data):
    return hashlib.sha256(data.encode()).hexdigest()

def A3(Ki,RAND):
    return hash_value(str(Ki) + ":" + str(RAND))

def A8(Ki,RAND):
    return hash_value(str(Ki) + ":" + str(RAND) + ":A8")

def A5(message,Kc):
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr( ord(message[i]) ^ ord(Kc[ i % len(Kc) ]))
    return encrypted

Ki = "123"
RAND = "45"
data = "Hello"
SRES = A3(Ki,RAND)
Kc = A8(Ki,RAND)

expected_SRES = A3(Ki,RAND)

print("SRES: ", SRES)
print("Kc: ",Kc)

if SRES == expected_SRES:
    print("Authentication Successful")
    encrypted = A5(data,Kc)
    print("Encrypted: ",repr(encrypted))
else:
    print("Authentication Failed!!!")
