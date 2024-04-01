from sys import stdin
from collections import deque

n = int(stdin.readline())


arr = []
for _ in range(n):
    arr.append(list(map(int, list(stdin.readline().strip()))))
# print(arr)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

counts = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            count = 0
            queue = deque([(i, j)])
            arr[i][j] = 0
            while queue:
                y, x = queue.popleft()
                count += 1
                for k in range(4):
                    if (
                        0 <= y + dy[k] < n
                        and 0 <= x + dx[k] < n
                        and arr[y + dy[k]][x + dx[k]] == 1
                    ):
                        queue.append((y + dy[k], x + dx[k]))
                        arr[y + dy[k]][x + dx[k]] = 0

            counts.append(count)
counts.sort()

print(len(counts))
for c in counts:
    print(c)
