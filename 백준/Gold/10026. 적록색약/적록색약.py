import sys
from collections import deque

# sys.setrecursionlimit(10000000)
n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    row = list(sys.stdin.readline().strip())
    arr.append(row)

visited = [[False] * n for _ in range(n)]
rg_visited = [[False] * n for _ in range(n)]

queue = deque([])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
rg_count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            queue.append((i, j))
            color = arr[i][j]
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny and ny < n and 0 <= nx and nx < n:
                        if arr[ny][nx] == color and not visited[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
            count += 1

        if not rg_visited[i][j]:
            queue.append((i, j))
            color = arr[i][j]
            if color == "B":
                colors = ["B"]
            else:
                colors = ["R", "G"]
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny and ny < n and 0 <= nx and nx < n:
                        if arr[ny][nx] in colors and not rg_visited[ny][nx]:
                            queue.append((ny, nx))
                            rg_visited[ny][nx] = True
            rg_count += 1

print(count, rg_count)
