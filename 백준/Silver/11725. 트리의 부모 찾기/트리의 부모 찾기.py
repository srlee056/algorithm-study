import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

edges = {}
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    edges[v1] = edges.get(v1, [])
    edges[v1].append(v2)
    edges[v2] = edges.get(v2, [])
    edges[v2].append(v1)

parent_nodes = {1: 0}
parents = deque([1])
while parents:
    parent = parents.popleft()
    children = edges[parent]
    for child in children:
        if child not in parent_nodes:
            parent_nodes[child] = parent
            parents.append(child)

for i in range(2, n + 1):
    print(parent_nodes[i])