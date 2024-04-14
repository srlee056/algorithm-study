import sys
from collections import defaultdict, deque


def main():
    n = int(sys.stdin.readline().strip())

    prev_row = [(0, 0), (0, 0), (0, 0)]
    for _ in range(n):

        cur_row = list(map(int, sys.stdin.readline().split()))

        temp_row = []
        temp_row.append(
            (
                cur_row[0] + max(prev_row[0:2], key=lambda x: x[0])[0],
                cur_row[0] + min(prev_row[0:2], key=lambda x: x[1])[1],
            )
        )
        temp_row.append(
            (
                cur_row[1] + max(prev_row, key=lambda x: x[0])[0],
                cur_row[1] + min(prev_row, key=lambda x: x[1])[1],
            )
        )
        temp_row.append(
            (
                cur_row[2] + max(prev_row[1:], key=lambda x: x[0])[0],
                cur_row[2] + min(prev_row[1:], key=lambda x: x[1])[1],
            )
        )
        prev_row = temp_row
    print(max(prev_row, key=lambda x: x[0])[0], min(prev_row, key=lambda x: x[1])[1])


if __name__ == "__main__":
    main()
