import math
W = [1.0,-1.0]
eta = 1.0
bias = 0
X = [[1.0,-2.0],[0.0,1.0],[2.0,3.0],[1.0,-1.0]]
epoch = 3

def f(net):
    return (1 - math.exp(-net))/(1 + math.exp(-net))

count=0

while count<epoch:
    for i in range(len(X)):
        net = bias
        for j in range(len(X[0])):
            net += X[i][j]*W[j]
        y = f(net)

        for j in range(len(W)):
            W[j] = W[j] + eta*y*X[i][j]

        bias = bias + eta*y
        print(f"-----\nnet = {net}, f(net) = {y}")

    count += 1
    print(f"=====\nAfter Epoch {count}:\nW = ", W, f", bias = {bias}")

