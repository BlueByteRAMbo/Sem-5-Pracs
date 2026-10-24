n = int(input("Number of sample points: "))

x = []
membership = []

for i in range(n):
    x.append(float(input("Enter x value: ")))

for i in range(n):
    membership.append(float(input("Enter membership value: ")))

numerator = 0
denominator = 0

for i in range(n):
    numerator += x[i] * membership[i]
    denominator += membership[i]

if denominator != 0:
    print("Centroid:", numerator / denominator)
else:
    print("Undefined")