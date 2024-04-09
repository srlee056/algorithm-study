import sys
from collections import defaultdict


def main():
    n, m = map(int, sys.stdin.readline().split())
    result = de_desc(1, n, m)
    # print(result)
    for ele in result:
        print(" ".join(map(str, ele)))


def de_desc(start, end, count):
    if count == 0:
        return [[]]
    result = []
    for num in range(start, end + 1):
        temp = [[num] + ele for ele in de_desc(num, end, count - 1)]
        result += temp
    return result


if __name__ == "__main__":
    main()
