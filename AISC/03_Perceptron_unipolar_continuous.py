import math

W = [1.0,0.0,1.0]
eta = 0.1
bias = 0
X = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
T = [0, 0, 0, 0, 0, 0, 0, 1]
epoch = 500

def f(net):
    return 1 / (1 + math.exp(-net))

def f_dash(y):
    return y * (1 - y)

count=0

while count<epoch:
    total_error = 0
    for i in range(len(X)):
        net = bias
        for j in range(len(X[0])):
            net += X[i][j]*W[j]
        y = f(net)

        for j in range(len(W)):
            W[j] = W[j] + eta*(T[i]-y)*f_dash(y)*X[i][j]

        bias = bias + eta*(T[i]-y)*f_dash(y)

        total_error += (T[i]-y)**2
        
        print(f"-----\nnet = {net}, f(net) = {y}")

    count += 1
    print("=======================================")
    print(f"After Epoch {count}: \nW = ", W, f"\nbias = {bias}")
    print(f"Total error in this epoch: {total_error}")
    print("=======================================")
    
