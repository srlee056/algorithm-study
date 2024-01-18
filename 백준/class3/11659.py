import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

sums = [0]
# 시간 초과 기준 되게 빡빡하네...
for i, n in enumerate(numbers):
    sums.append(sums[i] + numbers[i])
    # sums.append(sum(numbers[i:])) -> 시간초과됨
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(sums[j] - sums[i - 1])
