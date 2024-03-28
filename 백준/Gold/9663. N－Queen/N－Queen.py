import sys

#
def backtrack(n, col, rows, diagonals):
    if n == 1 and col == 0:
        return 1
    if col >= n:
        return 1
    result = 0
    for row in range(n):

        if rows[row] and diagonals[0][col + row] and diagonals[1][col - row + (n - 1)]:
            rows[row] = False
            diagonals[0][col + row] = False
            diagonals[1][col - row + (n - 1)] = False
        else:
            continue

        case = backtrack(n, col + 1, rows, diagonals)

        rows[row] = True
        diagonals[0][col + row] = True
        diagonals[1][col - row + (n - 1)] = True
        # print(case)
        if case > 0:
            result += case

    return result


def main():
    input = sys.stdin.readline

    n = int(input().strip())

    rows = [True for _ in range(n)]
    diagonals = [[True for _ in range(2 * n - 1)] for _ in range(2)]
    sum_cases = backtrack(n, 0, rows, diagonals)
    print(sum_cases)


if __name__ == "__main__":
    main()
