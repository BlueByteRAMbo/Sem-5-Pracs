n = int(input("Number of sample points: "))

x = []
membership = []

for i in range(n):
    x.append(float(input("Enter x value: ")))

for i in range(n):
    membership.append(float(input("Enter membership value: ")))

best = 0

for i in range(1, n):
    if membership[i] > membership[best]:
        best = i

print("Height Defuzzification:", x[best])