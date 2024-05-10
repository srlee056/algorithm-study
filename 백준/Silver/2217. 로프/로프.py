import sys


def main():
    n = int(sys.stdin.readline().strip())

    lopes = []
    for _ in range(n):
        lopes.append(int(sys.stdin.readline().strip()))

    lopes.sort()

    max_weight = 0
    for i in range(n):
        max_weight = max(max_weight, (n - i) * lopes[i])

    print(max_weight)


if __name__ == "__main__":
    main()
