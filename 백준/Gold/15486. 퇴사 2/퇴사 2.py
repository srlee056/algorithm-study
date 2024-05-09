import sys
from collections import defaultdict, deque


def main():
    n = int(sys.stdin.readline().strip())

    profits = [0 for _ in range(n + 1)]
    for i in range(n):
        t, p = map(int, sys.stdin.readline().split())
        profits[i] = max(profits[i], profits[i - 1])
        if i + t <= n:
            profits[i + t] = max(profits[i + t], profits[i] + p)
    # print(profits)
    print(max(profits[-2:]))


if __name__ == "__main__":
    main()
