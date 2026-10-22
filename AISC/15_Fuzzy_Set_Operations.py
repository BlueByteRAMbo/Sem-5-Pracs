import matplotlib.pyplot as plt

n = int(input("Enter no of elements: "))

A = [0.2,0.5,0.8,0.4,0.9]
B = [0.1,0.7,0.6,0.3,0.2]

print("FUzzy Operations on A and B: ")

union = []
intersection = []
complement_A = []
complement_B = []
algebraic_sum = []
algebraic_product = []

for i in range(n):
    union.append(max(A[i],B[i]))
    intersection.append(min(A[i],B[i]))
    complement_A.append(1-A[i])
    complement_B.append(1-B[i])
    algebraic_product.append(A[i]*B[i])
    algebraic_sum.append(A[i] + B[i] - A[i]*B[i])

x = list(range(1,n+1))

plt.plot(x,A,marker='o',label='Set_A')
plt.plot(x,B,marker='o',label='Set_B')

plt.plot(x,union,marker='o',label='A U B')

# plt.plot(x,intersection,marker='o',label='A n B')

# plt.plot(x,complement_A,marker='o',label='Complement_A')

# plt.plot(x,complement_B,marker='o',label='Complement_B')

# plt.plot(x,algebraic_product,marker='o',label='A * B')

# plt.plot(x,algebraic_sum,marker='o',label='A + B')

plt.title('Fuzzy Set Operations')
plt.xlabel('Values')
plt.ylabel('Membership Values')
plt.xticks(x)
plt.ylim(0,1)
plt.legend()
plt.grid(True)
plt.show()