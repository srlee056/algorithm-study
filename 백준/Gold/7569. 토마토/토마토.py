from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())

tmt_boxes = [[] for _ in range(h)]

for i in range(h):
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        tmt_boxes[i].append(row)

# print(tmt_boxes)

riped_tmts = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmt_boxes[i][j][k] == 1:
                riped_tmts.append((0, i, j, k))

# print(riped_tmts)

di = [0, 0, 0, 0, 1, -1]
dj = [0, 0, 1, -1, 0, 0]
dk = [1, -1, 0, 0, 0, 0]


while riped_tmts:
    day, i, j, k = riped_tmts.popleft()
    for t in range(6):
        ni, nj, nk = i + di[t], j + dj[t], k + dk[t]
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m:
            if tmt_boxes[ni][nj][nk] == 0:
                tmt_boxes[ni][nj][nk] = 1
                riped_tmts.append((day + 1, ni, nj, nk))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tmt_boxes[i][j][k] == 0:
                day = -1
print(day)
