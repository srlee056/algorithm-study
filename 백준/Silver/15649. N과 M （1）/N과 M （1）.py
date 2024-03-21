import sys


def backtracking(n, m, backtrack_db):
    if m == 1:
        result = [[i] for i in range(1, n + 1)]
    else:
        result = []
        for i in range(1, n + 1):
            if (n, m - 1) in backtrack_db:
                temp = backtrack_db[(n, m - 1)]
            else:
                temp = backtracking(n, m - 1, backtrack_db)

            for ele in temp:
                # print(i, ele)
                if i not in ele:
                    result.append([i] + ele)
    backtrack_db[(n, m)] = result
    return result


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    backtrack_db = {}
    for arr in backtracking(n, m, backtrack_db):
        print(" ".join(map(str, arr)))


if __name__ == "__main__":
    main()
