from sys import stdin
from collections import deque

test = int(stdin.readline())

ns = []

for _ in range(test):
    ns.append(int(stdin.readline()))

ps = [0 for i in range(101)]

ps[1], ps[2], ps[3] = 1, 1, 1
ps[4], ps[5] = 2, 2

for i in range(5, 101):
    ps[i] = ps[i - 1] + ps[i - 5]

for n in ns:
    print(ps[n])
