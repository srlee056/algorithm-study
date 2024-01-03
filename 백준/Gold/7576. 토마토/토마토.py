import sys
from collections import deque

# n: 세로, m: 가로
m, n = map(int, sys.stdin.readline().split())


tomatoes = []
riped_tomatoes = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    tomatoes.append(row)


# y좌표, x좌표, 익은 날짜
riped_tomatoes = deque(
    [(i, j, 0) for i in range(n) for j in range(m) if tomatoes[i][j] == 1]
)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cur_datecount = -1
while riped_tomatoes:
    tmt = riped_tomatoes.popleft()
    cur_datecount = tmt[2]
    for _dx, _dy in zip(dx, dy):
        ty = tmt[0] + _dy
        tx = tmt[1] + _dx
        if tx >= 0 and tx < m and ty >= 0 and ty < n:
            if tomatoes[ty][tx] == 0:
                # 해당 좌표의 토마토가 익었음을 표시하고, riped_tomatoes에 좌표와 익은 날짜를 넘긴다.
                riped_tomatoes.append((ty, tx, cur_datecount + 1))
                tomatoes[ty][tx] = 1

# 만약 tomatoes 에 0 이 존재하는 채로 종료됐다면, 모두 익지 못하는 상황이므로 -1을 출력한다.
# 반복문 내부 tmt가 아닌 밖에 cur_datecount를 참고하여 런타임에러를 해결
result = cur_datecount
for row in tomatoes:
    if 0 in row:
        result = -1
        break

print(result)
