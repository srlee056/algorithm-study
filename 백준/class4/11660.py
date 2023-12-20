import sys

n, m = map(int, sys.stdin.readline().split())


points = []
for _ in range(n):
    temp_list = list(map(int, sys.stdin.readline().split()))
    points.append(temp_list)

    # n x n 각 point에 1,1~ i, j 누적합을 계산한다
    # x1, y1 -> x2, y2 계산은 (x1-1, n) + (n, y1-1)-(x1-1, y1-1)
    # 내일 이 시간에 풀어볼 것

sums = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        sum = points[i][j]

        sum = sum + sums[i - 1][j] if i >= 1 else sum
        sum = sum + sums[i][j - 1] if j >= 1 else sum
        sum = sum - sums[i - 1][j - 1] if i >= 1 and j >= 1 else sum

        sums[i][j] = sum

# print(sums)

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = sums[x2 - 1][y2 - 1]
    # print(result, sums[x2 - 1][y1 - 2], sums[x1 - 2][y2 - 1], sums[x1 - 2][y1 - 2])

    if x1 == 1 and y1 > 1:
        result = result - sums[x2 - 1][y1 - 2]
    elif y1 == 1 and x1 > 1:
        result = result - sums[x1 - 2][y2 - 1]
    elif x1 > 1 and y1 > 1:
        result = (
            result - sums[x2 - 1][y1 - 2] - sums[x1 - 2][y2 - 1] + sums[x1 - 2][y1 - 2]
        )

    print(result)
