import sys
from collections import defaultdict, deque


def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())

    costs = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        costs[i][i] = 0

    for _ in range(m):
        from_, to_, cost_ = map(int, sys.stdin.readline().split())
        if costs[from_][to_] == -1 or costs[from_][to_] > cost_:
            costs[from_][to_] = cost_

    start, end = map(int, sys.stdin.readline().split())
    # print(costs)
    visited = [False for _ in range(n + 1)]

    def get_min_cost(node):
        min_cost = -1
        min_index = 0
        for i in range(1, n + 1):
            if not visited[i]:
                if costs[node][i] != -1 and (
                    min_cost > costs[node][i] or min_cost == -1
                ):
                    min_cost = costs[node][i]
                    min_index = i

        return min_index

    # print(costs)
    visited[start] = True
    while True:
        next_node = get_min_cost(start)
        if next_node == 0:
            break
        visited[next_node] = True
        # print(next_node)
        for i in range(1, n + 1):
            if costs[next_node][i] != -1:
                if (
                    costs[start][i] == -1
                    or costs[start][i] > costs[start][next_node] + costs[next_node][i]
                ):
                    costs[start][i] = costs[start][next_node] + costs[next_node][i]
        # print(costs)
    # print(costs)
    print(costs[start][end])


if __name__ == "__main__":
    main()
