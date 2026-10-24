n = int(input("Number of output fuzzy sets: "))

centre = []
weight = []

for i in range(n):
    centre.append(float(input("Enter centre: ")))

for i in range(n):
    weight.append(float(input("Enter weight: ")))

numerator = 0
denominator = 0

for i in range(n):
    numerator += weight[i] * centre[i]
    denominator += weight[i]

if denominator != 0:
    print("Weighted Average:", numerator / denominator)
else:
    print("Undefined")