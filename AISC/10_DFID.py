#DFID
def dls(graph, node, goal, limit):
    print("Visiting:", node, "| Depth:", limit)

    if node == goal:
        print("Goal found:", node)
        return True

    if limit == 0:
        return False

    for child in graph[node]:
        if dls(graph, child, goal, limit - 1):
            return True

    print("Backtracking to:", node)

    return False

def dfid(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth limit:", depth)

        if dls(graph, start, goal, depth):
            return True

    return False

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    children = input("Enter children separated by space: ").split()
    graph[node] = children

start = input("Enter starting node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

if dfid(graph, start, goal, max_depth):
    print("\nGoal found")
else:
    print("\nGoal not found")