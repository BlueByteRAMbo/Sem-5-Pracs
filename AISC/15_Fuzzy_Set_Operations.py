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
difference=[]
bounded_sum=[]
bounded_difference=[]

for i in range(n):
    union.append(max(A[i],B[i]))
    intersection.append(min(A[i],B[i]))
    complement.append(1-A[i])
    algebric_product.append(A[i]*B[i])
    algebric_sum.append(A[i]+B[i]-A[i]*B[i])
    difference.append(min(A[i],1-B[i]))
    bounded_sum.append(min(1,A[i]+B[i]))
    bounded_difference.append(max(0,A[i]-B[i]))

print("Union: ", union)
print("Intersection: ", intersection)
print("Complement: ", complement)
print("Algebric Product: ", algebric_product)
print("Algebric Sum: ", algebric_sum)
print("Difference: ", difference)
print("Bounded Sum: ", bounded_sum)
print("Bounded Difference: ", bounded_difference)
