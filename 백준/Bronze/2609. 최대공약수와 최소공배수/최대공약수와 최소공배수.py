import sys


def main():
    a, b = map(int, sys.stdin.readline().split())

    n, m = max(a, b), min(a, b)
    while True:
        if m == 0 or n == m:
            gcd = n
            break
        else:
            n, m = m, n % m

    lcm = a * b // gcd

    print(gcd)
    print(lcm)


if __name__ == "__main__":
    main()
