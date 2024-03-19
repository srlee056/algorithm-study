import sys
from collections import deque

n, m = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(nodes, maze_array, visited):
    global n, m
    dists = []
    while nodes:
        y, x, dist = nodes.popleft()
        if (y, x) == (n - 1, m - 1):
            dists.append(dist)
            continue
        for i in range(4):
            adj_y, adj_x = y + dy[i], x + dx[i]

            if adj_y < 0 or adj_y >= n or adj_x < 0 or adj_x >= m:
                continue
            if visited[adj_y][adj_x]:
                continue
            if maze_array[adj_y][adj_x] == 0:
                continue

            nodes.append([adj_y, adj_x, dist + 1])
            if (y, x) != (n - 1, m - 1):
                visited[adj_y][adj_x] = True
    # print(dists)
    return min(dists)


def main():
    global n, m
    input = sys.stdin.readline

    n, m = map(int, input().split())

    maze_array = []
    for _ in range(n):
        input_list = list(map(int, input().strip()))
        maze_array.append(input_list)

    # print(maze_array)

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    print(bfs(deque([[0, 0, 1]]), maze_array, visited))


if __name__ == "__main__":
    main()
