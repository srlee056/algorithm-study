import sys
from collections import deque

# sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# print(arr)


# store each picture's size
pictures = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        points = deque([])
        count = 0
        if arr[i][j] == 1:
            points.append((i, j))
            arr[i][j] = 0
            while points:
                y, x = points.popleft()
                count += 1
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny and ny < n and 0 <= nx and nx < m:
                        if arr[ny][nx] == 1:
                            points.append((ny, nx))
                            arr[ny][nx] = 0
            pictures.append(count)
# print(pictures)
print(len(pictures))
if len(pictures) == 0:
    print(0)
else:
    print(max(pictures))
