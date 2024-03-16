import sys


def dfs(node, tree, visited):
    max_node, max_cost = 0, 0
    for adj_node, cost in tree[node]:
        if not visited[adj_node]:
            visited[adj_node] = True
            d_node, d_cost = dfs(adj_node, tree, visited)

            if d_node and d_cost:  # 둘 다 0이 아님
                if cost + d_cost > max_cost:
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

        cur_node = line[0]
        for adj_node, cost in zip(line[1::2], line[2::2]):
            tree[cur_node].append((adj_node, cost))
    # print(tree)
    # 1번 노드로부터 제일 먼 노드 찾기
    visited = [False for _ in range(n + 1)]
    visited[1] = True

    far_node, c = dfs(1, tree, visited)
    # print(far_node, c)
    visited = [False for _ in range(n + 1)]
    visited[far_node] = True
    print(dfs(far_node, tree, visited)[1])
