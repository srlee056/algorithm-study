import sys
from collections import deque


def main():
    cases = int(sys.stdin.readline().strip())

    for _ in range(cases):
        m, n, x, y = map(int, sys.stdin.readline().split())

        result = -1
        for i in range(n):
            if (m * i + x - y) % n == 0:
                result = m * i + x
                break

        print(result)


if __name__ == "__main__":
    main()
