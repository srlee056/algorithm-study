import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

sums = [0]
for i, n in enumerate(numbers):
    sums.append(sums[i] + numbers[i])

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(sums[j] - sums[i - 1])
