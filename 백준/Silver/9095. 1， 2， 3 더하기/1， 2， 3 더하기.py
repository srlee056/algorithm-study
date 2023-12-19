import sys


def main():
    test_cases = int(sys.stdin.readline())

    for _ in range(test_cases):
        num = int(sys.stdin.readline())

        counts = {1: 1, 2: 2, 3: 4}
        counts = counts_of_sum(counts, num)

        print(counts[num])


def counts_of_sum(counts, n):
    for i in range(4, n + 1):
        if i not in counts:
            counts[i] = counts[i - 1] + counts[i - 2] + counts[i - 3]

    return counts


if __name__ == "__main__":
    main()
