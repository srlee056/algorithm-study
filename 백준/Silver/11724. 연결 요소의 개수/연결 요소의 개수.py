import sys

input = sys.stdin.readline

v, e = map(int, input().split())

edges = []
for _ in range(e):
    v1, v2 = map(int, input().split())
    edges.append((v1, v2))
# print(edges)
root_nodes = [i for i in range(v + 1)]


# 모든
def dfs_find(node, root_nodes):
    if root_nodes[node] != node:
        root_nodes[node] = dfs_find(root_nodes[node], root_nodes)
    return root_nodes[node]


visited = [False for _ in range(v + 1)]

while edges:
    v1, v2 = edges.pop()
    # print("---")
    # print(v1, v2)
    if visited[v1] and visited[v2] and root_nodes[v1] == root_nodes[v2]:

        continue

    r1 = dfs_find(v1, root_nodes)
    r2 = dfs_find(v2, root_nodes)

    # print(r1, r2)
    root_nodes[r2] = r1

for node in range(1, v + 1):
    dfs_find(node, root_nodes)

print(len(set(root_nodes[1:])))
