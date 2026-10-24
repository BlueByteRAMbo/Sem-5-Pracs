W = [[0.2, 0.8], [0.7, 0.3]]
eta = 0.5

X = [[1, 0], [0, 1], [1, 1]]

for epoch in range(1, 4):
    print("Epoch:", epoch)

    for x in X:
        net = []

        for w in W:
            value = 0

            for i in range(len(x)):
                value += x[i] * w[i]

            net.append(value)

        winner = net.index(max(net))

        for i in range(len(x)):
            W[winner][i] += eta * (x[i] - W[winner][i])

        print("Input:", x)
        print("Net values:", net)
        print("Winner neuron:", winner + 1)
        print("Updated weights:", W)

    print()