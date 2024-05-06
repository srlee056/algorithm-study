import sys
from collections import defaultdict, deque


def main():

    n = int(sys.stdin.readline().strip())

    pinary_number_zero = [0 for _ in range(n + 1)]
    pinary_number_one = [0 for _ in range(n + 1)]

    pinary_number_one[1] = 1

    for i in range(2, n + 1):
        pinary_number_one[i] = pinary_number_zero[i - 1]
        pinary_number_zero[i] = pinary_number_zero[i - 1] + pinary_number_one[i - 1]

    # print(pinary_numbers[n])
    print(pinary_number_one[n] + pinary_number_zero[n])


if __name__ == "__main__":
    main()
