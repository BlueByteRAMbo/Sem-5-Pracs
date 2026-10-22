#DLS
def dls(graph,node,goal,limit):
    print("Current Node: ", node, " Limit: ", limit)
    if node == goal:
        return True

    if limit == 0:
        return False

    for child in graph[node]:
        if dls(graph,child,goal,limit-1):
            return True
    return False

graph = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("Enter the node: ")
    childern = input("Enter childern separted by space: ").split()
    graph[node] = childern

start = input("Enter the starting node: ")
goal = input("Enter the goal: ")
limit = int(input("Enter the limit: "))

if dls(graph,start,goal,limit):
    print("Goal Found")
else:
    print("Not Found")