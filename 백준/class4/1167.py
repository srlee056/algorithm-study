import sys
from collections import deque


def dfs(node, tree, visited):
    max_node, max_cost = 0, 0
    for adj_node, cost in tree[node]:
        # print(visited)
        # print(adj_node, cost)
        if not visited[adj_node] and cost != -1:
            visited[adj_node] = True
            d_node, d_cost = dfs(adj_node, tree, visited)

            if d_cost != 0 and cost + d_cost > max_cost:
                max_node, max_cost = d_node, cost + d_cost
            elif cost > max_cost:
                max_node, max_cost = adj_node, cost
    return (max_node, max_cost)


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    tree = [[] for _ in range(n + 1)]

    for i in range(n):
        line = list(map(int, input().split()))

        # print(f"v: {line[0]}")
        cur_node = line[0]
        for adj_node, cost in zip(line[1::2], line[2::2]):
            tree[cur_node].append((adj_node, cost))

    # 1번 노드로부터 제일 먼 노드 찾기
    visited = [False for _ in range(n + 1)]
    visited[1] = True
    # print(n, visited)
    far_node, c = dfs(1, tree, visited)
    print(far_node, c)
    visited = [False for _ in range(n + 1)]
    visited[n] = True
    print(dfs(far_node, tree, visited)[1])
