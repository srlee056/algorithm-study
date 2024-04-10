import sys
from collections import defaultdict, deque


def main():
    n = int(sys.stdin.readline().strip())
    edges = defaultdict(list)
    arr = []
    for i in range(n):
        row = map(int, sys.stdin.readline().split())
        for j, num in enumerate(row):
            if num == 1:
                edges[i].append(j)
        arr.append(row)
    # print(edges)

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        visited = [False for _ in range(n)]
        points = deque(edges[i])
        while points:
            p = points.popleft()
            if visited[p]:
                continue
            result[i][p] = 1
            visited[p] = True
            points.extend(edges[p])

    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
