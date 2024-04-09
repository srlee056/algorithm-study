import sys
from collections import deque


def main():
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        from_, to_ = map(int, sys.stdin.readline().split())
        visited = [False for _ in range(10000)]
        queue = deque([("", from_)])
        visited[from_] = True
        while queue:
            commands, num = queue.popleft()
            if num == to_:
                print(commands)
                break

            operations = [
                ("L", to_left(num)),
                ("R", to_right(num)),
                ("D", double(num)),
                ("S", subtract(num)),
            ]

            for command, new_num in operations:
                if not visited[new_num]:
                    visited[new_num] = True
                    queue.append((commands + command, new_num))


def to_left(number):
    return number % 1000 * 10 + number // 1000


def to_right(number):
    return number % 10 * 1000 + number // 10


def double(number):
    return number * 2 % 10000


def subtract(number):
    return (number - 1) % 10000


if __name__ == "__main__":
    main()
