import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

circle = deque([i for i in range(1, n + 1)])
removed = []

while circle:
    circle.rotate(-(k - 1))
    removed.append(circle.popleft())

print("<{}>".format(", ".join(map(str, removed))))
