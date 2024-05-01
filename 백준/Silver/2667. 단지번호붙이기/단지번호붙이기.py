import sys
from collections import defaultdict, deque


def main():

    n = int(sys.stdin.readline().strip())

    arr = []
    for _ in range(n):
        row = list(map(int, list(sys.stdin.readline().strip())))
        arr.append(row)

    visited = [[False] * n for _ in range(n)]
    number_of_apts = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                number_of_apts.append(find_connected_cells(arr, visited, i, j))

    print(len(number_of_apts))
    for number in sorted(number_of_apts):
        print(number)

    # return count


def find_connected_cells(arr, visited, i, j):
    n = len(arr)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(i, j)])
    visited[i][j] = True
    count = 1
    while queue:
        y, x = queue.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    count += 1

    return count


if __name__ == "__main__":
    main()
