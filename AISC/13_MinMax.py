
def minmax(depth, node, is_max, values, max_depth,b):
    if depth == max_depth:
        return values[node]

    if is_max:
        best = -9999
        for i in range(b):
            best = max(best, minmax(depth+1, node*b + i, False,values, max_depth,b))
        print("At depth: ",depth,"Best val: ",best)
        return best
    
    else:
        best = 9999
        for i in range(b):
            best = min(best, minmax(depth+1, node*b + i, True, values, max_depth,b))
        print("At depth: ",depth,"Best val: ",best)
        return best

max_depth = int(input("Enter the maximum depth of the tree: "))
b = int(input("Enter no of children at each node: "))

no_of_leaves = b ** max_depth

values = []
for i in range(no_of_leaves):
    values.append(int(input(f"Enter value for leaf {i+1}: ")))

result = minmax(0,0,True,values,max_depth,b)
print(f"===========================\nThe best value is {result}")