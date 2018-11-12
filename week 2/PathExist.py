import sys

def reach(nodes, x, y):
    neighbours = nodes[x]['neighbours']
    nodes[x]['visited'] = True
    if y in neighbours:
        return 1
    for node in neighbours:
        reach(nodes, node, y)
    return 0

input = sys.stdin.read()
data = list(map(int, input.split()))
n, m = data[0:2]
data = data[2:]
edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
x, y = data[2*m:]
x, y = x -1, y -1
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
nodes = list({'visited': False, 'neighbours': neighbours} for neighbours in adj)
print(reach(nodes, x, y))

