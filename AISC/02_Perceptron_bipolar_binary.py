W = [1.0,0.0,1.0]
eta = 0.1
bias = 0
X = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
T = [-1, -1, -1, -1, -1, -1, -1, 1]
epoch = 8

def f(net):
    return 1 if net >=0 else -1

count=0

while count<epoch:
    corrections = 0
    for i in range(len(X)):
        net = bias
        for j in range(len(X[0])):
            net += X[i][j]*W[j]
        y = f(net)

        for j in range(len(W)):
            W[j] = W[j] + eta*(T[i]-y)*X[i][j]

        bias = bias + eta*(T[i]-y)
        if y != T[i]:
            corrections += 1
        print(f"-----\nnet = {net}, f(net) = {y}")

    count += 1
    print("=======================================")
    print(f"After Epoch {count}: \nW = ", W, f"\nbias = {bias}")
    print(f"Total corrections made in this epoch: {corrections}")
    print("=======================================")
    if corrections == 0:
        print("Training complete. No corrections needed.")
        print("=======================================")
        break
