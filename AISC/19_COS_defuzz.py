n = int(input("Number of output fuzzy sets: "))

centre = []
area = []

for i in range(n):
    centre.append(float(input("Enter centroid: ")))

for i in range(n):
    area.append(float(input("Enter implied area: ")))

numerator = 0
denominator = 0

for i in range(n):
    numerator += area[i] * centre[i]
    denominator += area[i]

if denominator != 0:
    print("Centre of Sums:", numerator / denominator)
else:
    print("Undefined")