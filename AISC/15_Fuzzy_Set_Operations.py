import matplotlib.pyplot as plt

n = int(input("Enter the number of elements: "))

A = []
B = []

for i in range(n):
    A.append(float(input("Enter the value of A: ")))

for i in range(n):
    B.append(float(input("Enter the value of B: ")))

union = []
intersection=[]
complement=[]
algebric_product=[]
algebric_sum=[]

for i in range(n):
    union.append(max(A[i],B[i]))
    intersection.append(min(A[i],B[i]))
    complement.append(1-A[i])
    algebric_product.append(A[i]*B[i])
    algebric_sum.append(A[i]+B[i]-A[i]*B[i])

x = list(range(1,n+1))

plt.plot(x,A,marker='o',label='Set_A')
plt.plot(x,B,marker='o',label='Set_B')
plt.plot(x,union,marker='o',label='union')
plt.plot(x,intersection,marker='o',label='intersection')
plt.plot(x,complement,marker='o',label='complement')
plt.plot(x,algebric_product,marker='o',label='algebric_product')
plt.plot(x,algebric_sum,marker='o',label='algebric_sum')

plt.xlabel('Values')
plt.ylabel('Menbership valuse')
plt.ylim(0,1)
plt.xticks(x)
plt.legend()
plt.grid()
plt.show()
