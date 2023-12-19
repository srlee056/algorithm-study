import sys

n, m = map(int, sys.stdin.readline().split())


points = []
for _ in range(n):
    temp_list = list(map(int, sys.stdin.readline().split()))
    points.append(temp_list)

    # n x n 각 point에 1,1~ i, j 누적합을 계산한다
    # x1, y1 -> x2, y2 계산은 (x1-1, n) + (n, y1-1)-(x1-1, y1-1)
    # 내일 이 시간에 풀어볼 것

    print(sum)
