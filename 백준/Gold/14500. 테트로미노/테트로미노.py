import sys
from collections import defaultdict


def main():
    n, m = map(int, sys.stdin.readline().split())

    arr = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        arr.append(row)

    max_sum = 0
    for i in range(n):
        for j in range(m):
            # print(i, j)
            sums = [max_sum]
            if i + 3 < n:
                sums.append(sum([arr[i + k][j] for k in range(4)]))
            if i + 2 < n and j + 1 < m:
                l1, l2 = [arr[i + k][j] for k in range(3)], [
                    arr[i + k][j + 1] for k in range(3)
                ]
                # print(l1)
                # print(l2)
                sums.append(max(sum(l1) + max(l2), max(l1) + sum(l2)))
                sums.append(max(sum(l1[:-1]) + sum(l2[1:]), sum(l1[1:]) + sum(l2[:-1])))
            if i + 1 < n and j + 1 < m:
                sums.append(
                    arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
                )
            if i + 1 < n and j + 2 < m:
                # print(arr[i][j : j + 2])
                # print(arr[i + 1][j : j + 2])

                sums.append(
                    max(
                        sum(arr[i][j : j + 3]) + max(arr[i + 1][j : j + 3]),
                        max(arr[i][j : j + 3]) + sum(arr[i + 1][j : j + 3]),
                        sum(arr[i][j : j + 2]) + sum(arr[i + 1][j + 1 : j + 3]),
                        sum(arr[i][j + 1 : j + 3]) + sum(arr[i + 1][j : j + 2]),
                    )
                )
            if j + 3 < m:
                sums.append(sum(arr[i][j : j + 4]))
            max_sum = max(sums)
            # print(sums)
    print(max_sum)


if __name__ == "__main__":
    main()
