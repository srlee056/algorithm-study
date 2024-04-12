import sys
from collections import defaultdict, deque


def main():

    n, m = map(int, sys.stdin.readline().split())

    ladders = {}
    snakes = {}

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        ladders[x] = y

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        snakes[x] = y

    # print(ladders)
    # print(snakes)

    board = deque([(1, 0)])
    visited = [-1 for _ in range(101)]
    while board:
        pos, count = board.popleft()
        # print(pos, count)

        if pos == 100:
            print(count)
            break
        if pos in ladders:
            if visited[ladders[pos]] == -1 or visited[ladders[pos]] > count:
                board.appendleft((ladders[pos], count))
                visited[ladders[pos]] = count
        elif pos in snakes:
            if visited[snakes[pos]] == -1 or visited[snakes[pos]] > count:
                board.appendleft((snakes[pos], count))
                visited[snakes[pos]] = count
        else:
            for k in range(1, 7):
                if pos + k <= 100:
                    if visited[pos + k] == -1 or visited[pos + k] > count + 1:
                        board.append((pos + k, count + 1))
                        visited[pos + k] = count + 1


if __name__ == "__main__":
    main()
