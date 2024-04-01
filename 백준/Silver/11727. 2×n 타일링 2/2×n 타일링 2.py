from sys import stdin
from collections import deque

n = int(stdin.readline())

ways = [0 for _ in range(1001)]

ways[1] = 1
ways[2] = 3

for i in range(3, 1001):
    ways[i] = (ways[i - 1] + ways[i - 2] * 2) % 10007


print(ways[n])
