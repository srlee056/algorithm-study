import sys
from collections import deque

# sys.setrecursionlimit(10000000)
n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0

cases = 0
while left <= right and right < n:
    sum_ = sum(numbers[left : right + 1])
    # print(left, right, sum_)
    if sum_ < m:
        right += 1
    else:  # sum_ >= m
        if sum_ == m:
            cases += 1
        if left + 1 > right:
            left, right = left + 1, left + 1
        else:
            left += 1

print(cases)
