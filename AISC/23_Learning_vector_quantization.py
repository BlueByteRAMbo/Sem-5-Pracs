W = [[0.2, 0.8], [0.7, 0.3]]
labels = [0, 1]
eta = 0.5

X = [[1, 0], [0, 1], [1, 1]]
T = [0, 1, 0]

for epoch in range(1, 4):
    print("Epoch:", epoch)

    for j in range(len(X)):
        x = X[j]
        target = T[j]
        distance = []

        for w in W:
            d = 0
            for i in range(len(x)):
                d += (x[i] - w[i]) ** 2
            distance.append(d)

        winner = distance.index(min(distance))

        for i in range(len(x)):
            if labels[winner] == target:
                W[winner][i] += eta * (x[i] - W[winner][i])
            else:
                W[winner][i] -= eta * (x[i] - W[winner][i])

        print("Input:", x, "Target:", target)
        print("Winner:", winner + 1)
        print("Weights:", W)

    print()