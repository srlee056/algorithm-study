import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)


v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]

for i in range(e):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


count = 0
visited = [False for _ in range(v + 1)]

for i in range(1, v + 1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1

print(count)
