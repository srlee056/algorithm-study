import sys


def main():
    n = int(sys.stdin.readline())

    counts = {1: 1, 2: 2}

    for i in range(3, n + 1):
        counts[i] = (counts[i - 1] + counts[i - 2]) % 10007

    print(counts[n])


if __name__ == "__main__":
    main()
