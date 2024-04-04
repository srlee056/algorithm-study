import sys
from collections import deque

sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())

arr = []
f_queue = deque([])
for i in range(n):
    row = list(sys.stdin.readline().strip())
    arr.append(row)
    for j, cell in enumerate(row):
        if cell == "J":
            pos = (i, j)
        if cell == "F":
            f_queue.append((i, j))
            arr[i][j] = 0


# fires = [row[:] for row in arr]
# print(f_queue)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while f_queue:
    fy, fx = f_queue.popleft()

    for k in range(4):
        ny, nx = fy + dy[k], fx + dx[k]
        if 0 <= ny and ny < n and 0 <= nx and nx < m:
            if arr[ny][nx] == "." or arr[ny][nx] == "J":
                arr[ny][nx] = arr[fy][fx] + 1
                f_queue.append((ny, nx))

# print(arr)

queue = deque([(pos[0], pos[1])])

visited_time = [[0] * m for _ in range(n)]
# print(visited_time)
can_escape = False
while queue:
    y, x = queue.popleft()
    # print("popped", visited_time[y][x], y, x)
    if (y == 0 or y == n - 1) or (x == 0 or x == m - 1):
        can_escape = True
        print(visited_time[y][x] + 1)
        break
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny and ny < n and 0 <= nx and nx < m:
            if arr[ny][nx] != "#":
                # print(arr[ny][nx])
                if (
                    arr[ny][nx] in [".", "J"] or arr[ny][nx] > visited_time[y][x] + 1
                ) and visited_time[ny][nx] == 0:
                    visited_time[ny][nx] = visited_time[y][x] + 1
                    queue.append((ny, nx))
                    # print("added", visited_time[ny][nx], ny, nx)

if not can_escape:
    print("IMPOSSIBLE")
