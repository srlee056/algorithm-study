import sys
from collections import deque


def bfs(start_node, maze_array):
    n, m = len(maze_array), len(maze_array[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_node[0]][start_node[1]] = True
    nodes = deque([start_node])

    while nodes:
        y, x, dist = nodes.popleft()
        if (y, x) == (n - 1, m - 1):
            return dist
        for i in range(4):
            adj_y, adj_x = y + dy[i], x + dx[i]

            if (
                0 <= adj_y < n
                and 0 <= adj_x < m
                and not visited[adj_y][adj_x]
                and maze_array[adj_y][adj_x] == 1
            ):
                # 첫번째로 도착한 거리가 최단거리이므로, 도착점을 여러번 방문하는 것에 대해 고려할 필요 없음.
                visited[adj_y][adj_x] = True
                nodes.append([adj_y, adj_x, dist + 1])

    return -1


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    maze_array = []
    for _ in range(n):
        input_list = list(map(int, input().strip()))
        maze_array.append(input_list)

    print(bfs(deque([0, 0, 1]), maze_array))


if __name__ == "__main__":
    main()
