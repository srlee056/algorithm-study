import sys
from collections import defaultdict, deque


def main():

    n, m = map(int, sys.stdin.readline().split())
    pwds = {}
    for _ in range(n):
        site, pwd = sys.stdin.readline().split()
        pwds[site] = pwd

    for _ in range(m):
        site = sys.stdin.readline().strip()
        print(pwds[site])


if __name__ == "__main__":
    main()
